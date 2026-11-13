# C · El modelo: cuatro capas separadas

> **Archivos de referencia:**
> * Perfil: `ontologia/ohac.ttl`.
> * Tesauro: `ontologia/tesauro.ttl`.
> * Formas: `ontologia/formas.ttl`.
> * Mapeo: `src/laad/mapeo.py`.
> * Grafo de ejemplo: `datos/grafo/cc-14-18.trig`.
>
> La tabla completa de correspondencias está en `docs/C_correspondencias.md`; la trazabilidad pregunta → término →
> consulta → prueba, en `docs/C_trazabilidad.md`. Las notas de alcance literales de cada término, en
> `docs/anexos/C_terminos_verificados.md`.

## 1. Principios

1. **Cuatro capas, cuatro tipos de grafo nombrado.** El dato de cada capa vive en un grafo propio y no se mezcla con los demás (`tests/test_capas.py`).
   1. **Documento:** lo que es el papel.
   2. **Texto:** lo que está escrito, tal como está.
   3. **Afirmación:** quién dijo qué, a quién, en qué acto.
   4. **Reconstrucción:** lo que propone un investigador.
2. **Ningún valor de verdad en las capas 1–3.** Una resolución es una afirmación con fuerza institucional. Solo la capa 4 tiene creencias, y siempre con autor y fecha.
3. **Ninguna fusión en la capa 2.** Cada aparición escrita es un nodo. Las identidades son hipótesis de la capa 4, que pueden coexistir en competencia.
4. **Lo andino y lo procesal son datos (SKOS), no clases.** Ampliar el vocabulario no cambia el núcleo.
5. **Solo términos existentes en los estándares**, verificados en sus archivos (`vendor/`). OHAC no declara términos propios (§6).
6. **PROV-O solo para la procedencia del dato**, nunca para «quién lo dijo en 1806».
7. **Determinismo.** Del registro plano al grafo hay una función pura. Todo identificador se deriva del expediente, el tramo y el ordinal.

## 2. Grafos nombrados e identificadores

| Grafo | Capa | Contenido | Produce |
|---|---|---|---|
| `g:documento` | 1 | Jerarquía archivística, piezas, actuaciones, instanciaciones (original, transcripción, tramos, folios) | Curación humana (`datos/piezas.jsonl` + manifiesto) |
| `g:texto/<lote>` | 2 | Menciones (observaciones) + anclas `oa:` + participaciones en la actuación (PC14) | Extracción (LLM o anotador) |
| `g:afirmaciones/<lote>` | 3 | E13 + PC14 del afirmante + anclas `oa:` + hechos narrados (E89) | Extracción |
| `g:reconstruccion/R-x` | 4 | Una proposición del investigador: identidad, evento o ejercicio de cargo | Investigador |
| `g:argumentacion/R-x` | 4 | La inferencia (I5) y la creencia (I2) **sobre** `g:reconstruccion/R-x` | Investigador |
| `g:procedencia` | P | PROV-O de todos los grafos | Mapeo |

Identificadores:

* `https://w3id.org/laad/id/<expediente>/{pieza,actuacion,mencion,afirmacion,hecho,anotacion,transcripcion/<sha12>/<tramo>}/…`
* Las entidades reconstruidas (`id:persona/…`, `id:lugar/…`, `id:evento/…`, `id:ejercicio-cargo/…`) **no** llevan expediente, porque pueden reunir menciones de varios.

**Pendiente:** registrar el espacio `w3id.org/laad` (hoy es nominal).

## 3. Capa por capa

### 3.1 Capa 1 — documento (RiC-O 1.1 + CRM)

```text
Fondo Intendencia ─includesOrIncluded→ Sección Causas Criminales → Serie Cusco → Legajo 14 → Expediente 18 (rico:RecordSet + tipo)
Expediente ─includesOrIncluded→ Pieza P00…P31 (rico:Record ∧ crm:E31_Document; hasDocumentaryFormType act:*; directlyPrecedesInSequence)
Pieza ─hasOrHadInstantiation→ Tramo UTnn (rico:Instantiation, componente de la Transcripción sha256:…)
Transcripción ─isOrWasDerivedFromInstantiation→ Original (rico:Instantiation; imágenes no disponibles)
Tramo con marca explícita ─isOrWasDerivedFromInstantiation→ Folio N (rico:Instantiation, componente del Original)
Actuación (crm:E65_Creation) ─P94_has_created→ Pieza; P2_has_type act:* y fza:*; P4 → E52 con la fecha ESCRITA (E41)
```

