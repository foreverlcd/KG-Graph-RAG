# H1 · Alternativas para modelar afirmaciones disputadas y la capa de reconstrucción

> **Fecha de la búsqueda:** 2026-11-12.
> **Alcance:** cómo representar enunciados atribuidos y en conflicto («quién dijo qué»), enunciados sobre enunciados y la reconstrucción de personas, comparado con lo que ya hace LAAD (capa 3 = E13/STAR; capa 4 = PiCo/ROAR + CRMinf + PROV-O, en grafos nombrados).
> **Qué no repito:** las fichas de FPO, PiCo, ROAR, Enslaved, Wikibase/Wikidata, CRMinf (ResearchSpace), RiC-O y HGIS ya están en `docs/anexos/F_informe_precedentes_y_literatura.md` y en `docs/F_precedentes.md`. Aquí solo añado lo nuevo o lo que corrige esos documentos.
>
> **Marcas.** **[VERIFICADO]** = leí la fuente primaria (especificación, archivo de ontología, artículo o metadatos Crossref/Zenodo/DataCite) y la cita o el dato salen de ahí. **[NO VERIFICADO]** = dato de segunda mano, resumen indexado o deducción mía no comprobada en la fuente.
> Fuentes descargadas para la verificación (no forman parte del proyecto): especificación RDF 1.2 Concepts (CR Draft 2026-11-12), PDF de CIDOC CRM 7.4, texto completo de Andrews 2025, Mariani 2023 y Massari et al. 2025; el `CRMinf_v1.2.1.rdf` y el `CIDOC_CRM_v7.1.3_PC.rdfs` son los de `vendor/`.

---

## 1. Resumen y recomendación

**Recomendación: mantener la arquitectura** (E13 al estilo STAR en la capa 3; PiCo/ROAR + CRMinf + PROV-O en grafos nombrados en la capa 4). Ninguna alternativa revisada la mejora para un expediente judicial con varios afirmantes, roles procesales y retractaciones. Ninguna lo hace sin, a la vez, (a) introducir un juicio de verdad en los datos o (b) abandonar los estándares que el proyecto ya verifica. Hay, sin embargo, **cuatro hallazgos que obligan a corregir o precisar el modelo y su documentación**:

1. **CRMinf 1.2.1 cambia la lectura de E13 [VERIFICADO en `vendor/crminf/CRMinf_v1.2.1.rdf`].**
   * Declara `crm:E13_Attribute_Assignment rdfs:subClassOf crminf:I1_Argumentation`. I1 se define como una inferencia u observación «honesta», en la que el actor «justifies and believes» el valor de creencia.
   * Introduce `J33_assigned_propositions` (E13 → `I17_One-Proposition_Set`), descrita como atajo del camino «E13 → J2 → I2 Belief → J4 → I4 → J5 holds to be (= "TRUE")».
   * Consecuencia: con CRMinf cargado (y `scripts/razonar.py` carga todo `vendor/`), cada afirmación de la capa 3 se lee como *creencia sincera del afirmante en que la proposición es verdadera*. Eso agrava **L5**: un E13 con `pol:niega` dice formalmente que el testigo cree verdadero lo que niega. Y tensiona el caso central, una retractación jurada, en el que al menos una de las dos declaraciones no fue «honesta».
   * Es un defecto nuevo que debe documentarse junto a D1–D5 (propuesta: **D6**). Ver §5, R2–R3.
2. **STAR ya usa P140/P177/P141 [VERIFICADO en Andrews 2025, párr. 21].** El artículo de 2025 en *Digital Medievalist* codifica sujeto, predicado y objeto con P140, P177 y P141, la autoridad con P14, la evidencia con P17 y el documento con P70.
   * `docs/C_modelo.md` §3.3 («STAR no nombra P140, P141 ni P177») y `docs/F_precedentes.md` describen solo el resumen de 2023. Hay que citar también Andrews 2025 y reducir las «diferencias con STAR» a dos: la fuente como actuación (`P9i`) más el ancla `oa:` en lugar de P17/P70, y el uso de P17 para relaciones de discurso.
3. **Inconsistencia interna sobre P17 [VERIFICADO en el repositorio].** `docs/F_precedentes.md` y `docs/C_correspondencias.md` (fila «En qué actuación») dicen que P17 «se reserva a las premisas de capa 4». En cambio, `docs/C_modelo.md` §3.3, `docs/C_correspondencias.md` (filas «Corrige o niega…» y «Discurso referido») y `src/laad/mapeo.py` (líneas 306 y 309) usan P17 también en la capa 3 (`responde_a`, `segun`). Hay que unificar el texto. El uso actual es compatible con STAR, que pone en P17 «a text passage, an inscription, or another assertion».
4. **RDF 1.2 sigue sin ser Recomendación [VERIFICADO].** *RDF 1.2 Concepts and Abstract Data Model* figura hoy como **W3C Candidate Recommendation Draft, 12 de noviembre de 2026** (hubo un CR Snapshot el 7 de abril de 2026). Turtle y TriG 1.2 siguen como Working Drafts, y *What's New in RDF 1.2* es un Group Note Draft del 14 de julio de 2026. No conviene basar el modelo en triple terms. Sí conviene preparar una **vista derivada** en la que el IRI de cada E13 sea el *reificador* de su triple (§5, R6).

---

## 2. Estado de los estándares (noviembre de 2026)

