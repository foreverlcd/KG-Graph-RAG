"""Genera ontologia/alineaciones.ttl desde datos/alineaciones_tesauro.csv (determinista).

Solo skos:closeMatch / skos:relatedMatch hacia Wikidata y Getty AAT (ADR-024): nunca exactMatch.
Las etiquetas quechuas (@quz) solo se añaden cuando están atestiguadas (González Holguín 1608).
Uso: python scripts/alineaciones.py
"""
import csv, pathlib
from rdflib import Graph, Literal, URIRef
from rdflib.namespace import SKOS, DCTERMS

RAIZ = pathlib.Path(__file__).resolve().parents[1]
RELACIONES = {"skos:closeMatch": SKOS.closeMatch, "skos:relatedMatch": SKOS.relatedMatch}
# Etiquetas quechuas atestiguadas. Fuente: Diego González Holguín, Vocabulario de la lengua general de todo el Perú
# llamada lengua qquichua (Lima, 1608), archive.org vocabulariodelal01gonz. «qquellccaycamayoc» (escribano) queda fuera:
# el OCR es dudoso y no se cotejó la imagen.
QUECHUA = {
    "https://w3id.org/laad/tesauro/entidad/ayllu": ("ayllu", "«Ayllu. parcialidad, genealogía, linaje…»"),
    "https://w3id.org/laad/tesauro/cargo/cacique": ("curaca", "«Curaca. El señor del pueblo»"),
}
FUENTE_QUECHUA = "González Holguín, D. (1608). Vocabulario de la lengua general de todo el Perú llamada lengua qquichua. Lima."


def construir() -> Graph:
    g = Graph()
    g.bind("skos", SKOS); g.bind("dct", DCTERMS)
    with open(RAIZ / "datos/alineaciones_tesauro.csv", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            g.add((URIRef(fila["concepto_iri"]), RELACIONES[fila["relacion"]], URIRef(fila["iri_externo"])))
    for c, (etq, entrada) in QUECHUA.items():
        g.add((URIRef(c), SKOS.altLabel, Literal(etq, lang="quz")))
        g.add((URIRef(c), SKOS.historyNote, Literal(f"Forma quechua atestiguada: {entrada} ({FUENTE_QUECHUA})", lang="es")))
    return g


if __name__ == "__main__":
    salida = RAIZ / "ontologia/alineaciones.ttl"
    texto = construir().serialize(format="turtle")
    salida.write_text("# GENERADO por scripts/alineaciones.py desde datos/alineaciones_tesauro.csv. No editar a mano.\n" + texto,
                      encoding="utf-8")
    print(f"escrito {salida}")
