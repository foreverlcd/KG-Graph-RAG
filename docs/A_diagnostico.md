# A · Diagnóstico de los intentos previos

> **Alcance.** El «intento 1» (la pila de cinco ontologías) es el proyecto `../Grafo-Conocimiento-Cusco`, auditado en
> todas sus ramas (main, linux, feature/chat-local-gemini, stats, fork/*) y en sus 45 commits «Agent host session».
> El **«intento 2» (Ontología del Expediente CC L14E18) no se ha podido diagnosticar**: el marcador `[Pegar aquí…]` de
> la solicitud llegó vacío y el documento no está en el historial git ni en `~/Projects`, `~/Downloads`, `~/Documents`
> o `~/Desktop`. Este diagnóstico se completará cuando se aporte. Tampoco llegaron por separado el «export del grafo»
> ni los «prompts»; se usaron los que contiene el repositorio (`data/grafo.json`, `pipeline/extractor.py`,
> `chat/local_chat.py`).
>
> **Evidencia.** Todas las afirmaciones de este documento remiten a `docs/anexos/A_evidencia_intento_previo.md`, que da
> archivo:línea o nodo de `grafo.json`. Esa auditoría la hizo un subagente en solo lectura. El modelador comprobó por
> su cuenta los puntos 4, 6 y 13: definición de estados en `extractor.py:73-77`, los ocho `DECLARO` hacia
> `afirmacion_01`, el recuento de los ocho tipos de arista y «Selva» presente en el grafo pero ausente en la fuente.
> Las cifras de citas son reproducibles con `scripts/diag/medir_citas.py`.

## Resumen en una frase

El intento 1 tiene buenas intenciones epistémicas, pero las aplica mal. Lo anuncian sus comentarios: reificar
afirmaciones, exigir citas, guardar variantes. Pero no hay un modelo que lo haga cumplir. Las ontologías son
**etiquetas en docstrings**. Un LLM decide en un solo paso la identidad, el rol, el folio, el tipo de acto y la
**verdad**. El constructor del grafo **sobrescribe por id**, y el resultado atribuye frases a personas que no las
dijeron.

## 1. Los puntos que pidió revisar la solicitud

### 1.1 Roles como subclases de Persona — **Falla (en variante)**

No hay subclases OWL porque no hay OWL. El mismo error aparece en tres formas:

* Hay **12 nodos «Persona» cuya identidad es un rol**: `persona_subdelegado_tinta`, `actor_fiscal_declarante` («Fiscal Declarante (Anónimo)»), `persona_declarante_anonimo`, `persona_presidente_intendente`…
* Los roles procesales se guardan como propiedad de la persona en `cargos_mencionados`. `persona_ysidro_cano` tiene `['Testigo']`. `persona_mariano_figueroa` tiene `['Testigo a falta de escribano']`. Pero ser testigo es un papel en *una* actuación, no un atributo de la persona.
* El rol de la participación es **texto libre**: 25 valores, con erratas (`Agresor_Alegato`) y absurdos. Por ejemplo, `institucion_real_hacienda` aparece con rol `Juez_Subdelegado`, y también el presidente, el fiscal y el teniente asesor.

**Consecuencia.** No se puede preguntar «¿en qué actuaciones intervino Mata y con qué papel?». La respuesta está repartida entre nodos-rol y nodos-persona que no se unen.

**Decisión.** El rol es un `skos:Concept` (`tes:roles`), valor de `crm:P14.1_in_the_role_of` sobre la participación en una actuación concreta. Ninguna persona lleva un rol como tipo. SHACL lo prohíbe (`ontologia/formas.ttl`, forma `NoRolComoTipo`).

### 1.2 Predicados hechos a medida del caso — **Falla**

Hay ocho tipos de arista en mayúsculas sin IRI: `MENCIONADO_EN` (193), `ROL_EN_EVENTO` (106), `OCURRE_EN` (60), `DECLARO` (49), `DESCRIBE_EVENTO` (49), `EXTRAIDO_DE` (49), `PARTICIPA_EN` (47) e `INVOLUCRA_BIEN` (21). `tipo_evento` es texto libre: `ServicioMilitar`, `Ratificacion_Escrito`, `Compraventa`… Los predicados que el diseño necesitaba de verdad, `CONTRADICE` y `RATIFICA`, están declarados pero tienen **0 instancias**.

**Decisión.** No hay predicados propios. Lo que cambia de un expediente a otro (qué se afirma) es **dato**: una lista cerrada de atributos en SKOS (`tes:atributos`), usada como valor de `crm:P177_assigned_property_of_type`. La contradicción no se guarda como arista. **Se calcula** con una consulta: mismo sujeto (o sujetos co-referidos en una reconstrucción), mismo atributo, valor o polaridad incompatibles.

### 1.3 Clases mezcladas con individuos — **Falla**

* «Subdelegado» es a la vez valor de vocabulario (`standards.py:121`), rol (`('actor_pedro_de_la_mara','Subdelegado')`), cargo y **persona** (`persona_subdelegado_tinta`). Lo mismo pasa con «Fiscal» y «Presidente».
* `CondicionTributaria` y `CargoVirreinal` se declaran «padre: skos:Concept», pero sus valores son cadenas de un `Literal[...]` de Pydantic y nunca llegan a conceptos con IRI.
* Los ayllus son a la vez `Actor` (`ayllu_tinta`) y `Lugar` (`lugar_ayllu_tinta`), sin arista que los una. Un colectivo indeterminado («Indios sublevados») se modela como individuo con condición fiscal.

**Decisión.** Hay tres planos y no se cruzan: clases (solo las de los estándares), individuos (personas, grupos, piezas, actuaciones) y conceptos SKOS (cargos, condiciones, roles, tipos). SHACL comprueba que ningún `skos:Concept` del tesauro aparezca como `rdf:type` ni como sujeto de `P14_carried_out_by`. El ayllu es un `crm:E74_Group` con `P2_has_type ent:ayllu`. Si hace falta su territorio, es un `crm:E53_Place` distinto, enlazado mediante una actividad o con `crm:P74_has_current_or_former_residence`. No son dos nodos sueltos.

### 1.4 Estados de verdad que toman la resolución como hecho — **Falla grave**

El prompt lo establece por definición (`extractor.py:73-77`): «Confirmado_Oficial: Una resolución posterior lo confirma como verdadero. Desmentido_Falso: Una resolución lo declara falso o fabricado».

* La vista del fiscal («menos conforme a la verdad») se convierte en `Desmentido_Falso`.
* El informe del subdelegado Mata, que es **parte interesada** porque fue él quien mandó llevar a Huancachoque a la cárcel (UT18), y una **orden** de retiro se convierten en `Confirmado_Oficial`.
* Una venta republicana ajena al expediente (Ugarte) también queda `Confirmado_Oficial`.

Los tests lo exigen (`tests/test_ontology.py:125-154`; `tests/test_chat_evaluation.py`, casos `tinta-1806` y `resolucion-quejas`, con `required_state="Desmentido_Falso"`).

Para el historiador es el error más dañino. Precisamente la pregunta abierta del expediente es si la Audiencia resolvió sobre testimonios fabricados, o sobre retractaciones obtenidas por el mismo subdelegado al que se acusaba de pasividad. El grafo la daba por cerrada.

**Decisión.** El grafo **no guarda valores de verdad** en las capas 1–3. Una resolución es una afirmación (`crm:E13_Attribute_Assignment`) hecha en una actuación de tipo `act:auto` o `act:vista-fiscal`, por un agente en rol `rol:resolutor` o `rol:dictaminador`. Su **fuerza institucional** (`fza:resolutiva`, `fza:dictaminadora`) se registra aparte y no es verdad. Las creencias solo existen en la capa 4, como `crminf:I2_Belief` de un investigador con nombre y fecha.

### 1.5 PROV-O usado para «quién lo dijo en 1806» — **Falla**

`standards.py:82-85` define `wasAttributedTo` como «Actor histórico o testigo que emitió la declaración». No se registra ni el modelo, ni el prompt, ni la versión de la transcripción, ni la fecha de extracción, ni quién validó. El modelo (`gemini-3.6-flash`) solo existe como constante en el código. El extractor reutiliza extracciones viejas por id sin dejar rastro. `confianza_extraccion` = 1.0 en 47 de 49 casos es una cifra autodeclarada por el LLM.

**Decisión.** Quién lo dijo en 1806 es CIDOC CRM (`P14_carried_out_by` en el E13). PROV-O describe **cómo se produjo el dato**. Cada lote de registros es un grafo nombrado y `prov:Entity`, `prov:wasGeneratedBy` una `prov:Activity` de extracción que `prov:used` la transcripción, identificada por su sha256, y el prompt versionado (`prov:Plan`), `prov:wasAssociatedWith` el modelo (`prov:SoftwareAgent`) y la persona que validó.

### 1.6 ¿Se usan de verdad las cinco ontologías? — **No: solo nombran etiquetas**

**Nunca se emite RDF** (`rdflib` no está en `requirements.txt`). Hay **cero** IRIs `rico:`, `crm:`, `prov:` o `skos:` en `grafo.json` y en `extracciones.jsonl`. Los `*_MAPPING` de `standards.py` no los importa el pipeline; solo un test comprueba que existen sus claves. RiC-O, CIDOC CRM, PROV-O y SKOS aparecen en docstrings («Equivalente a crm:E21_Person»). OHAC tiene un espacio de nombres inventado (`archivo-cusco.pe`) y sus «extensiones» (`AfirmacionHistorica`, `contradice`, `ratifica`) o no se instancian o se instancian sin relaciones.

**Decisión.** Todo término usado tiene que existir en el archivo de especificación descargado (`vendor/`; prueba `tests/test_terminos_existen.py`). El grafo se emite en RDF (TriG). SHACL valida contra él y un razonador comprueba que es consistente.

## 2. Otros fallos encontrados (no estaban en la lista)

### 2.1 Colisión de identificadores: el grafo atribuye frases a quien no las dijo

`graph_builder.py:409-410` sobrescribe nodos por id y añade un `DECLARO` por extracción. Hay 49 afirmaciones extraídas y quedan 34 nodos. `afirmacion_01` conserva el texto del **fiscal** («menos conforme a la verdad las quejas dadas por Manuel Guancoichoque»), pero tiene **ocho declarantes**, entre ellos el propio Huancachoque (`persona_manuel_mancachoque`, `actor_manuel_guancachoque`). Según el grafo, el denunciante declaró que sus quejas eran falsas. Las métricas del proyecto («Integridad referencial 574/574», «KGCQ 94,1 A+») no lo detectan.

**Decisión.** Los identificadores son deterministas, con `tramo + ordinal` (`A-UT11-003`). El mapeo falla si se repite un id. Un test comprueba que cada E13 tiene exactamente un afirmante.

### 2.2 Folios inventados

El segmentador toma el **primer** `folio N` de cada bloque, aunque sea una referencia interna («En folio 10 remito», «De folio 4»). Si no lo encuentra, cuenta bloques. Así el marcador real «Folio 20» se ignora y la numeración retrocede de 10 a 4. **Solo 2 de 21 folios son correctos.** Ese folio heurístico se le da al LLM como dato, con la orden de copiarlo.

**Decisión.** Hay tramos con folio solo cuando existe una marca explícita verificada; en el resto, «no consta». Recto/vuelto: pendiente de cotejo con las imágenes (`docs/01_materiales.md` §3).

### 2.3 Citas no literales

De 49 citas, **32 (65,3 %) son subcadena exacta** de la paleográfica, 43 (87,8 %) tras colapsar espacios y **6 (12,2 %) no están en ningún texto**. Las causas son elisiones con «…» que pegan pasajes, palabras partidas que el LLM recompone y abreviaturas expandidas. El informe del proyecto lo maquilla con `fuzz.partial_ratio >= 85` hasta un «98 % de anclaje» y un «0 % de riesgo de alucinación».

**Decisión.** Verificación exacta por tramo (`verificar_cita`), con umbral del 100 % y rechazo del registro si falla. La única normalización es el colapso de espacios.

### 2.4 El tipo de acto se decide por subcadenas

«he **visto** con mis ojos» clasifica una certificación como `Auto_Decreto_Judicial`. «el señor Agustin **Fiscal** Don Althamacio Zotelo» clasifica el informe del cura como `Dictamen_Fiscal`. De ahí el LLM inventa un «Fiscal Declarante (Anónimo)» de condición «Eclesiástico» y le atribuye los insultos del cura contra Huancachoque.

**Decisión.** La lista de piezas y su tipo de actuación es capa 1 y **la cura un humano** (`datos/piezas.jsonl`). El LLM la recibe como contexto cerrado y no la decide.

### 2.5 Fusiones y divisiones de personas sin prueba

* **Fusiones sin evidencia registrada:**
  * Huancachoque con su presunto padre («Ortis o Guancachoque», «Ortiz»).
  * «Mariano Casorla» con «Martin casorla».
  * Mata con Mara. Es probable, pero no hay rastro.
  * «Chuquitaza» con un cargo que es una acusación («Coronel y comisionado de Túpac Amaru»).
* **Divisiones:**
  * Huancachoque aparece en 6 nodos, Chuquitapa en 6 y Túpac Amaru en 5.
  * «Don Francisco Muñoz y Señor Clemente» se parte en dos personas e inventa `persona_clemente`.
* **Hechos inventados:**
  * A Ruiz de Castilla se le asigna el título «Marqués de Selva Alegre», que no está en la fuente.
  * El ejemplo del README atribuye a Cano la cita «mandó a medianoche a matarle», que no existe.
* **Ignora el propio texto:** «Juan Quiñones», de quien la fuente dice «no hay tal hombre en el pueblo de Tinta», figura como persona real y como declarante.
* **Material ajeno integrado:** el notario republicano Ugarte entra como una compraventa de 1806.

**Decisión.** La capa 2 **nunca fusiona** (una mención = un nodo `pico:PersonObservation`). Las identidades viven en la capa 4: una `pico:PersonReconstruction` derivada de menciones concretas, con autor, fecha, argumento y valor de creencia. Las identidades disputadas (N3, N4) quedan como dos reconstrucciones alternativas o como ninguna.

### 2.6 Fechas imposibles copiadas como hechos

* «13 de agosto» para una ratificación que cumple un decreto del 21.
* «1806-11-26» para el informe del cura, que ya cita el informe del 8 de noviembre.
* «23 de diciembre de 1810» para una notificación (`evento_notificacion_auto_1810`).

Los dos primeros casos *están* en la transcripción. El fallo es convertirlos en datos normalizados sin avisar.

**Decisión.** La capa 2/3 guarda la fecha **tal como está escrita** (`crm:E52_Time-Span` con `P1_is_identified_by` → `E41_Appellation`). Una fecha normalizada solo existe en la capa 4, y si contradice el orden de las piezas lo marca una prueba (`consultas/control_secuencia.rq`).

### 2.7 Evaluación que premia el error

* Las preguntas de chat exigen el estado `Desmentido_Falso`.
* Con el LLM real fallaron 6 de 10 casos, que **no se nombran en ningún sitio**: solo hay categorías como «tributarios», «Ayllu Tinta» o «resoluciones».
* Las métricas propias («Factor de consolidación 2.36x», «Tasa de reificación 100 %») se cumplen por construcción.

**Decisión.** Hay 20 preguntas de competencia **escritas antes de modelar** (`docs/B_preguntas_competencia.md`), con respuesta fijada por un historiador antes de construir, y umbrales externos (`docs/G_evaluacion.md`).

## 3. Lo que sí vale del intento 1 (y se conserva)

* La intención de **reificar afirmaciones**, ahora en E13, y la **cita literal obligatoria**, ahora verificada.
* Guardar **variantes gráficas**, ahora como menciones en la capa 2, no como `altLabel` de una persona ya fusionada.
* Las listas cerradas en la salida del LLM. Se mantienen, pero más pequeñas, sin decisiones de verdad ni de identidad, y generadas desde un tesauro.
* Validar con Pydantic y reintentar, pero con validación de citas **dentro** del esquema.

## 4. Matriz fallo → decisión → control

| Fallo (intento 1) | Decisión de diseño | Control automático |
|---|---|---|
| Rol como tipo o atributo de la persona | Rol SKOS en `P14.1_in_the_role_of` | SHACL `NoRolComoTipo` |
| Predicados ad hoc | Atributos SKOS en `P177`; contradicción calculada | `tests/test_terminos_existen.py` |
| Concepto = individuo | Tres planos separados | SHACL `ConceptoNoInstanciado` |
| Verdad por resolución | E13 + fuerza institucional; creencia solo en capa 4 | SHACL: ningún E13 lleva valor de creencia |
| PROV para 1806 | PROV solo para el dato | SHACL `LoteConProcedencia` |
| Ontologías decorativas | RDF real e IRIs verificadas | tests de términos y razonador |
| Colisión de ids | Ids deterministas; el mapeo falla si se duplican | `tests/test_mapeo.py` |
| Folios inventados | Tramos y «no consta» | `tests/test_fuente.py` |
| Citas no literales | Verificación exacta por tramo | `scripts/verificar_citas.py` (100 %) |
| Tipo de acto heurístico | Piezas curadas a mano | SHACL: cada actuación tiene un tipo de `tes:actuaciones` |
| Fusiones sin prueba | Capa 2 sin fusión; capa 4 con autor | SHACL `ReconstruccionConArgumento` |
| Fechas imposibles silenciadas | Fecha escrita frente a normalizada, en capas distintas | `consultas/control_secuencia.rq` |
| Evaluación circular | PC previas y umbrales externos | `tests/test_preguntas_competencia.py` |
