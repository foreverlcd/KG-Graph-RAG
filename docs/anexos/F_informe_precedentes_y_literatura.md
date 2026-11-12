# Precedentes, literatura y fuentes de contraste — expediente ARC, Intendencia, Causas Criminales, Leg. 14, Exp. 18 (1806)

Fecha de la búsqueda: 2026-11-12. Cómo se verificó: cada URL se abrió con `curl` (HTTP 200) o con lectura directa. Cada DOI se resolvió en `doi.org/api/handles` y se cotejó con Crossref (título, autores, año). En los PDF de artículos y ontologías se extrajo el texto y se buscaron dentro las clases, propiedades y cifras citadas. Lo que no se pudo comprobar así lleva la marca **NO VERIFICADO**.

---

## (1) PRECEDENTES (8 elegidos)

Criterio: parecido del *problema* (afirmaciones atribuidas o en conflicto, procedencia archivística, grafías inestables, archivo colonial hispano), no del dominio.

### 1. Factoid prosopography / Factoid Prosopography Ontology (FPO)
- **Institución:** King's College London, Department of Digital Humanities (J. Bradley, M. Pasin, H. Short). Lo usan PoMS (https://www.poms.ac.uk/) y PASE (https://pase.ac.uk/), entre otros.
- **Por qué se parece:** el *factoid* es justamente "la fuente S dice, en tal lugar, que la persona referida como X hizo o fue Y". No es un hecho del mundo, sino una aserción anclada a la fuente. Es nuestra capa 3 en versión mínima.
- **Patrón que copiamos** (términos comprobados en `fpo.owl`):
  - `fpo:Factoid rdfs:subClassOf fpo:Assertion`, unido a la fuente por `fpo:sourcedFrom` → `fpo:Source`.
  - `fpo:PersonReference` (la mención), con `fpo:hasNameInSourceAs` (grafía literal) y `fpo:hasPlaceInSource` (folio o lugar).
  - `fpo:referencesPerson` (enlace mención → persona).
  - `fpo:hasDateAssertionMade` / `fpo:dateAsserted` (cuándo se hizo la aserción, distinto de cuándo ocurrió lo aseverado: `fpo:dateForAssertion`).
  - En nuestro esquema plano, cada "registro de afirmación" funciona como un factoid. Las columnas `nombre_tal_como_aparece` y `folio` salen de `hasNameInSourceAs` y `hasPlaceInSource`.
- **Enlaces:**
  - Ontología: https://github.com/johnBradley501/FPO (archivo `fpo.owl`).
  - Página KCL: https://www.kcl.ac.uk/factoid-prosopography/ontology
  - Artículo: Pasin & Bradley, *Digital Scholarship in the Humanities* (2013/2015), DOI 10.1093/llc/fqt037 (resuelve).
- **Lo que no nos sirve:**
  - La propia KCL presenta la FPO como trabajo en curso, ligero y sin alinear con CIDOC CRM.
  - El factoid trata la fuente como el único aseverador. No separa quién declara, ante quién, quién escribe y quién firma, que es nuestro núcleo (certificación de agosto frente a retractación jurada de septiembre).
  - No tiene tipos de actuación procesal.

### 2. Persons in Context (PiCo)
- **Institución:** CBG Centrum voor familiegeschiedenis (Países Bajos). Woltjer et al. 2024, *Historical Life Course Studies* 14:105–125, DOI 10.51964/hlcs19312 (resuelve).
- **Por qué se parece:** separa formalmente la persona "tal como aparece en la fuente" de la persona reconstruida por el investigador. Es nuestra separación entre capa 2 y capa 4, y su nota de alcance exige conservar la grafía del registro.
- **Patrón que copiamos** (comprobado en `pico.ttl`, v1.1.0):
  - `picom:PersonObservation`: "must always be related to a source", con `prov:hadPrimarySource` → `sdo:ArchiveComponent`. Los valores se registran "with the age, occupation, and spelling of the person's name recorded as in the record".
  - Las fechas llevan doble literal: la cadena original (`"21 Junij 1858"^^xsd:string`) y la forma ISO (`"1858-06-21"^^xsd:date`).
  - `picom:hasRole` → tesauro de roles.
  - `picom:PersonReconstruction`, unida por `prov:wasDerivedFrom` a una o más observaciones y por `prov:wasGeneratedBy` a una `prov:Activity` con `prov:wasAssociatedWith` (quién reconstruyó) y fechas.
  - Uso para nosotros: una observación por cada aparición de "Guancachoque", "Huancachoque" o "Mancachoque", y una sola reconstrucción derivada de todas.
- **Enlaces:**
  - Repositorio: https://github.com/CBG-Centrum-voor-familiegeschiedenis/PiCo
  - TTL: https://raw.githubusercontent.com/CBG-Centrum-voor-familiegeschiedenis/PiCo/refs/heads/main/pico.ttl
  - Web: https://personsincontext.org/
- **Lo que no nos sirve:**
  - Se apoya en schema.org (`sdo:`), no en CIDOC CRM. Habría que traducir las clases, no importarlas.
  - Está pensado para registros civiles neerlandeses (una persona, un rol por acta). No modela actos de habla, testimonios ni contradicciones.
  - El tesauro de roles no tiene "cacique recaudador", "subdelegado" ni "testigo retractante".

