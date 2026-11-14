"""Consulta estructurada sobre el grafo (SPARQL de consultas/*.rq) para el agente conversacional.

El agente NO genera SPARQL libre: elige una consulta con nombre y le pasa parámetros (bloque VALUES). Cada fila
devuelta lleva la cita literal, el tramo y el folio (o «no consta»), de modo que la respuesta se compone de
filas verificables (docs/D_extraccion_consulta.md §4).

Motor de consulta. Por defecto las consultas se ejecutan en Oxigraph (pyoxigraph: almacén de cuádruplas en Rust),
cargado desde los N-Quads canónicos de datos/grafo/ más el tesauro; el grafo por defecto de la consulta es la unión
de los grafos nombrados (materializada al cargar: ver _unir). La variable de entorno LAAD_MOTOR=rdflib vuelve al motor anterior (rdflib en memoria, lento
pero sin dependencias compiladas); tests/test_motores.py comprueba que los dos devuelven las mismas filas. rdflib
sigue siendo quien CONSTRUYE, serializa y valida el grafo: Oxigraph solo lo consulta.
"""
from __future__ import annotations

import os
import re
from functools import lru_cache
from pathlib import Path

import rdflib
from rdflib import URIRef

from . import fuente

RAIZ = Path(__file__).resolve().parents[2]
CONSULTAS = RAIZ / "consultas"
GRAFO = RAIZ / "datos" / "grafo"
ONTOLOGIA = RAIZ / "ontologia"
G_TESAURO = URIRef("https://w3id.org/laad/grafo/tesauro")
MOTORES = ("oxigraph", "rdflib")


def motor() -> str:
    """Motor de consulta en uso: «oxigraph» (por defecto) o «rdflib» (variable de entorno LAAD_MOTOR)."""
    m = os.environ.get("LAAD_MOTOR", "").strip().lower() or MOTORES[0]
    if m not in MOTORES:
        raise ValueError(f"LAAD_MOTOR={m!r} no es un motor conocido ({', '.join(MOTORES)})")
    return m


def vocabularios() -> list[Path]:
    """Lo que se carga junto al grafo en el grafo nombrado del tesauro: ontologia/tesauro.ttl y, si existe,
    ontologia/candidatos.ttl (conceptos candidatos aún no admitidos en el tesauro)."""
    return [r for r in (ONTOLOGIA / "tesauro.ttl", ONTOLOGIA / "candidatos.ttl") if r.exists()]


@lru_cache(maxsize=2)
def dataset(directorio: Path = GRAFO) -> rdflib.Dataset:
    """El corpus entero en rdflib: todos los datos/grafo/*.trig (uno por expediente más comun.trig) y el tesauro.
    Es el acceso para quien necesita la API de rdflib (pruebas, razonador) y el almacén del motor «rdflib»."""
    trigs = sorted(directorio.glob("*.trig"))
    if not trigs:
        raise FileNotFoundError(f"no hay ningún .trig en {directorio}; ejecute scripts/construir.py")
    ds = rdflib.Dataset(default_union=True)
    for trig in trigs:
        ds.parse(trig, format="trig")
    for voc in vocabularios():
        ds.graph(G_TESAURO).parse(voc)
    return ds


def archivos_grafo(directorio: Path = GRAFO) -> list[Path]:
    """Un archivo por parte del corpus (<exp> y comun): el .nq canónico si existe; si no, el .trig."""
    por_nombre = {p.stem: p for p in sorted(directorio.glob("*.trig"))}
    por_nombre.update({p.stem: p for p in sorted(directorio.glob("*.nq"))})
    if not por_nombre:
        raise FileNotFoundError(f"no hay ningún .nq ni .trig en {directorio}; ejecute scripts/construir.py")
    return [por_nombre[n] for n in sorted(por_nombre)]


def _cargar_vocabularios(store) -> None:
    import pyoxigraph as ox
    for voc in vocabularios():
        store.load(path=str(voc), format=ox.RdfFormat.TURTLE, to_graph=ox.NamedNode(str(G_TESAURO)))


def _unir(store) -> None:
    """Copia cada tripleta de los grafos nombrados al grafo por defecto del almacén: así el grafo por defecto ES la
    unión (un conjunto de tripletas), como en rdflib con default_union. No se usa la unión «al vuelo» de Oxigraph
    (use_default_graph_as_union) porque devuelve una solución por cada grafo que contiene la tripleta: la misma
    tripleta en dos grafos (p. ej. el título del fondo en el grafo de cada expediente) duplicaría filas. El precio
    es guardar cada tripleta dos veces."""
    store.update("INSERT { ?s ?p ?o } WHERE { GRAPH ?g { ?s ?p ?o } }")