| Estándar | Versión vigente | Estado | Fuente | Marca |
|---|---|---|---|---|
| CIDOC CRM | 7.1.3 (feb. 2024) | *Official (ISO Correspondence)* | cidoc-crm.org/versions-of-the-cidoc-crm | VERIFICADO |
| CIDOC CRM (borrador) | 7.4 (ago. 2026); antes 7.3.2 (mar. 2026) | *Draft* | ídem; PDF 7.4 | VERIFICADO |
| E13 en 7.4 | Nota de alcance sin cambios de fondo: «the maintaining team is in general neutral to the validity of the respective assertion»; «Multiple use of instances of E13 … may possibly lead to a collection of contradictory values» | — | PDF 7.4, p. 69–70 | VERIFICADO |
| Clases PC (n-arias) | 17 clases `PC*` en `CIDOC_CRM_v7.1.3_PC.rdfs` («representation of the n-ary relationship form of the property»), solo para las propiedades con «.1» (P14.1, P3.1, P67.1…) | Suplemento RDFS oficial | `vendor/` | VERIFICADO |
| CRMinf | 1.2.1 (abr. 2026) | *Stable*; sin versión posterior | cidoc-crm.org/crminf/ModelVersion/crminf-1.2.1 | VERIFICADO |
| CRMtex | 2.0 | *Release Candidate* | cidoc-crm.org/extensions | VERIFICADO (estado); contenido NO VERIFICADO |
| CRMsoc | 0.1 (sobre CRM 6.2.5) | Borrador sin estado | ídem | VERIFICADO |
| RDF 1.2 Concepts | CR Draft 12-11-2026 | No es Recomendación | w3.org/TR/rdf12-concepts | VERIFICADO |
| PROV-O | 30-04-2013 | Recomendación W3C | w3.org/TR/prov-o | VERIFICADO |
| Web Annotation Data Model | 23-02-2017 | Recomendación W3C | w3.org/TR/annotation-model | VERIFICADO |
| N-ary Relations | 12-04-2006 | Working Group Note | w3.org/TR/swbp-n-aryRelations | VERIFICADO |
| PiCo | 1.1.0; último commit 2026-09-14 | Activo | GitHub API | VERIFICADO |
| ROAR | 0.1; último commit 2019-09-24 | Inactivo | GitHub API | VERIFICADO |
| FPO | último commit 2020-06-19 | Inactivo | GitHub API | VERIFICADO |
| SNAP:DRGN Ontology | último commit 2022-03-01 (ontología de 2015) | Inactivo | GitHub API | VERIFICADO |
| Linked Art | «Model 1.0» / «API 1.0» | Estable | linked.art/model/assertion | VERIFICADO (etiqueta de navegación) |

---

## 3. Alternativas, una por una

### 3.A Mecanismos genéricos de «enunciado sobre enunciado» (nivel RDF)

**A1. Reificación RDF clásica (`rdf:Statement`).**
* **Qué es:** un nodo con `rdf:subject`, `rdf:predicate` y `rdf:object`.
* **Madurez:** RDF 1.0/1.1, sin semántica formal útil. Massari et al. (2025) señalan que «the size of the dataset is at least quadrupled» [VERIFICADO].
* **Para nosotros:** E13 + P140/P177/P141 *es* una reificación, pero tipada y con agente, tiempo y actuación. CRMinf 1.2.1 lo dice expresamente: la terna de E13 puede leerse como «a 'reification' which is implicit in the declaring class» (nota de alcance de I17) [VERIFICADO].
* **Decisión:** no adoptar `rdf:Statement`. No aporta nada que E13 no tenga.

**A2. Relaciones n-arias (Noy y Rector 2006).**
* **Qué es:** un nodo intermedio para la relación. Es el patrón que E13 y las clases PC ya instancian.
* **Madurez:** Note W3C estable.
* **Decisión:** ya está adoptado vía CRM. No hace falta citarlo como alternativa, sino como fundamento.

**A3. Propiedades singleton (Nguyen, Bodenreider y Sheth 2014).**
* **Qué es:** una propiedad nueva por cada aserción (`:cargo#1 rdf:singletonPropertyOf :cargo`).
* **Madurez:** propuesta académica, sin estándar. Massari et al. (2025) le atribuyen «non-standard terms and … scalability challenges» [VERIFICADO].
* **Para nosotros:** viola el principio 5 (solo términos existentes) y fabrica miles de propiedades.
* **Decisión:** descartar.

**A4. Grafos nombrados (RDF 1.1 Datasets).**
* **Qué es:** cuádruplas; el grafo es la unidad de procedencia.
* **Para nosotros:** ya es el mecanismo de separación de capas y de cada reconstrucción (`g:reconstruccion/R-x`).
* **Ventaja frente a E13:** Mariani (2023) observa que E13 describe el contexto de *una* afirmación. Cuando la hipótesis es un evento entero, «we would need to repeat the same information multiple times» y propone empaquetar cada hipótesis como grafo [VERIFICADO]. Es exactamente nuestra elección en la capa 4 (proposición = grafo, creencia sobre el grafo).
* **Debilidad:** la semántica de RDF 1.1 no dice qué *significa* el nombre del grafo. Por eso la creencia va en CRMinf.
* **Decisión:** mantener. La crítica de Mariani es un buen argumento para el artículo a favor de nuestro diseño híbrido: E13 para enunciados atómicos de fuente y grafo nombrado para hipótesis compuestas del investigador.

**A5. RDF 1.2: *triple terms* y reificadores (antes RDF-star).**
* **Qué es [VERIFICADO, CR Draft 12-11-2026]:** un triple term es «an RDF triple used as an RDF term within another triple». No se afirma salvo que el triple también esté en el grafo. Un *reifying triple* tiene `rdf:reifies` como predicado y un triple term como objeto; su sujeto (el reificador) puede ser un enunciado, una creencia o una situación. «The meaning of the rdf:reifies property is deliberately generic», y puede haber varios reificadores para la misma proposición («statements with different sources»).
* **Madurez:** no es Recomendación (§1). La compatibilidad de triplestores y bibliotecas (rdflib, pySHACL) con la sintaxis final está **NO VERIFICADA**. Massari et al. (2025) aún la llaman «non-standard».
* **Fortalezas:** es compacta, consultable en SPARQL 1.2 y separa «expresar» de «afirmar», que es justo nuestro principio 2. ATR4CH (Schimmenti et al. 2025, ya en el anexo F) la usa para opiniones de estudiosos.
* **Debilidades para nosotros:**
  * El reificador no trae tipología ni roles. Quién declara, ante quién, quién firma, la fuerza y el fundamento seguirían necesitando CRM.
  * SHACL 1.2 está en preparación, y sus formas sobre triple terms quedan **NO VERIFICADAS**.
  * Cambiar ahora rompería `tests/test_terminos_existen.py` y la canonización N-Quads (commit `e5b2cb8`).