### 3. ROAR — Reconstructions and Observations in Archival Resources (Golden Agents)
- **Institución:** L. van Wissen y M. den Engelse, en el proyecto Golden Agents (Ámsterdam: actas notariales y registros del Stadsarchief Amsterdam).
  - El pipeline SAA de Golden Agents dice convertir los datos "into Linked Open Data … in the Golden Agents Archival Ontology ROAR++" (Zenodo, DOI 10.5281/zenodo.7669368, resuelve).
  - Contexto del pipeline sobre actas notariales: van Wissen et al. 2020, DOI 10.5281/zenodo.3862817 (resuelve).
- **Por qué se parece:** es el antecedente directo de PiCo, pero general (personas, lugares y otras entidades). Su comentario de ontología dice expresamente que la reconstrucción combina información "complementary (or sometimes conflicting)" de varias observaciones.
- **Patrón que copiamos** (comprobado en `roar.ttl`):
  - Superclases `roar:Observation` y `roar:Reconstruction`, con `roar:LocationObservation` y `roar:LocationReconstruction`. Sirven para "Tinta", "pueblo de Tinta" y "provincia de Tinta".
  - `roar:documentedIn` → `roar:Document`.
  - `roar:locationInDocument` y `roar:onScan` (puntero al folio o imagen).
  - `roar:hasPerson` con valor estructurado `[ rdf:value …; roar:role "…" ]`.
  - Para documentar cómo se hizo la reconstrucción (actividad, agente, plan): `prov:qualifiedDerivation`.
- **Enlaces:**
  - Documentación: https://w3id.org/roar
  - Repositorio: https://github.com/LvanWissen/roar (`roar.ttl`)
- **Lo que no nos sirve:**
  - Es la versión 0.1 y los roles son literales de cadena.
  - Usa SEM (`sem:`) para los eventos, que en nuestro diseño cubre CIDOC CRM.
  - ROAR++ (la variante de Golden Agents) no tiene documentación de esquema publicada que yo haya podido abrir (**NO VERIFICADO** el detalle de ROAR++).

### 4. Enslaved.org Ontology
- **Institución:** Michigan State University, con Kansas State y Wright State (Shimizu, Hitzler et al.). *Journal of Web Semantics* 2020, DOI 10.1016/j.websem.2020.100567 (resuelve).
- **Por qué se parece:** agrega personas atestiguadas en fuentes heterogéneas, con nombres inestables y sin identidad garantizada entre fuentes. Cada atributo lleva su procedencia.
- **Patrón que copiamos** (comprobado en `enslaved-v2.owl`):
  - **Reificación por atributo.** `NameRecord`, `ParticipantRoleRecord`, `OccupationRecord`, `PersonStatusRecord`, `AgeRecord`… son subclases de `AgentRecord`, que a su vez es `rdfs:subClassOf EntityWithProvenance`.
  - `AgentRecord` tiene `recordedAt` (máx. 1) hacia un `Event`, es decir, el acto de registro.
  - Para nombres: `hasNameVariant` y `hasPreferredNameVariant`.
  - Para la conciliación entre registros: `Match`, subclase de `EntityWithProvenance`, con `matches` y exactamente un `hasMatchType`.
  - Lo que importamos es la idea de que el enlace de identidad ("Chuquitapa ≡ Choquitapa") es una entidad con tipo y procedencia, no un `owl:sameAs` desnudo.
- **Enlaces:**
  - https://docs.enslaved.org/ontology/ (OWL v2: https://docs.enslaved.org/ontology/v2/enslaved-v2.owl)
  - PDF de documentación: https://docs.enslaved.org/ontology/v2/Enslaved_Documentation_V2_0-2.pdf
- **Lo que no nos sirve:**
  - Su vocabulario es propio (no CRM).
  - Está orientado a agregar bases de datos ya estructuradas, no a extraer de un expediente.
  - No modela testimonio ni juramento, y "recordedAt" no distingue escribano de declarante.

### 5. Wikidata / Wikibase (statement + qualifiers + references + rank)
- **Institución:** Wikimedia Foundation. Modelo: https://www.mediawiki.org/wiki/Wikibase/DataModel. Ayuda: https://www.wikidata.org/wiki/Help:Sources, https://www.wikidata.org/wiki/Help:Qualifiers, https://www.wikidata.org/wiki/Help:Ranking
- **Por qué se parece:** es el patrón más difundido de "afirmación con fuente, cita y matiz". Admite afirmaciones contradictorias coexistentes y las ordena con rangos, en lugar de borrarlas.
- **Patrón que copiamos** (etiquetas comprobadas por la API de Wikidata). Sirve como lista de control de los campos del registro plano:
  - `P248` *stated in* → `documento`.
  - `P958` *section* → `folio`.
  - `P1683` *quotation* ("quotation supporting the statement claim") → nuestra **cita literal obligatoria**.
  - `P1810` *subject named as* y `P1932` *object of statement named as* → grafía tal como aparece.
  - `P5102` *nature of statement* y `P1480` *sourcing circumstances* → modalidad (afirma, niega, matiza, "dice no saber").
  - Rangos *preferred*, *normal* y *deprecated*, con `P2241` *reason for deprecated rank* y `P7452` *reason for preferred rank* → valoración del investigador (capa 4), nunca de la capa 3.
- **Enlaces:**
  - https://www.wikidata.org/wiki/Property:P1683
  - https://www.wikidata.org/wiki/Property:P1932
- **Lo que no nos sirve:**
  - La reificación RDF de Wikibase (`wds:`, `pq:`, `pr:`) no es CIDOC CRM.
  - El "quién asevera" se reduce a la referencia; no hay roles de ante quién ni de quién firma.
  - Wikidata no admite investigación original, así que no es un repositorio para nuestros datos.

