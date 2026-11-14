"""Esquema plano y cerrado de extracción (lo que llena el LLM o un anotador humano).

El LLM no escribe CIDOC CRM ni IRIs: llena tres tipos de registro planos con listas cerradas,
cuyos valores admitidos se leen del tesauro SKOS (ontologia/tesauro.ttl) y de sus conceptos CANDIDATOS
(ontologia/candidatos.ttl: lo que un anotador necesitó y el tesauro aún no tiene). Un concepto retirado
(owl:deprecated) no se admite. Un mapeo determinista (src/laad/mapeo.py) los lleva al grafo.
Qué puede ser sujeto y valor de cada atributo lo dice datos/atributos.csv (dominio y rango).
Ver docs/D_extraccion_consulta.md y ontologia/README.md.

Registros:
* Pieza      (capa 1) — unidad documental producida en una actuación. La cura un humano.
* Mencion    (capa 2) — una persona, grupo o lugar TAL COMO ESTÁ ESCRITO en un tramo. Sin fusionar.
* Afirmacion (capa 3) — quién afirma qué sobre qué, en qué pieza, con cita literal obligatoria.
La capa 4 (reconstrucción) no se extrae: la escribe el investigador (Reconstruccion).
"""
from __future__ import annotations

import re
from enum import Enum
from functools import lru_cache
from pathlib import Path
from typing import Literal, Optional

import rdflib
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from rdflib.namespace import DCTERMS, OWL, SKOS

from .fuente import verificar_cita, tramos

RAIZ = Path(__file__).resolve().parents[2]
TESAURO = RAIZ / "ontologia" / "tesauro.ttl"
CANDIDATOS = RAIZ / "ontologia" / "candidatos.ttl"     # generado por scripts/candidatos.py
ATRIBUTOS = RAIZ / "datos" / "atributos.csv"           # dominio y rango de cada atributo
BASE_TES = "https://w3id.org/laad/tesauro/"
COLECCION_CANDIDATOS = rdflib.URIRef(BASE_TES + "candidatos")


def grafo_tesauro() -> rdflib.Graph:
    """El vocabulario completo, recién leído: el tesauro y, si existe, sus conceptos candidatos."""
    g = rdflib.Graph().parse(TESAURO)
    if CANDIDATOS.exists():
        g.parse(CANDIDATOS)
    return g


@lru_cache(maxsize=1)
def _tesauro() -> rdflib.Graph:
    return grafo_tesauro()


def grafo_tesauro_en_cache() -> rdflib.Graph:
    """El vocabulario con el que se cargó el esquema (objeto compartido: NO modificarlo)."""
    return _tesauro()


def _local(iri) -> str:
    return str(iri).rsplit("/", 1)[1]


def _retirado(g: rdflib.Graph, c) -> bool:
    return any(bool(o) for o in g.objects(c, OWL.deprecated))


def conceptos(esquema: str) -> list[str]:
    """Nombres locales de los conceptos VIGENTES de un esquema (p. ej. 'actuaciones' -> ['peticion', ...]):
    los del tesauro y los candidatos pendientes; nunca los retirados (owl:deprecated)."""
    g = _tesauro()
    sch = rdflib.URIRef(BASE_TES + esquema)
    return sorted(_local(c) for c in g.subjects(SKOS.inScheme, sch) if not _retirado(g, c))


def retirados(esquema: str) -> dict[str, Optional[str]]:
    """Conceptos retirados de un esquema (candidatos rechazados o conceptos dados de baja) → concepto que los
    reemplaza (dct:isReplacedBy), o None. Su IRI existe, pero un registro no puede usarlos."""
    g = _tesauro()
    out: dict[str, Optional[str]] = {}
    for c in g.subjects(SKOS.inScheme, rdflib.URIRef(BASE_TES + esquema)):
        if _retirado(g, c):
            r = g.value(c, DCTERMS.isReplacedBy)
            out[_local(c)] = _local(r) if r is not None else None
    return out


def candidatos(esquema: str) -> frozenset[str]:
    """Conceptos candidatos (pendientes de revisión) de un esquema: se pueden usar, y la validación lo avisa."""
    g = _tesauro()
    sch = rdflib.URIRef(BASE_TES + esquema)
    return frozenset(_local(c) for c in g.objects(COLECCION_CANDIDATOS, SKOS.member) if (c, SKOS.inScheme, sch) in g)


