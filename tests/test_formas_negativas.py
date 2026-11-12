"""Pruebas negativas de las formas SHACL (ontologia/formas.ttl): ninguna forma aprueba en vacío.

Cada mutación introduce una violación mínima y concreta sobre nodos DISTINTOS de una copia de la unión.
Todas las mutaciones se aplican a un único grafo y se valida una sola vez (≈10 s); después cada caso
comprueba que entre los sh:ValidationResult (incluidos los anidados en sh:detail) hay uno cuyo foco es el
nodo mutado y cuya sh:sourceShape es la forma esperada o una forma/propiedad/SPARQL anidada en ella.

Forma → casos:
  PiezaForma                 pieza-sin-titulo, pieza-tipo-fuera-de-actuaciones
  ActuacionForma             actuacion-dos-fuerzas, actuacion-sin-pieza, actuacion-sin-fuerza
  FechaEscritaForma          fecha-normalizada
  ObservacionForma           mencion-sin-anotacion, mencion-sameas, mencion-derivada
  ApelacionForma             apelacion-sin-contenido
  AnotacionForma             anotacion-dos-cuerpos
  ObjetivoForma              objetivo-sin-cita, objetivo-posicion-mal-tipada
  ParticipacionForma         participacion-rol-fuera-de-roles
  AfirmacionForma            afirmacion-valor-de-verdad, afirmacion-dos-afirmantes, afirmacion-sin-polaridad,
                             afirmacion-atributo-fuera, afirmacion-sin-fundamento, afirmacion-rol-no-afirmante
  ValorLiteralForma          valor-literal-sin-contenido
  ConceptoNoInstanciadoForma concepto-como-clase
  ReconstruccionForma        reconstruccion-sin-derivacion
  InferenciaForma            inferencia-sin-nota
  CreenciaForma              creencia-sin-j5, creencia-fuera-de-lista
  LoteConProcedenciaForma    lote-reconstruccion-sin-autor, lote-actividad-sin-plan
  CargoForma                 cargo-sin-vigencia, cargo-sin-premisa            (revisión C1)
  AfirmacionForma (+)        afirmacion-eliptica-sin-nota                     (revisión I2)
  PiezaForma (+)             pieza-tipo-abstracto-sin-fuerza                  (revisión C2)
"""
from __future__ import annotations

import functools
from collections.abc import Callable
from dataclasses import dataclass

import pytest
import rdflib
from rdflib import RDF, Literal, URIRef
from rdflib.compare import to_isomorphic
from rdflib.namespace import DCTERMS, OWL, PROV, SH

from laad import mapeo as M
from laad import validacion

from ._fixtures import copia_union, union

OHAC = rdflib.Namespace("https://w3id.org/laad/ohac#")
ANIDADORES = (SH.property, SH.sparql, SH.qualifiedValueShape)


# ─────────────────────────── utilidades ───────────────────────────
def _de_tipo(g: rdflib.Graph, clase: URIRef) -> list[URIRef]:
    return sorted(s for s in g.subjects(RDF.type, clase) if isinstance(s, URIRef))


def _n(g: rdflib.Graph, clase: URIRef, i: int) -> URIRef:
    return _de_tipo(g, clase)[i]


def _quitar(g: rdflib.Graph, s, p, filtro: Callable[[rdflib.term.Node], bool] = lambda o: True) -> None:
    objs = [o for o in g.objects(s, p) if filtro(o)]
    assert objs, f"nada que quitar en {s} {p}"
    for o in objs:
        g.remove((s, p, o))


def _en(esquema: str) -> Callable[[rdflib.term.Node], bool]:
    return lambda o: str(o).startswith(f"https://w3id.org/laad/tesauro/{esquema}/")


@functools.lru_cache(maxsize=1)
def _formas() -> rdflib.Graph:
    return rdflib.Graph().parse(validacion.ONT / "formas.ttl")


def _formas_con_nombre() -> list[URIRef]:
    return sorted(s for s in _formas().subjects(RDF.type, SH.NodeShape) if isinstance(s, URIRef))


