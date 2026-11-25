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

Repaso completo y detallado para el equipo: qué es LAAD y qué preguntas clave responde; diagnóstico del prototipo
(matriz fallo → decisión → control); principios y por qué; decisiones tecnológicas con sus alternativas descartadas
(RDF frente a Neo4j, cada estándar, informe H1, pila de software, agente propio y Gemini); la ontología capa por capa
con TriG real (la negación de Cano, las hipótesis sobre el declarante de P19); fuerza institucional, tesauro,
formas SHACL, análisis de carencias, defectos D1–D7 y límites L1–L10; construcción del grafo y por qué el modelo de
lenguaje rellena un esquema plano; cifras con gráficos y visor; validación, consulta y escala; diseño del harness y
recorrido real de la PC09; las 20 PC; resultados y coste; preguntas frecuentes respondidas; problemas, propuestas,
pendientes, uso y glosario. Las cifras generales salen de `../articulo/cifras.tex`; las distribuciones y los
resultados del harness, de `datos_proyecto.tex`, que genera `scripts/datos_presentacion.py` a partir del grafo y de
los informes de `datos/evaluacion/`:

    python scripts/cifras.py && python scripts/datos_presentacion.py && (cd presentacion && latexmk -pdf proyecto.tex)

A diferencia de `main.tex`, esta presentación recoge resultados que el artículo aún no incluye (el harness).

## Charla de avances (`avances.tex`)

Unos 10 minutos con los docentes del proyecto, centrada en la ontología OHAC, el tesauro y cómo se construye y usa el
grafo. El guion de cada diapositiva, lo que hay que saber explicar y las preguntas probables están en
`guion_charla.md`. La captura del visor (`figuras/visor.png`) se tomó de `visor/index.html`.

    python scripts/cifras.py && python scripts/datos_presentacion.py && (cd presentacion && latexmk -pdf avances.tex)