* **Decisión:** no adoptar como fuente. Cuando sea Recomendación, generar una **vista** en la que el IRI del E13 sea el reificador (§5, R6).

**A6. Nanopublicaciones (Groth et al. 2010; Kuhn et al. 2016).**
* **Qué es:** tres grafos (aserción, procedencia, información de publicación) más un grafo cabecera. Vocabulario: `np:Nanopublication`, `np:hasAssertion`, `np:hasProvenance`, `np:hasPublicationInfo` (`http://www.nanopub.org/nschema#`). Se identifican con hashes (*trusty URIs*), se firman y son inmutables [VERIFICADO en nanopub.net y sus guías].
* **Madurez:** hay una red descentralizada activa (Nanodash, Knowledge Pixels; ejemplos de 2026).
* **Para nosotros:** nuestro par de grafos de capa 4 (proposición + argumentación) más `g:procedencia` es, de hecho, una nanopublicación sin cabecera. Mariani (2023) propone las nanopublicaciones precisamente para que «two conflicting hypotheses about the same activity can coexist» [VERIFICADO].
* **Decisión:** adoptarlas como **formato de exportación** de la capa 4, no como cambio del núcleo (§5, R5).

**A7. *Conjectural graphs* (Daquino, Pasqual, Tomasi y Vitali 2022) y DEC (Vitali y Pasqual 2026).**
* **Qué son:** «Express Without Asserting». Cada triple conjetural usa un predicado único con `conj:isAConjecturalFormOf` el predicado original, dentro de un grafo nombrado [VERIFICADO vía Massari et al. 2025, listado 10]. DEC formaliza «mundos cognitivos» por procedencia y es «conservative over RDF 1.2 semantics», con un razonador prototipo sobre Fuseki [VERIFICADO: resumen de arXiv; cuerpo NO VERIFICADO].
* **Para nosotros:** resuelven el mismo problema que nuestra capa 4 sin CRMinf, pero con un predicado conjetural por triple (un problema parecido al de A3) y con vocabularios de grupo pequeño.
* **Decisión:** no adoptar. Citar DEC en el artículo como trabajo paralelo: su «factualización controlada» equivale a nuestra elección explícita de creencia por reconstrucción.

### 3.B Modelos de aserción del dominio

**B1. Factoid (Bradley y Pasin; FPO) e IPIF.**
* **Qué es:** ya está descrito en el anexo F.
* **Lo nuevo:** IPIF (Vogeler, Vasold y Schlögl 2019; actualizado en 2022) es una API REST/OpenAPI con cuatro entidades (Factoid, Source, Person, Statement) que «requires a Source for each Factoid» [VERIFICADO: repositorio y resúmenes DHd; texto del artículo de 2019 NO VERIFICADO].
* **Madurez:** FPO está inactiva desde 2020; IPIF no tiene actividad reciente comprobada.
* **Para nosotros:**
  * El factoid funde fuente y aseverador, y el «Statement» de IPIF es plano (sin roles procesales).
  * Baillie (2021) y Andrews (2023/2025) critican que el factoid prioriza la procedencia «at the expense of providing coherent and non-contradictory accounts» [VERIFICADO en el PDF de STAR, `vendor/star/`].
* **Decisión:** no cambiar. Opcional: IPIF como **API de salida** prosopográfica (Statement ≈ E13; Factoid ≈ actuación + ancla; Person ≈ reconstrucción PiCo).

**B2. Wikibase / Wikidata / FactGrid.**
* **Lo nuevo frente al anexo F:**
  * La exportación RDF de Wikibase genera, además del nodo `wikibase:Statement` con `prov:wasDerivedFrom` hacia las referencias, *truthy statements* (`wdt:`) «that have the best non-deprecated rank» [VERIFICADO en *Wikibase/Indexing/RDF Dump Format*]. Es decir, **materializa como hecho** la afirmación mejor clasificada, justo lo que nuestras capas 1–3 prohíben.
  * FactGrid (instancia Wikibase para historiadores, Universidad de Erfurt / Gotha) admite afirmaciones contradictorias, `P51` «primary source», `P12` «literature», `P129` «according to» («to build distance from the (doubtful) statement») y `P155` «How sure is this?» [VERIFICADO en *Help:How do I feed data into FactGrid?*]. A diferencia de Wikidata, admite investigación propia.
* **Para nosotros:**
  * `P129` es el análogo más cercano a nuestro afirmante, pero no separa afirmante, receptor y firmante.
  * `P155` es el análogo de `cre:*`, pero cuelga del enunciado, no de una inferencia con autor.
* **Decisión:** no adoptar como modelo. FactGrid es un **destino plausible de publicación** de la capa 4 (reconstrucciones con `P155` y referencias a la pieza), siempre sin exportar las capas 1–3 como *truthy*.

**B3. STAR (RELEVEN).**
* **Autoría:** Tara L. Andrews (Universität Wien, proyecto RELEVEN). Primer resumen en GrapHNR 2023 (PDF en `vendor/star/`; metadatos «Author: Tara L Andrews») y artículo en *Digital Medievalist* 18 (2025), DOI 10.16995/dm.16708 [VERIFICADO]. **No encontré ninguna relación con «Ocampo» ni «Tittel»**: no figuran como autores en ninguna de las dos fuentes.
* **Modelo [VERIFICADO, Andrews 2025, párr. 20–21]:** «we reify the predicate and express the assertion as a CRM E13 Attribute Assignment … P140 assigned attribute to, P177 assigned property of type, and P141 assigned … authority … via P14 carried out by, and the evidence via P17 was motivated by. The assertion is then linked back to its source … via the P70 documents property».
* **Madurez:** aplicado a toda la parte del siglo XI de la PBW; sin OWL propio publicado (no lo necesita, porque usa solo CRM). Andrews anuncia «experimentation with ontological reasoning software to detect where assertions conflict».
* **Para nosotros:** es nuestro patrón. Diferencias reales: (i) usamos la actuación (`P9i`) + `oa:` como fuente; (ii) añadimos los roles PC14 de la actuación (ante quién, quién firma); (iii) polaridad, fundamento y fuerza como `P2_has_type`.
* **Decisión:** mantener y corregir la documentación (§1, punto 2).

