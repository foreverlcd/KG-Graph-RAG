"""Construcción del dataset compartida por las pruebas (idéntica a scripts/construir.py), cacheada."""
from __future__ import annotations

import functools
from pathlib import Path

import rdflib

from laad import corpus, mapeo
from laad.corpus import RAIZ, RECONSTRUCCIONES  # noqa: F401
from laad.preguntas import EXPEDIENTE_PILOTO

LOTES = corpus.rutas_registros(EXPEDIENTE_PILOTO)      # registros del expediente piloto (según su manifiesto)
REGISTROS = LOTES[0]
PROCEDENCIA = corpus.procedencia(EXPEDIENTE_PILOTO)


def construir() -> rdflib.Dataset:
    """Construye un Dataset nuevo del corpus (sin caché), igual que scripts/construir.py."""
    return corpus.construir()


@functools.lru_cache(maxsize=1)
def dataset() -> rdflib.Dataset:
    """Dataset compartido: NO mutarlo; copiar antes de modificar."""
    return construir()


@functools.lru_cache(maxsize=1)
def _union() -> rdflib.Graph:
    return mapeo.union(dataset())


def union() -> rdflib.Graph:
    """Unión de los grafos nombrados (objeto cacheado: copiar antes de modificar)."""
    return _union()


def copia_union() -> rdflib.Graph:
    g = rdflib.Graph()
    for t in union():
        g.add(t)
    return g
