# F · Precedentes (máximo ocho)

> Elegidos por **parecido de problema**, no de dominio:
> * testimonios en conflicto o afirmaciones atribuidas;
> * procedencia archivística;
> * grafías inestables;
> * archivo colonial hispanoamericano.
>
> **Verificación.** La ficha completa de cada precedente está en `docs/anexos/F_informe_precedentes_y_literatura.md`.
> Ese anexo lo redactó un subagente que abrió cada enlace y buscó cada término en el archivo de ontología o en el código.
> Lo que el modelador comprobó además por su cuenta está marcado **[verif. modelador]**. Lo que nadie pudo comprobar
> está marcado **NO VERIFICADO**.

| # | Precedente | Patrón concreto que copiamos | Dónde está en LAAD | Modelo de datos / repositorio | Qué no nos sirve |
|---|---|---|---|---|---|
| 1 | **Factoid prosopography** (KCL; PoMS, PASE) | La aserción anclada a una fuente y a un lugar en ella (`fpo:Factoid ⊑ fpo:Assertion`, `fpo:sourcedFrom`). La mención con la grafía de la fuente (`fpo:PersonReference`, `fpo:hasNameInSourceAs`, `fpo:hasPlaceInSource`). Distinción entre la fecha de la aserción y la fecha de lo aseverado. | Registro de afirmación (capa 3) con `tramo` y `cita`. Mención (capa 2) con `texto` literal. Fecha de la actuación frente a `atr:fecha-del-hecho`. | https://github.com/johnBradley501/FPO (`fpo.owl`); DOI 10.1093/llc/fqt037 | La fuente es el único aseverador: no separa quién declara, ante quién, quién escribe y quién firma. No tiene tipos de actuación. No está alineado con CRM. |
| 2 | **PiCo 1.1.0** (CBG, NL) | `picom:PersonObservation` con `prov:hadPrimarySource` y la grafía literal. `picom:PersonReconstruction` con `prov:wasDerivedFrom` y `prov:wasGeneratedBy`. Rol en la fuente con `picom:hasRole`. | Capas 2 y 4 de personas (clases importadas tal cual). `ohac.ttl` alinea los roles con el tesauro de PiCo. | https://github.com/CBG-Centrum-voor-familiegeschiedenis/PiCo; `vendor/pico/pico.ttl` **[verif. modelador: términos en el archivo]** | Usa schema.org y no CRM. Está pensado para registros civiles. No tiene actos de habla. Su tesauro de roles carece de querellante, juez, escribano e intérprete. Hay una discrepancia de IRI entre `picot_roles:` (`…/roles/`) y los conceptos publicados (`…/ThesaurusHistorischePersoonsgegevens/`). |
| 3 | **ROAR 0.1** (Golden Agents) | `roar:LocationObservation` / `roar:LocationReconstruction` para lugares, y `roar:Observation` / `roar:Reconstruction` para grupos. Fuente con `roar:documentedIn`. | Capas 2 y 4 de lugares y grupos (el ayllu como grupo). | https://github.com/LvanWissen/roar; `vendor/roar/roar.ttl` **[verif. modelador]** | Roles como literales. Eventos en SEM. **Defecto D1**: declara `rdfs:domain roar:Reconstruction` sobre `prov:wasDerivedFrom`, lo que, combinado con PiCo, produce una inconsistencia (`docs/C_modelo.md` §7). |
| 4 | **Enslaved.org Ontology** (MSU) | El enlace de identidad es una **entidad con tipo y procedencia** (`Match`, `hasMatchType`), no un `owl:sameAs`. Cada atributo lleva su procedencia (`EntityWithProvenance`). | La reconstrucción es un grafo nombrado con `crminf:I5`/`I2`, autor, fecha y argumento. Cero `owl:sameAs` (prueba en `tests/test_capas.py`). | https://docs.enslaved.org/ontology/ (`enslaved-v2.owl`); DOI 10.1016/j.websem.2020.100567 | Vocabulario propio. Está orientado a fusionar bases de datos ya estructuradas. No modela testimonio ni juramento. |
| 5 | **Wikibase / Wikidata** | Lista de control de los campos del registro plano: cita (`P1683` *quotation*), grafía tal como aparece (`P1810` / `P1932`), naturaleza del enunciado (`P5102`). Las afirmaciones contradictorias coexisten sin borrarse. | `cita`, `texto`, `polaridad`, `fundamento`. Las disputas coexisten y se calculan. | https://www.mediawiki.org/wiki/Wikibase/DataModel | La reificación no es CRM. El «quién asevera» se reduce a la referencia. Los rangos (*preferred* / *deprecated*) serían un juicio de verdad dentro de los datos, justo lo que evitamos en las capas 1–3. |
| 6 | **CRMinf 1.2.1** (CIDOC SIG), tal como lo usa **ResearchSpace** (British Museum) | `I2_Belief` → `J4_that` → `I4_Proposition_Set` con `J5_holds_to_be`, concluida por `I5_Inference_Making` (`J2_concluded_that`). La capa del investigador apunta a las inferiores y no las sobrescribe. | Capa 4: cada reconstrucción es un `I4_Proposition_Set` (su grafo nombrado), con una creencia y una inferencia. | https://cidoc-crm.org/crminf/ModelVersion/crminf-1.2.1; `vendor/crminf/CRMinf_v1.2.1.rdf` **[verif. modelador]**; https://github.com/researchspace/researchspace | ResearchSpace es una plataforma pesada. En la 1.2.1 `J6_adopted` no existe e `I6_Belief_Value` no es clase (el rango de J5 es un literal). Además, `J2_concluded_that` se declara subpropiedad de P175/P185, así que no conviene hacer inferencia RDFS ingenua sobre CRMinf. |
| 7 | **RiC-O 1.1** (ICA-EGAD), implementado en los Archives nationales de France (PIAAF → RiC-O Converter) | `RecordSet` → `includesOrIncluded` → `Record`. `hasDocumentaryFormType`. `hasOrHadInstantiation`. Componentes de instanciación (`hasOrHadComponent`) y derivación (`isOrWasDerivedFromInstantiation`). `rico:Date` con `expressedDate`. | Capa 1 completa: jerarquía, piezas, original, transcripción, tramos y folios explícitos. | https://github.com/ICA-EGAD/RiC-O; `vendor/ric-o/RiC-O_1-1.rdf` **[verif. modelador]**; https://github.com/ArchivesNationalesFR/rico-converter | No modela el contenido aseverado. Sus agentes y actividades duplicarían a CRM, así que se limita a la capa 1. No tiene «folio», «sección» ni «legajo» (se resuelven con conceptos SKOS propios). **NO VERIFICADO:** un alineamiento oficial RiC-O ↔ CRM. |
| 8 | **HGIS de las Indias** (W. Stangl) en **World Historical Gazetteer** (Linked Places Format) | Cada topónimo lleva su cita y su periodo de validez. Identificadores estables de lugares (`src_id`) y territorios (código de 8 caracteres). | Reconstrucción de lugares con `crm:P48_has_preferred_identifier` + `rdfs:seeAlso` hacia WHG. Tinta = HGIS 6000357 (WHG 177060). | https://whgazetteer.org/datasets/15/places; DOI 10.7910/DVN/FUSJD3; https://github.com/LinkedPasts/linked-places-format | Es GeoJSON-LD, no CRM. No cubre personas. Las URI de hgis-indias.net devuelven 404 (consultado el 2026-11-12). Los ayllus no tienen entrada. San Pedro (6000358) = San Pedro de Cacha es **probable, no confirmado**. |

