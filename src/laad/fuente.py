"""Capa 0 — acceso a la fuente de verdad (transcripción paleográfica).

Reglas (ver docs/01_materiales.md y docs/decisiones/ADR-002-citas.md):
* La única fuente citable de cada expediente es la transcripción paleográfica que nombra su manifiesto
  (datos/expedientes/<exp>.json); el expediente en curso lo fija usando_expediente(exp).
* El texto se carga sin tocar: solo se quita el BOM y se convierte CRLF→LF.
* Unidad de transcripción (UT): por defecto, bloque entre líneas '#'. Probablemente una imagen
  o página del original; NO es un folio. UT00 = lo anterior al primer corte (la carátula en el piloto).
* Tramo: parte de una UT delimitada por una marca de folio explícita escrita por el
  transcriptor (p. ej. 'Folio 20', '[Folio 34 ]'). Solo los tramos
  que siguen a una marca tienen folio explícito; el resto queda "no consta".
  Recto/vuelto no consta en ningún punto de la transcripción del piloto.
* Cómo se corta cada transcripción lo declara su manifiesto: las marcas de folio verificadas a mano
  («marcas_folio») y, si la transcripción sigue otra convención (Markdown, marcas de folio regulares, otra
  codificación, líneas editoriales), la clave opcional «formato» (ver FORMATO_POR_DEFECTO y formato()).
* Una cita es válida si, tras colapsar secuencias de espacios en blanco a un solo
  espacio (única normalización permitida: la transcripción parte líneas a mitad de
  frase), es subcadena exacta del tramo indicado. Sin plegar mayúsculas, acentos
  ni grafías.
"""
from __future__ import annotations

import contextvars
import hashlib
import json
import re
from contextlib import contextmanager
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
MANIFIESTOS = RAIZ / "datos" / "expedientes"
# Expediente que rige cuando nadie fija el contexto (usando_expediente): el piloto. Es solo una comodidad para
# las utilidades de una sola fuente (verificar una cita suelta); todo lo que construye el grafo fija el contexto.
EXPEDIENTE_POR_DEFECTO = "cc-14-18"
_EXPEDIENTE = contextvars.ContextVar("expediente", default=EXPEDIENTE_POR_DEFECTO)


def manifiesto(exp: str | None = None) -> dict:
    """Manifiesto del expediente: la ÚNICA fuente de su configuración (transcripción, marcas de folio verificadas
    a mano, jerarquía archivística, piezas, registros, fechas, procedencia del lote y signatura en el catálogo).
    Todo lo que es propio de un expediente vive aquí, no en el código (revisión C2)."""
    return _manifiesto(MANIFIESTOS, exp or _EXPEDIENTE.get())


@lru_cache(maxsize=None)
def _manifiesto(directorio: Path, exp: str) -> dict:
    ruta = directorio / f"{exp}.json"
    if not ruta.exists():
        raise KeyError(f"expediente desconocido: {exp!r} (no existe {ruta})")
    return json.loads(ruta.read_text(encoding="utf-8"))


def expedientes(borradores: bool = False) -> list[str]:
    """Identificadores de los expedientes con manifiesto, en orden alfabético. Un manifiesto con
    "estado": "borrador" (el esqueleto que deja scripts/nuevo_expediente.py) aún no forma parte del corpus: solo se
    lista con borradores=True. Sus tramos y citas sí se pueden consultar y verificar por su identificador."""
    ids = sorted(p.stem for p in MANIFIESTOS.glob("*.json"))
    return ids if borradores else [e for e in ids if _manifiesto(MANIFIESTOS, e).get("estado") != "borrador"]


def expediente_actual() -> str:
    return _EXPEDIENTE.get()


@contextmanager
def usando_expediente(exp: str):
    tok = _EXPEDIENTE.set(exp)
    try:
        yield
    finally:
        _EXPEDIENTE.reset(tok)


def ruta(relativa: str | Path) -> Path:
    """Ruta de un archivo citado en un manifiesto: relativa a la raíz del repositorio (o absoluta)."""
    return RAIZ / relativa


def ruta_transcripcion(exp: str | None = None) -> Path:
    return ruta(manifiesto(exp)["transcripcion"])


def marcas_folio(exp: str | None = None) -> list[tuple[str, str, str]]:
    """(UT, texto exacto de la marca, folio). Las referencias internas del documento («a folios 2»,
    «De folio 4», «En folio 10») NO son marcas del transcriptor y no figuran aquí."""
    return [tuple(x) for x in manifiesto(exp)["marcas_folio"]]


