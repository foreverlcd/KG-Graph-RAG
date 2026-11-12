"""Construcción del dataset compartida por las pruebas (idéntica a scripts/construir.py), cacheada."""
from __future__ import annotations

import functools
from pathlib import Path

import rdflib

from laad import mapeo
from laad.registros import cargar

from laad.hilo import PROCEDENCIA, RECONSTRUCCIONES, REGISTROS, RAIZ  # noqa: F401
from laad.hilo import construir as _construir_canonico


def construir() -> rdflib.Dataset:
    """Construye un Dataset nuevo (sin caché), igual que scripts/construir.py."""
    return _construir_canonico()


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
