"""Expediente civil SINTÉTICO para las pruebas de generalidad y de corpus con varios expedientes.

TODO lo de este módulo es INVENTADO para las pruebas: el texto no es una fuente histórica, no procede del Archivo
Regional del Cusco y no debe citarse. Sirve para comprobar que un segundo expediente entra solo con su manifiesto.
"""
from __future__ import annotations

import json
from pathlib import Path

EXP_SINTETICO = "co-99-1"

TEXTO = """Caratula de prueba sintetica: autos sobre unas tierras
#
El comun del ayllu Sintetico parece y dice que el comprador Pedro Prueba tomo las chacras de Llaqta sin titulo alguno
#
Folio 2
Pedro Prueba indio forastero responde que las chacras de Llaqta las compro con escritura ante el escribano
"""

PIEZAS = [
    {"id": "P00", "orden": 0, "tramos": ["UT00"], "tipo_actuacion": "caratula", "titulo": "Carátula",
     "cita_inicio": "Caratula de prueba sintetica"},
    {"id": "P01", "orden": 1, "tramos": ["UT01"], "tipo_actuacion": "peticion", "titulo": "Petición del común",
     "cita_inicio": "El comun del ayllu Sintetico parece y dice"},
    {"id": "P02", "orden": 2, "tramos": ["UT02"], "tipo_actuacion": "declaracion-jurada", "titulo": "Respuesta",
     "cita_inicio": "Pedro Prueba indio forastero responde"},
]

# Los ids (M-UT01-001, A-UT01-001, P01…) coinciden A PROPÓSITO con ids del expediente piloto: los ids de registro
# solo son únicos dentro de un expediente y nada debe confundirlos.
REGISTROS = [
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
]


def _jsonl(ruta: Path, filas: list[dict]) -> None:
    ruta.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in filas) + "\n", encoding="utf-8")


def instalar(base: Path, manifiestos: Path) -> str:
    """Escribe en `base` la transcripción, las piezas y los registros sintéticos, y su manifiesto en `manifiestos`
    (con rutas absolutas). Devuelve el identificador del expediente sintético."""
    datos = base / EXP_SINTETICO
    datos.mkdir(parents=True, exist_ok=True)
    manifiestos.mkdir(parents=True, exist_ok=True)
    (datos / "transcripcion.txt").write_text(TEXTO, encoding="utf-8")
    _jsonl(datos / "piezas.jsonl", PIEZAS)
    _jsonl(datos / "registros.jsonl", REGISTROS)
    (manifiestos / f"{EXP_SINTETICO}.json").write_text(json.dumps({
        "id": EXP_SINTETICO, "descripcion": "SINTÉTICO para pruebas (texto inventado; no es una fuente)",
        "transcripcion": str(datos / "transcripcion.txt"), "marcas_folio": [["UT02", "Folio 2", "2"]],
        "jerarquia": [
            {"id": "arc/fondo/intendencia", "tipo": "rst:Fonds", "titulo": "Intendencia", "padre": None},
            {"id": "arc/seccion/causas-ordinarias", "tipo": "doc:seccion", "titulo": "Causas Ordinarias",
             "padre": "arc/fondo/intendencia"},
            {"id": f"arc/expediente/{EXP_SINTETICO}", "tipo": "rst:File", "titulo": "Expediente sintético",
             "padre": "arc/seccion/causas-ordinarias"}],
        "piezas": str(datos / "piezas.jsonl"), "registros": [str(datos / "registros.jsonl")], "fechas": None,
        "lote": {"nombre": "sintetico", "agente": "prueba", "tipo_agente": "Person", "plan": "prueba",
                 "fecha": "2026-11-12T00:00:00"},
        "signatura_catalogo": None,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    return EXP_SINTETICO
