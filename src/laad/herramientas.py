"""Núcleo del harness de consulta: las herramientas con que un agente (un LLM, o una persona desde
scripts/preguntar.py) responde preguntas libres sobre el grafo (docs/D_extraccion_consulta.md §4).

Reglas que este módulo hace cumplir:
* El agente no escribe SPARQL: cada herramienta envuelve consultas con nombre de consultas/ (laad.consulta.consultar).
* El agente no escribe IRIs: las entidades se nombran con ids de registro —«R-…» (reconstrucción, capa 4) o
  «<expediente>:M-…» (mención), «<expediente>:A-…» (afirmación), «<expediente>:P…» (pieza)— que se validan
  contra el grafo; un id mal escrito o inexistente es un ErrorHerramienta con un mensaje que dice cómo corregirlo.
* Para pasar de un nombre escrito por una persona a esos ids está buscar(): normaliza las variantes gráficas del
  corpus y compara con difflib contra las etiquetas de las reconstrucciones y el texto de las menciones. Devuelve
  TODOS los candidatos con su creencia, y para cada reconstrucción las rivales que comparten menciones con ella:
  nunca elige una hipótesis.
* Cada herramienta devuelve un Resultado: las filas (lo único que el agente puede citar) y un texto compuesto con
  laad.responder, que separa AFIRMACIÓN (capa 3: quién dijo qué, con cita, tramo, folio o «no consta», afirmante,
  rol y fuerza) de RECONSTRUCCIÓN (capa 4: hipótesis con autor y creencia).
* verificar() es la verificación posterior de §4.5: las citas entre comillas de una respuesta redactada deben ser
  subcadena de alguna fila devuelta, y los ids de afirmación citados deben estar en las filas.
"""
from __future__ import annotations

import difflib
import re
import unicodedata
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Callable

from . import consulta, fuente
from .consulta import consultar
from .responder import (NO_CONSTA, Respuesta, _unicas, forma_de, linea_reconstruccion, pronunciamientos,
                        resumen_disputa)


class ErrorHerramienta(ValueError):
    """Parámetro no válido. El mensaje está pensado para que el agente lo corrija en la llamada siguiente."""


# ───────────────────────── resultado ─────────────────────────

@dataclass
class Resultado:
    herramienta: str
    parametros: dict
    forma: str                 # forma CALCULADA de lo devuelto: D | A | DISPUTA | NC | R | P
    resumen: str
    filas: list[dict] = field(default_factory=list)
    texto: str = ""


def cabecera(nombre: str, params: dict) -> str:
    """«nombre(clave=valor; …)», sin comillas, para mostrar la llamada (scripts/preguntar.py). No forma parte del
    texto del resultado: ese texto solo contiene lo que respaldan sus filas (verificar())."""
    partes = [f"{k}={', '.join(map(str, v)) if isinstance(v, list) else v}" for k, v in params.items() if v is not None]
    return f"{nombre}({'; '.join(partes)})"


def _afirmaciones_agrupadas(filas: list[dict]) -> list[str]:
    """Las afirmaciones agrupadas por pieza y afirmante: la ficha de la pieza (fecha, ante, redacta, firma) y la del
    afirmante se escriben una vez por grupo, no en cada afirmación. Mismos datos que responder.linea_afirmacion con
    un tercio del texto: lo lee el modelo, y cada carácter se paga en tokens y en cuota."""
    grupos: dict[tuple, list[dict]] = {}
    for r in filas:
        clave = (r.get("pieza"), r.get("tipoAct"), r.get("fecha"), r.get("ante"), r.get("redactorDoc"),
                 r.get("redaccionDisputada"), r.get("firmantes"), r.get("afirmante"), r.get("rolAf"),
                 r.get("afirmanteR"))
        grupos.setdefault(clave, []).append(r)
    out = ["— Lo que se afirma en el expediente (capa 3) —"]
    for (pieza, tipo, fecha, ante, redacta, disputada, firma, af, rol, afr), rs in grupos.items():
        redacta = redacta or NO_CONSTA
        if disputada == "true":
            redacta += " (DISPUTADO: ver atributo «redactó la pieza»)"
        fecha = f"fecha escrita «{fecha}»" if fecha else "sin fecha escrita"
        out.append(f"PIEZA {pieza} ({tipo}), {fecha}; ante: {ante or NO_CONSTA}; redacta: {redacta}; "
                   f"firma la pieza: {firma or NO_CONSTA}")
        out.append(f"  Afirmante: «{af}» ({rol})" + (f" [= {afr}, según reconstrucción]" if afr else ""))
        for r in rs:
            pol = "" if r["pol"] == "afirma" else " [NIEGA]"
            eliptico = " (sujeto elíptico resuelto por el anotador)" if r.get("eliptico") == "true" else ""
            rel = (f"; responde a {r['respondeA']}" if r.get("respondeA") else "") + \
                  (f"; según lo que le dijo «{r['segun']}» (discurso referido)" if r.get("segun") else "")
            folio = r["folio"] if r.get("folio") else "folio no consta"
            out.append(f"  AFIRMACIÓN {r['aid']}{pol}: {r['atrLabel']} → {r['valorLabel']}{eliptico} «{r['cita']}» "
                       f"[{r['tramo']}, {folio}; fundamento: {r['fundamento']}; fuerza institucional: "
                       f"{r['fuerza']}{rel}]")
    return out + [""]


def _resultado(nombre: str, params: dict, forma: str, resumen: str, filas: list[dict], *,
               afirmaciones: list[dict] = (), reconstrucciones: list[dict] = (), extra: list[str] = ()) -> Resultado:
    texto = Respuesta(nombre, forma, resumen, [], list(reconstrucciones), list(extra)).texto()
    cabeza, resto = texto.split("\n", 2)[1], texto.split("\n", 2)[2]   # sin la línea «PREGUNTA: …»
    bloque = "\n".join(_afirmaciones_agrupadas(list(afirmaciones))) + "\n" if afirmaciones else ""
    texto = f"HERRAMIENTA: {nombre}\n{cabeza}\n\n{bloque}{resto.lstrip(chr(10))}".rstrip() + "\n"
    return Resultado(nombre, {k: v for k, v in params.items() if v is not None}, forma, resumen, filas, texto)


# ───────────────────────── normalización de nombres ─────────────────────────

_VACIAS = {"de", "del", "la", "las", "el", "los", "lo", "y", "e", "o", "u", "a", "al", "en", "ante", "con", "por",
           "para", "sobre", "contra", "entre", "sin", "tras", "don", "dona", "d", "senor", "senora", "su", "sus",
           "dicho", "dicha", "mi", "que"}


