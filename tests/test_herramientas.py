"""Núcleo del harness de consulta (src/laad/herramientas.py) y su banco de pruebas (src/laad/evaluacion_harness.py):
buscador de nombres, validación de parámetros, verificación posterior de citas y las 20 PC alcanzadas por su plan."""
from __future__ import annotations

import inspect

import pytest

from laad import evaluacion_harness as E
from laad import herramientas as H
from laad.preguntas import PREGUNTAS

EXP = "cc-14-18"


def _ids(nombre: str, **kw) -> list[str]:
    return [c["id"] for c in H.buscar(nombre, **kw).filas]


# ───────────────────────── buscador ─────────────────────────

@pytest.mark.parametrize("nombre,esperado", [
    ("Huancachoque", "R-huancachoque"), ("Guancachoque", "R-huancachoque"), ("Mancachoque", "R-huancachoque"),
    ("Huancachoqe", "R-huancachoque"),
    ("Chuquitapa", "R-chuquitapa"), ("Chuquiitapa", "R-chuquitapa"), ("Choquetapa", "R-chuquitapa"),
    ("Chiquitas", "R-chiquitas"),
    ("Casorla", "R-martin-cazorla"), ("Martín Casorla", "R-martin-cazorla"), ("Cazorla", "R-martin-cazorla"),
    ("Agustin Baldez", "R-cura-valdes"),            # b/v y s/z
    ("Aillo Tinta", "R-ayllu-tinta"),               # y/i, ll
    ("Ayllu Uchu", "R-ayllu-ucho"),                 # o/u
    ("QUINONES", "R-quinones"),                     # mayúsculas, sin tilde
])
def test_variantes_graficas(nombre, esperado):
    assert esperado in _ids(nombre)


def test_el_nombre_exacto_sale_primero():
    assert _ids("Huancachoque", clase="persona")[0] == "R-huancachoque"
    assert _ids("Mancachoque", clase="persona")[0] == "R-huancachoque"
    assert _ids("Tinta", clase="lugar")[0] == "R-tinta"
    assert _ids("Isidro Cano")[0] == "R-cano"


def test_mayusculas_y_tildes_no_cuentan():
    assert set(_ids("ANDRÉS CHUQUITAPA")) == set(_ids("andres chuquitapa")) == set(_ids("Andrés Chuquitapa"))


def test_las_rivales_salen_todas_con_su_creencia():
    """Dos lecturas de «corregidor Don Andres ……» (P18): las dos son candidatas y cada una nombra a la otra como
    rival; el buscador no elige."""
    filas = {c["id"]: c for c in H.buscar("corregidor Don Andrés").filas}
    a, b = "R-don-andres-p18-es-reparaz", "R-don-andres-p18-es-chuquitapa"
    assert a in filas and b in filas
    assert filas[a]["creencia"] and filas[b]["creencia"]
    assert b in {r["id"] for r in filas[a]["rivales"]} and a in {r["id"] for r in filas[b]["rivales"]}
    assert all(r["creencia"] for r in filas[a]["rivales"])
    # Y la hipótesis del pariente homónimo sale junto a Chuquitapa, como candidata y como rival.
    ch = {c["id"]: c for c in H.buscar("Chuquitapa", clase="persona").filas}
    assert "R-chuquitapa-1780-pariente" in ch
    assert "R-chuquitapa-1780-pariente" in {r["id"] for r in ch["R-chuquitapa"]["rivales"]}


def test_nombre_inexistente_lista_vacia():
    for nombre in ("Napoleón Bonaparte", "Juan Bautista Pérez"):
        r = H.buscar(nombre)
        assert r.filas == [] and r.forma == "NC"


def test_menciones_sueltas():
    sueltas = [c for c in H.buscar("Chuquitapa").filas if c["candidato"] == "mención suelta"]
    assert sueltas
    for c in sueltas:
        assert c["id"].startswith(EXP + ":M-") and c["texto"] and c["pieza"] and c["tramo"] and c["cita"]
        assert c["texto"] in c["cita"]
        assert H.indice_menciones()[c["id"]]["reconstrucciones"] == []       # no enlazada a ninguna reconstrucción