* **Jerarquía.** Sigue al catálogo: Causas Criminales es una *sección* (K4). RiC-O no tiene sección ni legajo; se tipan con `doc:seccion` y `doc:legajo`.
* **Fecha.** La capa 1 solo guarda la fecha **tal como está escrita** (`rico:expressedDate`, E41). SHACL prohíbe `rico:normalizedDateValue`.
* **Material ajeno.** P32 (notario republicano) es una pieza sin `isOrWasIncludedIn`.

### 3.2 Capa 2 — menciones (PiCo / ROAR + Web Annotation)

* Una mención es `picom:PersonObservation` (personas) o `roar:LocationObservation` / `roar:Observation` (lugares, grupos, cosas). **No** se tipa como E21/E53/E74 (revisión I3).
* Su nombre literal va en `crm:P1_is_identified_by` → E41 (`P190`). La fuente se enlaza con `prov:hadPrimarySource` (PiCo) o `roar:documentedIn` (ROAR; defecto D1).
* Su ancla es una `oa:Annotation` con `TextQuoteSelector` y `TextPositionSelector` sobre el tramo.
* Si la mención tiene un papel en la actuación (firmante, receptor, declarante, testigo de asistencia…), el mapeo crea una `crm:PC14_carried_out_by` con `P14.1_in_the_role_of rol:*` en esa actuación. De ahí salen las facetas **«ante quién»** y **«quién firma»** de toda afirmación hecha en esa actuación.

### 3.3 Capa 3 — afirmaciones (patrón STAR sobre E13)

Una afirmación es un `crm:E13_Attribute_Assignment`:

| Faceta pedida | Dónde |
|---|---|
| Quién la hace | `P14_carried_out_by` + PC14 con rol de la rama `rol:afirmante` (mención de persona o grupo) |
| En qué actuación | `P9i_forms_part_of` → `E65_Creation`. De la actuación se toman: **tipo** (`act:*`), **fecha escrita**, **ante quién** (PC14 `rol:receptor`), **quién firma** (PC14 `rol:firmante`), **quién escribe** (PC14 `rol:redactor` si el documento lo dice; si se disputa, E13 `atr:redacto`) |
| Sobre qué | `P140_assigned_attribute_to` → mención, pieza o hecho narrado (`E89`) |
| Qué | `P177_assigned_property_of_type` → `atr:*` (lista cerrada) |
| Valor | `P141_assigned` → concepto admitido (`dct:conformsTo`), mención, pieza, hecho, `E33` (literal) o `E52` (tiempo literal) |
| Polaridad, fundamento, fuerza | `P2_has_type` → `pol:*`, `fun:*`, `fza:*` |
| Relación con otras afirmaciones | `P17_was_motivated_by` → E13 a la que responde (`anot:responde-a`) o mención de quien se lo dijo (`anot:segun-otro`) |
| Decisiones del anotador | `P2_has_type anot:*` + `P3_has_note` obligatoria |
| Cita | `oa:Annotation` → `oa:hasBody` E13 |

**Diferencias con STAR** (Andrews 2023; Andrews 2025, *Digital Medievalist* 18, doi:10.16995/dm.16708):

* STAR usa P17 para la fuente; aquí la fuente es la actuación (`P9i`) más el ancla `oa:`, y P17 queda para relaciones de discurso (capa 3) y premisas (capa 4).
* La formulación de 2025 de STAR ya usa P140, P177 y P141, igual que este modelo (la de 2023 no los nombraba).
* STAR toma la autoridad (P14) como quien respalda la afirmación; aquí P14 es quien la hace en 1806, y la autoridad del investigador vive solo en la capa 4.

#### 3.4 Fuerza institucional

La fuerza es un dato del tesauro: `act:x skos:related fza:y`, solo en conceptos hoja.