def normalizar(s: str) -> str:
    """Minúsculas, sin tildes ni signos, espacios simples: «Andrés  Chuquitapa,» → «andres chuquitapa»."""
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s).split())


def clave_grafica(palabra: str) -> str:
    """Clave de una palabra ya normalizada que iguala las variantes gráficas del corpus: qu/c/k, c/s/z ante e/i,
    hu/gu + vocal (Huancachoque, Guancachoque), h muda, b/v, y/i/ll, e/i y o/u (Choquetapa, Chuquitapa) y letras
    dobladas (Chuquiitapa). La «ch» se conserva. No decide nada: solo acerca grafías para difflib."""
    w = palabra.replace("ch", "\x01")
    w = re.sub(r"qu(?=[ei])", "k", w).replace("qu", "k").replace("q", "k")
    w = re.sub(r"c(?=[ei])", "s", w).replace("c", "k")
    w = re.sub(r"[gh]u(?=[aeio])", "w", w)
    w = w.replace("h", "").replace("ll", "i").replace("y", "i").replace("v", "b").replace("z", "s")
    w = w.replace("e", "i").replace("o", "u").replace("\x01", "ch")
    return re.sub(r"(.)\1+", r"\1", w)


def _claves(texto: str) -> tuple[str, ...]:
    return tuple(clave_grafica(p) for p in normalizar(texto).split() if p not in _VACIAS and len(p) > 1)


@lru_cache(maxsize=None)
def _trozos(texto: str) -> tuple[str, ...]:
    """Claves de las palabras de un texto y de sus uniones de dos y tres palabras seguidas («Guancacho que»)."""
    c = _claves(texto)
    return tuple(dict.fromkeys(c + tuple("".join(c[i:i + n]) for n in (2, 3) for i in range(len(c) - n + 1))))


UMBRAL = 0.8   # parecido mínimo (difflib) de CADA palabra del nombre buscado con alguna palabra del candidato


def _parecido(a: str, b: str) -> float:
    if 2 * min(len(a), len(b)) / (len(a) + len(b)) < UMBRAL:      # cota superior de ratio(): no hace falta calcularlo
        return 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def _puntuar(buscado: tuple[str, ...], texto: str) -> float:
    """Media del parecido de cada palabra buscada con su mejor trozo del texto; 0 si alguna no llega al UMBRAL."""
    trozos = _trozos(texto)
    if not trozos:
        return 0.0
    por_palabra = [max(_parecido(q, t) for t in trozos) for q in buscado]
    if min(por_palabra) < UMBRAL:
        junto = "".join(buscado)                    # «Guanca choque» escrito separado en la pregunta
        mejor = max(_parecido(junto, t) for t in trozos)
        return mejor if len(buscado) > 1 and mejor >= UMBRAL else 0.0
    return sum(por_palabra) / len(por_palabra)


def _global(buscado: tuple[str, ...], texto: str) -> float:
    """Parecido del nombre entero con el texto entero: desempata a favor de «Tinta (pueblo)» frente a una etiqueta
    larga que también contiene «Tinta»."""
    return difflib.SequenceMatcher(None, " ".join(buscado), " ".join(_claves(texto))).ratio()


# ───────────────────────── índices (de consultas con nombre) ─────────────────────────

def _ref_calificada(ref: str) -> str:
    """«cc-14-18/mencion/M-UT01-003» (forma de las consultas) → «cc-14-18:M-UT01-003» (forma del agente)."""
    partes = ref.split("/")
    return f"{partes[0]}:{partes[-1]}" if len(partes) == 3 else ref


CLASES = ("persona", "lugar", "grupo", "cosa", "hecho", "cargo")
_CLASE_IRI = {"hecho": "evento", "cargo": "ejercicio-cargo"}            # clase del agente → segmento de la IRI
_CLASE_AGENTE = {v: k for k, v in _CLASE_IRI.items()}
_CLASE_MENCION = {"persona": "persona", "lugar": "lugar", "grupo": "grupo o cosa", "cosa": "grupo o cosa"}


@lru_cache(maxsize=1)
def indice_reconstrucciones() -> dict[str, dict]:
    """id «R-…» → fila de consultas/indice_reconstrucciones.rq, con «deriva_de» (refs calificadas), «menciones»
    (solo las de capa 2 y los hechos) y «clase» en el vocabulario del agente."""
    out = {}
    for f in consultar("indice_reconstrucciones"):
        refs = [_ref_calificada(r) for r in (f["derivaDe"] or "").split()]
        out[f["rid"]] = {**f, "clase": _CLASE_AGENTE.get(f["clase"], f["clase"]), "deriva_de": refs,
                         "menciones": [r for r in refs if re.search(r":(M|H)-", r)]}
    return out


@lru_cache(maxsize=1)
def indice_menciones() -> dict[str, dict]:
    """«<exp>:M-…» → fila de consultas/indice_menciones.rq (texto literal, clase, pieza, tramo, cita y las
    reconstrucciones que la agrupan, como lista)."""
    return {f"{f['exp']}:{f['mid']}": {**f, "id": f"{f['exp']}:{f['mid']}",
                                       "reconstrucciones": (f["reconstrucciones"] or "").split()}
            for f in consultar("indice_menciones")}


def rivales(rid: str) -> list[dict]:
    """Otras reconstrucciones que derivan de alguna de las mismas menciones (o hechos) que `rid`: hipótesis
    rivales o solapadas. Se devuelven todas con su creencia; no se juzga cuál vale (ADR-044)."""
    idx = indice_reconstrucciones()
    propias = set(idx[rid]["menciones"])
    out = []
    for otro, r in idx.items():
        comunes = propias & set(r["menciones"])
        if otro != rid and comunes:
            out.append({"id": otro, "etiqueta": r["label"], "creencia": r["creencia"], "compartidas": len(comunes)})
    return sorted(out, key=lambda r: (-r["compartidas"], r["id"]))


# ───────────────────────── validación de parámetros ─────────────────────────

def _expediente_iri(exp: str | None):
    if exp is None:
        return None
    validos = fuente.expedientes()
    if exp not in validos:
        raise ErrorHerramienta(f"expediente desconocido: {exp!r}; los expedientes del corpus son: {', '.join(validos)}")
    return consulta.expediente(exp)


def _sugerir(valor: str, opciones) -> str:
    opciones = list(opciones)
    cerca = difflib.get_close_matches(valor, opciones, n=3, cutoff=0.6)
    cerca += [o for o in opciones if normalizar(valor) and normalizar(valor) in normalizar(o) and o not in cerca][:3]
    return f" ¿Quiso decir {' o '.join(cerca)}?" if cerca else ""


