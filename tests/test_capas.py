"""Separación de capas por grafo nombrado (lo que SHACL sobre la unión no puede ver)."""
import pytest
from rdflib import Namespace, URIRef
from rdflib.namespace import PROV, RDF

from tests._fixtures import dataset

CRM = Namespace("http://www.cidoc-crm.org/cidoc-crm/")
CRMINF = Namespace("http://www.cidoc-crm.org/extensions/crminf/")
PICOM = Namespace("https://personsincontext.org/model#")
ROAR = Namespace("https://w3id.org/roar#")
G = "https://w3id.org/laad/grafo/"


def capa(gid: URIRef) -> str:
    s = str(gid)
    for c in ("documento", "texto", "afirmaciones", "reconstruccion", "argumentacion", "procedencia"):
        if s.startswith(G + c):
            return c
    return "otro"


def donde(pred, obj=None):
    out = set()
    for ctx in dataset().graphs():
        if (None, pred, obj) in ctx:
            out.add(capa(ctx.identifier))
    return out


@pytest.mark.parametrize("pred,obj,capas", [
    (RDF.type, CRM.E13_Attribute_Assignment, {"afirmaciones"}),
    (RDF.type, PICOM.PersonObservation, {"texto"}),
    (RDF.type, ROAR.LocationObservation, {"texto"}),
    (RDF.type, PICOM.PersonReconstruction, {"reconstruccion"}),
    (RDF.type, CRMINF.I2_Belief, {"argumentacion"}),            # la creencia, fuera de la proposición (revisión I4)
    (RDF.type, CRMINF.I5_Inference_Making, {"argumentacion"}),
    (CRMINF.J5_holds_to_be, None, {"argumentacion"}),           # creencias solo en capa 4 (fallo 1.4)
    (CRM.P82a_begin_of_the_begin, None, {"reconstruccion", "argumentacion"}),  # fechas normalizadas: capa 4 (fallo 2.6)
    (PROV.wasAttributedTo, None, {"procedencia"}),              # PROV solo para el dato (fallo 1.5)
    (PROV.wasGeneratedBy, None, {"procedencia", "reconstruccion"}),
    (RDF.type, CRM.E65_Creation, {"documento"}),
    (RDF.type, CRM.E89_Propositional_Object, {"afirmaciones"}),  # hechos narrados: proposición, no evento
    (RDF.type, CRM.E5_Event, {"reconstruccion"}),                # el evento ocurrido solo lo afirma el investigador
])
def test_termino_solo_en_su_capa(pred, obj, capas):
    assert donde(pred, obj) == capas


def test_ninguna_mencion_se_fusiona_en_capa_2():
    from rdflib.namespace import OWL
    assert donde(OWL.sameAs) == set()


def test_prov_no_atribuye_a_actores_de_1806():
    """wasAttributedTo solo apunta a agentes del proyecto (id/agente/...), nunca a menciones o personas de 1806."""
    for ctx in dataset().graphs():
        for o in ctx.objects(None, PROV.wasAttributedTo):
            assert str(o).startswith("https://w3id.org/laad/id/agente/"), o


def test_menciones_no_afirman_existencia():
    """Revisión I3: una mención no es crm:E21_Person/E53/E74 (eso afirmaría que existe)."""
    for c in (CRM.E21_Person, CRM.E53_Place, CRM.E74_Group):
        assert "texto" not in donde(RDF.type, c), c


def test_ningun_grafo_de_reconstruccion_contiene_su_propia_creencia():
    for ctx in dataset().graphs():
        if capa(ctx.identifier) == "reconstruccion":
            assert (None, CRMINF.J5_holds_to_be, None) not in ctx, ctx.identifier
