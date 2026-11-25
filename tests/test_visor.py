"""Visor del grafo (scripts/visor.py): los datos se generan y respetan la regla de identidad del harness."""
import json
import pathlib
import runpy

RAIZ = pathlib.Path(__file__).resolve().parents[1]


def _datos():
    modulo = runpy.run_path(str(RAIZ / "scripts" / "visor.py"))
    assert modulo["main"]() == 0
    texto = (RAIZ / "visor" / "datos.js").read_text(encoding="utf-8")
    return json.loads(texto.split("window.GRAFO = ", 1)[1].rstrip().rstrip(";"))


def test_visor_genera_nodos_aristas_y_afirmaciones_coherentes():
    g = _datos()
    nodos = {n["id"]: n for n in g["nodos"]}
    assert "R-chuquitapa" in nodos and nodos["R-chuquitapa"]["tipo"] == "reconstruccion"
    assert all(e["de"] in nodos and e["a"] in nodos for e in g["aristas"])
    a = g["afirmaciones"]["A-UT11-004"]                       # Cano niega que fuera coronel
    assert a["niega"] and a["disputa"] and "no coronel" in a["cita"]


def test_las_menciones_con_hipotesis_rivales_no_se_fusionan():
    g = _datos()
    rivales = [n for n in g["nodos"] if n["tipo"] == "mencion" and len(n.get("rivales", [])) > 1]
    assert rivales, "debería haber menciones reclamadas por varias reconstrucciones"
    ids = {n["id"] for n in g["nodos"]}
    for n in rivales:
        hip = {e["a"] for e in g["aristas"] if e["de"] == n["id"] and e["tipo"] == "hipotesis"}
        assert hip == set(n["rivales"]) and hip <= ids
