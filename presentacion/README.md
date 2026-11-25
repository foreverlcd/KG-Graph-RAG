# Presentación del perfil OHAC

Diapositivas en Beamer (tema Metropolis, 16:9). Compilar: `latexmk -pdf main.tex`. Limpiar: `latexmk -C`.

## Cómo se mantiene al día

* **Cifras.** Ninguna se escribe en `main.tex`: todas son macros `\cifra…` de `../articulo/cifras.tex`, que genera
  `scripts/cifras.py` a partir de los datos. Tras cambiar los datos o reconstruir el grafo:
  `python scripts/cifras.py && latexmk -pdf presentacion/main.tex`. La prueba `tests/test_cifras.py` falla si las
  cifras están desfasadas o si la presentación usa una macro que no existe.
* **Contenido.** Sigue las secciones del artículo (`articulo/main.tex`). Todo cambio del modelo que toque el artículo
  debe reflejarse aquí en la misma rama; una diapositiva por idea.
* **Lo que no va aquí.** Declaraciones que el artículo no sostiene, ni cifras de mediciones no versionadas.

## Presentación de estado del proyecto (`proyecto.tex`)

Repaso completo para el equipo: qué es LAAD, materiales y restricciones, cronología, modelo, construcción del grafo,
cifras con gráficos, validación, consulta y escala, el harness de consulta y sus resultados, problemas abiertos,
pendientes, uso y glosario. Las cifras generales salen de `../articulo/cifras.tex`; las distribuciones y los
resultados del harness, de `datos_proyecto.tex`, que genera `scripts/datos_presentacion.py` a partir del grafo y de
los informes de `datos/evaluacion/`:

    python scripts/cifras.py && python scripts/datos_presentacion.py && (cd presentacion && latexmk -pdf proyecto.tex)

A diferencia de `main.tex`, esta presentación recoge resultados que el artículo aún no incluye (el harness).
