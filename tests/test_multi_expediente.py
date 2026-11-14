"""Corpus con VARIOS expedientes en un mismo Dataset: el expediente piloto (real) y un segundo SINTÉTICO.

El segundo expediente (tests/_sintetico.py) es texto inventado para la prueba, no una fuente; sus ids de registro
repiten a propósito ids del piloto. Se comprueba que: (a) ningún grafo de las capas 1–3 se comparte entre
expedientes; (b) una reconstrucción (capa 4, común) puede reunir una mención de cada uno y el conjunto conforma
SHACL; (c) una referencia sin calificar o inexistente es un error claro; (d) todo grafo de las capas 1–3 tiene
procedencia; (e) las consultas con nombre se pueden restringir a un expediente; (f) se escribe un archivo por
expediente y uno común.
"""
from __future__ import annotations

import shutil
from types import SimpleNamespace

import pytest
from rdflib.namespace import DCTERMS, PROV, RDF

from laad import consulta, corpus, fuente, mapeo, validacion
from laad.esquema import Reconstruccion
from laad.preguntas import EXPEDIENTE_PILOTO

from ._sintetico import EXP_SINTETICO, instalar

# Reconstrucción SINTÉTICA (no es una hipótesis histórica): une una mención real del piloto con una del sintético.
R_MIXTA = dict(id="R-prueba-sintetica-mixta", tipo="identidad", etiqueta="Persona de prueba (SINTÉTICA)",
               menciones=[f"{EXPEDIENTE_PILOTO}:M-UT01-003", f"{EXP_SINTETICO}:M-UT01-002"], creencia="improbable",
               argumento="Reconstrucción SINTÉTICA para probar el enlace entre expedientes; no es una hipótesis.",
               autor="prueba", fecha="2026-11-14")
CAPAS_PROPIAS = ("documento", "texto", "afirmaciones")


@pytest.fixture(scope="module")
def doble(tmp_path_factory):
    """Dataset del corpus piloto + sintético, construido UNA vez para todo el módulo."""
    base = tmp_path_factory.mktemp("corpus")
    manifiestos = base / "expedientes"
    manifiestos.mkdir()
    shutil.copy(fuente.MANIFIESTOS / f"{EXPEDIENTE_PILOTO}.json", manifiestos)   # sus rutas son relativas a la raíz
    instalar(base, manifiestos)
    mp = pytest.MonkeyPatch()
    mp.setattr(fuente, "MANIFIESTOS", manifiestos)
    try:
        exps = corpus.expedientes()
        assert exps == sorted([EXPEDIENTE_PILOTO, EXP_SINTETICO])
        lotes = {e: corpus.cargar(e) for e in exps}
        assert not any(l.errores for l in lotes.values())
        recs = mapeo.cargar_reconstrucciones(corpus.RECONSTRUCCIONES) + [Reconstruccion(**R_MIXTA)]
        ds = corpus.construir(lotes=lotes, reconstrucciones=recs)
        yield SimpleNamespace(ds=ds, lotes=lotes, base=base)
    finally:
        mp.undo()


def _grafos(ds):
    return {g.identifier: g for g in ds.graphs() if len(g)}


def test_a_ningun_grafo_de_capas_1_a_3_se_comparte(doble):
    por_exp: dict[str, set[str]] = {}
    for gid, g in _grafos(doble.ds).items():
        exp = mapeo.expediente_de_grafo(gid)
        if exp is None:
            continue
        por_exp.setdefault(exp, set()).add(str(gid)[len(str(mapeo.G)) + len(exp) + 1:].split("/")[0])
        # todo recurso propio de un expediente (id/<exp>/…) descrito en el grafo es de ESE expediente
        otro = EXP_SINTETICO if exp == EXPEDIENTE_PILOTO else EXPEDIENTE_PILOTO
        ajenos = [s for s in set(g.subjects()) if str(s).startswith(f"{mapeo.ID}{otro}/")]
        assert not ajenos, (gid, ajenos[:3])
    assert por_exp == {EXPEDIENTE_PILOTO: set(CAPAS_PROPIAS), EXP_SINTETICO: set(CAPAS_PROPIAS)}
    # las clases de las capas 1–3 no aparecen en ningún grafo sin expediente en el nombre
    for gid, g in _grafos(doble.ds).items():
        if mapeo.expediente_de_grafo(gid) is None:
            for clase in (mapeo.CRM.E65_Creation, mapeo.PICOM.PersonObservation, mapeo.CRM.E13_Attribute_Assignment):
                assert (None, RDF.type, clase) not in g, (gid, clase)


