"""Construye el grafo del hilo central, lo serializa en TriG y lo valida (SHACL).

Uso: python scripts/construir.py [--sin-ontologias]
"""
import sys, pathlib
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from laad import mapeo, validacion

from laad.hilo import construir
ds = construir()
out = RAIZ / "datos/grafo/hilo_central.trig"
out.parent.mkdir(exist_ok=True)
ds.serialize(out, format="trig")
print(f"escrito {out} ({sum(len(g) for g in ds.graphs())} tripletas en {len(list(ds.graphs()))} grafos)")
conforma, _, texto = validacion.shacl(mapeo.union(ds), con_ontologias="--sin-ontologias" not in sys.argv)
print("SHACL conforma:", conforma)
if not conforma:
    print(texto[:6000])
    sys.exit(1)
