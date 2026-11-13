"""Construye el grafo del expediente CC 14-18, lo serializa en TriG y lo valida (SHACL).

Uso: python scripts/construir.py [--sin-ontologias]
"""
import sys, pathlib
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from laad import mapeo, validacion

from laad.hilo import construir
ds = construir()
out = RAIZ / "datos/grafo/cc-14-18.trig"
out.parent.mkdir(exist_ok=True)
ds.serialize(out, format="trig")
# Forma canónica para git: N-Quads ordenado (el orden de TriG de rdflib no es estable entre ejecuciones;
# los grafos son isomorfos, ver tests/test_mapeo.py).
nq = sorted(l for l in ds.serialize(format="nquads").splitlines() if l.strip())
(out.with_suffix(".nq")).write_text("\n".join(nq) + "\n", encoding="utf-8")
print(f"escrito {out} ({sum(len(g) for g in ds.graphs())} tripletas en {len(list(ds.graphs()))} grafos)")
conforma, _, texto = validacion.shacl(mapeo.union(ds), con_ontologias="--sin-ontologias" not in sys.argv)
print("SHACL conforma:", conforma)
if not conforma:
    print(texto[:6000])
    sys.exit(1)
