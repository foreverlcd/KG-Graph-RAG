"""Versión y política de cambios del tesauro (ontologia/README.md, ontologia/CHANGELOG.md).

El tesauro se versiona entero: todos los esquemas llevan la misma owl:versionInfo y dct:modified, que coinciden con
la entrada más reciente del registro de cambios. Una IRI nunca se borra: se retira (owl:deprecated).
"""
from __future__ import annotations

import re

import rdflib
from rdflib import RDF, URIRef
from rdflib.namespace import DCTERMS, OWL, SKOS, XSD

from laad import esquema

from ._fixtures import RAIZ

ONT = RAIZ / "ontologia"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


def _tesauro() -> rdflib.Graph:
    return rdflib.Graph().parse(ONT / "tesauro.ttl")


def _entradas_changelog() -> list[tuple[str, str]]:
    return re.findall(r"(?m)^## \[(\d+\.\d+\.\d+)\] — (\d{4}-\d{2}-\d{2})", (ONT / "CHANGELOG.md").read_text(encoding="utf-8"))


def test_todos_los_esquemas_llevan_la_misma_version_y_fecha():
    t = _tesauro()
    esquemas = sorted(t.subjects(RDF.type, SKOS.ConceptScheme))
    assert len(esquemas) >= 12
    versiones = {e: list(t.objects(e, OWL.versionInfo)) for e in esquemas}
    fechas = {e: list(t.objects(e, DCTERMS.modified)) for e in esquemas}
    assert all(len(v) == 1 for v in versiones.values()), versiones
    assert all(len(f) == 1 and f[0].datatype == XSD.date for f in fechas.values()), fechas
    assert len({str(v[0]) for v in versiones.values()}) == 1, "el tesauro se versiona entero: una sola versión"
    assert len({str(f[0]) for f in fechas.values()}) == 1
    assert SEMVER.match(str(next(iter(versiones.values()))[0]))


def test_la_version_coincide_con_la_ultima_entrada_del_registro_de_cambios():
    t = _tesauro()
    esq = URIRef("https://w3id.org/laad/tesauro/atributos")
    entradas = _entradas_changelog()
    assert entradas and entradas[-1][0] == "0.1.0", "el registro empieza en 0.1.0 (estado anterior)"
    assert (str(t.value(esq, OWL.versionInfo)), str(t.value(esq, DCTERMS.modified))) == entradas[0]
    orden = [tuple(map(int, v.split("."))) for v, _ in entradas]
    assert orden == sorted(orden, reverse=True), "entradas de la más reciente a la más antigua"
    perfil = rdflib.Graph().parse(ONT / "ohac.ttl")
    assert str(perfil.value(URIRef("https://w3id.org/laad/ohac"), OWL.versionInfo)) == entradas[0][0]


def test_la_politica_esta_escrita():
    texto = (ONT / "README.md").read_text(encoding="utf-8")
    for apartado in ("Proponer", "Aprobar", "Rechazar", "Retirar", "Renombrar", "MAYOR", "MENOR", "PARCHE",
                     "owl:deprecated", "dct:isReplacedBy", "scripts/candidatos.py", "datos/atributos.csv"):
        assert apartado in texto, f"ontologia/README.md no trata «{apartado}»"


def test_un_concepto_retirado_conserva_definicion_y_esquema():
    """Retirar no es borrar: lo retirado sigue siendo un skos:Concept con etiqueta y esquema (y su reemplazo existe)."""
    g = esquema.grafo_tesauro()
    for c in set(g.subjects(OWL.deprecated, None)):
        assert (c, RDF.type, SKOS.Concept) in g and g.value(c, SKOS.prefLabel) and g.value(c, SKOS.inScheme), c
        for r in g.objects(c, DCTERMS.isReplacedBy):
            assert (r, RDF.type, SKOS.Concept) in g and (r, OWL.deprecated, None) not in g, (c, r)


def test_los_candidatos_no_estan_en_el_tesauro_versionado():
    """Un candidato no tiene versión: vive en candidatos.ttl hasta que se aprueba."""
    t = _tesauro()
    cand = rdflib.Graph().parse(ONT / "candidatos.ttl")
    for c in cand.objects(esquema.COLECCION_CANDIDATOS, SKOS.member):
        assert (c, None, None) not in t, c
