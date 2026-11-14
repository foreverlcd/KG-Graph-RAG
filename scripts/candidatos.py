"""Conceptos candidatos del tesauro: lo que un anotador encuentra y el tesauro no tiene (determinista).

Fuente: datos/candidatos_tesauro.csv (una fila por concepto propuesto). De ahí se generan:
  * ontologia/candidatos.ttl — los candidatos PENDIENTES (skos:Concept en su esquema, miembros de la colección
    tes:candidatos) y los RECHAZADOS (owl:deprecated true + dct:isReplacedBy si se indica; su IRI no se borra nunca);
  * la sección marcada «APROBADOS» de ontologia/tesauro.ttl — los candidatos aprobados, ya conceptos del tesauro.
Solo vocabulario estándar: SKOS, DCTERMS, OWL (anotaciones) y PROV. Política: ontologia/README.md.

Uso:
  python scripts/candidatos.py                      regenera candidatos.ttl, tesauro.ttl y formas_atributos.ttl
  python scripts/candidatos.py --proponer ESQUEMA LOCAL "etiqueta" "definición" --expediente X --ejemplo "…"
                               [--broader LOCAL] [--por QUIEN] [--fecha AAAA-MM-DD]
  python scripts/candidatos.py --aprobar ESQUEMA/LOCAL
  python scripts/candidatos.py --rechazar ESQUEMA/LOCAL [--reemplazo LOCAL]
  python scripts/candidatos.py --listar
"""
from __future__ import annotations

import argparse
import csv
import datetime
import json
import pathlib
import re
import sys

import rdflib
from rdflib.namespace import RDF, SKOS

RAIZ = pathlib.Path(__file__).resolve().parents[1]
TESAURO = RAIZ / "ontologia/tesauro.ttl"
CANDIDATOS = RAIZ / "ontologia/candidatos.ttl"
CSV = RAIZ / "datos/candidatos_tesauro.csv"
MANIFIESTOS = RAIZ / "datos/expedientes"
BASE_TES = "https://w3id.org/laad/tesauro/"
BASE_ID = "https://w3id.org/laad/id/"
COLECCION = BASE_TES + "candidatos"
COLUMNAS = ["esquema", "local", "etiqueta", "definicion", "broader", "propuesto_por", "fecha", "expediente",
            "ejemplo", "estado", "reemplazado_por"]
ESTADOS = ("candidato", "aprobado", "rechazado")
OBLIGATORIAS = ("esquema", "local", "etiqueta", "definicion", "propuesto_por", "fecha", "expediente", "ejemplo",
                "estado")
INICIO = ("# >>> APROBADOS — GENERADO por scripts/candidatos.py desde datos/candidatos_tesauro.csv "
          "(filas con estado «aprobado»). No editar a mano.")
FIN = "# <<< FIN APROBADOS"
_SECCION = re.compile(re.escape(INICIO) + r".*?" + re.escape(FIN) + r"\n", re.S)
_LOCAL = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PREFIJOS = """@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dct:  <http://purl.org/dc/terms/> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix tes:  <https://w3id.org/laad/tesauro/> .
"""


class ErrorCandidatos(ValueError):
    """El CSV de candidatos no cumple la política (ontologia/README.md)."""


