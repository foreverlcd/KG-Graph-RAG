"""Conceptos candidatos del tesauro (scripts/candidatos.py, ontologia/candidatos.ttl): lo que un anotador necesita y
el tesauro no tiene se registra, se puede usar con AVISO y acaba aprobado o rechazado; nunca se pierde ni se borra.

(a) lo generado coincide con datos/candidatos_tesauro.csv; (b) todo candidato lleva definición, proponente, fecha y
ejemplo, con vocabulario estándar; (c) el ciclo proponer → aprobar / rechazar; (d) los registros pueden usar un
candidato (aviso) y no un concepto retirado (error); (e) la validación SHACL y la consulta con nombre los cuentan;
(f) ningún registro ni reconstrucción usa un concepto retirado.
"""
from __future__ import annotations

import importlib.util
import json
import shutil

import pytest
import rdflib
from rdflib import RDF, URIRef
from rdflib.namespace import DCTERMS, OWL, PROV, SKOS, XSD

from laad import consulta, corpus, esquema, validacion

from ._fixtures import EXPEDIENTE_PILOTO, RAIZ, RECONSTRUCCIONES, dataset, union

TES = "https://w3id.org/laad/tesauro/"


def _script():
    spec = importlib.util.spec_from_file_location("candidatos", RAIZ / "scripts/candidatos.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


C = _script()


def _fila(**cambios) -> dict:
    f = dict(esquema="cargos", local="pregonero", etiqueta="pregonero", definicion="Oficial que publica los bandos.",
             broader="", propuesto_por="anotadora-x (lote de prueba)", fecha="2026-11-14",
             expediente=EXPEDIENTE_PILOTO, ejemplo="UT99: «el pregonero»", estado="candidato", reemplazado_por="")
    f.update(cambios)
    return f


def _grafos(filas: list[dict]) -> tuple[rdflib.Graph, rdflib.Graph]:
    candidatos, tesauro = C.generar(filas)
    return rdflib.Graph().parse(data=candidatos, format="turtle"), rdflib.Graph().parse(data=tesauro, format="turtle")


# ─────────────── (a) lo generado está al día ───────────────
def test_candidatos_ttl_y_seccion_de_aprobados_al_dia_con_el_csv():
    candidatos, tesauro = C.generar()
    assert C.CANDIDATOS.read_text(encoding="utf-8") == candidatos, "ejecutar scripts/candidatos.py"
    assert C.TESAURO.read_text(encoding="utf-8") == tesauro, "ejecutar scripts/candidatos.py"


def test_cada_fila_pendiente_es_un_concepto_de_su_esquema_y_miembro_de_la_coleccion():
    g = rdflib.Graph().parse(C.CANDIDATOS)
    ns = C.espacios(C.tesauro_base())
    pendientes = [f for f in C.leer() if f["estado"] == "candidato"]
    assert pendientes
    assert (esquema.COLECCION_CANDIDATOS, RDF.type, SKOS.Collection) in g
    assert len(set(g.objects(esquema.COLECCION_CANDIDATOS, SKOS.member))) == len(pendientes)
    for f in pendientes:
        c = URIRef(ns[f["esquema"]] + f["local"])
        assert (c, RDF.type, SKOS.Concept) in g and (c, SKOS.inScheme, URIRef(TES + f["esquema"])) in g
        assert (esquema.COLECCION_CANDIDATOS, SKOS.member, c) in g
        assert f["local"] in esquema.conceptos(f["esquema"]) and f["local"] in esquema.candidatos(f["esquema"])


# ─────────────── (b) todo candidato está documentado ───────────────
def test_todo_candidato_tiene_definicion_proponente_fecha_y_ejemplo():
    for f in C.leer():
        for campo in ("definicion", "propuesto_por", "fecha", "ejemplo", "expediente", "etiqueta"):
            assert f[campo], f"{f['esquema']}/{f['local']} sin {campo}"
    g = rdflib.Graph().parse(C.CANDIDATOS)
    conceptos = set(g.subjects(RDF.type, SKOS.Concept))
    assert conceptos
    for c in conceptos:
        assert [d for d in g.objects(c, SKOS.definition) if d.language == "es"], c
        assert g.value(c, SKOS.prefLabel) is not None and g.value(c, SKOS.example) is not None, c
        assert g.value(c, DCTERMS.created).datatype == XSD.date, c
        agente = g.value(c, PROV.wasAttributedTo)
        assert (agente, RDF.type, PROV.Agent) in g, c
        assert g.value(c, DCTERMS.source) is not None and g.value(c, SKOS.historyNote) is not None, c


def test_los_candidatos_solo_usan_vocabulario_estandar():
    g = rdflib.Graph().parse(C.CANDIDATOS)
    estandar = tuple(str(n) for n in (SKOS, DCTERMS, OWL, PROV, RDF, rdflib.RDFS))
    propios = {p for p in g.predicates() if not str(p).startswith(estandar)}
    propios |= {o for o in g.objects(None, RDF.type) if not str(o).startswith(estandar)}
    assert not propios, propios


@pytest.mark.parametrize("cambios, mensaje", [
    (dict(ejemplo=""), "falta «ejemplo»"),
    (dict(definicion=""), "falta «definicion»"),
    (dict(propuesto_por=""), "falta «propuesto_por»"),
    (dict(fecha="14/11/2026"), "AAAA-MM-DD"),
    (dict(esquema="oficios"), "esquema desconocido"),
    (dict(local="Pregonero Mayor"), "nombre local no válido"),
    (dict(local="cacique"), "ya existe en el tesauro"),
    (dict(broader="no-existe"), "broader"),
    (dict(expediente="zz-0-0"), "expediente desconocido"),
    (dict(estado="quizas"), "estado"),
    (dict(reemplazado_por="cacique"), "solo se admite en filas rechazadas"),
    (dict(estado="rechazado", reemplazado_por="no-existe"), "reemplazado_por"),
])
def test_una_fila_incompleta_o_incoherente_no_se_genera(cambios, mensaje):
    with pytest.raises(C.ErrorCandidatos, match=mensaje):
        C.generar([_fila(**cambios)])


def test_fila_repetida_es_error():
    with pytest.raises(C.ErrorCandidatos, match="repetida"):
        C.generar([_fila(), _fila()])


# ─────────────── (c) ciclo de vida ───────────────
def test_un_rechazado_conserva_su_iri_queda_retirado_y_apunta_a_su_reemplazo():
    cand, tes = _grafos([_fila(estado="rechazado", reemplazado_por="escribano")])
    c = URIRef(TES + "cargo/pregonero")
    assert (c, RDF.type, SKOS.Concept) in cand and (c, OWL.deprecated, rdflib.Literal(True)) in cand
    assert cand.value(c, DCTERMS.isReplacedBy) == URIRef(TES + "cargo/escribano")
    assert (esquema.COLECCION_CANDIDATOS, SKOS.member, c) not in cand
    assert (c, None, None) not in tes


def test_un_aprobado_pasa_al_tesauro_y_sale_de_la_coleccion():
    texto = C.TESAURO.read_text(encoding="utf-8")
    cand, tes = _grafos([_fila(estado="aprobado", broader="oficial-real")])
    c = URIRef(TES + "cargo/pregonero")
    assert (c, None, None) not in cand
    assert (c, SKOS.inScheme, URIRef(TES + "cargos")) in tes and (c, OWL.deprecated, None) not in tes
    assert tes.value(c, SKOS.broader) == URIRef(TES + "cargo/oficial-real")
    assert [d for d in tes.objects(c, SKOS.definition) if d.language == "es"]
    # solo cambia la sección generada: lo escrito a mano queda intacto
    _, nuevo = C.generar([_fila(estado="aprobado", broader="oficial-real")])
    assert C.sin_seccion(nuevo) == C.sin_seccion(texto)


def test_un_aprobado_no_puede_colgar_de_un_candidato_pendiente():
    padre = _fila(local="oficial-de-bandos", etiqueta="oficial de bandos")
    with pytest.raises(C.ErrorCandidatos, match="ya aprobado"):
        C.generar([padre, _fila(estado="aprobado", broader="oficial-de-bandos")])
    C.generar([padre, _fila(broader="oficial-de-bandos")])        # candidato bajo candidato: admitido


@pytest.fixture()
def copia(tmp_path, monkeypatch):
    """El script trabajando sobre copias del CSV y de los .ttl (no toca el repositorio)."""
    m = _script()
    for nombre, origen in (("CSV", m.CSV), ("TESAURO", m.TESAURO), ("CANDIDATOS", m.CANDIDATOS)):
        destino = tmp_path / origen.name
        shutil.copy(origen, destino)
        monkeypatch.setattr(m, nombre, destino)
    monkeypatch.setattr(m, "regenerar_formas_de_atributos", lambda: None)
    return m


def test_cli_proponer_aprobar_y_rechazar(copia, capsys):
    m = copia
    antes = len(m.leer())
    assert m.main(["--proponer", "cargos", "pregonero", "pregonero", "Oficial que publica los bandos.",
                   "--expediente", EXPEDIENTE_PILOTO, "--ejemplo", "UT99: «el pregonero»", "--por", "anotadora-x"]) == 0
    filas = m.leer()
    assert len(filas) == antes + 1 and filas[-1]["estado"] == "candidato" and filas[-1]["fecha"]
    c = URIRef(TES + "cargo/pregonero")
    g = rdflib.Graph().parse(m.CANDIDATOS)
    assert (esquema.COLECCION_CANDIDATOS, SKOS.member, c) in g

    assert m.main(["--aprobar", "cargos/pregonero"]) == 0
    assert (c, None, None) not in rdflib.Graph().parse(m.CANDIDATOS)
    assert (c, RDF.type, SKOS.Concept) in rdflib.Graph().parse(m.TESAURO)
    assert m.main(["--aprobar", "cargos/pregonero"]) == 1          # ya no es un candidato pendiente

    assert m.main(["--rechazar", "cargos/granadero", "--reemplazo", "soldado"]) == 0
    g = rdflib.Graph().parse(m.CANDIDATOS)
    gran = URIRef(TES + "cargo/granadero")
    assert (gran, OWL.deprecated, rdflib.Literal(True)) in g
    assert g.value(gran, DCTERMS.isReplacedBy) == URIRef(TES + "cargo/soldado")
    capsys.readouterr()


def test_cli_proponer_sin_ejemplo_no_escribe_nada(copia, capsys):
    m = copia
    antes = m.CSV.read_text(encoding="utf-8")
    assert m.main(["--proponer", "cargos", "pregonero", "pregonero", "Oficial que publica los bandos.",
                   "--expediente", EXPEDIENTE_PILOTO]) == 1
    assert "falta «ejemplo»" in capsys.readouterr().err
    assert m.CSV.read_text(encoding="utf-8") == antes


# ─────────────── (d) los registros: candidato = aviso; retirado = error ───────────────
def _registro(ident: str) -> dict:
    for ruta in corpus.rutas_registros(EXPEDIENTE_PILOTO):
        for linea in ruta.read_text(encoding="utf-8").splitlines():
            d = json.loads(linea)
            if d["id"] == ident:
                d.pop("tipo_registro")
                return d
    raise KeyError(ident)


def test_los_registros_usan_candidatos_y_el_lote_lo_avisa():
    lote = corpus.cargar(EXPEDIENTE_PILOTO)
    assert not lote.errores
    assert lote.afirmaciones["A-UT04-201"].valor.concepto == "granadero"
    assert lote.menciones["M-UT05-208"].tipo_entidad == "real-audiencia"
    assert ("cargos", "granadero") in lote.afirmaciones["A-UT04-201"].candidatos_usados()
    assert any("A-UT04-201" in a and "granadero" in a for a in lote.avisos)
    assert any("M-UT05-208" in a and "real-audiencia" in a for a in lote.avisos)


def test_un_concepto_retirado_es_error_y_dice_su_reemplazo(monkeypatch):
    monkeypatch.setattr(esquema, "retirados", lambda esq: {"entidades": {"carcel": "edificio"},
                                                           "cargos": {"sargento": None}}.get(esq, {}))
    m = _registro("M-UT01-205")
    assert m["tipo_entidad"] == "carcel"
    with pytest.raises(ValueError, match=r"RETIRADO de tes:entidades.*use 'edificio'"):
        esquema.Mencion(**m)
    a = _registro("A-UT01-201")
    assert a["valor"] == {"concepto": "sargento"} or a["valor"]["concepto"] == "sargento"
    with pytest.raises(ValueError, match=r"'sargento' es un concepto RETIRADO de tes:cargos.*no tiene reemplazo"):
        esquema.Afirmacion(**a)
    with pytest.raises(ValueError, match="RETIRADO de tes:cargos"):
        esquema.Reconstruccion(id="R-x", tipo="cargo", etiqueta="x", titular="R-y", cargo="sargento",
                               premisas=[f"{EXPEDIENTE_PILOTO}:A-UT01-201"], creencia="probable",
                               argumento="argumento de prueba suficientemente largo", autor="x", fecha="2026-11-14")


def test_un_retirado_no_esta_en_la_lista_cerrada(tmp_path, monkeypatch):
    """Un candidato rechazado sigue en candidatos.ttl (su IRI no se borra), pero el esquema ya no lo ofrece."""
    filas = [dict(f, estado="rechazado", reemplazado_por="soldado") if f["local"] == "granadero" else f
             for f in C.leer()]
    ruta = tmp_path / "candidatos.ttl"
    ruta.write_text(C.generar(filas)[0], encoding="utf-8")
    monkeypatch.setattr(esquema, "CANDIDATOS", ruta)
    esquema._tesauro.cache_clear()
    try:
        assert "granadero" not in esquema.conceptos("cargos")
        assert esquema.retirados("cargos") == {"granadero": "soldado"}
        assert "granadero" not in esquema.candidatos("cargos")
    finally:
        monkeypatch.undo()
        esquema._tesauro.cache_clear()
    assert "granadero" in esquema.conceptos("cargos")


# ─────────────── (e) SHACL y consulta con nombre ───────────────
def _usos_esperados() -> int:
    lote = corpus.cargar(EXPEDIENTE_PILOTO)
    return sum(len(r.candidatos_usados())
               for r in [*lote.piezas.values(), *lote.menciones.values(), *lote.afirmaciones.values()])


def test_la_consulta_candidatos_en_uso_cuenta_los_mismos_usos_que_los_registros():
    filas = consulta.consultar("candidatos_en_uso", consulta.consultable(dataset()))
    assert filas and all(f["etiqueta"] and f["esquema"].startswith(TES) for f in filas)
    assert sum(int(f["usos"]) for f in filas) == _usos_esperados()
    cargos = consulta.consultar("candidatos_en_uso", consulta.consultable(dataset()), esquema=TES + "cargos")
    assert {f["concepto"] for f in cargos} >= {TES + "cargo/granadero"}
    assert all(f["esquema"] == TES + "cargos" for f in cargos)


def test_los_avisos_shacl_son_los_usos_de_candidatos_y_no_impiden_conformar():
    conforma, resultados, _ = validacion.shacl(union(), con_ontologias=True)
    assert conforma
    avisos = validacion.avisos(resultados)
    assert len(avisos) == _usos_esperados() > 0
    assert all("candidato" in mensaje for _, _, mensaje in avisos)
    assert "granadero" in validacion.resumen_avisos(resultados)


# ─────────────── (f) nada usa un concepto retirado ───────────────
def test_ningun_registro_ni_reconstruccion_usa_un_concepto_retirado():
    voc = esquema.grafo_tesauro()
    retirados = {c for c in voc.subjects(OWL.deprecated, None) if any(bool(o) for o in voc.objects(c, OWL.deprecated))}
    usados = {x for t in union() for x in t if isinstance(x, URIRef) and str(x).startswith(TES)}
    assert not usados & retirados, sorted(usados & retirados)
    # y en los registros planos (antes de mapear): ningún concepto fuera de las listas vigentes
    lote = corpus.cargar(EXPEDIENTE_PILOTO)
    for r in [*lote.piezas.values(), *lote.menciones.values(), *lote.afirmaciones.values()]:
        for esq, c in r.conceptos_usados():
            assert c in esquema.conceptos(esq) and c not in esquema.retirados(esq), (r.id, esq, c)
    from laad import mapeo
    for r in mapeo.cargar_reconstrucciones(RECONSTRUCCIONES):
        for esq, c in r.conceptos_usados():
            assert c in esquema.conceptos(esq) and c not in esquema.retirados(esq), (r.id, esq, c)
