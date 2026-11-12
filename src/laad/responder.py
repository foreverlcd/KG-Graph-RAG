"""Composición determinista de respuestas para el investigador.

Toda respuesta:
* separa AFIRMACIÓN (capa 3: alguien lo dijo en 1806, con cita) de RECONSTRUCCIÓN (capa 4: lo propone un
  investigador, con autor, fecha y creencia);
* lleva para cada afirmación la cita literal, el tramo y el folio («no consta en la transcripción» si no lo hay);
* nunca convierte una resolución en un hecho: la muestra como afirmación con su fuerza institucional.
El LLM conversacional (fase posterior) solo puede reformular estas filas; no puede añadir hechos (docs/D §4).
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field

from .consulta import atributo as atr_iri, consultar

NO_CONSTA = "no consta"


def _folio(r: dict) -> str:
    return r["folio"] if r.get("folio") else "folio no consta en la transcripción"


def linea_afirmacion(r: dict) -> str:
    fecha = f", fecha escrita «{r['fecha']}»" if r.get("fecha") else ", sin fecha escrita"
    ante = r.get("ante") or NO_CONSTA
    firma = r.get("firmantes") or NO_CONSTA
    pol = "" if r["pol"] == "afirma" else " [NIEGA]"
    eliptico = " (sujeto elíptico resuelto por el anotador)" if r.get("eliptico") == "true" else ""
    return (f"AFIRMACIÓN {r['aid']}{pol}: {r['atrLabel']} → {r['valorLabel']}{eliptico}\n"
            f"    «{r['cita']}»\n"
            f"    Afirmante: «{r['afirmante']}» ({r['rolAf']})"
            f"{' [= ' + r['afirmanteR'] + ', según reconstrucción]' if r.get('afirmanteR') else ''}; {r['tipoAct']} {r['pieza']}{fecha}; "
            f"ante: {ante}; firma la pieza: {firma}\n"
            f"    Fundamento invocado: {r['fundamento']}; fuerza institucional: {r['fuerza']}; "
            f"{r['tramo']}, {_folio(r)}")


def linea_reconstruccion(r: dict) -> str:
    return (f"RECONSTRUCCIÓN «{r['label']}» — creencia: {r['creencia']}; autor: {r['autor']}; fecha: {r['fecha']}\n"
            f"    Deriva de: {r['menciones']}\n    Argumento: {r['argumento']}")


@dataclass
class Respuesta:
    pregunta: str
    forma: str                       # D | A | DISPUTA | NC | R | P
    resumen: str
    afirmaciones: list[dict] = field(default_factory=list)
    reconstrucciones: list[dict] = field(default_factory=list)
    extra: list[str] = field(default_factory=list)

    def texto(self) -> str:
        out = [f"PREGUNTA: {self.pregunta}", f"RESPUESTA ({self.forma}): {self.resumen}", ""]
        if self.afirmaciones:
            out.append("— Lo que se afirma en el expediente (capa 3) —")
            out += [linea_afirmacion(r) for r in self.afirmaciones]
            out.append("")
        if self.reconstrucciones:
            out.append("— Reconstrucción del investigador (capa 4) —")
            out += [linea_reconstruccion(r) for r in self.reconstrucciones]
            out.append("")
        out += self.extra
        return "\n".join(out).rstrip() + "\n"


def _unicas(filas: list[dict]) -> list[dict]:
    vistos, out = set(), []
    for f in filas:
        if f["aid"] not in vistos:
            vistos.add(f["aid"])
            out.append(f)
    return out


def _quien(r: dict) -> str:
    ident = f" [= {r['afirmanteR']}, según reconstrucción]" if r.get("afirmanteR") else ""
    return f"«{r['afirmante']}»{ident} ({r['tipoAct']} {r['pieza']}, {r['tramo']})"


def disputa(entidad: str, atributo: str, valor_label: str | None = None) -> tuple[str, list[dict]]:
    """Agrupa las afirmaciones sobre una entidad y atributo; resume «X lo afirma, Y lo niega»."""
    filas = _unicas(consultar("afirmaciones", filtroEntidad=entidad, atributo=atr_iri(atributo)))
    if valor_label:
        filas = [f for f in filas if f["valorLabel"] == valor_label]
    if not filas:
        return "El expediente no lo dice (no hay afirmaciones registradas sobre ello).", filas
    por_valor: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    for f in filas:
        por_valor[f["valorLabel"]][f["pol"]].append(_quien(f))
    if len(por_valor) == 1:
        (v, pols), = por_valor.items()
        if pols.get("afirma") and pols.get("niega"):
            res = (f"Está en disputa («{v}»). Lo afirman: {'; '.join(pols['afirma'])}. "
                   f"Lo niegan: {'; '.join(pols['niega'])}.")
        else:
            res = f"Solo hay afirmaciones concordantes ({len(filas)}) sobre «{v}»."
    else:
        partes = []
        for v, pols in sorted(por_valor.items()):
            p = f"«{v}»: " + (f"lo afirman {'; '.join(pols['afirma'])}" if pols.get("afirma") else "nadie lo afirma")
            if pols.get("niega"):
                p += f"; lo niegan {'; '.join(pols['niega'])}"
            partes.append(p)
        res = "Está en disputa por valores incompatibles. " + " || ".join(partes)
    return res, filas


def reconstrucciones_de(entidad: str) -> list[dict]:
    return [r for r in consultar("reconstrucciones") if r["entidad"] == str(entidad)]
