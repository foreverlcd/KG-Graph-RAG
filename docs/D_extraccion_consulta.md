# D · Extracción y consulta

> **Alcance de esta fase.** Lo implementado y probado:
> * el **esquema plano y cerrado** (`src/laad/esquema.py`);
> * el **cargador con integridad** (`src/laad/registros.py`);
> * el **mapeo determinista** (`src/laad/mapeo.py`);
> * las **consultas con nombre** (`consultas/*.rq`, `src/laad/consulta.py`);
> * el **compositor de respuestas** (`src/laad/responder.py`, `src/laad/preguntas.py`).
>
> **No está implementada** la conexión con el LLM, ni para extraer ni para conversar. Se especifica aquí, pero se deja
> para la fase siguiente, tal como pide el encargo («antes de empezar con la conexión, prepara muy bien la ontología»).

## 1. Principio: el LLM no escribe CIDOC CRM

```text
transcripción ──► [LLM o anotador] ──► registros planos (JSON) ──► validación ──► mapeo determinista ──► TriG
   (tramo)          esquema cerrado       Pieza/Mención/Afirmación   esquema + citas     (Python, sin LLM)     4 capas + PROV
```

El LLM rellena tres tipos de registro y nunca ve IRIs, clases ni propiedades de CRM, RiC-O, PROV ni oa:. Las listas
cerradas se **generan del tesauro** (`conceptos(esquema)`): no hay una segunda lista que pueda desincronizarse. El
mapeo a RDF es una función pura. El mismo lote produce grafos isomorfos (`tests/test_mapeo.py`), y un id repetido
aborta el proceso. Esa colisión de ids fue el fallo 2.1 del intento previo.

### 1.1 Qué decide el LLM y qué no

| Decide el extractor (LLM o humano) | No decide nunca |
|---|---|
| Menciones tal como están escritas, con su cita | El tipo de actuación de la pieza: viene de `datos/piezas.jsonl`, curado a mano (fallo 2.4) |
| Rol del mencionado en la pieza (de la lista cerrada) | El folio: viene de la capa de fuente (fallo 2.2) |
| Afirmaciones: afirmante, sujeto, atributo, valor, polaridad, fundamento, cita | Si dos menciones son la misma persona (capa 4, investigador) |
| Si el sujeto es elíptico; entonces está obligado a explicarlo en `nota` | Si una afirmación es verdadera (no existe ese campo) |
| | La fuerza institucional: se deriva de la actuación, con una tabla fija en `mapeo.FUERZA` |

Esta división responde a lo que ha encontrado la literatura reciente. Las fichas están en `docs/anexos/F_informe_precedentes_y_literatura.md` §2.

* **Montenegro et al. (2026), arXiv:2607.24551, sobre un grafo jurídico francés.** El modelador comprobó en el resumen el título, los autores y el aviso de una «lower exact signature compliance», es decir, combinaciones dominio–rango no previstas. El cuerpo del artículo, según el subagente, da estos datos:
  * JSON válido en el 100 % de los casos;
  * firmas dominio–rango exactas solo entre el 49,86 % y el 72,61 % cuando la ontología va únicamente en el prompt;
  * una arquitectura de tablas intermedias elevadas a RDF con RML.

  **Apoya** sacar la ontología del LLM: en un esquema cerrado con mapeo determinista, ese tipo de error no puede producirse.
* **Marketakis, Lintanff-Castel y Tzitzikas (SETN 2026), y Marketakis y Tzitzikas (CEUR Vol-4192), del grupo FORTH, que mantiene CIDOC CRM.** En zero-shot, los mapeos X3ML a CRM que genera el LLM tienen precisión «very close to zero». Los errores típicos son elegir mal la clase o la propiedad y producir mapeos sintácticamente válidos que violan las restricciones de la ontología. Los autores critican el *prompt-to-RDF*.

  **Apoya** la decisión. La nuestra es incluso más conservadora: el mapeo lo escribe una persona y no el LLM.
* **Schimmenti et al. (2025), ATR4CH, arXiv:2511.10354.** El modelador comprobó en el resumen el título, los autores y las cifras: F1 de 0,96–0,99 en metadatos, 0,7–0,8 en entidades, 0,65–0,75 en hipótesis y 0,95–0,97 en evidencia. Según el subagente, el método usa respuestas JSON con esquema más algoritmos de mapeo, atribuye las opiniones a quien las sostiene y el LLM sobregenera tripletas.

  Es el precedente **más parecido** en método. Su F1 bajo en hipótesis respalda que la reconstrucción (capa 4) no la haga el LLM.
* **Wang (2026), arXiv:2606.00994.** Vocabulario cerrado más una cita literal por fila: solo el 90,12 % de las citas eran realmente literales. **Apoya** que la verificación de subcadena sea determinista y bloqueante.
* **Tam et al. (2024), EMNLP Industry, DOI 10.18653/v1/2024.emnlp-industry.91.** El formato estricto degrada el *razonamiento* pero no la *clasificación*. **Matiza** la decisión: el esquema solo pide clasificaciones locales (tipo, rol, polaridad), y los juicios que requieren razonar (identidad, verdad, si una retractación es parcial) quedan en la capa 4.

  Pendiente de evaluar: añadir un campo de razonamiento previo, que no se mapea, antes de rellenar el registro.

