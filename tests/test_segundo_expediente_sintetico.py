"""Prueba ESTRUCTURAL de generalidad (revisión C2): un expediente civil SINTÉTICO entra sin tocar el núcleo.

El texto (tests/_sintetico.py) es inventado para la prueba (no es una fuente histórica ni debe citarse). La prueba
real del criterio 5 usa el expediente sorteado a ciegas (CO Cusco Leg. 70 Exp. 15) cuando haya transcripción.
Comprueba: (1) parametrización por manifiesto, sin constantes de CC L14E18; (2) clase de mención «cosa»,
afirmante colectivo (grupo) y concepto validado por dct:conformsTo; (3) SHACL conforma; (4) no aparece ninguna
clase ni propiedad que no use ya el grafo del expediente piloto (núcleo cerrado).
"""
import pytest
import rdflib

from laad import consulta, corpus, fuente, mapeo, validacion

from ._sintetico import EXP_SINTETICO, instalar


@pytest.fixture
def expediente_sintetico(tmp_path, monkeypatch):
    """Corpus de UN solo expediente, el sintético: su manifiesto es todo lo que hace falta para construirlo."""
    instalar(tmp_path, tmp_path / "expedientes")
    monkeypatch.setattr(fuente, "MANIFIESTOS", tmp_path / "expedientes")
    assert corpus.expedientes() == [EXP_SINTETICO]
    lote = corpus.cargar(EXP_SINTETICO)
    assert not lote.errores, lote.errores
    return corpus.construir(reconstrucciones=None, catalogo=None)


def _vocabulario(g: rdflib.Graph) -> tuple[set, set]:
    clases = {o for o in g.objects(None, rdflib.RDF.type) if not str(o).startswith("https://w3id.org/laad/")}
    props = {p for p in g.predicates()}
    return clases, props


def test_expediente_sintetico_conforma_sin_tocar_el_nucleo(expediente_sintetico):
    ref = rdflib.Dataset()
    for trig in sorted(consulta.GRAFO.glob("*.trig")):
        ref.parse(trig, format="trig")
    u = mapeo.union(expediente_sintetico)
    conforma, _, texto = validacion.shacl(u, con_ontologias=True)
    assert conforma, texto[:3000]
    c2, p2 = _vocabulario(u)
    c1, p1 = _vocabulario(mapeo.union(ref))
    # prov:Person ya pertenece al perfil (agente humano: anotador o validador, mapeo._agente); el expediente piloto
    # solo lo anotó un prov:SoftwareAgent, por eso no aparece en su grafo.
    c1 |= {rdflib.PROV.Person}
    assert c2 <= c1, f"clases nuevas: {c2 - c1}"
    assert p2 <= p1, f"propiedades nuevas: {p2 - p1}"


def test_iris_del_sintetico_no_colisionan_con_cc_14_18(expediente_sintetico):
    s = {str(x) for x in mapeo.union(expediente_sintetico).subjects()}
    assert any(f"/{EXP_SINTETICO}/" in x for x in s)
    assert not any("/cc-14-18/" in x for x in s)
