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


def test_ontologia_y_tesauro_salen_del_grafo_real():
    g = _datos()
    rdf = g["rdf"]
    # las tripletas de la afirmación de Cano viven en el grafo nombrado de la capa 3, con la polaridad «niega»
    filas = rdf["r"]["A-UT11-004"]
    capa3 = [(rdf["grafos"][gi], po) for gi, s, po in filas if s.endswith("/afirmacion/A-UT11-004")]
    assert capa3 and all("/afirmaciones/" in grafo for grafo, _ in capa3)
    assert ["crm:P2_has_type", "pol:niega"] in capa3[0][1]
    assert ["rdf:type", "crm:E13_Attribute_Assignment"] in capa3[0][1]
    # la reconstrucción separa proposición y argumento en dos grafos de la capa 4
    grafos_r = {rdf["grafos"][gi] for gi, _, _ in rdf["r"]["R-chuquitapa"]}
    assert {"g:reconstruccion/R-chuquitapa", "g:argumentacion/R-chuquitapa"} <= grafos_r
    assert "_procedencia" in rdf["r"]
    # el tesauro: 12 esquemas; 164 aprobados + 26 candidatos (las mismas cifras que docs/cifras.md)
    tes = g["tesauro"]
    conceptos = [c for e in tes for c in e["conceptos"]]
    assert len(tes) == 12 and len(conceptos) == 190
    assert sum(c["candidato"] for c in conceptos) == g["cifras"]["candidatos"] == 26
    cano = {c["id"]: c for c in conceptos}
    assert cano["pol:niega"]["usos"] == g["cifras"]["negaciones"]
    assert any(r.startswith("fza:") for c in conceptos if c["id"].startswith("act:") for r in c["relacionado"])
    # las reglas SHACL con nombre, cada una con su explicación
    assert len(g["formas"]) == 18 and all(f["id"].startswith("ohac:") and f["explica"] for f in g["formas"])


def test_ejemplo_en_tres_niveles_solo_dibuja_tripletas_que_existen():
    # visor.py ya aborta si una arista no está en el grafo ni en el tesauro; aquí se fija el reparto por niveles
    ej = _datos()["ejemplo"]
    nivel = {n["id"]: n["nivel"] for n in ej["nodos"]}
    assert {"onto", "datos", "tes"} == set(nivel.values())
    por_fuente = {a["fuente"].startswith("g:") for a in ej["aristas"]}
    assert por_fuente == {True, False}                         # unas del grafo, otras del tesauro
    for a in ej["aristas"]:
        if a["p"] == "rdf:type":                                 # «es un»: de los datos a la ontología
            assert nivel[a["s"]] == "datos" and nivel[a["o"]] == "onto"
        if nivel[a["s"]] == "tes":                               # la red propia del tesauro (SKOS) vive en tesauro.ttl
            assert a["p"].startswith("skos:") and a["fuente"] == "ontologia/tesauro.ttl"
    niega = [a for a in ej["aristas"] if a["o"] == "pol:niega"][0]
    assert niega["s"].endswith("A-UT11-004") and "/afirmaciones/" in niega["fuente"]
