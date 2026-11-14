"""Los dos motores de consulta (Oxigraph, por defecto, y rdflib con LAAD_MOTOR=rdflib) devuelven las mismas filas.

Se ejecuta CADA consulta con nombre (consultas/*.rq), con y sin parámetros, sobre el corpus de datos/grafo/ en los dos
motores. Las filas deben coincidir como multiconjunto; si la consulta tiene ORDER BY, también debe coincidir la
secuencia de sus claves de orden (las filas que empatan en todas las claves pueden salir en otro orden).
Las consultas usan LATERAL (Oxigraph); para rdflib laad.consulta las reescribe en SPARQL 1.1 (sin_lateral).
Este módulo es lento a propósito: es el único que sigue ejecutando las consultas pesadas en rdflib.
"""
from __future__ import annotations

import re
from collections import Counter

import pytest
import rdflib

from laad import consulta as C
from laad.preguntas import EXPEDIENTE_PILOTO

E = C.expediente(EXPEDIENTE_PILOTO)
CASOS = [
    ("afirmaciones", dict(expediente=E)),
    ("afirmaciones", dict(expediente=E, filtroEntidad=C.persona("huancachoque"), atributo=C.atributo("tiene-condicion"))),
    ("afirmaciones", dict(expediente=E, filtroAfirmante=C.persona("cano"), atributo=C.atributo("ejerce-cargo"))),
    ("afirmaciones", dict(pieza_iri=C.pieza(EXPEDIENTE_PILOTO, "P09"))),
    ("candidatos_en_uso", {}),
    ("cargos", {}),
    ("cargos", dict(titular=C.persona("chuquitapa"))),
    ("catalogo", {}),
    ("control_secuencia", {}),
    ("control_secuencia", dict(expediente=E)),
    ("control_secuencia", dict(expediente=E, desde=1805, hasta=1807)),          # parámetros enteros
    ("control_secuencia", dict(hasta=1805)),
    ("disputas", {}),
    ("disputas_firma", dict(expediente=E)),
    ("identificadores_externos", {}),
    ("menciones_de", dict(expediente=E, filtroEntidad=C.persona("huancachoque"))),
    ("participantes", dict(expediente=E)),
    ("piezas", {}),
    ("piezas", dict(expediente=E)),
    ("procedencia", dict(x=C.afirmacion(EXPEDIENTE_PILOTO, "A-UT01-001"))),     # usa GRAPH
    ("procedencia", dict(x=C.mencion(EXPEDIENTE_PILOTO, "M-UT01-003"))),
    ("reconstrucciones", {}),
    ("reconstrucciones", dict(m=C.mencion(EXPEDIENTE_PILOTO, "M-UT01-003"))),
]


def test_los_casos_cubren_todas_las_consultas_con_nombre():
    assert {n for n, _ in CASOS} == set(C.nombres())


def _multiconjunto(filas, salvo=()):
    return Counter(tuple(sorted((k, "\0" if v is None else v) for k, v in f.items() if k not in salvo)) for f in filas)


@pytest.mark.parametrize("nombre,params", CASOS, ids=[f"{n}({','.join(p)})" for n, p in CASOS])
def test_mismas_filas_en_oxigraph_y_en_rdflib(nombre, params):
    ox = C.consultar(nombre, C.almacen(), **params)
    rd = C.consultar(nombre, C.dataset(), **params)
    assert ox, "caso sin filas: no compara nada"
    assert all(v is None or isinstance(v, str) for f in ox + rd for v in f.values())
    assert [list(f) for f in ox] == [list(f) for f in rd]                     # mismas columnas, mismo orden
    # SAMPLE elige un valor cualquiera del grupo (cada motor el suyo): esas columnas solo deben estar ligadas a la vez
    muestras = re.findall(r"SAMPLE\s*\([^)]*\)\s+AS\s+\?(\w+)", C.texto_consulta(nombre))
    assert _multiconjunto(ox, muestras) == _multiconjunto(rd, muestras)
    assert all(sorted((f[k] is None) for f in ox) == sorted((f[k] is None) for f in rd) for k in muestras)
    claves = C.claves_orden(nombre)
    assert [[f[k] for k in claves] for f in ox] == [[f[k] for k in claves] for f in rd]


def test_booleanos_numeros_y_no_ligados_como_texto():
    """Lo que esperan laad.preguntas y laad.responder: «true»/«false», números como texto y None si no hay valor."""
    piezas = C.consultar("piezas", expediente=E)
    assert {f["ajena"] for f in piezas} == {"true", "false"}
    assert any(f["fecha"] is None for f in piezas)
    assert all(f["n"].isdigit() for f in C.consultar("disputas"))
    afirm = C.consultar("afirmaciones", expediente=E, atributo=C.atributo("redacto"))
    assert afirm and all(f["eliptico"] in ("true", "false") and f["redaccionDisputada"] in ("true", "false") for f in afirm)
    assert {f["redaccionDisputada"] for f in C.consultar("afirmaciones", expediente=E)} == {"true", "false"}


def test_motor_por_variable_de_entorno(monkeypatch):
    assert C.motor() == "oxigraph"
    con_oxigraph = C.consultar("piezas", expediente=E)
    monkeypatch.setenv("LAAD_MOTOR", "rdflib")
    assert C.motor() == "rdflib"
    assert C.consultar("piezas", expediente=E) == con_oxigraph              # no reutiliza la caché del otro motor
    assert ("rdflib", "piezas", (("expediente", str(E)),)) in C._RESULTADOS
    assert isinstance(C.consultable(rdflib.Dataset()), rdflib.Dataset)
    monkeypatch.setenv("LAAD_MOTOR", "otro")
    with pytest.raises(ValueError):
        C.motor()