_REF = re.compile(r"^(?P<exp>[a-z0-9][a-z0-9-]*):(?P<local>(?:M|A|H)-[\w.-]+|P[\w.-]*)$")
_NOMBRE_CLASE = {"reconstruccion": "reconstrucción («R-…»)", "mencion": "mención", "afirmacion": "afirmación",
                 "pieza": "pieza", "hecho": "hecho"}
_NO_IRI = ("no se admiten IRIs ni nombres: use buscar(nombre) para obtener un id «R-…» (reconstrucción) o "
           "«<expediente>:M-…» (mención)")


def _separar(ref: str, admite: tuple[str, ...], parametro: str) -> tuple[str, str, str]:
    """Clasifica un id del agente: ("reconstruccion", "R-x", "") o (clase, local, exp) con clase mencion,
    afirmacion o pieza. Comprueba que exista."""
    if not isinstance(ref, str) or not ref.strip():
        raise ErrorHerramienta(f"{parametro}: falta el id")
    ref = ref.strip()
    if ref.startswith(("http://", "https://", "<")):
        raise ErrorHerramienta(f"{parametro}={ref!r}: {_NO_IRI}")
    if ref.startswith("R-"):
        if "reconstruccion" not in admite:
            raise ErrorHerramienta(f"{parametro}={ref!r}: aquí no se admite una reconstrucción; se espera "
                                   f"{' o '.join(_NOMBRE_CLASE[a] for a in admite)}")
        if ref not in indice_reconstrucciones():
            raise ErrorHerramienta(f"{parametro}: no existe la reconstrucción {ref!r}."
                                   + _sugerir(ref, indice_reconstrucciones()) + " Use buscar(nombre).")
        return "reconstruccion", ref, ""
    m = _REF.match(ref)
    if not m:
        if re.match(r"^(?:M|A|H)-|^P\d", ref):
            raise ErrorHerramienta(f"{parametro}={ref!r}: el id va calificado con su expediente, p. ej. "
                                   f"«{fuente.EXPEDIENTE_POR_DEFECTO}:{ref}»")
        raise ErrorHerramienta(f"{parametro}={ref!r}: {_NO_IRI}")
    exp, local = m["exp"], m["local"]
    _expediente_iri(exp)
    clase = {"M": "mencion", "A": "afirmacion", "H": "hecho", "P": "pieza"}[local[0]]
    if clase not in admite:
        raise ErrorHerramienta(f"{parametro}={ref!r}: aquí no se admite un id de {_NOMBRE_CLASE[clase]}; se espera "
                               f"{' o '.join(_NOMBRE_CLASE[a] for a in admite)}")
    existentes = {"mencion": lambda: {k.split(":", 1)[1] for k in indice_menciones() if k.startswith(exp + ":")},
                  "afirmacion": lambda: _ids_afirmaciones(exp),
                  "pieza": lambda: {f["pieza"] for f in consultar("piezas", expediente=consulta.expediente(exp))}}
    if clase in existentes and local not in (ids := existentes[clase]()):
        raise ErrorHerramienta(f"{parametro}: no existe la {_NOMBRE_CLASE[clase]} {local!r} en el expediente {exp}."
                               + _sugerir(local, ids))
    return clase, local, exp


def _ids_afirmaciones(exp: str) -> set[str]:
    return {f["aid"] for f in consultar("afirmaciones", expediente=consulta.expediente(exp))}


def _iri(clase: str, local: str, exp: str):
    if clase == "reconstruccion":
        return indice_reconstrucciones()[local]["entidad"]
    return {"mencion": consulta.mencion, "afirmacion": consulta.afirmacion, "pieza": consulta.pieza}[clase](exp, local)


@lru_cache(maxsize=None)
def vocabulario_de(esquema: str) -> tuple[dict, ...]:
    return tuple(consultar("vocabulario", esquema=consulta.TES + esquema))


def _concepto(valor: str, esquema: str, parametro: str) -> dict:
    """Concepto del tesauro por su nombre local («ejerce-cargo») o por su etiqueta («ejerce el cargo»)."""
    conceptos = vocabulario_de(esquema)
    for c in conceptos:
        if valor == c["local"] or normalizar(valor) == normalizar(c["etiqueta"]):
            return c
    raise ErrorHerramienta(f"{parametro}: {valor!r} no está en el vocabulario «{esquema}»."
                           + _sugerir(valor, [c["local"] for c in conceptos])
                           + f" La lista completa la da vocabulario(esquema={esquema}).")


def _validar(h: "Herramienta", params: dict) -> dict:
    """Comprueba los parámetros contra el JSON Schema de la herramienta (el subconjunto que usamos: object con
    properties de tipo string, integer o array de string, enum, required y sin propiedades adicionales). Un string
    suelto donde se espera una lista se acepta como lista de uno."""
    props, req = h.parametros["properties"], h.parametros.get("required", [])
    desconocidos = [k for k in params if k not in props]
    if desconocidos:
        raise ErrorHerramienta(f"{h.nombre}: parámetro desconocido {', '.join(desconocidos)}; admite: "
                               f"{', '.join(props) or 'ninguno'}")
    faltan = [k for k in req if params.get(k) in (None, "", [])]
    if faltan:
        raise ErrorHerramienta(f"{h.nombre}: falta el parámetro obligatorio {', '.join(faltan)}")
    out = {}
    for k, v in params.items():
        if v is None:
            continue
        esp = props[k]
        if esp["type"] == "array":
            v = [v] if isinstance(v, str) else v
            if not isinstance(v, list) or not all(isinstance(x, str) for x in v):
                raise ErrorHerramienta(f"{h.nombre}: {k} debe ser una lista de textos")
            if "enum" in esp.get("items", {}):
                malos = [x for x in v if x not in esp["items"]["enum"]]
                if malos:
                    raise ErrorHerramienta(f"{h.nombre}: {k} no admite {', '.join(malos)}; valores: "
                                           f"{', '.join(esp['items']['enum'])}")
        elif esp["type"] == "integer":
            if isinstance(v, str) and re.fullmatch(r"-?\d+", v):
                v = int(v)
            if not isinstance(v, int) or isinstance(v, bool):
                raise ErrorHerramienta(f"{h.nombre}: {k} debe ser un número entero")
        else:
            if not isinstance(v, str):
                raise ErrorHerramienta(f"{h.nombre}: {k} debe ser un texto")
            if "enum" in esp and v not in esp["enum"]:
                raise ErrorHerramienta(f"{h.nombre}: {k}={v!r} no es válido; valores: {', '.join(esp['enum'])}")
        out[k] = v
    return out