def error_si_retirado(esquema: str, local: Optional[str], donde: str = "") -> None:
    """ValueError claro si `local` es un concepto retirado de tes:`esquema` (dice cuál usar en su lugar)."""
    ret = retirados(esquema)
    if local in ret:
        raise ValueError(f"{donde}{local!r} es un concepto RETIRADO de tes:{esquema} (owl:deprecated)"
                         + (f"; use {ret[local]!r}" if ret[local] else "; no tiene reemplazo")
                         + " — ontologia/README.md")


def _enum(nombre: str, esquema: str) -> type[Enum]:
    return Enum(nombre, {re.sub(r"\W", "_", c): c for c in conceptos(esquema)}, type=str)


TipoActuacion = _enum("TipoActuacion", "actuaciones")
Rol = _enum("Rol", "roles")
Atributo = _enum("Atributo", "atributos")
Fundamento = _enum("Fundamento", "fundamentos")
Polaridad = _enum("Polaridad", "polaridades")
Cargo = _enum("Cargo", "cargos")
Condicion = _enum("Condicion", "condiciones")
TipoEntidad = _enum("TipoEntidad", "entidades")
ValorCreencia = _enum("ValorCreencia", "creencias")

ID_PIEZA = r"^P\d{2,3}$"
ID_MENCION = r"^M-[A-Za-z0-9.]+-\d{3}$"
ID_AFIRMACION = r"^A-[A-Za-z0-9.]+-\d{3}$"
ID_HECHO = r"^H-[a-z0-9-]+$"
ID_EXPEDIENTE = r"[a-z0-9]+(?:-[a-z0-9]+)*"
# La capa 4 es común a todos los expedientes: sus referencias a menciones, hechos narrados y afirmaciones van
# CALIFICADAS con el expediente («cc-14-18:M-UT01-003»), porque los ids de registro solo son únicos dentro de uno.
_REF = re.compile(rf"^({ID_EXPEDIENTE}):(.+)$")
_ID_LOCAL = {"mencion": ID_MENCION, "hecho": ID_HECHO, "afirmacion": ID_AFIRMACION}


def separar_ref(ref: str, *clases: str) -> tuple[str, str, str]:
    """«cc-14-18:M-UT01-003» → ("cc-14-18", "M-UT01-003", "mencion"). `clases` restringe lo admitido
    ("mencion", "hecho", "afirmacion"). Una referencia sin calificar o mal formada es un error."""
    m = _REF.match(ref)
    if not m:
        raise ValueError(f"referencia sin calificar: {ref!r}; en la capa 4 se escribe «expediente:id» "
                         f"(p. ej. «cc-14-18:{ref}»)")
    exp, local = m.groups()
    for clase in clases or tuple(_ID_LOCAL):
        if re.match(_ID_LOCAL[clase], local):
            return exp, local, clase
    raise ValueError(f"referencia mal formada: {ref!r}; tras el expediente se espera un id de "
                     f"{' o '.join(clases or tuple(_ID_LOCAL))}")


def _tramos_validos() -> set[str]:
    return {t.id for t in tramos()}


# Campo de un registro → esquema del tesauro del que toma su valor.
CAMPOS_DE_CONCEPTO = {"tipo_actuacion": "actuaciones", "rol_en_pieza": "roles", "tipo_entidad": "entidades",
                      "rol_afirmante": "roles", "atributo": "atributos", "rol_en_hecho": "roles",
                      "polaridad": "polaridades", "fundamento": "fundamentos", "cargo": "cargos",
                      "creencia": "creencias"}


class _Base(BaseModel):
    model_config = ConfigDict(extra="forbid", use_enum_values=True, frozen=True)

    @model_validator(mode="before")
    @classmethod
    def _sin_conceptos_retirados(cls, datos):
        """Un concepto retirado no está en la lista cerrada; aquí se dice por qué y cuál lo reemplaza."""
        if isinstance(datos, dict):
            for campo, esquema in CAMPOS_DE_CONCEPTO.items():
                if campo in cls.model_fields and isinstance(datos.get(campo), str):
                    error_si_retirado(esquema, datos[campo], f"{datos.get('id', '?')}: {campo} = ")
        return datos

    def conceptos_usados(self) -> list[tuple[str, str]]:
        """(esquema, concepto) de cada concepto del tesauro que el registro usa."""
        return [(esq, v) for campo, esq in CAMPOS_DE_CONCEPTO.items()
                if campo in type(self).model_fields and (v := getattr(self, campo))]

    def candidatos_usados(self) -> list[tuple[str, str]]:
        """Los conceptos usados que aún son candidatos (motivo de aviso, no de error)."""
        return [(esq, c) for esq, c in self.conceptos_usados() if c in candidatos(esq)]