**Descartados:**

* **Digital Panopticon / Old Bailey:** heurísticas de enlace de registros, sin modelo RDF publicado.
* **Candela et al. 2023, JOCCH (Relaciones Geográficas):** colonial hispano, pero a nivel de metadatos de colección.
* **Early Modern Inquisition Database:** el sitio no respondió (NO VERIFICADO).
* **STAR (Andrews 2023, RELEVEN):** no es un precedente aparte, porque es el *patrón* que seguimos en la capa 3. No tiene OWL publicado. El PDF está en `vendor/star/`.

  STAR modela cada afirmación como E13, con sujeto y objeto E1, predicado E55, fuente por P17 y autoridad por P14.

  **Lo que cambiamos respecto de STAR:**
  * Sujeto, predicado y objeto van en P140, P177 y P141, que es la lectura estándar de E13 en CRM 7.1.3.
  * La fuente se modela como la actuación de la que forma parte la afirmación (`P9i_forms_part_of`), más un ancla textual `oa:`. STAR usa `P17`.
  * El P17 se reserva para las premisas del investigador en la capa 4.

## Contraste con fuentes independientes: estado

Detalle en el anexo, §3.

| Fuente | Estado |
|---|---|
| Catálogo del ARC | Contrastado: hay 5 discrepancias (K1–K5, `docs/01_materiales.md` §4.2). |
| Libros parroquiales de Tinta | En el Archivo Histórico de la Prelatura de Sicuani. Para 1806 constan matrimonios 1795–1827 y entierros 1795–1823; laguna de bautismos 1797–1818. **No consultados.** |
| Matrícula o revisita de Tinta (c. 1805–1806) | **No localizada.** Punto de partida: ARC, Intendencia, Real Hacienda. |
| Andrés Chuquitapa en la bibliografía | **No se halló mención publicada.** O'Phelan (1979, *Histórica* III(2), p. 113) registra a una «Asencia Chuquitapa» casada con un cacique «Coronel en Sangarara»: es un punto de contraste para la fórmula «coronel/comisionado», no una identificación. |
| HGIS | Tinta identificado; el resto, pendiente (PC07). |
