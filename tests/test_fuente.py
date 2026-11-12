"""Pruebas de la capa de fuente: segmentación, marcas de folio y verificador de citas."""
from laad.fuente import tramos, tramo, verificar_cita, sha256, MARCAS_FOLIO

SHA_ESPERADO = "bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe"


def test_transcripcion_no_modificada():
    # Si la transcripción cambia, todas las citas deben re-verificarse (nueva versión PROV).
    assert sha256() == SHA_ESPERADO


def test_21_unidades_de_transcripcion():
    assert len({t.ut for t in tramos()}) == 21


def test_marcas_de_folio_abren_su_tramo():
    for ut, marca, folio in MARCAS_FOLIO:
        conf = [t for t in tramos() if t.ut == ut and t.folio == folio]
        assert len(conf) == 1 and conf[0].texto.startswith(marca)


def test_tramos_sin_marca_no_tienen_folio():
    assert all(t.folio is None for t in tramos() if t.marca is None)


def test_tramos_cubren_texto_sin_solaparse():
    ts = tramos()
    for a, b in zip(ts, ts[1:]):
        assert a.fin <= b.inicio


def test_cita_exacta_valida():
    r = verificar_cita("en tiempo del rebelde Tupa amaro fue", "UT11")
    assert r.valida and r.ocurrencias_en_tramo == 1


def test_cita_cruza_salto_de_linea():
    # La transcripción corta la frase en dos líneas; el colapso de espacios lo admite.
    r = verificar_cita("Comisionado por este y no coronel como expone en su certificación", "UT11")
    assert r.valida


def test_cita_modernizada_rechazada():
    # Grafía del corpus modernizado ("Huancachoque" en el cuerpo del texto de Cano): no vale.
    r = verificar_cita("al denunciante Manuel Huancachoque lo estropearon", "UT01")
    assert not r.valida


def test_cita_en_tramo_equivocado_informa_donde_esta():
    r = verificar_cita("No sabe escribir que es cierto", "UT12.a")
    assert not r.valida and "UT12.b" in r.tramos_donde_aparece


def test_no_se_pliegan_mayusculas_ni_acentos():
    assert not verificar_cita("isidro cano", "UT01").valida
    assert verificar_cita("Isidro Cano.", "UT01").valida


def test_tramo_folio_34():
    assert tramo("UT20").folio == "34"