class Pieza(_Base):
    """Capa 1. Pieza documental: lo produce una actuación; ocupa uno o varios tramos."""
    id: str = Field(pattern=ID_PIEZA)
    orden: int = Field(ge=0, description="Orden físico en el expediente (según la transcripción)")
    tramos: list[str] = Field(min_length=1)
    tipo_actuacion: TipoActuacion
    titulo: str = Field(min_length=3, description="Descripción breve del archivista/modelador")
    fecha_escrita: Optional[str] = Field(None, description="Fecha tal como está escrita (cita literal)")
    lugar_escrito: Optional[str] = Field(None, description="Lugar de data tal como está escrito (cita literal)")
    cita_inicio: str = Field(min_length=8, description="Primeras palabras literales de la pieza")
    ajena_al_expediente: bool = False

    @field_validator("tramos")
    @classmethod
    def _tramos_existen(cls, v):
        malos = set(v) - _tramos_validos()
        if malos:
            raise ValueError(f"tramos inexistentes: {sorted(malos)}")
        return v

    @model_validator(mode="after")
    def _citas_literales(self):
        for campo in ("cita_inicio", "fecha_escrita", "lugar_escrito"):
            val = getattr(self, campo)
            if val and not any(verificar_cita(val, t).valida for t in self.tramos):
                raise ValueError(f"{campo} no es literal en {self.tramos}: {val!r}")
        return self


class Mencion(_Base):
    """Capa 2. Una aparición escrita de una persona, grupo o lugar. Nunca se fusiona aquí."""
    id: str = Field(pattern=ID_MENCION)
    tramo: str
    pieza: str = Field(pattern=ID_PIEZA)
    clase: Literal["persona", "grupo", "lugar", "cosa"] = Field(description="cosa: bien, tierra, dinero, documento "
                                                                "mencionado como objeto (pleitos civiles, inventarios)")
    texto: str = Field(min_length=2, description="Nombre exactamente como está escrito")
    rol_en_pieza: Optional[Rol] = Field(None, description="Rol de la persona en la actuación, si lo tiene "
                                        "(firmante, afirmante, receptor...). None si solo se la nombra.")
    tipo_entidad: Optional[TipoEntidad] = Field(None, description="Para grupos y lugares: ayllu, pueblo, cárcel…")
    cita: str = Field(min_length=8, description="Contexto literal que contiene la mención")

    @model_validator(mode="after")
    def _literal(self):
        if self.texto not in self.cita:
            raise ValueError(f"la mención {self.texto!r} no está dentro de su cita")
        r = verificar_cita(self.cita, self.tramo)
        if not r.valida:
            raise ValueError(f"{self.id}: {r.motivo}")
        return self


class Valor(_Base):
    """Valor de una afirmación: exactamente uno de los campos de referencia, más el texto literal."""
    concepto: Optional[str] = Field(None, description="Concepto del tesauro (cargo, condición) — nombre local")
    mencion: Optional[str] = Field(None, pattern=ID_MENCION)
    pieza: Optional[str] = Field(None, pattern=ID_PIEZA)
    hecho: Optional[str] = Field(None, pattern=ID_HECHO)
    literal: Optional[str] = Field(None, description="Valor tal como se escribe (hora, cantidad, calificativo)")

    @model_validator(mode="after")
    def _uno(self):
        refs = [x for x in (self.concepto, self.mencion, self.pieza, self.hecho) if x]
        if len(refs) > 1:
            raise ValueError("un valor referencia como máximo una entidad")
        if not refs and not self.literal:
            raise ValueError("valor vacío")
        return self


