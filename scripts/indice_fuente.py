"""Genera el índice de tramos de la transcripción paleográfica de un expediente.

Uso: python scripts/indice_fuente.py [expediente] [salida.csv]
Sin argumentos: el expediente por defecto (el piloto) en fuente/tramos.csv; para otro expediente la salida por
defecto es fuente/<expediente>/tramos.csv.
"""
import csv, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from laad import fuente
from laad.fuente import tramos, colapsar, sha256

RAIZ = pathlib.Path(__file__).resolve().parents[1]
exp = sys.argv[1] if len(sys.argv) > 1 else fuente.EXPEDIENTE_POR_DEFECTO
por_defecto = RAIZ / "fuente" / "tramos.csv" if exp == fuente.EXPEDIENTE_POR_DEFECTO else RAIZ / "fuente" / exp / "tramos.csv"
out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else por_defecto
out.parent.mkdir(parents=True, exist_ok=True)
with fuente.usando_expediente(exp), out.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["tramo", "ut", "linea_inicio", "linea_fin", "folio_explicito", "lado",
                "marca", "caracteres", "comienzo", "final"])
    for t in tramos():
        x = colapsar(t.texto)
        w.writerow([t.id, t.ut, t.linea_inicio, t.linea_fin, t.folio or "no consta",
                    "no consta", t.marca or "", len(x), x[:60], x[-40:]])
    print(f"{out} escrito; sha256 transcripción = {sha256()}  ({fuente.ruta_transcripcion().name})")
