"""Genera ontologia/formas_atributos.ttl: una forma SHACL por atributo con su DOMINIO Y RANGO (determinista).

Fuente: datos/atributos.csv (atributo, sujeto, valor, nota). Cada tipo de sujeto o de valor se traduce a la clase
RDF que el mapeo emite para él (src/laad/mapeo.py):
  persona → picom:PersonObservation        lugar → roar:LocationObservation      grupo, cosa → roar:Observation
  pieza → rico:Record                      hecho → crm:E89_Propositional_Object  afirmacion → crm:E13_Attribute_Assignment
  literal → crm:E33_Linguistic_Object (crm:E52_Time-Span en los atributos de tiempo)
  concepto → un concepto de los esquemas que el atributo declara con dct:conformsTo en el tesauro
Se compara el rdf:type DIRECTO del nodo (sin jerarquía de clases: E31 ⊑ E89 confundiría pieza y hecho). El grafo no
distingue grupo de cosa (ambos son roar:Observation): esa diferencia solo la comprueba laad.registros.

Todo atributo vigente de tes:atributos necesita una fila. Un atributo CANDIDATO sin fila no es un error: su forma
solo avisa (sh:Warning) de cada afirmación que lo usa.
Uso: python scripts/atributos.py
"""
from __future__ import annotations

import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
SALIDA = RAIZ / "ontologia/formas_atributos.ttl"
CSV = RAIZ / "datos/atributos.csv"
OHAC = "https://w3id.org/laad/ohac#"
TES = "https://w3id.org/laad/tesauro/"

CABECERA = """# Formas SHACL de DOMINIO Y RANGO de los atributos — GENERADO por scripts/atributos.py desde datos/atributos.csv.
# No editar a mano. Se cargan junto a ontologia/formas.ttl (laad.validacion.grafo_formas).
# Cada forma toma las afirmaciones (crm:E13) de UN atributo y exige que su sujeto (P140) y su valor (P141) tengan
# como rdf:type directo una de las clases que el mapeo emite para los tipos admitidos en el CSV.

@prefix sh:    <http://www.w3.org/ns/shacl#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos:  <http://www.w3.org/2004/02/skos/core#> .
@prefix crm:   <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix ohac:  <https://w3id.org/laad/ohac#> .
"""


class ErrorAtributos(ValueError):
    """datos/atributos.csv no cubre el tesauro o nombra algo que no existe."""


