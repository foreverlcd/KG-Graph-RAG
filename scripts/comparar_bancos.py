"""Compara varias ejecuciones del banco del agente (informes datos/evaluacion/agente_*.jsonl): medias y
dispersión de las PC completas, con lo esencial correcto, con la forma correcta y verificadas, y estabilidad por PC.

    python scripts/comparar_bancos.py datos/evaluacion/agente_…_r1.jsonl datos/evaluacion/agente_…_r2.jsonl …

«Esencial»: la ejecución no tiene más fallos que citas o ids periféricos de la referencia (la forma, las
afirmaciones, los afirmantes, las reconstrucciones y las participaciones están; la respuesta está verificada).
"""
import json
import pathlib
import re
import statistics
import sys

PERIFERICO = re.compile(r"\d+ citas de la referencia|ids de afirmación de la referencia|\d+ ids de la referencia")


def medir(ruta: pathlib.Path) -> dict[str, dict]:
    out = {}
    for x in ruta.read_text(encoding="utf-8").splitlines():
        d = json.loads(x)
        if "fallos" not in d:                     # error del proveedor (cuota): la PC no se midió
            continue
        out[d["pc"]] = {"completa": d["alcanzada"],
                        "esencial": not [f for f in d["fallos"] if not PERIFERICO.match(f)],
                        "forma": d["forma"] == d["forma_referencia"], "verificada": d["estado"] == "verificada",
                        "tokens": d["tokens_entrada"] + d["tokens_salida"], "pasos": d["pasos"]}
    return out


def main(rutas: list[str]) -> int:
    ejecuciones = [(pathlib.Path(r).name, medir(pathlib.Path(r))) for r in rutas]
    print(f"{'ejecución':70} PC  compl. esenc. forma verif. tokens/PC")
    for nombre, m in ejecuciones:
        n = len(m)
        print(f"{nombre[:70]:70} {n:2}  {sum(x['completa'] for x in m.values()):5} {sum(x['esencial'] for x in m.values()):6} "
              f"{sum(x['forma'] for x in m.values()):5} {sum(x['verificada'] for x in m.values()):6} "
              f"{statistics.mean(x['tokens'] for x in m.values()) if m else 0:9.0f}")
    if len(ejecuciones) > 1:
        print("\nmedia ± desviación (sobre las ejecuciones con las 20 PC medidas):")
        llenas = [m for _, m in ejecuciones if len(m) == 20]
        for k in ("completa", "esencial", "forma", "verificada"):
            v = [sum(x[k] for x in m.values()) for m in llenas]
            if v:
                print(f"  {k:10} {statistics.mean(v):5.1f} ± {statistics.pstdev(v):.1f}   ({', '.join(map(str, v))})")
        pcs = sorted({pc for _, m in ejecuciones for pc in m})
        print("\nlo esencial por PC (✓ correcto, · no, - sin medir):")
        for pc in pcs:
            marcas = "".join("-" if pc not in m else "✓" if m[pc]["esencial"] else "·" for _, m in ejecuciones)
            print(f"  {pc}  {marcas}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