# ───────────────────────── herramientas ─────────────────────────

def buscar(nombre: str, clase: str | None = None, expediente: str | None = None, maximo: int = 20) -> Resultado:
    """Candidatos para un nombre escrito por una persona: reconstrucciones (capa 4) y menciones sueltas (capa 2, no
    agrupadas por ninguna reconstrucción). Insensible a mayúsculas y tildes y tolerante a las variantes gráficas
    (clave_grafica + difflib). Un nombre que no se parece a nada devuelve una lista vacía: no se inventa."""
    buscado = _claves(nombre or "")
    if not buscado:
        raise ErrorHerramienta(f"buscar: el nombre {nombre!r} no tiene ninguna palabra que buscar")
    if clase is not None and clase not in CLASES:
        raise ErrorHerramienta(f"buscar: clase={clase!r} no es válida; valores: {', '.join(CLASES)}")
    if expediente is not None:
        _expediente_iri(expediente)
    menciones = indice_menciones()
    candidatos = []
    for rid, r in indice_reconstrucciones().items():
        if clase and r["clase"] != clase:
            continue
        if expediente and not any(x.startswith(expediente + ":") for x in r["deriva_de"]):
            continue
        # La etiqueta, las palabras del id (R-alboroto-carcel: el nombre que le dio el investigador) y el texto
        # literal de cada mención que agrupa.
        textos = ([(r["label"], None), (rid[2:].replace("-", " "), None)]
                  + [(menciones[m]["texto"], m) for m in r["menciones"] if m in menciones])
        puntos = [(_puntuar(buscado, t), _global(buscado, t), t, m) for t, m in textos]
        puntos = [p for p in puntos if p[0] > 0]
        if not puntos:
            continue
        mejor = max(puntos, key=lambda p: (p[0], p[1]))
        candidatos.append({
            "candidato": "reconstrucción", "id": rid, "tipo": r["clase"], "etiqueta": r["label"],
            "creencia": r["creencia"], "n_menciones": len(r["menciones"]),
            "coincide_con": sorted({t for _, _, t, _ in puntos}),
            "menciones_coincidentes": sorted({m for *_, m in puntos if m}),
            "rivales": rivales(rid), "puntuacion": round(mejor[0], 3), "_orden": (mejor[0], mejor[1], len(r["menciones"])),
        })
    for mid, m in menciones.items():
        if m["reconstrucciones"]:
            continue                       # enlazada: ya sale dentro de su reconstrucción
        if clase and _CLASE_MENCION.get(clase) != m["clase"]:
            continue
        if expediente and m["exp"] != expediente:
            continue
        p = _puntuar(buscado, m["texto"])
        if p > 0:
            candidatos.append({"candidato": "mención suelta", "id": mid, "tipo": m["clase"], "texto": m["texto"],
                               "pieza": m["pieza"], "tramo": m["tramo"], "cita": m["cita"], "puntuacion": round(p, 3),
                               "_orden": (p, _global(buscado, m["texto"]), 0)})
    candidatos.sort(key=lambda c: (c["_orden"][0], c["_orden"][1], c["_orden"][2]), reverse=True)
    omitidos = max(0, len(candidatos) - maximo)
    filas = [{k: v for k, v in c.items() if k != "_orden"} for c in candidatos[:maximo]]
    lineas = []
    for c in filas:
        if c["candidato"] == "reconstrucción":
            lineas.append(f"  RECONSTRUCCIÓN {c['id']} [{c['tipo']}] «{c['etiqueta']}» — creencia: {c['creencia']}; "
                          f"{c['n_menciones']} menciones o hechos; coincide con: "
                          + ", ".join(f"«{t}»" for t in c["coincide_con"]))
            for rv in c["rivales"]:
                lineas.append(f"      comparte {rv['compartidas']} con {rv['id']} «{rv['etiqueta']}» "
                              f"(creencia: {rv['creencia']})")
        else:
            lineas.append(f"  MENCIÓN SUELTA {c['id']} [{c['tipo']}] «{c['texto']}» — pieza {c['pieza']}, "
                          f"{c['tramo']}: «{c['cita']}»")
    n_rec = sum(c["candidato"] == "reconstrucción" for c in filas)
    resumen = (f"{n_rec} reconstrucciones y {len(filas) - n_rec} menciones sueltas candidatas"
               + (f" (y {omitidos} más, omitidas)" if omitidos else "")
               + ". Son candidatos: el buscador no elige entre hipótesis rivales." if filas
               else "Ningún candidato: el nombre no se parece a ninguna etiqueta ni a ninguna mención del grafo.")
    return _resultado("buscar", {"nombre": nombre, "clase": clase, "expediente": expediente}, "D" if filas else "NC",
                      resumen, filas, extra=lineas)


def _normal_en(buscados: list[str], *textos: str | None) -> bool:
    ts = [normalizar(t) for t in textos if t]
    return any(normalizar(b) in t or normalizar(b) == t for b in buscados for t in ts)