def test_a_ids_repetidos_no_colisionan(doble):
    """M-UT01-001 existe en los dos expedientes: son dos recursos, cada uno en el grafo de texto del suyo."""
    for exp in (EXPEDIENTE_PILOTO, EXP_SINTETICO):
        assert "M-UT01-001" in doble.lotes[exp].menciones
        m = mapeo.mencion_iri("M-UT01-001", exp)
        donde = {mapeo.expediente_de_grafo(gid) for gid, g in _grafos(doble.ds).items() if (m, RDF.type, None) in g}
        assert donde == {exp}


def test_b_reconstruccion_que_une_dos_expedientes(doble):
    g = doble.ds.graph(mapeo.G["reconstruccion/R-prueba-sintetica-mixta"])
    nodo = mapeo.ID["persona/prueba-sintetica-mixta"]
    assert (nodo, RDF.type, mapeo.PICOM.PersonReconstruction) in g
    assert set(g.objects(nodo, PROV.wasDerivedFrom)) == {
        mapeo.mencion_iri("M-UT01-003", EXPEDIENTE_PILOTO), mapeo.mencion_iri("M-UT01-002", EXP_SINTETICO)}
    assert mapeo.expediente_de_grafo(g.identifier) is None      # la capa 4 no es de ningún expediente


def test_b_el_corpus_doble_conforma_shacl(doble):
    conforma, _, texto = validacion.shacl(mapeo.union(doble.ds), con_ontologias=True)
    assert conforma, texto[:3000]


def test_c_referencia_sin_calificar_es_error_en_el_esquema():
    with pytest.raises(ValueError, match="sin calificar"):
        Reconstruccion(**{**R_MIXTA, "menciones": ["M-UT01-003"]})
    with pytest.raises(ValueError, match="sin calificar"):
        Reconstruccion(**{**R_MIXTA, "premisas": ["A-UT11-004"]})
    with pytest.raises(ValueError, match="mal formada"):          # una afirmación no es una mención
        Reconstruccion(**{**R_MIXTA, "menciones": [f"{EXPEDIENTE_PILOTO}:A-UT11-004"]})


@pytest.mark.parametrize("cambio,mensaje", [
    ({"menciones": ["M-UT01-003"]}, "sin calificar"),                                    # sin expediente
    ({"menciones": [f"{EXPEDIENTE_PILOTO}:M-UT99-999"]}, "no existe mencion M-UT99-999"),  # mención inexistente
    ({"menciones": ["zz-0-0:M-UT01-003"]}, "no está cargado"),                            # expediente desconocido
    ({"premisas": [f"{EXP_SINTETICO}:A-UT99-999"]}, "no existe afirmacion A-UT99-999"),
    ({"tipo": "hecho", "menciones": [f"{EXP_SINTETICO}:H-p01-inexistente"]}, "no existe hecho"),
])
def test_c_referencia_invalida_es_error_al_mapear(doble, cambio, mensaje):
    """El mapeo vuelve a comprobarlo aunque el registro no haya pasado por el esquema (model_construct)."""
    r = Reconstruccion.model_construct(**{**R_MIXTA, "premisas": [], **cambio})
    with pytest.raises(ValueError, match=mensaje) as e:
        mapeo.capa_reconstruccion(mapeo.nuevo_dataset(), [r], doble.lotes)
    assert str(e.value).startswith("R-prueba-sintetica-mixta")


def test_c_reconstruccion_de_un_expediente_no_cargado(doble):
    """Construir solo el sintético con las reconstrucciones reales (que citan el piloto) es un error, no un grafo
    con referencias colgantes."""
    with pytest.raises(ValueError, match="no está cargado"):
        corpus.construir([EXP_SINTETICO], catalogo=None)


def test_d_todo_grafo_de_capas_1_a_3_tiene_procedencia(doble):
    pg = doble.ds.graph(mapeo.G.procedencia)
    propios = [gid for gid in _grafos(doble.ds) if mapeo.expediente_de_grafo(gid)]
    assert len(propios) == 6
    actividades = {}
    for gid in propios:
        exp = mapeo.expediente_de_grafo(gid)
        acts = list(pg.objects(gid, PROV.wasGeneratedBy))
        assert len(acts) == 1, gid
        assert str(acts[0]).startswith(f"{mapeo.ID}actividad/{exp}/"), acts
        assert list(pg.objects(gid, PROV.wasDerivedFrom)) == [mapeo.transcripcion_iri(exp)]
        assert (gid, PROV.wasAttributedTo, None) in pg and (gid, DCTERMS.type, None) in pg
        actividades[gid] = acts[0]
        # cada actividad usa UNA transcripción: la de su expediente
        assert list(pg.objects(acts[0], PROV.used)) == [mapeo.transcripcion_iri(exp)]
    # y también los grafos comunes (capa 4, argumentación, catálogo)
    for gid in _grafos(doble.ds):
        if gid != mapeo.G.procedencia and not str(gid).startswith("urn:"):
            assert (gid, DCTERMS.type, None) in pg, gid


