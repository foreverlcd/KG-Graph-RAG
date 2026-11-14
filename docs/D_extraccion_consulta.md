# D · Extracción y consulta

> **Alcance de esta fase.** Lo implementado y probado:
> * el **esquema plano y cerrado** (`src/laad/esquema.py`);
> * la **capa de fuente** con el formato de transcripción configurable (`src/laad/fuente.py`);
> * el **cargador con integridad** (`src/laad/registros.py`) y el **corpus de expedientes** (`src/laad/corpus.py`);
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
cerradas se **generan del tesauro** (`conceptos(esquema)`) y de sus conceptos candidatos: no hay una segunda lista que
pueda desincronizarse. El
mapeo a RDF es una función pura. El mismo lote produce grafos isomorfos (`tests/test_mapeo.py`), y un id repetido
aborta el proceso. Esa colisión de ids fue el fallo 2.1 del intento previo.

### 1.1 Qué decide el LLM y qué no

| Decide el extractor (LLM o humano) | No decide nunca |
|---|---|
| Menciones tal como están escritas, con su cita | El tipo de actuación de la pieza: viene del archivo de piezas que declara el manifiesto (`datos/piezas.jsonl` en el piloto), curado a mano (fallo 2.4) |
| Rol del mencionado en la pieza (de la lista cerrada) | El folio: viene de la capa de fuente (fallo 2.2) |
| Afirmaciones: afirmante, sujeto, atributo, valor, polaridad, fundamento, cita | Si dos menciones son la misma persona (capa 4, investigador) |
| Si el sujeto es elíptico; entonces está obligado a explicarlo en `nota` | Si una afirmación es verdadera (no existe ese campo) |
| Un concepto que el tesauro no tiene: lo **propone** como candidato y lo usa (§2.1) | La fuerza institucional: se deriva del tipo de actuación, según el tesauro (`act:x skos:related fza:y`) |

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
| `Mencion` (capa 2) | id, tramo, pieza, clase (persona, grupo, lugar o cosa), texto, rol_en_pieza, tipo_entidad, cita | `texto` está dentro de `cita`; `cita` es literal en `tramo`; `tramo` pertenece a `pieza` |
| `Afirmacion` (capa 3) | id, tramo, pieza, afirmante, rol_afirmante, sujeto{mencion, pieza o hecho; eliptico}, atributo, valor{concepto, mencion, pieza, hecho o literal}, rol_en_hecho, polaridad, fundamento, cita, responde_a, segun, afirmante_de_otra_pieza, distribuida, nota | Cita literal; listas cerradas tomadas del tesauro; el concepto de valor debe estar en el esquema que admite el atributo (`dct:conformsTo`); rol_afirmante dentro de la rama `rol:afirmante`; el afirmante es persona o grupo y, si es de otra pieza, debe marcarse; las decisiones del anotador exigen nota; `segun` exige fundamento «oidas»; los hechos son locales a la pieza; las referencias existen |
| `Reconstruccion` (capa 4, la escribe el investigador) | id, tipo (identidad, hecho o cargo), etiqueta, menciones, premisas, creencia, argumento, autor, fecha, externo, identificador_externo; para cargo: titular, cargo, ambito, ambito_literal, inicio, fin, vigencia_literal | Argumento de al menos 20 caracteres; creencia de la lista cerrada; menciones de una sola clase; un cargo exige titular, cargo del tesauro y premisas |

Al LLM se le dará el JSON Schema que genera Pydantic, como salida estructurada. Siempre se re-valida en Python,
porque la salida estructurada no garantiza que la cita sea literal.

En una `Reconstruccion`, las menciones, los hechos y las premisas se escriben calificados con el expediente
(`cc-14-18:M-UT01-003`): la capa 4 es común al corpus y los ids de registro solo son únicos dentro de un expediente
(`esquema.separar_ref`, ADR-036).

### 2.1 Listas cerradas que crecen: candidatos, dominio y rango

* **Conceptos candidatos.** Las listas cerradas incluyen los conceptos aprobados del tesauro y los candidatos
  pendientes (`ontologia/candidatos.ttl`). Un registro que usa un candidato se acepta con un **aviso**
  (`Lote.avisos`, y `sh:Warning` en el grafo); uno que usa un concepto retirado se rechaza y el mensaje dice cuál
  usar en su lugar. Se propone con `scripts/candidatos.py --proponer` (ADR-038; procedimiento en
  `ontologia/README.md`).
* **Dominio y rango.** `datos/atributos.csv` dice qué puede ser sujeto y valor de cada atributo. El esquema lo
  comprueba al cargar cada afirmación y `registros.py` lo repite con la clase real de cada mención; el grafo lo
  comprueba otra vez con `ontologia/formas_atributos.ttl` (ADR-039). Un atributo candidato sin fila solo produce
  un aviso.

### 2.2 La transcripción: formato configurable