| Tipo de actuación | Fuerza | Comentario |
|---|---|---|
| certificación, declaración jurada, reconocimiento y ratificación | testimonial | — |
| petición | de parte | — |
| informe, oficio, carátula | informativa | El informe del subdelegado es informativo aunque lo emita una autoridad, y además es de una **parte interesada** |
| vista fiscal | dictaminadora | — |
| auto, auto cabeza de proceso, decreto | resolutiva | Obliga dentro del proceso; **no hace verdadero** lo resuelto |
| notificación, desglose | fedataria | — |

### 3.5 Capa 4 — reconstrucción del investigador

Cada reconstrucción es un **par de grafos**:

* **Proposición** (`g:reconstruccion/R-x`), que puede ser de tres tipos:
  * **Identidad:** `picom:PersonReconstruction ∧ E21` (o `roar:LocationReconstruction ∧ E53`, `roar:Reconstruction ∧ E74/E70`), derivada de menciones. Opcionalmente con identificador HGIS (`P48` → E42) y `rdfs:seeAlso` WHG.
  * **Evento:** `E5_Event`, derivado de hechos narrados.
  * **Ejercicio de cargo:** `E7_Activity` tipada con el cargo. El titular se enlaza por PC14 con el **cargo como rol**, la vigencia con `E52` (P82a/P82b) más una nota de cómo se sabe, el ámbito con `P7` o una nota, y las premisas con `prov:wasDerivedFrom` hacia E13.
* **Argumentación** (`g:argumentacion/R-x`): `I5_Inference_Making ∧ prov:Activity`, que lleva:
  * el autor (`P14`);
  * el argumento (`P3`);
  * las premisas E13 (`P17`);
  * la fecha (`P4`);
  * `J2_concluded_that` → `I2_Belief` (`J4_that` → el grafo de la proposición, `J5_holds_to_be` → literal de `cre:*`).

**Hipótesis en competencia.** Coexisten como reconstrucciones distintas, sin elegir una (p. ej. R-declarante-p19-es-martin «probable» frente a -es-mariano «posible»).

**Fechas normalizadas.** Son una reconstrucción más (R-fechas-normalizadas). `consultas/control_secuencia.rq` las contrasta con el orden físico y **señala** F1, F2, F5 y F6 sin corregirlas.

### 3.6 Capa P — procedencia del dato (PROV-O)

* Todo grafo es un `prov:Entity`, con `dct:type` igual a su capa.
* Los grafos de las capas 1–3 llevan `prov:wasGeneratedBy` → `prov:Activity`, que a su vez lleva:
  * `prov:used` → la transcripción (`dct:identifier "sha256:…"`);
  * `prov:qualifiedAssociation` → `prov:agent` (`prov:SoftwareAgent` o `prov:Person`) + `prov:hadPlan` (prompt o guía);
  * `prov:endedAtTime`.
* Los grafos de la capa 4 llevan `prov:wasAttributedTo` (autor) y `prov:generatedAtTime`.
* La validación humana es una `prov:Activity` que `prov:used` el grafo. Hoy **no hay ninguna**, y la PC20 lo dice.

## 4. Tesauro SKOS: lo andino y lo procesal como datos

* **Doce esquemas, 164 conceptos.** Ver `docs/C_correspondencias.md` §T. El tesauro **nunca** se usa como clase: SHACL `ConceptoNoInstanciadoForma`.
* **Ayllu.** Es un *grupo* (`roar:Observation` / `E74`, `P2_has_type ent:ayllu`). Si hace falta su territorio, este se modela como lugar aparte.
* **Condiciones y cargos.** Originario, forastero, tributario, reservado; cacique, recaudador de tributos, segunda, alcalde, principal. Son **atribuciones de alguien** (`atr:tiene-condicion`, `atr:ejerce-cargo`) y solo se vuelven rasgos de una persona en una reconstrucción de capa 4 con creencia.
* **Rarezas conservadas sin asimilar.**
  * «India Ordinaria» → `cond:ordinario` con nota, **no** = originario.
  * «Sanbo» → `cond:zambo`.
  * «Gobernador» (UT12.a) → `cargo:gobernador` con nota de referente dudoso.