def afirmaciones(entidad: str | None = None, atributo: str | None = None, afirmante: str | None = None,
                 pieza: str | None = None, valor: list[str] | None = None, fuerza: list[str] | None = None,
                 fundamento: list[str] | None = None, excluir_fundamento: list[str] | None = None,
                 responden_a: list[str] | None = None, expediente: str | None = None) -> Resultado:
    """Afirmaciones de capa 3 (consultas/afirmaciones.rq) con filtros. Si se fijan entidad y atributo, la forma es
    la calculada (A, DISPUTA o NC) y el resumen dice quién afirma y quién niega cada valor."""
    params = {}
    if entidad:
        clase, local, exp = _separar(entidad, ("reconstruccion", "mencion", "pieza"), "entidad")
        params["filtroEntidad" if clase == "reconstruccion" else "sujeto"] = _iri(clase, local, exp)
    if afirmante:
        clase, local, exp = _separar(afirmante, ("reconstruccion", "mencion"), "afirmante")
        params["filtroAfirmante" if clase == "reconstruccion" else "af"] = _iri(clase, local, exp)
    if pieza:
        params["pieza_iri"] = _iri(*_separar(pieza, ("pieza",), "pieza"))
    if atributo:
        params["atributo"] = _concepto(atributo, "atributos", "atributo")["concepto"]
    if expediente:
        params["expediente"] = _expediente_iri(expediente)
    fuerzas = [_concepto(x, "fuerzas", "fuerza")["etiqueta"] for x in fuerza or []]
    fundamentos = [_concepto(x, "fundamentos", "fundamento")["etiqueta"] for x in fundamento or []]
    excluidos = [_concepto(x, "fundamentos", "excluir_fundamento")["etiqueta"] for x in excluir_fundamento or []]
    respondidas = set()
    for r in responden_a or []:
        _, local, exp = _separar(r, ("afirmacion",), "responden_a")
        respondidas.add((exp, local))
    filas = _unicas(consultar("afirmaciones", **params))
    for f in filas:
        f["ref"] = _ref_calificada(f["a"].split("/id/", 1)[1])
    if valor:
        filas = [f for f in filas if _normal_en(valor, f["valorLabel"]) or f["valor"].rsplit("/", 1)[-1] in valor]
    if fuerzas:
        filas = [f for f in filas if f["fuerza"] in fuerzas]
    if fundamentos:
        filas = [f for f in filas if f["fundamento"] in fundamentos]
    if excluidos:
        filas = [f for f in filas if f["fundamento"] not in excluidos]
    if responden_a is not None:
        filas = [f for f in filas if f.get("respondeA") and (f["ref"].split(":")[0], f["respondeA"]) in respondidas]
    pares = entidad and atributo
    forma = forma_de(filas, atributo) if pares else ("A" if filas else "NC")
    if pares:
        resumen = resumen_disputa(filas, atributo) + " " + pronunciamientos(filas)
    elif filas:
        resumen = f"{len(filas)} afirmaciones (capa 3): cada una es de quien la hace, no un hecho."
    else:
        resumen = "El expediente no lo dice (no hay afirmaciones registradas con esos filtros)."
    if not filas:
        resumen += (" Que no lo diga vale en la medida en que la extracción de afirmaciones sea exhaustiva "
                    "(docs/G_evaluacion.md).")
    return _resultado("afirmaciones", dict(entidad=entidad, atributo=atributo, afirmante=afirmante, pieza=pieza,
                                           valor=valor, fuerza=fuerza, fundamento=fundamento,
                                           excluir_fundamento=excluir_fundamento, responden_a=responden_a,
                                           expediente=expediente),
                      forma, resumen, filas, afirmaciones=filas)


def disputas(entidad: str | None = None, atributo: str | None = None) -> Resultado:
    """Disputas calculadas en todo el corpus (consultas/disputas.rq): afirma/niega, valores distintos, negación
    enlazada y firma negada. Señala; no resuelve."""
    params = {}
    iri = _iri(*_separar(entidad, ("reconstruccion", "pieza"), "entidad")) if entidad else None
    if atributo:
        params["atributo"] = _concepto(atributo, "atributos", "atributo")["concepto"]
    filas = consultar("disputas", **params)
    if iri:       # no como parámetro: la consulta liga ?entidad con BIND en una de sus ramas (SPARQL no lo admite)
        filas = [f for f in filas if f["entidad"] == str(iri)]
    lineas = [f"  {f['entLabel']} — {f['atributo'].rsplit('/', 1)[-1]}: {f['tipo']} ({f['n']} afirmaciones: "
              f"{f['afirmaciones']})" for f in filas]
    resumen = (f"{len(filas)} disputas calculadas (no almacenadas); el historiador juzga si son incompatibles."
               if filas else "Ninguna disputa calculada con esos filtros.")
    return _resultado("disputas", dict(entidad=entidad, atributo=atributo), "DISPUTA" if filas else "NC", resumen,
                      filas, extra=lineas)


def disputas_firma(expediente: str | None = None) -> Resultado:
    """Disputa texto/afirmación: la pieza muestra la firma de alguien y en capa 3 alguien niega que firmara."""
    filas = consultar("disputas_firma", **({"expediente": _expediente_iri(expediente)} if expediente else {}))
    lineas = [f"  Pieza {f['pieza']}: muestra la firma «{f['firmaEscrita']}» ({f['mencionFirma']}), y "
              f"{f['negacion']} («{f['afirmante']}») lo niega: «{f['cita']}»" for f in filas]
    return _resultado("disputas_firma", dict(expediente=expediente), "DISPUTA" if filas else "NC",
                      f"{len(filas)} firmas que constan en el texto y alguien niega." if filas
                      else "Ninguna firma negada.", filas, extra=lineas)


def menciones_de(entidad: str, expediente: str | None = None) -> Resultado:
    """Menciones (capa 2) agrupadas por una reconstrucción: grafía tal como está escrita, tramo y pieza."""
    _, rid, _ = _separar(entidad, ("reconstruccion",), "entidad")
    params = {"filtroEntidad": _iri("reconstruccion", rid, "")}
    if expediente:
        params["expediente"] = _expediente_iri(expediente)
    filas = consultar("menciones_de", **params)
    for f in filas:
        f["id"] = f"{f['exp']}:{f['mid']}"
    lineas = [f"  «{f['texto']}» — {f['tramo']}, pieza {f['pieza']} ({f['tipoAct']}), mención {f['id']}" for f in filas]
    grafias = sorted({f["texto"] for f in filas})
    recs = [r for r in consultar("reconstrucciones") if r["entidad"] == params["filtroEntidad"]]
    return _resultado("menciones_de", dict(entidad=entidad, expediente=expediente), "D" if filas else "NC",
                      f"{len(grafias)} grafías en {len(filas)} menciones, agrupadas por la reconstrucción {rid} "
                      "(capa 4: es una hipótesis, ver su creencia).", filas + recs,
                      reconstrucciones=recs, extra=lineas)


def reconstrucciones(entidad: str | None = None, mencion: str | None = None, clase: str | None = None,
                     creencia: list[str] | None = None) -> Resultado:
    """Reconstrucciones (capa 4) con autor, fecha, creencia, argumento y de qué derivan. Con `mencion`, todas las
    que incluyen esa mención: las rivales salen juntas y ninguna se impone."""
    params = {}
    if mencion:
        params["m"] = _iri(*_separar(mencion, ("mencion",), "mencion"))
    filas = consultar("reconstrucciones", **params)
    por_entidad = {r["entidad"]: rid for rid, r in indice_reconstrucciones().items()}
    for f in filas:
        f["id"] = por_entidad.get(f["entidad"])
        f["clase"] = indice_reconstrucciones()[f["id"]]["clase"] if f["id"] else None
    if entidad:
        _, rid, _ = _separar(entidad, ("reconstruccion",), "entidad")
        filas = [f for f in filas if f["id"] == rid]
    if clase:
        if clase not in CLASES:
            raise ErrorHerramienta(f"reconstrucciones: clase={clase!r} no es válida; valores: {', '.join(CLASES)}")
        filas = [f for f in filas if f["clase"] == clase]
    if creencia:
        validas = {c["local"] for c in vocabulario_de("creencias")}
        malas = [c for c in creencia if c not in validas]
        if malas:
            raise ErrorHerramienta(f"reconstrucciones: creencia {', '.join(malas)} no válida; valores: "
                                   f"{', '.join(sorted(validas))}")
        filas = [f for f in filas if f["creencia"] in creencia]
    return _resultado("reconstrucciones", dict(entidad=entidad, mencion=mencion, clase=clase, creencia=creencia),
                      "R" if filas else "NC",
                      f"{len(filas)} reconstrucciones (hipótesis del investigador, con su creencia; ninguna se "
                      "impone a otra)." if filas else "Ninguna reconstrucción con esos filtros.", filas,
                      reconstrucciones=filas)


