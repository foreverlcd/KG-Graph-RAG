# LAAD — Grafo de conocimiento del Fondo Intendencia (ARC), caso piloto CC L14 E18

Rediseño del modelo de datos para el expediente *Causas Criminales, Legajo 14, Expediente 18 (1806)*:
Manuel Huancachoque (y variantes) contra el cacique recaudador Andrés Chuquitapa, pueblo de Tinta.

Fuentes, en orden de autoridad (ver `docs/01_materiales.md`):
1. `corpus/Transcripcion_CC_L14E18.txt` — transcripción paleográfica, única fuente de verdad.
2. `corpus/corpus_modernizado.txt` — ayuda de lectura; nunca se cita.
3. `archivos/Catálogo Intendencia I CO y CC.pdf` — dato a contrastar.

La documentación completa está en `docs/` (índice y pasos de reproducción en `docs/00_indice.md`).

## Estructura
- `ontologia/` — perfil OHAC (sin términos propios), tesauro SKOS, formas SHACL
- `src/laad/` — fuente y citas, esquema plano, mapeo determinista, consulta y respuestas
- `consultas/` — consultas SPARQL con nombre
- `datos/` — manifiesto del expediente, piezas (capa 1), registros anotados (capas 2–3), reconstrucciones (capa 4), grafo TriG
- `vendor/` — especificaciones de los estándares (descarga reproducible con `scripts/fetch_vendor.sh`)
- `tests/` — 205 pruebas (fuente, formas negativas, términos, capas, mapeo, preguntas de competencia, segundo expediente sintético)

## Entorno
```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/pytest -q
```

El estado de cada criterio de aceptación está en `docs/G_evaluacion.md`.