**B4. CIDOC CRM E13 y clases PC.** Ya se usan. Matiz de documentación: PC solo existe para las propiedades con «.1». No hay `PC140`, `PC141` ni `PC177` (comprobado en el RDFS PC 7.1.3). Por tanto, no se puede «tipar» P141 con un rol: polaridad y fuerza deben colgar del E13 (como ya hacemos).

**B5. Linked Art 1.0.**
* **Qué es [VERIFICADO, linked.art/model/assertion]:** `AttributeAssignment` (`attributed_by`/`assigned_by`, `assigned`, `assigned_property`) se usa para «either uncertain or previously held to be true claims» (p. ej. «Possibly By»), y las asignaciones «should be kept to a minimum». No trata atribuciones rechazadas.
* **Crítica [VERIFICADO, Mariani 2023]:** Linked Art «deliberately leaves out … uncertainty and data provenance».
* **Decisión:** no adoptar; sirve para museos. Útil solo como argumento: incluso el perfil de CRM más usado limita E13 a casos marginales, mientras que en un expediente judicial E13 *es* el dato principal.

### 3.C Creencia, argumentación y discurso

**C1. CRMinf 1.2.1. Novedades que el proyecto todavía no usa [VERIFICADO en `vendor/`]:**
* `I16_Meaning_Comprehension` (⊑ I1): «interpreting the intended meaning … resolving named entities, references and co-references, and completing missing text parts, without however arguing about the actual truth of the information». Es **exactamente** lo que hoy marcamos como `anot:*` (sujeto elíptico, afirmante tomado de otra pieza; L6).
* `I13_Intended_Meaning_Belief` (⊑ I2): creencia de que un conjunto de proposiciones representa «the intended meaning that was created by another … Actor, without considering an opinion yet about its truth». Se enlaza con `J16_assumed_meaning` → I4 y con `J17_about` → la fuente.
* `I7_Belief_Adoption` / `I12_Adopted_Belief`: el investigador adopta una proposición «by arguments of trust» en la fuente (`J7_is_based_on_evidence_from` → E73). Es el modelo correcto para «acepto la fecha que da el escribano» frente a una inferencia I5.
* `I17_One-Proposition_Set` + `J30/J31/J32` y `J33_assigned_propositions` (E13 → I17): la «interfaz lógica» entre E13 y una proposición explícita. La propia nota dice que, para documentar, «the use of simpler shortcut properties will, typically, be the preferred approach».
* `I11_Situation` admite expresamente la negación: «persons A and B have met is FALSE».
* **Defecto/tensión nueva (D6):** `E13 ⊑ I1` y J33 como atajo de «J5 = TRUE» (§1, punto 1).

**C2. HiCO (Daquino y Tomasi 2015).** `hico:InterpretationAct` con criterio y tipo. Mariani (2023, tabla 1) lo alinea con CRMinf (I1, J2→I2→J4) [VERIFICADO]. Es redundante con CRMinf. **No adoptar.**

**C3. AIF / AIF-EL / IAT (argumentación).**
* **Qué es:**
  * AIF (Chesñevar et al. 2006; Rahwan, Zablith y Reed 2007) tiene nodos I (información) y S (RA = inferencia, CA = conflicto, PA = preferencia).
  * AIF-EL (Cerutti et al. 2018) es la versión OWL 2 EL.
  * IAT (Budzynska et al. 2014) añade locuciones e ilocuciones (*asserting*, *disagreeing*, *challenging*) ancladas en el diálogo.
  * [VERIFICADO: metadatos Crossref y resúmenes. Texto completo de AIF-EL e IAT NO VERIFICADO.]
* **Para nosotros:** IAT es el modelo teórico más cercano a una declaración que *responde* a otra (`anot:responde-a`): distingue conflicto, apoyo y reformulación, y ancla cada ilocución en una locución con hablante. Pero no está alineado con CRM, la ontología OWL de AIF ha tenido errores de perfil (motivo de AIF-EL) y no tiene roles procesales.
* **Decisión:** no importar. Usarlo para **refinar el esquema SKOS `anot:`** (subconceptos «contradice», «confirma», «matiza», «se retracta de» con `skos:closeMatch` a los tipos de nodo S de AIF si se publican IRIs estables [NO VERIFICADO que existan IRIs estables]).

**C4. CRMsoc 0.1 / CRMtex 2.0.**
* CRMsoc está en borrador sobre CRM 6.2.5: **no usar**.
* CRMtex 2.0 (RC) modela la materialidad del texto escrito; su utilidad para menciones y segmentos frente a `oa:` queda **NO VERIFICADA**. Revisarlo cuando sea *stable*, si se quiere modelar la foliación (L1) con CRM en lugar de RiC-O.

### 3.D Personas: menciones y reconstrucciones

**D1. PiCo 1.1.0** (activo, commit 2026-09-14) y **ROAR 0.1** (inactivo desde 2019): sin cambios respecto del anexo F. Riesgo: el defecto D1 de ROAR difícilmente se corregirá en origen. Conviene notificarlo de todos modos y valorar a medio plazo usar `picom:`/`prov:` también para grupos y lugares, si PiCo los amplía [NO VERIFICADO que haya planes].

**D2. SNAP:DRGN** (Bodard et al.; ontología de 2015, repositorio inactivo desde 2022). Es un índice de co-referencias para personas antiguas sobre LAWD/PROV. Lo supera PiCo. **No adoptar.** (DOI 10.11588/dco.2017.0.37975: el *handle* resuelve, pero no pude abrir la página por un bloqueo anti-bots; título y paginación **NO VERIFICADOS**.)

