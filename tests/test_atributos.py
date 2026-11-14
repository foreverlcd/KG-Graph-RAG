"""Dominio y rango de cada atributo (datos/atributos.csv), comprobado dos veces: en los registros
(laad.esquema / laad.registros, con error que nombra el atributo y lo que admite) y en el grafo
(ontologia/formas_atributos.ttl, generado por scripts/atributos.py; sus casos negativos, uno por atributo y lado,
están en tests/test_formas_negativas.py).
"""
from __future__ import annotations

import importlib.util
import json

import pytest
import rdflib
from rdflib import RDF, Literal, URIRef
from rdflib.namespace import SH

from laad import corpus, esquema, mapeo as M, registros
from laad.registros import Lote

from ._fixtures import EXPEDIENTE_PILOTO, RAIZ

OHAC = rdflib.Namespace("https://w3id.org/laad/ohac#")


def _script():
    spec = importlib.util.spec_from_file_location("atributos", RAIZ / "scripts/atributos.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


S = _script()


# ─────────────── el CSV y lo generado ───────────────
def test_todo_atributo_vigente_tiene_fila_incluidos_los_candidatos():
    filas = esquema.dominio_rango()
    assert set(filas) == set(esquema.conceptos("atributos"))
    assert esquema.candidatos("atributos") <= set(filas)


def test_los_tipos_de_concepto_del_csv_tienen_esquema_en_el_tesauro():
    for atr, (_, valor) in esquema.dominio_rango().items():
        assert ("concepto" in valor) == bool(esquema.esquemas_admitidos(atr)), atr


def test_formas_de_atributos_al_dia_con_el_csv_y_el_tesauro():
    assert S.SALIDA.read_text(encoding="utf-8") == S.texto_actual(), "ejecutar scripts/atributos.py"


def test_hay_una_forma_por_atributo():
    g = rdflib.Graph().parse(S.SALIDA)
    formas = {str(f) for f in g.subjects(RDF.type, SH.NodeShape)}
    assert formas == {S.nombre_forma(a) for a in esquema.conceptos("atributos")}


def test_las_clases_de_cada_tipo_son_las_que_emite_el_mapeo():
    assert S.clases_rdf("persona", "edad") == [str(M.PICOM.PersonObservation)]
    assert S.clases_rdf("lugar", "edad") == [str(M.ROAR.LocationObservation)]
    assert S.clases_rdf("grupo", "edad") == S.clases_rdf("cosa", "edad") == [str(M.ROAR.Observation)]
    assert S.clases_rdf("literal", "edad") == [str(M.CRM.E33_Linguistic_Object)]
    assert S.clases_rdf("literal", "duracion") == [str(M.CRM["E52_Time-Span"])]
    assert S.clases_rdf("concepto", "ejerce-cargo", ("cargos",)) == ["https://w3id.org/laad/tesauro/cargos"]
    with pytest.raises(S.ErrorAtributos, match="dct:conformsTo"):
        S.clases_rdf("concepto", "edad")


def test_el_generador_exige_fila_para_todo_atributo_del_tesauro():
    filas = {"edad": (frozenset({"persona"}), frozenset({"literal"}))}
    with pytest.raises(S.ErrorAtributos, match=r"sin fila.*\['motivo'\]"):
        S.generar(filas, {"edad", "motivo"}, set(), {})
    with pytest.raises(S.ErrorAtributos, match=r"no están vigentes.*\['edad'\]"):
        S.generar(filas, {"motivo"}, {"motivo"}, {})


def test_un_atributo_candidato_sin_fila_solo_avisa_en_shacl():
    """Forma de severidad sh:Warning: el grafo conforma, y cada afirmación que usa el atributo queda señalada."""
    from pyshacl import validate
    texto = S.generar({"edad": (frozenset({"persona"}), frozenset({"literal"}))}, {"edad", "apodo"}, {"apodo"}, {})
    formas = rdflib.Graph().parse(data=texto, format="turtle")
    assert (URIRef(S.nombre_forma("apodo")), SH.severity, SH.Warning) in formas
    g = rdflib.Graph()
    a, p, v = (URIRef(f"https://w3id.org/laad/id/prueba/{x}") for x in "apv")
    g.add((a, RDF.type, M.CRM.E13_Attribute_Assignment))
    g.add((a, M.CRM.P177_assigned_property_of_type, M.ATR.apodo))
    g.add((a, M.CRM.P140_assigned_attribute_to, p))
    g.add((a, M.CRM.P141_assigned, v))
    g.add((v, M.CRM.P190_has_symbolic_content, Literal("el Tuerto")))
    conforma, res, _ = validate(g, shacl_graph=formas, inference="none", advanced=True, allow_warnings=True)
    assert conforma
    assert [res.value(r, SH.focusNode) for r in res.subjects(SH.resultSeverity, SH.Warning)] == [a]
    assert not list(res.subjects(SH.resultSeverity, SH.Violation))


def test_csv_mal_formado_es_error(tmp_path):
    ruta = tmp_path / "atributos.csv"
    ruta.write_text("atributo,sujeto,valor,nota\nedad,persona|animal,literal,\n", encoding="utf-8")
    with pytest.raises(ValueError, match="edad: sujeto"):
        esquema.leer_dominio_rango(ruta)
    ruta.write_text("atributo,sujeto,valor,nota\nedad,persona,literal,\nedad,persona,literal,\n", encoding="utf-8")
    with pytest.raises(ValueError, match="repetido"):
        esquema.leer_dominio_rango(ruta)
    ruta.write_text("atributo,sujeto,valor,nota\nedad,literal,literal,\n", encoding="utf-8")
    with pytest.raises(ValueError, match="edad: sujeto"):       # un literal nunca es sujeto
        esquema.leer_dominio_rango(ruta)


# ─────────────── validación de los registros ───────────────
def _registro(ident: str) -> dict:
    for ruta in corpus.rutas_registros(EXPEDIENTE_PILOTO):
        for linea in ruta.read_text(encoding="utf-8").splitlines():
            d = json.loads(linea)
            if d["id"] == ident:
                d.pop("tipo_registro")
                return d
    raise KeyError(ident)


def _con_atributo(atributo: str) -> dict:
    """Un registro real del piloto con ese atributo (su cita ya es literal)."""
    lote = corpus.cargar(EXPEDIENTE_PILOTO)
    return _registro(next(a.id for a in lote.afirmaciones.values() if a.atributo == atributo))


def test_el_expediente_piloto_cumple_dominio_y_rango():
    lote = corpus.cargar(EXPEDIENTE_PILOTO)
    assert not lote.errores
    assert not [a for a in lote.avisos if "dominio ni rango" in a]


@pytest.mark.parametrize("atributo, cambio, mensaje", [
    # el error nombra el atributo, lo que se le dio y lo que admite
    ("edad", {"sujeto": {"pieza": "P01"}}, r"el atributo edad no admite como sujeto pieza; admite: persona"),
    ("edad", {"valor": {"pieza": "P01"}}, r"el atributo edad no admite como valor pieza; admite: literal"),
    ("firmo", {"sujeto": {"hecho": "H-p11-x"}}, r"el atributo firmo no admite como sujeto hecho; admite: pieza"),
    ("fecha-del-hecho", {"sujeto": {"pieza": "P01"}}, r"fecha-del-hecho no admite como sujeto pieza; admite: hecho"),
    ("se-conforma-con", {"valor": {"literal": "lo pedido"}}, r"se-conforma-con no admite como valor literal; admite: pieza"),
])
def test_sujeto_o_valor_de_tipo_no_admitido_es_error_en_el_esquema(atributo, cambio, mensaje):
    d = _con_atributo(atributo)
    esquema.Afirmacion(**d)                              # el registro real es válido
    with pytest.raises(ValueError, match=mensaje):
        esquema.Afirmacion(**{**d, **cambio})


def test_tiene_condicion_exige_concepto_no_literal():
    d = _con_atributo("tiene-condicion")
    with pytest.raises(ValueError, match=r"tiene-condicion no admite como valor literal; admite: concepto"):
        esquema.Afirmacion(**{**d, "valor": {"literal": "Oriundo de el"}})


def _lote_con(afirmacion: esquema.Afirmacion) -> Lote:
    real = corpus.cargar(EXPEDIENTE_PILOTO)
    lote = Lote(piezas=real.piezas, menciones=real.menciones, afirmaciones={afirmacion.id: afirmacion})
    registros._integridad(lote)
    return lote


def _mencion(clase: str, pieza: str | None = None) -> str:
    real = corpus.cargar(EXPEDIENTE_PILOTO)
    return next(m.id for m in real.menciones.values() if m.clase == clase and (pieza is None or m.pieza == pieza))


def test_la_clase_de_la_mencion_se_comprueba_con_el_lote():
    """El registro solo no sabe de qué clase es una mención: «dijo» con un LUGAR como sujeto pasa el esquema y
    lo rechaza la integridad del lote, que sí conoce la mención."""
    d = _con_atributo("dijo")
    a = esquema.Afirmacion(**{**d, "sujeto": {"mencion": _mencion("lugar")}})
    errores = _lote_con(a).errores
    assert any(f"{a.id}: el atributo dijo no admite como sujeto lugar; admite: persona, grupo" in e for e in errores), errores
    assert not _lote_con(esquema.Afirmacion(**d)).errores


def test_grupo_y_cosa_se_distinguen_en_los_registros():
    """En el grafo los dos son roar:Observation; en los registros «solicita» admite un grupo y no una cosa."""
    d = _con_atributo("solicita")
    con_cosa = esquema.Afirmacion(**{**d, "sujeto": {"mencion": _mencion("cosa")}})
    assert any("solicita no admite como sujeto cosa" in e for e in _lote_con(con_cosa).errores)
    con_grupo = esquema.Afirmacion(**{**d, "sujeto": {"mencion": _mencion("grupo")}})
    assert not [e for e in _lote_con(con_grupo).errores if "no admite" in e]


def test_filas_ampliadas_a_proposito_admiten_una_cosa():
    """«ordena» y «folio-de-pieza» admiten una cosa como sujeto (datos/atributos.csv, columna nota)."""
    filas = esquema.dominio_rango()
    assert "cosa" in filas["ordena"][0] and "cosa" in filas["folio-de-pieza"][0]
    lote = corpus.cargar(EXPEDIENTE_PILOTO)
    assert lote.menciones[lote.afirmaciones["A-UT10-514"].sujeto.mencion].clase == "cosa"


def test_atributo_candidato_sin_fila_es_aviso_y_atributo_del_tesauro_sin_fila_es_error(monkeypatch):
    d = _con_atributo("dijo")
    a = esquema.Afirmacion(**d)
    sin_dijo = {k: v for k, v in esquema.dominio_rango().items() if k != "dijo"}
    monkeypatch.setattr(esquema, "dominio_rango", lambda: sin_dijo)
    lote = _lote_con(a)
    assert any("el atributo dijo no tiene fila en datos/atributos.csv" in e for e in lote.errores)
    monkeypatch.setattr(esquema, "candidatos", lambda esq: frozenset({"dijo"}) if esq == "atributos" else frozenset())
    lote = _lote_con(a)
    assert not lote.errores
    assert any("atributo candidato dijo no tiene dominio ni rango" in x for x in lote.avisos)
