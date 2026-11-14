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


# Perfil: el tesauro, sus conceptos candidatos (generados: scripts/candidatos.py) y el encabezado OHAC.
ARCHIVOS_PERFIL = ("tesauro.ttl", "candidatos.ttl", "ohac.ttl")
# Formas: las escritas a mano y las de dominio y rango de cada atributo (generadas: scripts/atributos.py).
ARCHIVOS_FORMAS = ("formas.ttl", "formas_atributos.ttl")


def grafo_perfil() -> rdflib.Graph:
    g = rdflib.Graph()
    for f in ARCHIVOS_PERFIL:
        if (ONT / f).exists():
            g.parse(ONT / f)
    return g


def grafo_formas() -> rdflib.Graph:
    g = rdflib.Graph()
    for f in ARCHIVOS_FORMAS:
        if (ONT / f).exists():
            g.parse(ONT / f)
    return g


def shacl(datos: rdflib.Graph, con_ontologias: bool = True):
    """(conforma, grafo de resultados, informe). Los AVISOS (sh:Warning: conceptos candidatos en uso, atributos
    candidatos sin dominio ni rango) no impiden conformar; se cuentan con avisos(grafo de resultados)."""
    d = rdflib.Graph()
    for t in datos:
        d.add(t)
    for t in grafo_perfil():
        d.add(t)
    ont = jerarquia_clases() if con_ontologias else None
    return validate(d, shacl_graph=grafo_formas(), ont_graph=ont, inference="none", advanced=True,
                    allow_warnings=True)


SH = rdflib.Namespace("http://www.w3.org/ns/shacl#")


def avisos(resultados: rdflib.Graph) -> list[tuple[str, str, str]]:
    """Avisos de una validación: (nodo foco, valor, mensaje) de cada resultado de severidad sh:Warning."""
    out = []
    for r in resultados.subjects(SH.resultSeverity, SH.Warning):
        out.append((str(resultados.value(r, SH.focusNode)), str(resultados.value(r, SH.value) or ""),
                    " ".join(sorted(str(m) for m in resultados.objects(r, SH.resultMessage)))))
    return sorted(out)


def resumen_avisos(resultados: rdflib.Graph) -> str:
    """Una línea por concepto o atributo avisado, con el número de nodos que lo usan."""
    from collections import Counter
    cuenta = Counter((foco, msj) for foco, _, msj in avisos(resultados))
    return "\n".join(f"  {n:>4} × {foco.rsplit('/tesauro/', 1)[-1]} — {msj}" for (foco, msj), n in sorted(cuenta.items()))


def jerarquia_clases() -> rdflib.Graph:
    """Solo rdfs:subClassOf entre IRIs de los estándares: lo que sh:class necesita, sin materializar
    dominios ni rangos (la inferencia RDFS completa sobre RiC-O tarda >6 min y no aporta a las formas)."""
    g = rdflib.Graph()
    for s, o in grafo_estandares().subject_objects(rdflib.RDFS.subClassOf):
        if isinstance(s, rdflib.URIRef) and isinstance(o, rdflib.URIRef):
            g.add((s, rdflib.RDFS.subClassOf, o))
    return g