La segmentación de la transcripción en unidades (`UT00`, `UT01`, …) y tramos ya no supone la convención del piloto.
La clave opcional `formato` del manifiesto la describe con cinco claves, todas opcionales (`separador`, `encabezado`,
`marca_folio`, `ignorar`, `codificacion`; valores por defecto en `fuente.FORMATO_POR_DEFECTO`). Sin esa clave rige la
del piloto: unidades separadas por líneas `#` y marcas de folio escritas a mano en `marcas_folio`. Lo que casa
`ignorar` (texto editorial) se sustituye por espacios: no es citable y los desplazamientos siguen siendo los del
archivo. Una clave desconocida o una expresión que no compila es un error. `scripts/nuevo_expediente.py` crea el
esqueleto del manifiesto en estado `borrador` y muestra la tabla de tramos para que una persona la revise antes de
anotar (`--solo-ver` no escribe nada). La guía completa está en `datos/expedientes/README.md`; las pruebas, en
`tests/test_formato_transcripcion.py` (ADR-041).

## 3. Extracción con LLM (especificación de la fase siguiente)

1. **Unidad de trabajo: una pieza.** El extractor recibe:
   * el texto **paleográfico** de sus tramos, nunca el modernizado;
   * la ficha de la pieza (tipo, fecha y tramos, del archivo de piezas del expediente);
   * el esquema;
   * la guía de anotación, cuyo ejemplo es `hilo_central.py`.
2. **Salida:** una lista de registros de mención y de afirmación.
3. **Validación.** `scripts/validar_lote.py <expediente> [registros.jsonl …]` valida un lote nuevo junto con el resto del corpus sin escribir el grafo (el expediente es el primer argumento, obligatorio). Cada registro que falla vuelve al LLM con el mensaje exacto del validador, hasta 2 reintentos. Si sigue fallando, se descarta y se registra. **No se repara la cita a mano.**
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

1. **Elige una consulta con nombre** de `consultas/` (`consulta.nombres()` las lista; entre ellas `afirmaciones`, `disputas`, `disputas_firma`, `reconstrucciones`, `menciones_de`, `piezas`, `participantes`, `cargos`, `catalogo`, `control_secuencia`, `procedencia` y `candidatos_en_uso`). Varias admiten el parámetro opcional `?expediente`.
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

### 4.1 Motor de consulta: Oxigraph

Desde el 2026-11-14 las consultas se ejecutan por defecto en **Oxigraph** (`pyoxigraph`), cargado desde los N-Quads
canónicos de `datos/grafo/` más el tesauro y los candidatos; el grafo por defecto de la consulta es la unión de los
grafos nombrados, materializada al cargar. La variable de entorno `LAAD_MOTOR=rdflib` vuelve al motor anterior
(rdflib en memoria, sin dependencias compiladas), y `tests/test_motores.py` comprueba que los dos devuelven las
mismas filas. rdflib sigue siendo quien **construye, serializa y valida** el grafo; Oxigraph solo lo consulta
(ADR-042).

`scripts/servir.py` responde una consulta con nombre desde la línea de órdenes
(`scripts/servir.py piezas expediente=cc-14-18`); no es un servidor HTTP. Con `--volcar` escribe un almacén
persistente en disco y con `--almacen` lo consulta sin volver a cargar el corpus.

## 5. Rendimiento medido

### 5.1 Medición del 2026-11-14 (expediente completo, Oxigraph)

| Operación | Tiempo | Fuente |
|---|---|---|
| Carga del corpus en Oxigraph (memoria) | 0,13 s | `datos/grafo/escala.md` |
| `piezas(expediente)` | 0,002 s | `datos/grafo/escala.md` |
| `afirmaciones(expediente, filtroEntidad, atributo)` | 0,026 s | `datos/grafo/escala.md` |
| `afirmaciones(expediente)`, todas con sus facetas | 0,081 s | `datos/grafo/escala.md` |
| `disputas()` | 0,35 s | `datos/grafo/escala.md` |
| La misma `afirmaciones` filtrada con `LAAD_MOTOR=rdflib` | ≈ 15 s (frente a 0,05 s con Oxigraph en la misma ejecución) | Medición puntual al redactar este apartado; una sola ejecución |

La medición de escala replica el expediente piloto hasta 1 000 veces (no son expedientes reales). Su conclusión:
la carga y el almacenamiento crecen linealmente y están comprobados hasta 1 000 expedientes sintéticos; las
consultas con nombre, tal como están escritas, solo son interactivas hasta unas decenas de expedientes y habrá que
reescribirlas (restricción al expediente como patrón de tripletas). No se midieron a escala la construcción del
grafo, la validación SHACL ni el razonador. Método, tablas y cautelas: `datos/grafo/escala.md`.

### 5.2 Medición del 2026-11-12 (solo el hilo central, rdflib; histórica)

| Operación | Tiempo |
|---|---|
| Construir el grafo (5455 tripletas, 59 grafos nombrados) + SHACL | ≈ 10 s |
| Consulta `afirmaciones` filtrada | ≈ 2 s |
| `disputas` | 2,5 s. La primera versión tardaba 144 s y fallaba en los casos de piezas; ver la bitácora |
| Cierre OWL RL con todos los estándares | ≈ 79 s |
| Batería de pruebas completa (205 pruebas en esa fecha) | ≈ 90 s |