* **Definiciones de trabajo.** Las escribió el modelador. Unos 100 conceptos aún no tienen `skos:definition`, y todos deben revisarlos historiadores (`skos:editorialNote`).

## 5. Formas SHACL (perfil)

Hay 16 formas con nombre, y cada una tiene al menos una prueba negativa (`tests/test_formas_negativas.py`).

| Forma | Hace cumplir |
|---|---|
| PiezaForma | Título, tramos, un tipo de actuación del tesauro **con fuerza** (no abstracto) |
| ActuacionForma | Crea una pieza; exactamente un tipo y una fuerza |
| FechaEscritaForma | Solo fecha escrita en la capa 1 |
| ObservacionForma | Fuente (PiCo o ROAR), nombre literal, ancla; sin `wasDerivedFrom` ni `sameAs` |
| ApelacionForma, ValorLiteralForma | Contenido simbólico presente |
| AnotacionForma, ObjetivoForma | Un cuerpo; tramo; selector de cita exacta y de posición |
| ParticipacionForma | El rol va en PC14 y pertenece a `tes:roles` (o a `tes:cargos` para el ejercicio de un cargo) |
| AfirmacionForma | Un afirmante con rol de la rama afirmante; una actuación, un sujeto, un atributo de la lista cerrada y un valor; una polaridad, un fundamento y una fuerza; ancla; **sin `J5` ni `J2`** (sin verdad); nota obligatoria en las decisiones del anotador |
| ConceptoNoInstanciadoForma | Ningún concepto como clase, agente o sujeto |
| ReconstruccionForma, CargoForma, InferenciaForma, CreenciaForma | La capa 4 lleva derivación, inferencia con autor, argumento y fecha, y creencia de la lista |
| LoteConProcedenciaForma | Los grafos de las capas 1–3 tienen actividad, agente, plan y transcripción; los de la capa 4, autor y fecha |

## 6. Análisis de carencias: qué contiene OHAC

Para cada necesidad se buscó primero en los estándares. Solo se añadiría a OHAC lo que no existiera.

| Necesidad | ¿Existe? | Término | ¿En OHAC? |
|---|---|---|---|
| Sección y legajo como niveles de descripción | No en el vocabulario de RiC-O | `rico:RecordSet` + concepto SKOS `doc:seccion` / `doc:legajo` | No (dato) |
| Folio, recto/vuelto | No en RiC-O | `rico:Instantiation` + `dct:type doc:folio` / `doc:recto` | No (dato) |
| Tramo de transcripción | Sí (genérico) | `rico:Instantiation` componente | No |
| Afirmación con actor, actuación y tiempo | Sí | `crm:E13` | No |
| Rol de alguien en una actuación | Sí | `crm:PC14` + `P14.1` | No |
| Ante quién / quién escribe / quién firma | Sí, como roles | PC14 + `rol:*` | No (dato) |
| Polaridad (afirma/niega) | No hay propiedad específica en CRM | `crm:P2_has_type pol:*` | No (dato) |
| Fundamento de conocimiento del testigo | No hay propiedad específica | `crm:P2_has_type fun:*` | No (dato) |
| Fuerza institucional | No | `crm:P2_has_type fza:*` | No (dato) |
| Relación «responde a» entre afirmaciones | Sí, genérica | `crm:P17_was_motivated_by` | No |
| Mención tal como está escrita | Sí | PiCo / ROAR | No |
| Ancla textual exacta | Sí | Web Annotation | No |
| Creencia del investigador | Sí | CRMinf | No |
| Procedencia del dato | Sí | PROV-O | No |
| Ejercicio de cargo con vigencia | Sí | `crm:E7` + PC14 + E52 | No |
| Identificador HGIS | Sí | `crm:P48` + `E42` | No |

**Conclusión verificable.** OHAC declara **cero** clases y **cero** propiedades:

* `tests/test_terminos_existen.py` comprueba que toda IRI usada de los estándares existe en `vendor/`.
* La prueba del expediente sintético comprueba que un pleito civil no introduce clases ni propiedades nuevas.

Lo que podría reclamarse como «extensión» (polaridad, fundamento, fuerza, roles procesales) son **conceptos** del tesauro usados con propiedades genéricas de CRM. Es la solución que CRM prescribe con E55 Type para la especialización local.

