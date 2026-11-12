"""Carga y valida registros planos (piezas, menciones, afirmaciones) con integridad referencial."""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from .esquema import Afirmacion, Mencion, Pieza

RAIZ = Path(__file__).resolve().parents[2]
PIEZAS = RAIZ / "datos" / "piezas.jsonl"


@dataclass
class Lote:
    piezas: dict[str, Pieza] = field(default_factory=dict)
    menciones: dict[str, Mencion] = field(default_factory=dict)
    afirmaciones: dict[str, Afirmacion] = field(default_factory=dict)
    errores: list[str] = field(default_factory=list)


def _leer(ruta: Path):
    for n, linea in enumerate(ruta.read_text(encoding="utf-8").splitlines(), 1):
        if linea.strip():
            yield n, json.loads(linea)


def cargar(rutas_registros: list[Path], ruta_piezas: Path = PIEZAS) -> Lote:
    lote = Lote()
    for n, d in _leer(ruta_piezas):
        try:
            p = Pieza(**d)
            if p.id in lote.piezas:
                lote.errores.append(f"pieza duplicada {p.id}")
            lote.piezas[p.id] = p
        except Exception as e:  # noqa: BLE001
            lote.errores.append(f"{ruta_piezas.name}:{n} {e}")
    for ruta in rutas_registros:
        for n, d in _leer(ruta):
            tipo = d.pop("tipo_registro")
            try:
                if tipo == "mencion":
                    r = Mencion(**d)
                    destino = lote.menciones
                elif tipo == "afirmacion":
                    r = Afirmacion(**d)
                    destino = lote.afirmaciones
                else:
                    raise ValueError(f"tipo_registro desconocido: {tipo}")
                if r.id in lote.menciones or r.id in lote.afirmaciones:
                    lote.errores.append(f"id duplicado {r.id}")
                destino[r.id] = r
            except Exception as e:  # noqa: BLE001
                lote.errores.append(f"{ruta.name}:{n} {d.get('id')} {str(e).splitlines()[:3]}")
    _integridad(lote)
    return lote


def _integridad(lote: Lote) -> None:
    E = lote.errores
    for mm in lote.menciones.values():
        p = lote.piezas.get(mm.pieza)
        if not p:
            E.append(f"{mm.id}: pieza inexistente {mm.pieza}")
        elif mm.tramo not in p.tramos:
            E.append(f"{mm.id}: tramo {mm.tramo} no pertenece a {p.id} {p.tramos}")
    for a in lote.afirmaciones.values():
        p = lote.piezas.get(a.pieza)
        if not p:
            E.append(f"{a.id}: pieza inexistente {a.pieza}")
        elif a.tramo not in p.tramos:
            E.append(f"{a.id}: tramo {a.tramo} no pertenece a {p.id} {p.tramos}")
        refs = [a.afirmante, a.sujeto.mencion, a.valor.mencion]
        for r in filter(None, refs):
            if r not in lote.menciones:
                E.append(f"{a.id}: mención inexistente {r}")
        for r in filter(None, [a.sujeto.pieza, a.valor.pieza]):
            if r not in lote.piezas:
                E.append(f"{a.id}: pieza inexistente {r}")
        if lote.menciones.get(a.afirmante) and lote.menciones[a.afirmante].clase != "persona":
            E.append(f"{a.id}: el afirmante debe ser una mención de persona")
        for h in filter(None, [a.sujeto.hecho, a.valor.hecho]):
            if not h.startswith(f"H-{a.pieza.lower()}-"):
                E.append(f"{a.id}: el hecho {h} debe ser local a la pieza {a.pieza} (H-{a.pieza.lower()}-…)")
