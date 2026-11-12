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