def cargos(titular: str | None = None) -> Resultado:
    """Ejercicios de cargo reconstruidos (capa 4) con vigencia, creencia y premisas."""
    params = {}
    if titular:
        _, rid, _ = _separar(titular, ("reconstruccion",), "titular")
        params["titular"] = _iri("reconstruccion", rid, "")
    filas = consultar("cargos", **params)
    lineas = [f"  EJERCICIO DE CARGO (capa 4): {c['cargo']} — titular {c['titularLabel']}; vigencia: "
              f"{c['inicio'] or '¿?'} a {c['fin'] or '¿?'} ({c['vigenciaNota'] or 'sin nota'}); creencia: "
              f"{c['creencia']}; autor: {c['autor']}; premisas: {c['premisasRef']}" for c in filas]
    return _resultado("cargos", dict(titular=titular), "R" if filas else "NC",
                      f"{len(filas)} ejercicios de cargo reconstruidos (capa 4)." if filas
                      else "Ningún ejercicio de cargo reconstruido.", filas, extra=lineas)


def piezas(expediente: str | None = None) -> Resultado:
    """Piezas (capa 1) en orden físico, con tipo de actuación, título y fecha escrita."""
    filas = consultar("piezas", **({"expediente": _expediente_iri(expediente)} if expediente else {}))
    lineas = [f"  {f['pieza']} [{f['tipo']}] {f['titulo']} — " + (f"fecha escrita: «{f['fecha']}»" if f["fecha"]
              else "sin fecha escrita") + (" (pieza ajena al expediente)" if f["ajena"] == "true" else "")
              for f in filas]
    return _resultado("piezas", dict(expediente=expediente), "D" if filas else "NC",
                      f"{len(filas)} piezas en orden físico de la transcripción.", filas, extra=lineas)


def control_secuencia(expediente: str | None = None, desde: int | None = None, hasta: int | None = None,
                      margen: int | None = None) -> Resultado:
    """Piezas cuyo orden físico contradice sus fechas normalizadas (capa 4) o con año fuera del expediente."""
    params = {k: v for k, v in dict(desde=desde, hasta=hasta, margen=margen).items() if v is not None}
    if expediente:
        params["expediente"] = _expediente_iri(expediente)
    filas = consultar("control_secuencia", **params)
    lineas = [f"  {s['p1']} ({s['f1']}) antes que {s['p2']} ({s['f2']}): {s['motivo']}" if s["p2"]
              else f"  {s['p1']} ({s['f1']}): {s['motivo']}" for s in filas]
    return _resultado("control_secuencia", dict(expediente=expediente, desde=desde, hasta=hasta, margen=margen),
                      "D", f"{len(filas)} incoherencias de fecha señaladas (se señalan, no se corrigen).", filas,
                      extra=lineas)


def participantes(expediente: str | None = None, pieza: str | None = None) -> Resultado:
    """Quién actúa en cada pieza y con qué papel procesal (capa 2), con su identidad reconstruida si la hay."""
    params = {}
    if pieza:
        _, local, exp = _separar(pieza, ("pieza",), "pieza")
        if expediente and expediente != exp:
            raise ErrorHerramienta(f"participantes: la pieza {pieza} no es del expediente {expediente}")
        expediente = expediente or exp
    if expediente:
        params["expediente"] = _expediente_iri(expediente)
    filas = consultar("participantes", **params)
    if pieza:
        filas = [f for f in filas if f["pieza"] == local]
    lineas = [f"  {f['pieza']} [{f['tipoAct']}] fecha escrita «{f['fecha'] or 'no consta'}»; data "
              f"«{f['lugar'] or 'no consta'}» — {f['rol']}: «{f['texto']}»"
              + (f" [{f['persona']}]" if f["persona"] else "") + f" ({f['mid']}, {f['tramo']})" for f in filas]
    return _resultado("participantes", dict(expediente=expediente, pieza=pieza), "D" if filas else "NC",
                      f"{len(filas)} participaciones en {len({f['pieza'] for f in filas})} piezas.", filas,
                      extra=lineas)


def procedencia(registro: str) -> Resultado:
    """Procedencia PROV-O de una afirmación o mención: transcripción (sha256), actividad, agente, plan, validación."""
    clase, local, exp = _separar(registro, ("afirmacion", "mencion"), "registro")
    filas = [{**f, "registro": f"{exp}:{local}"} for f in consultar("procedencia", x=_iri(clase, local, exp))]
    lineas = [f"  grafo {f['grafo']} ({f['capa'].rsplit('/', 1)[1]}): actividad {f['actividad']}, agente {f['agente']} "
              f"({f['tipoAgente'].rsplit('#', 1)[1]}), plan «{f['plan']}», transcripción {f['sha']}, "
              f"fecha {f['fecha']}, validación humana: {f['validador'] or 'NO REGISTRADA'}" for f in filas]
    return _resultado("procedencia", dict(registro=registro), "P" if filas else "NC",
                      "Procedencia del dato (PROV-O), no del testimonio de 1806.", filas, extra=lineas)


AVISO_CATALOGO = ("Según el catálogo del ARC (afirmaciones de los catalogadores, no hechos del modelo), extraído de "
                  "la capa de texto del PDF sin cotejo de imágenes; la pertinencia la marcó el extractor.")


def catalogo(pc: str | None = None, texto: str | None = None) -> Resultado:
    """Fichas e índices del catálogo del ARC marcados como pertinentes (capa C), con su texto literal."""
    filas = consultar("catalogo")
    if pc:
        filas = [f for f in filas if f["pc"] == pc]
    if texto:
        filas = [f for f in filas if normalizar(texto) in normalizar(f["texto"])]
    lineas = [f"  {f['etiqueta']} ({f['paginas']}): «{' '.join(f['texto'].split())}» — "
              f"{f['motivo'] or 'entrada de índice'}" + (f" [certeza: {f['certeza']}]" if f["certeza"] else "")
              + (" [nombra el pueblo de Tinta]" if f["pueblo"] == "true" else "") for f in filas]
    return _resultado("catalogo", dict(pc=pc, texto=texto), "A" if filas else "NC",
                      f"{len(filas)} fichas o índices. {AVISO_CATALOGO}", filas, extra=lineas)


