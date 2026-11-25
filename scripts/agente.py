"""Pregunta en lenguaje natural al agente de consulta (laad.agente) con un modelo real.

    python scripts/agente.py "¿Fue Chuquitapa coronel de Túpac Amaru?"
    python scripts/agente.py --modelo gemini-3.6-flash --traza "¿Quién redactó la querella?"
    python scripts/agente.py --env ../otro/.env "…"        # carga GOOGLE_API_KEY de ese archivo (no se imprime)
    python scripts/agente.py --banco [--pc PC09 --pc PC11] [--pausa 15]   # las 20 PC del banco, con comprobar()

La clave se lee de GOOGLE_API_KEY; si no está, de LAAD/.env (ignorado por git; ver .env.example) o del --env dado.
Imprime la respuesta, la forma declarada, el estado de verificación, las llamadas hechas y los tokens.
El modo --banco escribe un informe en datos/evaluacion/agente_<proveedor>_<modelo>.jsonl.
"""
import argparse
import json
import pathlib
import sys
import time

RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from laad import agente as AG  # noqa: E402
from laad import proveedores  # noqa: E402


def _mostrar(r: AG.RespuestaAgente, traza: bool) -> None:
    print(r.texto or "(sin texto)")
    print("\n" + "─" * 70)
    print(f"forma: {r.forma}   estado: {r.estado.upper()}   pasos: {r.pasos}   "
          f"tokens: {r.tokens_entrada} entrada / {r.tokens_salida} salida   {r.segundos:.1f} s")
    if r.verificacion["citas"] or r.verificacion["ids"]:
        print(f"NO VERIFICADO: {r.verificacion}")
    print("llamadas: " + ("; ".join(t for t in r.traza if not t.startswith("verificación")) or "ninguna"))
    if r.ejecucion.errores:
        print("errores de herramienta: " + " | ".join(r.ejecucion.errores))
    if traza:
        print("traza completa:\n  " + "\n  ".join(r.traza))


def _banco(prov, pcs: list[str], pausa: float, max_pasos: int) -> int:
    from laad.evaluacion_harness import Ejecucion, cargar, cobertura, comprobar
    from laad.preguntas import PREGUNTAS
    lineas = [x for x in cargar() if not pcs or x["pc"] in pcs]
    salida = RAIZ / "datos" / "evaluacion" / f"agente_{prov.nombre}_{prov.modelo}_{AG.PROMPT.stem}.jsonl"
    alcanzadas = forma_ok = verificadas = 0
    with salida.open("w", encoding="utf-8") as f:
        for i, linea in enumerate(lineas):
            if i:
                time.sleep(pausa)                     # cuota del nivel gratuito y calor del portátil
            try:
                r = AG.preguntar(linea["pregunta"], prov, max_pasos=max_pasos)
            except Exception as e:                    # noqa: BLE001 — un fallo del proveedor no detiene el banco
                error = f"{type(e).__name__}: {str(e)[:200]}"
                print(f"{linea['pc']}: ERROR del proveedor: {error}", flush=True)
                f.write(json.dumps({"pc": linea["pc"], "error": error}, ensure_ascii=False) + "\n")
                if type(e).__name__ == "CuotaDiaria":   # el resto fallaría igual: se para y se dice
                    print(f"Cuota diaria agotada: se detiene el banco en {linea['pc']}; "
                          f"el resultado no mide el agente.", flush=True)
                    break
                continue
            referencia = PREGUNTAS[linea["pc"]]()
            # un error de herramienta que el agente corrigió en la llamada siguiente no es un fallo de la respuesta:
            # se informa aparte («avisos»); los planes escritos a mano sí lo cuentan como fallo
            ej = Ejecucion(r.ejecucion.resultados, r.ejecucion.tiempos, [])
            fallos = comprobar(referencia, ej, r.forma or "?")
            if not r.verificada:
                fallos.append(f"respuesta {r.estado}")
            cob = cobertura(referencia, ej)
            alcanzadas += not fallos
            forma_ok += r.forma == linea["forma"]
            verificadas += r.verificada
            print(f"{linea['pc']}: {'OK ' if not fallos else 'NO '} forma {r.forma} (ref. {linea['forma']}), "
                  f"{r.pasos} pasos, {r.tokens_entrada}+{r.tokens_salida} tokens, cobertura "
                  + ", ".join(f"{k} {'—' if v is None else f'{v:.0%}'}" for k, v in cob.items())
                  + ("" if not r.ejecucion.errores else f"\n    avisos (errores corregidos): {len(r.ejecucion.errores)}")
                  + ("" if not fallos else "\n    " + "\n    ".join(f[:220] for f in fallos)), flush=True)
            f.write(json.dumps({"pc": linea["pc"], "pregunta": linea["pregunta"], "respuesta": r.texto,
                                "forma": r.forma, "forma_referencia": linea["forma"], "estado": r.estado,
                                "alcanzada": not fallos, "fallos": fallos, "cobertura": cob,
                                "avisos": r.ejecucion.errores, "instrucciones": AG.PROMPT.name, "traza": r.traza, "pasos": r.pasos,
                                "tokens_entrada": r.tokens_entrada, "tokens_salida": r.tokens_salida,
                                "segundos": round(r.segundos, 1), "proveedor": prov.nombre, "modelo": prov.modelo,
                                "fecha": time.strftime("%Y-%m-%d")}, ensure_ascii=False) + "\n")
    print(f"\n{alcanzadas}/{len(lineas)} PC alcanzadas por {prov.nombre}/{prov.modelo} ({AG.PROMPT.name}); "
          f"forma correcta {forma_ok}/{len(lineas)}; respuestas verificadas {verificadas}/{len(lineas)} "
          f"→ {salida.relative_to(RAIZ)}")
    return 0 if alcanzadas == len(lineas) else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pregunta", nargs="?")
    ap.add_argument("--proveedor", default="gemini")
    ap.add_argument("--modelo")
    ap.add_argument("--env", help="archivo .env del que cargar la clave")
    ap.add_argument("--max-pasos", type=int, default=12)
    ap.add_argument("--traza", action="store_true")
    ap.add_argument("--banco", action="store_true")
    ap.add_argument("--pc", action="append", default=[])
    ap.add_argument("--pausa", type=float, default=10.0, help="segundos entre preguntas del banco")
    a = ap.parse_args()
    for env in filter(None, [a.env, RAIZ / ".env"]):
        if pathlib.Path(env).exists():
            proveedores.cargar_env(env)
    prov = proveedores.crear(a.proveedor, a.modelo)
    if a.banco:
        return _banco(prov, a.pc, a.pausa, a.max_pasos)
    if not a.pregunta:
        ap.error("falta la pregunta (o --banco)")
    r = AG.preguntar(a.pregunta, prov, max_pasos=a.max_pasos)
    _mostrar(r, a.traza)
    return 0 if r.verificada else 1


if __name__ == "__main__":
    sys.exit(main())
