# G · Evaluación: criterios, umbrales y estado actual

> Cada criterio de la solicitud lleva:
> * un **umbral** propuesto, fijado **antes** de medir (2026-11-12);
> * el **instrumento** reproducible;
> * el **estado** a esta fecha: CUMPLE, NO CUMPLE, PENDIENTE (falta un insumo externo) o PARCIAL.
>
> Los umbrales que dependen de la literatura citan su fuente. Los demás son propuestas del modelador, a discutir con
> el equipo.

## Resumen

| # | Criterio | Umbral | Estado | Medición |
|---|---|---|---|---|
| 1 | Cita = subcadena exacta del tramo | **100 %** (bloqueante) | CUMPLE (tramo) / PENDIENTE (folio r/v) | 112/112 citas de registros + 33 piezas; folio r/v necesita imágenes |
| 2a | SHACL | **0 violaciones** y cada forma con prueba negativa | CUMPLE | 16 formas, 31 mutaciones detectadas |
| 2b | Razonador | **0 inconsistencias**, 0 individuos de `owl:Nothing` | CUMPLE (con D1 informado) | OWL 2 RL (owlrl): 0 / 0; 50 tipificaciones espurias por D1 (ROAR) |
| 2c | OOPS! | **0 trampas críticas** | CUMPLE | 0 críticas; 1 «Important» (P34, artefacto) |
| 3 | 20 PC con respuesta fijada por historiador antes de construir | ≥ 18/20 correctas; **6/6** en las de DISPUTA/NC | PENDIENTE (falta historiador) | Respuestas provisionales: 13/20 respondidas, 7 PENDIENTES de anotación |
| 4 | Estándar de oro de dos anotadores | α de Krippendorff ≥ 0,80 (≥ 0,67 aceptable); P ≥ 0,90, R ≥ 0,80 | PENDIENTE (faltan anotadores) | Protocolo definido; piloto de 59 afirmaciones |
| 5 | Segundo expediente sin clases nuevas | **0** clases y propiedades nuevas en el núcleo; 0 cambios en las formas | PENDIENTE (falta su transcripción) | Elegido a ciegas: CO Cusco Leg. 70 Exp. 15 |
| 6 | Contraste con fuentes independientes | Cada discrepancia registrada; ninguna resuelta en silencio | PARCIAL | Catálogo: 5 discrepancias; HGIS: Tinta; parroquiales y matrícula: localizadas o no localizadas, sin consultar |
| 7 | Líneas base (LLM con contexto completo; RAG vectorial) | El grafo gana las PC de agregación con atribución | PENDIENTE (fase de conexión) | Hipótesis registrada antes de medir |

## 1. Citas (criterio 1)

* **Instrumento.** `scripts/verificar_citas.py` y `laad.fuente.verificar_cita`. Cada registro se valida además en el esquema (`esquema.py`): un registro con cita no literal **no entra** en el grafo. El test `tests/test_mapeo.py::(f)` comprueba que los desplazamientos `oa:start`/`oa:end` recuperan exactamente la cita.
* **Única normalización:** colapsar espacios en blanco, porque la transcripción parte frases entre líneas. No se pliegan mayúsculas, acentos ni grafías (`tests/test_fuente.py`).
* **Umbral: 100 %.** La literatura muestra que pedir cita literal no basta: Wang (2026, arXiv:2606.00994) obtiene un 90,12 % de citas literales en 5,4 M de filas. Por eso la comprobación es determinista y bloqueante.
* **Folio y recto/vuelto.** La transcripción no marca recto ni vuelto, y solo tiene 4 marcas de folio. El umbral se aplicará cuando se coteje `fuente/folios_cotejo.csv` con las imágenes: 100 % de los tramos con folio y lado cotejados por una persona.

## 2. Validación formal (criterio 2)

* **SHACL.** `ontologia/formas.ttl` se valida con pyshacl contra la unión de los grafos, el tesauro y la jerarquía de clases de los estándares (`src/laad/validacion.py`). Las reglas que dependen del grafo nombrado (separación de capas) se comprueban con `tests/test_capas.py`.
  * **Pruebas negativas.** `tests/test_formas_negativas.py` introduce 31 mutaciones y exige que cada forma con nombre dispare al menos una vez. Así se descubrió que `ActuacionForma` aprobaba en vacío (`docs/bitacora.md`).
