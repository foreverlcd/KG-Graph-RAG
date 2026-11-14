"""Construye el grafo del corpus (todos los expedientes con manifiesto), lo serializa y lo valida (SHACL).

Escribe en datos/grafo/ un par <exp>.trig + <exp>.nq por expediente (sus capas 1–3) y comun.trig + comun.nq (capa 4,
argumentación, procedencia y catálogo). Los .nq, ordenados, son la forma canónica para git.
Uso: python scripts/construir.py [--sin-ontologias] [expediente ...]
"""
import sys, pathlib
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from laad import corpus, mapeo, validacion

exps = [a for a in sys.argv[1:] if not a.startswith("--")] or None
ds = corpus.construir(exps)
for ruta in corpus.escribir(ds):
    parte = mapeo.nuevo_dataset(); parte.parse(ruta, format="trig")
    print(f"escrito {ruta} ({sum(len(g) for g in parte.graphs())} tripletas en "
          f"{sum(1 for g in parte.graphs() if len(g))} grafos)")
print(f"corpus: {', '.join(exps or corpus.expedientes())}; {sum(len(g) for g in ds.graphs())} tripletas")
conforma, _, texto = validacion.shacl(mapeo.union(ds), con_ontologias="--sin-ontologias" not in sys.argv)
print("SHACL conforma:", conforma)
if not conforma:
    print(texto[:6000])
    sys.exit(1)
