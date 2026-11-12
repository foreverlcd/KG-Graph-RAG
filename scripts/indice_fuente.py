"""Genera fuente/tramos.csv: índice de tramos de la transcripción paleográfica."""
import csv, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from laad.fuente import tramos, colapsar, sha256, TRANSCRIPCION

out = pathlib.Path(__file__).resolve().parents[1] / "fuente" / "tramos.csv"
with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["tramo", "ut", "linea_inicio", "linea_fin", "folio_explicito", "lado",
                "marca", "caracteres", "comienzo", "final"])
    for t in tramos():
        x = colapsar(t.texto)
        w.writerow([t.id, t.ut, t.linea_inicio, t.linea_fin, t.folio or "no consta",
                    "no consta", t.marca or "", len(x), x[:60], x[-40:]])
print(f"{out} escrito; sha256 transcripción = {sha256()}  ({TRANSCRIPCION.name})")
