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

RAIZ = Path(__file__).resolve().parents[2]
CONSULTAS = RAIZ / "consultas"
TRIG = RAIZ / "datos" / "grafo" / "cc-14-18.trig"


@lru_cache(maxsize=2)
def dataset(trig: Path = TRIG) -> rdflib.Dataset:
    ds = rdflib.Dataset(default_union=True)
    ds.parse(trig, format="trig")
    tes = ds.graph(URIRef("https://w3id.org/laad/grafo/tesauro"))
    tes.parse(RAIZ / "ontologia" / "tesauro.ttl")
    return ds


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
    ds = ds or dataset()
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


def persona(slug: str) -> URIRef: return URIRef(f"{ID}persona/{slug}")
def evento(slug: str) -> URIRef: return URIRef(f"{ID}evento/{slug}")
def atributo(local: str) -> URIRef: return URIRef(f"{TES}atributo/{local}")
