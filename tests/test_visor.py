"""Visor del grafo (scripts/visor.py): un HTML autónomo cuyos datos respetan la regla de identidad del harness."""
import json
import pathlib
import runpy

RAIZ = pathlib.Path(__file__).resolve().parents[1]


def _datos():
    modulo = runpy.run_path(str(RAIZ / "scripts" / "visor.py"))
    assert modulo["main"]() == 0
    html = (RAIZ / "visor" / "index.html").read_text(encoding="utf-8")
    assert "/*DATOS_DEL_GRAFO*/" not in html                    # la marca de la plantilla se sustituyó
    crudo = html.split("window.GRAFO = ", 1)[1].split(";</script>", 1)[0]
    assert "</" not in crudo                                     # ninguna cita puede cerrar el <script>
    return json.loads(crudo.replace("<\\/", "</"))


def test_visor_genera_nodos_relaciones_y_afirmaciones_coherentes():
    g = _datos()
    nodos = {n["id"]: n for n in g["nodos"]}
    assert nodos["R-chuquitapa"]["etiqueta"] == "Persona"
    assert all(r["source"] in nodos and r["target"] in nodos for r in g["relaciones"])
    assert {r["tipo"] for r in g["relaciones"]} == {"AFIRMA", "NIEGA", "TIENE_VALOR", "HIPOTESIS_DE", "INTERVIENE_EN"}
    a = g["afirmaciones"]["A-UT11-004"]                         # Cano niega que fuera coronel
    assert a["niega"] and a["disputa"] and "no coronel" in a["cita"]
    niega = [r for r in g["relaciones"] if "A-UT11-004" in r["afirmaciones"] and r["tipo"] == "NIEGA"]
    assert len(niega) == 1 and niega[0]["rotulo"] == "ejerce-cargo"


def test_las_menciones_con_hipotesis_rivales_no_se_fusionan():
    g = _datos()
    rivales = [n for n in g["nodos"] if n["etiqueta"] == "Mención" and len(n.get("rivales", [])) > 1]
    assert rivales, "debería haber menciones reclamadas por varias reconstrucciones"
    for n in rivales:
        hip = {r["target"] for r in g["relaciones"] if r["source"] == n["id"] and r["tipo"] == "HIPOTESIS_DE"}
        assert hip == set(n["rivales"])