class Sujeto(_Base):
    mencion: Optional[str] = Field(None, pattern=ID_MENCION)
    pieza: Optional[str] = Field(None, pattern=ID_PIEZA)
    hecho: Optional[str] = Field(None, pattern=ID_HECHO, description="Hecho narrado EN ESTA PIEZA (p. ej. "
                                 "H-p01-alboroto). Que dos piezas narren el mismo hecho es una reconstrucción (capa 4).")
    eliptico: bool = Field(False, description="True si el sujeto no está escrito en la cita y lo resolvió el anotador "
                           "(p. ej. sujeto omitido que remite a una pieza anterior). Debe explicarse en 'nota'.")

    @model_validator(mode="after")
    def _uno(self):
        if sum(x is not None for x in (self.mencion, self.pieza, self.hecho)) != 1:
            raise ValueError("el sujeto debe ser exactamente una mención, una pieza o un hecho")
        return self


class Afirmacion(_Base):
    """Capa 3. Registro de afirmación. Toda afirmación tiene afirmante, pieza y cita literal."""
    id: str = Field(pattern=ID_AFIRMACION)
    tramo: str
    pieza: str = Field(pattern=ID_PIEZA)
    afirmante: str = Field(pattern=ID_MENCION, description="Mención de quien afirma")
    rol_afirmante: Rol
    sujeto: Sujeto
    atributo: Atributo
    valor: Valor
    rol_en_hecho: Optional[Rol] = Field(None, description="Solo para atributo participa-en-hecho")
    polaridad: Polaridad = "afirma"
    fundamento: Fundamento = "no-indica"
    cita: str = Field(min_length=8, description="Cita literal obligatoria que contiene la afirmación")
    responde_a: Optional[str] = Field(None, pattern=ID_AFIRMACION, description="Afirmación anterior que esta niega, "
                                      "corrige o matiza (p. ej. la declaración que rectifica la certificación)")
    segun: Optional[str] = Field(None, pattern=ID_MENCION, description="Discurso referido: mención de la persona a "
                                 "quien el afirmante atribuye el contenido («porque se lo dijo X»)")
    afirmante_de_otra_pieza: bool = Field(False, description="La pieza no nombra al afirmante; se usa una mención de "
                                          "otra pieza (exige nota)")
    distribuida: bool = Field(False, description="Enunciado colectivo repartido en un registro por objeto (exige nota)")
    nota: Optional[str] = None

    @model_validator(mode="after")
    def _coherencia(self):
        r = verificar_cita(self.cita, self.tramo)
        if not r.valida:
            raise ValueError(f"{self.id}: {r.motivo}")
        if self.rol_afirmante not in _descendientes("roles", "afirmante"):
            raise ValueError(f"{self.id}: rol_afirmante debe ser rol:afirmante o un hijo suyo")
        if self.atributo == "participa-en-hecho" and not self.rol_en_hecho:
            raise ValueError(f"{self.id}: participa-en-hecho exige rol_en_hecho")
        if (self.sujeto.eliptico or self.afirmante_de_otra_pieza or self.distribuida) and not self.nota:
            raise ValueError(f"{self.id}: una decisión del anotador (elíptico, afirmante de otra pieza, "
                             "afirmación distribuida) exige nota que la justifique")
        if self.valor.concepto:
            admitidos = conceptos_admitidos(self.atributo)
            if not admitidos:
                raise ValueError(f"{self.id}: el atributo {self.atributo} no admite valor de concepto (dct:conformsTo)")
            for esq in esquemas_admitidos(self.atributo):
                error_si_retirado(esq, self.valor.concepto, f"{self.id}: valor = ")
            if self.valor.concepto not in admitidos:
                raise ValueError(f"{self.id}: {self.valor.concepto} no está en los esquemas admitidos por {self.atributo}")
        # Dominio y rango (datos/atributos.csv). La clase exacta de una mención solo se conoce con el lote
        # (registros._integridad); aquí se descarta lo que ya es imposible con el registro solo.
        error = error_dominio_rango(self.atributo, tipos_de(self.sujeto), tipos_de(self.valor, valor=True))
        if error:
            raise ValueError(f"{self.id}: {error}")
        if self.segun and self.fundamento != "oidas":
            raise ValueError(f"{self.id}: 'segun' exige fundamento 'oidas'")
        if self.rol_en_hecho and self.rol_en_hecho not in _descendientes("roles", "participante-en-hecho"):
            raise ValueError(f"{self.id}: rol_en_hecho fuera de la rama participante-en-hecho")
        return self

    def conceptos_usados(self) -> list[tuple[str, str]]:
        """Los de sus campos y, además, el concepto que lleva como valor (cargo, condición)."""
        out = super().conceptos_usados()
        if self.valor.concepto:
            out += [(esq, self.valor.concepto) for esq in esquemas_admitidos(self.atributo)
                    if self.valor.concepto in conceptos(esq)]
        return out


