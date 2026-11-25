"""Genera presentacion/datos_proyecto.tex: las cifras y series de los gráficos de la presentación de estado del
proyecto (presentacion/proyecto.tex), calculadas a partir del grafo y de los informes de evaluación del harness.

    python scripts/datos_presentacion.py && (cd presentacion && latexmk -pdf proyecto.tex)

Las cifras generales (menciones, afirmaciones…) siguen saliendo de articulo/cifras.tex (scripts/cifras.py); aquí solo
se añaden las distribuciones y los resultados del harness, que el artículo aún no recoge.
"""
import collections
import json
import pathlib
import statistics
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
sys.path.insert(0, str(RAIZ / "scripts"))
from comparar_bancos import PERIFERICO, medir  # noqa: E402
from laad.consulta import consultar  # noqa: E402

SALIDA = RAIZ / "presentacion" / "datos_proyecto.tex"
EVAL = RAIZ / "datos" / "evaluacion"
PREFIJO = "agente_gemini_gemini-3.5-flash-lite_agente_consulta_"
# ejecuciones del banco del agente, en orden; etiqueta corta para los gráficos
EJECUCIONES = [("v1", "v1"), ("v2_herramientas1", "h1"), ("v2_herramientas2", "h2"),
               ("v2_r1", "r1"), ("v2_r2", "r2"), ("v2_r3", "r3")]


def _macro(nombre: str, valor) -> str:
    return f"\\newcommand{{\\{nombre}}}{{{valor}}}\n"


def _coords(pares) -> str:
    """Coordenadas por posición (0, 1, 2…): las etiquetas van aparte, en una macro de rótulos."""
    return " ".join(f"({i},{y})" for i, (_, y) in enumerate(pares))


def _rotulos(nombres) -> str:
    return ",".join("{" + str(n) + "}" for n in nombres)


def main() -> int:
    out = ["% Generado por scripts/datos_presentacion.py. No editar a mano.\n"]

    # ── capa 4 ──
    R = consultar("indice_reconstrucciones")
    clases = collections.Counter(r["clase"] for r in R)
    orden_c = ["persona", "lugar", "cosa", "grupo", "evento", "ejercicio-cargo"]
    out.append(_macro("serieClases", _coords((c, clases.get(c, 0)) for c in orden_c)))
    out.append(_macro("rotulosClases", _rotulos(["persona", "lugar", "cosa", "grupo", "hecho", "cargo"])))
    creencia = collections.Counter(r["creencia"] for r in R)
    orden_k = ["verdadero", "probable", "posible", "improbable", "indeterminado"]
    out.append(_macro("serieCreencia", _coords((k, creencia.get(k, 0)) for k in orden_k)))
    out.append(_macro("rotulosCreencia", _rotulos(orden_k)))

    # ── capa 3 ──
    A = {a["aid"]: a for a in consultar("afirmaciones")}
    fuerza = collections.Counter(str(a["fuerza"]) for a in A.values())
    orden_f = [f for f, _ in fuerza.most_common()]
    out.append(_macro("serieFuerza", _coords((f, fuerza[f]) for f in orden_f)))
    out.append(_macro("rotulosFuerza", _rotulos(orden_f)))
    out.append(_macro("serieFuerzaX", " ".join(f"({fuerza[f]},{i})" for i, f in enumerate(orden_f))))
    pol = collections.Counter(a["pol"] for a in A.values())
    out.append(_macro("datoAfirma", pol.get("afirma", 0)))
    out.append(_macro("datoNiega", sum(v for k, v in pol.items() if k != "afirma")))
    porpieza = collections.Counter(a["pieza"] for a in A.values())
    piezas = sorted(porpieza, key=lambda p: int(p[1:]))
    out.append(_macro("seriePiezas", _coords((p, porpieza[p]) for p in piezas)))
    out.append(_macro("rotulosPiezas", _rotulos(piezas)))
    out.append(_macro("nPiezasConAfirmaciones", len(piezas)))

    # ── harness: ejecuciones del agente ──
    filas, medidas = [], []
    for suf, et in EJECUCIONES:
        ruta = EVAL / f"{PREFIJO}{suf}.jsonl"
        if not ruta.exists():
            continue
        m = medir(ruta)
        medidas.append((et, m))
        filas.append((et, len(m), *(sum(x[k] for x in m.values()) for k in ("completa", "esencial", "forma", "verificada")),
                      round(statistics.mean(x["tokens"] for x in m.values()) / 1000) if m else 0))
    for i, k in enumerate(("completa", "esencial", "forma", "verificada")):
        out.append(_macro("serieAgente" + k.capitalize(), _coords((f[0], f[2 + i]) for f in filas)))
    out.append(_macro("rotulosAgente", _rotulos(f[0] for f in filas)))
    out.append("\\newcommand{\\tablaAgente}{%\n" + "".join(
        f"{et} & {n} & {c} & {e} & {fo} & {v} & {t}\\,k \\\\\n" for et, n, c, e, fo, v, t in filas) + "}\n")
    # medias solo sobre las repeticiones con la misma configuración (instrucciones v2 y herramientas actuales)
    llenas = [m for et, m in medidas if len(m) == 20 and et.startswith("r")]
    for k in ("completa", "esencial", "forma", "verificada"):
        v = [sum(x[k] for x in m.values()) for m in llenas]
        out.append(_macro("media" + k.capitalize(), f"{statistics.mean(v):.1f}".replace(".", ",")))
        out.append(_macro("num" + k.capitalize(), f"{statistics.mean(v):.2f}"))   # para pgfplots (punto decimal)
        out.append(_macro("desv" + k.capitalize(), f"{statistics.pstdev(v):.1f}".replace(".", ",")))
    out.append(_macro("nEjecucionesLlenas", len(llenas)))

    # matriz PC × ejecución (lo esencial): 1 correcto, 0 no, -1 sin medir
    pcs = [f"PC{i:02d}" for i in range(1, 21)]
    celdas = []
    for j, (et, m) in enumerate(medidas):
        for i, pc in enumerate(pcs):
            v = -1 if pc not in m else int(m[pc]["esencial"])
            celdas.append(f"({i},{j}) [{v}]")   # x = PC, y = ejecución
    out.append(_macro("matrizEsencial", " ".join(celdas)))

    # ── intermediario (Claude con las mismas herramientas), medido hoy contra las referencias vigentes ──
    from laad.evaluacion_harness import evaluar_respuesta
    inter = [json.loads(x) for x in (EVAL / "intermediario_claude.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    c = e = fo = v = 0
    for d in inter:
        r = evaluar_respuesta(d["pc"], d["llamadas"], d["respuesta"])
        c += r["alcanzada"]
        e += not [f for f in r["fallos"] if not PERIFERICO.match(f)]
        fo += r["forma"] == r["forma_referencia"]
        v += r["verificada"]
    for k, x in (("Completa", c), ("Esencial", e), ("Forma", fo), ("Verificada", v)):
        out.append(_macro("inter" + k, x))

    SALIDA.write_text("".join(out), encoding="utf-8")
    print(f"→ {SALIDA.relative_to(RAIZ)}: {len(R)} reconstrucciones, {len(A)} afirmaciones, {len(filas)} ejecuciones, "
          f"intermediario {c}/{e}/{fo}/{v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
