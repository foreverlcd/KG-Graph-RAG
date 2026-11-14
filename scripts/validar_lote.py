"""Valida registros nuevos de un expediente JUNTO con los que ya tiene, sin escribir el grafo del repositorio.

Carga los registros que lista el manifiesto del expediente + los .jsonl dados, comprueba esquema e integridad
referencial, mapea a RDF todo el corpus (lo que verifica que toda cita es subcadena literal anclable en su tramo y
que las reconstrucciones siguen resolviendo sus referencias) y valida SHACL.
Uso: python scripts/validar_lote.py <expediente> datos/<expediente>/otro.jsonl [...]
"""
import sys, pathlib
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from laad import corpus, mapeo, validacion

if len(sys.argv) < 2 or sys.argv[1] not in corpus.expedientes():
    print(f"Uso: python scripts/validar_lote.py <expediente> [registros.jsonl ...]\n"
          f"expedientes con manifiesto: {', '.join(corpus.expedientes())}")
    sys.exit(2)
exp = sys.argv[1]
extra = [pathlib.Path(p).resolve() for p in sys.argv[2:]]
rutas = [r for r in corpus.rutas_registros(exp) if r.exists() and r not in extra] + extra
lote = corpus.cargar(exp, rutas)
if lote.errores:
    print("ERRORES DE REGISTRO:\n" + "\n".join(lote.errores[:80]))
    sys.exit(1)
print(f"{exp}: {len(lote.menciones)} menciones, {len(lote.afirmaciones)} afirmaciones")
ds = corpus.construir(lotes={exp: lote}, catalogo=None)
conforma, _, texto = validacion.shacl(mapeo.union(ds), con_ontologias=True)
print("SHACL conforma:", conforma)
if not conforma:
    print(texto[:6000])
    sys.exit(1)
