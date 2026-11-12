"""Mapeo DETERMINISTA de registros planos a RDF (TriG), una capa por grafo nombrado.

Mismo registro -> mismas tripletas; ids repetidos -> error. No hay LLM en este paso.
Patrones (docs/C_modelo.md):
  capa 1  g:documento            RiC-O (jerarquía, piezas, instanciaciones, tramos) + crm:E65_Creation (actuación)
  capa 2  g:texto/<lote>         picom:PersonObservation / roar:LocationObservation / roar:Observation + oa:Annotation
  capa 3  g:afirmaciones/<lote>  crm:E13_Attribute_Assignment (STAR) + PC14 para roles + oa:Annotation
  capa 4  g:reconstruccion/<id>  picom:PersonReconstruction / crm:E5_Event + crminf:I5/I2
  P       g:procedencia          PROV-O (cómo se produjo cada grafo)
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

from rdflib import BNode, Dataset, Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, PROV, RDF, RDFS, SKOS, XSD

from . import fuente
from .esquema import Afirmacion, Mencion, Pieza, Reconstruccion
from .registros import Lote

# ── espacios de nombres (verificados en vendor/, ver tests/test_terminos_existen.py) ──
RICO = Namespace("https://www.ica.org/standards/RiC/ontology#")
RST = Namespace("https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#")
CRM = Namespace("http://www.cidoc-crm.org/cidoc-crm/")
CRMINF = Namespace("http://www.cidoc-crm.org/extensions/crminf/")
OA = Namespace("http://www.w3.org/ns/oa#")
PICOM = Namespace("https://personsincontext.org/model#")
ROAR = Namespace("https://w3id.org/roar#")
TES = "https://w3id.org/laad/tesauro/"
ACT, ROL, COND, CARGO, ENT, ATR, POL, FUN, FZA, DOC, ANOT = (
    Namespace(TES + x + "/") for x in
    ("actuacion", "rol", "condicion", "cargo", "entidad", "atributo", "polaridad", "fundamento", "fuerza",
     "documento", "anotacion"))
ID = Namespace("https://w3id.org/laad/id/")
G = Namespace("https://w3id.org/laad/grafo/")
EXP = "cc-14-18"

PREFIJOS = dict(rico=RICO, rst=RST, crm=CRM, crminf=CRMINF, oa=OA, picom=PICOM, roar=ROAR, prov=PROV,
                skos=SKOS, dct=DCTERMS, owl=OWL, act=ACT, rol=ROL, cond=COND, cargo=CARGO, ent=ENT, atr=ATR,
                pol=POL, fun=FUN, fza=FZA, doc=DOC, anot=ANOT, id=ID, g=G)

# Fuerza institucional = f(tipo de actuación). Tabla documentada en docs/C_modelo.md §3.4.
FUERZA = {
    "certificacion": "testimonial", "declaracion-jurada": "testimonial", "reconocimiento-y-ratificacion": "testimonial",
    "peticion": "de-parte", "informe": "informativa", "oficio": "informativa", "caratula": "informativa",
    "vista-fiscal": "dictaminadora", "auto": "resolutiva", "auto-cabeza-de-proceso": "resolutiva",
    "decreto": "resolutiva", "notificacion": "fedataria", "desglose": "fedataria",
}
ATRIBUTOS_TIEMPO = {"fecha-del-hecho", "duracion"}


def iri(*partes: str) -> URIRef:
    return ID["/".join([EXP, *partes])]


def pieza_iri(p: str) -> URIRef: return iri("pieza", p)
def actuacion_iri(p: str) -> URIRef: return iri("actuacion", p)
def mencion_iri(m: str) -> URIRef: return iri("mencion", m)
def afirmacion_iri(a: str) -> URIRef: return iri("afirmacion", a)
def hecho_iri(h: str) -> URIRef: return iri("hecho", h)


def transcripcion_iri() -> URIRef:
    return iri("transcripcion", fuente.sha256()[:12])


def tramo_iri(t: str) -> URIRef:
    return URIRef(f"{transcripcion_iri()}/{t}")


@dataclass(frozen=True)
class Procedencia:
    """Metadatos de cómo se produjo un lote (capa P)."""
    lote: str
    agente: str                # p. ej. "claude-opus-5-5" o "anotador-a"
    tipo_agente: str           # "SoftwareAgent" | "Person"
    plan: str                  # p. ej. "prompts/extraccion_v1.md" o "anotacion-manual"
    fecha: str                 # ISO 8601
    validado_por: str | None = None


def _ns(ds: Dataset) -> None:
    for k, v in PREFIJOS.items():
        ds.bind(k, v)


def _apelacion(g: Graph, sujeto: URIRef, texto: str, sufijo: str = "nombre") -> URIRef:
    ap = URIRef(f"{sujeto}/{sufijo}")
    g.add((sujeto, CRM.P1_is_identified_by, ap))
    g.add((ap, RDF.type, CRM.E41_Appellation))
    g.add((ap, CRM.P190_has_symbolic_content, Literal(texto)))
    return ap


def _ancla(g: Graph, cuerpo: URIRef, ident: str, tramo: str, cita: str, motivo: URIRef) -> None:
    """oa:Annotation que ancla un registro a su cita literal en el tramo."""
    tr = fuente.tramo(tramo)
    col, idx = fuente._mapa_colapsado(tr.texto)
    c = fuente.colapsar(cita)
    k = col.find(c)
    if k < 0:
        raise ValueError(f"{ident}: cita no anclable en {tramo}")
    ini, fin = idx[k], idx[k + len(c) - 1] + 1
    an = iri("anotacion", ident)
    tgt, qs, ps = (URIRef(f"{an}/{x}") for x in ("objetivo", "cita", "posicion"))
    g.add((an, RDF.type, OA.Annotation))
    g.add((an, OA.hasBody, cuerpo))
    g.add((an, OA.motivatedBy, motivo))
    g.add((an, OA.hasTarget, tgt))
    g.add((tgt, RDF.type, OA.SpecificResource))
    g.add((tgt, OA.hasSource, tramo_iri(tramo)))
    g.add((tgt, OA.hasSelector, qs))
    g.add((tgt, OA.hasSelector, ps))
    g.add((qs, RDF.type, OA.TextQuoteSelector))
    g.add((qs, OA.exact, Literal(cita)))
    g.add((ps, RDF.type, OA.TextPositionSelector))
    g.add((ps, OA.start, Literal(ini, datatype=XSD.nonNegativeInteger)))
    g.add((ps, OA.end, Literal(fin, datatype=XSD.nonNegativeInteger)))


def _participa(g: Graph, actividad: URIRef, actor: URIRef, rol: str, ident: str) -> None:
    """PC14_carried_out_by + P14.1_in_the_role_of (patrón del archivo _PC de CRM 7.1.3) y el atajo P14."""
    pc = URIRef(f"{actividad}/participacion/{ident}")
    g.add((pc, RDF.type, CRM.PC14_carried_out_by))
    g.add((pc, CRM.P01_has_domain, actividad))
    g.add((pc, CRM.P02_has_range, actor))
    g.add((pc, CRM["P14.1_in_the_role_of"], ROL[rol]))
    g.add((actividad, CRM.P14_carried_out_by, actor))


# ───────────────────────── capa 1 ─────────────────────────
def capa_documento(ds: Dataset, piezas: dict[str, Pieza]) -> Graph:
    g = ds.graph(G.documento)
    arc = ID["arc"]
    fondo, secc, serie, leg, exp = (URIRef(f"{arc}/{x}") for x in
                                    ("fondo/intendencia", "seccion/causas-criminales", "serie/cc-cusco",
                                     "legajo/cc-14", "expediente/cc-14-18"))
    jer = [(fondo, RST.Fonds, "Intendencia", None), (secc, DOC.seccion, "Causas Criminales", fondo),
           (serie, RST.Series, "Cusco", secc), (leg, DOC.legajo, "Legajo 14", serie),
           (exp, RST.File, "Expediente 18", leg)]
    for nodo, tipo, titulo, padre in jer:
        g.add((nodo, RDF.type, RICO.RecordSet))
        g.add((nodo, RICO.hasRecordSetType, tipo))
        g.add((nodo, RICO.title, Literal(titulo, lang="es")))
        if padre is not None:
            g.add((nodo, RICO.isOrWasIncludedIn, padre))
            g.add((padre, RICO.includesOrIncluded, nodo))
    # instanciación original (no disponible: solo se describe) y transcripción derivada
    orig, trans = iri("original"), transcripcion_iri()
    g.add((orig, RDF.type, RICO.Instantiation))
    g.add((orig, RICO.isOrWasInstantiationOf, exp))
    g.add((orig, RDFS.comment, Literal("Expediente físico en el ARC; imágenes no disponibles en el proyecto.", lang="es")))
    g.add((trans, RDF.type, RICO.Instantiation))
    g.add((trans, RICO.isOrWasInstantiationOf, exp))
    g.add((trans, RICO.isOrWasDerivedFromInstantiation, orig))
    g.add((trans, DCTERMS.identifier, Literal("sha256:" + fuente.sha256())))
    g.add((trans, DCTERMS.type, DOC["transcripcion-paleografica"]))
    previo = None
    for t in fuente.tramos():
        ti = tramo_iri(t.id)
        g.add((ti, RDF.type, RICO.Instantiation))
        g.add((ti, DCTERMS.type, DOC.tramo))
        g.add((ti, RICO.isOrWasComponentOf, trans))
        g.add((ti, RDFS.label, Literal(t.id)))
        g.add((ti, RICO.title, Literal(f"{t.id} (líneas {t.linea_inicio}-{t.linea_fin})")))
        if t.folio:
            fo = iri("original", "folio", t.folio)
            g.add((fo, RDF.type, RICO.Instantiation))
            g.add((fo, DCTERMS.type, DOC.folio))
            g.add((fo, RICO.isOrWasComponentOf, orig))
            g.add((fo, RICO.title, Literal(f"folio {t.folio}")))
            g.add((ti, RICO.isOrWasDerivedFromInstantiation, fo))
        if previo is not None:
            g.add((previo, RICO.directlyPrecedesInSequence, ti))
        previo = ti
    # piezas y actuaciones
    previo = None
    for p in sorted(piezas.values(), key=lambda x: x.orden):
        pi, ai = pieza_iri(p.id), actuacion_iri(p.id)
        g.add((pi, RDF.type, RICO.Record))
        g.add((pi, RDF.type, CRM.E31_Document))
        g.add((pi, RICO.title, Literal(p.titulo, lang="es")))
        g.add((pi, RDFS.label, Literal(p.id)))
        g.add((pi, RICO.hasDocumentaryFormType, ACT[p.tipo_actuacion]))
        for t in p.tramos:
            g.add((pi, RICO.hasOrHadInstantiation, tramo_iri(t)))
        if p.ajena_al_expediente:
            g.add((pi, RDFS.comment, Literal("Documento ajeno al expediente capturado junto a él (docs/01_materiales.md).", lang="es")))
        else:
            g.add((pi, RICO.isOrWasIncludedIn, exp))
            g.add((exp, RICO.includesOrIncluded, pi))
            if previo is not None:
                g.add((previo, RICO.directlyPrecedesInSequence, pi))
            previo = pi
        g.add((ai, RDF.type, CRM.E65_Creation))
        g.add((ai, CRM.P94_has_created, pi))
        g.add((ai, CRM.P2_has_type, ACT[p.tipo_actuacion]))
        g.add((ai, CRM.P2_has_type, FZA[FUERZA[p.tipo_actuacion]]))
        if p.fecha_escrita:
            fecha = URIRef(f"{pi}/fecha")
            g.add((pi, RICO.hasCreationDate, fecha))
            g.add((fecha, RDF.type, RICO.Date))
            g.add((fecha, RICO.expressedDate, Literal(p.fecha_escrita)))
            ts = URIRef(f"{ai}/tiempo")
            g.add((ai, CRM["P4_has_time-span"], ts))
            g.add((ts, RDF.type, CRM["E52_Time-Span"]))
            _apelacion(g, ts, p.fecha_escrita, "expresion")
        if p.lugar_escrito:
            g.add((ai, CRM.P3_has_note, Literal(f"Data (literal): {p.lugar_escrito}")))
    return g


# ───────────────────────── capa 2 ─────────────────────────
CLASES_MENCION = {
    "persona": (PICOM.PersonObservation, CRM.E21_Person),
    "lugar": (ROAR.LocationObservation, CRM.E53_Place),
    "grupo": (ROAR.Observation, CRM.E74_Group),
}


def capa_texto(ds: Dataset, menciones: dict[str, Mencion], lote: str) -> Graph:
    g = ds.graph(G[f"texto/{lote}"])
    for mm in menciones.values():
        mi = mencion_iri(mm.id)
        for c in CLASES_MENCION[mm.clase]:
            g.add((mi, RDF.type, c))
        g.add((mi, RDFS.label, Literal(mm.texto)))
        # PiCo enlaza la observación con su fuente mediante prov:hadPrimarySource; ROAR, con roar:documentedIn.
        # No se usa prov:hadPrimarySource en observaciones ROAR: ROAR declara rdfs:domain roar:Reconstruction para
        # prov:wasDerivedFrom (superpropiedad de hadPrimarySource) y Observation ⊓ Reconstruction = ∅ (ver
        # docs/C_modelo.md §7, defecto D1, hallado con el razonador).
        fuente_prop = PROV.hadPrimarySource if mm.clase == "persona" else ROAR.documentedIn
        g.add((mi, fuente_prop, pieza_iri(mm.pieza)))
        _apelacion(g, mi, mm.texto)
        if mm.tipo_entidad:
            g.add((mi, CRM.P2_has_type, ENT[mm.tipo_entidad]))
        if mm.rol_en_pieza:
            g.add((mi, PICOM.hasRole, ROL[mm.rol_en_pieza]))
            _participa(g, actuacion_iri(mm.pieza), mi, mm.rol_en_pieza, mm.id)
        _ancla(g, mi, mm.id, mm.tramo, mm.cita, OA.identifying)
    return g


# ───────────────────────── capa 3 ─────────────────────────
def _ref(campo) -> URIRef | None:
    if getattr(campo, "mencion", None):
        return mencion_iri(campo.mencion)
    if getattr(campo, "pieza", None):
        return pieza_iri(campo.pieza)
    if getattr(campo, "hecho", None):
        return hecho_iri(campo.hecho)
    return None


def capa_afirmaciones(ds: Dataset, lote_reg: Lote, lote: str) -> Graph:
    g = ds.graph(G[f"afirmaciones/{lote}"])
    for a in lote_reg.afirmaciones.values():
        ai = afirmacion_iri(a.id)
        act = actuacion_iri(a.pieza)
        g.add((ai, RDF.type, CRM.E13_Attribute_Assignment))
        g.add((ai, RDFS.label, Literal(a.id)))
        g.add((ai, CRM.P9i_forms_part_of, act))
        _participa(g, ai, mencion_iri(a.afirmante), a.rol_afirmante, "afirmante")
        g.add((ai, CRM.P140_assigned_attribute_to, _ref(a.sujeto)))
        g.add((ai, CRM.P177_assigned_property_of_type, ATR[a.atributo]))
        g.add((ai, CRM.P2_has_type, POL[a.polaridad]))
        g.add((ai, CRM.P2_has_type, FUN[a.fundamento]))
        tipo_act = lote_reg.piezas[a.pieza].tipo_actuacion
        g.add((ai, CRM.P2_has_type, FZA[FUERZA[tipo_act]]))
        if a.rol_en_hecho:
            g.add((ai, CRM.P2_has_type, ROL[a.rol_en_hecho]))
        if a.sujeto.eliptico:
            g.add((ai, CRM.P2_has_type, ANOT["sujeto-eliptico"]))
        if a.nota:
            g.add((ai, CRM.P3_has_note, Literal(a.nota, lang="es")))
        # valor
        v = a.valor
        if v.concepto:
            esquema = CARGO if v.concepto in _locales(CARGO) else COND
            g.add((ai, CRM.P141_assigned, esquema[v.concepto]))
        elif _ref(v) is not None:
            g.add((ai, CRM.P141_assigned, _ref(v)))
        if v.literal and _ref(v) is None and not v.concepto:
            vi = URIRef(f"{ai}/valor")
            if a.atributo in ATRIBUTOS_TIEMPO:
                g.add((vi, RDF.type, CRM["E52_Time-Span"]))
                _apelacion(g, vi, v.literal, "expresion")
            else:
                g.add((vi, RDF.type, CRM.E33_Linguistic_Object))
                g.add((vi, CRM.P190_has_symbolic_content, Literal(v.literal)))
            g.add((ai, CRM.P141_assigned, vi))
        elif v.literal:
            g.add((ai, CRM.P3_has_note, Literal(f"valor literal: {v.literal}")))
        # hechos narrados: existen solo como objeto de discurso de su pieza
        for h in filter(None, [a.sujeto.hecho, v.hecho]):
            hi = hecho_iri(h)
            g.add((hi, RDF.type, CRM.E5_Event))
            g.add((hi, RDFS.label, Literal(h)))
            g.add((hi, PROV.hadPrimarySource, pieza_iri(a.pieza)))
        _ancla(g, ai, a.id, a.tramo, a.cita, OA.describing)
    return g


_LOCALES_CACHE: dict[str, set[str]] = {}


def _locales(ns: Namespace) -> set[str]:
    from .esquema import conceptos
    clave = str(ns)
    if clave not in _LOCALES_CACHE:
        nombre = clave.rstrip("/").rsplit("/", 1)[1]
        esquema = {"cargo": "cargos", "condicion": "condiciones"}[nombre]
        _LOCALES_CACHE[clave] = set(conceptos(esquema))
    return _LOCALES_CACHE[clave]


# ───────────────────────── capa 4 ─────────────────────────
def capa_reconstruccion(ds: Dataset, recs: list[Reconstruccion], lote_reg: Lote) -> None:
    for r in recs:
        gi = G[f"reconstruccion/{r.id}"]
        g = ds.graph(gi)
        slug = r.id[2:]
        autor = ID[f"agente/{r.autor}"]
        if r.tipo == "identidad":
            clases = {lote_reg.menciones[m].clase for m in r.menciones}
            if len(clases) != 1:
                raise ValueError(f"{r.id}: menciones de clases distintas {clases}")
            clase = clases.pop()
            nodo = ID[f"{clase}/{slug}"]
            tipos = {"persona": (PICOM.PersonReconstruction, CRM.E21_Person),
                     "lugar": (ROAR.LocationReconstruction, CRM.E53_Place),
                     "grupo": (ROAR.Reconstruction, CRM.E74_Group)}[clase]
            for t in tipos:
                g.add((nodo, RDF.type, t))
            for m in r.menciones:
                g.add((nodo, PROV.wasDerivedFrom, mencion_iri(m)))
        elif r.tipo == "hecho":
            nodo = ID[f"evento/{slug}"]
            g.add((nodo, RDF.type, CRM.E5_Event))
            for h in r.menciones:  # aquí 'menciones' lleva ids de hechos narrados
                g.add((nodo, PROV.wasDerivedFrom, hecho_iri(h)))
        else:
            raise ValueError(f"{r.id}: tipo {r.tipo} aún no mapeado")
        g.add((nodo, RDFS.label, Literal(r.etiqueta, lang="es")))
        g.add((nodo, PROV.wasGeneratedBy, ID[f"inferencia/{r.id}"]))
        if r.externo:
            ide = URIRef(f"{nodo}/identificador-externo")
            g.add((nodo, CRM.P48_has_preferred_identifier, ide))
            g.add((ide, RDF.type, CRM.E42_Identifier))
            g.add((ide, CRM.P190_has_symbolic_content, Literal(r.externo)))
            g.add((nodo, RDFS.seeAlso, URIRef(r.externo)))
        # argumentación CRMinf: la inferencia concluye una creencia sobre ESTE grafo nombrado
        inf, cre = ID[f"inferencia/{r.id}"], ID[f"creencia/{r.id}"]
        g.add((inf, RDF.type, CRMINF.I5_Inference_Making))
        g.add((inf, CRM.P14_carried_out_by, autor))
        g.add((inf, CRM.P3_has_note, Literal(r.argumento, lang="es")))
        for p in r.premisas:
            g.add((inf, CRM.P17_was_motivated_by, afirmacion_iri(p)))
        g.add((inf, CRMINF.J2_concluded_that, cre))
        g.add((cre, RDF.type, CRMINF.I2_Belief))
        g.add((cre, CRMINF.J4_that, gi))
        g.add((gi, RDF.type, CRMINF.I4_Proposition_Set))
        g.add((cre, CRMINF.J5_holds_to_be, Literal(r.creencia)))
        ts = URIRef(f"{inf}/tiempo")
        g.add((inf, CRM["P4_has_time-span"], ts))
        g.add((ts, RDF.type, CRM["E52_Time-Span"]))
        g.add((ts, CRM.P82a_begin_of_the_begin, Literal(r.fecha, datatype=XSD.date)))
        g.add((ts, CRM.P82b_end_of_the_end, Literal(r.fecha, datatype=XSD.date)))
        pg = ds.graph(G.procedencia)
        pg.add((gi, RDF.type, PROV.Entity))
        pg.add((gi, PROV.wasAttributedTo, autor))
        pg.add((gi, PROV.generatedAtTime, Literal(r.fecha, datatype=XSD.date)))
        pg.add((gi, DCTERMS.type, ID["capa/reconstruccion"]))
        _agente(pg, r.autor)


def capa_fechas(ds: Dataset, ruta: Path, autor: str, fecha: str) -> None:
    """Capa 4: lectura normalizada de las fechas escritas (una reconstrucción más, con autor y creencia).
    La fecha escrita (capa 1) no se toca; aquí se añade un segundo E52 con P82a/P82b."""
    import csv
    rid = "R-fechas-normalizadas"
    gi = G[f"reconstruccion/{rid}"]
    g = ds.graph(gi)
    for fila in csv.DictReader(ruta.open(encoding="utf-8")):
        act = actuacion_iri(fila["pieza"])
        ts = URIRef(f"{act}/tiempo-normalizado")
        g.add((act, CRM["P4_has_time-span"], ts))
        g.add((ts, RDF.type, CRM["E52_Time-Span"]))
        g.add((ts, CRM.P82a_begin_of_the_begin, Literal(fila["fecha"], datatype=XSD.date)))
        g.add((ts, CRM.P82b_end_of_the_end, Literal(fila["fecha"], datatype=XSD.date)))
        if fila["nota"]:
            g.add((ts, CRM.P3_has_note, Literal(fila["nota"], lang="es")))
    inf, cre = ID[f"inferencia/{rid}"], ID[f"creencia/{rid}"]
    g.add((inf, RDF.type, CRMINF.I5_Inference_Making))
    g.add((inf, CRM.P14_carried_out_by, ID[f"agente/{autor}"]))
    g.add((inf, CRM.P3_has_note, Literal("Lectura literal de cada fecha escrita al calendario gregoriano, sin corregir "
                                          "las fechas de secuencia imposible (F1–F6); el control de secuencia las señala.", lang="es")))
    g.add((inf, CRMINF.J2_concluded_that, cre))
    g.add((cre, RDF.type, CRMINF.I2_Belief))
    g.add((cre, CRMINF.J4_that, gi))
    g.add((gi, RDF.type, CRMINF.I4_Proposition_Set))
    g.add((cre, CRMINF.J5_holds_to_be, Literal("probable")))
    ts = URIRef(f"{inf}/tiempo")
    g.add((inf, CRM["P4_has_time-span"], ts))
    g.add((ts, RDF.type, CRM["E52_Time-Span"]))
    g.add((ts, CRM.P82a_begin_of_the_begin, Literal(fecha, datatype=XSD.date)))
    g.add((ts, CRM.P82b_end_of_the_end, Literal(fecha, datatype=XSD.date)))
    pg = ds.graph(G.procedencia)
    pg.add((gi, RDF.type, PROV.Entity))
    pg.add((gi, PROV.wasAttributedTo, ID[f"agente/{autor}"]))
    pg.add((gi, PROV.generatedAtTime, Literal(fecha, datatype=XSD.date)))
    pg.add((gi, DCTERMS.type, ID["capa/reconstruccion"]))
    _agente(pg, autor)


def _agente(pg: Graph, nombre: str, tipo: str | None = None) -> URIRef:
    ag = ID[f"agente/{nombre}"]
    tipo = tipo or ("SoftwareAgent" if nombre.startswith("claude") else "Person")
    pg.add((ag, RDF.type, PROV[tipo]))
    pg.add((ag, RDF.type, PROV.Agent))
    pg.add((ag, RDF.type, CRM.E39_Actor))
    pg.add((ag, RDFS.label, Literal(nombre)))
    return ag


# ───────────────────────── capa P ─────────────────────────
def procedencia(ds: Dataset, pr: Procedencia, grafos: list[tuple[URIRef, str]]) -> None:
    pg = ds.graph(G.procedencia)
    trans = transcripcion_iri()
    pg.add((trans, RDF.type, PROV.Entity))
    pg.add((trans, DCTERMS.identifier, Literal("sha256:" + fuente.sha256())))
    act = ID[f"actividad/{pr.lote}"]
    ag = _agente(pg, pr.agente, pr.tipo_agente)
    plan = ID[f"plan/{pr.plan}"]
    pg.add((plan, RDF.type, PROV.Plan))
    pg.add((plan, RDFS.label, Literal(pr.plan)))
    pg.add((act, RDF.type, PROV.Activity))
    pg.add((act, PROV.used, trans))
    pg.add((act, PROV.wasAssociatedWith, ag))
    asoc = URIRef(f"{act}/asociacion")
    pg.add((act, PROV.qualifiedAssociation, asoc))
    pg.add((asoc, RDF.type, PROV.Association))
    pg.add((asoc, PROV.agent, ag))
    pg.add((asoc, PROV.hadPlan, plan))
    pg.add((act, PROV.endedAtTime, Literal(pr.fecha, datatype=XSD.dateTime)))
    for gi, capa in grafos:
        pg.add((gi, RDF.type, PROV.Entity))
        pg.add((gi, PROV.wasGeneratedBy, act))
        pg.add((gi, PROV.wasAttributedTo, ag))
        pg.add((gi, PROV.wasDerivedFrom, trans))
        pg.add((gi, PROV.generatedAtTime, Literal(pr.fecha, datatype=XSD.dateTime)))
        pg.add((gi, DCTERMS.type, ID[f"capa/{capa}"]))
    if pr.validado_por:
        val = ID[f"actividad/validacion-{pr.lote}"]
        vag = _agente(pg, pr.validado_por, "Person")
        pg.add((val, RDF.type, PROV.Activity))
        pg.add((val, PROV.wasAssociatedWith, vag))
        for gi, _ in grafos:
            pg.add((val, PROV.used, gi))


# ───────────────────────── orquestación ─────────────────────────
def construir(lote_reg: Lote, pr: Procedencia, reconstrucciones: list[Reconstruccion] = (),
              fechas: Path | None = None) -> Dataset:
    if lote_reg.errores:
        raise ValueError("lote con errores; no se mapea:\n" + "\n".join(lote_reg.errores))
    ds = Dataset()
    _ns(ds)
    gdoc = capa_documento(ds, lote_reg.piezas)
    gtex = capa_texto(ds, lote_reg.menciones, pr.lote)
    gafi = capa_afirmaciones(ds, lote_reg, pr.lote)
    procedencia(ds, Procedencia(lote="curacion-piezas-v1", agente=pr.agente, tipo_agente=pr.tipo_agente,
                                plan="curacion-manual-piezas", fecha=pr.fecha),
                [(gdoc.identifier, "documento")])
    procedencia(ds, pr, [(gtex.identifier, "texto"), (gafi.identifier, "afirmaciones")])
    capa_reconstruccion(ds, list(reconstrucciones), lote_reg)
    if fechas is not None:
        capa_fechas(ds, fechas, pr.agente, pr.fecha[:10])
    return ds


def union(ds: Dataset) -> Graph:
    g = Graph()
    for k, v in PREFIJOS.items():
        g.bind(k, v)
    for ctx in ds.graphs():
        for t in ctx:
            g.add(t)
    return g


def cargar_reconstrucciones(ruta: Path) -> list[Reconstruccion]:
    out = []
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        if linea.strip():
            out.append(Reconstruccion(**json.loads(linea)))
    return out
