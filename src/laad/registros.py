"""Carga y valida registros planos (piezas, menciones, afirmaciones) con integridad referencial.

Además de las referencias, comprueba el DOMINIO Y RANGO de cada atributo (datos/atributos.csv) con la clase real
de cada mención, y deja en `Lote.avisos` lo que no es un error pero debe revisarse: conceptos candidatos en uso y
atributos candidatos sin dominio ni rango declarados (ontologia/README.md)."""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from . import fuente
from . import esquema
from .esquema import Afirmacion, Mencion, Pieza


@dataclass
class Lote:
    piezas: dict[str, Pieza] = field(default_factory=dict)
    menciones: dict[str, Mencion] = field(default_factory=dict)
    afirmaciones: dict[str, Afirmacion] = field(default_factory=dict)
    errores: list[str] = field(default_factory=list)
    avisos: list[str] = field(default_factory=list)   # no impiden mapear: candidatos en uso, atributos sin fila

    def hechos(self) -> set[str]:
        """Hechos narrados (H-…) que alguna afirmación del lote usa como sujeto o como valor."""
        return {h for a in self.afirmaciones.values() for h in (a.sujeto.hecho, a.valor.hecho) if h}


def _leer(ruta: Path):
    for n, linea in enumerate(ruta.read_text(encoding="utf-8").splitlines(), 1):
        if linea.strip():
            yield n, json.loads(linea)


def cargar(rutas_registros: list[Path], ruta_piezas: Path | None = None) -> Lote:
    """Carga los registros del expediente EN CURSO (fuente.usando_expediente): las citas se verifican contra su
    transcripción. Sin `ruta_piezas`, las piezas son las que nombra su manifiesto."""
    if ruta_piezas is None:
        ruta_piezas = fuente.ruta(fuente.manifiesto()["piezas"])
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
        refs = [a.afirmante, a.sujeto.mencion, a.valor.mencion, a.segun]
        if a.responde_a and a.responde_a not in lote.afirmaciones:
            E.append(f"{a.id}: responde_a inexistente {a.responde_a}")
        for r in filter(None, refs):
            if r not in lote.menciones:
                E.append(f"{a.id}: mención inexistente {r}")
        for r in filter(None, [a.sujeto.pieza, a.valor.pieza]):
            if r not in lote.piezas:
                E.append(f"{a.id}: pieza inexistente {r}")
        if lote.menciones.get(a.afirmante) and lote.menciones[a.afirmante].clase not in ("persona", "grupo"):
            E.append(f"{a.id}: el afirmante debe ser una mención de persona o grupo (p. ej. el común de un ayllu)")
        if lote.menciones.get(a.afirmante) and lote.menciones[a.afirmante].pieza != a.pieza and not a.afirmante_de_otra_pieza:
            E.append(f"{a.id}: el afirmante es de otra pieza; marque afirmante_de_otra_pieza y justifíquelo en nota")
        for h in filter(None, [a.sujeto.hecho, a.valor.hecho]):
            if not h.startswith(f"H-{a.pieza.lower()}-"):
                E.append(f"{a.id}: el hecho {h} debe ser local a la pieza {a.pieza} (H-{a.pieza.lower()}-…)")
        _dominio_rango(lote, a)
    for r in [*lote.piezas.values(), *lote.menciones.values(), *lote.afirmaciones.values()]:
        for esq, c in r.candidatos_usados():
            lote.avisos.append(f"{r.id}: usa el concepto candidato {c} (tes:{esq}), pendiente de aprobación")


def _dominio_rango(lote: Lote, a: Afirmacion) -> None:
    """El sujeto y el valor de la afirmación son de un tipo que su atributo admite (datos/atributos.csv), ahora
    con la clase real de cada mención. Un atributo candidato sin fila es un aviso; uno del tesauro, un error."""
    if a.atributo not in esquema.dominio_rango():
        if a.atributo in esquema.candidatos("atributos"):
            lote.avisos.append(f"{a.id}: el atributo candidato {a.atributo} no tiene dominio ni rango declarados "
                               f"en datos/atributos.csv; no se comprueban su sujeto ni su valor")
        else:
            lote.errores.append(f"{a.id}: el atributo {a.atributo} no tiene fila en datos/atributos.csv")
        return

    def clase(ref):
        return lote.menciones[ref].clase if ref in lote.menciones else None

    error = esquema.error_dominio_rango(a.atributo, esquema.tipos_de(a.sujeto, clase(a.sujeto.mencion)),
                                        esquema.tipos_de(a.valor, clase(a.valor.mencion), valor=True))
    if error:
        lote.errores.append(f"{a.id}: {error}")
