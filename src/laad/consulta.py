"""Consulta estructurada sobre el grafo (SPARQL de consultas/*.rq) para el agente conversacional.

El agente NO genera SPARQL libre: elige una consulta con nombre y le pasa parámetros (initBindings). Cada fila
devuelta lleva la cita literal, el tramo y el folio (o «no consta»), de modo que la respuesta se compone de
filas verificables (docs/D_extraccion_consulta.md §4).
"""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

import rdflib
from rdflib import URIRef

from . import fuente

RAIZ = Path(__file__).resolve().parents[2]
CONSULTAS = RAIZ / "consultas"
GRAFO = RAIZ / "datos" / "grafo"
G_TESAURO = URIRef("https://w3id.org/laad/grafo/tesauro")


@lru_cache(maxsize=2)
def dataset(directorio: Path = GRAFO) -> rdflib.Dataset:
    """El corpus entero: todos los datos/grafo/*.trig (uno por expediente más comun.trig) y el tesauro."""
    trigs = sorted(directorio.glob("*.trig"))
    if not trigs:
        raise FileNotFoundError(f"no hay ningún .trig en {directorio}; ejecute scripts/construir.py")
    ds = rdflib.Dataset(default_union=True)
    for trig in trigs:
        ds.parse(trig, format="trig")
    ds.graph(G_TESAURO).parse(RAIZ / "ontologia" / "tesauro.ttl")
    return ds


def consultable(ds: rdflib.Dataset) -> rdflib.Dataset:
    """Copia de un Dataset recién construido (laad.corpus.construir) lista para consultar: unión de grafos por
    defecto y tesauro, igual que dataset()."""
    out = rdflib.Dataset(default_union=True)
    for g in ds.graphs():
        if len(g):
            destino = out.graph(g.identifier)
            for t in g:
                destino.add(t)
    out.graph(G_TESAURO).parse(RAIZ / "ontologia" / "tesauro.ttl")
    return out


def texto_consulta(nombre: str) -> str:
    return (CONSULTAS / "_prefijos.rq").read_text() + "\n" + (CONSULTAS / f"{nombre}.rq").read_text()


_IRI_SEGURA = re.compile(r"^https?://[^\s<>\"{}|\\^`]+$")


def _values(params: dict) -> str:
    """Bloque VALUES con IRIs validadas (el agente nunca inyecta texto SPARQL libre)."""
    lineas = []
    for k, v in params.items():
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", k):
            raise ValueError(f"parámetro no válido: {k}")
        vals = v if isinstance(v, (list, tuple)) else [v]
        celdas = []
        for x in vals:
            if not _IRI_SEGURA.match(str(x)):
                raise ValueError(f"IRI no válida para {k}: {x!r}")
            celdas.append(f"<{x}>")
        lineas.append(f"VALUES ?{k} {{ {' '.join(celdas)} }}")
    return "\n  ".join(lineas)


def consultar(nombre: str, ds: rdflib.Dataset | None = None, **params) -> list[dict]:
    """Ejecuta una consulta con nombre. Sin `ds` consulta el corpus de datos/grafo/ y recuerda el resultado (el
    grafo en disco no cambia durante el proceso; tras reconstruirlo, limpiar_cache())."""
    if ds is None:
        clave = (nombre, tuple(sorted((k, tuple(map(str, v)) if isinstance(v, (list, tuple)) else str(v))
                                      for k, v in params.items())))
        if clave not in _RESULTADOS:
            _RESULTADOS[clave] = _consultar(nombre, dataset(), params)
        return [dict(f) for f in _RESULTADOS[clave]]
    return _consultar(nombre, ds, params)


_RESULTADOS: dict[tuple, list[dict]] = {}


def limpiar_cache() -> None:
    """Olvida el corpus leído de disco y los resultados recordados (p. ej. tras scripts/construir.py)."""
    _RESULTADOS.clear()
    dataset.cache_clear()


def _consultar(nombre: str, ds: rdflib.Dataset, params: dict) -> list[dict]:
    q = texto_consulta(nombre)
    marca = re.compile(r"(?m)^[ \t]*#PARAMETROS[ \t]*$")
    if params and not marca.search(q):
        raise ValueError(f"la consulta {nombre} no admite parámetros")
    res = ds.query(marca.sub(lambda _: "  " + _values(params), q, count=1))
    filas = []
    for r in res:
        filas.append({str(k): (str(r[k]) if r[k] is not None else None) for k in res.vars})
    return filas


ID = "https://w3id.org/laad/id/"
TES = "https://w3id.org/laad/tesauro/"


# IRIs de recursos de UN expediente (parámetros de las consultas con nombre).
def expediente(exp: str) -> URIRef:
    """IRI archivística del expediente (último nivel de la jerarquía de su manifiesto): valor del parámetro
    ?expediente con el que las consultas se restringen a un expediente."""
    return URIRef(ID + fuente.manifiesto(exp)["jerarquia"][-1]["id"])


def pieza(exp: str, pid: str) -> URIRef: return URIRef(f"{ID}{exp}/pieza/{pid}")
def mencion(exp: str, mid: str) -> URIRef: return URIRef(f"{ID}{exp}/mencion/{mid}")
def afirmacion(exp: str, aid: str) -> URIRef: return URIRef(f"{ID}{exp}/afirmacion/{aid}")


# IRIs de la capa 4 (comunes al corpus: no llevan expediente).
def persona(slug: str) -> URIRef: return URIRef(f"{ID}persona/{slug}")
def evento(slug: str) -> URIRef: return URIRef(f"{ID}evento/{slug}")
def atributo(local: str) -> URIRef: return URIRef(f"{TES}atributo/{local}")