def test_la_cache_devuelve_copias():
    a = C.consultar("piezas", expediente=E)
    a[0]["pieza"] = "MUTADA"
    assert C.consultar("piezas", expediente=E)[0]["pieza"] != "MUTADA"


def test_parametros_validados():
    with pytest.raises(ValueError):
        C.consultar("piezas", expediente="https://w3id.org/laad/id/x> } INSERT {")
    with pytest.raises(ValueError):
        C.sparql("piezas", {"x y": E})
    assert f"VALUES ?expediente {{ <{E}> }}" in C.sparql("piezas", {"expediente": E})
    assert "#PARAMETROS" not in C.sparql("piezas")


def test_bloques_condicionales_y_fragmentos():
    """#SI … #FIN solo deja el bloque si llega el parámetro (#SI NO: si no llega); #PARAMETROS con nombres repite el
    VALUES dentro de una subconsulta; #INCLUIR trae un fragmento compartido. El parámetro opcional es un patrón que
    solo existe cuando se pide, no un FILTER (!BOUND(?p) || …)."""
    codigo = lambda q: "\n".join(x for x in q.split("\n") if not x.lstrip().startswith("#"))  # noqa: E731
    con, sin = codigo(C.sparql("piezas", {"expediente": E})), codigo(C.sparql("piezas"))
    assert con.count(f"VALUES ?expediente {{ <{E}> }}") == 2 and "rico:isOrWasInstantiationOf ?expediente" in con
    assert "?expediente" not in sin and "isOrWasInstantiationOf" not in sin
    for q in (con, sin):
        assert not re.search(r"(?m)^\s*#(SI|FIN|INCLUIR|PARAMETROS)\b", q)
    assert all("!BOUND(?expediente)" not in codigo(C.texto_consulta(n)) for n in C.nombres())
    assert "VALUES ?desde { 1805 }" in C.sparql("control_secuencia", {"desde": 1805})
    assert "?fc_" in C.sparql("control_secuencia") and "?fc_" not in codigo(C.sparql("control_secuencia", {"hasta": 1807}))
    with pytest.raises(ValueError):
        C.sparql("control_secuencia", {"desde": True})
    with pytest.raises(ValueError):
        C.sparql("control_secuencia", {"desde": "1805"})


def test_lateral_se_reescribe_para_rdflib():
    """LATERAL (Oxigraph) no existe en rdflib: sin_lateral lo reescribe en SPARQL 1.1 con OPTIONAL + BOUND."""
    q = C.sin_lateral("SELECT * WHERE { ?a ?b ?c . LATERAL { ?c ?d ?e . } LATERAL { OPTIONAL { ?e ?f ?g } } }")
    assert "LATERAL" not in q and q.count("OPTIONAL") == 2 and "FILTER (BOUND(?_ok1))" in q and "?_ok2" not in q
    rdflib.Graph().query(q)                                                  # es SPARQL 1.1 válido
    assert all("LATERAL" not in C.sin_lateral(C.sparql(n)) for n in C.nombres())
    with pytest.raises(ValueError):
        C.sin_lateral("SELECT * WHERE { ?a ?b ?c LATERAL { SELECT ?c WHERE { ?c ?d ?e } } }")


def test_control_de_secuencia_sin_intervalo_fijo():
    """El intervalo plausible sale de la carátula del expediente (± ?margen) o de ?desde/?hasta, no de la consulta."""
    fuera = lambda **p: {f["p1"] for f in C.consultar("control_secuencia", expediente=E, **p) if f["p2"] is None}  # noqa: E731
    assert fuera() == fuera(desde=1805, hasta=1807) == {"P31"}
    assert fuera(margen=5) == fuera(hasta=1810) == set()
    assert "P00" in fuera(desde=1807)


def test_cargos_con_premisas_calificadas():
    for f in C.consultar("cargos"):
        assert [r.rsplit("/", 1)[1] for r in f["premisasRef"].split()] == f["premisas"].split()
        assert all(r.startswith(f"{EXPEDIENTE_PILOTO}/afirmacion/") for r in f["premisasRef"].split())


def test_la_union_no_duplica_tripletas_repetidas_en_dos_grafos():
    """La misma tripleta en dos grafos nombrados cuenta UNA vez en el grafo por defecto (como en rdflib)."""
    ds = rdflib.Dataset()
    s, p, o = (rdflib.URIRef(f"https://example.org/{x}") for x in "spo")
    ds.graph(rdflib.URIRef("https://example.org/g1")).add((s, p, o))
    ds.graph(rdflib.URIRef("https://example.org/g2")).add((s, p, o))
    store = C.consultable(ds)
    n = lambda q: int(next(iter(store.query(q)))[0].value)  # noqa: E731
    assert n("SELECT (COUNT(*) AS ?n) WHERE { <https://example.org/s> ?p ?o }") == 1
    assert n("SELECT (COUNT(*) AS ?n) WHERE { GRAPH ?g { <https://example.org/s> ?p ?o } }") == 2


def test_almacen_persistente_y_carga_masiva(tmp_path):
    """El almacén en disco (scripts/servir.py --volcar: carga masiva, unión por texto) contiene exactamente las
    mismas cuádruplas que el de memoria (unión por actualización SPARQL) y responde igual al reabrirlo."""
    store = C.nuevo_almacen(persistente=tmp_path / "oxi", masivo=True)
    assert set(store) == set(C.almacen())
    del store
    disco = C.abrir_almacen(tmp_path / "oxi")
    for nombre, params in (("piezas", dict(expediente=E)), ("procedencia", dict(x=C.afirmacion(EXPEDIENTE_PILOTO, "A-UT01-001"))),
                           ("reconstrucciones", {})):
        assert C.consultar(nombre, disco, **params) == C.consultar(nombre, **params)
