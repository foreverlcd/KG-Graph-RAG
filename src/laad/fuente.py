"""Capa 0 — acceso a la fuente de verdad (transcripción paleográfica).

Reglas (ver docs/01_materiales.md y docs/decisiones/ADR-002-citas.md):
* La única fuente citable es corpus/Transcripcion_CC_L14E18.txt.
* El texto se carga sin tocar: solo se quita el BOM y se convierte CRLF→LF.
* Unidad de transcripción (UT): bloque entre líneas '#'. Probablemente una imagen
  o página del original; NO es un folio. UT00 = carátula.
* Tramo: parte de una UT delimitada por una marca de folio explícita escrita por el
  transcriptor ('Folio 20', 'folio 28', 'Folio 33', '[Folio 34 ]'). Solo los tramos
  que siguen a una marca tienen folio explícito; el resto queda "no consta".
  Recto/vuelto no consta en ningún punto de la transcripción.
* Una cita es válida si, tras colapsar secuencias de espacios en blanco a un solo
  espacio (única normalización permitida: la transcripción parte líneas a mitad de
  frase), es subcadena exacta del tramo indicado. Sin plegar mayúsculas, acentos
  ni grafías.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
TRANSCRIPCION = RAIZ / "corpus" / "Transcripcion_CC_L14E18.txt"

# Marca de folio escrita por el transcriptor. Se exige la palabra "folio" seguida de
# número; se excluyen referencias internas del propio documento ("a folios 2",
# "de folio 4", "En folio 10") mediante la lista explícita de abajo, verificada a mano.
MARCAS_FOLIO = [
    # (UT, texto exacto de la marca, folio)
    ("UT12", "Folio 20", "20"),
    ("UT16", "folio 28", "28"),
    ("UT19", "Folio 33", "33"),
    ("UT20", "[Folio 34 ]", "34"),
]

_WS = re.compile(r"\s+")


def colapsar(texto: str) -> str:
    return _WS.sub(" ", texto).strip()


@dataclass(frozen=True)
class Tramo:
    id: str                 # p. ej. "UT12.b"
    ut: str                 # "UT12"
    inicio: int             # desplazamiento en el texto canónico (LF, sin BOM)
    fin: int
    linea_inicio: int       # 1-based, en el texto canónico
    linea_fin: int
    folio: str | None       # folio explícito o None ("no consta")
    marca: str | None       # texto de la marca que abre el tramo
    texto: str = field(repr=False)


def texto_canonico(ruta: Path = TRANSCRIPCION) -> str:
    return ruta.read_text(encoding="utf-8-sig").replace("\r\n", "\n")


def sha256(ruta: Path = TRANSCRIPCION) -> str:
    return hashlib.sha256(ruta.read_bytes()).hexdigest()


def _linea(texto: str, pos: int) -> int:
    return texto.count("\n", 0, pos) + 1


@lru_cache(maxsize=4)
def tramos(ruta: Path = TRANSCRIPCION) -> tuple[Tramo, ...]:
    t = texto_canonico(ruta)
    # 1) unidades de transcripción
    uts: list[tuple[str, int, int]] = []
    pos, n = 0, 0
    for m in re.finditer(r"(?m)^[ \t]*#[ \t]*$", t):
        uts.append((f"UT{n:02d}", pos, m.start()))
        pos, n = m.end(), n + 1
    uts.append((f"UT{n:02d}", pos, len(t)))
    # 2) cortes por marcas de folio
    res: list[Tramo] = []
    for ut, a, b in uts:
        cortes = []
        for ut_m, marca, folio in MARCAS_FOLIO:
            if ut_m == ut:
                k = t.find(marca, a, b)
                if k < 0:
                    raise ValueError(f"Marca {marca!r} no encontrada en {ut}")
                cortes.append((k, marca, folio))
        cortes.sort()
        limites = [(a, None, None)] + cortes
        partes = []
        for i, (ini, marca, folio) in enumerate(limites):
            fin = limites[i + 1][0] if i + 1 < len(limites) else b
            if colapsar(t[ini:fin]):          # se descartan tramos vacíos
                partes.append((ini, fin, marca, folio))
        for i, (ini, fin, marca, folio) in enumerate(partes):
            sufijo = "" if len(partes) == 1 else "." + "abcdefgh"[i]
            res.append(Tramo(
                id=ut + sufijo, ut=ut, inicio=ini, fin=fin,
                linea_inicio=_linea(t, ini), linea_fin=_linea(t, max(ini, fin - 1)),
                folio=folio, marca=marca, texto=t[ini:fin]))
    return tuple(res)


def tramo(id_: str) -> Tramo:
    for tr in tramos():
        if tr.id == id_:
            return tr
    raise KeyError(id_)


@dataclass(frozen=True)
class ResultadoCita:
    valida: bool
    tramo: str
    ocurrencias_en_tramo: int
    tramos_donde_aparece: tuple[str, ...]
    inicio: int | None   # desplazamiento en el texto canónico (aprox. si hubo colapso)
    motivo: str = ""


def _mapa_colapsado(texto: str) -> tuple[str, list[int]]:
    """Texto con espacios colapsados y mapa índice_colapsado -> índice_original."""
    out, idx, prev_ws = [], [], False
    for i, ch in enumerate(texto):
        if ch.isspace():
            if not prev_ws:
                out.append(" ")
                idx.append(i)
            prev_ws = True
        else:
            out.append(ch)
            idx.append(i)
            prev_ws = False
    return "".join(out), idx


def verificar_cita(cita: str, tramo_id: str) -> ResultadoCita:
    c = colapsar(cita)
    if len(c) < 8:
        return ResultadoCita(False, tramo_id, 0, (), None, "cita demasiado corta (<8)")
    donde = []
    for tr in tramos():
        if c in colapsar(tr.texto):
            donde.append(tr.id)
    try:
        tr = tramo(tramo_id)
    except KeyError:
        return ResultadoCita(False, tramo_id, 0, tuple(donde), None, "tramo inexistente")
    col, idx = _mapa_colapsado(tr.texto)
    k = col.find(c)
    n = col.count(c)
    if k < 0:
        motivo = ("la cita existe en otro tramo: " + ", ".join(donde)) if donde else \
                 "la cita no es subcadena de la transcripción paleográfica"
        return ResultadoCita(False, tramo_id, 0, tuple(donde), None, motivo)
    return ResultadoCita(True, tramo_id, n, tuple(donde), tr.inicio + idx[k])
