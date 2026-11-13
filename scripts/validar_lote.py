"""Valida registros nuevos JUNTO con los existentes, sin escribir el grafo del repositorio.

Carga datos/registros/hilo_central.jsonl + los .jsonl dados, comprueba esquema e integridad referencial,
mapea a RDF (lo que verifica que toda cita es subcadena literal anclable en su tramo) y valida SHACL.
Uso: python scripts/validar_lote.py datos/registros/otro.jsonl [...]
"""
import sys, pathlib
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from laad import mapeo, validacion
from laad.hilo import FECHAS, LOTES, PROCEDENCIA, RECONSTRUCCIONES
from laad.registros import cargar

extra = [pathlib.Path(p).resolve() for p in sys.argv[1:]]
rutas = [r for r in LOTES if r.exists() and r not in extra] + extra
lote = cargar(rutas)
if lote.errores:
    print("ERRORES DE REGISTRO:\n" + "\n".join(lote.errores[:80]))
    sys.exit(1)
print(f"registros: {len(lote.menciones)} menciones, {len(lote.afirmaciones)} afirmaciones")
ds = mapeo.construir(lote, PROCEDENCIA, mapeo.cargar_reconstrucciones(RECONSTRUCCIONES), fechas=FECHAS)
conforma, _, texto = validacion.shacl(mapeo.union(ds), con_ontologias=True)
print("SHACL conforma:", conforma)
if not conforma:
    print(texto[:6000])
    sys.exit(1)