* **Razonador.** `scripts/razonar.py` hace un cierre OWL 2 RL (owlrl) de los datos con RiC-O 1.1, CRM 7.1.3 + PC, CRMinf 1.2.1, PROV-O, SKOS, OA, PiCo y ROAR (29 093 tripletas → 99 337). Tarda unos 75 s.
  * Primera ejecución: **1 inconsistencia real** (defecto D1 de ROAR, `docs/C_modelo.md` §7).
  * Tras la corrección: 0.
  * Se informa además de 50 tipificaciones espurias que el axioma de ROAR sigue produciendo sobre observaciones PiCo.
  * Límite: OWL RL no es completo para OWL 2 DL. Un razonador DL (HermiT) sobre CRM no es viable directamente, porque CRM es RDFS y no OWL DL.
* **OOPS!** Servicio REST (oops.linkeddata.es) sobre `ohac.ttl` + `tesauro.ttl` en RDF/XML. Respuesta guardada en `datos/evaluacion/oops_respuesta.xml`.
  * Con `owl:imports` el servicio devuelve «unexpected error». Sin ellos: 0 críticas y 1 «Important» (P34 *Untyped class* sobre `skos:Concept`/`skos:ConceptScheme`), producida precisamente por haber quitado la importación de SKOS.
  * Límite: OOPS! evalúa ontologías OWL, y OHAC no declara términos. El valor del resultado es acotado.

## 3. Preguntas de competencia (criterio 3)

* **Instrumento.** `src/laad/preguntas.py`, `tests/test_preguntas_competencia.py` y `docs/anexos/respuestas_pc.md`, este último generado.
* **Protocolo.**
  1. Un historiador del Cusco colonial que no haya participado en el modelado responde las 20 PC en `docs/B_respuestas_referencia.csv` **antes** de ver el grafo y las respuestas del modelador. Solo usa la transcripción y las imágenes.
  2. Se comparan sus respuestas con las del grafo.
  3. Los tests de aceptación se reescriben para comparar contra el historiador.
* **Umbral.**
  * **6/6** en las preguntas cuya respuesta es «en disputa» o «no lo dice». Son la razón de ser del modelo.
  * **≥ 18/20** en total, contando como correcta una respuesta que contiene todas las afirmaciones pertinentes con su atribución correcta.
* **Estado.** El grafo responde 13 PC. Las 7 restantes (PC02, PC03, PC04, PC07, PC15, PC17 y PC18) **no fallan por el modelo**: faltan anotaciones. Cada una indica en `preguntas.py` qué hay que anotar, y ninguna requiere términos nuevos.

## 4. Estándar de oro y extracción (criterio 4)

* **Unidad de anotación.** El registro plano de `esquema.py`: menciones y afirmaciones.
* **Guía.** `datos/registros/hilo_central.py` es el piloto, anotado por el modelador (un LLM). **No forma parte** del estándar de oro: lo usará la guía, y el subconjunto de esas piezas se anotará de nuevo a ciegas.
* **Procedimiento.**
  1. Dos personas formadas en paleografía anotan **todo** el expediente de forma independiente. No pueden ver la anotación piloto.
  2. **Acuerdo entre anotadores.**
     * Campos categóricos (atributo, polaridad, fundamento, rol): α de Krippendorff nominal.
     * Menciones: F1 de tramos con coincidencia exacta de `texto`.
     * Afirmaciones: F1 por emparejamiento (mismo tramo, mismo atributo, sujeto y afirmante co-referidos).
  3. **Adjudicación** por una tercera persona; ese es el estándar de oro.
  4. **Evaluación de la extracción LLM.** Precisión y exhaustividad en coincidencia estricta: mismo afirmante, sujeto, atributo, valor y polaridad, con la cita solapada en al menos un 50 %. Se informa además la coincidencia laxa: atributo y sujeto.
