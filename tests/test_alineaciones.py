"""Alineaciones externas del tesauro (ADR-024): solo closeMatch/relatedMatch, hacia conceptos existentes."""
from __future__ import annotations

import subprocess
import sys

from rdflib import RDF, Graph
from rdflib.namespace import SKOS

from ._fixtures import RAIZ

EXTERNOS = ("http://www.wikidata.org/entity/Q", "http://vocab.getty.edu/aat/")


def _grafos():
    return Graph().parse(RAIZ / "ontologia/alineaciones.ttl"), Graph().parse(RAIZ / "ontologia/tesauro.ttl")


def test_alineaciones_sin_exactmatch_ni_closeMatch_interno():
    al, _ = _grafos()
    assert not list(al.triples((None, SKOS.exactMatch, None)))
    preds = {p for _, p, _ in al} - {SKOS.altLabel, SKOS.historyNote}
    assert preds <= {SKOS.closeMatch, SKOS.relatedMatch}, preds


def test_alineaciones_apuntan_a_conceptos_del_tesauro_y_a_autoridades_externas():
    al, tes = _grafos()
    conceptos = set(tes.subjects(RDF.type, SKOS.Concept))
    for s, p, o in al:
        assert s in conceptos, s
        if p in (SKOS.closeMatch, SKOS.relatedMatch):
            assert str(o).startswith(EXTERNOS), o


def test_etiquetas_quechuas_atestiguadas_llevan_nota_de_fuente():
    al, _ = _grafos()
    for s, _, lab in al.triples((None, SKOS.altLabel, None)):
        assert lab.language == "quz"
        assert any("González Holguín" in str(n) for n in al.objects(s, SKOS.historyNote)), s


def test_alineaciones_ttl_esta_al_dia_con_el_csv():
    ruta = RAIZ / "ontologia/alineaciones.ttl"
    antes = ruta.read_bytes()
    subprocess.run([sys.executable, str(RAIZ / "scripts/alineaciones.py")], check=True, capture_output=True)
    assert ruta.read_bytes() == antes, "alineaciones.ttl no coincide con el CSV: regenerar"
