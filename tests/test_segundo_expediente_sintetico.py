"""Prueba ESTRUCTURAL de generalidad (revisión C2): un expediente civil SINTÉTICO entra sin tocar el núcleo.

El texto de abajo es inventado para la prueba (no es una fuente histórica ni debe citarse). La prueba real
del criterio 5 usa el expediente sorteado a ciegas (CO Cusco Leg. 70 Exp. 15) cuando haya transcripción.
Comprueba: (1) parametrización por manifiesto, sin constantes de CC L14E18; (2) clase de mención «cosa»,
afirmante colectivo (grupo) y concepto validado por dct:conformsTo; (3) SHACL conforma; (4) no aparece ninguna
clase ni propiedad que no use ya el grafo del hilo central (núcleo cerrado).
"""
import json

import pytest
import rdflib

from laad import fuente, mapeo, validacion
from laad.registros import cargar

TEXTO = """Caratula de prueba sintetica: autos sobre unas tierras
#
El comun del ayllu Sintetico parece y dice que el comprador Pedro Prueba tomo las chacras de Llaqta sin titulo alguno
#
Folio 2
Pedro Prueba indio forastero responde que las chacras de Llaqta las compro con escritura ante el escribano
"""


@pytest.fixture
def expediente_sintetico(tmp_path, monkeypatch):
    (tmp_path / "corpus").mkdir()
    tr = tmp_path / "corpus" / "sintetico.txt"
    tr.write_text(TEXTO, encoding="utf-8")
    man_dir = tmp_path / "expedientes"
    man_dir.mkdir()
    (man_dir / "co-99-1.json").write_text(json.dumps({
        "id": "co-99-1", "descripcion": "SINTÉTICO para pruebas",
        "transcripcion": str(tr), "marcas_folio": [["UT02", "Folio 2", "2"]],
        "jerarquia": [
            {"id": "arc/fondo/intendencia", "tipo": "rst:Fonds", "titulo": "Intendencia", "padre": None},
            {"id": "arc/seccion/causas-ordinarias", "tipo": "doc:seccion", "titulo": "Causas Ordinarias", "padre": "arc/fondo/intendencia"},
            {"id": "arc/expediente/co-99-1", "tipo": "rst:File", "titulo": "Expediente sintético", "padre": "arc/seccion/causas-ordinarias"}],
    }), encoding="utf-8")
    monkeypatch.setattr(fuente, "MANIFIESTOS", man_dir)
    monkeypatch.setattr(fuente, "RAIZ", tmp_path)
    fuente.manifiesto.cache_clear()
    fuente._tramos.cache_clear()
    piezas = tmp_path / "piezas.jsonl"
    regs = tmp_path / "registros.jsonl"
    with fuente.usando_expediente("co-99-1"):
        piezas.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in [
            {"id": "P00", "orden": 0, "tramos": ["UT00"], "tipo_actuacion": "caratula", "titulo": "Carátula",
             "cita_inicio": "Caratula de prueba sintetica"},
            {"id": "P01", "orden": 1, "tramos": ["UT01"], "tipo_actuacion": "peticion", "titulo": "Petición del común",
             "cita_inicio": "El comun del ayllu Sintetico parece y dice"},
            {"id": "P02", "orden": 2, "tramos": ["UT02"], "tipo_actuacion": "declaracion-jurada", "titulo": "Respuesta",
             "cita_inicio": "Pedro Prueba indio forastero responde"}]), encoding="utf-8")
        regs.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in [
            {"tipo_registro": "mencion", "id": "M-UT01-001", "tramo": "UT01", "pieza": "P01", "clase": "grupo",
             "texto": "El comun del ayllu Sintetico", "rol_en_pieza": "denunciante", "tipo_entidad": "ayllu",
             "cita": "El comun del ayllu Sintetico parece y dice"},
            {"tipo_registro": "mencion", "id": "M-UT01-002", "tramo": "UT01", "pieza": "P01", "clase": "persona",
             "texto": "Pedro Prueba", "cita": "el comprador Pedro Prueba tomo"},
            {"tipo_registro": "mencion", "id": "M-UT01-003", "tramo": "UT01", "pieza": "P01", "clase": "cosa",
             "texto": "las chacras de Llaqta", "cita": "tomo las chacras de Llaqta sin titulo alguno"},
            {"tipo_registro": "mencion", "id": "M-UT02-001", "tramo": "UT02", "pieza": "P02", "clase": "persona",
             "texto": "Pedro Prueba", "rol_en_pieza": "declarante", "cita": "Pedro Prueba indio forastero responde"},
            {"tipo_registro": "afirmacion", "id": "A-UT01-001", "tramo": "UT01", "pieza": "P01", "afirmante": "M-UT01-001",
             "rol_afirmante": "denunciante", "sujeto": {"mencion": "M-UT01-002"}, "atributo": "motivo",
             "valor": {"literal": "sin titulo alguno"}, "cita": "tomo las chacras de Llaqta sin titulo alguno"},
            {"tipo_registro": "afirmacion", "id": "A-UT02-001", "tramo": "UT02", "pieza": "P02",
             "afirmante": "M-UT02-001", "rol_afirmante": "declarante", "sujeto": {"mencion": "M-UT02-001"},
             "atributo": "tiene-condicion", "valor": {"concepto": "forastero"}, "cita": "Pedro Prueba indio forastero"},
        ]), encoding="utf-8")
        lote = cargar([regs], ruta_piezas=piezas)
        assert not lote.errores, lote.errores
        pr = mapeo.Procedencia(lote="sintetico", agente="prueba", tipo_agente="Person", plan="prueba",
                               fecha="2026-11-12T00:00:00")
        ds = mapeo.construir(lote, pr)
        yield ds
    fuente.manifiesto.cache_clear()
    fuente._tramos.cache_clear()


def _vocabulario(g: rdflib.Graph) -> tuple[set, set]:
    clases = {o for o in g.objects(None, rdflib.RDF.type) if not str(o).startswith("https://w3id.org/laad/")}
    props = {p for p in g.predicates()}
    return clases, props


def test_expediente_sintetico_conforma_sin_tocar_el_nucleo(expediente_sintetico):
    from pathlib import Path
    ref = rdflib.Dataset()
    ref.parse(Path(__file__).resolve().parents[1] / "datos/grafo/hilo_central.trig", format="trig")
    u = mapeo.union(expediente_sintetico)
    conforma, _, texto = validacion.shacl(u, con_ontologias=True)
    assert conforma, texto[:3000]
    c2, p2 = _vocabulario(u)
    c1, p1 = _vocabulario(mapeo.union(ref))
    # prov:Person ya pertenece al perfil (agente humano: anotador o validador, mapeo._agente); el hilo central
    # solo lo anotó un prov:SoftwareAgent, por eso no aparece en su grafo.
    c1 |= {rdflib.PROV.Person}
    assert c2 <= c1, f"clases nuevas: {c2 - c1}"
    assert p2 <= p1, f"propiedades nuevas: {p2 - p1}"


def test_iris_del_sintetico_no_colisionan_con_cc_14_18(expediente_sintetico):
    s = {str(x) for x in mapeo.union(expediente_sintetico).subjects()}
    assert any("/co-99-1/" in x for x in s)
    assert not any("/cc-14-18/" in x for x in s)
