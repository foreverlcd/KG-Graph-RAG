"""Inserta en ontologia/tesauro.ttl las definiciones de datos/definiciones_tesauro.csv (determinista).

La sección queda entre las marcas INICIO/FIN y se regenera entera; el resto del tesauro se edita a mano.
Cada definición lleva su fuente en skos:editorialNote; las no verificadas se marcan como definición de trabajo.
Uso: python scripts/definiciones.py
"""
import csv, pathlib, re

RAIZ = pathlib.Path(__file__).resolve().parents[1]
TESAURO = RAIZ / "ontologia/tesauro.ttl"
CSV = RAIZ / "datos/definiciones_tesauro.csv"
INICIO = "# >>> DEFINICIONES — GENERADO por scripts/definiciones.py desde datos/definiciones_tesauro.csv. No editar a mano."
FIN = "# <<< FIN DEFINICIONES"


def lit(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"@es'


def seccion() -> str:
    lineas = [INICIO]
    with open(CSV, encoding="utf-8") as f:
        filas = sorted(csv.DictReader(f), key=lambda r: r["concepto_iri"])
    for r in filas:
        if r["verificado"] == "si" and r["fuente"].strip():
            nota = f"Fuente de la definición: {r['fuente'].strip()}."
        else:
            nota = "Definición de trabajo: fuente no verificada."
        lineas.append(f"<{r['concepto_iri']}> skos:definition {lit(r['definicion'].strip())} ;\n"
                      f"    skos:editorialNote {lit(nota)} .")
    lineas.append(FIN)
    return "\n".join(lineas) + "\n"


def aplicar(texto: str) -> str:
    patron = re.compile(re.escape(INICIO) + r".*?" + re.escape(FIN) + r"\n", re.S)
    nueva = seccion()
    if patron.search(texto):
        return patron.sub(lambda _: nueva, texto)
    return texto.rstrip("\n") + "\n\n" + nueva


if __name__ == "__main__":
    TESAURO.write_text(aplicar(TESAURO.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"escrito {TESAURO}")