def identificadores_externos() -> Resultado:
    """Lugares y grupos reconstruidos (capa 4) con identificador externo (HGIS de las Indias, WHG)."""
    filas = consultar("identificadores_externos")
    lineas = [f"  {e['label']}: {e['identificador']} {e['url'] or ''}".rstrip() for e in filas]
    return _resultado("identificadores_externos", {}, "R" if filas else "NC",
                      f"{len(filas)} lugares o grupos reconstruidos con identificador externo.", filas, extra=lineas)


ESQUEMAS = ("atributos", "fuerzas", "fundamentos", "polaridades", "roles", "cargos", "condiciones", "actuaciones",
            "entidades", "creencias", "documentos")


def vocabulario(esquema: str) -> Resultado:
    """Conceptos de un esquema del tesauro: nombre local (el que aceptan las herramientas) y etiqueta."""
    if esquema not in ESQUEMAS:
        raise ErrorHerramienta(f"vocabulario: esquema={esquema!r} no es válido; valores: {', '.join(ESQUEMAS)}")
    filas = [dict(c) for c in vocabulario_de(esquema)]
    lineas = [f"  {c['local']}: {c['etiqueta']}" + (" (candidato, sin aprobar)" if c["candidato"] == "true" else "")
              for c in filas]
    return _resultado("vocabulario", dict(esquema=esquema), "D", f"{len(filas)} conceptos del esquema {esquema}.", filas,
                      extra=lineas)


# ───────────────────────── registro ─────────────────────────

@dataclass(frozen=True)
class Herramienta:
    nombre: str
    descripcion: str
    parametros: dict           # JSON Schema (object)
    funcion: Callable[..., Resultado]


def _esquema(props: dict, requeridos: tuple[str, ...] = ()) -> dict:
    return {"type": "object", "properties": props, "required": list(requeridos), "additionalProperties": False}


_EXP = {"type": "string", "description": "Identificador del expediente (p. ej. «cc-14-18»). Sin él, todo el corpus."}
_ENT = ("Id de una reconstrucción («R-…», de buscar) o, calificado con su expediente, de una mención "
        "(«cc-14-18:M-UT01-003»)")
_LISTA = {"type": "array", "items": {"type": "string"}}

HERRAMIENTAS: list[Herramienta] = [
    Herramienta("buscar",
                "Resuelve un nombre escrito (persona, lugar, grupo, cosa o hecho; con cualquier grafía) a ids del "
                "grafo. Úsela SIEMPRE antes que cualquier otra herramienta que pida una entidad. Devuelve "
                "reconstrucciones (capa 4: hipótesis con creencia, número de menciones y las rivales que comparten "
                "menciones) y menciones sueltas no agrupadas. Si hay varias reconstrucciones o rivales, NO elija una: "
                "preséntelas todas con su creencia. Una lista vacía significa que el grafo no tiene ese nombre.",
                _esquema({"nombre": {"type": "string", "description": "Nombre tal como lo escribiría una persona."},
                          "clase": {"type": "string", "enum": list(CLASES)}, "expediente": _EXP,
                          "maximo": {"type": "integer", "description": "Candidatos como máximo (20)."}}, ("nombre",)),
                buscar),
    Herramienta("afirmaciones",
                "Afirmaciones (capa 3: quién dijo qué en 1806, con cita literal, tramo, folio, rol y fuerza "
                "institucional) sobre una entidad, de un afirmante, en una pieza o de un atributo. Con entidad y "
                "atributo calcula la forma: A (concordantes), DISPUTA (se afirma y se niega, o valores distintos) o "
                "NC (no consta). Una afirmación NUNCA es un hecho: preséntela como lo que alguien dijo. Los "
                "atributos válidos los da vocabulario(esquema=atributos).",
                _esquema({"entidad": {"type": "string", "description": _ENT + " o de una pieza («cc-14-18:P03»)."},
                          "atributo": {"type": "string", "description": "Nombre local del atributo (p. ej. «ejerce-cargo»)."},
                          "afirmante": {"type": "string", "description": _ENT + "."},
                          "pieza": {"type": "string", "description": "Pieza calificada («cc-14-18:P09»)."},
                          "valor": {**_LISTA, "description": "Solo filas cuyo valor contiene alguno de estos textos "
                                    "(sin distinguir mayúsculas ni tildes) o es ese concepto."},
                          "fuerza": {**_LISTA, "description": "Solo esas fuerzas (vocabulario fuerzas): p. ej. resolutiva, dictaminadora."},
                          "fundamento": {**_LISTA, "description": "Solo esos fundamentos (vocabulario fundamentos)."},
                          "excluir_fundamento": {**_LISTA, "description": "Excluye esos fundamentos (p. ej. «actuado»: la "
                                                 "autoridad resume lo actuado, no se pronuncia)."},
                          "responden_a": {**_LISTA, "description": "Solo afirmaciones que responden a (cumplen, niegan, "
                                          "contestan) alguna de estas afirmaciones calificadas («cc-14-18:A-UT19-004»)."},
                          "expediente": _EXP}),
                afirmaciones),
    Herramienta("disputas",
                "Disputas calculadas en todo el corpus para una entidad o un atributo: afirma/niega, valores "
                "distintos, negación enlazada. Señala desacuerdos; no dice quién tiene razón.",
                _esquema({"entidad": {"type": "string", "description": "Reconstrucción «R-…» o pieza calificada."},
                          "atributo": {"type": "string"}}),
                disputas),
    Herramienta("disputas_firma",
                "Firmas que constan en el texto de una pieza y que alguien niega haber puesto (disputa texto/afirmación).",
                _esquema({"expediente": _EXP}), disputas_firma),
    Herramienta("menciones_de",
                "Todas las menciones (grafías literales, tramo, pieza) que una reconstrucción agrupa. Para preguntas "
                "de grafías o de dónde aparece alguien.",
                _esquema({"entidad": {"type": "string", "description": "Reconstrucción «R-…»."}, "expediente": _EXP},
                         ("entidad",)),
                menciones_de),
    Herramienta("reconstrucciones",
                "Reconstrucciones del investigador (capa 4) con autor, fecha, creencia y argumento. Con «mencion» "
                "devuelve TODAS las hipótesis que incluyen esa mención (identidades en competencia). Filtros por clase "
                "y creencia (p. ej. posible, indeterminado, improbable para las identificaciones dudosas).",
                _esquema({"entidad": {"type": "string", "description": "Reconstrucción «R-…»."},
                          "mencion": {"type": "string", "description": "Mención calificada («cc-14-18:M-UT12.a-005»)."},
                          "clase": {"type": "string", "enum": list(CLASES)},
                          "creencia": {**_LISTA, "description": "falso, improbable, indeterminado, posible, probable, verdadero."}}),
                reconstrucciones),
    Herramienta("cargos",
                "Ejercicios de cargo reconstruidos (capa 4): cargo, titular, vigencia conocida, creencia y "
                "afirmaciones en que se apoyan.",
                _esquema({"titular": {"type": "string", "description": "Reconstrucción de persona «R-…»."}}), cargos),
    Herramienta("piezas",
                "Piezas del expediente en orden físico, con tipo de actuación, título y fecha escrita (capa 1).",
                _esquema({"expediente": _EXP}), piezas),
    Herramienta("control_secuencia",
                "Piezas cuyo orden físico contradice sus fechas normalizadas, o con año fuera del expediente.",
                _esquema({"expediente": _EXP, "desde": {"type": "integer"}, "hasta": {"type": "integer"},
                          "margen": {"type": "integer"}}),
                control_secuencia),
    Herramienta("participantes",
                "Quién actúa en cada pieza y con qué papel procesal (firmante, redactor, escribano, receptor, "
                "testigo…), con fecha y data escritas: cadena de autoridades y circulación del expediente.",
                _esquema({"expediente": _EXP, "pieza": {"type": "string", "description": "Pieza calificada."}}),
                participantes),
    Herramienta("procedencia",
                "De qué transcripción (sha256), qué actividad, qué agente y qué plan procede un dato, y quién lo validó.",
                _esquema({"registro": {"type": "string", "description": "Afirmación o mención calificada "
                                       "(«cc-14-18:A-UT11-004»)."}}, ("registro",)),
                procedencia),
    Herramienta("catalogo",
                "Fichas e índices del catálogo del ARC marcados como pertinentes para otras series y expedientes. "
                "Todo es «según el catálogo», no un hecho.",
                _esquema({"pc": {"type": "string", "description": "Pregunta para la que se marcó (PC03, PC04)."},
                          "texto": {"type": "string", "description": "Solo fichas cuyo texto contiene esto."}}),
                catalogo),
    Herramienta("identificadores_externos",
                "Lugares y grupos reconstruidos con identificador externo (HGIS de las Indias, WHG).",
                _esquema({}), identificadores_externos),
    Herramienta("vocabulario",
                "Lista cerrada de conceptos de un esquema del tesauro (atributos, fuerzas, fundamentos, cargos, "
                "condiciones…): los valores que aceptan los demás parámetros.",
                _esquema({"esquema": {"type": "string", "enum": list(ESQUEMAS)}}, ("esquema",)),
                vocabulario),
]
POR_NOMBRE = {h.nombre: h for h in HERRAMIENTAS}


