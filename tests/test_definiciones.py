"""El tesauro define todos sus conceptos y la sección generada coincide con el CSV."""
import importlib.util, pathlib
import rdflib
from rdflib.namespace import SKOS

RAIZ = pathlib.Path(__file__).resolve().parents[1]


def _script():
    spec = importlib.util.spec_from_file_location("definiciones", RAIZ / "scripts/definiciones.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def test_todos_los_conceptos_tienen_una_definicion_en_espanol():
    t = rdflib.Graph().parse(RAIZ / "ontologia/tesauro.ttl")
    for c in t.subjects(rdflib.RDF.type, SKOS.Concept):
        defs = [d for d in t.objects(c, SKOS.definition) if d.language == "es"]
        assert len(defs) == 1, f"{c}: {len(defs)} definiciones"


def test_seccion_de_definiciones_al_dia_con_el_csv():
    m = _script()
    texto = m.TESAURO.read_text(encoding="utf-8")
    assert m.aplicar(texto) == texto, "tesauro.ttl no coincide con definiciones_tesauro.csv: ejecutar scripts/definiciones.py"


def test_definiciones_sin_fuente_se_marcan_de_trabajo():
    t = rdflib.Graph().parse(RAIZ / "ontologia/tesauro.ttl")
    import csv
    with open(RAIZ / "datos/definiciones_tesauro.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            notas = {str(n) for n in t.objects(rdflib.URIRef(r["concepto_iri"]), SKOS.editorialNote)}
            if r["verificado"] != "si":
                assert "Definición de trabajo: fuente no verificada." in notas
