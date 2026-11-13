"""Construcción canónica del grafo del expediente CC 14-18 (usada por scripts/construir.py y por las pruebas).

Carga el hilo central (anotado el 2026-11-12) y los lotes que completan el expediente (expediente_a/b/c,
anotados el 2026-11-13 por agentes del mismo modelo, por tramos UT00–UT08, UT09–UT14 y UT15–UT20).
"""
from __future__ import annotations

from pathlib import Path

import rdflib

from . import mapeo
from .registros import cargar

RAIZ = Path(__file__).resolve().parents[2]
REGISTROS = RAIZ / "datos/registros/hilo_central.jsonl"
LOTES = [REGISTROS] + [RAIZ / f"datos/registros/expediente_{x}.jsonl" for x in "abc"]
RECONSTRUCCIONES = RAIZ / "datos/reconstrucciones.jsonl"
FECHAS = RAIZ / "datos/fechas_normalizadas.csv"
CATALOGO = RAIZ / "datos/catalogo/fichas_pc03_pc04.jsonl"
PROCEDENCIA = mapeo.Procedencia(lote="anotacion-manual-expediente-v1", agente="claude-opus-5-5",
                                tipo_agente="SoftwareAgent", plan="anotacion-manual",
                                fecha="2026-11-13T00:00:00")


def construir() -> rdflib.Dataset:
    lote = cargar(LOTES)
    recs = mapeo.cargar_reconstrucciones(RECONSTRUCCIONES)
    return mapeo.construir(lote, PROCEDENCIA, recs, fechas=FECHAS, catalogo=CATALOGO)