**Coste de esta decisión.** La semántica de la polaridad y de la fuerza no la «entiende» un consumidor CRM genérico que ignore `P2_has_type` (§8, L5).

## 7. Defectos y carencias encontrados en los estándares

Son defectos de interoperabilidad, documentados para comunicarlos a sus mantenedores.

| Id | Estándar | Defecto | Efecto | Cómo se trató |
|---|---|---|---|---|
| D1 | ROAR 0.1 | `prov:wasDerivedFrom rdfs:domain roar:Reconstruction` es un dominio global sobre una propiedad de PROV. Como `prov:hadPrimarySource ⊑ prov:wasDerivedFrom` y `roar:Observation ⊓ roar:Reconstruction = ∅`, el patrón de PiCo (observación + `hadPrimarySource`) aplicado a una observación ROAR es **inconsistente** | El razonador OWL RL detectó 1 inconsistencia (M-UT01-007). Tras la corrección quedan 0, más 59 tipificaciones espurias de observaciones PiCo como `roar:Reconstruction` en el modelo revisado | Las observaciones ROAR usan `roar:documentedIn`; `scripts/razonar.py` informa de las espurias en cada ejecución |
| D2 | PiCo 1.1.0 | `pico.ttl` declara `picot_roles: <…/roles/>`, pero los conceptos publicados usan `…/ThesaurusHistorischePersoonsgegevens/NNN`. Además, `prov:wasAssociatedWith` aparece como `owl:DatatypeProperty` | Las alineaciones podrían apuntar a IRIs que no resuelven | Se usa la IRI del concepto publicado (`ohac.ttl`) |
| D3 | CRMinf 1.2.1 | `J2_concluded_that` es subpropiedad de P175, P175i y P185 | Una inferencia RDFS ingenua añadiría relaciones temporales | No se hace inferencia RDFS para SHACL (solo jerarquía de clases) |
| D4 | CRMinf 1.2.1 | `I6_Belief_Value` no está declarada como clase y el rango de J5 es un literal; `J6_adopted` solo aparece en una fórmula (errata) | Los valores de creencia no pueden ser conceptos | Literal de J5 = `skos:notation` de `cre:*` + `sh:in` |
| D5 | RiC-O 1.1 | Expresa la *extensión* en folios (`rico:CarrierExtent` + `rico:quantity` + `rico:hasUnitOfMeasurement`), pero no el folio individual direccionable, ni recto y verso, ni los niveles *sección* y *legajo* de la tradición hispana; DocumentaryFormTypes no incluye tipos judiciales | — | Extensión con `rico:CarrierExtent` (19 folios según el catálogo, contrastado: K5); folio, sección y legajo como conceptos SKOS con propiedades de RiC-O |
| D6 | CRMinf 1.2.1 | Declara `crm:E13_Attribute_Assignment ⊑ crminf:I1_Argumentation`, cuya nota de alcance define I1 como «honest inferences or observations» (el actor cree correcto el valor resultante). Además ofrece `J33_assigned_propositions` como atajo cuya ruta completa termina en `J5 = TRUE`; el atajo no se impone a ninguna E13, pero documenta la misma lectura | Cargado CRMinf, toda afirmación de la capa 3 hereda por la jerarquía una **presunción de sinceridad** del testigo. En un pleito con retractación jurada y firmas «sin saber sus contenidos» (informe del subdelegado, A-UT17-111…114) eso es un juicio histórico, no un dato | Se documenta, no se corrige: la E13 de la capa 3 se interpreta como **afirmación profesada en el registro**. `scripts/razonar.py` cuenta las E13 inferidas I1 (74) y las negaciones afectadas (12). ADR-021 |
| D7 | CIDOC CRM 7.1.3 + PiCo 1.1.0 | `P14_carried_out_by` tiene rango `E39_Actor`, de modo que toda mención que afirma se infiere `E39_Actor`; y `picom:PersonObservation ⊑ picom:Person ⊑ pnv:Person` | La capa 2 no afirma existencia por tipado propio (no se usa E21), pero la inferencia sí tipa como actores a las menciones afirmantes, incluido el certificante del que el juez dice «no hay tal hombre» | Se interpreta según la nota de alcance de PiCo: la observación es «how a person is recorded on a Source»; `E39` inferido = actor **tal como consta en la fuente**. La existencia e identidad solo se proponen en la capa 4. ADR-026 |

