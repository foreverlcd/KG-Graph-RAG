"""Adaptador de transcripciones: la segmentación se configura en el manifiesto (clave «formato»).

Las transcripciones de este módulo son SINTÉTICAS: texto inventado para la prueba, no procede de ningún archivo y
no debe citarse. Se comprueba que (a) el expediente piloto se segmenta exactamente igual que antes; (b) una
transcripción en Markdown y otra con marcas de folio regulares se cortan como se espera; (c) lo editorial no es
citable; (d) scripts/nuevo_expediente.py deja un borrador que no entra en el corpus y nunca sobrescribe.
"""
from __future__ import annotations

import csv
import importlib.util
import json

import pytest

from laad import fuente
from laad.preguntas import EXPEDIENTE_PILOTO

# SINTÉTICO (inventado): convención Markdown con preámbulo YAML, comentario del editor y títulos de pieza.
MD_SINTETICO = """---
titulo: Transcripcion SINTETICA de prueba
transcriptor: nadie
---
# Caratula

Autos SINTETICOS de prueba sobre unas tierras inventadas

<!-- nota del editor: imagen 0002 -->
## Peticion

[f. 1r] El comun del ayllu Sintetico parece y dice
> Nota del editor: mancha de tinta en el margen
que le tomaron las chacras
[f. 1v] y pide justicia

## Decreto
Por presentada. Traslado a la otra parte
"""
FORMATO_MD = {"separador": None, "encabezado": r"^#{1,3} ", "marca_folio": r"^\[f\. ?(\d+[rv]?)\]",
              "ignorar": [r"(?s)\A---\n.*?\n---\n", r"(?s)<!--.*?-->", r"^> .*$"]}

# SINTÉTICO (inventado): texto corrido sin separadores; cada marca «Folio n» al comienzo de línea inicia una unidad.
FOLIOS_SINTETICO = """Caratula SINTETICA de prueba
Folio 1
En el pueblo de Prueba parecio Pedro Prueba y dijo que a folios 2 consta su titulo
Folio 2 vuelto
Titulo inventado de las chacras de Llaqta
[Folio 3]
Auto final de prueba
"""
FORMATO_FOLIOS = {"separador": None, "encabezado": r"^\[?[Ff]olio \d+", "marca_folio": r"^\[?[Ff]olio (\d+)\]?"}


def _resumen(tramos):
    return [(t.id, t.folio, fuente.colapsar(t.texto)[:24]) for t in tramos]


# ───────────── (a) el piloto no cambia ─────────────
def test_el_piloto_usa_el_formato_por_defecto():
    assert "formato" not in fuente.manifiesto(EXPEDIENTE_PILOTO)
    assert fuente.formato(EXPEDIENTE_PILOTO) == fuente.formato_completo()
    assert fuente.formato_completo()["separador"] == r"^[ \t]*#[ \t]*$"


def test_el_piloto_se_segmenta_igual_que_su_indice():
    """fuente/tramos.csv es el índice publicado del piloto: ids, líneas, folio y marca deben seguir coincidiendo."""
    with (fuente.RAIZ / "fuente" / "tramos.csv").open(encoding="utf-8", newline="") as f:
        indice = list(csv.DictReader(f))
    tramos = fuente.tramos(EXPEDIENTE_PILOTO)
    assert [(t.id, t.ut, str(t.linea_inicio), str(t.linea_fin), t.folio or "no consta", t.marca or "",
             str(len(fuente.colapsar(t.texto)))) for t in tramos] \
        == [(r["tramo"], r["ut"], r["linea_inicio"], r["linea_fin"], r["folio_explicito"], r["marca"], r["caracteres"])
            for r in indice]
    texto = fuente.texto_canonico(fuente.ruta_transcripcion(EXPEDIENTE_PILOTO))
    assert all(t.texto == texto[t.inicio:t.fin] for t in tramos)      # nada ignorado: el tramo es el texto tal cual


def test_segmentar_por_defecto_es_la_convencion_del_piloto():
    ruta = fuente.ruta_transcripcion(EXPEDIENTE_PILOTO)
    assert fuente.segmentar(fuente.texto_canonico(ruta), tuple(fuente.marcas_folio(EXPEDIENTE_PILOTO))) \
        == fuente.tramos(EXPEDIENTE_PILOTO)


