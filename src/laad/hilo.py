"""Construcción canónica del grafo del hilo central (usada por scripts/construir.py y por las pruebas)."""
from __future__ import annotations

from pathlib import Path

import rdflib

from . import mapeo
from .registros import cargar

RAIZ = Path(__file__).resolve().parents[2]
REGISTROS = RAIZ / "datos/registros/hilo_central.jsonl"
RECONSTRUCCIONES = RAIZ / "datos/reconstrucciones.jsonl"
FECHAS = RAIZ / "datos/fechas_normalizadas.csv"
PROCEDENCIA = mapeo.Procedencia(lote="anotacion-manual-hilo-central-v1", agente="claude-opus-5-5",
                                tipo_agente="SoftwareAgent", plan="anotacion-manual",
                                fecha="2026-11-12T00:00:00")


def construir() -> rdflib.Dataset:
    lote = cargar([REGISTROS])
    recs = mapeo.cargar_reconstrucciones(RECONSTRUCCIONES)
    return mapeo.construir(lote, PROCEDENCIA, recs, fechas=FECHAS)