* **Umbrales propuestos.**
  * Acuerdo entre anotadores: α ≥ 0,80, con 0,67 como mínimo para conclusiones provisionales, según la convención de Krippendorff (2004, *Content Analysis*, 2.ª ed.). Esta referencia no está en el anexo F y hay que verificarla y añadirla antes del artículo; el anexo §D cita a Hayes y Krippendorff (2007) y a Artstein y Poesio (2008) para la elección de α.
  * Extracción: P ≥ 0,90 y R ≥ 0,80 en coincidencia estricta.

  La exhaustividad importa especialmente: las respuestas «el expediente no lo dice» (PC12, PC13) **solo son válidas si la exhaustividad es alta**. Por eso PC12 lo advierte en su propia respuesta.

## 5. Segundo expediente a ciegas (criterio 5)

* **Selección.** Se hizo el 2026-11-12, **antes** de leer su ficha.
  * Universo: los 3651 expedientes del Tomo I, extraídos del catálogo y excluido CC L14 E18.
  * Sorteo con `random.Random(18061806).choice(...)`.
  * **Resultado: Causas Ordinarias, serie Cusco, Legajo 70, Expediente 15.**
  * Es de otra **sección** (causa ordinaria, no criminal), lo que hace la prueba más exigente.
* **Criterio de éxito.**
  * **0** clases o propiedades nuevas en OHAC y **0** cambios en `formas.ttl`.
  * Se permite añadir **conceptos** al tesauro, que es un dato. Se cuentan y se informan, junto con la proporción de registros que necesitan un concepto nuevo.
  * Cambios de código permitidos: solo parametrizar el expediente.
* **Lo que hay que parametrizar antes de la prueba.** Hoy `fuente.py` y `mapeo.py` asumen un solo expediente: ruta de la transcripción, prefijo `cc-14-18`, marcas de folio. Ver `docs/C_modelo.md` §8.
* **Estado.** PENDIENTE: no hay transcripción de ese expediente en el proyecto.

## 6. Contraste con fuentes independientes (criterio 6)

| Fuente | Qué se contrasta | Estado |
|---|---|---|
| Catálogo del ARC (ficha y índice) | Grafía, contenido, folios, jerarquía | Hecho: K1–K5 en `docs/01_materiales.md` |
| Matrícula de tributarios de Tinta (revisita de 1805–1806) | 44 + 7 tributarios denunciados; condición de Huancachoque | No localizada; buscar en ARC, Intendencia, Real Hacienda |
| Registros parroquiales de Tinta | Filiación (Antolín Ortiz, Agustina Falcón), edades | En el Archivo Histórico de la Prelatura de Sicuani; laguna de bautismos 1797–1818 |
| HGIS de las Indias | Lugares | Tinta = 6000357; resto pendiente (PC07) |
| Bibliografía sobre tributo y caciques recaudadores | Cargos de Chuquitapa; «coronel» y «comisionado» en 1780 | Sin mención publicada de Andrés Chuquitapa; fichas en el anexo F §3 |

**Regla:** todo resultado de contraste entra como **afirmación de capa 3** de su propia fuente (el catálogo, la matrícula), con su cita. Nunca corrige el expediente.

## 7. Líneas base (criterio 7)

* **Sistemas.**
  * (a) El mismo LLM con la transcripción paleográfica completa en contexto. Son unos 40 KB, así que cabe.
  * (b) RAG vectorial simple: fragmentos por tramo, embeddings y los 5 mejores fragmentos.
  * (c) Agente sobre el grafo: consultas con nombre más el compositor de respuestas (`docs/D_extraccion_consulta.md`).
* **Medidas por pregunta**, puntuadas a ciegas por el historiador:
  1. Exactitud.
  2. **Atribución correcta**: quién lo dice y en qué actuación.
  3. **Distinción entre afirmación y reconstrucción**.
  4. **Validez de cita**, automática con `verificar_cita`.
  5. Folio correcto.
* **Hipótesis registrada antes de medir** (`docs/B_preguntas_competencia.md` §final): solo el grafo gana las PC de **agregación con atribución**, que son PC05, PC06, PC08, PC09, PC10, PC14, PC16, PC18 y PC19 (y PC03–PC04 a escala de serie).
  * Un LLM con contexto completo puede acertar PC09 o PC11 en prosa, pero tenderá a perder exhaustividad (todas las grafías, todas las piezas) y a presentar la resolución fiscal como un hecho.
  * El RAG tenderá a recuperar un solo lado de cada disputa.
* **Estado.** PENDIENTE: pertenece a la fase de conexión, que la solicitud pide no adelantar.
