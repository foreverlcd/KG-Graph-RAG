"""Prepara un expediente nuevo: esqueleto de manifiesto, carpeta de datos y vista previa de la segmentación.

Crea datos/expedientes/<id>.json (con "estado": "borrador": el corpus no lo incluye hasta que se quite esa clave),
datos/<id>/piezas.jsonl y datos/<id>/registros/anotacion.jsonl (vacíos), e imprime los tramos detectados (id,
líneas, folio, primeras palabras) para que una persona compruebe la segmentación. NO sobrescribe nada: si el
manifiesto o la carpeta ya existen, termina con error. La transcripción no se copia ni se modifica.

Uso:
  python scripts/nuevo_expediente.py <id> <ruta_transcripcion> [opciones]
  python scripts/nuevo_expediente.py <id> <ruta_transcripcion> --solo-ver [opciones]   # no escribe nada

Opciones de formato (todas opcionales; ver datos/expedientes/README.md y laad.fuente.FORMATO_POR_DEFECTO):
  --formato X          «piloto» (por defecto: unidades separadas por líneas «#»), «markdown» (cada título
                       «#», «##» o «###» inicia una unidad; preámbulo YAML y comentarios HTML ignorados), o un
                       objeto JSON con las claves de «formato» (texto o ruta de un archivo .json)
  --separador RX       línea que separa unidades («no» = sin separadores)
  --encabezado RX      línea que inicia una unidad
  --marca-folio RX     marca de folio con un grupo que captura el folio
  --ignorar RX         texto editorial no citable (repetible)
  --codificacion C     codificación del archivo (por defecto utf-8-sig)
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from laad import fuente  # noqa: E402

PREAJUSTES = {
    "piloto": {},
    "markdown": {"separador": None, "encabezado": r"^#{1,3} ",
                 "ignorar": [r"(?s)\A---\n.*?\n---\n", r"(?s)<!--.*?-->"]},
}
POR_CURAR = "POR CURAR"


def leer_formato(valor: str | None) -> dict:
    """«piloto», «markdown», un objeto JSON o la ruta de un .json con las claves de «formato»."""
    if not valor:
        return {}
    if valor in PREAJUSTES:
        return dict(PREAJUSTES[valor])
    texto = pathlib.Path(valor).read_text(encoding="utf-8") if not valor.lstrip().startswith("{") else valor
    fmt = json.loads(texto)
    if not isinstance(fmt, dict):
        raise ValueError("--formato debe ser un objeto JSON")
    return fmt


def esqueleto(exp: str, transcripcion: str, fmt: dict, datos: str) -> dict:
    """Manifiesto mínimo. Lo marcado «POR CURAR» lo completa una persona (datos/expedientes/README.md)."""
    m = {
        "id": exp,
        "estado": "borrador",
        "descripcion": f"{POR_CURAR}: fondo, sección, serie, legajo, expediente y año",
        "transcripcion": transcripcion,
        "marcas_folio": [],
        "jerarquia": [
            {"id": f"arc/expediente/{exp}", "tipo": "rst:File", "titulo": f"{POR_CURAR}: título del expediente",
             "padre": None},
        ],
        "piezas": f"{datos}/piezas.jsonl",
        "registros": [f"{datos}/registros/anotacion.jsonl"],
        "fechas": None,
        "lote": {"nombre": f"{POR_CURAR}-nombre-del-lote", "agente": POR_CURAR, "tipo_agente": "Person",
                 "plan": "anotacion-manual", "fecha": f"{POR_CURAR}: AAAA-MM-DDT00:00:00"},
        "signatura_catalogo": None,
    }
    if fmt:
        m["formato"] = fmt
    return m


def vista_previa(tramos) -> str:
    """Tabla de tramos para revisar la segmentación a ojo."""
    lineas = [f"{'tramo':<10} {'líneas':<11} {'folio':<9} {'caract.':>7}  comienzo",
              f"{'-' * 10} {'-' * 11} {'-' * 9} {'-' * 7}  {'-' * 40}"]
    for t in tramos:
        x = fuente.colapsar(t.texto)
        lineas.append(f"{t.id:<10} {f'{t.linea_inicio}-{t.linea_fin}':<11} {t.folio or 'no consta':<9} "
                      f"{len(x):>7}  {x[:60]}")
    con_folio = sum(1 for t in tramos if t.folio)
    lineas.append(f"{len(tramos)} tramos en {len({t.ut for t in tramos})} unidades; {con_folio} con folio explícito")
    return "\n".join(lineas)


def segmentar(ruta: pathlib.Path, fmt: dict):
    f = fuente.formato_completo(fmt)
    return fuente.segmentar(fuente.texto_canonico(ruta, f["codificacion"]), (), fmt)


def crear(exp: str, transcripcion: pathlib.Path, fmt: dict | None = None, *, manifiestos: pathlib.Path | None = None,
          datos: pathlib.Path | None = None, raiz: pathlib.Path = RAIZ) -> pathlib.Path:
    """Escribe el manifiesto y la carpeta de datos del expediente; devuelve la ruta del manifiesto.
    FileExistsError si el manifiesto o la carpeta ya existen (nunca se sobrescribe)."""
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", exp):
        raise ValueError(f"identificador no válido: {exp!r} (minúsculas, cifras y guiones, p. ej. co-70-15)")
    manifiestos = manifiestos or fuente.MANIFIESTOS
    datos = datos or raiz / "datos" / exp
    destino = manifiestos / f"{exp}.json"
    transcripcion = transcripcion.resolve()
    if not transcripcion.is_file():
        raise FileNotFoundError(f"no existe la transcripción {transcripcion}")
    for existente in (destino, datos):
        if existente.exists():
            raise FileExistsError(f"ya existe {existente}: no se sobrescribe")
    fmt = fmt or {}
    segmentar(transcripcion, fmt)          # valida el formato y la codificación ANTES de escribir nada

    def rel(p: pathlib.Path) -> str:       # rutas relativas a la raíz del repositorio siempre que se pueda
        try:
            return p.relative_to(raiz).as_posix()
        except ValueError:
            return str(p)

    manifiestos.mkdir(parents=True, exist_ok=True)
    (datos / "registros").mkdir(parents=True)
    (datos / "piezas.jsonl").write_text("", encoding="utf-8")
    (datos / "registros" / "anotacion.jsonl").write_text("", encoding="utf-8")
    destino.write_text(json.dumps(esqueleto(exp, rel(transcripcion), fmt, rel(datos)), ensure_ascii=False, indent=2)
                       + "\n", encoding="utf-8")
    return destino


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("id")
    ap.add_argument("transcripcion", type=pathlib.Path)
    ap.add_argument("--formato")
    ap.add_argument("--separador")
    ap.add_argument("--encabezado")
    ap.add_argument("--marca-folio", dest="marca_folio")
    ap.add_argument("--ignorar", action="append")
    ap.add_argument("--codificacion")
    ap.add_argument("--solo-ver", action="store_true", help="solo imprime la segmentación; no escribe nada")
    a = ap.parse_args(argv)
    try:
        fmt = leer_formato(a.formato)
        for clave in ("separador", "encabezado", "marca_folio", "codificacion"):
            v = getattr(a, clave)
            if v is not None:
                fmt[clave] = None if v.lower() in ("no", "null", "none", "") else v
        if a.ignorar:
            fmt["ignorar"] = list(fmt.get("ignorar") or []) + a.ignorar
        tramos = segmentar(a.transcripcion, fmt)
        destino = None if a.solo_ver else crear(a.id, a.transcripcion, fmt)
    except (ValueError, OSError, LookupError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    print(vista_previa(tramos))
    if not tramos:
        print("AVISO: no se detectó ningún tramo; revise la codificación y el formato.", file=sys.stderr)
    if destino is None:
        print("\n(--solo-ver: no se ha escrito nada)")
        return 0
    print(f"\nescrito {destino} (estado: borrador) y {RAIZ / 'datos' / a.id}/")
    print("Siguiente: revise la tabla, cure el manifiesto y siga datos/expedientes/README.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
