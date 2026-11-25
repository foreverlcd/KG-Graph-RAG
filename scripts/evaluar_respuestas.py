"""Evalúa respuestas redactadas por un intermediario (un modelo que consultó con scripts/preguntar.py en lugar de
hacerlo dentro de laad.agente). Cada línea del archivo:

    {"pc": "PC09", "llamadas": [{"herramienta": "buscar", "parametros": {"nombre": "Chuquitapa"}}, …],
     "respuesta": "… texto con citas …\nFORMA: DISPUTA", "modelo": "…"}

Se vuelven a ejecutar las llamadas, se verifica la respuesta contra sus filas y se mide con el mismo comprobador
y la misma cobertura que el banco del agente (scripts/agente.py --banco).

    python scripts/evaluar_respuestas.py datos/evaluacion/intermediario_<modelo>.jsonl
"""
import json
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from laad.evaluacion_harness import evaluar_respuesta  # noqa: E402


def main(ruta: str) -> int:
    lineas = [json.loads(x) for x in pathlib.Path(ruta).read_text(encoding="utf-8").splitlines() if x.strip()]
    completas = esenciales = formas = verificadas = 0
    for d in lineas:
        r = evaluar_respuesta(d["pc"], d["llamadas"], d["respuesta"])
        periferico = ("citas de la referencia", "ids de afirmación de la referencia", "ids de la referencia")
        esencial = not [f for f in r["fallos"] if not any(p in f for p in periferico)]
        completas += r["alcanzada"]; esenciales += esencial
        formas += r["forma"] == r["forma_referencia"]; verificadas += r["verificada"]
        cob = ", ".join(f"{k} {'—' if v is None else f'{v:.0%}'}" for k, v in r["cobertura"].items())
        print(f"{r['pc']}: {'COMPLETA' if r['alcanzada'] else 'ESENCIAL' if esencial else 'NO'} forma {r['forma']} "
              f"(ref. {r['forma_referencia']}), {r['llamadas']} llamadas, cobertura {cob}"
              + (f"\n    avisos: {len(r['avisos'])}" if r["avisos"] else "")
              + ("".join(f"\n    {f[:220]}" for f in r["fallos"])))
    n = len(lineas)
    print(f"\ncompletas {completas}/{n}; esencial {esenciales}/{n}; forma {formas}/{n}; verificadas {verificadas}/{n}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
