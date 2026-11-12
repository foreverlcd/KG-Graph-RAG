"""Todo término de un estándar externo usado en el grafo, en las formas o en el perfil existe en los
archivos descargados (vendor/); todo concepto del tesauro usado está declarado y bien formado."""
from __future__ import annotations

import functools
import re

import rdflib
from rdflib import RDF, URIRef
from rdflib.namespace import OWL, SH, SKOS

from laad import validacion

from ._fixtures import union

ESPACIOS = {
    "rico": "https://www.ica.org/standards/RiC/ontology#",
    "rst": "https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#",
    "crm": "http://www.cidoc-crm.org/cidoc-crm/",
    "crminf": "http://www.cidoc-crm.org/extensions/crminf/",
    "prov": "http://www.w3.org/ns/prov#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "oa": "http://www.w3.org/ns/oa#",
    "picom": "https://personsincontext.org/model#",
    "roar": "https://w3id.org/roar#",
    "picot_roles": "https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/",
}
PROYECTO = "https://w3id.org/laad/"
TES = "https://w3id.org/laad/tesauro/"


def _vigilada(x) -> bool:
    return isinstance(x, URIRef) and not str(x).startswith(PROYECTO) and str(x).startswith(tuple(ESPACIOS.values()))


@functools.lru_cache(maxsize=1)
def _declaradas() -> frozenset:
    g = validacion.grafo_estandares()
    for f in sorted((validacion.VENDOR / "pico-roles").glob("*.rdf")):
        g.parse(f, format="xml")
    return frozenset(s for s in g.subjects() if isinstance(s, URIRef))


def _terminos_sparql(formas: rdflib.Graph) -> set[URIRef]:
    """Términos citados dentro del texto de las consultas sh:select (prefijados o entre <>)."""
    pref = {str(p): str(n) for d in formas.objects(None, SH.declare)
            for p, n in [(formas.value(d, SH.prefix), formas.value(d, SH.namespace))]}
    out = set()
    for q in formas.objects(None, SH.select):
        for m in re.finditer(r"<([^<>\s]+)>", str(q)):
            out.add(URIRef(m.group(1)))
        for m in re.finditer(r"(?<![\w<:#])([A-Za-z][\w-]*):([A-Za-z_][\w.\-]*[\w-])", str(q)):
            if m.group(1) in pref:
                out.add(URIRef(pref[m.group(1)] + m.group(2)))
    return out


def _usadas() -> dict[URIRef, set[str]]:
    fuentes = {"unión": union(),
               "formas.ttl": rdflib.Graph().parse(validacion.ONT / "formas.ttl"),
               "ohac.ttl": rdflib.Graph().parse(validacion.ONT / "ohac.ttl")}
    usadas: dict[URIRef, set[str]] = {}
    for nombre, g in fuentes.items():
        # los objetos de owl:imports son IRI nominales de ontología (versión), no términos (ver ohac.ttl)
        importadas = set(g.objects(None, OWL.imports))
        for t in g:
            for x in t:                       # sujeto, predicado y objeto (incluye objetos de rdf:type)
                if _vigilada(x) and x not in importadas:
                    usadas.setdefault(x, set()).add(nombre)
    for x in _terminos_sparql(fuentes["formas.ttl"]):
        if _vigilada(x):
            usadas.setdefault(x, set()).add("formas.ttl (SPARQL)")
    return usadas


def test_terminos_de_estandares_declarados_en_vendor():
    usadas = _usadas()
    assert len(usadas) > 50, "la recogida de términos parece vacía"
    faltan = {x: sorted(d) for x, d in usadas.items() if x not in _declaradas()}
    assert not faltan, "términos no declarados en vendor/:\n" + "\n".join(
        f"  {x}  (en {', '.join(d)})" for x, d in sorted(faltan.items()))


def test_se_usan_todos_los_espacios_esperados():
    # salvaguarda contra una prueba anterior vacía por un error de espacio de nombres
    usados = {p for x in _usadas() for p, n in ESPACIOS.items() if str(x).startswith(n)}
    assert {"rico", "rst", "crm", "crminf", "prov", "skos", "oa", "picom", "roar", "picot_roles"} <= usados


@functools.lru_cache(maxsize=1)
def _tesauro() -> rdflib.Graph:
    return rdflib.Graph().parse(validacion.ONT / "tesauro.ttl")


def test_conceptos_del_tesauro_usados_estan_declarados():
    tes = _tesauro()
    declarados = set(tes.subjects(RDF.type, SKOS.Concept)) | set(tes.subjects(RDF.type, SKOS.ConceptScheme))
    usados = {x for t in union() for x in t if isinstance(x, URIRef) and str(x).startswith(TES)}
    assert usados, "la unión no usa ningún concepto del tesauro"
    faltan = sorted(usados - declarados)
    assert not faltan, "conceptos usados sin declarar en tesauro.ttl:\n" + "\n".join(map(str, faltan))


def test_conceptos_del_tesauro_tienen_preflabel_e_inscheme():
    tes = _tesauro()
    conceptos = sorted(tes.subjects(RDF.type, SKOS.Concept))
    assert conceptos
    malos = [f"{c} sin {', '.join(f for f, p in (('prefLabel', SKOS.prefLabel), ('inScheme', SKOS.inScheme)) if tes.value(c, p) is None)}"
             for c in conceptos if tes.value(c, SKOS.prefLabel) is None or tes.value(c, SKOS.inScheme) is None]
    assert not malos, "\n".join(malos)


def test_catalogo_resuelve_todas_las_importaciones():
    """Cada owl:imports de ohac.ttl tiene entrada en catalog-v001.xml, el archivo existe y declara esa IRI."""
    import xml.etree.ElementTree as ET
    from pathlib import Path
    from rdflib import Graph, OWL, RDF
    raiz = Path(__file__).resolve().parents[1]
    perfil = Graph().parse(raiz / "ontologia/ohac.ttl")
    imports = {str(o) for o in perfil.objects(None, OWL.imports)}
    ns = {"c": "urn:oasis:names:tc:entity:xmlns:xml:catalog"}
    cat = {u.get("name"): u.get("uri") for u in ET.parse(raiz / "ontologia/catalog-v001.xml").getroot().findall("c:uri", ns)}
    assert imports <= set(cat), imports - set(cat)
    for iri in imports:
        ruta = (raiz / "ontologia" / cat[iri]).resolve()
        fmt = "xml" if ruta.suffix in (".rdf", ".rdfs") else "turtle"
        g = Graph().parse(ruta, format=fmt)
        declaradas = {str(s) for s in g.subjects(RDF.type, OWL.Ontology)} | {str(v) for v in g.objects(None, OWL.versionIRI)}
        assert iri in declaradas, (iri, ruta)
