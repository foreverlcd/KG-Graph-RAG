"""Responde una consulta con nombre desde la línea de órdenes, con el corpus cargado en Oxigraph.

Uso:
  python scripts/servir.py                                   # lista las consultas con nombre
  python scripts/servir.py piezas expediente=cc-14-18
  python scripts/servir.py afirmaciones expediente=cc-14-18 atributo=redacto filtroEntidad=persona/huancachoque
  python scripts/servir.py procedencia x=cc-14-18/afirmacion/A-UT01-001 --json
  python scripts/servir.py --volcar /ruta/almacen            # escribe un almacén Oxigraph persistente en disco
  python scripts/servir.py --almacen /ruta/almacen piezas    # consulta ese almacén sin volver a cargar el corpus

Parámetros (clave=valor): `expediente` admite el identificador (cc-14-18); `atributo`, el nombre local del tesauro
(redacto); cualquier otro, un IRI completo o una ruta relativa a https://w3id.org/laad/id/ (persona/huancachoque,
cc-14-18/mencion/M-UT01-003). Varios valores separados por comas. Opciones: --json (filas en JSON), --tsv,
--motor rdflib (motor de referencia, lento), --grafo DIR (otro directorio de .nq/.trig; por defecto datos/grafo).
No es un servidor HTTP: cada invocación carga el corpus (décimas de segundo) o abre el almacén en disco.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import time

RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from laad import consulta, fuente  # noqa: E402


def iri(clave: str, valor: str) -> str:
    if valor.startswith(("http://", "https://")):
        return valor
    if clave == "expediente":
        if valor not in fuente.expedientes(borradores=True):
            raise ValueError(f"expediente desconocido: {valor!r} (hay: {', '.join(fuente.expedientes())})")
        return str(consulta.expediente(valor))
    if clave == "atributo":
        return str(consulta.atributo(valor))
    return consulta.ID + valor


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("consulta", nargs="?")
    ap.add_argument("parametros", nargs="*", metavar="clave=valor")
    ap.add_argument("--volcar", type=pathlib.Path, metavar="DIR")
    ap.add_argument("--almacen", type=pathlib.Path, metavar="DIR")
    ap.add_argument("--grafo", type=pathlib.Path, default=consulta.GRAFO, metavar="DIR")
    ap.add_argument("--motor", choices=consulta.MOTORES)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--tsv", action="store_true")
    a = ap.parse_args(argv)
    if a.motor:
        os.environ["LAAD_MOTOR"] = a.motor
    if a.volcar:
        if a.volcar.exists() and any(a.volcar.iterdir()):
            print(f"ERROR: {a.volcar} ya existe y no está vacío: no se sobrescribe", file=sys.stderr)
            return 1
        t = time.perf_counter()
        store = consulta.nuevo_almacen(a.grafo, persistente=a.volcar, masivo=True)
        print(f"almacén Oxigraph escrito en {a.volcar}: {len(store)} cuádruplas (grafos nombrados + su unión en el "
              f"grafo por defecto), {time.perf_counter() - t:.2f} s", file=sys.stderr)
        del store
        if not a.consulta:
            return 0
        a.almacen = a.volcar
    if not a.consulta:
        print("consultas con nombre: " + ", ".join(consulta.nombres()))
        return 0
    if a.consulta not in consulta.nombres():
        print(f"ERROR: no existe la consulta {a.consulta!r}; hay: {', '.join(consulta.nombres())}", file=sys.stderr)
        return 2
    params: dict = {}
    for par in a.parametros:
        clave, sep, valor = par.partition("=")
        if not sep or not valor:
            print(f"ERROR: parámetro mal formado {par!r} (se espera clave=valor)", file=sys.stderr)
            return 2
        try:
            valores = [iri(clave, v) for v in valor.split(",")]
        except ValueError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 2
        params[clave] = valores if len(valores) > 1 else valores[0]
    t0 = time.perf_counter()
    if a.almacen:
        ds = consulta.abrir_almacen(a.almacen)
    elif consulta.motor() == "rdflib":
        ds = consulta.dataset(a.grafo)
    else:
        ds = consulta.almacen(a.grafo)
    t1 = time.perf_counter()
    try:
        filas = consulta.consultar(a.consulta, ds, **params)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    t2 = time.perf_counter()
    if a.json:
        print(json.dumps(filas, ensure_ascii=False, indent=1))
    elif a.tsv:
        if filas:
            print("\t".join(filas[0]))
        for f in filas:
            print("\t".join("" if v is None else v.replace("\t", " ").replace("\n", " ") for v in f.values()))
    else:
        for i, f in enumerate(filas, 1):
            print(f"— {i}")
            for k, v in f.items():
                if v is not None:
                    print(f"  {k}: {v}")
    print(f"{len(filas)} filas; carga {t1 - t0:.3f} s, consulta {t2 - t1:.3f} s "
          f"(motor: {'oxigraph (disco)' if a.almacen else consulta.motor()})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