# ───────────── (b) otras convenciones (SINTÉTICAS) ─────────────
def test_markdown_sintetico_se_segmenta_por_titulos():
    tramos = fuente.segmentar(MD_SINTETICO, (), FORMATO_MD)
    assert _resumen(tramos) == [
        ("UT01", None, "# Caratula Autos SINTETI"),
        ("UT02.a", None, "## Peticion"),
        ("UT02.b", "1r", "[f. 1r] El comun del ayl"),
        ("UT02.c", "1v", "[f. 1v] y pide justicia"),
        ("UT03", None, "## Decreto Por presentad"),
    ]
    # no hay UT00: antes del primer título solo está el preámbulo, que se ignora
    assert tramos[0].linea_inicio == 5 and tramos[2].marca == "[f. 1r]"
    # los desplazamientos se refieren al texto del archivo, también después de lo ignorado
    assert all(MD_SINTETICO[t.inicio:t.fin].startswith(t.texto[:10]) for t in tramos)
    for a, b in zip(tramos, tramos[1:]):
        assert a.fin <= b.inicio


def test_folios_regulares_sinteticos_se_detectan_sin_listarlos():
    tramos = fuente.segmentar(FOLIOS_SINTETICO, (), FORMATO_FOLIOS)
    assert _resumen(tramos) == [
        ("UT00", None, "Caratula SINTETICA de pr"),
        ("UT01", "1", "Folio 1 En el pueblo de "),
        ("UT02", "2", "Folio 2 vuelto Titulo in"),
        ("UT03", "3", "[Folio 3] Auto final de "),
    ]
    # la referencia interna «a folios 2» no es una marca: la expresión está anclada al comienzo de línea
    assert "a folios 2" in tramos[1].texto


def test_marcas_a_mano_y_detectadas_se_combinan():
    texto = "uno\n#\nFolio 7\ndos\n(al margen: foja ocho)\ntres\n"
    tramos = fuente.segmentar(texto, (("UT01", "(al margen: foja ocho)", "8"),), {"marca_folio": r"^Folio (\d+)$"})
    assert [(t.id, t.folio) for t in tramos] == [("UT00", None), ("UT01.a", "7"), ("UT01.b", "8")]


def test_mas_de_ocho_partes_en_una_unidad():
    texto = "".join(f"[f. {i}]\ntexto del folio {i}\n" for i in range(1, 31))
    tramos = fuente.segmentar(texto, (), {"marca_folio": r"^\[f\. (\d+)\]"})
    assert [t.id for t in tramos][:3] == ["UT00.a", "UT00.b", "UT00.c"]
    assert [t.id for t in tramos][25:28] == ["UT00.z", "UT00.aa", "UT00.ab"] and tramos[29].folio == "30"


def test_formato_invalido_es_un_error_claro():
    with pytest.raises(ValueError, match="desconocida"):
        fuente.segmentar("x", (), {"separadro": "^#$"})
    with pytest.raises(ValueError, match="no válida"):
        fuente.segmentar("x", (), {"encabezado": "(sin cerrar"})
    with pytest.raises(ValueError, match="grupo"):
        fuente.segmentar("x", (), {"marca_folio": r"^Folio \d+"})


# ───────────── (c) por manifiesto: codificación y texto editorial ─────────────
@pytest.fixture
def expediente_md(tmp_path, monkeypatch):
    """Manifiesto SINTÉTICO con «formato» Markdown y transcripción en latin-1."""
    (tmp_path / "t.md").write_bytes((MD_SINTETICO + "\n## Año\nseñor fiscal de prueba\n").encode("latin-1"))
    manifiestos = tmp_path / "expedientes"
    manifiestos.mkdir()
    (manifiestos / "zz-md-1.json").write_text(json.dumps({
        "id": "zz-md-1", "descripcion": "SINTÉTICO para pruebas", "transcripcion": str(tmp_path / "t.md"),
        "marcas_folio": [], "formato": dict(FORMATO_MD, codificacion="latin-1")}), encoding="utf-8")
    monkeypatch.setattr(fuente, "MANIFIESTOS", manifiestos)
    return "zz-md-1"


