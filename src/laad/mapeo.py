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


def iri(*partes: str) -> URIRef:
    return ID["/".join([exp_id(), *partes])]


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


def nodo_reconstruccion(r: Reconstruccion, lote_reg: Lote) -> URIRef:
    slug = r.id[2:]
    if r.tipo == "identidad":
        clase = lote_reg.menciones[r.menciones[0]].clase
        return ID[f"{clase}/{slug}"]
    if r.tipo == "hecho":
        return ID[f"evento/{slug}"]
    return ID[f"ejercicio-cargo/{slug}"]


def _argumentacion(ds: Dataset, rid: str, autor: str, fecha: str, argumento: str, creencia: str,
                   premisas: list[str], gi: URIRef) -> URIRef:
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
        ga.add((inf, CRM.P17_was_motivated_by, afirmacion_iri(p)))
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


def capa_reconstruccion(ds: Dataset, recs: list[Reconstruccion], lote_reg: Lote) -> None:
    por_id = {r.id: r for r in recs}
    for r in recs:
        gi = G[f"reconstruccion/{r.id}"]
        g = ds.graph(gi)
        nodo = nodo_reconstruccion(r, lote_reg)
        inf = _argumentacion(ds, r.id, r.autor, r.fecha, r.argumento, r.creencia, r.premisas, gi)
        g.add((nodo, RDFS.label, Literal(r.etiqueta, lang="es")))
        if r.tipo == "identidad":
            clases = {lote_reg.menciones[m].clase for m in r.menciones}
            if len(clases) != 1:
                raise ValueError(f"{r.id}: menciones de clases distintas {clases}")
            for t in CLASES_RECONSTRUCCION[clases.pop()]:
                g.add((nodo, RDF.type, t))
            for m in r.menciones:
                g.add((nodo, PROV.wasDerivedFrom, mencion_iri(m)))
            g.add((nodo, PROV.wasGeneratedBy, inf))       # patrón PiCo: la reconstrucción la genera una actividad
        elif r.tipo == "hecho":
            g.add((nodo, RDF.type, CRM.E5_Event))
            for h in r.menciones:  # aquí 'menciones' lleva ids de hechos narrados (E89)
                g.add((nodo, PROV.wasDerivedFrom, hecho_iri(h)))
            g.add((nodo, PROV.wasGeneratedBy, inf))
        else:  # cargo: ejercicio de un cargo con vigencia (revisión C1)
            tit = por_id.get(r.titular)
            if tit is None or tit.tipo != "identidad":
                raise ValueError(f"{r.id}: titular {r.titular} no es una reconstrucción de identidad")
            persona = nodo_reconstruccion(tit, lote_reg)
            cargo = CARGO[r.cargo]
            g.add((nodo, RDF.type, CRM.E7_Activity))
            g.add((nodo, CRM.P2_has_type, cargo))
            _participa_cargo(g, nodo, persona, cargo)
            for p in r.premisas:
                g.add((nodo, PROV.wasDerivedFrom, afirmacion_iri(p)))
            g.add((nodo, PROV.wasGeneratedBy, inf))
            if r.ambito:
                amb = nodo_reconstruccion(por_id[r.ambito], lote_reg)
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


def _participa_cargo(g: Graph, actividad: URIRef, persona: URIRef, cargo: URIRef) -> None:
    """El cargo es el rol (P14.1, rango E55) con que la persona lleva a cabo la actividad de ejercerlo."""
    pc = URIRef(f"{actividad}/titular")
    g.add((pc, RDF.type, CRM.PC14_carried_out_by))
    g.add((pc, CRM.P01_has_domain, actividad))
    g.add((pc, CRM.P02_has_range, persona))
    g.add((pc, CRM["P14.1_in_the_role_of"], cargo))
    g.add((actividad, CRM.P14_carried_out_by, persona))


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
    _argumentacion(ds, rid, autor, fecha,
                   "Lectura literal de cada fecha escrita al calendario gregoriano, sin corregir las fechas de "
                   "secuencia imposible (F1–F6); el control de secuencia las señala.", "probable", [], gi)


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