def usar(herramienta: str, /, **parametros) -> Resultado:
    """Punto de entrada único del agente: valida los parámetros contra el esquema y ejecuta la herramienta."""
    if herramienta not in POR_NOMBRE:
        raise ErrorHerramienta(f"no existe la herramienta {herramienta!r}." + _sugerir(herramienta, POR_NOMBRE)
                               + f" Hay: {', '.join(POR_NOMBRE)}")
    h = POR_NOMBRE[herramienta]
    return h.funcion(**_validar(h, parametros))


# ───────────────────────── verificación posterior (§4.5) ─────────────────────────

_CITA = re.compile(r"«([^«»]*)»|\"([^\"]*)\"|“([^”]*)”")
_ID_AFIRMACION = re.compile(r"(?<![\w-])(?:[a-z0-9][a-z0-9-]*:)?(A-[A-Za-z0-9.-]*[A-Za-z0-9])")
# Frases que el compositor (laad.responder, laad.preguntas) pone entre comillas sin citar el documento: «no consta»
# (responder.NO_CONSTA), «no lo dice» (advertencia de exhaustividad) y la etiqueta del atributo «redactó la pieza»
# (aviso de redacción disputada en responder.linea_afirmacion). Se comparan sin distinguir mayúsculas.
EXENTAS = {"no consta", "no lo dice", "redactó la pieza"}


def _espacios(s: str) -> str:
    return " ".join(s.split())


def valores(filas) -> list[str]:
    """Todos los valores de texto de unas filas (también dentro de listas y diccionarios anidados)."""
    out = []
    pila = [filas]
    while pila:
        x = pila.pop()
        if isinstance(x, dict):
            pila.extend(x.values())
        elif isinstance(x, (list, tuple)):
            pila.extend(x)
        elif x is not None:
            out.append(str(x))
    return out


def citas(texto: str) -> list[str]:
    """Las citas entre comillas de un texto («…», "…" o “…”), con los espacios normalizados, sin repetir ni las exentas."""
    out = []
    for m in _CITA.finditer(texto):
        c = _espacios(next(g for g in m.groups() if g is not None))
        if c and c.lower() not in EXENTAS and c not in out:
            out.append(c)
    return out


def verificar(texto: str, filas) -> dict[str, list[str]]:
    """Lo que la respuesta `texto` cita y las filas no respaldan:
    * «citas»: las citas entre comillas («…», "…" o “…”) que no son subcadena, con los espacios normalizados, de
      ningún valor de las filas (se distinguen mayúsculas, tildes y cualquier letra);
    * «ids»: los ids de afirmación (A-…, solos o calificados) citados en el texto que no aparecen en las filas.
    Las dos listas vacías = respuesta verificada."""
    vals = [_espacios(v) for v in valores(filas)]
    faltan = [c for c in citas(texto) if not any(c in v for v in vals)]
    presentes = {i for v in vals for i in _ID_AFIRMACION.findall(v)}
    unidos = "\n".join(vals)
    ids = []
    for m in _ID_AFIRMACION.finditer(texto):
        completo, aid = m.group(0), m.group(1)
        if completo != aid:                       # calificado: debe constar en ese expediente
            exp = completo[: -len(aid) - 1]
            ok = bool(re.search(rf"(?<![\w-]){re.escape(exp)}(?::|/afirmacion/){re.escape(aid)}(?![A-Za-z0-9])",
                                unidos))
        else:
            ok = aid in presentes
        if not ok and completo not in ids:
            ids.append(completo)
    return {"citas": faltan, "ids": ids}
