"""La forma de la respuesta (DISPUTA / NC / A) se calcula a partir de las filas, no se escribe a mano."""
from laad.responder import forma_de, pronunciamientos


def _f(valor, pol, fuerza="testimonial"):
    return {"valorLabel": valor, "pol": pol, "fuerza": fuerza, "afirmante": "x", "afirmanteR": None,
            "tipoAct": "declaración", "pieza": "P1", "tramo": "UT01"}


def test_sin_filas_es_no_consta():
    assert forma_de([]) == "NC"


def test_afirmar_y_negar_el_mismo_valor_es_disputa():
    assert forma_de([_f("coronel", "afirma"), _f("coronel", "niega")]) == "DISPUTA"


def test_valores_distintos_es_disputa():
    assert forma_de([_f("dos días", "afirma"), _f("una noche", "afirma")]) == "DISPUTA"


def test_concordantes_no_es_disputa():
    assert forma_de([_f("coronel", "afirma"), _f("coronel", "afirma")]) == "A"


def test_pronunciamiento_de_autoridad_se_calcula():
    assert pronunciamientos([_f("coronel", "afirma")]).startswith("Ninguna")
    assert pronunciamientos([_f("coronel", "afirma", "resolutiva")]).startswith("Se pronuncian")


# ── cardinalidad de los atributos (datos/atributos.csv, columna «valores») ──

def test_valores_distintos_de_un_atributo_multivaluado_no_son_disputa():
    """Una persona puede ser cacique y recaudador a la vez: no es disputa (decisión del usuario, 2026-11-24)."""
    filas = [_f("cacique", "afirma"), _f("recaudador de tributos", "afirma")]
    assert forma_de(filas, "ejerce-cargo") == "A"
    assert forma_de(filas) == "DISPUTA"          # sin atributo: lo prudente


def test_afirmar_y_negar_el_mismo_valor_sigue_siendo_disputa_aunque_admita_varios():
    filas = [_f("coronel", "afirma"), _f("coronel", "niega"), _f("cacique", "afirma")]
    assert forma_de(filas, "ejerce-cargo") == "DISPUTA"


def test_valores_distintos_de_un_atributo_de_un_solo_valor_son_disputa():
    assert forma_de([_f("dos días", "afirma"), _f("una noche", "afirma")], "duracion") == "DISPUTA"


def test_toda_fila_de_atributos_declara_uno_o_varios():
    import csv
    from laad.responder import ATRIBUTOS
    with open(ATRIBUTOS, encoding="utf-8") as f:
        assert {r["valores"] for r in csv.DictReader(f)} == {"uno", "varios"}
