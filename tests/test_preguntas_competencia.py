"""Pruebas de aceptación: cada pregunta de competencia respondida por el grafo (docs/B_preguntas_competencia.md).

Las aserciones fijan las respuestas PROVISIONALES del modelador; cuando el historiador fije las suyas
(docs/B_respuestas_referencia.csv) estas pruebas deben actualizarse para comparar contra ellas.
"""
import pytest

from laad import preguntas as P
from laad.consulta import consultar

FORMAS_ESPERADAS = {"PC09": "DISPUTA", "PC10": "DISPUTA", "PC11": "DISPUTA", "PC12": "NC", "PC13": "NC",
                    "PC14": "DISPUTA"}


@pytest.mark.parametrize("pc,forma", sorted(FORMAS_ESPERADAS.items()))
def test_las_seis_preguntas_de_disputa_o_silencio(pc, forma):
    assert P.PREGUNTAS[pc]().forma == forma


def test_toda_pregunta_tiene_funcion():
    assert sorted(P.PREGUNTAS) == [f"PC{i:02d}" for i in range(1, 21)]


def test_pc01_orden_y_secuencia():
    r = P.pc01()
    assert "33 piezas" in r.resumen
    sec = {(s["p1"], s["p2"]) for s in consultar("control_secuencia")}
    assert ("P06", "P07") in sec      # F1: vista fiscal anterior al escrito
    assert ("P08", "P09") in sec      # F2: ratificación anterior al decreto
    assert ("P23", "P27") in sec      # F5: informe del cura posterior al informe que lo cita
    assert ("P31", None) in sec       # F6: 1810


def test_pc05_grafias_sin_fusionar_en_capa_2():
    r = P.pc05()
    textos = {l.split("«")[1].split("»")[0] for l in r.extra}
    assert {"Manuel Guamanchoque", "MANUEL HUANCACHOQQUE", "guasscachoque", "Manuel Guancoichoque"} <= textos


def test_pc08_mismo_testigo_agosto_y_septiembre():
    r = P.pc08("cano")
    tipos = {f["tipoAct"] for f in r.afirmaciones}
    assert tipos == {"certificación", "declaración jurada"}


def test_pc09_cano_afirma_y_niega_coronel():
    r = P.pc09()
    pol = {(f["pieza"], f["pol"]) for f in r.afirmaciones}
    assert ("P01", "afirma") in pol and ("P18", "niega") in pol and ("P04", "afirma") in pol
    assert all(f["valorLabel"] == "coronel (de Túpac Amaru)" for f in r.afirmaciones)
    assert all(f["cita"] and f["tramo"] for f in r.afirmaciones)
    assert r.reconstrucciones and r.reconstrucciones[0]["creencia"] == "probable"


def test_pc10_redaccion_disputada_y_firma_negada():
    r = P.pc10()
    assert {"P04", "P05"} <= {f["sujetoLabel"] for f in r.afirmaciones}
    assert any("P04" in e and "Fernando Orue" in e for e in r.extra)


def test_pc11_dos_duraciones():
    r = P.pc11()
    assert {f["valorLabel"] for f in r.afirmaciones} == {"dos días", "esa misma noche ... al otro dia por la tarde"}


def test_pc12_y_pc13_no_lo_dice_pero_muestra_evidencia():
    assert any("desglose" in e.lower() or "Nota de desglose" in e for e in P.pc12().extra)
    assert P.pc13().afirmaciones and all(f["atrLabel"] == "ordena o manda" for f in P.pc13().afirmaciones)


def test_pc14_al_menos_cinco_horas():
    r = P.pc14()
    horas = {f["valorLabel"] for f in r.afirmaciones if f["atrLabel"].startswith("fecha")}
    assert len(horas) >= 5


def test_pc16_resolucion_es_afirmacion_no_hecho():
    r = P.pc16()
    assert r.afirmaciones and {f["fuerza"] for f in r.afirmaciones} <= {"dictaminadora", "resolutiva"}
    assert any(f["atrLabel"].startswith("veracidad") and f["valorLabel"] == "menos conforme a la verdad"
               for f in r.afirmaciones)


def test_pc19_reconstrucciones_en_competencia():
    r = P.pc19()
    assert {x["creencia"] for x in r.reconstrucciones} == {"probable", "posible"}


def test_pc20_procedencia_declara_falta_de_validacion_humana():
    r = P.pc20()
    assert any("claude-opus-5-5" in l and "sha256:" in l for l in r.extra)
    assert any("NO REGISTRADA" in l for l in r.extra)


def test_todas_las_respuestas_con_afirmaciones_llevan_cita_y_tramo():
    for pc, f in P.PREGUNTAS.items():
        for fila in f().afirmaciones:
            assert fila["cita"] and fila["tramo"], (pc, fila["aid"])