class Reconstruccion(_Base):
    """Capa 4. Identidad (menciones → persona/grupo/lugar/cosa), hecho (hechos narrados → evento) o cargo
    (ejercicio de un cargo con vigencia), propuesta con autor, fecha, argumento y creencia. En el piloto las
    propone el modelo de lenguaje (autor «claude-opus-5-5») y las revisó una auditoría de un segundo modelo
    (docs/anexos/I_auditoria_reconstrucciones.md); ningún especialista humano las ha validado."""
    id: str = Field(pattern=r"^R-[a-z0-9-]+$")
    tipo: Literal["identidad", "hecho", "cargo"]
    etiqueta: str
    menciones: list[str] = Field(default_factory=list, description="identidad: ids de mención; hecho: ids de hecho "
                                 "narrado. Siempre calificados con el expediente («cc-14-18:M-UT01-003», "
                                 "«cc-14-18:H-p01-prision»); pueden mezclar expedientes")
    # — solo para tipo "cargo" —
    titular: Optional[str] = Field(None, pattern=r"^R-[a-z0-9-]+$", description="Reconstrucción de identidad del titular")
    cargo: Optional[str] = Field(None, description="Concepto de tes:cargos")
    ambito: Optional[str] = Field(None, pattern=r"^R-[a-z0-9-]+$", description="Reconstrucción del grupo o lugar")
    ambito_literal: Optional[str] = None
    inicio: Optional[str] = Field(None, pattern=r"^\d{4}(-\d{2}(-\d{2})?)?$")
    fin: Optional[str] = Field(None, pattern=r"^\d{4}(-\d{2}(-\d{2})?)?$")
    vigencia_literal: Optional[str] = Field(None, description="Cómo se sabe la vigencia («consta en 1806», «no consta inicio»)")
    identificador_externo: Optional[str] = Field(None, description="p. ej. HGIS:6000357")
    premisas: list[str] = Field(default_factory=list, description="Afirmaciones usadas como premisa, calificadas "
                                "con el expediente («cc-14-18:A-UT11-004»)")
    creencia: ValorCreencia
    argumento: str = Field(min_length=20)
    autor: str
    fecha: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$")
    externo: Optional[str] = Field(None, description="IRI externa (p. ej. ficha WHG de HGIS de las Indias)")
    ver_tambien: list[str] = Field(default_factory=list, description="Otras IRIs de autoridad (Wikidata, TGN); se añaden como identificadores y rdfs:seeAlso, nunca owl:sameAs")

    @model_validator(mode="after")
    def _cargo(self):
        try:
            for ref in self.menciones:
                separar_ref(ref, "hecho" if self.tipo == "hecho" else "mencion")
            for ref in self.premisas:
                separar_ref(ref, "afirmacion")
        except ValueError as e:
            raise ValueError(f"{self.id}: {e}") from None
        if self.tipo == "cargo":
            if not (self.titular and self.cargo and self.premisas):
                raise ValueError(f"{self.id}: un cargo exige titular, cargo y al menos una premisa")
            if self.cargo not in set(conceptos("cargos")):
                raise ValueError(f"{self.id}: cargo fuera de tes:cargos: {self.cargo}")
        elif not self.menciones:
            raise ValueError(f"{self.id}: identidad y hecho exigen menciones")
        return self


@lru_cache(maxsize=None)
def _descendientes_cache(esquema: str, raiz: str) -> frozenset[str]:
    g = _tesauro()
    base = BASE_TES + esquema.rstrip("s").replace("role", "rol") + "/"
    raiz_iri = rdflib.URIRef(BASE_TES + {"roles": "rol"}.get(esquema, esquema) + "/" + raiz)
    out = {raiz}
    frontera = [raiz_iri]
    while frontera:
        n = frontera.pop()
        for h in g.subjects(SKOS.broader, n):
            out.add(str(h).rsplit("/", 1)[1])
            frontera.append(h)
    return frozenset(out)


def _descendientes(esquema: str, raiz: str) -> frozenset[str]:
    return _descendientes_cache(esquema, raiz)