def lit(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"@es'


def clases_rdf(tipo: str, atributo: str, esquemas: tuple[str, ...] = ()) -> list[str]:
    """IRIs que identifican en el grafo un nodo del tipo dado: su rdf:type directo o, para un concepto, su esquema."""
    from laad import mapeo as M
    if tipo in M.CLASES_MENCION:
        return [str(c) for c in M.CLASES_MENCION[tipo]]
    if tipo == "pieza":
        return [str(M.RICO.Record)]
    if tipo == "hecho":
        return [str(M.CRM.E89_Propositional_Object)]
    if tipo == "afirmacion":
        return [str(M.CRM.E13_Attribute_Assignment)]
    if tipo == "literal":
        return [str(M.CRM["E52_Time-Span"] if atributo in M.ATRIBUTOS_TIEMPO else M.CRM.E33_Linguistic_Object)]
    if tipo == "concepto":
        if not esquemas:
            raise ErrorAtributos(f"{atributo}: admite «concepto» como valor pero el tesauro no le declara ningún "
                                 f"esquema (dct:conformsTo)")
        return [TES + e for e in esquemas]
    raise ErrorAtributos(f"{atributo}: tipo desconocido {tipo!r}")


def _iris(tipos, atributo: str, esquemas: tuple[str, ...]) -> list[str]:
    vistos: list[str] = []
    for t in sorted(tipos):
        for c in clases_rdf(t, atributo, esquemas):
            if c not in vistos:
                vistos.append(c)
    return sorted(vistos)


def nombre_forma(atributo: str) -> str:
    return f"{OHAC}AtributoForma-{atributo}"


def _objetivo(atributo: str) -> str:
    return ("    sh:target [ a sh:SPARQLTarget ; sh:select "
            f"\"\"\"SELECT ?this WHERE {{ ?this <http://www.cidoc-crm.org/cidoc-crm/P177_assigned_property_of_type> "
            f"<{TES}atributo/{atributo}> }}\"\"\" ] ;")


def _propiedad(camino: str, iris: list[str], mensaje: str) -> str:
    return (f"    sh:property [ sh:path {camino} ;\n"
            f"        sh:qualifiedValueShape [ sh:in ( {' '.join(f'<{i}>' for i in iris)} ) ] ; sh:qualifiedMinCount 1 ;\n"
            f"        sh:message {lit(mensaje)} ]")


def forma(atributo: str, sujeto, valor, esquemas: tuple[str, ...] = ()) -> str:
    def lista(tipos):
        return ", ".join(sorted(tipos))
    rango = lista(valor) + (f" de tes:{', tes:'.join(esquemas)}" if "concepto" in valor and esquemas else "")
    camino_valor = ("( crm:P141_assigned [ sh:alternativePath ( rdf:type skos:inScheme ) ] )" if "concepto" in valor
                    else "( crm:P141_assigned rdf:type )")
    return "\n".join([
        f"<{nombre_forma(atributo)}> a sh:NodeShape ;",
        f"    rdfs:comment {lit(f'atr:{atributo} — sujeto: {lista(sujeto)}; valor: {rango}.')} ;",
        _objetivo(atributo),
        _propiedad("( crm:P140_assigned_attribute_to rdf:type )", _iris(sujeto, atributo, esquemas),
                   f"atr:{atributo}: el sujeto de la afirmación no es de un tipo admitido ({lista(sujeto)}).") + " ;",
        _propiedad(camino_valor, _iris(valor, atributo, esquemas),
                   f"atr:{atributo}: el valor de la afirmación no es de un tipo admitido ({rango}).") + " ."])


def forma_sin_fila(atributo: str) -> str:
    return "\n".join([
        f"<{nombre_forma(atributo)}> a sh:NodeShape ; sh:severity sh:Warning ;",
        f"    rdfs:comment {lit(f'atr:{atributo} — atributo CANDIDATO sin fila en datos/atributos.csv: solo se avisa.')} ;",
        _objetivo(atributo),
        "    sh:property [ sh:path crm:P177_assigned_property_of_type ; sh:maxCount 0 ; sh:severity sh:Warning ;",
        f"        sh:message {lit(f'atr:{atributo} es un atributo candidato sin dominio ni rango declarados en datos/atributos.csv: no se comprueban su sujeto ni su valor.')} ] ."])


def generar(filas: dict, vigentes: set[str], candidatos: set[str], esquemas: dict[str, tuple[str, ...]]) -> str:
    """Texto de formas_atributos.ttl. `filas`: atributo → (sujeto, valor); `vigentes`: atributos no retirados de
    tes:atributos (incluidos los candidatos); `esquemas`: atributo → esquemas de su valor de concepto."""
    sobran = sorted(set(filas) - vigentes)
    if sobran:
        raise ErrorAtributos(f"datos/atributos.csv nombra atributos que no están vigentes en tes:atributos: {sobran}")
    faltan = sorted(vigentes - set(filas) - candidatos)
    if faltan:
        raise ErrorAtributos(f"atributos del tesauro sin fila en datos/atributos.csv: {faltan}")
    bloques = [CABECERA]
    for atr in sorted(vigentes):
        if atr in filas:
            bloques.append(forma(atr, *filas[atr], esquemas.get(atr, ())))
        else:
            bloques.append(forma_sin_fila(atr))
    return "\n\n".join(b.rstrip("\n") for b in bloques) + "\n"


def texto_actual() -> str:
    """El texto que corresponde al CSV y al vocabulario EN DISCO (tesauro + candidatos), sin cachés."""
    import rdflib
    from rdflib.namespace import DCTERMS, OWL, SKOS
    from laad import esquema
    g = esquema.grafo_tesauro()
    sch = rdflib.URIRef(TES + "atributos")
    local = lambda x: str(x).rsplit("/", 1)[1]  # noqa: E731
    vigentes = {local(c) for c in g.subjects(SKOS.inScheme, sch) if not any(bool(o) for o in g.objects(c, OWL.deprecated))}
    candidatos = {local(c) for c in g.objects(esquema.COLECCION_CANDIDATOS, SKOS.member)} & vigentes
    esquemas = {a: tuple(sorted(local(e) for e in g.objects(rdflib.URIRef(TES + "atributo/" + a), DCTERMS.conformsTo)))
                for a in vigentes}
    return generar(esquema.leer_dominio_rango(CSV), vigentes, candidatos, esquemas)


def regenerar() -> None:
    SALIDA.write_text(texto_actual(), encoding="utf-8")
    print(f"escrito {SALIDA}")


if __name__ == "__main__":
    try:
        regenerar()
    except (ErrorAtributos, ValueError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