Ningún artículo compara cabeza a cabeza, sobre el mismo corpus, la generación directa de CRM frente al esquema
intermedio. Esa comparación podría ser una contribución del proyecto, siempre que se haga con el estándar de oro de
`docs/G_evaluacion.md`.

## 2. El esquema plano

Se define en `src/laad/esquema.py` (Pydantic v2, `extra="forbid"`).

| Registro | Campos | Validaciones bloqueantes |
|---|---|---|
| `Pieza` (capa 1, la cura un humano) | id, orden, tramos, tipo_actuacion, titulo, fecha_escrita, lugar_escrito, cita_inicio, ajena_al_expediente | Los tramos existen; fecha, lugar y cita son literales en sus tramos |
| `Mencion` (capa 2) | id, tramo, pieza, clase (persona, grupo o lugar), texto, rol_en_pieza, tipo_entidad, cita | `texto` está dentro de `cita`; `cita` es literal en `tramo`; `tramo` pertenece a `pieza` |
| `Afirmacion` (capa 3) | id, tramo, pieza, afirmante, rol_afirmante, sujeto{mencion, pieza o hecho; eliptico}, atributo, valor{concepto, mencion, pieza, hecho o literal}, rol_en_hecho, polaridad, fundamento, cita, nota | Cita literal; listas cerradas tomadas del tesauro; rol_afirmante dentro de la rama `rol:afirmante`; `participa-en-hecho` exige rol; un sujeto elíptico exige nota; los hechos son locales a la pieza; las referencias existen |
| `Reconstruccion` (capa 4, la escribe el investigador) | id, tipo (identidad, hecho o cargo), etiqueta, menciones, premisas, creencia, argumento, autor, fecha, externo | Argumento de al menos 20 caracteres; creencia de la lista cerrada; menciones de una sola clase |

Al LLM se le dará el JSON Schema que genera Pydantic, como salida estructurada. Siempre se re-valida en Python,
porque la salida estructurada no garantiza que la cita sea literal.

## 3. Extracción con LLM (especificación de la fase siguiente)

1. **Unidad de trabajo: una pieza.** El extractor recibe:
   * el texto **paleográfico** de sus tramos, nunca el modernizado;
   * la ficha de la pieza (tipo, fecha y tramos, de `piezas.jsonl`);
   * el esquema;
   * la guía de anotación, cuyo ejemplo es `hilo_central.py`.
2. **Salida:** una lista de registros de mención y de afirmación.
3. **Validación.** Cada registro que falla vuelve al LLM con el mensaje exacto del validador, hasta 2 reintentos. Si sigue fallando, se descarta y se registra. **No se repara la cita a mano.**
4. **Procedencia.** Cada lote es un grafo nombrado con su `prov:Activity`, que registra:
   * modelo y versión;
   * prompt versionado en `prompts/`, como `prov:Plan`;
   * sha256 de la transcripción;
   * fecha;
   * persona validadora.

   El mapeo ya lo implementa (`mapeo.Procedencia`).
5. **Lo que queda fuera de la extracción:** identidad (capa 4), normalización de fechas y valores (capa 4) y tipo de actuación (capa 1).

## 4. Consulta y respuesta

El agente conversacional **no genera SPARQL libre**.

1. **Elige una consulta con nombre** de `consultas/`: `afirmaciones`, `disputas`, `disputas_firma`, `reconstrucciones`, `menciones_de`, `piezas`, `control_secuencia` o `procedencia`.
2. **Le pasa IRIs**, que `consulta._values` valida y convierte en un bloque `VALUES`.
3. **Para resolver nombres de entidades**, por ejemplo «Chuquitapa», consulta el índice de etiquetas de las reconstrucciones y de las menciones, y devuelve candidatos. Esta parte está pendiente; hoy los slugs se pasan a mano.
4. **Compone la respuesta** con `responder.Respuesta`, que garantiza:
   * Que se separen **AFIRMACIÓN** (capa 3) y **RECONSTRUCCIÓN** (capa 4).
   * Que cada afirmación lleve cita literal, tramo y folio. Si no hay folio, dice «folio no consta en la transcripción».
   * Que cada afirmación lleve afirmante (mención y reconstrucción), rol, actuación, fecha escrita, ante quién y quién firma. Si falta un dato, dice «no consta».
   * Que las resoluciones aparezcan con su **fuerza institucional**, nunca como hechos.
   * Que las respuestas «no lo dice» muestren la evidencia de lo que sí consta, con la advertencia sobre la exhaustividad.
5. **El LLM conversacional** solo puede reformular las filas. Antes de mostrarla, se comprueba que toda cita entre comillas de su respuesta sea subcadena de una fila devuelta (verificación posterior, pendiente de implementar).

Las respuestas completas a las 20 PC están en `docs/anexos/respuestas_pc.md`.

## 5. Rendimiento medido (2026-11-12, en el portátil del proyecto)

| Operación | Tiempo |
|---|---|
| Construir el grafo (4315 tripletas, 23 grafos nombrados) + SHACL | ≈ 9 s |
| Consulta `afirmaciones` filtrada | ≈ 2 s |
| `disputas` | 1,7 s. La primera versión tardaba 144 s y fallaba en los casos de piezas; ver la bitácora |
| Cierre OWL RL con todos los estándares | ≈ 75 s |
| Batería de pruebas completa | ≈ 55 s |