# Claves de «formato» en el manifiesto (todas opcionales; sin «formato» rige esta convención, la del piloto).
# Las expresiones regulares son de Python (módulo re) y se aplican con re.MULTILINE: ^ y $ casan en cada línea.
FORMATO_POR_DEFECTO: dict = {
    # Codificación del archivo. «utf-8-sig» lee UTF-8 con o sin BOM; otras: «latin-1», «cp1252»…
    "codificacion": "utf-8-sig",
    # Línea SEPARADORA de unidades: la línea casada no pertenece a ninguna unidad (no es citable).
    # null = la transcripción no usa separadores.
    "separador": r"^[ \t]*#[ \t]*$",
    # Línea de ENCABEZADO: INICIA una unidad y pertenece a ella (es citable). P. ej. Markdown «^#{1,3} » o
    # «^\[?[Ff]olio \d+». null = no hay encabezados. Puede combinarse con «separador».
    "encabezado": None,
    # Marca de folio escrita por el transcriptor, detectada automáticamente: expresión con UN grupo que captura el
    # folio (o un grupo con nombre (?P<folio>…)), p. ej. «^\[f\. ?(\d+[rv]?)\]». Cada coincidencia abre un tramo
    # con ese folio, igual que una entrada de «marcas_folio». CUIDADO: una expresión laxa toma por marcas las
    # referencias internas del documento («a folios 2»); ánclela al comienzo de línea y revise la salida de
    # scripts/nuevo_expediente.py. null = solo valen las marcas listadas a mano en «marcas_folio».
    "marca_folio": None,
    # Texto EDITORIAL que no es transcripción (preámbulo YAML, notas del editor, comentarios, números de imagen):
    # una expresión o una lista de expresiones. Lo casado se sustituye por espacios en el texto citable (los
    # desplazamientos y los números de línea no cambian): ninguna cita puede contenerlo, ni corta unidades ni cuenta
    # como marca. Una cita sí puede continuar al otro lado de una línea ignorada, como al otro lado de un salto de
    # línea. P. ej. «(?s)\A---\n.*?\n---\n» (preámbulo YAML), «^> .*$» (notas), «(?s)<!--.*?-->» (comentarios).
    "ignorar": None,
}


def formato(exp: str | None = None) -> dict:
    """Convención de la transcripción del expediente: FORMATO_POR_DEFECTO con lo que sobrescriba la clave
    «formato» de su manifiesto. Una clave desconocida es un error (no se ignora en silencio una errata)."""
    return formato_completo(manifiesto(exp).get("formato"))


def formato_completo(fmt: dict | None = None) -> dict:
    """FORMATO_POR_DEFECTO con lo que sobrescriba `fmt`, validado («ignorar» siempre como tupla)."""
    return dict(_formato(_congelar(fmt or {})))


def _congelar(f: dict) -> tuple:
    return tuple(sorted((k, tuple(v) if isinstance(v, list) else v) for k, v in f.items()))


def _formato(declarado: tuple) -> tuple:
    """Formato completo y validado (claves conocidas, expresiones que compilan), en forma hashable."""
    f = dict(FORMATO_POR_DEFECTO)
    for k, v in declarado:
        if k not in FORMATO_POR_DEFECTO:
            raise ValueError(f"clave de «formato» desconocida: {k!r} (válidas: {', '.join(FORMATO_POR_DEFECTO)})")
        f[k] = v
    if not isinstance(f["codificacion"], str):
        raise ValueError("formato.codificacion debe ser el nombre de una codificación")
    for k in ("separador", "encabezado", "marca_folio"):
        if f[k] is not None:
            _regex(k, f[k])
    if f["marca_folio"] is not None and _regex("marca_folio", f["marca_folio"]).groups < 1:
        raise ValueError("formato.marca_folio debe tener un grupo que capture el folio, p. ej. «[Ff]olio (\\d+)»")
    ign = f["ignorar"]
    f["ignorar"] = () if ign is None else (ign,) if isinstance(ign, str) else tuple(ign)
    for x in f["ignorar"]:
        _regex("ignorar", x)
    return tuple(sorted(f.items()))


def _regex(clave: str, patron: str) -> re.Pattern:
    try:
        return re.compile(patron, re.MULTILINE)
    except (re.error, TypeError) as e:
        raise ValueError(f"formato.{clave}: expresión regular no válida {patron!r}: {e}") from None


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


def texto_canonico(ruta: Path | None = None, codificacion: str | None = None) -> str:
    """Texto de la transcripción tal cual, sin BOM y con CRLF→LF: a él se refieren desplazamientos y líneas.
    Sin argumentos, la transcripción del expediente en curso con la codificación de su «formato»."""
    if ruta is None:
        ruta, codificacion = ruta_transcripcion(), codificacion or formato()["codificacion"]
    return ruta.read_text(encoding=codificacion or FORMATO_POR_DEFECTO["codificacion"]).replace("\r\n", "\n")


def sha256(ruta: Path | None = None) -> str:
    return _sha256(ruta or ruta_transcripcion())