def _ancestros(forma: rdflib.term.Node) -> set[rdflib.term.Node]:
    """La forma y todas las que la contienen vía sh:property / sh:sparql / sh:qualifiedValueShape."""
    f, vistos, pila = _formas(), set(), [forma]
    while pila:
        x = pila.pop()
        if x in vistos:
            continue
        vistos.add(x)
        for p in ANIDADORES:
            pila.extend(f.subjects(p, x))
    return vistos


@dataclass(frozen=True)
class Resultado:
    foco: rdflib.term.Node
    formas: frozenset
    mensaje: str


@functools.lru_cache(maxsize=1)
def _bnodes_formas() -> list[tuple[rdflib.BNode, rdflib.Graph]]:
    f = _formas()
    return [(b, to_isomorphic(f.cbd(b))) for b in set(f.subjects()) if isinstance(b, rdflib.BNode)]


def _formas_de(g_res: rdflib.Graph, fuente: rdflib.term.Node) -> set[rdflib.term.Node]:
    """Ancestros (en formas.ttl) de la sh:sourceShape de un resultado.

    validacion.shacl() lee formas.ttl por su cuenta, así que los BNode de las formas anónimas no coinciden
    con los de _formas(); pyshacl copia la descripción (CBD) de la forma al grafo de resultados y se
    identifica por isomorfismo."""
    if isinstance(fuente, URIRef):
        return _ancestros(fuente)
    cbd = to_isomorphic(g_res.cbd(fuente))
    out: set[rdflib.term.Node] = set()
    for b, iso in _bnodes_formas():
        if iso == cbd:
            out |= _ancestros(b)
    return out


def _resultados(g_res: rdflib.Graph) -> list[Resultado]:
    out = []
    for r in g_res.subjects(RDF.type, SH.ValidationResult):   # incluye los anidados en sh:detail
        out.append(Resultado(g_res.value(r, SH.focusNode),
                             frozenset(_formas_de(g_res, g_res.value(r, SH.sourceShape))),
                             " ".join(str(m) for m in g_res.objects(r, SH.resultMessage))))
    return out


# ─────────────────────────── mutaciones ───────────────────────────
@dataclass(frozen=True)
class Mutacion:
    id: str
    forma: URIRef
    aplicar: Callable[[rdflib.Graph], rdflib.term.Node]   # devuelve el foco esperado
    mensaje: str | None = None                           # subcadena del sh:resultMessage, si hace falta
    xfail: str | None = None


def m_pieza_sin_titulo(g):
    p = _n(g, M.RICO.Record, 0)
    _quitar(g, p, M.RICO.title)
    return p


def m_pieza_tipo_fuera(g):
    p = _n(g, M.RICO.Record, 1)
    _quitar(g, p, M.RICO.hasDocumentaryFormType)
    g.add((p, M.RICO.hasDocumentaryFormType, M.FZA.testimonial))
    return p


def m_actuacion_dos_fuerzas(g):
    a = _n(g, M.CRM.E65_Creation, 1)
    g.add((a, M.CRM.P2_has_type, M.FZA.resolutiva))
    g.add((a, M.CRM.P2_has_type, M.FZA.testimonial))
    return a


def m_actuacion_sin_fuerza(g):
    a = _n(g, M.CRM.E65_Creation, 2)
    _quitar(g, a, M.CRM.P2_has_type, _en("fuerza"))
    return a


def m_actuacion_sin_pieza(g):
    a = _n(g, M.CRM.E65_Creation, 3)
    _quitar(g, a, M.CRM.P94_has_created)
    return a


def m_fecha_normalizada(g):
    f = _n(g, M.RICO.Date, 0)
    g.add((f, M.RICO.normalizedDateValue, Literal("1783-01-01")))
    return f


def m_mencion_sin_anotacion(g):
    m = _n(g, M.PICOM.PersonObservation, 0)
    for an in list(g.subjects(M.OA.hasBody, m)):
        g.remove((an, M.OA.hasBody, m))
    return m


def m_mencion_sameas(g):
    a, b = _n(g, M.PICOM.PersonObservation, 1), _n(g, M.PICOM.PersonObservation, 2)
    g.add((a, OWL.sameAs, b))
    return a


def m_mencion_derivada(g):
    a, b = _n(g, M.ROAR.LocationObservation, 0), _n(g, M.PICOM.PersonObservation, 5)
    g.add((a, PROV.wasDerivedFrom, b))
    return a