**D3. PROV-O para la reconstrucción.** PiCo usa `prov:wasDerivedFrom`/`prov:wasGeneratedBy`; ROAR, `prov:qualifiedDerivation`. Nuestro `I5 ∧ prov:Activity` es coherente con ambos. No hay alternativa mejor.

**D4. Web Annotation** (Rec. 2017). Montenegro et al. (2026) y ATR4CH también la usan como ancla de evidencia. Mantener.

**D5. Precedente andino nuevo: *The People of Aucará (1760–1921)*** (Melo Flórez, Ramos, de la Puente Luna, Cobo Betancourt et al., UCSB, Zenodo, 2026-03-11, v1.0.0, DOI 10.5281/zenodo.18969893) [VERIFICADO en metadatos Zenodo].
* **Qué es:** «structured mention instances ("personas")» de registros parroquiales de Aucará (Ayacucho), presentado «rather than a completed family reconstitution» como insumo para *probabilistic record linkage*.
* **Por qué importa:** es la misma separación mención/reconstrucción que nuestras capas 2 y 4, en fuentes andinas coloniales, y no es RDF.
* **Uso:** es el contraste más cercano en dominio que he encontrado. Merece entrar en `docs/F_precedentes.md` o en el estado de la cuestión del artículo.
* **Lo que no encontré:** ningún modelo de datos enlazados específico para la antroponimia andina (variantes quechuas y aimaras, apellidos de cacique) ni para expedientes judiciales coloniales con testimonios en RDF. La búsqueda no prueba que no existan, pero refuerza la novedad del caso.

---

## 4. Literatura 2022–2026 pertinente (además del anexo F)

| Trabajo | Qué aporta | Relación con LAAD | Marca |
|---|---|---|---|
| Massari, Peroni, Tomasi y Heibi (2025), *DSH* 41(S1) | Compara reificación, n-arias, grafos nombrados, RDF-star, singleton, E13, nanopublicaciones y conjectural graphs. Concluye que no hay «one-size-fits-all» y destaca grafos nombrados, RDF-star, PROV-O y conjectural graphs | Marco comparativo para el artículo. Valida grafos nombrados + PROV + E13 | VERIFICADO |
| Mariani (2023), COMHUM 2022, CEUR 3602 | E13 es verboso para hipótesis de varios enunciados y contradicciones → nanopublicación por hipótesis | Apoya nuestra capa 4 como grafo + creencia | VERIFICADO |
| Andrews (2025), *Digital Medievalist* 18 | STAR completo sobre E13/P140/P177/P141/P14/P17/P70 | Corrige `C_modelo` §3.3 | VERIFICADO |
| Vitali y Pasqual (2026), arXiv:2606.15246 | DEC: semántica epistémica de la procedencia sobre RDF 1.2 | Trabajo paralelo a la capa 4 | VERIFICADO (resumen) |
| Daquino, Pasqual, Tomasi y Vitali (2022), IRCDL, CEUR 3160 | Conjectural graphs (EWA) | Alternativa descartada (A7) | VERIFICADO vía Massari et al.; texto original NO VERIFICADO |
| Rao y Feng (2026), AIDS 2026, ACM | Conflicto fecha de archivo frente a dendrocronología conservado como afirmaciones con procedencia, alineado con CRM | Ejemplo menor de coexistencia | VERIFICADO (Crossref); contenido NO VERIFICADO |
| Tambuscio y Vogeler (2025), CHR 2025 | Red prosopográfica tipada (corte de Maximiliano I), grupo IPIF | Contexto prosopográfico | VERIFICADO (Crossref); contenido NO VERIFICADO |
| Melo Flórez et al. (2026), Zenodo | Menciones andinas para *record linkage* | Precedente de dominio (D5) | VERIFICADO |
| Baillie (2021), *IJHAC* 15 | Estructuras alternativas al factoid | Crítica al factoid citada por STAR | VERIFICADO (Crossref) |

---

## 5. Recomendaciones concretas

| # | Acción | Tipo | Motivo |
|---|---|---|---|
| **R1** | **Mantener** E13/STAR (capa 3) + PiCo/ROAR/CRMinf/PROV en grafos nombrados (capas 2 y 4) | Sin cambio | Ninguna alternativa cubre afirmante, receptor, firmante y fuerza sin un vocabulario propio. E13 es Official (7.1.3) y no cambia en 7.4; STAR lo valida en un proyecto grande |
| **R2** | Documentar **D6** (CRMinf 1.2.1: `E13 ⊑ I1` y J33 = «J5 TRUE»). Hacer que `scripts/razonar.py` informe del número de E13 inferidos como `I1_Argumentation` y que el texto explique que la capa 3 **no** debe leerse con la semántica de CRMinf | Documentación + informe | La «honestidad» de I1 contradice retractaciones y `pol:niega` |
| **R3** | **Negación (L5), opción mejorada sin términos nuevos:** cuando un testigo *contradice una afirmación previa*, modelarlo como un E13 cuyo `P140` es el E13 contradicho, con `P177 → atr:veracidad` y `P141 → concepto «falso»`. Así el E13 que niega «cree verdadero» que la otra afirmación es falsa, coherente con J33. Conservar `pol:niega` solo para negaciones sin antecedente explícito y documentarlo | Cambio acotado (tesauro + mapeo) | Elimina la contradicción formal en el caso central (retractación) |
| **R4** | **Discurso referido (L4):** E13 anidado. El E13 externo (Cano) tiene `P141` → E13 interno («Santiago afirmó X», `P14` → mención de Santiago, `P2 fun:oidas`). E13 admite E1 como valor, y STAR usa P17 → «another assertion» como evidencia | Implementar | Más fiel que `segun`, sin términos nuevos |
| **R5** | **Exportar la capa 4 como nanopublicaciones:** cabecera `np:Nanopublication` con `np:hasAssertion` → `g:reconstruccion/R-x`, `np:hasProvenance` → `g:argumentacion/R-x` y `np:hasPublicationInfo` → extracto de `g:procedencia` | Exportación opcional | Citable, inmutable y alineado con Mariani 2023; el núcleo no cambia |
| **R6** | Vigilar RDF 1.2. Cuando sea Recomendación y pySHACL/rdflib la soporten, generar una **vista**: `<<( mención atr:x valor )>>` con `rdf:reifies` desde el **mismo IRI** del E13 | Vista derivada, futuro | Interoperabilidad con ATR4CH, DEC y triplestores; nunca como fuente |
| **R7** | **Decisiones del anotador (L6) → CRMinf I16/I13** en un grafo propio de capa 4 (o «capa 3b»): `I16_Meaning_Comprehension` (P14 = anotador o LLM, `J22_interpreted_meaning_of` → tramo) → `J23` → `I13_Intended_Meaning_Belief`. Primero en un piloto con 5 casos `anot:*` | Piloto | Da a las decisiones del anotador un hogar estándar, sin juicio de verdad («without … arguing about the actual truth») |
| **R8** | Modelar la aceptación de datos de la fuente por confianza (fechas del escribano, foliación) como `I7_Belief_Adoption` (`J7` → pieza) en lugar de `I5` | Precisión | CRMinf 1.2.1 distingue adopción por confianza de inferencia |
| **R9** | Refinar `anot:responde-a` con subconceptos inspirados en AIF/IAT (contradice, confirma, matiza, se retracta) | Tesauro | Mejora las consultas de disputa (I1 de la revisión) |
| **R10** | Corregir la documentación: STAR 2025 (§1.2) y la frase sobre P17 en `F_precedentes.md` y `C_correspondencias.md` (§1.3). Añadir el dataset de Aucará como precedente de dominio | Documentación | Exactitud |
| — | **No adoptar:** `rdf:Statement`, propiedades singleton, conjectural graphs, rangos y *truthy* de Wikibase, HiCO, SNAP:DRGN, CRMsoc, Linked Art como perfil | — | Ver §3 |