### 6. CRMinf (CIDOC CRM SIG), implementado en ResearchSpace (British Museum)
- **Institución:** CIDOC CRM SIG. La versión actual de CRMinf es la 1.2.1, publicada en abril de 2026: https://cidoc-crm.org/crminf/ModelVersion/crminf-1.2.1. ResearchSpace (Trustees of the British Museum): https://github.com/researchspace/researchspace
- **Por qué se parece:** modela creencias, observaciones e inferencias atribuidas a actores. Es lo que necesita nuestra capa 4 para decir "el investigador cree, con valor V, que Chuquitapa = Choquitapa" o "que la retractación es parcial".
- **Patrón que copiamos.** Comprobado en el código de ResearchSpace (`src/main/web/data/vocabularies/crminf.ts`, `components/arguments/AssertionsStore.ts`, `BeliefsUtil.ts`):
  - `crminf:I2_Belief` con `crminf:J4_that` → `crminf:I4_Proposition_Set` y `crminf:J5_holds_to_be` (valor de creencia).
  - `crminf:I1_Argumentation` / `I5_Inference_Making` con `J2_concluded_that` y `J1_used_as_premise`.
  - La "aserción" de ResearchSpace (`rso:EX_Assertion`) lleva `rso:targetsRecord`, `rso:targetsField` y `rso:PX_asserts` → `I2_Belief`, más `crm:P14_carried_out_by`, `crm:P4_has_time_span` y `crm:P70i_is_documented_in`.
  - Patrón a copiar: la capa 4 apunta a registros o campos de capas inferiores y nunca los sobrescribe.
- **Lo que no nos sirve:**
  - ResearchSpace es una plataforma pesada (Java y triplestore), así que solo copiamos el patrón.
  - El propio código anota que `J6_adopted` está "deprecated in the latest CRMinf version". Conviene seguir la 1.2.1, no el código.
  - Para las declaraciones de los testigos (capa 3) basta `E13 Attribute Assignment` de CRM base. CRMinf queda reservado al investigador.