def test_clase_y_expediente_filtran():
    assert all(c["tipo"] == "hecho" for c in H.buscar("prisión de Huancachoque", clase="hecho").filas)
    assert "R-prision" in _ids("prisión de Huancachoque", clase="hecho")
    assert _ids("Chuquitapa", expediente=EXP)
    with pytest.raises(H.ErrorHerramienta):
        H.buscar("Chuquitapa", clase="persona humana")


def test_los_datos_del_buscador_salen_del_grafo():
    """Los índices son consultas con nombre: 118 reconstrucciones del jsonl, una mención por registro."""
    import json
    rids = {json.loads(x)["id"] for x in (E.RAIZ / "datos/reconstrucciones.jsonl").read_text().splitlines() if x.strip()}
    assert rids <= set(H.indice_reconstrucciones())
    assert all(":M-" in k for k in H.indice_menciones())


# ───────────────────────── validación ─────────────────────────

@pytest.mark.parametrize("herramienta,params,mensaje", [
    ("afirmaciones", dict(entidad="Chuquitapa"), "buscar"),
    ("afirmaciones", dict(entidad="https://w3id.org/laad/id/persona/chuquitapa"), "no se admiten IRIs"),
    ("afirmaciones", dict(entidad="R-chuquitpa"), "R-chuquitapa"),
    ("afirmaciones", dict(entidad="M-UT01-003"), "cc-14-18:M-UT01-003"),
    ("afirmaciones", dict(entidad="cc-14-18:M-UT99-001"), "no existe"),
    ("afirmaciones", dict(atributo="cargo"), "ejerce-cargo"),
    ("afirmaciones", dict(fuerza=["resolutivo"]), "resolutiva"),
    ("afirmaciones", dict(expediente="cc-99"), "cc-14-18"),
    ("afirmaciones", dict(responden_a=["cc-14-18:A-UT99-999"]), "no existe"),
    ("afirmaciones", dict(foo="x"), "parámetro desconocido"),
    ("procedencia", {}, "obligatorio"),
    ("procedencia", dict(registro="R-chuquitapa"), "no se admite una reconstrucción"),
    ("cargos", dict(titular="cc-14-18:M-UT01-003"), "no se admite"),
    ("control_secuencia", dict(desde="mil"), "entero"),
    ("reconstrucciones", dict(creencia=["segura"]), "posible"),
    ("vocabulario", dict(esquema="todo"), "atributos"),
    ("buscr", {}, "buscar"),
])
def test_parametros_validados_con_mensaje_claro(herramienta, params, mensaje):
    with pytest.raises(H.ErrorHerramienta) as e:
        H.usar(herramienta, **params)
    assert mensaje in str(e.value)


def test_registro_de_herramientas():
    nombres = [h.nombre for h in H.HERRAMIENTAS]
    assert len(nombres) == len(set(nombres))
    for h in H.HERRAMIENTAS:
        assert len(h.descripcion) > 40
        esquema = h.parametros
        assert esquema["type"] == "object" and esquema["additionalProperties"] is False
        firma = inspect.signature(h.funcion).parameters
        assert set(esquema["properties"]) == set(firma), h.nombre                 # esquema = firma de la función
        assert set(esquema.get("required", [])) == {k for k, p in firma.items() if p.default is p.empty}, h.nombre


def test_una_lista_admite_un_texto_suelto():
    a = H.usar("afirmaciones", fuerza="resolutiva", expediente=EXP)
    assert a.filas and {f["fuerza"] for f in a.filas} == {"resolutiva"}


def test_afirmacion_y_reconstruccion_separadas():
    """El texto de una herramienta de capa 3 rotula las afirmaciones como tales, con afirmante, cita, tramo, folio o
    «no consta» y fuerza; la de capa 4, con creencia y autor."""
    t = H.usar("afirmaciones", entidad="R-prision", atributo="duracion", expediente=EXP).texto
    assert "— Lo que se afirma en el expediente (capa 3) —" in t and "RECONSTRUCCIÓN" not in t
    assert "Afirmante:" in t and "fuerza institucional:" in t and "folio no consta" in t
    t = H.usar("reconstrucciones", entidad="R-prision").texto
    assert "— Reconstrucción del investigador (capa 4) —" in t and "creencia:" in t and "AFIRMACIÓN" not in t


