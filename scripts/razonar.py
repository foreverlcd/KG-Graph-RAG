"""Comprueba la consistencia del grafo con un razonador OWL 2 RL (owlrl).

Carga la unión de datos/grafo/hilo_central.trig + tesauro + todos los estándares de vendor/, calcula el
cierre OWL RL y extrae los mensajes de inconsistencia que owlrl añade como tripletas
<http://www.daml.org/2002/03/agents/agent-ont#error>. Escribe datos/grafo/razonador.txt.
Uso: python scripts/razonar.py [ruta.trig]
"""
import sys, time, pathlib
import rdflib, owlrl
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from laad import validacion

ERROR = rdflib.URIRef("http://www.daml.org/2002/03/agents/agent-ont#error")
trig = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ / "datos/grafo/hilo_central.trig"
t0 = time.time()
ds = rdflib.Dataset(); ds.parse(trig, format="trig")
g = rdflib.Graph()
for ctx in ds.graphs():
    for t in ctx: g.add(t)
n_datos = len(g)
for t in validacion.grafo_perfil(): g.add(t)
for t in validacion.grafo_estandares(): g.add(t)
n_total = len(g)
owlrl.DeductiveClosure(owlrl.OWLRL_Semantics, axiomatic_triples=False, datatype_axioms=False).expand(g)
errores = sorted(str(o) for o in g.objects(None, ERROR))
nothing = sorted(str(s) for s in g.subjects(rdflib.RDF.type, rdflib.OWL.Nothing))
# Defecto D1 (ROAR): rdfs:domain roar:Reconstruction sobre prov:wasDerivedFrom tipifica como reconstrucción
# todo lo que derive de algo (incluidas las observaciones PiCo vía prov:hadPrimarySource). No es inconsistente
# para PiCo, pero es una inferencia espuria: se cuenta y se informa, no se oculta.
ROAR = rdflib.Namespace("https://w3id.org/roar#"); PICOM = rdflib.Namespace("https://personsincontext.org/model#")
espurias = sorted(str(s) for s in g.subjects(rdflib.RDF.type, PICOM.PersonObservation)
                  if (s, rdflib.RDF.type, ROAR.Reconstruction) in g)
informe = [f"datos: {n_datos} tripletas; con estándares y perfil: {n_total}; tras cierre OWL RL: {len(g)}",
           f"tiempo: {time.time() - t0:.0f} s",
           f"inconsistencias (agent-ont#error): {len(errores)}",
           *[f"  - {e}" for e in errores],
           f"individuos de owl:Nothing: {len(nothing)}", *[f"  - {x}" for x in nothing],
           f"inferencias espurias por el defecto D1 de ROAR (PersonObservation inferida roar:Reconstruction): {len(espurias)}"]
(RAIZ / "datos/grafo/razonador.txt").write_text("\n".join(informe) + "\n", encoding="utf-8")
print("\n".join(informe[:40]))
sys.exit(1 if errores or nothing else 0)
