"""Calcula las cifras del proyecto y las escribe en un único lugar del que beben el artículo y la presentación.

Salidas (deterministas, se versionan):
  datos/cifras.json        — todas las cifras, con su origen
  articulo/cifras.tex      — una macro LaTeX por cifra (\\cifraMenciones, …); lo cargan articulo/main.tex y
                             presentacion/main.tex con \\input, de modo que no pueden decir cosas distintas
  docs/cifras.md           — la misma tabla para la documentación

Uso: python scripts/cifras.py            (regenera)
     python scripts/cifras.py --comprobar (sale con 1 si algún archivo no está al día; lo usa tests/test_cifras.py)

Las cifras salen de los datos y de los archivos generados (datos/grafo/*.nq, datos/grafo/razonador.txt); las que
exigen ejecutar algo lento (razonador, número de pruebas) se leen de su última salida guardada.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))

import rdflib  # noqa: E402
from rdflib.namespace import OWL, RDF, SKOS  # noqa: E402

from laad import corpus  # noqa: E402

SALIDA_JSON = RAIZ / "datos/cifras.json"
SALIDA_TEX = RAIZ / "articulo/cifras.tex"
SALIDA_MD = RAIZ / "docs/cifras.md"


def _registros() -> tuple[list[dict], list[dict]]:
    menciones, afirmaciones = [], []
    for exp in corpus.expedientes():
        for ruta in corpus.rutas_registros(exp):
            for linea in ruta.read_text(encoding="utf-8").splitlines():
                if not linea.strip():
                    continue
                r = json.loads(linea)
                r["_exp"] = exp
                (menciones if r["tipo_registro"] == "mencion" else afirmaciones).append(r)
    return menciones, afirmaciones


def _lineas(ruta: Path) -> list[str]:
    return [l for l in ruta.read_text(encoding="utf-8").splitlines() if l.strip()]


def _razonador() -> dict[str, int]:
    t = (RAIZ / "datos/grafo/razonador.txt").read_text(encoding="utf-8")
    def n(patron: str) -> int:
        m = re.search(patron, t)
        return int(m.group(1)) if m else -1
    return {
        "razonador_tripletas": n(r"con estándares y perfil: (\d+)"),
        "razonador_cierre": n(r"tras cierre OWL RL: (\d+)"),
        "razonador_inconsistencias": n(r"inconsistencias \(agent-ont#error\): (\d+)"),
        "d1_espurias": n(r"PersonObservation inferida roar:Reconstruction\): (\d+)"),
        "d6_afirmaciones": n(r"E13 inferida I1_Argumentation\): (\d+)"),
        "d6_negaciones": n(r"creídas verdaderas: (\d+)"),
    }


def calcular() -> dict[str, int]:
    menciones, afirmaciones = _registros()
    c: dict[str, int] = {}
    c["expedientes"] = len(corpus.expedientes())
    c["piezas"] = sum(len(_lineas(corpus.ruta_piezas(e))) for e in corpus.expedientes())
    c["menciones"] = len(menciones)
    c["afirmaciones"] = len(afirmaciones)
    c["negaciones"] = sum(1 for a in afirmaciones if a.get("polaridad") == "niega")
    c["negaciones_con_respuesta"] = sum(1 for a in afirmaciones if a.get("polaridad") == "niega" and a.get("responde_a"))
    c["citas"] = sum(1 for r in menciones + afirmaciones for k in ("cita", "cita_firma") if r.get(k))
    c["valores_literales"] = sum(1 for a in afirmaciones if a["valor"].get("literal") is not None)

    recs = [json.loads(l) for l in _lineas(corpus.RECONSTRUCCIONES)]
    c["reconstrucciones"] = len(recs)
    c["reconstrucciones_con_fechas"] = len(recs) + sum(1 for e in corpus.expedientes() if corpus.ruta_fechas(e))
    enlazadas = {m for r in recs for m in r.get("menciones", []) if ":M-" in m}
    hechos_rec = {m for r in recs for m in r.get("menciones", []) if ":H-" in m}
    c["menciones_enlazadas"] = len(enlazadas)
    with open(RAIZ / "datos/auditoria_reconstrucciones.csv", encoding="utf-8") as f:
        auditadas = {next(iter(r.values())) for r in csv.DictReader(f)}
    # auditadas y no modificadas después de la auditoría del 2026-11-13
    c["reconstrucciones_auditadas"] = len(auditadas & {r["id"] for r in recs if r["fecha"] <= "2026-11-13"})
    c["reconstrucciones_sin_auditar"] = len(recs) - c["reconstrucciones_auditadas"]
    c["personas"] = sum(1 for m in menciones if m["clase"] == "persona")
    c["personas_enlazadas"] = sum(1 for m in menciones if m["clase"] == "persona" and f"{m['_exp']}:{m['id']}" in enlazadas)
    hechos = {f"{a['_exp']}:{x['hecho']}" for a in afirmaciones for x in (a["sujeto"], a["valor"]) if x.get("hecho")}
    c["hechos_narrados"] = len(hechos)
    c["hechos_enlazados"] = len(hechos & hechos_rec)
    no_persona = [m for m in menciones if m["clase"] != "persona"]
    c["entidades_sin_tipo"] = sum(1 for m in no_persona if not m.get("tipo_entidad"))
    c["entidades_no_persona"] = len(no_persona)

    tes = rdflib.Graph().parse(RAIZ / "ontologia/tesauro.ttl")
    c["esquemas"] = len(set(tes.subjects(RDF.type, SKOS.ConceptScheme)))
    c["conceptos"] = len(set(tes.subjects(RDF.type, SKOS.Concept)))
    c["atributos"] = len(set(tes.subjects(SKOS.inScheme, rdflib.URIRef("https://w3id.org/laad/tesauro/atributos"))))
    with open(RAIZ / "datos/definiciones_tesauro.csv", encoding="utf-8") as f:
        c["definiciones_de_trabajo"] = sum(1 for r in csv.DictReader(f) if r["verificado"] != "si")
    with open(RAIZ / "datos/candidatos_tesauro.csv", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    c["candidatos"] = sum(1 for r in filas if r["estado"] == "candidato")
    with open(RAIZ / "datos/alineaciones_tesauro.csv", encoding="utf-8") as f:
        c["alineaciones"] = sum(1 for _ in csv.DictReader(f))

    quads = [l for p in sorted((RAIZ / "datos/grafo").glob("*.nq")) for l in _lineas(p)]
    ds = rdflib.Dataset()
    ds.parse(data="\n".join(quads), format="nquads")
    tripletas, clases, props = set(), set(), set()
    grafos = 0
    for g in ds.graphs():
        if len(g):
            grafos += 1
        for s, p, o in g:
            tripletas.add((s, p, o))
            props.add(p)
            if p == RDF.type:
                clases.add(o)
    c["tripletas"] = len(tripletas)
    c["grafos"] = grafos
    c["clases"] = len(clases)
    c["propiedades"] = len(props)
    propios = [x for x in clases | props if str(x).startswith("https://w3id.org/laad/") and "/tesauro/" not in str(x)]
    c["terminos_propios"] = len(propios)

    fichas = [json.loads(l) for l in _lineas(RAIZ / "datos/catalogo/fichas_pc03_pc04.jsonl")]
    c["catalogo_registros"] = len(fichas)

    formas = rdflib.Graph()
    for f in ("formas.ttl", "formas_atributos.ttl"):
        formas.parse(RAIZ / "ontologia" / f)
    c["formas"] = len(set(formas.subjects(RDF.type, rdflib.URIRef("http://www.w3.org/ns/shacl#NodeShape"))))
    t = (RAIZ / "tests/test_formas_negativas.py").read_text(encoding="utf-8")
    c["mutaciones_declaradas"] = len(re.findall(r"^\s+Mutacion\(", t, flags=re.M))
    c["preguntas"] = 20
    c.update(_razonador())
    return dict(sorted(c.items()))


_DIGITOS = dict(zip("0123456789", "Cero Uno Dos Tres Cuatro Cinco Seis Siete Ocho Nueve".split()))


def _macro(clave: str) -> str:
    """Nombre de macro LaTeX (sin dígitos ni guiones): d6_negaciones → cifraDSeisNegaciones."""
    partes = [re.sub(r"\d", lambda m: _DIGITOS[m.group()], p) for p in clave.split("_")]
    return "cifra" + "".join(p[0].upper() + p[1:] for p in partes)


def _miles(n: int) -> str:
    return f"{n:,}".replace(",", r"\,")


def tex(c: dict[str, int]) -> str:
    lineas = ["% GENERADO por scripts/cifras.py. No editar a mano: ejecutar el script.",
              "% Lo cargan articulo/main.tex y presentacion/main.tex."]
    for k, v in c.items():
        lineas.append(f"\\newcommand{{\\{_macro(k)}}}{{{_miles(v)}}}")
    return "\n".join(lineas) + "\n"


def md(c: dict[str, int]) -> str:
    lineas = ["# Cifras del proyecto", "",
              "> Generado por `scripts/cifras.py` a partir de los datos. No editar a mano. El artículo y la presentación",
              "> usan estas mismas cifras por medio de `articulo/cifras.tex`.", "",
              "| Cifra | Valor | Macro LaTeX |", "|---|---:|---|"]
    for k, v in c.items():
        lineas.append(f"| {k.replace('_', ' ')} | {v:,} | `\\{_macro(k)}` |".replace(",", " "))
    return "\n".join(lineas) + "\n"


def salidas(c: dict[str, int]) -> dict[Path, str]:
    return {SALIDA_JSON: json.dumps(c, ensure_ascii=False, indent=2) + "\n", SALIDA_TEX: tex(c), SALIDA_MD: md(c)}


if __name__ == "__main__":
    s = salidas(calcular())
    if "--comprobar" in sys.argv:
        viejos = [str(p.relative_to(RAIZ)) for p, txt in s.items() if not p.exists() or p.read_text(encoding="utf-8") != txt]
        if viejos:
            print("no están al día (ejecutar scripts/cifras.py):", ", ".join(viejos))
            sys.exit(1)
        print("cifras al día")
    else:
        for p, txt in s.items():
            p.write_text(txt, encoding="utf-8")
            print("escrito", p.relative_to(RAIZ))