def lit(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"@es'


# ───────────────────────── lectura ─────────────────────────
def leer(ruta: pathlib.Path | None = None) -> list[dict]:
    ruta = ruta or CSV
    with open(ruta, encoding="utf-8", newline="") as f:
        lector = csv.DictReader(f)
        if lector.fieldnames != COLUMNAS:
            raise ErrorCandidatos(f"{ruta.name}: columnas {lector.fieldnames}; se esperan {COLUMNAS}")
        return [{k: (v or "").strip() for k, v in fila.items()} for fila in lector]


def escribir_csv(filas: list[dict], ruta: pathlib.Path | None = None) -> None:
    with open(ruta or CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNAS, lineterminator="\n")
        w.writeheader()
        w.writerows(filas)


def sin_seccion(texto: str) -> str:
    """El tesauro sin la sección generada de aprobados (lo escrito a mano y las definiciones)."""
    return _SECCION.sub("", texto)


def tesauro_base(texto: str | None = None) -> rdflib.Graph:
    texto = TESAURO.read_text(encoding="utf-8") if texto is None else texto
    return rdflib.Graph().parse(data=sin_seccion(texto), format="turtle")


def espacios(base: rdflib.Graph) -> dict[str, str]:
    """Esquema → espacio de nombres de sus conceptos, leído del propio tesauro («cargos» → «…/tesauro/cargo/»)."""
    out: dict[str, str] = {}
    for esq in base.subjects(RDF.type, SKOS.ConceptScheme):
        c = next(iter(sorted(base.subjects(SKOS.inScheme, esq))), None)
        if c is not None:
            out[str(esq)[len(BASE_TES):]] = str(c).rsplit("/", 1)[0] + "/"
    return out


def expediente_iri(exp: str, manifiestos: pathlib.Path = MANIFIESTOS) -> str:
    ruta = manifiestos / f"{exp}.json"
    if not ruta.exists():
        raise ErrorCandidatos(f"expediente desconocido: {exp!r} (no existe {ruta})")
    return BASE_ID + json.loads(ruta.read_text(encoding="utf-8"))["jerarquia"][-1]["id"]


def agente_iri(propuesto_por: str) -> tuple[str, str]:
    """«claude-opus-5-5 (lote expediente_c)» → (IRI del agente, «claude-opus-5-5»): el mismo agente que en la capa P."""
    nombre = re.sub(r"[^A-Za-z0-9._-]+", "-", propuesto_por.split("(")[0].strip()).strip("-")
    if not nombre:
        raise ErrorCandidatos(f"propuesto_por sin nombre de agente: {propuesto_por!r}")
    return f"{BASE_ID}agente/{nombre}", nombre


# ───────────────────────── validación ─────────────────────────
def validar(filas: list[dict], base: rdflib.Graph, manifiestos: pathlib.Path = MANIFIESTOS) -> dict[str, str]:
    """Comprueba el CSV contra el tesauro escrito a mano. Devuelve esquema → espacio de nombres. Todo candidato
    lleva definición, proponente, fecha, expediente y ejemplo; nunca reutiliza la IRI de un concepto que ya existe."""
    ns = espacios(base)
    errores: list[str] = []
    estado = {(f["esquema"], f["local"]): f["estado"] for f in filas}
    vistos: set[tuple[str, str]] = set()

    def existe(esq: str, local: str, admite: tuple[str, ...]) -> bool:
        if (rdflib.URIRef(ns[esq] + local), SKOS.inScheme, rdflib.URIRef(BASE_TES + esq)) in base:
            return True
        return estado.get((esq, local)) in admite

    for n, f in enumerate(filas, 2):
        donde = f"fila {n} ({f['esquema']}/{f['local']})"
        for campo in OBLIGATORIAS:
            if not f[campo]:
                errores.append(f"{donde}: falta «{campo}»")
        if f["esquema"] not in ns:
            errores.append(f"{donde}: esquema desconocido; existen {sorted(ns)}")
            continue
        if not _LOCAL.match(f["local"]):
            errores.append(f"{donde}: nombre local no válido (minúsculas, cifras y guiones)")
            continue
        clave = (f["esquema"], f["local"])
        if clave in vistos:
            errores.append(f"{donde}: fila repetida")
        vistos.add(clave)
        if f["estado"] not in ESTADOS:
            errores.append(f"{donde}: estado {f['estado']!r}; se admite {ESTADOS}")
        if (rdflib.URIRef(ns[f["esquema"]] + f["local"]), RDF.type, SKOS.Concept) in base:
            errores.append(f"{donde}: el concepto ya existe en el tesauro; una IRI no se reutiliza")
        if f["fecha"] and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", f["fecha"]):
            errores.append(f"{donde}: fecha {f['fecha']!r}; se espera AAAA-MM-DD")
        if f["expediente"]:
            try:
                expediente_iri(f["expediente"], manifiestos)
            except ErrorCandidatos as e:
                errores.append(f"{donde}: {e}")
        if f["propuesto_por"]:
            try:
                agente_iri(f["propuesto_por"])
            except ErrorCandidatos as e:
                errores.append(f"{donde}: {e}")
        if f["broader"]:
            # un concepto aprobado no puede colgar de uno pendiente; ninguno, de uno rechazado
            admite = ("aprobado",) if f["estado"] == "aprobado" else ("aprobado", "candidato")
            if f["broader"] == f["local"] or not existe(f["esquema"], f["broader"], admite):
                errores.append(f"{donde}: broader «{f['broader']}» no es un concepto vigente de tes:{f['esquema']}"
                               + (" ya aprobado" if f["estado"] == "aprobado" else ""))
        if f["reemplazado_por"]:
            if f["estado"] != "rechazado":
                errores.append(f"{donde}: reemplazado_por solo se admite en filas rechazadas")
            elif f["reemplazado_por"] == f["local"] or not existe(f["esquema"], f["reemplazado_por"],
                                                                   ("aprobado", "candidato")):
                errores.append(f"{donde}: reemplazado_por «{f['reemplazado_por']}» no es un concepto vigente de "
                               f"tes:{f['esquema']}")
    if errores:
        raise ErrorCandidatos("datos/candidatos_tesauro.csv:\n  " + "\n  ".join(errores))
    return ns


# ───────────────────────── generación ─────────────────────────
def _concepto(f: dict, ns: dict[str, str], manifiestos: pathlib.Path) -> str:
    iri = ns[f["esquema"]] + f["local"]
    esq = f"tes:{f['esquema']}"
    agente, _ = agente_iri(f["propuesto_por"])
    lineas = [f"<{iri}> a skos:Concept ; skos:inScheme {esq} ; "
              + (f"skos:broader <{ns[f['esquema']] + f['broader']}> ;" if f["broader"] else f"skos:topConceptOf {esq} ;"),
              f"    skos:prefLabel {lit(f['etiqueta'])} ;",
              f"    skos:definition {lit(f['definicion'])} ;",
              f"    skos:example {lit(f['ejemplo'])} ;",
              f"    dct:created \"{f['fecha']}\"^^xsd:date ; prov:wasAttributedTo <{agente}> ; "
              f"dct:source <{expediente_iri(f['expediente'], manifiestos)}> ;"]
    historia = f"Propuesto por {f['propuesto_por']} el {f['fecha']} al anotar el expediente {f['expediente']}."
    if f["estado"] == "candidato":
        lineas.append(f"    skos:editorialNote {lit('Concepto candidato: pendiente de revisión; puede aprobarse o rechazarse.')} ;")
    elif f["estado"] == "aprobado":
        historia += " Aprobado: forma parte del tesauro."
    else:
        historia += " Rechazado: no debe usarse" + (f"; en su lugar, «{f['reemplazado_por']}»." if f["reemplazado_por"] else ".")
        lineas.append("    owl:deprecated true ;"
                      + (f" dct:isReplacedBy <{ns[f['esquema']] + f['reemplazado_por']}> ;" if f["reemplazado_por"] else ""))
    lineas.append(f"    skos:historyNote {lit(historia)} .")
    return "\n".join(lineas)


def _agentes(filas: list[dict]) -> list[str]:
    vistos = sorted({agente_iri(f["propuesto_por"]) for f in filas})
    return [f"<{iri}> a prov:Agent ; rdfs:label \"{nombre}\" ." for iri, nombre in vistos]


def _orden(filas: list[dict]) -> list[dict]:
    return sorted(filas, key=lambda f: (f["esquema"], f["local"]))


def ttl_candidatos(filas: list[dict], ns: dict[str, str], manifiestos: pathlib.Path = MANIFIESTOS) -> str:
    pendientes = _orden([f for f in filas if f["estado"] == "candidato"])
    rechazados = _orden([f for f in filas if f["estado"] == "rechazado"])
    out = ["# Conceptos CANDIDATOS del tesauro LAAD — GENERADO por scripts/candidatos.py desde "
           "datos/candidatos_tesauro.csv. No editar a mano.",
           "# Un candidato es un concepto que un anotador necesitó y el tesauro no tenía: puede usarse en los "
           "registros (la validación",
           "# lo señala con un aviso, no con un error) hasta que se apruebe —pasa a ontologia/tesauro.ttl— o se "
           "rechace —queda aquí,",
           "# owl:deprecated, y usarlo es un error—. Política: ontologia/README.md.",
           "", PREFIJOS,
           "tes:candidatos a skos:Collection ; skos:prefLabel \"Conceptos candidatos (pendientes de revisión)\"@es ;",
           "    dct:description \"Conceptos propuestos durante la anotación que aún no forman parte del tesauro. "
           "No tienen versión: entran en una al aprobarse.\"@es"
           + (" ;" if pendientes else " .")]
    if pendientes:
        out.append("    skos:member " + " ,\n        ".join(f"<{ns[f['esquema']] + f['local']}>" for f in pendientes) + " .")
    out.append("")
    out += _agentes(pendientes + rechazados)
    if pendientes:
        out += ["", "# ── pendientes ──"] + [_concepto(f, ns, manifiestos) for f in pendientes]
    if rechazados:
        out += ["", "# ── rechazados (la IRI se conserva; no usar) ──"] + [_concepto(f, ns, manifiestos) for f in rechazados]
    return "\n".join(out) + "\n"


def seccion_aprobados(filas: list[dict], ns: dict[str, str], manifiestos: pathlib.Path = MANIFIESTOS) -> str:
    aprobados = _orden([f for f in filas if f["estado"] == "aprobado"])
    lineas = [INICIO]
    if aprobados:
        lineas.append("@prefix prov: <http://www.w3.org/ns/prov#> .")
        lineas.append("@prefix owl:  <http://www.w3.org/2002/07/owl#> .")
        lineas += _agentes(aprobados) + [_concepto(f, ns, manifiestos) for f in aprobados]
    lineas.append(FIN)
    return "\n".join(lineas) + "\n"


def aplicar(texto: str, filas: list[dict], ns: dict[str, str], manifiestos: pathlib.Path = MANIFIESTOS) -> str:
    """tesauro.ttl con la sección de aprobados puesta al día (se regenera entera; el resto no se toca)."""
    nueva = seccion_aprobados(filas, ns, manifiestos)
    if _SECCION.search(texto):
        return _SECCION.sub(lambda _: nueva, texto)
    return texto.rstrip("\n") + "\n\n" + nueva


def generar(filas: list[dict] | None = None, texto_tesauro: str | None = None,
            manifiestos: pathlib.Path = MANIFIESTOS) -> tuple[str, str]:
    """(texto de candidatos.ttl, texto de tesauro.ttl) que corresponden al CSV; no escribe nada."""
    filas = leer() if filas is None else filas
    texto = TESAURO.read_text(encoding="utf-8") if texto_tesauro is None else texto_tesauro
    ns = validar(filas, tesauro_base(texto), manifiestos)
    return ttl_candidatos(filas, ns, manifiestos), aplicar(texto, filas, ns, manifiestos)


def regenerar_formas_de_atributos() -> None:
    """Las formas de dominio y rango dependen de qué atributos existen (también los candidatos)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("atributos", RAIZ / "scripts/atributos.py")
    atributos = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(atributos)
    atributos.regenerar()


def regenerar() -> None:
    candidatos, tesauro = generar()
    CANDIDATOS.write_text(candidatos, encoding="utf-8")
    TESAURO.write_text(tesauro, encoding="utf-8")
    print(f"escrito {CANDIDATOS}\nescrito {TESAURO}")
    regenerar_formas_de_atributos()


# ───────────────────────── órdenes ─────────────────────────
def _buscar(filas: list[dict], ref: str) -> dict:
    esq, _, local = ref.partition("/")
    for f in filas:
        if (f["esquema"], f["local"]) == (esq, local):
            return f
    raise ErrorCandidatos(f"no hay ninguna fila {ref!r} en {CSV.name} (se escribe esquema/local, p. ej. cargos/granadero)")


def proponer(filas: list[dict], esquema: str, local: str, etiqueta: str, definicion: str, expediente: str,
             ejemplo: str, broader: str = "", por: str = "", fecha: str = "") -> dict:
    fila = dict(esquema=esquema, local=local, etiqueta=etiqueta, definicion=definicion, broader=broader,
                propuesto_por=por or "anotador", fecha=fecha or datetime.date.today().isoformat(),
                expediente=expediente, ejemplo=ejemplo, estado="candidato", reemplazado_por="")
    filas.append({k: v.strip() for k, v in fila.items()})
    return fila


def cambiar_estado(filas: list[dict], ref: str, estado: str, reemplazo: str = "") -> dict:
    fila = _buscar(filas, ref)
    if fila["estado"] != "candidato":
        raise ErrorCandidatos(f"{ref} ya está {fila['estado']}; solo se aprueba o rechaza un candidato pendiente")
    fila["estado"], fila["reemplazado_por"] = estado, reemplazo
    return fila


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Conceptos candidatos del tesauro LAAD (ontologia/README.md).")
    ap.add_argument("--proponer", nargs=4, metavar=("ESQUEMA", "LOCAL", "ETIQUETA", "DEFINICION"))
    ap.add_argument("--expediente", default="")
    ap.add_argument("--ejemplo", default="")
    ap.add_argument("--broader", default="")
    ap.add_argument("--por", default="", help="quién propone (persona o modelo, con el lote si procede)")
    ap.add_argument("--fecha", default="")
    ap.add_argument("--aprobar", metavar="ESQUEMA/LOCAL")
    ap.add_argument("--rechazar", metavar="ESQUEMA/LOCAL")
    ap.add_argument("--reemplazo", default="", help="con --rechazar: concepto vigente que debe usarse en su lugar")
    ap.add_argument("--listar", action="store_true")
    a = ap.parse_args(argv)
    try:
        filas = leer()
        original = [dict(f) for f in filas]
        if a.listar:
            for f in _orden(filas):
                print(f"{f['estado']:<10} {f['esquema'] + '/' + f['local']:<34} {f['etiqueta']}")
            return 0
        if a.proponer:
            f = proponer(filas, *a.proponer, expediente=a.expediente, ejemplo=a.ejemplo, broader=a.broader,
                         por=a.por, fecha=a.fecha)
            print(f"propuesto {f['esquema']}/{f['local']}")
        if a.aprobar:
            cambiar_estado(filas, a.aprobar, "aprobado")
            print(f"aprobado {a.aprobar}: es un cambio MENOR del tesauro; suba la versión (owl:versionInfo, "
                  f"dct:modified) y anótelo en ontologia/CHANGELOG.md")
        if a.rechazar:
            cambiar_estado(filas, a.rechazar, "rechazado", a.reemplazo)
            print(f"rechazado {a.rechazar}: si algún registro lo usa, la validación dará error hasta corregirlo")
        if filas != original:
            generar(filas)            # valida antes de tocar el CSV
            escribir_csv(filas)
        regenerar()
    except ErrorCandidatos as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