## 8. Límites conocidos y trabajo pendiente

**Hay que resolver antes de extraer el expediente completo:**

* **L1. Folio y recto/vuelto** de 19 de los 23 tramos: requiere las imágenes (`fuente/folios_cotejo.csv`). Las autorreferencias del documento («De folio 4», «a folios 2») ya están como afirmaciones (PC02) y permitirían reconstruir la foliación en la capa 4.
* **L2. Normalización de valores literales** («dies» / «diez»; horas compatibles como «a media noche» y «primer puesto del gallo»). Hoy la consulta de disputas los **señala** («valores distintos (revisar)») y no los juzga. Las negaciones explícitas se detectan por `responde_a`, no por el texto. Una normalización de capa 4 con autor resolvería el resto.
* **L3. Identidad entre expedientes.** Las reconstrucciones se mapean con el lote de un expediente. Para unir menciones de dos expedientes, los ids de mención deben calificarse con el expediente (`cc-14-18:M-UT01-001`). El IRI ya lo permite; falta el cargador.
* **L4. Discurso referido de segundo grado.** «Cano dice que Santiago le dijo X» se modela con `segun` + `fun:oidas`. La alternativa más fiel, un E13 anidado («Santiago afirmó X», atribuido por Cano), queda sin implementar.

**Decisiones de modelado con coste explícito:**

* **L5. Negación.** Va como `P2_has_type pol:niega` del E13 (agravado por D6). Un consumidor CRM que ignore P2 leería «asignó coronel». Mitigación: toda respuesta y toda consulta exige la polaridad (SHACL), y el compositor marca [NIEGA]. Alternativa evaluada y descartada por ahora: modelar el rechazo como creencia del testigo (CRMinf I2 con J5 «falso»), que exigiría CRMinf en la capa 3.
* **L6. Decisiones del anotador dentro de la capa 3.** Sujeto elíptico resuelto a una mención de otra pieza, afirmante tomado de otra pieza, afirmaciones colectivas distribuidas. Van marcadas (`anot:*`), con nota obligatoria y con la autoría del lote (PROV). No llevan creencia propia. Si el estándar de oro muestra desacuerdo frecuente en ellas, deberán pasar a la capa 4.
* **L7. Hechos narrados por pieza** (E89). Exigen una reconstrucción de evento para comparar relatos entre piezas. Es deliberado, pero las disputas sobre hechos dependen de que exista esa reconstrucción.

**Cobertura pendiente:**

* **L8. Anotación.** Expediente completo anotado (544 menciones, 500 afirmaciones; ADR-030), por el modelo y sin validación humana; las lecturas dudosas constan en la `nota` de cada registro. PC03 y PC04 se responden según el catálogo (capa C, ADR-033).
* **L9. Tesauro.** Los 164 conceptos tienen definición (ADR-032); 22 son definiciones de trabajo sin fuente verificada y todas deben validarlas historiadores.
* **L10. Rendimiento.** RDF genera unas 25 tripletas por afirmación. El razonador tarda unos 79 s y lleva el grafo de 5,5 k a unas 103 k tripletas (30 k con los estándares). Asumible a escala de expediente; para la serie completa habrá que medirlo.

## 9. Decisión: RDF nativo frente a grafo de propiedades

**Decisión: RDF nativo (TriG con grafos nombrados), más una vista aplanada documentada para el agente o un grafo de propiedades si se necesita.**

| Criterio | RDF nativo | Grafo de propiedades (Neo4j u otro) |
|---|---|---|
| Uso real de los estándares | IRIs de RiC-O, CRM, CRMinf, PROV y PiCo **son** los datos; se prueban contra `vendor/` | Etiquetas y tipos de relación libres: es justo el fallo 1.6 del intento previo |
| Separación de capas | Grafos nombrados con procedencia propia por capa (PROV sobre el grafo) | Propiedades o etiquetas de capa en cada nodo; la procedencia se repite por nodo |
| Reificación (E13, PC14) | Nativa en CRM: nodos | Natural: atributos en aristas. **Ventaja del grafo de propiedades** |
| Validación | SHACL estándar + razonador OWL RL | Restricciones propias o un esquema ad hoc |
| Consulta | SPARQL (verboso; ~2 s por consulta en rdflib) | Cypher (más legible) |
| Enlace externo (HGIS, WHG, PiCo) | IRIs y alineaciones SKOS | Cadenas |
| Intercambio con archivos | RiC-O es el formato de intercambio de la ICA | Requiere exportar |