def nuevo_almacen(directorio: Path = GRAFO, persistente: Path | None = None, masivo: bool = False):
    """Almacén Oxigraph NUEVO con el corpus de `directorio` y el tesauro. Con `persistente`, se guarda en disco en
    esa carpeta (reabrirlo: abrir_almacen); sin él, vive en memoria.

    `masivo` es la vía para corpus grandes (la medida en datos/grafo/escala.md): carga por lotes de Oxigraph, sin
    transacción, y la unión se carga como N-Triples —cada N-Quad canónico sin su grafo— en vez de con la
    actualización SPARQL de _unir, que mantiene toda la unión en una sola transacción. Exige los .nq canónicos
    (toda línea con su grafo, como los escribe laad.corpus.escribir)."""
    import pyoxigraph as ox
    store = ox.Store(str(persistente)) if persistente is not None else ox.Store()
    archivos = archivos_grafo(directorio)
    if masivo and all(r.suffix == ".nq" for r in archivos):
        for ruta in archivos:
            datos = ruta.read_bytes()
            store.bulk_load(input=datos, format=ox.RdfFormat.N_QUADS)
            store.bulk_load(input=_SIN_GRAFO.sub(b" .\n", datos), format=ox.RdfFormat.N_TRIPLES)
        for voc in vocabularios():
            store.bulk_load(path=str(voc), format=ox.RdfFormat.TURTLE, to_graph=ox.NamedNode(str(G_TESAURO)))
            store.bulk_load(path=str(voc), format=ox.RdfFormat.TURTLE)
    else:
        for ruta in archivos:
            store.load(path=str(ruta), format=ox.RdfFormat.N_QUADS if ruta.suffix == ".nq" else ox.RdfFormat.TRIG)
        _cargar_vocabularios(store)
        _unir(store)
    if persistente is not None:
        store.flush()
        store.optimize()
    return store


_SIN_GRAFO = re.compile(rb" <[^<>\s]*> \.\n")     # el grafo y el punto final de una línea N-Quads canónica


def abrir_almacen(carpeta: Path):
    """Abre en solo lectura un almacén Oxigraph en disco escrito por nuevo_almacen(persistente=…) o
    scripts/servir.py --volcar."""
    import pyoxigraph as ox
    return ox.Store.read_only(str(carpeta))


@lru_cache(maxsize=2)
def almacen(directorio: Path = GRAFO):
    """El corpus entero en Oxigraph (en memoria), recordado: es el almacén del motor por defecto."""
    return nuevo_almacen(directorio)


def consultable(ds: rdflib.Dataset):
    """Almacén listo para consultar a partir de un Dataset recién construido (laad.corpus.construir): unión de
    grafos por defecto y tesauro, igual que el corpus de disco. Devuelve un almacén del motor en uso (Oxigraph, o un
    rdflib.Dataset con LAAD_MOTOR=rdflib); en ambos casos se pasa a consultar(nombre, ds, …)."""
    if motor() == "oxigraph":
        import pyoxigraph as ox
        store = ox.Store()
        store.load(input=ds.serialize(format="nquads").encode("utf-8"), format=ox.RdfFormat.N_QUADS)
        _cargar_vocabularios(store)
        _unir(store)
        return store
    out = rdflib.Dataset(default_union=True)
    for g in ds.graphs():
        if len(g):
            destino = out.graph(g.identifier)
            for t in g:
                destino.add(t)
    for voc in vocabularios():
        out.graph(G_TESAURO).parse(voc)
    return out


def texto_consulta(nombre: str) -> str:
    return (CONSULTAS / "_prefijos.rq").read_text() + "\n" + (CONSULTAS / f"{nombre}.rq").read_text()


_IRI_SEGURA = re.compile(r"^https?://[^\s<>\"{}|\\^`]+$")


def _values(params: dict) -> str:
    """Bloque VALUES con IRIs validadas (el agente nunca inyecta texto SPARQL libre)."""
    lineas = []
    for k, v in params.items():
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", k):
            raise ValueError(f"parámetro no válido: {k}")
        vals = v if isinstance(v, (list, tuple)) else [v]
        celdas = []
        for x in vals:
            if not _IRI_SEGURA.match(str(x)):
                raise ValueError(f"IRI no válida para {k}: {x!r}")
            celdas.append(f"<{x}>")
        lineas.append(f"VALUES ?{k} {{ {' '.join(celdas)} }}")
    return "\n  ".join(lineas)