@lru_cache(maxsize=None)
def _sha256(ruta: Path) -> str:
    return hashlib.sha256(ruta.read_bytes()).hexdigest()


def _linea(texto: str, pos: int) -> int:
    return texto.count("\n", 0, pos) + 1


def tramos(exp: str | None = None) -> tuple[Tramo, ...]:
    return _tramos(ruta_transcripcion(exp), tuple(marcas_folio(exp)),
                   _formato(_congelar(manifiesto(exp).get("formato") or {})))


def _sufijo(i: int) -> str:
    """a, b, …, z, aa, ab, … (partes de una unidad cortada por marcas de folio)."""
    s = ""
    while True:
        s = "abcdefghijklmnopqrstuvwxyz"[i % 26] + s
        i = i // 26 - 1
        if i < 0:
            return s


def _citable(t: str, ignorar: tuple[str, ...]) -> str:
    """El texto con lo editorial («formato.ignorar») sustituido por espacios: misma longitud, mismas líneas."""
    for patron in ignorar:
        t = _regex("ignorar", patron).sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), t)
    return t


def segmentar(t: str, marcas: tuple[tuple[str, str, str], ...] = (), fmt: dict | None = None) -> tuple[Tramo, ...]:
    """Corta el texto canónico `t` en tramos según un «formato» (por defecto, el del piloto) y unas marcas de
    folio listadas a mano. Función pura: la usan tramos() y scripts/nuevo_expediente.py (vista previa)."""
    f = formato_completo(fmt)
    t = _citable(t, f["ignorar"])
    # 1) unidades de transcripción: cortes por separador (la línea no pertenece a nadie) y por encabezado (inicia)
    cortes_ut: list[tuple[int, int]] = []            # (fin de la unidad anterior, inicio de la siguiente)
    if f["separador"]:
        cortes_ut += [(m.start(), m.end()) for m in _regex("separador", f["separador"]).finditer(t)]
    if f["encabezado"]:
        cortes_ut += [(m.start(), m.start()) for m in _regex("encabezado", f["encabezado"]).finditer(t)]
    cortes_ut.sort()
    uts: list[tuple[str, int, int]] = []
    pos, n = 0, 0
    for a, b in cortes_ut:
        if a < pos:                                  # coincidencia dentro de un separador ya consumido
            continue
        uts.append((f"UT{n:02d}", pos, a))
        pos, n = b, n + 1
    uts.append((f"UT{n:02d}", pos, len(t)))
    # 2) cortes por marcas de folio: las del manifiesto (a mano) y las que detecta formato.marca_folio
    auto = []
    if f["marca_folio"]:
        rx = _regex("marca_folio", f["marca_folio"])
        for m in rx.finditer(t):
            folio = m.group("folio") if "folio" in rx.groupindex else m.group(1)
            if folio is not None:
                auto.append((m.start(), m.group(0), folio.strip()))
    res: list[Tramo] = []
    for ut, a, b in uts:
        cortes = {}
        for k, marca, folio in auto:
            if a <= k < b:
                cortes[k] = (k, marca, folio)
        for ut_m, marca, folio in marcas:            # las marcas a mano prevalecen sobre las detectadas
            if ut_m == ut:
                k = t.find(marca, a, b)
                if k < 0:
                    raise ValueError(f"Marca {marca!r} no encontrada en {ut}")
                cortes[k] = (k, marca, folio)
        limites = [(a, None, None)] + sorted(cortes.values())
        partes = []
        for i, (ini, marca, folio) in enumerate(limites):
            fin = limites[i + 1][0] if i + 1 < len(limites) else b
            if colapsar(t[ini:fin]):          # se descartan tramos vacíos
                partes.append((ini, fin, marca, folio))
        for i, (ini, fin, marca, folio) in enumerate(partes):
            sufijo = "" if len(partes) == 1 else "." + _sufijo(i)
            res.append(Tramo(
                id=ut + sufijo, ut=ut, inicio=ini, fin=fin,
                linea_inicio=_linea(t, ini), linea_fin=_linea(t, max(ini, fin - 1)),
                folio=folio, marca=marca, texto=t[ini:fin]))
    return tuple(res)


@lru_cache(maxsize=None)
def _tramos(transcripcion: Path, marcas: tuple[tuple[str, str, str], ...], fmt: tuple = ()) -> tuple[Tramo, ...]:
    """Caché por archivo, marcas y formato (no por identificador): dos manifiestos distintos nunca comparten
    tramos."""
    f = dict(fmt) if fmt else formato_completo()
    return segmentar(texto_canonico(transcripcion, f["codificacion"]), marcas, f)


def tramo(id_: str, exp: str | None = None) -> Tramo:
    for tr in tramos(exp):
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
