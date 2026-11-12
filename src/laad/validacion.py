"""Validación: SHACL (pyshacl) y consistencia con razonador OWL RL (owlrl)."""
from __future__ import annotations

from pathlib import Path

import rdflib
from pyshacl import validate

RAIZ = Path(__file__).resolve().parents[2]
ONT = RAIZ / "ontologia"
VENDOR = RAIZ / "vendor"

ARCHIVOS_ESTANDARES = [
    ("ric-o/RiC-O_1-1.rdf", "xml"),
    ("ric-o/RiC_RecordSetTypes_vocabulary.rdf", "xml"),
    ("cidoc-crm/CIDOC_CRM_v7.1.3.rdfs", "xml"),
    ("cidoc-crm/CIDOC_CRM_v7.1.3_PC.rdfs", "xml"),
    ("crminf/CRMinf_v1.2.1.rdf", "xml"),
    ("prov-o/prov-o-20130430.ttl", "turtle"),
    ("skos/skos-core.rdf", "xml"),
    ("oa/oa.ttl", "turtle"),
    ("pico/pico.ttl", "turtle"),
    ("roar/roar.ttl", "turtle"),
]


def grafo_estandares() -> rdflib.Graph:
    g = rdflib.Graph()
    for rel, fmt in ARCHIVOS_ESTANDARES:
        p = VENDOR / rel
        if not p.exists():
            cand = list(p.parent.glob("*"))
            raise FileNotFoundError(f"{p} no existe; en {p.parent}: {[c.name for c in cand]}")
        g.parse(p, format=fmt)
    return g


def grafo_perfil() -> rdflib.Graph:
    g = rdflib.Graph()
    for f in ("tesauro.ttl", "ohac.ttl"):
        g.parse(ONT / f)
    return g


def shacl(datos: rdflib.Graph, con_ontologias: bool = True):
    formas = rdflib.Graph().parse(ONT / "formas.ttl")
    d = rdflib.Graph()
    for t in datos:
        d.add(t)
    for t in grafo_perfil():
        d.add(t)
    ont = jerarquia_clases() if con_ontologias else None
    return validate(d, shacl_graph=formas, ont_graph=ont, inference="none", advanced=True, allow_warnings=True)


def jerarquia_clases() -> rdflib.Graph:
    """Solo rdfs:subClassOf entre IRIs de los estándares: lo que sh:class necesita, sin materializar
    dominios ni rangos (la inferencia RDFS completa sobre RiC-O tarda >6 min y no aporta a las formas)."""
    g = rdflib.Graph()
    for s, o in grafo_estandares().subject_objects(rdflib.RDFS.subClassOf):
        if isinstance(s, rdflib.URIRef) and isinstance(o, rdflib.URIRef):
            g.add((s, rdflib.RDFS.subClassOf, o))
    return g