def consultar(nombre: str, ds=None, **params) -> list[dict]:
    """Ejecuta una consulta con nombre y devuelve sus filas como dict variable → texto (None si no está ligada;
    los literales, por su forma léxica: «true»/«false», «3», «1806-08-26»).

    Sin `ds` consulta el corpus de datos/grafo/ con el motor en uso (motor()) y recuerda el resultado (el grafo en
    disco no cambia durante el proceso; tras reconstruirlo, limpiar_cache()). `ds` puede ser un almacén Oxigraph
    (almacen(), consultable(), abrir_almacen(): su grafo por defecto es la unión) o un rdflib.Dataset/Graph: cada uno se consulta con su motor."""
    if ds is None:
        m = motor()
        clave = (m, nombre, tuple(sorted((k, tuple(map(str, v)) if isinstance(v, (list, tuple)) else str(v))
                                         for k, v in params.items())))
        if clave not in _RESULTADOS:
            _RESULTADOS[clave] = _consultar(nombre, almacen() if m == "oxigraph" else dataset(), params)
        return [dict(f) for f in _RESULTADOS[clave]]
    return _consultar(nombre, ds, params)


_RESULTADOS: dict[tuple, list[dict]] = {}


def limpiar_cache() -> None:
    """Olvida el corpus leído de disco (los dos motores) y los resultados recordados (p. ej. tras
    scripts/construir.py)."""
    _RESULTADOS.clear()
    dataset.cache_clear()
    almacen.cache_clear()


_MARCA = re.compile(r"(?m)^[ \t]*#PARAMETROS[ \t]*$")


def sparql(nombre: str, params: dict | None = None) -> str:
    """Texto SPARQL final de una consulta con nombre: prefijos + consulta con el bloque VALUES de los parámetros
    en el lugar de la línea #PARAMETROS."""
    q = texto_consulta(nombre)
    if params and not _MARCA.search(q):
        raise ValueError(f"la consulta {nombre} no admite parámetros")
    return _MARCA.sub(lambda _: "  " + _values(params or {}), q, count=1)


_CONCAT = re.compile(r'''GROUP_CONCAT\s*\(\s*DISTINCT\s+\?\w+\s*;\s*separator\s*=\s*"([^"]*)"\s*\)\s+AS\s+\?(\w+)''', re.I)


def _consultar(nombre: str, ds, params: dict) -> list[dict]:
    q = sparql(nombre, params)
    if isinstance(ds, rdflib.Graph):                 # rdflib.Dataset es un rdflib.Graph
        res = ds.query(q)
        filas = [{str(k): (str(r[k]) if r[k] is not None else None) for k in res.vars} for r in res]
    else:
        res = ds.query(q)                            # el grafo por defecto del almacén ya es la unión (_unir)
        nombres = [v.value for v in res.variables]
        # .value es el IRI de un NamedNode, la forma léxica de un Literal o la etiqueta de un nodo en blanco
        filas = [{n: (t.value if (t := sol[n]) is not None else None) for n in nombres} for sol in res]
    # SPARQL no fija el orden de los elementos de GROUP_CONCAT (cada motor da el suyo, y rdflib uno distinto en cada
    # ejecución): se ordenan aquí para que la fila sea la misma con cualquier motor y en cualquier ejecución.
    for separador, columna in _CONCAT.findall(q):
        for f in filas:
            if f.get(columna):
                f[columna] = separador.join(sorted(f[columna].split(separador)))
    return filas


def claves_orden(nombre: str) -> list[str]:
    """Variables del ORDER BY final de una consulta con nombre ([] si no ordena), sin ASC()/DESC(). Las filas que
    empatan en todas ellas pueden salir en distinto orden según el motor."""
    m = re.search(r"(?m)^ORDER BY\s+(.+?)\s*\Z", (CONSULTAS / f"{nombre}.rq").read_text())
    return re.findall(r"\?(\w+)", m.group(1)) if m else []


def nombres() -> list[str]:
    """Consultas con nombre disponibles (consultas/*.rq, sin el archivo de prefijos)."""
    return sorted(p.stem for p in CONSULTAS.glob("*.rq") if not p.stem.startswith("_"))


ID = "https://w3id.org/laad/id/"
TES = "https://w3id.org/laad/tesauro/"


# IRIs de recursos de UN expediente (parámetros de las consultas con nombre).
def expediente(exp: str) -> URIRef:
    """IRI archivística del expediente (último nivel de la jerarquía de su manifiesto): valor del parámetro
    ?expediente con el que las consultas se restringen a un expediente."""
    return URIRef(ID + fuente.manifiesto(exp)["jerarquia"][-1]["id"])


def pieza(exp: str, pid: str) -> URIRef: return URIRef(f"{ID}{exp}/pieza/{pid}")
def mencion(exp: str, mid: str) -> URIRef: return URIRef(f"{ID}{exp}/mencion/{mid}")
def afirmacion(exp: str, aid: str) -> URIRef: return URIRef(f"{ID}{exp}/afirmacion/{aid}")


# IRIs de la capa 4 (comunes al corpus: no llevan expediente).
def persona(slug: str) -> URIRef: return URIRef(f"{ID}persona/{slug}")
def evento(slug: str) -> URIRef: return URIRef(f"{ID}evento/{slug}")
def atributo(local: str) -> URIRef: return URIRef(f"{TES}atributo/{local}")