---

## 6. Bibliografía (datos para BibTeX)

```bibtex
@article{andrews2025star,
  author  = {Andrews, Tara L.},
  title   = {Byzantine Sigillography, Linked Open Data, and the Structured Assertion Record},
  journal = {Digital Medievalist},
  volume  = {18},
  year    = {2025},
  doi     = {10.16995/dm.16708},
  note    = {Publicado el 30-01-2025. VERIFICADO}
}
@misc{andrews2023star,
  author       = {Andrews, Tara L.},
  title        = {The STructured Assertion Record (STAR) Model for Event-based Representation of Historical Information},
  howpublished = {Resumen, Graphs and Networks in the Humanities 2023 (GrapHNR)},
  year         = {2023},
  url          = {https://graphentechnologien.hypotheses.org/files/2023/05/GrapHNR-2023-32-Andrews-STAR.pdf},
  note         = {VERIFICADO (copia en vendor/star)}
}
@techreport{crm74,
  author      = {{CIDOC CRM Special Interest Group}},
  title       = {Definition of the CIDOC Conceptual Reference Model, version 7.4},
  institution = {ICOM/CIDOC},
  year        = {2026},
  month       = aug,
  type        = {Draft},
  url         = {https://cidoc-crm.org/sites/default/files/cidoc_crm_version_7.4.pdf},
  note        = {La versión oficial sigue siendo la 7.1.3 (feb. 2024). VERIFICADO}
}
@techreport{crminf121,
  author      = {Doerr, Martin and Fafalios, Pavlos and Kritsotaki, Athina and Ore, Christian-Emil and Stead, Stephen},
  title       = {CRMinf: the Argumentation Model, version 1.2.1},
  institution = {CIDOC CRM SIG (FORTH; Paveprime Ltd.)},
  year        = {2026},
  month       = apr,
  type        = {Stable},
  url         = {https://cidoc-crm.org/crminf/ModelVersion/crminf-1.2.1},
  note        = {VERIFICADO}
}
@article{doerr2011factual,
  author  = {Doerr, Martin and Kritsotaki, Athina and Boutsika, Katerina},
  title   = {Factual argumentation---a core model for assertions making},
  journal = {Journal on Computing and Cultural Heritage},
  volume  = {3}, number = {3}, pages = {1--34}, year = {2011},
  doi     = {10.1145/1921614.1921615},
  note    = {VERIFICADO (Crossref)}
}
@techreport{rdf12concepts,
  author      = {Hartig, Olaf and Champin, Pierre-Antoine and Seaborne, Andy and Kellogg, Gregg},
  title       = {RDF 1.2 Concepts and Abstract Data Model},
  institution = {W3C},
  type        = {Candidate Recommendation Draft},
  year        = {2026},
  month       = nov,
  url         = {https://www.w3.org/TR/rdf12-concepts/},
  note        = {CR Draft del 12-11-2026; CR Snapshot del 07-04-2026. No es Recomendación. VERIFICADO}
}
@article{massari2025provenance,
  author  = {Massari, Arcangelo and Peroni, Silvio and Tomasi, Francesca and Heibi, Ivan},
  title   = {Representing provenance and track changes of cultural heritage metadata in RDF: a survey of existing approaches},
  journal = {Digital Scholarship in the Humanities},
  volume  = {41}, number = {Supplement\_1}, pages = {i196--i212}, year = {2025},
  doi     = {10.1093/llc/fqaf076},
  note    = {En línea el 30-07-2025; número de 2026. VERIFICADO}
}
@inproceedings{mariani2023visu,
  author    = {Mariani, Fabio},
  title     = {Introducing VISU: Vagueness, Incompleteness, Subjectivity, and Uncertainty in Art Provenance Data},
  booktitle = {Proceedings of the Workshop on Computational Methods in the Humanities 2022 (COMHUM 2022)},
  series    = {CEUR Workshop Proceedings}, volume = {3602}, pages = {63--84}, year = {2023},
  url       = {https://ceur-ws.org/Vol-3602/paper5.pdf},
  note      = {VERIFICADO}
}
@inproceedings{daquino2022ewa,
  author    = {Daquino, Marilena and Pasqual, Valentina and Tomasi, Francesca and Vitali, Fabio},
  title     = {Expressing Without Asserting in the Arts},
  booktitle = {Proceedings of the 18th Italian Research Conference on Digital Libraries (IRCDL 2022)},
  series    = {CEUR Workshop Proceedings}, volume = {3160}, year = {2022},
  url       = {http://ceur-ws.org/Vol-3160/short14.pdf},
  note      = {Datos tomados de Massari et al. 2025; texto original NO VERIFICADO}
}
@misc{vitali2026dec,
  author = {Vitali, Fabio and Pasqual, Valentina},
  title  = {Provenance-Enhanced Statements in Knowledge Graphs},
  year   = {2026},
  eprint = {2606.15246}, archivePrefix = {arXiv},
  note   = {Preprint del 13-06-2026. VERIFICADO (resumen)}
}
@inproceedings{nguyen2014singleton,
  author    = {Nguyen, Vinh and Bodenreider, Olivier and Sheth, Amit},
  title     = {Don't like RDF reification? Making statements about statements using singleton property},
  booktitle = {Proceedings of the 23rd International Conference on World Wide Web (WWW '14)},
  pages     = {759--770}, year = {2014},
  doi       = {10.1145/2566486.2567973},
  note      = {VERIFICADO (Crossref)}
}
@techreport{noy2006nary,
  author      = {Noy, Natasha and Rector, Alan},
  title       = {Defining N-ary Relations on the Semantic Web},
  institution = {W3C}, type = {Working Group Note}, year = {2006}, month = apr,
  url         = {https://www.w3.org/TR/swbp-n-aryRelations/},
  note        = {VERIFICADO (título y fecha)}
}
@article{frey2019metadata,
  author  = {Frey, Johannes and M{\"u}ller, Kay and Hellmann, Sebastian and Rahm, Erhard and Vidal, Maria-Esther},
  title   = {Evaluation of metadata representations in RDF stores},
  journal = {Semantic Web}, volume = {10}, number = {2}, pages = {205--229}, year = {2019},
  doi     = {10.3233/SW-180307},
  note    = {VERIFICADO (Crossref)}
}
@article{groth2010nanopub,
  author  = {Groth, Paul and Gibson, Andrew and Velterop, Jan},
  title   = {The anatomy of a nanopublication},
  journal = {Information Services and Use}, volume = {30}, number = {1--2}, pages = {51--56}, year = {2010},
  doi     = {10.3233/ISU-2010-0613},
  note    = {VERIFICADO (Crossref)}
}
@article{kuhn2016nanopub,
  author  = {Kuhn, Tobias and Chichester, Christine and Krauthammer, Michael and Queralt-Rosinach, N{\'u}ria and Verborgh, Ruben and Giannakopoulos, George and Ngonga Ngomo, Axel-Cyrille and Viglianti, Raffaele and Dumontier, Michel},
  title   = {Decentralized provenance-aware publishing with nanopublications},
  journal = {PeerJ Computer Science}, volume = {2}, pages = {e78}, year = {2016},
  doi     = {10.7717/peerj-cs.78},
  note    = {VERIFICADO (Crossref)}
}
@article{pasin2015factoid,
  author  = {Pasin, Michele and Bradley, John},
  title   = {Factoid-based prosopography and computer ontologies: towards an integrated approach},
  journal = {Digital Scholarship in the Humanities}, volume = {30}, number = {1}, pages = {86--97}, year = {2015},
  doi     = {10.1093/llc/fqt037},
  note    = {En línea en 2013. VERIFICADO (Crossref)}
}
@article{baillie2021prosopography,
  author  = {Baillie, James},
  title   = {Alternative Database Structures for Prosopographical Research},
  journal = {International Journal of Humanities and Arts Computing},
  volume  = {15}, number = {1--2}, pages = {117--132}, year = {2021},
  doi     = {10.3366/ijhac.2021.0265},
  note    = {VERIFICADO (Crossref)}
}
@misc{vogeler2019ipif,
  author = {Vogeler, Georg and Vasold, Gunter and Schl{\"o}gl, Matthias},
  title  = {Data Exchange in Practice: Towards a Prosopographical API},
  year   = {2019},
  url    = {https://github.com/IPIF/prosopogrAPhI},
  note   = {Título según fuentes secundarias; texto NO VERIFICADO. Repositorio VERIFICADO}
}
@article{woltjer2024pico,
  author  = {Woltjer, Pieter E. and Zandhuis, Ivo and Coret, Bob and Lindeman, Mark and Balkenende, Jeroen D. and Zijdeman, Richard L. and Mourits, Rick J.},
  title   = {Persons in Context. A Model to Represent Observations and Reconstructions of Historical Persons in Linked Data},
  journal = {Historical Life Course Studies}, volume = {14}, pages = {105--125}, year = {2024},
  doi     = {10.51964/hlcs19312},
  note    = {VERIFICADO (Crossref)}
}
@article{bodard2017snap,
  author  = {Bodard, Gabriel and Cayless, Hugh and Depauw, Mark and Isaksen, Leif and Lawrence, K. Faith and Rahtz, Sebastian},
  title   = {Standards for Networking Ancient Person data: Digital approaches to problems in prosopographical space},
  journal = {Digital Classics Online}, volume = {3}, number = {2}, year = {2017},
  doi     = {10.11588/dco.2017.0.37975},
  note    = {El DOI resuelve; título y autores NO VERIFICADOS en la página del editor}
}
@inproceedings{daquino2015hico,
  author    = {Daquino, Marilena and Tomasi, Francesca},
  title     = {Historical Context Ontology (HiCO): A Conceptual Model for Describing Context Information of Cultural Heritage Objects},
  booktitle = {Metadata and Semantics Research (MTSR 2015)},
  series    = {Communications in Computer and Information Science}, volume = {544}, pages = {424--436}, year = {2015},
  doi       = {10.1007/978-3-319-24129-6_37},
  note      = {VERIFICADO (Crossref; el volumen 544 NO VERIFICADO)}
}
@article{chesnevar2006aif,
  author  = {Ches{\~n}evar, Carlos and McGinnis, Jarred and Modgil, Sanjay and Rahwan, Iyad and Reed, Chris and Simari, Guillermo and South, Matthew and Vreeswijk, Gerard and Willmott, Steven},
  title   = {Towards an argument interchange format},
  journal = {The Knowledge Engineering Review}, volume = {21}, number = {4}, pages = {293--316}, year = {2006},
  doi     = {10.1017/S0269888906001044},
  note    = {VERIFICADO (Crossref)}
}
@article{rahwan2007wwaw,
  author  = {Rahwan, Iyad and Zablith, Fouad and Reed, Chris},
  title   = {Laying the foundations for a World Wide Argument Web},
  journal = {Artificial Intelligence}, volume = {171}, number = {10--15}, pages = {897--921}, year = {2007},
  doi     = {10.1016/j.artint.2007.04.015},
  note    = {VERIFICADO (Crossref)}
}
@inproceedings{cerutti2018aifel,
  author    = {Cerutti, Federico and Toniolo, Alice and Norman, Timothy J. and Bex, Floris and Rahwan, Iyad and Reed, Chris},
  title     = {AIF-EL -- An OWL2-EL-Compliant AIF Ontology},
  booktitle = {Computational Models of Argument (COMMA 2018)},
  series    = {Frontiers in Artificial Intelligence and Applications}, year = {2018},
  doi       = {10.3233/978-1-61499-906-5-455},
  note      = {VERIFICADO (Crossref)}
}
@inproceedings{budzynska2014iat,
  author    = {Budzynska, Katarzyna and Janier, Mathilde and Reed, Chris and Saint-Dizier, Patrick and Stede, Manfred and Yakorska, Olena},
  title     = {A Model for Processing Illocutionary Structures and Argumentation in Debates},
  booktitle = {Proceedings of the Ninth International Conference on Language Resources and Evaluation (LREC 2014)},
  year      = {2014},
  doi       = {10.63317/52zr77iewo78},
  note      = {Metadatos VERIFICADOS (Crossref)}
}
@article{lawrence2020argmining,
  author  = {Lawrence, John and Reed, Chris},
  title   = {Argument Mining: A Survey},
  journal = {Computational Linguistics}, volume = {45}, number = {4}, pages = {765--818}, year = {2020},
  doi     = {10.1162/coli_a_00364},
  note    = {VERIFICADO (Crossref)}
}
@techreport{provo2013,
  author      = {Lebo, Timothy and Sahoo, Satya and McGuinness, Deborah},
  title       = {PROV-O: The PROV Ontology},
  institution = {W3C}, type = {Recommendation}, year = {2013}, month = apr,
  url         = {https://www.w3.org/TR/2013/REC-prov-o-20130430/},
  note        = {Fecha VERIFICADA; editores según la especificación}
}
@techreport{webannotation2017,
  author      = {Sanderson, Robert and Ciccarese, Paolo and Young, Benjamin},
  title       = {Web Annotation Data Model},
  institution = {W3C}, type = {Recommendation}, year = {2017}, month = feb,
  url         = {https://www.w3.org/TR/annotation-model/},
  note        = {Fecha VERIFICADA}
}
@misc{linkedart2025assertion,
  author       = {{Linked Art}},
  title        = {Linked Art Model 1.0: Assertions (AttributeAssignment)},
  howpublished = {\url{https://linked.art/model/assertion/}},
  note         = {Consultado el 2026-11-12. VERIFICADO}
}
@misc{factgrid2026help,
  author       = {{FactGrid}},
  title        = {Help: How do I feed data into FactGrid?},
  howpublished = {\url{https://database.factgrid.de/wiki/Help:How_do_I_feed_data_into_FactGrid%3F}},
  note         = {P51, P12, P129, P155. Consultado el 2026-11-12. VERIFICADO}
}
@misc{wikibaseRdfDump,
  author       = {{Wikimedia Foundation}},
  title        = {Wikibase/Indexing/RDF Dump Format},
  howpublished = {\url{https://www.mediawiki.org/wiki/Wikibase/Indexing/RDF_Dump_Format}},
  note         = {Truthy statements y prov:wasDerivedFrom. Consultado el 2026-11-12. VERIFICADO}
}
@dataset{meloflorez2026aucara,
  author    = {Melo Fl{\'o}rez, Jairo Antonio and Ramos, Gabriela and de la Puente Luna, Jos{\'e} Carlos and Cobo Betancourt, Juan and Ancho, Benjamin and Xue, Dongchi and Ayinaparthi, Saketh and Roque Ortega, Grecia and Gonzales Rojas, Edwin and Quillca, James and Velarde Loayza, Javier and Asto Campos, Clark},
  title     = {The People of Aucar{\'a} (1760--1921): An Intermediary Dataset from Parish Records of the Sondondo Valley, Peru},
  publisher = {Zenodo}, version = {1.0.0}, year = {2026},
  doi       = {10.5281/zenodo.18969893},
  note      = {UCSB Archives, Memory \& Preservation Lab. VERIFICADO}
}
@inproceedings{rao2026mingxianling,
  author    = {Rao, Jian and Feng, Disong},
  title     = {Knowledge Graph Construction and Applications for the Protection of the Ming Xianling Mausoleum},
  booktitle = {Proceedings of the 2026 International Conference on Artificial Intelligence and Digital Services},
  pages     = {179--185}, year = {2026},
  doi       = {10.1145/3803686.3803716},
  note      = {Metadatos VERIFICADOS; contenido NO VERIFICADO}
}
@article{tambuscio2025maximilian,
  author  = {Tambuscio, Marcella and Vogeler, Georg},
  title   = {Bridging Semantics and Structure: a Typed Prosopographical Network of Maximilian I's Court},
  journal = {Anthology of Computers and the Humanities (Computational Humanities Research 2025)},
  pages   = {131--141}, year = {2025},
  doi     = {10.63744/ewebtidsvfzv},
  note    = {Metadatos VERIFICADOS; contenido NO VERIFICADO}
}
```
