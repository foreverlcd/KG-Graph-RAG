"""El corpus: todos los expedientes con manifiesto y las capas que comparten.

Cada expediente se configura SOLO en su manifiesto (datos/expedientes/<exp>.json): transcripción, marcas de folio,
jerarquía, «piezas», «registros», «fechas», «lote» (procedencia de la anotación) y «signatura_catalogo». Aquí no hay
ningún identificador de expediente: añadir uno es añadir su manifiesto y sus datos (datos/<exp>/…).

Capas propias de un expediente (grafos g:<exp>/documento, g:<exp>/texto/<lote>, g:<exp>/afirmaciones/<lote>) y
capas comunes (g:reconstruccion/R-x, g:argumentacion/R-x, g:procedencia, g:catalogo): una reconstrucción puede
reunir menciones de varios expedientes, y el catálogo los describe a todos.
"""
from __future__ import annotations

from pathlib import Path

import rdflib

from . import fuente, mapeo
from .esquema import Reconstruccion
from .registros import Lote
from .registros import cargar as _cargar_registros

RAIZ = Path(__file__).resolve().parents[2]
RECONSTRUCCIONES = RAIZ / "datos" / "reconstrucciones.jsonl"
CATALOGO = RAIZ / "datos" / "catalogo" / "fichas_pc03_pc04.jsonl"
GRAFO = RAIZ / "datos" / "grafo"
COMUN = "comun"     # nombre del archivo de las capas comunes (datos/grafo/comun.trig)
# Quién y cuándo extrajo las fichas del catálogo (capa C; no es de ningún expediente).
AGENTE_CATALOGO, FECHA_CATALOGO = "claude-opus-5-5", "2026-11-13T00:00:00"


def expedientes() -> list[str]:
    """Identificadores de los expedientes del corpus (uno por manifiesto)."""
    return fuente.expedientes()


def rutas_registros(exp: str) -> list[Path]:
    return [fuente.ruta(r) for r in fuente.manifiesto(exp)["registros"]]


def ruta_piezas(exp: str) -> Path:
    return fuente.ruta(fuente.manifiesto(exp)["piezas"])


def ruta_fechas(exp: str) -> Path | None:
    f = fuente.manifiesto(exp).get("fechas")
    return fuente.ruta(f) if f else None


def procedencia(exp: str) -> mapeo.Procedencia:
    """Procedencia del lote de anotación del expediente, tal como la declara su manifiesto («lote»)."""
    d = fuente.manifiesto(exp)["lote"]
    return mapeo.Procedencia(lote=d["nombre"], agente=d["agente"], tipo_agente=d["tipo_agente"], plan=d["plan"],
                             fecha=d["fecha"], validado_por=d.get("validado_por"))


def cargar(exp: str, registros: list[Path] | None = None) -> Lote:
    """Lote del expediente (piezas, menciones y afirmaciones), validado contra SU transcripción.
    `registros` sustituye a la lista del manifiesto (para validar un lote nuevo antes de incorporarlo)."""
    with fuente.usando_expediente(exp):
        return _cargar_registros(registros if registros is not None else rutas_registros(exp), ruta_piezas(exp))


def signaturas() -> dict[str, rdflib.URIRef]:
    """Signatura en el catálogo del ARC → IRI del expediente, para todos los manifiestos que la declaran."""
    return {s: mapeo.expediente_iri(e) for e in expedientes() if (s := fuente.manifiesto(e).get("signatura_catalogo"))}


def construir(exps: list[str] | None = None, reconstrucciones: Path | list[Reconstruccion] | None = RECONSTRUCCIONES,
              catalogo: Path | None = CATALOGO, lotes: dict[str, Lote] | None = None) -> rdflib.Dataset:
    """UN Dataset con las capas 1–3 de cada expediente (todos, o los de `exps`) y las capas comunes.

    Las reconstrucciones se validan contra los lotes cargados: si citan un expediente que no está en `exps`, es un
    error. `lotes` permite pasar lotes ya cargados (expediente → Lote) en vez de leerlos del manifiesto."""
    exps = list(exps) if exps is not None else expedientes()
    cargados: dict[str, Lote] = {}
    ds = mapeo.nuevo_dataset()
    for exp in exps:
        lote = (lotes or {}).get(exp) or cargar(exp)
        with fuente.usando_expediente(exp):
            mapeo.capas_expediente(ds, lote, procedencia(exp), ruta_fechas(exp),
                                   fuente.manifiesto(exp).get("fechas_argumento"))
        cargados[exp] = lote
    if reconstrucciones is not None:
        recs = (mapeo.cargar_reconstrucciones(reconstrucciones) if isinstance(reconstrucciones, Path)
                else list(reconstrucciones))
        mapeo.capa_reconstruccion(ds, recs, cargados)
    if catalogo is not None:
        mapeo.capa_catalogo(ds, catalogo, AGENTE_CATALOGO, FECHA_CATALOGO, signaturas())
    return ds


def partes(ds: rdflib.Dataset) -> dict[str, rdflib.Dataset]:
    """Reparte los grafos nombrados en un Dataset por expediente y uno común («comun»): es lo que se escribe."""
    out: dict[str, rdflib.Dataset] = {}
    for g in ds.graphs():
        if not len(g):
            continue
        nombre = mapeo.expediente_de_grafo(g.identifier) or COMUN
        if nombre not in out:
            out[nombre] = mapeo.nuevo_dataset()
        destino = out[nombre].graph(g.identifier)
        for t in g:
            destino.add(t)
    return out


def nquads(ds: rdflib.Dataset) -> str:
    """Forma canónica para git: N-Quads ordenado (el orden de TriG de rdflib no es estable entre ejecuciones)."""
    return "\n".join(sorted(l for l in ds.serialize(format="nquads").splitlines() if l.strip())) + "\n"


def escribir(ds: rdflib.Dataset, directorio: Path = GRAFO) -> list[Path]:
    """Escribe <exp>.trig/.nq por expediente y comun.trig/.nq; borra los .trig/.nq de expedientes que ya no están."""
    directorio.mkdir(parents=True, exist_ok=True)
    por_nombre = partes(ds)
    for viejo in list(directorio.glob("*.trig")) + list(directorio.glob("*.nq")):
        if viejo.stem not in por_nombre:
            viejo.unlink()
    escritos = []
    for nombre, parte in sorted(por_nombre.items()):
        trig = directorio / f"{nombre}.trig"
        parte.serialize(trig, format="trig")
        trig.with_suffix(".nq").write_text(nquads(parte), encoding="utf-8")
        escritos.append(trig)
    return escritos