def m_apelacion_sin_contenido(g):
    ap = _n(g, M.CRM.E41_Appellation, 0)
    _quitar(g, ap, M.CRM.P190_has_symbolic_content)
    return ap


def m_anotacion_dos_cuerpos(g):
    an = _n(g, M.OA.Annotation, 5)
    g.add((an, M.OA.hasBody, _n(g, M.PICOM.PersonObservation, 3)))
    return an


def m_objetivo_sin_cita(g):
    tgt = g.value(_n(g, M.OA.Annotation, 6), M.OA.hasTarget)
    _quitar(g, tgt, M.OA.hasSelector, lambda s: (s, RDF.type, M.OA.TextQuoteSelector) in g)
    return tgt


def m_objetivo_posicion_mal_tipada(g):
    tgt = g.value(_n(g, M.OA.Annotation, 7), M.OA.hasTarget)
    ps = next(s for s in g.objects(tgt, M.OA.hasSelector) if (s, RDF.type, M.OA.TextPositionSelector) in g)
    ini = g.value(ps, M.OA.start)
    g.remove((ps, M.OA.start, ini))
    g.add((ps, M.OA.start, Literal(str(ini))))     # xsd:string en vez de xsd:nonNegativeInteger
    return tgt


def m_participacion_rol_fuera(g):
    pc = _n(g, M.CRM.PC14_carried_out_by, 0)
    _quitar(g, pc, M.CRM["P14.1_in_the_role_of"])
    g.add((pc, M.CRM["P14.1_in_the_role_of"], M.ATR["fecha-del-hecho"]))
    return pc


def m_afirmacion_valor_verdad(g):
    a = _n(g, M.CRM.E13_Attribute_Assignment, 0)
    g.add((a, M.CRMINF.J5_holds_to_be, Literal("verdadero")))
    return a


def m_afirmacion_dos_afirmantes(g):
    a = _n(g, M.CRM.E13_Attribute_Assignment, 1)
    actual = g.value(a, M.CRM.P14_carried_out_by)
    otra = next(m for m in _de_tipo(g, M.PICOM.PersonObservation) if m != actual)
    g.add((a, M.CRM.P14_carried_out_by, otra))
    return a


def m_afirmacion_sin_polaridad(g):
    a = _n(g, M.CRM.E13_Attribute_Assignment, 2)
    _quitar(g, a, M.CRM.P2_has_type, _en("polaridad"))
    return a


def m_afirmacion_atributo_fuera(g):
    a = _n(g, M.CRM.E13_Attribute_Assignment, 3)
    _quitar(g, a, M.CRM.P177_assigned_property_of_type)
    g.add((a, M.CRM.P177_assigned_property_of_type, M.COND.indio))
    return a


def m_afirmacion_sin_fundamento(g):
    a = _n(g, M.CRM.E13_Attribute_Assignment, 4)
    _quitar(g, a, M.CRM.P2_has_type, _en("fundamento"))
    return a


def m_afirmacion_rol_no_afirmante(g):
    a = _n(g, M.CRM.E13_Attribute_Assignment, 5)
    pc = next(g.subjects(M.CRM.P01_has_domain, a))
    _quitar(g, pc, M.CRM["P14.1_in_the_role_of"])
    g.add((pc, M.CRM["P14.1_in_the_role_of"], M.ROL.preso))   # rol válido, pero no bajo rol:afirmante
    return a


def m_valor_literal_sin_contenido(g):
    v = _n(g, M.CRM.E33_Linguistic_Object, 0)
    _quitar(g, v, M.CRM.P190_has_symbolic_content)
    return v


def m_concepto_como_clase(g):
    g.add((_n(g, M.PICOM.PersonObservation, 4), RDF.type, M.ROL.declarante))
    return M.ROL.declarante


def m_reconstruccion_sin_derivacion(g):
    r = _n(g, M.PICOM.PersonReconstruction, 0)
    _quitar(g, r, PROV.wasDerivedFrom)
    return r


def m_inferencia_sin_nota(g):
    i = _n(g, M.CRMINF.I5_Inference_Making, 1)
    _quitar(g, i, M.CRM.P3_has_note)
    return i


