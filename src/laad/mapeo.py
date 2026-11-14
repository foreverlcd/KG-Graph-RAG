"""Mapeo DETERMINISTA de registros planos a RDF (TriG), una capa por grafo nombrado.

Mismo registro -> mismas tripletas; ids repetidos -> error. No hay LLM en este paso.
Patrones (docs/C_modelo.md). Las capas 1–3 son de UN expediente y su grafo lleva el expediente en el nombre;
las demás son comunes a todo el corpus (una reconstrucción puede reunir menciones de varios expedientes):
  capa 1  g:<exp>/documento            RiC-O (jerarquía, piezas, instanciaciones, tramos) + crm:E65_Creation
  capa 2  g:<exp>/texto/<lote>         picom:PersonObservation / roar:LocationObservation / roar:Observation + oa:Annotation
  capa 3  g:<exp>/afirmaciones/<lote>  crm:E13_Attribute_Assignment (STAR) + PC14 para roles + oa:Annotation
  capa 4  g:reconstruccion/<id>        picom:PersonReconstruction / crm:E5_Event (común)
          g:argumentacion/<id>         crminf:I5/I2 (común)
  P       g:procedencia                PROV-O (cómo se produjo cada grafo; común)
  C       g:catalogo                   fichas del catálogo del ARC (común)
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

from rdflib import BNode, Dataset, Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, PROV, RDF, RDFS, SKOS, XSD

from . import fuente
from .esquema import Afirmacion, Mencion, Pieza, Reconstruccion, separar_ref
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
# Places gazetteer of Spanish America 1701-1808 (HGIS de las Indias), Harvard Dataverse; CC BY-NC-SA 4.0:
# solo se citan sus identificadores, nunca se copian geometrías ni atributos.
HGIS_DATASET = "https://doi.org/10.7910/DVN/FUSJD3"
CONTEXTO_CITA = 32  # caracteres de prefijo/sufijo en el TextQuoteSelector
# El expediente NO es una constante: lo fija fuente.usando_expediente(...) (revisión C2).

PREFIJOS = dict(rico=RICO, rst=RST, crm=CRM, crminf=CRMINF, oa=OA, picom=PICOM, roar=ROAR, prov=PROV,
                skos=SKOS, dct=DCTERMS, owl=OWL, act=ACT, rol=ROL, cond=COND, cargo=CARGO, ent=ENT, atr=ATR,
                pol=POL, fun=FUN, fza=FZA, doc=DOC, anot=ANOT, id=ID, g=G)

ATRIBUTOS_TIEMPO = {"fecha-del-hecho", "duracion"}


def fuerza_de(tipo_actuacion: str) -> str:
    """Fuerza institucional de un tipo de actuación: dato del tesauro (act:x skos:related fza:y), no código."""
    from .esquema import _tesauro
    g = _tesauro()
    fz = [str(o).rsplit("/", 1)[1] for o in g.objects(ACT[tipo_actuacion], SKOS.related)
          if str(o).startswith(str(FZA))]
    if len(fz) != 1:
        raise ValueError(f"el tipo de actuación {tipo_actuacion!r} no tiene exactamente una fuerza en el tesauro "
                         f"(¿es un concepto abstracto, no hoja?)")
    return fz[0]


def concepto_iri(local: str, atributo: str) -> URIRef:
    """IRI de un concepto admitido por el atributo (dct:conformsTo en el tesauro)."""
    from .esquema import _tesauro
    g = _tesauro()
    for esq in g.objects(ATR[atributo], DCTERMS.conformsTo):
        for c in g.subjects(SKOS.inScheme, esq):
            if str(c).rsplit("/", 1)[1] == local:
                return URIRef(c)
    raise ValueError(f"concepto {local!r} no admitido por {atributo!r}")


def exp_id() -> str:
    return fuente.expediente_actual()


def iri(*partes: str, exp: str | None = None) -> URIRef:
    """IRI de un recurso de un expediente (el indicado o, si no, el que está en curso)."""
    return ID["/".join([exp or exp_id(), *partes])]


def grafo_iri(*partes: str, exp: str | None = None) -> URIRef:
    """Grafo nombrado de una capa propia de un expediente: g:<exp>/documento, g:<exp>/texto/<lote>…"""
    return G["/".join([exp or exp_id(), *partes])]


def expediente_de_grafo(gid) -> str | None:
    """Expediente al que pertenece un grafo nombrado, o None si es un grafo común (capa 4, procedencia, catálogo)."""
    m = re.match(re.escape(str(G)) + r"([^/]+)/(documento$|texto/|afirmaciones/)", str(gid))
    return m.group(1) if m else None


def pieza_iri(p: str, exp: str | None = None) -> URIRef: return iri("pieza", p, exp=exp)
def actuacion_iri(p: str, exp: str | None = None) -> URIRef: return iri("actuacion", p, exp=exp)
def mencion_iri(m: str, exp: str | None = None) -> URIRef: return iri("mencion", m, exp=exp)
def afirmacion_iri(a: str, exp: str | None = None) -> URIRef: return iri("afirmacion", a, exp=exp)
def hecho_iri(h: str, exp: str | None = None) -> URIRef: return iri("hecho", h, exp=exp)


def expediente_iri(exp: str | None = None) -> URIRef:
    """IRI archivística del expediente: el último nivel de la jerarquía de su manifiesto."""
    return ID[fuente.manifiesto(exp)["jerarquia"][-1]["id"]]


def transcripcion_iri(exp: str | None = None) -> URIRef:
    return iri("transcripcion", fuente.sha256(fuente.ruta_transcripcion(exp))[:12], exp=exp)


def tramo_iri(t: str) -> URIRef:
    return URIRef(f"{transcripcion_iri()}/{t}")


@dataclass(frozen=True)
class Procedencia:
    """Metadatos de cómo se produjo un lote (capa P)."""
    lote: str                  # nombre del lote DENTRO de su expediente
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
    # prefijo y sufijo (Web Annotation §4.2.4): desambiguan citas repetidas en el tramo sin depender de la posición
    if ini > 0:
        g.add((qs, OA.prefix, Literal(tr.texto[max(0, ini - CONTEXTO_CITA):ini])))
    if fin < len(tr.texto):
        g.add((qs, OA.suffix, Literal(tr.texto[fin:fin + CONTEXTO_CITA])))
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
    g = ds.graph(grafo_iri("documento"))
    pref = {"rst": RST, "doc": DOC}
    jer = []
    for n in fuente.manifiesto()["jerarquia"]:
        ns, local = n["tipo"].split(":")
        jer.append((ID[n["id"]], pref[ns][local], n["titulo"], ID[n["padre"]] if n["padre"] else None))
    exp = jer[-1][0]          # el último nivel del manifiesto es el expediente
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
    if ext := fuente.manifiesto().get("extension"):
        # RiC-O 1.1 sí expresa la extensión en folios (rico:CarrierExtent); lo que no tiene es el folio direccionable (D5)
        ex, um = URIRef(f"{orig}/extension"), URIRef(f"{orig}/extension/unidad")
        g.add((orig, RICO.hasExtent, ex))
        g.add((ex, RDF.type, RICO.CarrierExtent))
        g.add((ex, RICO.quantity, Literal(str(ext["cantidad"]), datatype=XSD.decimal)))
        g.add((ex, RICO.hasUnitOfMeasurement, um))
        g.add((um, RDF.type, RICO.UnitOfMeasurement))
        g.add((um, RDFS.label, Literal(ext["unidad"], lang="es")))
        g.add((ex, DCTERMS.source, Literal(ext["fuente"], lang="es")))
        g.add((ex, RDFS.comment, Literal(ext["nota"], lang="es")))
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
        g.add((ai, CRM.P2_has_type, FZA[fuerza_de(p.tipo_actuacion)]))
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
# Revisión I3: la mención NO se tipa como crm:E21_Person/E53/E74 (eso afirmaría que la persona existe; cf.
# «no hay tal hombre en el pueblo de Tinta»). Solo es observación PiCo/ROAR; su tipo de entidad va en P2_has_type.
# (Por rango de P14/P140, un razonador RDFS la inferirá E39_Actor/E1: «actor tal como lo presenta la fuente».)
CLASES_MENCION = {
    "persona": (PICOM.PersonObservation,),
    "lugar": (ROAR.LocationObservation,),
    "grupo": (ROAR.Observation,),
    "cosa": (ROAR.Observation,),
}


def capa_texto(ds: Dataset, menciones: dict[str, Mencion], lote: str) -> Graph:
    g = ds.graph(grafo_iri("texto", lote))
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
    g = ds.graph(grafo_iri("afirmaciones", lote))
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
        g.add((ai, CRM.P2_has_type, FZA[fuerza_de(tipo_act)]))
        if a.rol_en_hecho:
            g.add((ai, CRM.P2_has_type, ROL[a.rol_en_hecho]))
        if a.sujeto.eliptico:
            g.add((ai, CRM.P2_has_type, ANOT["sujeto-eliptico"]))
        if a.afirmante_de_otra_pieza:
            g.add((ai, CRM.P2_has_type, ANOT["afirmante-de-otra-pieza"]))
        if a.distribuida:
            g.add((ai, CRM.P2_has_type, ANOT["afirmacion-distribuida"]))
        if a.responde_a:            # corrige/niega/matiza otra afirmación (revisión I1)
            g.add((ai, CRM.P17_was_motivated_by, afirmacion_iri(a.responde_a)))
            g.add((ai, CRM.P2_has_type, ANOT["responde-a"]))
        if a.segun:                 # discurso referido (revisión C3)
            g.add((ai, CRM.P17_was_motivated_by, mencion_iri(a.segun)))
            g.add((ai, CRM.P2_has_type, ANOT["segun-otro"]))
        if a.nota:
            g.add((ai, CRM.P3_has_note, Literal(a.nota, lang="es")))
        # valor
        v = a.valor
        if v.concepto:
            g.add((ai, CRM.P141_assigned, concepto_iri(v.concepto, a.atributo)))
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
        # Hecho narrado: contenido proposicional de su pieza, NO un evento que ocurrió (revisión, menor):
        # crm:E89_Propositional_Object documentado por la pieza (P70). El evento ocurrido es capa 4 (E5).
        for h in filter(None, [a.sujeto.hecho, v.hecho]):
            hi = hecho_iri(h)
            g.add((hi, RDF.type, CRM.E89_Propositional_Object))
            g.add((hi, RDFS.label, Literal(h)))
            g.add((pieza_iri(a.pieza), CRM.P70_documents, hi))
        _ancla(g, ai, a.id, a.tramo, a.cita, OA.describing)
    return g


# ───────────────────────── capa 4 ─────────────────────────
CLASES_RECONSTRUCCION = {
    "persona": (PICOM.PersonReconstruction, CRM.E21_Person),
    "lugar": (ROAR.LocationReconstruction, CRM.E53_Place),
    "grupo": (ROAR.Reconstruction, CRM.E74_Group),
    "cosa": (ROAR.Reconstruction, CRM.E70_Thing),
}


_IRI_DE = {"mencion": mencion_iri, "hecho": hecho_iri, "afirmacion": afirmacion_iri}


def resolver_ref(ref: str, lotes: dict[str, Lote], *clases: str) -> URIRef:
    """IRI de una referencia calificada de la capa 4 («cc-14-18:M-UT01-003»), tras comprobar que el expediente
    está cargado y que el registro existe en él. Sin calificar, mal formada o inexistente: ValueError."""
    exp, local, clase = separar_ref(ref, *clases)
    lote = lotes.get(exp)
    if lote is None:
        raise ValueError(f"referencia {ref!r}: el expediente {exp!r} no está cargado (cargados: {sorted(lotes)})")
    existentes = {"mencion": lote.menciones, "afirmacion": lote.afirmaciones, "hecho": lote.hechos()}[clase]
    if local not in existentes:
        raise ValueError(f"referencia {ref!r}: no existe {clase} {local} en el expediente {exp}")
    return _IRI_DE[clase](local, exp)


def _clase_mencion(ref: str, lotes: dict[str, Lote]) -> str:
    resolver_ref(ref, lotes, "mencion")
    exp, local, _ = separar_ref(ref, "mencion")
    return lotes[exp].menciones[local].clase


def nodo_reconstruccion(r: Reconstruccion, lotes: dict[str, Lote]) -> URIRef:
    """La reconstrucción no pertenece a ningún expediente: su IRI no lleva ninguno."""
    slug = r.id[2:]
    if r.tipo == "identidad":
        return ID[f"{_clase_mencion(r.menciones[0], lotes)}/{slug}"]
    if r.tipo == "hecho":
        return ID[f"evento/{slug}"]
    return ID[f"ejercicio-cargo/{slug}"]


def _argumentacion(ds: Dataset, rid: str, autor: str, fecha: str, argumento: str, creencia: str,
                   premisas: list[URIRef], gi: URIRef) -> URIRef:
    """CRMinf en un grafo PROPIO (revisión I4): la creencia del investigador sobre el grafo gi (I4) no forma
    parte de la proposición que evalúa. Devuelve la IRI de la inferencia (también prov:Activity, como en PiCo)."""
    ga = ds.graph(G[f"argumentacion/{rid}"])
    inf, cre = ID[f"inferencia/{rid}"], ID[f"creencia/{rid}"]
    ga.add((inf, RDF.type, CRMINF.I5_Inference_Making))
    ga.add((inf, RDF.type, PROV.Activity))
    ga.add((inf, CRM.P14_carried_out_by, ID[f"agente/{autor}"]))
    ga.add((inf, PROV.wasAssociatedWith, ID[f"agente/{autor}"]))
    ga.add((inf, CRM.P3_has_note, Literal(argumento, lang="es")))
    for p in premisas:   # premisas: afirmaciones de capa 3 (E13 ⊑ crminf:I1_Argumentation en CRMinf 1.2.1)
        ga.add((inf, CRM.P17_was_motivated_by, p))
    ga.add((inf, CRMINF.J2_concluded_that, cre))
    ga.add((cre, RDF.type, CRMINF.I2_Belief))
    ga.add((cre, CRMINF.J4_that, gi))
    ga.add((gi, RDF.type, CRMINF.I4_Proposition_Set))
    ga.add((cre, CRMINF.J5_holds_to_be, Literal(creencia)))
    ts = URIRef(f"{inf}/tiempo")
    ga.add((inf, CRM["P4_has_time-span"], ts))
    ga.add((ts, RDF.type, CRM["E52_Time-Span"]))
    ga.add((ts, CRM.P82a_begin_of_the_begin, Literal(fecha, datatype=XSD.date)))
    ga.add((ts, CRM.P82b_end_of_the_end, Literal(fecha, datatype=XSD.date)))
    pg = ds.graph(G.procedencia)
    for gx, capa in ((gi, "reconstruccion"), (ga.identifier, "argumentacion")):
        pg.add((gx, RDF.type, PROV.Entity))
        pg.add((gx, PROV.wasAttributedTo, ID[f"agente/{autor}"]))
        pg.add((gx, PROV.generatedAtTime, Literal(fecha, datatype=XSD.date)))
        pg.add((gx, DCTERMS.type, ID[f"capa/{capa}"]))
    _agente(pg, autor)
    return inf


def _fecha_iso(x: str) -> tuple[Literal, Literal]:
    """'1806' / '1806-08' / '1806-08-21' -> (inicio, fin) xsd:date del intervalo."""
    import calendar
    partes = [int(v) for v in x.split("-")]
    a, m, d = (partes + [None, None])[:3]
    ini = f"{a:04d}-{(m or 1):02d}-{(d or 1):02d}"
    if d:
        fin = ini
    elif m:
        fin = f"{a:04d}-{m:02d}-{calendar.monthrange(a, m)[1]:02d}"
    else:
        fin = f"{a:04d}-12-31"
    return Literal(ini, datatype=XSD.date), Literal(fin, datatype=XSD.date)


def capa_reconstruccion(ds: Dataset, recs: list[Reconstruccion], lotes: dict[str, Lote]) -> None:
    """Capa 4, común al corpus. `lotes` son TODOS los lotes cargados (expediente → Lote): cada referencia va
    calificada con su expediente y se comprueba que existe; una reconstrucción puede mezclar expedientes."""
    por_id = {r.id: r for r in recs}
    if len(por_id) != len(recs):
        raise ValueError("reconstrucciones con id repetido")
    for r in recs:
        try:
            _reconstruccion(ds, r, por_id, lotes)
        except ValueError as e:
            if str(e).startswith(r.id):
                raise
            raise ValueError(f"{r.id}: {e}") from None


def _reconstruccion(ds: Dataset, r: Reconstruccion, por_id: dict[str, Reconstruccion], lotes: dict[str, Lote]) -> None:
    gi = G[f"reconstruccion/{r.id}"]
    g = ds.graph(gi)
    nodo = nodo_reconstruccion(r, lotes)
    premisas = [resolver_ref(p, lotes, "afirmacion") for p in r.premisas]
    inf = _argumentacion(ds, r.id, r.autor, r.fecha, r.argumento, r.creencia, premisas, gi)
    g.add((nodo, RDFS.label, Literal(r.etiqueta, lang="es")))
    if r.tipo == "identidad":
        clases = {_clase_mencion(m, lotes) for m in r.menciones}
        if len(clases) != 1:
            raise ValueError(f"{r.id}: menciones de clases distintas {clases}")
        for t in CLASES_RECONSTRUCCION[clases.pop()]:
            g.add((nodo, RDF.type, t))
        for m in r.menciones:
            g.add((nodo, PROV.wasDerivedFrom, resolver_ref(m, lotes, "mencion")))
        g.add((nodo, PROV.wasGeneratedBy, inf))       # patrón PiCo: la reconstrucción la genera una actividad
    elif r.tipo == "hecho":
        g.add((nodo, RDF.type, CRM.E5_Event))
        for h in r.menciones:  # aquí 'menciones' lleva ids de hechos narrados (E89)
            g.add((nodo, PROV.wasDerivedFrom, resolver_ref(h, lotes, "hecho")))
        g.add((nodo, PROV.wasGeneratedBy, inf))
    else:  # cargo: ejercicio de un cargo con vigencia (revisión C1)
        tit = por_id.get(r.titular)
        if tit is None or tit.tipo != "identidad":
            raise ValueError(f"{r.id}: titular {r.titular} no es una reconstrucción de identidad")
        persona = nodo_reconstruccion(tit, lotes)
        cargo = CARGO[r.cargo]
        g.add((nodo, RDF.type, CRM.E7_Activity))
        g.add((nodo, CRM.P2_has_type, cargo))
        _participa_cargo(g, nodo, persona, cargo)
        for p in premisas:
            g.add((nodo, PROV.wasDerivedFrom, p))
        g.add((nodo, PROV.wasGeneratedBy, inf))
        if r.ambito:
            if r.ambito not in por_id:
                raise ValueError(f"{r.id}: ámbito {r.ambito} no es una reconstrucción conocida")
            amb = nodo_reconstruccion(por_id[r.ambito], lotes)
            g.add((nodo, CRM.P7_took_place_at, amb))
        if r.ambito_literal:
            g.add((nodo, CRM.P3_has_note, Literal(f"Ámbito (literal): {r.ambito_literal}", lang="es")))
        ts = URIRef(f"{nodo}/vigencia")
        g.add((nodo, CRM["P4_has_time-span"], ts))
        g.add((ts, RDF.type, CRM["E52_Time-Span"]))
        if r.inicio:
            g.add((ts, CRM.P82a_begin_of_the_begin, _fecha_iso(r.inicio)[0]))
        if r.fin:
            g.add((ts, CRM.P82b_end_of_the_end, _fecha_iso(r.fin)[1]))
        if r.vigencia_literal:
            g.add((ts, CRM.P3_has_note, Literal(r.vigencia_literal, lang="es")))
    if r.externo or r.identificador_externo:
        ide = URIRef(f"{nodo}/identificador-externo")
        g.add((nodo, CRM.P48_has_preferred_identifier, ide))
        g.add((ide, RDF.type, CRM.E42_Identifier))
        g.add((ide, CRM.P190_has_symbolic_content, Literal(r.identificador_externo or r.externo)))
        if r.externo:
            g.add((nodo, RDFS.seeAlso, URIRef(r.externo)))
        if (r.identificador_externo or "").startswith("HGIS:"):
            g.add((ide, DCTERMS.source, URIRef(HGIS_DATASET)))
    for k, otra in enumerate(r.ver_tambien, 1):
        ide = URIRef(f"{nodo}/identificador-externo/{k}")
        g.add((nodo, CRM.P1_is_identified_by, ide))
        g.add((ide, RDF.type, CRM.E42_Identifier))
        g.add((ide, CRM.P190_has_symbolic_content, Literal(otra)))
        g.add((nodo, RDFS.seeAlso, URIRef(otra)))


def _participa_cargo(g: Graph, actividad: URIRef, persona: URIRef, cargo: URIRef) -> None:
    """El cargo es el rol (P14.1, rango E55) con que la persona lleva a cabo la actividad de ejercerlo."""
    pc = URIRef(f"{actividad}/titular")
    g.add((pc, RDF.type, CRM.PC14_carried_out_by))
    g.add((pc, CRM.P01_has_domain, actividad))
    g.add((pc, CRM.P02_has_range, persona))
    g.add((pc, CRM["P14.1_in_the_role_of"], cargo))
    g.add((actividad, CRM.P14_carried_out_by, persona))


ARGUMENTO_FECHAS = ("Lectura literal de cada fecha escrita al calendario gregoriano, sin corregir las fechas de "
                    "secuencia imposible; el control de secuencia las señala.")


def capa_fechas(ds: Dataset, ruta: Path, autor: str, fecha: str, argumento: str | None = None) -> None:
    """Capa 4: lectura normalizada de las fechas escritas del expediente EN CURSO (una reconstrucción más, con
    autor y creencia, propia de ese expediente: R-fechas-normalizadas-<exp>). La fecha escrita (capa 1) no se
    toca; aquí se añade un segundo E52 con P82a/P82b."""
    import csv
    rid = f"R-fechas-normalizadas-{exp_id()}"
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
    _argumentacion(ds, rid, autor, fecha, argumento or ARGUMENTO_FECHAS, "probable", [], gi)


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
    """Procedencia de grafos del expediente EN CURSO: la actividad lleva el expediente en su IRI (dos expedientes
    pueden llamar igual a su lote sin que sus actividades se confundan)."""
    pg = ds.graph(G.procedencia)
    trans = transcripcion_iri()
    pg.add((trans, RDF.type, PROV.Entity))
    pg.add((trans, DCTERMS.identifier, Literal("sha256:" + fuente.sha256())))
    act = ID[f"actividad/{exp_id()}/{pr.lote}"]
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
        val = ID[f"actividad/{exp_id()}/validacion-{pr.lote}"]
        vag = _agente(pg, pr.validado_por, "Person")
        pg.add((val, RDF.type, PROV.Activity))
        pg.add((val, PROV.wasAssociatedWith, vag))
        for gi, _ in grafos:
            pg.add((val, PROV.used, gi))


# ───────────────────────── capa C (catálogo) ─────────────────────────
CATALOGO_SHA256 = "752e0d2d3d9ed35f9296e5c9999a988d5c53a1aa31e175693651f4c5beacd955"  # sha256 del PDF del catálogo (archivos/)


def _sig(signatura: str) -> str:
    """«CCc 14 (18)» → «ccc-14-18» (tramo de IRI)."""
    return re.sub(r"[^a-z0-9]+", "-", signatura.lower()).strip("-")


def capa_catalogo(ds: Dataset, ruta: Path, agente: str, fecha: str,
                  signaturas: dict[str, URIRef] | None = None) -> Graph:
    """Fichas e índices del catálogo del ARC (Tomo I) como descripciones archivísticas de terceros.

    Cada ficha o entrada de índice es un rico:RecordPart del catálogo (la descripción, no el expediente) con su texto literal en rico:scopeAndContent y
    rico:describesOrDescribed hacia el expediente descrito; lo que la ficha dice es afirmación de los catalogadores,
    nunca un hecho del modelo. La pertinencia para PC03/PC04 es una nota del extractor (prov:Entity que referencia la ficha), con
    su motivo y sus dudas; no se infiere nada más del texto de la ficha.

    `signaturas` (signatura del catálogo → IRI del expediente, de los manifiestos: «signatura_catalogo») dice qué
    fichas describen un expediente del corpus: esa ficha apunta a la IRI del expediente, no a un nodo del catálogo.
    """
    signaturas = signaturas or {}
    g = ds.graph(G.catalogo)
    cat = ID["arc/catalogo/intendencia-tomo-1"]
    g.add((cat, RDF.type, RICO.Record))
    g.add((cat, RICO.title, Literal("Catálogo del Fondo Intendencia, Tomo I: Causas Ordinarias y Causas Criminales "
                                    "(Archivo Regional del Cusco)", lang="es")))
    act = ID["actividad/extraccion-catalogo-v1"]
    notas = []
    for n, linea in enumerate(ruta.read_text(encoding="utf-8").splitlines(), 1):
        if not linea.strip():
            continue
        r = json.loads(linea)
        if r["tipo"] == "ficha":
            sig = r["signatura_indice"]
            nodo = ID[f"arc/catalogo/ficha/{_sig(sig)}"]
            g.add((nodo, RDFS.label, Literal(f"Ficha del catálogo {sig}")))
            exp = signaturas.get(sig) or ID[f"arc/catalogo/expediente/{_sig(sig)}"]
            g.add((nodo, RICO.describesOrDescribed, exp))
            if sig not in signaturas:
                g.add((exp, RDF.type, RICO.RecordSet))
                g.add((exp, RDFS.label, Literal(f"{r['seccion']}, serie {r['serie']}, legajo {r['legajo']}, "
                                                f"expediente {r['expediente']} ({sig})")))
                g.add((exp, RICO.identifier, Literal(sig)))
        else:
            nodo = ID[f"arc/catalogo/indice/{n}"]
            g.add((nodo, RDFS.label, Literal(f"{r['indice']}: entrada")))
        g.add((nodo, RDF.type, RICO.RecordPart))
        g.add((nodo, RICO.isOrWasConstituentOf, cat))
        g.add((nodo, RICO.scopeAndContent, Literal(r["texto_literal"])))
        impresas = ", ".join(map(str, r.get("paginas_impresas") or []))
        pdf = ", ".join(map(str, r.get("paginas_pdf") or [r["pagina_pdf"]]))
        g.add((nodo, RDFS.comment, Literal(f"pp. impresas {impresas}; pp. del PDF {pdf}")))
        an = URIRef(f"{nodo}/pertinencia")
        g.add((an, RDF.type, PROV.Entity))
        g.add((an, DCTERMS.references, nodo))
        for pc in r["pc"]:
            g.add((an, DCTERMS.subject, Literal(pc)))
        if r.get("motivo"):
            g.add((an, DCTERMS.description, Literal(r["motivo"])))
        if r.get("tinta_pueblo_explicito"):
            g.add((an, RDFS.comment, Literal("Tinta: la ficha nombra el pueblo")))
        if r.get("pc04_certeza"):
            g.add((an, RDFS.comment, Literal(f"certeza PC04: {r['pc04_certeza']}")))
        if r.get("dudas"):
            g.add((an, SKOS.editorialNote, Literal(r["dudas"])))
        notas.append(an)
    pg = ds.graph(G.procedencia)
    fuente_cat = ID["fuente/catalogo-intendencia-tomo-1-pdf"]
    pg.add((fuente_cat, RDF.type, PROV.Entity))
    pg.add((fuente_cat, DCTERMS.identifier, Literal("sha256:" + CATALOGO_SHA256)))
    ag = _agente(pg, agente)
    pg.add((act, RDF.type, PROV.Activity))
    pg.add((act, PROV.used, fuente_cat))
    pg.add((act, PROV.wasAssociatedWith, ag))
    pg.add((act, PROV.endedAtTime, Literal(fecha, datatype=XSD.dateTime)))
    pg.add((g.identifier, RDF.type, PROV.Entity))
    pg.add((g.identifier, PROV.wasGeneratedBy, act))
    pg.add((g.identifier, PROV.wasAttributedTo, ag))
    pg.add((g.identifier, PROV.wasDerivedFrom, fuente_cat))
    pg.add((g.identifier, DCTERMS.type, ID["capa/catalogo"]))
    for an in notas:                       # PROV solo en el grafo de procedencia (tests/test_capas.py)
        pg.add((an, PROV.wasGeneratedBy, act))
    return g


# ───────────────────────── orquestación ─────────────────────────
def nuevo_dataset() -> Dataset:
    ds = Dataset()
    _ns(ds)
    return ds


def capas_expediente(ds: Dataset, lote_reg: Lote, pr: Procedencia, fechas: Path | None = None,
                     argumento_fechas: str | None = None) -> None:
    """Capas 1–3 del expediente EN CURSO (fuente.usando_expediente), su procedencia y sus fechas normalizadas."""
    if lote_reg.errores:
        raise ValueError(f"lote de {exp_id()} con errores; no se mapea:\n" + "\n".join(lote_reg.errores))
    gdoc = capa_documento(ds, lote_reg.piezas)
    gtex = capa_texto(ds, lote_reg.menciones, pr.lote)
    gafi = capa_afirmaciones(ds, lote_reg, pr.lote)
    procedencia(ds, Procedencia(lote="curacion-piezas-v1", agente=pr.agente, tipo_agente=pr.tipo_agente,
                                plan="curacion-manual-piezas", fecha=pr.fecha),
                [(gdoc.identifier, "documento")])
    procedencia(ds, pr, [(gtex.identifier, "texto"), (gafi.identifier, "afirmaciones")])
    if fechas is not None:
        capa_fechas(ds, fechas, pr.agente, pr.fecha[:10], argumento_fechas)


def construir(lote_reg: Lote, pr: Procedencia, reconstrucciones: list[Reconstruccion] = (),
              fechas: Path | None = None) -> Dataset:
    """Dataset de UN solo expediente (el que está en curso) con las reconstrucciones dadas. El corpus entero
    (todos los expedientes más las capas comunes) lo construye laad.corpus.construir."""
    ds = nuevo_dataset()
    capas_expediente(ds, lote_reg, pr, fechas)
    capa_reconstruccion(ds, list(reconstrucciones), {exp_id(): lote_reg})
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
