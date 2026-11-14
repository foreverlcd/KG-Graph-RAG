"""Integra en la capa 4 las propuestas de conectividad de datos/propuestas/ (determinista e idempotente).

Entradas (se conservan en el repositorio como registro de lo propuesto):
  datos/propuestas/personas.jsonl, entidades.jsonl, hechos.jsonl — reconstrucciones nuevas o ampliadas
  datos/propuestas/tipos_entidad.csv        — tipo de entidad propuesto para menciones que no lo tenían
  datos/propuestas/candidatos_propuestos.csv — conceptos candidatos y las menciones que los usarían

Efectos:
  * datos/reconstrucciones.jsonl: cada propuesta sustituye a la reconstrucción del mismo id o se añade al final.
    Una reconstrucción ampliada queda a nombre de quien la amplió, con la fecha de la ampliación; el autor
    original debe quedar nombrado en el argumento (se comprueba).
  * datos/registros/expediente_*.py: se añade tipo="…" a las menciones indicadas (nunca se cambia uno existente).
  * datos/candidatos_tesauro.csv: se añaden los candidatos que falten.
Después hay que ejecutar los generadores de registros, scripts/candidatos.py, scripts/construir.py y scripts/cifras.py.

Uso: python scripts/integrar_propuestas.py [--comprobar]
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PROP = RAIZ / "datos/propuestas"
REC = RAIZ / "datos/reconstrucciones.jsonl"
CAND = RAIZ / "datos/candidatos_tesauro.csv"
AUTOR = "claude-fable-5-2"
FECHA = "2026-11-14"


def _jsonl(p: Path) -> list[dict]:
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def reconstrucciones() -> tuple[list[dict], list[str]]:
    actuales = _jsonl(REC)
    por_id = {r["id"]: i for i, r in enumerate(actuales)}
    avisos = []
    for nombre in ("personas", "entidades", "hechos"):
        for p in _jsonl(PROP / f"{nombre}.jsonl"):
            if p["id"] in por_id:
                viejo = actuales[por_id[p["id"]]]
                if viejo == p or (viejo["autor"] == AUTOR and viejo["fecha"] == FECHA
                                  and set(p.get("menciones", [])) <= set(viejo.get("menciones", []))):
                    continue      # ya integrada
                perdidas = set(viejo.get("menciones", [])) - set(p.get("menciones", []))
                if perdidas:
                    avisos.append(f"{p['id']}: la propuesta quita menciones {sorted(perdidas)}")
                if viejo["autor"] != AUTOR:
                    if viejo["autor"] not in p["argumento"]:
                        p["argumento"] += f" Reconstrucción propuesta originalmente por {viejo['autor']} el {viejo['fecha']}."
                    p["autor"], p["fecha"] = AUTOR, FECHA
                actuales[por_id[p["id"]]] = {**viejo, **p}
            else:
                por_id[p["id"]] = len(actuales)
                actuales.append(p)
    return actuales, avisos


def tipos() -> dict[str, str]:
    """mención (sin calificar) → tipo de entidad propuesto."""
    t: dict[str, str] = {}
    with open(PROP / "tipos_entidad.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            t[r["mencion"].split(":", 1)[1]] = r["tipo_entidad_propuesto"]
    with open(PROP / "candidatos_propuestos.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            for m in r["menciones_que_lo_usarian"].split():
                t[m.split(":", 1)[1]] = r["local"]
    return t


def aplicar_tipos(t: dict[str, str]) -> tuple[dict[Path, str], list[str]]:
    salidas, avisos, vistos = {}, [], set()
    for ruta in sorted((RAIZ / "datos/registros").glob("expediente_*.py")):
        lineas = ruta.read_text(encoding="utf-8").split("\n")
        i = 0
        while i < len(lineas):
            mm = re.match(r'm\("(M-[^"]+)"', lineas[i])
            if mm and mm.group(1) in t:
                j = i
                while not lineas[j].rstrip().endswith(")"):
                    j += 1
                bloque = "\n".join(lineas[i:j + 1])
                vistos.add(mm.group(1))
                puesto = re.search(r'tipo="([^"]+)"', bloque)
                if puesto:
                    if puesto.group(1) != t[mm.group(1)]:
                        avisos.append(f"{mm.group(1)}: ya tiene tipo «{puesto.group(1)}»; no se cambia a «{t[mm.group(1)]}»")
                else:
                    lineas[j] = lineas[j].rstrip()[:-1] + f', tipo="{t[mm.group(1)]}")'
                i = j
            i += 1
        salidas[ruta] = "\n".join(lineas)
    avisos += [f"{m}: mención no encontrada en los generadores" for m in sorted(set(t) - vistos)]
    return salidas, avisos


def candidatos() -> str:
    with open(CAND, encoding="utf-8", newline="") as f:
        filas = list(csv.DictReader(f))
        columnas = list(filas[0].keys())
    hay = {(r["esquema"], r["local"]) for r in filas}
    with open(PROP / "candidatos_propuestos.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r["esquema"], r["local"]) not in hay:
                filas.append(dict(esquema=r["esquema"], local=r["local"], etiqueta=r["etiqueta"],
                                  definicion=r["definicion"], broader=r["broader"],
                                  propuesto_por=f"{AUTOR} (conectividad de entidades)", fecha=FECHA,
                                  expediente="cc-14-18", ejemplo=r["ejemplo"], estado="candidato", reemplazado_por=""))
    import io
    s = io.StringIO()
    w = csv.DictWriter(s, fieldnames=columnas, lineterminator="\n")
    w.writeheader()
    w.writerows(filas)
    return s.getvalue()


if __name__ == "__main__":
    recs, avisos = reconstrucciones()
    salidas, av2 = aplicar_tipos(tipos())
    salidas[REC] = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in recs)
    salidas[CAND] = candidatos()
    for a in avisos + av2:
        print("AVISO", a)
    pendientes = [p for p, txt in salidas.items() if p.read_text(encoding="utf-8") != txt]
    if "--comprobar" in sys.argv:
        print("pendiente de integrar:" if pendientes else "propuestas integradas", *[p.relative_to(RAIZ) for p in pendientes])
        sys.exit(1 if pendientes else 0)
    for p in pendientes:
        p.write_text(salidas[p], encoding="utf-8")
        print("escrito", p.relative_to(RAIZ))
    print(f"{len(recs)} reconstrucciones")
