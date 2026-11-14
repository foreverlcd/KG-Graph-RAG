# LAAD — Grafo de conocimiento del Fondo Intendencia (ARC), caso piloto CC L14 E18

Rediseño del modelo de datos para el expediente *Causas Criminales, Legajo 14, Expediente 18 (1806)*:
Manuel Huancachoque (y variantes) contra el cacique recaudador Andrés Chuquitapa, pueblo de Tinta.

Fuentes, en orden de autoridad (ver `docs/01_materiales.md`):
1. `corpus/Transcripcion_CC_L14E18.txt` — transcripción paleográfica, única fuente de verdad.
2. `corpus/corpus_modernizado.txt` — ayuda de lectura; nunca se cita.
3. `archivos/Catálogo Intendencia I CO y CC.pdf` — dato a contrastar.

La documentación completa está en `docs/` (índice y pasos de reproducción en `docs/00_indice.md`). Las cifras del
proyecto (menciones, afirmaciones, tripletas, formas…) están en `docs/cifras.md`, que se genera con
`scripts/cifras.py`; ningún otro documento las repite a mano.

## Estructura
- `ontologia/` — perfil OHAC (sin términos propios), tesauro SKOS versionado, conceptos candidatos, formas SHACL (incluidas las de dominio y rango por atributo); política de cambios en `ontologia/README.md`
- `src/laad/` — fuente y citas (`fuente.py`), esquema plano, mapeo determinista, corpus de expedientes (`corpus.py`), consulta sobre Oxigraph (`consulta.py`) y respuestas
- `consultas/` — consultas SPARQL con nombre
- `datos/` — un manifiesto por expediente (`datos/expedientes/<exp>.json`; guía en `datos/expedientes/README.md`), piezas (capa 1), registros anotados (capas 2–3), reconstrucciones (capa 4, comunes al corpus), candidatos del tesauro y dominio y rango de los atributos (CSV), y el grafo: `datos/grafo/<exp>.trig` por expediente más `datos/grafo/comun.trig`
- `scripts/` — construir y validar el grafo, razonar, responder las preguntas de competencia, preparar un expediente nuevo, gestionar candidatos y generar las cifras
- `articulo/` y `presentacion/` — artículo (LLNCS) y presentación (Beamer) del perfil; ambos cargan `articulo/cifras.tex` y deben actualizarse con cada cambio del modelo
- `vendor/` — especificaciones de los estándares (descarga reproducible con `scripts/fetch_vendor.sh`)
- `tests/` — pruebas de fuente y formato de transcripción, formas negativas, términos, capas, mapeo, preguntas de competencia, varios expedientes en un mismo corpus, candidatos, atributos, versión del tesauro, motores de consulta y cifras al día

## Entorno
```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/pytest -q
```

Las consultas se ejecutan en Oxigraph (`pyoxigraph`, incluido en `requirements.txt`); `LAAD_MOTOR=rdflib` usa el
motor anterior, más lento y sin dependencias compiladas.

El estado de cada criterio de aceptación está en `docs/G_evaluacion.md`.
