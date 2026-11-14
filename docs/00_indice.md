# Índice de la documentación

> Documentación técnica completa del rediseño. Es la base del futuro artículo, pero **no es el artículo**.
> Fecha de esta versión: 2026-11-14.
>
> **Regla sobre las cifras.** Los recuentos que cambian con los datos (menciones, afirmaciones, tripletas, formas,
> mutaciones, resultados del razonador…) viven solo en `cifras.md`, que genera `scripts/cifras.py`. Los demás
> documentos remiten a él o dan la cifra con su fecha; no se repiten a mano.

| Documento | Responde a | Contenido |
|---|---|---|
| `01_materiales.md` | Materiales y reglas | Inventario y orden de autoridad, unidades de transcripción y tramos, contradicciones de los materiales (F1–F7, N1–N10, H1–H7, K1–K5) y resoluciones silenciosas del modernizado |
| `A_diagnostico.md` | **A** | Por qué fallan los intentos previos, con evidencia; matriz fallo → decisión → control. El intento 2 no se aportó |
| `B_preguntas_competencia.md` | **B** | Las 20 PC (6 de disputa o silencio), respuestas provisionales del modelador e hipótesis sobre las líneas base |
| `B_respuestas_referencia.csv` | B | Plantilla para que el historiador fije sus respuestas antes de ver el grafo |
| `C_modelo.md` | **C** | Las cuatro capas, los grafos por expediente y los comunes, el tesauro y cómo crece (candidatos, dominio y rango, versión), las formas SHACL, el análisis de carencias (OHAC vacío), los defectos de los estándares (D1–D5), los límites (L1–L10), RDF frente a grafo de propiedades y la respuesta a la revisión independiente |
| `C_correspondencias.md` | C | Tabla de correspondencias necesidad → término → estándar → alternativa descartada |
| `C_trazabilidad.md` | B + C | PC → capas → términos → consulta → prueba |
| `D_extraccion_consulta.md` | **D** | Esquema plano y cerrado, justificación con la literatura, formato de transcripción configurable, especificación de la extracción con LLM (sin conexión aún), consulta con nombre sobre Oxigraph, composición de respuestas y rendimiento medido |
| `E_prueba_hilo_central.md` | **E** | Certificaciones de agosto frente a declaraciones de septiembre e imputación sobre Túpac Amaru: cita → registro → tripletas → consulta → respuesta |
| `F_precedentes.md` | **F** | Ocho precedentes: patrón copiado, enlace y lo que no sirve; estado del contraste con fuentes independientes |
| `G_evaluacion.md` | Criterios | Umbrales, instrumentos, estado de cada criterio y protocolo del estándar de oro, del segundo expediente y de las líneas base |
| `cifras.md` | Reproducibilidad | Las cifras del proyecto, generadas por `scripts/cifras.py` (no editar a mano); el artículo usa las mismas por `articulo/cifras.tex` |
| `bitacora.md` | Reproducibilidad | Incidencias, causas, correcciones y la prueba que fija cada una |
| `decisiones/README.md` | Reproducibilidad | Decisiones de diseño numeradas (ADR resumidos) |
| `../ontologia/README.md`, `../ontologia/CHANGELOG.md` | C | Política de cambios del tesauro (candidatos, retirada, versión) y registro de cambios |
| `../datos/expedientes/README.md` | D | Cómo añadir un expediente: manifiesto, clave `formato`, pasos y lo que se cura a mano |
| `../datos/grafo/escala.md` | G | Medición de escala del almacén de consulta con el expediente piloto replicado |
| `anexos/A_evidencia_intento_previo.md` | A | Auditoría con archivo:línea |
| `anexos/C_terminos_verificados.md` | C | Términos verificados en los archivos de especificación, con nota de alcance |
| `anexos/F_informe_precedentes_y_literatura.md` | D, F | Fichas completas de precedentes y literatura, y punteros a fuentes de contraste |
| `anexos/H1_alternativas_afirmaciones.md` | C | Alternativas 2026 para afirmaciones en disputa y reconstrucción (RDF 1.2, nanopublicaciones, Factoid, FactGrid, STAR, CRMinf 1.2.1); origen del defecto D6 |
| `anexos/H2_alternativas_documento_lugar.md` | C | Alternativas para documento, menciones, lugares, tiempo y SKOS; D5 matizado, identificadores de lugar |
| `anexos/H3_metodologia_y_publicacion.md` | G | Metodología citable (LOT, NeOn, ORSD), evaluación con un solo validador y sedes de publicación |
| `anexos/I_auditoria_reconstrucciones.md` | C, G | Auditoría de las reconstrucciones de la capa 4 por una segunda instancia del modelo (no es validación humana) |
| `anexos/J_skills.md` | Reproducibilidad | Búsqueda de «skills» para Claude Code útiles al proyecto (2026-11-14): candidatas y por qué no se instaló ninguna |
| `../articulo/` | — | Artículo sobre la ontología (castellano, LLNCS); pendientes en `articulo/README.md` |
| `anexos/respuestas_pc.md` | B, E | Respuestas generadas por el grafo a las 20 PC (no editar a mano) |

## Cómo reproducir

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
scripts/fetch_vendor.sh --check            # especificaciones con sha256 (o sin --check para descargarlas)
.venv/bin/python datos/registros/hilo_central.py   # registros planos del hilo central (ídem expediente_a/b/c.py)
.venv/bin/python scripts/candidatos.py     # ontologia/candidatos.ttl, sección APROBADOS y formas_atributos.ttl
.venv/bin/python scripts/construir.py      # datos/grafo/<exp>.trig/.nq + comun.trig/.nq, SHACL y avisos
.venv/bin/python scripts/razonar.py        # OWL RL (lento; resultado en datos/grafo/razonador.txt)
.venv/bin/python scripts/verificar_citas.py datos/registros/hilo_central.jsonl
.venv/bin/python scripts/responder_pc.py   # docs/anexos/respuestas_pc.md
.venv/bin/python scripts/cifras.py         # datos/cifras.json, articulo/cifras.tex y docs/cifras.md
.venv/bin/pytest -q                        # incluye tests/test_cifras.py: falla si las cifras no están al día
```

Otras órdenes:

```bash
.venv/bin/python scripts/validar_lote.py cc-14-18 nuevo.jsonl   # valida un lote sin escribir el grafo (el expediente es obligatorio)
.venv/bin/python scripts/servir.py piezas expediente=cc-14-18   # una consulta con nombre, sobre Oxigraph
.venv/bin/python scripts/nuevo_expediente.py <id> <transcripción> --solo-ver   # ver la segmentación de un expediente nuevo
LAAD_MOTOR=rdflib .venv/bin/python scripts/responder_pc.py      # motor de consulta anterior (lento)
```

Para añadir un expediente, seguir `datos/expedientes/README.md`.