def test_manifiesto_con_formato_y_codificacion(expediente_md):
    assert fuente.formato(expediente_md)["codificacion"] == "latin-1"
    tramos = fuente.tramos(expediente_md)
    assert [t.id for t in tramos] == ["UT01", "UT02.a", "UT02.b", "UT02.c", "UT03", "UT04"]
    assert "señor fiscal" in fuente.tramo("UT04", expediente_md).texto
    with fuente.usando_expediente(expediente_md):
        assert fuente.verificar_cita("El comun del ayllu Sintetico parece y dice", "UT02.b").valida
        # lo editorial no es citable…
        assert not fuente.verificar_cita("mancha de tinta en el margen", "UT02.b").valida
        assert not fuente.verificar_cita("Transcripcion SINTETICA de prueba", "UT01").valida
        # …y una cita continúa al otro lado de la línea ignorada, como al otro lado de un salto de línea
        r = fuente.verificar_cita("parece y dice que le tomaron las chacras", "UT02.b")
        assert r.valida and r.inicio == fuente.texto_canonico().index("parece y dice")


# ───────────── (d) scripts/nuevo_expediente.py ─────────────
def _script():
    spec = importlib.util.spec_from_file_location("nuevo_expediente", fuente.RAIZ / "scripts" / "nuevo_expediente.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_nuevo_expediente_deja_un_borrador_y_no_sobrescribe(tmp_path, monkeypatch, capsys):
    ne = _script()
    manifiestos = tmp_path / "expedientes"
    monkeypatch.setattr(fuente, "MANIFIESTOS", manifiestos)
    (tmp_path / "t.md").write_text(MD_SINTETICO, encoding="utf-8")
    destino = ne.crear("zz-9-1", tmp_path / "t.md", ne.leer_formato(json.dumps(FORMATO_MD)), datos=tmp_path / "zz-9-1",
                       raiz=tmp_path)
    m = json.loads(destino.read_text(encoding="utf-8"))
    assert m["estado"] == "borrador" and m["formato"] == FORMATO_MD and m["transcripcion"] == "t.md"
    assert m["piezas"] == "zz-9-1/piezas.jsonl" and m["registros"] == ["zz-9-1/registros/anotacion.jsonl"]
    assert (tmp_path / "zz-9-1" / "piezas.jsonl").read_text() == ""
    assert (tmp_path / "zz-9-1" / "registros" / "anotacion.jsonl").read_text() == ""
    # el borrador no forma parte del corpus, pero sus tramos se pueden pedir por su identificador
    assert fuente.expedientes() == [] and fuente.expedientes(borradores=True) == ["zz-9-1"]
    antes = destino.read_text(encoding="utf-8")
    with pytest.raises(FileExistsError):
        ne.crear("zz-9-1", tmp_path / "t.md", datos=tmp_path / "otra", raiz=tmp_path)
    with pytest.raises(FileExistsError):                             # la carpeta de datos tampoco se pisa
        ne.crear("zz-9-2", tmp_path / "t.md", datos=tmp_path / "zz-9-1", raiz=tmp_path)
    assert destino.read_text(encoding="utf-8") == antes and not (manifiestos / "zz-9-2.json").exists()
    with pytest.raises(ValueError):
        ne.crear("Mal Id", tmp_path / "t.md", datos=tmp_path / "x", raiz=tmp_path)
    # la vista previa lista cada tramo con sus líneas, su folio y sus primeras palabras
    assert ne.main(["zz-9-3", str(tmp_path / "t.md"), "--formato", "markdown", "--marca-folio", FORMATO_MD["marca_folio"],
                    "--ignorar", "^> .*$", "--solo-ver"]) == 0
    salida = capsys.readouterr().out
    assert "UT02.b" in salida and "1r" in salida and "[f. 1r] El comun del ayllu" in salida
    assert "5 tramos en 3 unidades; 2 con folio explícito" in salida
    assert not (manifiestos / "zz-9-3.json").exists()


def test_los_preajustes_son_formatos_validos():
    ne = _script()
    for nombre in ne.PREAJUSTES:
        fuente.formato_completo(ne.leer_formato(nombre))