@lru_cache(maxsize=None)
def esquemas_admitidos(atributo: str) -> tuple[str, ...]:
    """Esquemas de los que un atributo toma su valor de concepto (dct:conformsTo en el tesauro)."""
    g = _tesauro()
    return tuple(sorted(_local(esq) for esq in g.objects(rdflib.URIRef(BASE_TES + "atributo/" + atributo),
                                                         DCTERMS.conformsTo)))


@lru_cache(maxsize=None)
def conceptos_admitidos(atributo: str) -> frozenset[str]:
    """Conceptos vigentes que un atributo admite como valor, según dct:conformsTo en el tesauro."""
    out: set[str] = set()
    for esq in esquemas_admitidos(atributo):
        out |= set(conceptos(esq))
    return frozenset(out)


# ───────────────────────── dominio y rango de los atributos ─────────────────────────
# Tipos de lo que puede ser sujeto o valor de una afirmación. Los cuatro primeros son las clases de mención.
TIPOS_MENCION = ("persona", "grupo", "lugar", "cosa")
TIPOS_SUJETO = TIPOS_MENCION + ("pieza", "hecho", "afirmacion")
TIPOS_VALOR = TIPOS_SUJETO + ("concepto", "literal")


def leer_dominio_rango(ruta: Path) -> dict[str, tuple[frozenset[str], frozenset[str]]]:
    """datos/atributos.csv → atributo → (tipos admitidos como sujeto, tipos admitidos como valor)."""
    import csv
    out: dict[str, tuple[frozenset[str], frozenset[str]]] = {}
    with open(ruta, encoding="utf-8", newline="") as f:
        for n, fila in enumerate(csv.DictReader(f), 2):
            atr = fila["atributo"].strip()
            suj = frozenset(x.strip() for x in fila["sujeto"].split("|") if x.strip())
            val = frozenset(x.strip() for x in fila["valor"].split("|") if x.strip())
            if atr in out:
                raise ValueError(f"{ruta.name}:{n} atributo repetido: {atr}")
            if not suj or suj - set(TIPOS_SUJETO):
                raise ValueError(f"{ruta.name}:{n} {atr}: sujeto {sorted(suj)}; se admite {TIPOS_SUJETO}")
            if not val or val - set(TIPOS_VALOR):
                raise ValueError(f"{ruta.name}:{n} {atr}: valor {sorted(val)}; se admite {TIPOS_VALOR}")
            out[atr] = (suj, val)
    return out


@lru_cache(maxsize=1)
def dominio_rango() -> dict[str, tuple[frozenset[str], frozenset[str]]]:
    return leer_dominio_rango(ATRIBUTOS)


def tipos_de(campo, clase_mencion: Optional[str] = None, valor: bool = False) -> frozenset[str]:
    """Tipos posibles de un Sujeto o un Valor. De una mención, sin saber su clase, puede ser cualquiera de las
    cuatro; con `clase_mencion`, exactamente esa. Un valor con referencia y literal es la referencia (el literal
    queda como nota en el grafo)."""
    if valor and campo.concepto:
        return frozenset({"concepto"})
    if campo.mencion:
        return frozenset({clase_mencion}) if clase_mencion else frozenset(TIPOS_MENCION)
    if campo.pieza:
        return frozenset({"pieza"})
    if campo.hecho:
        return frozenset({"hecho"})
    return frozenset({"literal"})


def _lista(tipos) -> str:
    orden = {t: i for i, t in enumerate(TIPOS_VALOR)}
    return ", ".join(sorted(tipos, key=orden.get))


def error_dominio_rango(atributo: str, sujeto: frozenset[str], valor: frozenset[str]) -> Optional[str]:
    """Mensaje de error si el sujeto o el valor no son de un tipo admitido por el atributo (datos/atributos.csv);
    None si lo son o si el atributo no tiene fila (eso lo trata registros._integridad)."""
    dr = dominio_rango().get(atributo)
    if dr is None:
        return None
    admite_sujeto, admite_valor = dr
    if not sujeto & admite_sujeto:
        return (f"el atributo {atributo} no admite como sujeto {_lista(sujeto)}; admite: {_lista(admite_sujeto)} "
                f"(datos/atributos.csv)")
    if not valor & admite_valor:
        return (f"el atributo {atributo} no admite como valor {_lista(valor)}; admite: {_lista(admite_valor)} "
                f"(datos/atributos.csv)")
    return None