### 7. RiC-O (Records in Contexts, ICA-EGAD), con su implementación en los Archives nationales de France (PIAAF → RiC-O Converter)
- **Institución:** ICA Expert Group on Archival Description; Archives nationales de France.
  - PIAAF: "the first RiC-based proof of concept" (Clavaud 2019, HAL: https://hal-enc.archives-ouvertes.fr/hal-03958855).
  - Herramienta posterior: https://github.com/ArchivesNationalesFR/rico-converter
- **Por qué se parece:** es nuestra capa 1 (fondo → serie → legajo → expediente → foja o pieza documental), con tipos documentales y autoría.
- **Patrón que copiamos** (comprobado en `RiC-O_1-1.rdf`):
  - `rico:RecordSet` (Fondo Intendencia / Causas Criminales / Leg. 14), unido por `rico:includesOrIncluded` a `rico:Record` (Exp. 18).
  - `rico:hasOrHadConstituent` → `rico:RecordPart` para cada pieza: certificación de agosto, declaraciones de septiembre, informe del cura, informe del subdelegado, vista fiscal, auto de la Audiencia.
  - `rico:hasDocumentaryFormType` → `rico:DocumentaryFormType`.
  - `rico:hasCreator`, `rico:hasAuthor`, `rico:hasAddressee`, `rico:hasSender`.
  - `rico:hasOrHadInstantiation` → `rico:Instantiation` (transcripción paleográfica, imagen).
- **Enlace:** https://github.com/ICA-EGAD/RiC-O (`ontology/current-version/RiC-O_1-1.rdf`)
- **Lo que no nos sirve:**
  - RiC-O no modela el contenido aseverado. Tiene además agentes y eventos propios que duplicarían a CRM.
  - Hay que limitarlo a la capa 1 y enlazar con CRM solo a través del documento (`rico:Record` ↔ `crm:E31 Document`). **NO VERIFICADO:** existe un alineamiento oficial RiC-O↔CRM.

### 8. HGIS de las Indias + World Historical Gazetteer (Linked Places Format)
- **Institución:** HGIS de las Indias (W. Stangl, Austrian Academy of Sciences). Sus datos están en Dataverse:
  - Territorial: DOI 10.7910/DVN/YPEU5E (resuelve).
  - Lugares poblados, 1701–1808: DOI 10.7910/DVN/FUSJD3 (resuelve).
  - Dataset en WHG: https://whgazetteer.org/datasets/15/places
- **Por qué se parece:** es geografía administrativa borbónica (intendencia del Cuzco, partido de Tinta o Canas y Canchis) con validez temporal y variantes de nombre. Es el único precedente elegido que es colonial hispanoamericano y está en datos enlazados.
- **Patrón que copiamos** (comprobado en el README de LPF): en Linked Places Format, cada variante de nombre es un objeto propio `{"toponym": …, "citations": [...], "when": {"timespans": [...]}}`. Es decir, cada grafía lleva su propia cita y su tiempo, que es el mismo principio que aplicamos a los antropónimos.
- **Enlace al modelo:** https://github.com/LinkedPasts/linked-places-format
- **Lo que no nos sirve:**
  - Es GeoJSON-LD y no CRM.
  - No cubre personas.
  - **NO VERIFICADO:** que el pueblo de Tinta y sus ayllus tengan entrada propia en el dataset (no consulté registros concretos; la API de WHG no respondió).

### Evaluados y descartados (una línea)
- **Digital Panopticon / Old Bailey:** record linkage de procesados (nombre con tolerancia, Soundex, Levenshtein y fecha de condena; blog https://blog.digitalpanopticon.org/adventures-with-data-linkage/). Útil como heurística, pero no encontré un modelo de datos RDF publicado.
- **Candela et al. 2023**, "An Ontological Approach for Unlocking the Colonial Archive", *JOCCH* 16(4), DOI 10.1145/3594727 (resuelve). Trata colonial hispano (Relaciones Geográficas), pero a nivel de metadatos de colección; CIDOC CRM solo aparece en el estado de la cuestión. Repositorio: https://github.com/hibernator11/UCA-relacionesgeograficas
- **Early Modern Inquisition Database:** no resolvió (https://emid.h.uib.no dio error de conexión). **NO VERIFICADO**.
- **DPRR, SNAP:DRGN, SAMPO/WarSampo, Mapping the Republic of Letters, Slave Societies Digital Archive:** son redundantes con FPO o PiCo, o no tratan afirmaciones atribuidas. No los abrí en detalle.
- **GitHub `ianlw/Grafo-Conocimiento-Cusco`:** describe este mismo expediente. No es un precedente independiente; parece el propio proyecto o uno derivado.

---

## (2) LITERATURA RECIENTE (2023–2026) — LLM hacia CIDOC CRM o grafos de patrimonio

Resumen de la evidencia:
- Ningún artículo compara cabeza a cabeza, sobre el mismo corpus, "tripletas CRM directas" frente a "esquema intermedio + mapeo determinista".
- La evidencia indirecta sí converge en tres puntos:
  - (a) las restricciones solo en el prompt no garantizan validez ontológica;
  - (b) donde hay validez alta, el LLM rellena JSON o tablas y la elevación a RDF es declarativa;
  - (c) la cita literal se valida con un comprobador determinista de subcadena, y esa comprobación no prueba que la cita *apoye* el valor.

### A. Los más pertinentes

**1. Montenegro, G.; Billami, M. B.; Faron, C.; Gandon, F.; Monnin, P. (2026).** "LLM-Assisted Ontology Engineering and Construction of a French Legal Knowledge Graph". arXiv:2607.24551 (figura como SEMANTiCS 2026). https://arxiv.org/abs/2607.24551 (resuelve).
- **Qué hicieron:** extracción cerrada de tripletas guiada por firmas de propiedades. Las restricciones van solo en el prompt ("not enforced through a formal validation or repair loop"). Las salidas se organizan en "intermediate tabular representations … then lifted to RDF using declarative RML mappings". Usan Web Annotation para unir menciones con su evidencia textual.
- **Cifras** (Tabla 3, GPT-4.1 y mistral-large-2512, con y sin fusión):

  | Métrica | Rango |
  |---|---|
  | R_JSON | 100,00 % |
  | R_class | 99,97–99,99 % |
  | R_prop | 81,52–96,42 % |
  | R_sig (dominio–rango exacto) | 49,86–72,61 % |

  "Fewer than 20% of triples introduce previously unseen properties".
- **Relación con nuestra decisión: la apoya con fuerza.** El JSON siempre fue válido, pero las firmas dominio–rango fallaron entre el 27 % y el 50 % cuando la ontología solo se pedía en el prompt. Un esquema cerrado más un mapeo determinista elimina por construcción ese tipo de error. Además, su patrón intermedio (tabla → RML) es el nuestro.

**2. Marketakis, Y.; Lintanff-Castel, M.; Tzitzikas, Y. (2026).** "On the Use of Large Language Models for Schema Mapping Generation in Ontology-Based Data Integration". *Proc. 14th EETN Conference on AI (SETN 2026)*, ACM (el DOI aparece como marcador "XXXXXXX" en el preprint). https://users.ics.forth.gr/~tzitzik/publications/Tzitzikas-2026-MappingSETN.pdf (resuelve).
- **Complemento:** Marketakis & Tzitzikas (2026), "Beyond Prompt-to-RDF: A Vision for Scalable and Explainable Graph Transformations via LLM-assisted Schema Mappings", EDBT/ICDT 2026 Workshops, CEUR-WS Vol-4192. https://ceur-ws.org/Vol-4192/TGD-paper3.pdf (resuelve).
- **Qué hicieron:** crearon X3MLBench, con proyectos reales de mapeo X3ML hacia CIDOC CRM validados por expertos. Probaron varios LLM (GPT, Gemini, DeepSeek, Mistral, Grok, Llama) con prompts zero-shot, syntax-aware e in-context.
- **Hallazgos:**
  - El zero-shot logra precisión "very close to zero", sobre todo por X3ML inválido.
  - La línea base léxica obtiene de 0 a 0,36 (media 0,14).
  - Errores recurrentes: "incorrect selection of ontology classes or properties", "improper structural connections" y "syntactically valid mappings that violate ontological constraints".
  - El artículo de visión critica el *prompt-to-RDF* porque "modeling decisions remain implicit and difficult to validate or reuse".
- **Relación con nuestra decisión: la apoya.** El grupo que mantiene CIDOC CRM (FORTH) pide sacar al LLM de la transformación directa a RDF. Matiz: ellos proponen que el LLM *genere el mapeo*, mientras que nosotros lo escribimos a mano. Nuestro diseño es más conservador y está en línea con su conclusión de que el experto debe validar.

**3. Schimmenti, A.; Pasqual, V.; Vitali, F.; van Erp, M. (2025).** "Knowledge Graphs Generation from Cultural Heritage Texts: Combining LLMs and Ontological Engineering for Scholarly Debates" (ATR4CH). arXiv:2511.10354. https://arxiv.org/abs/2511.10354 (resuelve).
- **Qué hicieron:**
  - Primero un esquema de anotación, después "mapping algorithms" que llevan la anotación a RDF.
  - El LLM produce "JSON schema-based responses" y cada componente "produces a JSON … designed to be convertible to RDF at the end".
  - Las afirmaciones de los estudiosos se modelan con autor de la opinión (*cognizer*), evidencia y RDF-star, más HiCo y PROV-O.
  - Modelos: Claude Sonnet 3.7, Llama 3.3 70B y GPT-4o-mini, sobre artículos de Wikipedia con debates de autenticidad.
- **Cifras (resumen):**

  | Tarea | F1 |
  |---|---|
  | Metadatos | 0,96–0,99 |
  | Entidades | 0,7–0,8 |
  | Hipótesis | 0,65–0,75 |
  | Evidencia | 0,95–0,97 |

  Representación del discurso: 0,62 G-EVAL. Los grafos generados tienen "10,000-12,000 vs. 4,026" tripletas frente al estándar de referencia, lo que indica sobreproducción.
- **Relación con nuestra decisión: es el precedente más cercano en método.** Esquema JSON, mapeo programado, afirmaciones atribuidas a quien opina y evidencia. Advierte de que hace falta supervisión humana y de que el LLM sobregenera, lo que también apoya un esquema cerrado.

**4. Wang, J. (2026).** "A Registry-Bound LLM Pipeline for Evidence-Grounded Trait Extraction across Tropical Plants, Aquatic Species, and Exotic Pets". arXiv:2606.00994 (preprint de autor único). https://arxiv.org/abs/2606.00994 (resuelve).
- **Qué hicieron:** un registro cerrado de 39 claves con valores tipados, una "per-row verbatim evidence quote" y una etiqueta de confianza por fila.
- **Cifras:**
  - El 90,12 % de 5.427.588 filas tiene la cita como subcadena literal de la fuente (93,49 % sin una meta-clave).
  - En la auditoría de si la cita apoya el valor (n=100), el resultado fue 100/100, con cota inferior del 96,30 %.
  - El autor aclara: "Per-record correctness is not claimed".
- **Relación con nuestra decisión: la apoya.** Su arquitectura (vocabulario cerrado + cita literal + verificación) es la nuestra en otro dominio. Advierte de que alrededor del 10 % de las citas no son literales aunque se pidan, así que la comprobación de subcadena tiene que ser determinista y bloqueante.

**5. Tam, Z. R.; Wu, C.-K.; Tsai, Y.-L.; Lin, C.-Y.; Lee, H.; Chen, Y.-N. (2024).** "Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models". *EMNLP 2024 Industry Track*. DOI 10.18653/v1/2024.emnlp-industry.91 (resuelve).
- **Hallazgos:**
  - "A significant decline in LLMs' reasoning abilities under format restrictions" y "stricter format constraints generally lead to greater performance degradation in reasoning tasks".
  - En cambio, en tareas de clasificación, "JSON-mode performs competitively, and in some cases" mejora.
- **Relación con nuestra decisión: la matiza (contradicción parcial).** Rellenar campos cerrados como tipo de actuación, rol o modalidad es clasificación, y ahí la restricción ayuda. Interpretar si una retractación es parcial es razonamiento, y ahí la restricción estricta perjudica. Implicación práctica: dejar fuera del esquema del LLM los juicios interpretativos (van a la capa 4) o permitir un campo de razonamiento previo. **NO VERIFICADO:** si el razonamiento previo mejora este caso concreto.

### B. Otros estudios pertinentes

- **Féral, J.; Chazalon, J.; Puren, M. (2025).** "Producing Structured Data from Historical Sources: A Preliminary Application to French Senate Tables". *Anthology of Computers and the Humanities* 3. DOI 10.63744/oXn2aMxza3iJ (resuelve).
  - Qué hicieron: un esquema mínimo inyectado en el prompt y "lightly constrained generation rather than strict post-hoc validation". Introducen la métrica IMQ (Integrated Matching Quality).
  - Cifras: IMQ por página de 0,8193 a 0,9591 en la tabla principal.
  - Relación: **apoya** el esquema plano y mínimo en documentos históricos ruidosos. Optan por restricción ligera, en línea con Tam et al.
- **Mihindukulasooriya, N.; Tiwari, S.; Enguix, C. F.; Lata, K. (2023).** "Text2KGBench: A Benchmark for Ontology-Driven Knowledge Graph Generation from Text". ISWC 2023, LNCS. DOI 10.1007/978-3-031-47243-5_14 (resuelve).
  - Qué hicieron: siete métricas, incluidas conformidad con la ontología y alucinación de sujeto, relación y objeto.
  - Hallazgos: con Vicuna-13B y Alpaca-LoRA-13B, "Precision, Recall and F1 score have low intermediate values" y "Ontology Conformance is pretty high".
  - Relación: **apoya** que la conformidad sintáctica no implica extracción correcta. Sus métricas SH, RH y OH sirven de plantilla de evaluación.
- **Clarizia, F.; De Santo, M.; Esposito, P.; Loffredo, R.; Sabini, B. (2026).** "From Unstructured Heritage Texts to Validated Knowledge Graphs: A NLP-Ontology-LLM Pipeline with Ground-Truth-Free Evaluation". CEUR-WS Vol-4307 ("From Objects to Agents 2026"). https://ceur-ws.org/Vol-4307/paper14.pdf
  - Qué hicieron: NER alineado con CRM, LLM y validación SHACL, sobre 96.348 tripletas de 944 registros de biblioteca.
  - Cifras: puntuación global 8,0/10 con LLM como juez.
  - Relación: **neutral o débil.** Sin estándar de referencia no mide alucinación de contenido. Su validación SHACL es aprovechable.
- **Wesslund, D.; Stenström, V.; Linde, P.; Holmberg, A. (2026).** "LLM-based Triplet Extraction from Financial Reports". arXiv:2602.11886. https://arxiv.org/abs/2602.11886
  - Hallazgos: la ontología inducida alcanza "100% schema conformance". La verificación híbrida (regex más LLM como juez) baja la alucinación aparente de sujeto "from 65.2% to 1.6%", porque filtra falsos positivos por correferencia.
  - Relación: **apoya** la verificación de anclaje textual y alerta de que la correferencia ("el dicho cacique") genera falsos positivos si se exige coincidencia literal del nombre.
- **Rao, Saraogi, Reddy, Purohit (2026).** "Selective Extraction: A Hallucination-Free Approach to LLM-Based Document Information Extraction". IEEE CONECCT 2026. DOI 10.1109/CONECCT68978.2026.11700668 (resuelve).
  - Lo que se pudo ver: según el resumen indexado, un verificador determinista de caracteres conserva solo los fragmentos literales. Con generación libre, en torno al 22 % de las salidas tenía alucinaciones, frente al 0 % con verificación.
  - **NO VERIFICADO** en texto completo: IEEE bloqueó el acceso.
- **Vasic, I.; Fill, H.-G.; Quattrini, R.; Pierdicca, R. (2025).** "Knowledge Graphs vs. Large Language Models: Competitors or Partners in Supporting Virtual Museums". *ACM JOCCH* 18(4):1–28. DOI 10.1145/3756016 (resuelve).
  - Qué hicieron: anotación semántica con CIDOC CRM y generación de grafos con LLM sobre una muestra de pinturas.
  - Conclusión: "a combination of ontologies and LLMs may provide an optimal approach" y "relying solely on LLMs may be risky".
  - Solo leí el resumen (PDF con 403): **cifras NO VERIFICADAS**. Relación: apoyo cualitativo.
- **Hariri, A. (2025).** "From Text to Triples: Large Language Models for Ontology-Aligned Annotation in Archaeology". ER 2025 Doctoral Consortium, CEUR-WS Vol-4099. https://ceur-ws.org/Vol-4099/ER25_DC_hariri.pdf
  - Herramienta asociada: https://github.com/lias-laboratory/cidoccrm-llm-extractor. Usa GPT-4 con tres estrategias: *unguided*, *full ontology* y *ontology subset* (la recomendada). El README dice que inyectar CRM completo "can overwhelm the model".
  - Relación: **apoya** restringir el vocabulario CRM que ve el LLM. No publica cifras en el texto que revisé.
- **Boukhers, Z.; Kong, L.; Zabulis, X.; Toubekis, G. (2026).** "Automated Construction of FAIR Digital Object Knowledge Graphs from Flat Cultural Heritage Records". arXiv:2608.23263. https://arxiv.org/abs/2608.23263
  - Qué hicieron: el LLM *clasifica y enruta* valores de registros planos de Europeana hacia vocabularios controlados, y el grafo CRM se construye por programa.
  - Cifras: "links 86% of metadata slots"; las fusiones multilingües son correctas en "17 of 33" casos.
  - Relación: **apoya.** El LLM clasifica y el código construye el grafo. También avisa de que las fusiones de grafías que propone el LLM son poco fiables (17/33), lo que sostiene dejar la identidad en la capa 4.
- **Geng, S. et al. (2025).** "JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models". arXiv:2501.10868. https://arxiv.org/abs/2501.10868
  - Qué hicieron: evaluaron seis motores de decodificación restringida (Guidance, Outlines, Llamacpp, XGrammar, OpenAI, Gemini) sobre 10.000 esquemas reales.
  - Relación: **apoya** usar un esquema JSON *sencillo* (enums, campos obligatorios) para que la restricción esté bien soportada por todos los motores. No copié cifras por modelo.
- **Mountantonakis, M.; Tzitzikas, Y. (2025).** "Generating SPARQL Queries over CIDOC-CRM Using a Two-Stage Ontology Path Patterns Method in LLM Prompts". *ACM JOCCH*. DOI 10.1145/3708326 (resuelve).
  - Trata de consulta, no de extracción. Sirve para pasar las preguntas de competencia a SPARQL sobre CRM.
- **Wang, Y.; Zhang, M. (2025).** "CIDOC CRM-Based Knowledge Graph Construction for Cultural Heritage Using Large Language Models". *Applied Sciences* 15(22):12063. DOI 10.3390/app152212063 (resuelve).
  - Hacen generación directa de tripletas con GPT, en CRM 7.2. El resumen no informa de validez de clases ni de alucinación.
  - Relación: **pertinencia baja.** Es un ejemplo del enfoque directo sin evaluación de validez.

### C. Evaluación de ontologías con preguntas de competencia (CQ)
- **Grüninger, M.; Fox, M. S. (1995).** "Methodology for the Design and Evaluation of Ontologies". IJCAI-95 Workshop on Basic Ontological Issues in Knowledge Sharing, Montreal.
  - Ficha: https://bibsonomy.org/bibtex/26881473a37ed442cff66d02790a258c0/lysander07. **Texto completo NO VERIFICADO**: no encontré un PDF estable.
  - Origen de las CQ como especificación del alcance (TOVE).
- **Ren, Y.; Parvizi, A.; Mellish, C.; Pan, J. Z.; van Deemter, K.; Stevens, R. (2014).** "Towards Competency Question-Driven Ontology Authoring". ESWC 2014, LNCS. DOI 10.1007/978-3-319-07443-6_50 (resuelve). Patrones de CQ y presupuestos que la ontología debe satisfacer.
- **Bezerra, C.; Freitas, F.; Santana, F. (2013).** "Evaluating Ontologies with Competency Questions". WI-IAT 2013. DOI 10.1109/WI-IAT.2013.199 (resuelve). Las CQ se traducen a consultas y se comprueban de forma automática.
- **Wiśniewski, D.; Potoniec, J.; Ławrynowicz, A.; Keet, C. M. (2019).** "Analysis of Ontology Competency Questions and their formalizations in SPARQL-OWL". *J. Web Semantics*. DOI 10.1016/j.websem.2019.100534 (resuelve). Recomendado para pasar las CQ a SPARQL.
- **Poveda-Villalón, M.; Gómez-Pérez, A.; Suárez-Figueroa, M. C. (2014).** "OOPS! (OntOlogy Pitfall Scanner!): An On-line Tool for Ontology Evaluation". *IJSWIS* 10(2). DOI 10.4018/ijswis.2014040102 (resuelve). Herramienta en línea: https://oops.linkeddata.es/
- **McNamara, C.; Hederman, L.; O'Sullivan, D. (2025).** "Mind the Gap: LLMs, Competency Questions, and the Non-Technical User in the Humanities Domain". SEMANTiCS 2025 Posters/Workshops, CEUR-WS Vol-4064. https://ceur-ws.org/Vol-4064/UKG-paper1.pdf. Usan GPT-4o y Gemini para generar CQ sobre el KG de VRTI, y la revisión experta sigue siendo necesaria.

### D. Acuerdo entre anotadores (brevemente)
- **Cohen, J. (1960).** "A Coefficient of Agreement for Nominal Scales". *Educ. Psychol. Meas.* 20(1). DOI 10.1177/001316446002000104 (resuelve).
- **Hayes, A. F.; Krippendorff, K. (2007).** "Answering the Call for a Standard Reliability Measure for Coding Data". *Communication Methods and Measures* 1(1). DOI 10.1080/19312450709336664 (resuelve). Alfa admite varios codificadores, datos faltantes y escalas nominales u ordinales.
- **Artstein, R.; Poesio, M. (2008).** "Inter-Coder Agreement for Computational Linguistics". *Computational Linguistics* 34(4). DOI 10.1162/coli.07-034-R2 (resuelve). Es la referencia estándar para elegir entre κ y α en anotación.
- **Aplicación:** α nominal sobre los campos cerrados (tipo de actuación, rol, modalidad) entre el LLM y dos anotadores humanos. Para la cita literal, coincidencia de fragmento (exacta o por solapamiento).

---

## (3) FUENTES INDEPENDIENTES PARA CONTRASTE (solo punteros)

### Bibliografía académica (fichas comprobadas en Open Library o Crossref)
- **O'Phelan Godoy, Scarlett (1979).** "La rebelión de Túpac Amaru: organización interna, dirigencia y alianzas". *Histórica* III(2), pp. 89–121 aprox. (la paginación final se deduce del PDF de 33 páginas que empieza en p. 89). https://revistas.pucp.edu.pe/index.php/historica/article/view/7859. Contiene la mención de un Chuquitapa (ver abajo).
- **O'Phelan, S. (1988).** *Un siglo de rebeliones anticoloniales: Perú y Bolivia 1700–1783*. Cusco: CBC. https://openlibrary.org/works/OL23436744W
- **O'Phelan, S. (1997).** *Kurakas sin sucesiones: del cacique al alcalde de indios. Perú y Bolivia 1750–1835*. Cusco: CBC. https://openlibrary.org/works/OL23712793W. Es el libro más directo sobre caciques interinos y recaudadores después de 1780.
- **Garrett, David T. (2005).** *Shadows of Empire: The Indian Nobility of Cusco, 1750–1825*. Cambridge UP. DOI 10.1017/CBO9780511529085 (resuelve).
- **Stavig, Ward (1999).** *The World of Túpac Amaru: Conflict, Community, and Identity in Colonial Peru*. University of Nebraska Press. https://openlibrary.org/works/OL1946247W. Estudia precisamente Canas y Canchis / Quispicanchis con causas criminales.
- **Thomson, Sinclair (2002/2003).** *We Alone Will Rule: Native Andean Politics in the Age of Insurgency*. University of Wisconsin Press. https://openlibrary.org/works/OL8275776W
- **Walker, Charles F. (2014).** *The Tupac Amaru Rebellion*. Belknap/Harvard. https://openlibrary.org/works/OL19976352W. Edición en castellano: IEP, 2015, https://openlibrary.org/works/OL32710266W. Del mismo autor, *Smoldering Ashes* (Duke, 1999): https://openlibrary.org/works/OL25356898W
- **Sala i Vila, Núria (1996).** *Y se armó el tole tole: tributo indígena y movimientos sociales en el virreinato del Perú, 1784–1814*. Huamanga: IER José María Arguedas. https://openlibrary.org/works/OL2245516W. Reseña: https://dialnet.unirioja.es/descarga/articulo/5139792.pdf. Es la referencia central para revisitas y conflictos por tributo en 1784–1814.
- **Golte, Jürgen (1980).** *Repartos y rebeliones: Túpac Amaru y las contradicciones de la economía colonial*. Lima: IEP. https://openlibrary.org/works/OL31538585W

### ¿Dónde podrían estar la matrícula o revisita de Tinta (c. 1805–1806) y los libros parroquiales?
- **Archivo Regional del Cusco (ARC):**
  - Fondo Intendencia, subserie **Real Hacienda (1783–1825)**.
  - Fondo **Real Audiencia del Cuzco**, Causas Criminales (1788–1824, legs. 98–148). Ahí puede haber una contrapartida del mismo pleito, porque resolvió la Audiencia.
  - Fondo **Tesorería Fiscal, "Libros de Contribuciones"**.
  - Fuente de esta descripción: blog de la Red de Archivos y Bibliotecas Históricas del Perú, http://archivosybibliotecasdelperu.blogspot.com/2015/03/archivo-regional-del-cusco.html. Es secundaria. En esa página **no aparecen** las palabras "matrícula", "padrón" ni "revisita".
  - El sitio oficial (archivo.regioncusco.gob.pe) tenía un certificado TLS inválido y no pude abrirlo.
  - **NO VERIFICADO** que la matrícula de 1805–1806 exista en el ARC.
- **Archivo Histórico de la Prelatura de Sicuani** (los libros de Tinta salieron del Arzobispado del Cusco al crearse la Prelatura). Fuente: *Catálogo del Archivo Histórico de la Prelatura de Sicuani. Libros Parroquiales*, Cusco: IPA / PLALA-Harvard, 2012, comp. C. Zegarra Moretti. https://mapapape.agn.gob.pe:8081/agn-pape/vistas/documentos/8/59/Cat%C3%A1logo%20del%20Archivo%20Hist%C3%B3rico%20de%20la%20Prelatura%20de%20Sicuani.%20Libros%20Parroquiales.pdf. Sección "#27 Parroquia de Tinta (TIN)", pp. 95–96 del catálogo, con fichas descriptivas hacia pp. 249–259. Libros que cubren 1806:

  | Código | Contenido | Fechas |
  |---|---|---|
  | PER/APS/AH/LP/TIN/LM/02 | Matrimonios | 1795–1827 |
  | PER/APS/AH/LP/TIN/LE/02 | Entierros | 1795–1823 |
  | TIN/LF/01 y LF/02 | Fábrica | 1788–1907 y 1788–1866 |

  **Laguna en bautismos:** TIN/LB/06 llega a 1784–1797 y TIN/LB/07 empieza en 1818. En el texto extraído del catálogo no aparecen "Chuquitapa", "Choquitapa", "Huancachoque" ni "Guancachoque".
- **Archivo Arzobispal del Cusco:** probable para autos de visita y expedientes del cura de Tinta. **NO VERIFICADO**: no encontré un inventario en línea.
- **AGN (Lima):** busqué en el catálogo en línea (https://fondosdocumentales.agn.gob.pe) "partido de Tinta", "provincia de Tinta", "Canas y Canchis", "matrícula de indios" y "Chuquitapa". No aparece ninguna matrícula ni revisita de Tinta: salen sobre todo papeles de Guerra y Marina (1822–23) y una "Matrícula de indios" de 1815 de la Colección Tomás Diéguez sin relación con Tinta. **NO VERIFICADO** fuera de línea; habría que consultar en sala las series de tributos y Real Hacienda.
- **AGI (Sevilla, PARES):** no encontré una matrícula de Tinta de 1804–1806. Sí encontré dos punteros:
  - Mapa "del Partido de Canas y Canches o Tinta, Intendencia del Cuzco", MP-PERU_CHILE,94: https://pares.mcu.es/ParesBusquedas20/catalogo/description/22666
  - Los procesos de 1780–81 están en AGI, Audiencia del Cuzco, legs. 32–33, según la nota inicial de O'Phelan 1979.
- **FamilySearch:** la colección "Peru, Cusco, Civil Registration, 1889–1997" (https://www.familysearch.org/en/search/collection/1987564) es posterior a nuestro periodo. El catálogo de libros parroquiales pide iniciar sesión y no pude comprobar si existe microfilm de Tinta: **NO VERIFICADO**.

### ¿Menciones publicadas de Andrés Chuquitapa (o variantes)?
- **De Andrés Chuquitapa como cacique de Tinta: no encontré ninguna mención publicada.**
  - Busqué las grafías Chuquitapa, Choquitapa, Choquetapa y Chuquitape en buscadores web, en el AGN y en el catálogo de Sicuani.
  - Google Books (cuota agotada), HathiTrust (bloqueo anti-bots) e Internet Archive (0 resultados) no permitieron una búsqueda útil.
  - La única fuente en línea que lo nombra es el repositorio GitHub `ianlw/Grafo-Conocimiento-Cusco`, que describe este mismo expediente y no es independiente.
- **Mención de una Chuquitapa en 1780–81 (no es Andrés):** O'Phelan 1979, *Histórica* III(2), **p. 113**. Es la tabla anexa de procesados, que empieza en p. 110 con columnas "Nombre / Procedencia y residencia / Casta / Edad / Estado / Oficio". Según el OCR del PDF de PUCP:
  > "Joseph Marnani [sic OCR; probablemente "Mamani", NO VERIFICADO] — Tinta — indio — 35 — Casado con Asencia Chuquitapa — cacique — Coronel en Sangarara y Piccho. Enviaba gente. Forzado. — 200 azotes, 10 años de destierro."

  Enlace: https://revistas.pucp.edu.pe/index.php/historica/article/view/7859 (PDF: `/article/download/7859/8132`). Es solo un puntero de parentesco posible. No permite afirmar ningún vínculo con Andrés Chuquitapa, pero es pertinente para contrastar la fórmula del expediente "comisionado y no coronel".
- **Otra mención sin verificar:** un blog turístico atribuye a un "Juan Chuquitapa" la donación de un altar de plata a la iglesia de Tinta en 1784 (http://daylidia.blogspot.com/p/sitios-turisticos.html). No es una fuente académica: **NO VERIFICADO**.