@pytest.mark.parametrize("herramienta,params", [
    ("buscar", dict(nombre="Chuquitapa")),
    ("afirmaciones", dict(entidad="R-chuquitapa", atributo="ejerce-cargo", expediente=EXP)),
    ("disputas", dict(entidad="R-chuquitapa")),
    ("disputas_firma", dict(expediente=EXP)),
    ("menciones_de", dict(entidad="R-huancachoque")),
    ("reconstrucciones", dict(mencion="cc-14-18:M-UT12.a-005")),
    ("cargos", dict(titular="R-chuquitapa")),
    ("participantes", dict(pieza="cc-14-18:P09")),
    ("procedencia", dict(registro="cc-14-18:A-UT11-004")),
    ("catalogo", dict(pc="PC04")),
])
def test_el_texto_de_cada_herramienta_se_verifica_con_sus_filas(herramienta, params):
    r = H.usar(herramienta, **params)
    assert r.filas
    assert H.verificar(r.texto, r.filas) == {"citas": [], "ids": []}


# ───────────────────────── verificar ─────────────────────────

def test_verificar_detecta_cita_inventada_y_alterada():
    filas = H.usar("afirmaciones", entidad="R-prision", atributo="duracion", expediente=EXP).filas
    buena = "yo me mantuve dos días preso"
    assert any(f["cita"] == buena for f in filas)
    texto = (f"Huancachoque dice «{buena}» (A-UT06-001); según Mata, «al otro dia   por la tarde». "
             f"Pero nadie escribió «estuvo preso un mes», ni \"yo me mantuve dos dias preso\" (A-UT06-999).")
    v = H.verificar(texto, filas)
    assert v["citas"] == ["estuvo preso un mes", "yo me mantuve dos dias preso"]     # inventada; alterada en una letra
    assert v["ids"] == ["A-UT06-999"]


def test_verificar_ids_calificados():
    filas = H.usar("afirmaciones", entidad="R-prision", atributo="duracion", expediente=EXP).filas
    assert H.verificar("cc-14-18:A-UT06-001", filas)["ids"] == []
    assert H.verificar("otro-exp:A-UT06-001", filas)["ids"] == ["otro-exp:A-UT06-001"]
    assert H.verificar("A-UT06-00", filas)["ids"] == ["A-UT06-00"]                      # prefijo de un id real


# ───────────────────────── banco de pruebas ─────────────────────────

def test_el_banco_tiene_las_20_pc():
    banco = E.cargar()
    assert sorted(x["pc"] for x in banco) == sorted(PREGUNTAS)
    assert all(x["pregunta"].strip() and x["plan"] and x["forma"] in E.FORMAS for x in banco)


def test_el_evaluador_alcanza_las_20_pc():
    resultados = E.evaluar()
    fallidas = {r["pc"]: r["fallos"] for r in resultados if not r["alcanzada"]}
    assert not fallidas
    assert len(resultados) == 20


def _linea(pc: str) -> dict:
    return next(x for x in E.cargar() if x["pc"] == pc)


def test_el_comprobador_rechaza_la_forma_equivocada():
    linea = {**_linea("PC09"), "forma": "A"}
    assert any("forma declarada A" in f for f in E.evaluar_linea(linea)["fallos"])
    linea = {**_linea("PC12"), "plan": [p for p in _linea("PC12")["plan"] if p["herramienta"] != "afirmaciones"]}
    assert any("NC sin respaldo" in f for f in E.evaluar_linea(linea)["fallos"])


def test_el_comprobador_rechaza_un_plan_incompleto():
    linea = _linea("PC11")
    sin_afirmaciones = {**linea, "plan": [p for p in linea["plan"] if p["herramienta"] != "afirmaciones"]}
    fallos = E.evaluar_linea(sin_afirmaciones)["fallos"]
    assert any("faltan" in f and "afirmaciones" in f for f in fallos)


def test_el_comprobador_rechaza_una_eleccion_que_buscar_no_devolvio():
    linea = _linea("PC11")
    plan = [dict(p, elegir="R-cano") if p["herramienta"] == "buscar" else p for p in linea["plan"]]
    assert any("no está entre los candidatos" in f for f in E.evaluar_linea({**linea, "plan": plan})["fallos"])
