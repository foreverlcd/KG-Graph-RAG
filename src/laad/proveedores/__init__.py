"""Adaptadores de proveedores de modelos de lenguaje para laad.agente.

Cada adaptador implementa laad.agente.Proveedor (iniciar / enviar / devolver) y guarda la conversación en el formato
nativo de su API. El agente no sabe qué modelo hay detrás.

* gemini: API de Google (google-genai), con el nivel gratuito de AI Studio.

Para añadir otro proveedor basta un módulo con una clase que cumpla el protocolo y una entrada en `crear`.
"""
from __future__ import annotations

import os
from pathlib import Path


def cargar_env(ruta: str | Path) -> list[str]:
    """Carga variables KEY=valor de un archivo .env en os.environ sin pisar las ya definidas y sin imprimir nada.
    Devuelve los NOMBRES cargados (nunca los valores)."""
    cargadas = []
    for linea in Path(ruta).read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        clave, valor = linea.split("=", 1)
        clave, valor = clave.strip().removeprefix("export ").strip(), valor.strip().strip("'\"")
        if clave and clave not in os.environ:
            os.environ[clave] = valor
            cargadas.append(clave)
    return cargadas


def crear(nombre: str, modelo: str | None = None):
    """Crea el proveedor por nombre."""
    if nombre == "gemini":
        from .gemini import Gemini
        return Gemini(modelo)
    raise ValueError(f"proveedor desconocido: {nombre!r} (disponibles: gemini)")
