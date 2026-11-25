"""Ejecuta el banco de pruebas del harness (datos/evaluacion/preguntas_harness.jsonl): el plan de llamadas de cada
pregunta de competencia, y comprueba que alcanza lo esencial de la respuesta de laad.preguntas (forma, afirmaciones,
afirmantes, reconstrucciones, citas e ids). Ver src/laad/evaluacion_harness.py.

    python scripts/evaluar_harness.py [banco.jsonl] [--detalle]

--detalle imprime además el texto compuesto por las herramientas. Sale con 1 si alguna PC no se alcanza.
"""
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from laad import evaluacion_harness as E  # noqa: E402


def main(argv: list[str]) -> int:
    detalle = "--detalle" in argv
    rutas = [a for a in argv if not a.startswith("--")]
    resultados = E.evaluar(pathlib.Path(rutas[0]) if rutas else E.BANCO)
    for r in resultados:
        lenta = max(r["tiempos"], key=lambda x: x[1]) if r["tiempos"] else ("—", 0.0)
        print(f"{r['pc']}  {'alcanzada' if r['alcanzada'] else 'NO ALCANZADA'}  forma {r['forma']} "
              f"(referencia {r['forma_referencia']})  {r['llamadas']} llamadas  "
              f"{sum(t for _, t in r['tiempos']):.2f} s (la más lenta: {lenta[0]}, {lenta[1]:.2f} s)")
        for f in r["fallos"]:
            print(f"    - {f}")
        if detalle:
            print(r["ejecucion"].texto)
    n = sum(r["alcanzada"] for r in resultados)
    print(f"\n{n} de {len(resultados)} preguntas alcanzadas por su plan.")
    return 0 if n == len(resultados) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