def m_creencia_sin_j5(g):
    c = _n(g, M.CRMINF.I2_Belief, 2)
    _quitar(g, c, M.CRMINF.J5_holds_to_be)
    return c


def m_creencia_fuera_lista(g):
    c = _n(g, M.CRMINF.I2_Belief, 3)
    _quitar(g, c, M.CRMINF.J5_holds_to_be)
    g.add((c, M.CRMINF.J5_holds_to_be, Literal("cierto")))
    return c


def m_lote_reconstruccion_sin_autor(g):
    gi = sorted(g.subjects(DCTERMS.type, M.ID["capa/reconstruccion"]))[0]
    _quitar(g, gi, PROV.wasAttributedTo)
    return gi


def m_lote_actividad_sin_plan(g):
    asoc = URIRef(f"{M.ID['actividad/anotacion-manual-hilo-central-v1']}/asociacion")
    _quitar(g, asoc, PROV.hadPlan)
    return M.G["texto/anotacion-manual-hilo-central-v1"]


MUTACIONES = [
    Mutacion("pieza-sin-titulo", OHAC.PiezaForma, m_pieza_sin_titulo),
    Mutacion("pieza-tipo-fuera-de-actuaciones", OHAC.PiezaForma, m_pieza_tipo_fuera, "tes:actuaciones"),
    Mutacion("actuacion-dos-fuerzas", OHAC.ActuacionForma, m_actuacion_dos_fuerzas, "tes:fuerzas"),
    Mutacion("actuacion-sin-pieza", OHAC.ActuacionForma, m_actuacion_sin_pieza),
    # Esta mutación descubrió que ActuacionForma aprobaba en vacío (COUNT…GROUP BY sin OPTIONAL);
    # corregido en formas.ttl con el patrón OPTIONAL + !BOUND. Ver docs/bitacora.md.
    Mutacion("actuacion-sin-fuerza", OHAC.ActuacionForma, m_actuacion_sin_fuerza, "tes:fuerzas"),
    Mutacion("fecha-normalizada", OHAC.FechaEscritaForma, m_fecha_normalizada),
    Mutacion("mencion-sin-anotacion", OHAC.ObservacionForma, m_mencion_sin_anotacion),
    Mutacion("mencion-sameas", OHAC.ObservacionForma, m_mencion_sameas),
    Mutacion("mencion-derivada", OHAC.ObservacionForma, m_mencion_derivada),
    Mutacion("apelacion-sin-contenido", OHAC.ApelacionForma, m_apelacion_sin_contenido),
    Mutacion("anotacion-dos-cuerpos", OHAC.AnotacionForma, m_anotacion_dos_cuerpos),
    Mutacion("objetivo-sin-cita", OHAC.ObjetivoForma, m_objetivo_sin_cita),
    Mutacion("objetivo-posicion-mal-tipada", OHAC.ObjetivoForma, m_objetivo_posicion_mal_tipada),
    Mutacion("participacion-rol-fuera-de-roles", OHAC.ParticipacionForma, m_participacion_rol_fuera, "tes:roles"),
    Mutacion("afirmacion-valor-de-verdad", OHAC.AfirmacionForma, m_afirmacion_valor_verdad),
    Mutacion("afirmacion-dos-afirmantes", OHAC.AfirmacionForma, m_afirmacion_dos_afirmantes),
    Mutacion("afirmacion-sin-polaridad", OHAC.AfirmacionForma, m_afirmacion_sin_polaridad, "polaridad"),
    Mutacion("afirmacion-atributo-fuera", OHAC.AfirmacionForma, m_afirmacion_atributo_fuera, "tes:atributos"),
    Mutacion("afirmacion-sin-fundamento", OHAC.AfirmacionForma, m_afirmacion_sin_fundamento, "fundamento"),
    Mutacion("afirmacion-rol-no-afirmante", OHAC.AfirmacionForma, m_afirmacion_rol_no_afirmante, "rol:afirmante"),
    Mutacion("valor-literal-sin-contenido", OHAC.ValorLiteralForma, m_valor_literal_sin_contenido),
    Mutacion("concepto-como-clase", OHAC.ConceptoNoInstanciadoForma, m_concepto_como_clase),
    Mutacion("reconstruccion-sin-derivacion", OHAC.ReconstruccionForma, m_reconstruccion_sin_derivacion),
    Mutacion("inferencia-sin-nota", OHAC.InferenciaForma, m_inferencia_sin_nota),
    Mutacion("creencia-sin-j5", OHAC.CreenciaForma, m_creencia_sin_j5),
    Mutacion("creencia-fuera-de-lista", OHAC.CreenciaForma, m_creencia_fuera_lista),
    Mutacion("lote-reconstruccion-sin-autor", OHAC.LoteConProcedenciaForma, m_lote_reconstruccion_sin_autor,
             "reconstrucción"),
    Mutacion("lote-actividad-sin-plan", OHAC.LoteConProcedenciaForma, m_lote_actividad_sin_plan, "capa 1–3"),
]


