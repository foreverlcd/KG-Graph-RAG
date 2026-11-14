"""Las cifras que citan el artículo, la presentación y la documentación salen de un solo sitio y están al día."""
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def test_cifras_al_dia_con_los_datos():
    r = subprocess.run([sys.executable, str(RAIZ / "scripts/cifras.py"), "--comprobar"], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_articulo_y_presentacion_cargan_las_mismas_cifras():
    macros = set(re.findall(r"\\newcommand\{\\(cifra\w+)\}", (RAIZ / "articulo/cifras.tex").read_text(encoding="utf-8")))
    for doc in ("articulo/main.tex", "presentacion/main.tex"):
        ruta = RAIZ / doc
        if not ruta.exists():          # la presentación se añade después del artículo
            continue
        t = ruta.read_text(encoding="utf-8")
        assert "cifras.tex" in t or "{cifras}" in t, f"{doc} no carga cifras.tex"
        usadas = set(re.findall(r"\\(cifra[A-Za-z]+)", t))
        assert usadas, f"{doc} no usa ninguna cifra generada"
        assert usadas <= macros, f"{doc} usa cifras inexistentes: {sorted(usadas - macros)}"
