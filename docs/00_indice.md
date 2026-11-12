# Índice de la documentación

> Documentación técnica completa del rediseño. Es la base del futuro artículo, pero **no es el artículo**.
> Fecha de esta versión: 2026-11-12.

| Documento | Responde a | Contenido |
|---|---|---|
| `01_materiales.md` | Materiales y reglas | Inventario y orden de autoridad, unidades de transcripción y tramos, contradicciones de los materiales (F1–F7, N1–N10, H1–H7, K1–K5) y resoluciones silenciosas del modernizado |
| `A_diagnostico.md` | **A** | Por qué fallan los intentos previos, con evidencia; matriz fallo → decisión → control. El intento 2 no se aportó |
| `B_preguntas_competencia.md` | **B** | Las 20 PC (6 de disputa o silencio), respuestas provisionales del modelador e hipótesis sobre las líneas base |
| `B_respuestas_referencia.csv` | B | Plantilla para que el historiador fije sus respuestas antes de ver el grafo |
| `C_modelo.md` | **C** | Las cuatro capas, el tesauro, las formas SHACL, el análisis de carencias (OHAC vacío), los defectos de los estándares (D1–D5), los límites (L1–L10), RDF frente a grafo de propiedades y la respuesta a la revisión independiente |
| `C_correspondencias.md` | C | Tabla de correspondencias necesidad → término → estándar → alternativa descartada |
| `C_trazabilidad.md` | B + C | PC → capas → términos → consulta → prueba |
| `D_extraccion_consulta.md` | **D** | Esquema plano y cerrado, justificación con la literatura, especificación de la extracción con LLM (sin conexión aún), consulta con nombre y composición de respuestas |
| `E_prueba_hilo_central.md` | **E** | Certificaciones de agosto frente a declaraciones de septiembre e imputación sobre Túpac Amaru: cita → registro → tripletas → consulta → respuesta |
| `F_precedentes.md` | **F** | Ocho precedentes: patrón copiado, enlace y lo que no sirve; estado del contraste con fuentes independientes |
| `G_evaluacion.md` | Criterios | Umbrales, instrumentos, estado de cada criterio y protocolo del estándar de oro, del segundo expediente y de las líneas base |
| `bitacora.md` | Reproducibilidad | Incidencias, causas, correcciones y la prueba que fija cada una |
| `decisiones/README.md` | Reproducibilidad | 20 decisiones de diseño (ADR resumidos) |
| `anexos/A_evidencia_intento_previo.md` | A | Auditoría con archivo:línea |
| `anexos/C_terminos_verificados.md` | C | Términos verificados en los archivos de especificación, con nota de alcance |
| `anexos/F_informe_precedentes_y_literatura.md` | D, F | Fichas completas de precedentes y literatura, y punteros a fuentes de contraste |
| `anexos/respuestas_pc.md` | B, E | Respuestas generadas por el grafo a las 20 PC (no editar a mano) |

## Cómo reproducir

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
scripts/fetch_vendor.sh --check            # especificaciones con sha256 (o sin --check para descargarlas)
.venv/bin/python datos/registros/hilo_central.py   # registros planos del hilo central
.venv/bin/python scripts/construir.py      # TriG + SHACL
.venv/bin/python scripts/razonar.py        # OWL RL (≈ 80 s)
.venv/bin/python scripts/verificar_citas.py datos/registros/hilo_central.jsonl
.venv/bin/python scripts/responder_pc.py   # docs/anexos/respuestas_pc.md
.venv/bin/pytest -q                        # 205 pruebas
```