def m_cargo_sin_vigencia(g):
    c = _n(g, M.CRM.E7_Activity, 0)
    _quitar(g, c, M.CRM["P4_has_time-span"])
    return c


def m_cargo_sin_premisa(g):
    c = _n(g, M.CRM.E7_Activity, 1)
    _quitar(g, c, PROV.wasDerivedFrom)
    return c


def m_afirmacion_eliptica_sin_nota(g):
    a = M.ID["cc-14-18/afirmacion/A-UT01-002"]
    assert (a, M.CRM.P2_has_type, M.ANOT["sujeto-eliptico"]) in g
    _quitar(g, a, M.CRM.P3_has_note)
    return a


def m_pieza_tipo_abstracto(g):
    p = M.ID["cc-14-18/pieza/P13"]
    _quitar(g, p, M.RICO.hasDocumentaryFormType)
    g.add((p, M.RICO.hasDocumentaryFormType, M.ACT["de-autoridad"]))
    return p


MUTACIONES += [
    Mutacion("cargo-sin-vigencia", OHAC.CargoForma, m_cargo_sin_vigencia),
    Mutacion("cargo-sin-premisa", OHAC.CargoForma, m_cargo_sin_premisa),
    Mutacion("afirmacion-eliptica-sin-nota", OHAC.AfirmacionForma, m_afirmacion_eliptica_sin_nota, "exige nota"),
    Mutacion("pieza-tipo-abstracto-sin-fuerza", OHAC.PiezaForma, m_pieza_tipo_abstracto, "fuerza institucional"),
]


@functools.lru_cache(maxsize=1)
def _validacion_mutada():
    g = copia_union()
    focos = {m.id: m.aplicar(g) for m in MUTACIONES}
    conforma, g_res, _ = validacion.shacl(g, con_ontologias=True)
    return conforma, _resultados(g_res), focos


# ─────────────────────────── pruebas ───────────────────────────
def test_union_sin_modificar_conforma():
    conforma, _, texto = validacion.shacl(union(), con_ontologias=True)
    assert conforma, texto[:3000]


def test_toda_forma_con_nombre_tiene_caso_negativo():
    cubiertas = {m.forma for m in MUTACIONES if m.xfail is None}
    faltan = [f for f in _formas_con_nombre() if f not in cubiertas]
    assert not faltan, f"formas sin prueba negativa: {faltan}"


def test_grafo_mutado_no_conforma():
    conforma, _, _ = _validacion_mutada()
    assert not conforma


@pytest.mark.parametrize(
    "mut",
    [pytest.param(m, id=m.id, marks=[pytest.mark.xfail(reason=m.xfail, strict=True)] if m.xfail else [])
     for m in MUTACIONES])
def test_forma_detecta_violacion(mut: Mutacion):
    _, resultados, focos = _validacion_mutada()
    foco = focos[mut.id]
    del_foco = [r for r in resultados if r.foco == foco]
    ok = [r for r in del_foco if mut.forma in r.formas and (mut.mensaje is None or mut.mensaje in r.mensaje)]
    assert ok, (f"{mut.id}: ninguna violación de {mut.forma} con foco {foco}; resultados del foco: "
                f"{[(sorted(str(f) for f in r.formas if isinstance(f, URIRef)), r.mensaje[:120]) for r in del_foco]}")
