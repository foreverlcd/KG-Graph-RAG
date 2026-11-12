"""Esquema plano y cerrado de extracción (lo que llena el LLM o un anotador humano).

El LLM no escribe CIDOC CRM ni IRIs: llena tres tipos de registro planos con listas cerradas,
cuyos valores admitidos se leen del tesauro SKOS (ontologia/tesauro.ttl). Un mapeo determinista
(src/laad/mapeo.py) los lleva al grafo. Ver docs/D_extraccion_consulta.md.

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
from rdflib.namespace import SKOS

from .fuente import verificar_cita, tramos

TESAURO = Path(__file__).resolve().parents[2] / "ontologia" / "tesauro.ttl"
BASE_TES = "https://w3id.org/laad/tesauro/"


@lru_cache(maxsize=1)
def _tesauro() -> rdflib.Graph:
    return rdflib.Graph().parse(TESAURO)


def conceptos(esquema: str) -> list[str]:
    """Nombres locales de los conceptos de un esquema (p. ej. 'actuaciones' -> ['peticion', ...])."""
    g = _tesauro()
    sch = rdflib.URIRef(BASE_TES + esquema)
    out = []
    for c in g.subjects(SKOS.inScheme, sch):
        out.append(str(c).rsplit("/", 1)[1])
    return sorted(out)


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

ID_PIEZA = r"^P\d{2}$"
ID_MENCION = r"^M-[A-Za-z0-9.]+-\d{3}$"
ID_AFIRMACION = r"^A-[A-Za-z0-9.]+-\d{3}$"
ID_HECHO = r"^H-[a-z0-9-]+$"


def _tramos_validos() -> set[str]:
    return {t.id for t in tramos()}


class _Base(BaseModel):
    model_config = ConfigDict(extra="forbid", use_enum_values=True, frozen=True)


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
            if self.valor.concepto not in admitidos:
                raise ValueError(f"{self.id}: {self.valor.concepto} no está en los esquemas admitidos por {self.atributo}")
        if self.segun and self.fundamento != "oidas":
            raise ValueError(f"{self.id}: 'segun' exige fundamento 'oidas'")
        if self.rol_en_hecho and self.rol_en_hecho not in _descendientes("roles", "participante-en-hecho"):
            raise ValueError(f"{self.id}: rol_en_hecho fuera de la rama participante-en-hecho")
        return self


class Reconstruccion(_Base):
    """Capa 4. Identidad (menciones → persona/grupo/lugar/cosa), hecho (hechos narrados → evento) o cargo
    (ejercicio de un cargo con vigencia), propuesta por un investigador con fecha, argumento y creencia.
    No la produce el LLM."""
    id: str = Field(pattern=r"^R-[a-z0-9-]+$")
    tipo: Literal["identidad", "hecho", "cargo"]
    etiqueta: str
    menciones: list[str] = Field(default_factory=list, description="identidad: ids de mención; hecho: ids de hecho narrado")
    # — solo para tipo "cargo" —
    titular: Optional[str] = Field(None, pattern=r"^R-[a-z0-9-]+$", description="Reconstrucción de identidad del titular")
    cargo: Optional[str] = Field(None, description="Concepto de tes:cargos")
    ambito: Optional[str] = Field(None, pattern=r"^R-[a-z0-9-]+$", description="Reconstrucción del grupo o lugar")
    ambito_literal: Optional[str] = None
    inicio: Optional[str] = Field(None, pattern=r"^\d{4}(-\d{2}(-\d{2})?)?$")
    fin: Optional[str] = Field(None, pattern=r"^\d{4}(-\d{2}(-\d{2})?)?$")
    vigencia_literal: Optional[str] = Field(None, description="Cómo se sabe la vigencia («consta en 1806», «no consta inicio»)")
    identificador_externo: Optional[str] = Field(None, description="p. ej. HGIS:6000357")
    premisas: list[str] = Field(default_factory=list, description="IDs de afirmaciones usadas como premisa")
    creencia: ValorCreencia
    argumento: str = Field(min_length=20)
    autor: str
    fecha: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$")
    externo: Optional[str] = Field(None, description="IRI externa (p. ej. ficha WHG de HGIS de las Indias)")

    @model_validator(mode="after")
    def _cargo(self):
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
def conceptos_admitidos(atributo: str) -> frozenset[str]:
    """Conceptos que un atributo admite como valor, según dct:conformsTo en el tesauro."""
    from rdflib.namespace import DCTERMS
    g = _tesauro()
    out: set[str] = set()
    for esq in g.objects(rdflib.URIRef(BASE_TES + "atributo/" + atributo), DCTERMS.conformsTo):
        out |= set(conceptos(str(esq).rsplit("/", 1)[1]))
    return frozenset(out)