**Mapeo documentado RDF → grafo de propiedades** (para una vista de lectura, no como fuente de verdad):

* `E13` → nodo `:Afirmacion {id, atributo, polaridad, fundamento, fuerza, cita, tramo, folio}`.
* `(:Mencion)-[:AFIRMA {rol}]->(:Afirmacion)`, desde PC14.
* `(:Afirmacion)-[:SOBRE]->(sujeto)`, `-[:VALOR]->(valor)`, `-[:EN_ACTUACION]->(:Actuacion {tipo, fecha_escrita})`.
* `(:Actuacion)-[:PARTICIPA {rol}]->(:Mencion)`, desde PC14.
* `(:Reconstruccion {creencia, autor, fecha, argumento})-[:DERIVA_DE]->(:Mencion)`.
* La capa va como etiqueta del nodo. La procedencia, como propiedades del nodo `:Lote`.

Esta vista **se genera** desde el TriG y nunca se edita.

## 10. Revisión independiente y respuesta

Un revisor sin acceso a `docs/` leyó el código, los datos y los estándares. Sus hallazgos y lo hecho con cada uno (commit `953a55f`):

| Hallazgo | Gravedad | Acción | Estado |
|---|---|---|---|
| C1 Cargos con vigencia no implementados | Crítico | Registro `cargo` → E7 + PC14 (cargo como rol) + E52; `CargoForma`; PC18 | Resuelto |
| C2 Supuestos de un solo expediente (prefijo, jerarquía, transcripción, marcas, `FUERZA` en código, sin «cosa», afirmante solo persona, valores solo cargo y condición) | Crítico | Manifiesto por expediente + variable de contexto; fuerza en el tesauro; clase `cosa`; afirmante grupo; `dct:conformsTo`; prueba con expediente civil sintético | Resuelto (salvo L3) |
| C3 Faltaban «quién escribe» y el discurso referido | Crítico | `redactorDoc` + `redaccionDisputada` en la consulta; `segun` → P17 | Resuelto (L4 pendiente) |
| I1 Disputas por comparación literal; filas duplicadas | Importante | `responde_a`; «valores distintos (revisar)»; consulta sin duplicados (74 filas para 74 afirmaciones) | Resuelto (L2 pendiente) |
| I2 Decisiones de la capa 4 dentro de la capa 3 | Importante | Marcas `anot:*` + nota obligatoria (SHACL) | Mitigado (L6) |
| I3 La capa 2 afirmaba existencia (E21) | Importante | Las menciones son solo observaciones PiCo/ROAR | Resuelto |
| I4 Creencia dentro de la proposición que evalúa | Importante | Grafo de argumentación propio; I5 también `prov:Activity` | Resuelto |
| I5 Negación en P2 | Importante | Documentada (L5); SHACL exige polaridad; el compositor marca [NIEGA] | Aceptado con mitigación |
| I6 Folio | Importante | Autorreferencias como afirmaciones (PC02) | Parcial (L1) |
| I7 Fórmulas procesales | Importante | Atributos de juramento, generales de la ley, firma a ruego y folio de pieza; dirección de «se conforma con» y destinatario de la orden corregidos; doble negación corregida | Resuelto |
| I8 Lugares | Importante | Sicuani, Cusco, San Pedro (posible) y ayllus Tinta y Uchu; HGIS como E42 | Resuelto |
| Menor: hechos como E5 | Menor | E89 + P70 | Resuelto |
| Menor: atributos sin raíz, creencias sin uso | Menor | `topConceptOf` y `skos:notation` | Resuelto |
| Menor: definiciones faltantes | Menor | — | Resuelto: 164/164 (ADR-032; 22 de trabajo) |