def test_e_consultas_restringidas_a_un_expediente(doble):
    ds = consulta.consultable(doble.ds)
    # (con ?atributo para que la consulta sea rápida: «tiene-condicion» se afirma en los dos expedientes)
    atr = consulta.atributo("tiene-condicion")
    todas = consulta.consultar("afirmaciones", ds, atributo=atr)
    por_exp = {}
    for exp in (EXPEDIENTE_PILOTO, EXP_SINTETICO):
        filas = consulta.consultar("afirmaciones", ds, atributo=atr, expediente=consulta.expediente(exp))
        assert filas and all(f["a"].startswith(f"{mapeo.ID}{exp}/afirmacion/") for f in filas), exp
        assert {f["aid"] for f in filas} == {a.id for a in doble.lotes[exp].afirmaciones.values()
                                             if a.atributo == "tiene-condicion"}
        por_exp[exp] = {f["a"] for f in filas}
    assert por_exp[EXPEDIENTE_PILOTO] | por_exp[EXP_SINTETICO] == {f["a"] for f in todas}
    assert not por_exp[EXPEDIENTE_PILOTO] & por_exp[EXP_SINTETICO]
    assert por_exp[EXP_SINTETICO] == {str(mapeo.afirmacion_iri("A-UT02-001", EXP_SINTETICO))}
    sint = consulta.expediente(EXP_SINTETICO)
    assert {f["pieza"] for f in consulta.consultar("piezas", ds, expediente=sint)} == {"P00", "P01", "P02"}
    assert len(consulta.consultar("piezas", ds, expediente=consulta.expediente(EXPEDIENTE_PILOTO))) \
        == len(doble.lotes[EXPEDIENTE_PILOTO].piezas)
    assert {f["texto"] for f in consulta.consultar("participantes", ds, expediente=sint)} \
        == {"El comun del ayllu Sintetico", "Pedro Prueba"}
    mixta = mapeo.ID["persona/prueba-sintetica-mixta"]
    assert {(f["exp"], f["mid"]) for f in consulta.consultar("menciones_de", ds, filtroEntidad=mixta)} \
        == {(EXPEDIENTE_PILOTO, "M-UT01-003"), (EXP_SINTETICO, "M-UT01-002")}
    assert [(f["exp"], f["mid"]) for f in consulta.consultar("menciones_de", ds, filtroEntidad=mixta, expediente=sint)] \
        == [(EXP_SINTETICO, "M-UT01-002")]
    rec = [r for r in consulta.consultar("reconstrucciones", ds) if r["entidad"] == str(mixta)]
    assert set(rec[0]["menciones"].split()) == {f"{EXPEDIENTE_PILOTO}/mencion/M-UT01-003",
                                                f"{EXP_SINTETICO}/mencion/M-UT01-002"}


def test_f_un_archivo_por_expediente_y_uno_comun(doble, tmp_path):
    (tmp_path / "viejo.trig").write_text("", encoding="utf-8")      # salida de un expediente que ya no existe
    escritos = corpus.escribir(doble.ds, tmp_path)
    assert sorted(p.name for p in tmp_path.iterdir()) == sorted(
        f"{n}.{ext}" for n in (EXPEDIENTE_PILOTO, EXP_SINTETICO, corpus.COMUN) for ext in ("trig", "nq"))
    assert [p.stem for p in escritos] == sorted([EXPEDIENTE_PILOTO, EXP_SINTETICO, corpus.COMUN])
    for exp in (EXPEDIENTE_PILOTO, EXP_SINTETICO):
        grafos = {l.rsplit(" ", 2)[1] for l in (tmp_path / f"{exp}.nq").read_text(encoding="utf-8").splitlines()}
        assert grafos and all(g.startswith(f"<{mapeo.G}{exp}/") for g in grafos), grafos
    comun = {l.rsplit(" ", 2)[1] for l in (tmp_path / "comun.nq").read_text(encoding="utf-8").splitlines()}
    assert not any(mapeo.expediente_de_grafo(g.strip("<>")) for g in comun)
    nq = (tmp_path / "comun.nq").read_text(encoding="utf-8").splitlines()
    assert nq == sorted(nq)                                          # forma canónica: ordenada
    leido = consulta.dataset(tmp_path)
    assert sum(len(g) for g in leido.graphs() if g.identifier != consulta.G_TESAURO) \
        == sum(len(g) for g in doble.ds.graphs())
