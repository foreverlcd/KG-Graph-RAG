# C · Tabla de correspondencias

> Cada necesidad del modelo se cubre con un término **verificado en el archivo de especificación descargado** (`vendor/`).
> La prueba `tests/test_terminos_existen.py` falla si se usa una IRI no declarada.
>
> Columnas:
> * **Capa**: 1 documento · 2 menciones · 3 afirmaciones · 4 reconstrucción · P procedencia · T tesauro.
> * **Verif.**: comprobado en el archivo (sí) o solo en la documentación (doc).
>
> Las notas de alcance literales están en `docs/anexos/C_terminos_verificados.md`.

## Capa 1 — documento (RiC-O 1.1 + CRM)

| Necesidad | Término | Estándar | Verif. | Alternativa descartada y por qué |
|---|---|---|---|---|
| Fondo Intendencia | `rico:RecordSet` + `rico:hasRecordSetType rst:Fonds` | RiC-O 1.1 y vocabulario RecordSetTypes | sí | — |
| Sección Causas Criminales | `rico:RecordSet` + `rico:hasRecordSetType doc:seccion` | RiC-O + tesauro | sí | `Subfonds` no existe en el vocabulario RiC-O 1.1 |
| Serie Cusco | `rico:RecordSet` + `rst:Series` | RiC-O | sí | — |
| Legajo 14 | `rico:RecordSet` + `doc:legajo` | RiC-O + tesauro | sí | Tratarlo como `rico:Instantiation`, porque es una unidad física: se descarta porque el catálogo lo usa como nivel de descripción |
| Expediente 18 | `rico:RecordSet` + `rst:File` | RiC-O | sí | — |
| Inclusión jerárquica | `rico:isOrWasIncludedIn` / `rico:includesOrIncluded` | RiC-O | sí | — |
| Pieza (documento producido en una actuación) | `rico:Record` ∧ `crm:E31_Document` | RiC-O + CRM 7.1.3 | sí | Solo `rico:RecordPart`: la pieza es un documento completo, no una parte intelectual de otro |
| Tipo documental de la pieza | `rico:hasDocumentaryFormType` → concepto `act:*` | RiC-O + tesauro | sí | El vocabulario DocumentaryFormTypes de RiC-O solo tiene AuthorityRecord, FindingAid e IIIFManifest |
| Orden físico de las piezas y los tramos | `rico:directlyPrecedesInSequence` | RiC-O | sí | `rico:rankInSequence`: la propia RiC-O lo desaconseja |
| Fecha tal como está escrita | `rico:hasCreationDate` → `rico:Date` + `rico:expressedDate` | RiC-O | sí | `rico:normalizedDateValue`: prohibido en capa 1 por SHACL (fallo 2.6) |
| Expediente físico (sin imágenes) | `rico:Instantiation` + `rico:isOrWasInstantiationOf` | RiC-O | sí | — |
| Folio | `rico:Instantiation` + `rico:isOrWasComponentOf` (del original) + `dct:type doc:folio` | RiC-O | sí | RiC-O no tiene «folio»; `rico:hasOrHadLocation` es para lugares geográficos |
| Transcripción paleográfica (versión) | `rico:Instantiation` + `rico:isOrWasDerivedFromInstantiation` (del original) + `dct:identifier "sha256:…"` | RiC-O + DCTerms | sí | — |
| Tramo de transcripción | `rico:Instantiation` + `rico:isOrWasComponentOf` (de la transcripción); `rico:isOrWasDerivedFromInstantiation` (del folio, si consta) | RiC-O | sí | — |
| Pieza ↔ tramos | `rico:hasOrHadInstantiation` | RiC-O | sí | — |
| Actuación (acto procesal que crea la pieza) | `crm:E65_Creation` + `crm:P94_has_created` | CRM 7.1.3 | sí | `rico:Activity`: duplicaría los eventos de CRM; las afirmaciones necesitan un E7 al que pertenecer |
| Tipo de actuación | `crm:P2_has_type` → `act:*` | CRM + tesauro | sí | Subclases OWL de actuación: «procesal como clase», que el encargo prohíbe |
| Fecha de la actuación (escrita) | `crm:P4_has_time-span` → `crm:E52_Time-Span` + `crm:P1_is_identified_by` → `crm:E41_Appellation` + `crm:P190_has_symbolic_content` | CRM | sí | — |
| Fuerza institucional | `crm:P2_has_type` → `fza:*` | CRM + tesauro | sí | Un valor de verdad: prohibido (fallo 1.4) |

## Capa 2 — menciones (PiCo 1.1.0, ROAR 0.1, Web Annotation)

| Necesidad | Término | Estándar | Verif. | Alternativa descartada y por qué |
|---|---|---|---|---|
| Persona tal como aparece en la pieza | `picom:PersonObservation` ∧ `crm:E21_Person` | PiCo + CRM | sí | `fpo:PersonReference`: no está alineada con CRM. La doble tipificación con E21 permite que la mención sea rango de P14/P140, y equivale a `PersonObservation ⊑ sdo:Person` en PiCo |
| Lugar tal como aparece | `roar:LocationObservation` ∧ `crm:E53_Place` | ROAR + CRM | sí | PiCo no tiene observación de lugar |
| Grupo (ayllu…) tal como aparece | `roar:Observation` ∧ `crm:E74_Group` | ROAR + CRM | sí | Una subclase `Ayllu`: «andino como clase», que el encargo prohíbe |
| Fuente de la mención | `prov:hadPrimarySource` (PiCo) / `roar:documentedIn` (ROAR) | PiCo / ROAR | sí | `prov:hadPrimarySource` en ROAR: inconsistente por el defecto D1 |
| Grafía literal | `crm:P1_is_identified_by` → `crm:E41_Appellation` + `crm:P190_has_symbolic_content`; `rdfs:label` | CRM | sí | `skos:altLabel` sobre una persona ya fusionada: es el error del intento previo |
| Rol en la pieza | `picom:hasRole` → `rol:*`, y en la actuación `crm:PC14_carried_out_by` + `crm:P01_has_domain` / `crm:P02_has_range` + `crm:P14.1_in_the_role_of` (+ atajo `crm:P14_carried_out_by`) | PiCo + CRM `_PC` | sí | Rol como clase de persona (fallo 1.1) |
| Ancla textual | `oa:Annotation` + `oa:hasBody` / `oa:hasTarget` + `oa:SpecificResource` + `oa:hasSource` (tramo) + `oa:TextQuoteSelector` (`oa:exact`) + `oa:TextPositionSelector` (`oa:start` / `oa:end`) | W3C Web Annotation | sí | `crm:P70i_is_documented_in`: tiene dominio E31, no apunta a un pasaje y no admite selectores |

## Capa 3 — afirmaciones (patrón STAR sobre CRM E13)

| Necesidad | Término | Estándar | Verif. | Alternativa descartada y por qué |
|---|---|---|---|---|
| La afirmación | `crm:E13_Attribute_Assignment` (en CRMinf 1.2.1, `E13 ⊑ crminf:I1_Argumentation`) | CRM / CRMinf | sí | Reificación RDF (`rdf:Statement`), RDF-star o nanopublicaciones: ninguna da actor, tiempo y actividad en CRM |
| Quién la hace | `crm:P14_carried_out_by` + `crm:PC14_carried_out_by` con `crm:P14.1_in_the_role_of rol:declarante`… | CRM `_PC` | sí | `prov:wasAttributedTo`: es procedencia del dato (fallo 1.5) |
| En qué actuación (y de ahí: tipo, fecha, ante quién, quién escribe y quién firma) | `crm:P9i_forms_part_of` → `crm:E65_Creation` | CRM | sí | `crm:P17_was_motivated_by`, como en STAR: se reserva a las premisas de capa 4 |
| Ante quién | En la actuación: `PC14` con rol en la rama `rol:receptor` | CRM `_PC` + tesauro | sí | Una propiedad «ante» de OHAC: innecesaria |
| Quién escribe | En la actuación: `PC14` con `rol:redactor` cuando el documento lo dice; si está disputado, E13 con `atr:redacto` | CRM + tesauro | sí | — |
| Quién firma | Mención con `rol:firmante` (capa 2) → `PC14` en la actuación; si se niega, E13 con `atr:firmo` + `pol:niega` | CRM + tesauro | sí | — |
| Sobre qué | `crm:P140_assigned_attribute_to` → mención, pieza o hecho narrado | CRM | sí | Una persona reconstruida: mezclaría capas 3 y 4 |
| Qué se afirma | `crm:P177_assigned_property_of_type` → `atr:*` (lista cerrada en SKOS) | CRM + tesauro | sí | Predicados propios del caso (fallo 1.2); la IRI de una propiedad CRM como valor: *punning* |
| Valor | `crm:P141_assigned` → concepto (`cargo:`, `cond:`), mención, pieza, hecho, `crm:E33_Linguistic_Object` (literal) o `crm:E52_Time-Span` (tiempo literal) | CRM | sí | Un literal directo en P141: su rango es E1 |
| Polaridad (afirma o niega) | `crm:P2_has_type` → `pol:*` | CRM + tesauro | sí | Un valor de verdad |
| Fundamento invocado («con mis ojos», «de oídas») | `crm:P2_has_type` → `fun:*` | CRM + tesauro | sí | — |
| Sujeto elíptico resuelto | `crm:P2_has_type anot:sujeto-eliptico` + `crm:P3_has_note` | CRM + tesauro | sí | — |
| Hecho narrado (por pieza) | `crm:E5_Event` + `prov:hadPrimarySource` (pieza) | CRM + PROV | sí | Un evento único compartido entre testigos: es una correferencia (capa 4) |
| Cita | `oa:Annotation` → `oa:hasBody` E13 | Web Annotation | sí | — |

## Capa 4 — reconstrucción (PiCo, ROAR, CRM, CRMinf)

| Necesidad | Término | Estándar | Verif. | Alternativa descartada y por qué |
|---|---|---|---|---|
| Persona reconstruida | `picom:PersonReconstruction` ∧ `crm:E21_Person` + `prov:wasDerivedFrom` (menciones) | PiCo + CRM | sí | `owl:sameAs` entre menciones: destruye la capa 2 (prohibido por SHACL) |
| Lugar reconstruido | `roar:LocationReconstruction` ∧ `crm:E53_Place` + `crm:P48_has_preferred_identifier` (HGIS) + `rdfs:seeAlso` (WHG) | ROAR + CRM | sí | `owl:sameAs` hacia WHG |
| Evento reconstruido | `crm:E5_Event` + `prov:wasDerivedFrom` (hechos narrados) | CRM + PROV | sí | — |
| Quién reconstruye y por qué | `crminf:I5_Inference_Making` + `crm:P14_carried_out_by` (agente) + `crm:P3_has_note` (argumento) + `crm:P17_was_motivated_by` (E13 premisas) + `crm:P4_has_time-span` | CRMinf + CRM | sí | `crminf:J1_used_as_premise`: su rango es `I2_Belief`, no E13 |
| Creencia | `crminf:I2_Belief` + `crminf:J4_that` → `crminf:I4_Proposition_Set` (= el grafo nombrado de la reconstrucción) + `crminf:J5_holds_to_be` (literal) | CRMinf 1.2.1 | sí | `I6_Belief_Value` como clase: no existe en la 1.2.1 |
| Reconstrucciones en competencia | Dos grafos nombrados con creencias distintas (p. ej. R-declarante-p19-es-martin frente a -es-mariano) | — | — | Elegir una sola: el grafo no debe resolver en silencio |
| Fecha normalizada | Segundo `crm:E52_Time-Span` con `crm:P82a_begin_of_the_begin` / `crm:P82b_end_of_the_end` (xsd:date), en el grafo R-fechas-normalizadas | CRM | sí | Sobrescribir la fecha escrita |
| Cargo con vigencia | `crm:E7_Activity` + `P2_has_type cargo:*` + `PC14` + `P4_has_time-span` (ruta en `skos:editorialNote` de `atr:ejerce-cargo`) | CRM | sí (términos) | **No implementado en el mapeo** (ver `docs/C_modelo.md` §8) |

## Capa P — procedencia del dato (PROV-O)

| Necesidad | Término | Verif. |
|---|---|---|
| Cada grafo nombrado como entidad | `prov:Entity` + `dct:type` (capa) | sí |
| Proceso que lo generó | `prov:wasGeneratedBy` → `prov:Activity` + `prov:endedAtTime` | sí |
| Versión de la transcripción usada | `prov:used` → entidad con `dct:identifier "sha256:…"`; `prov:wasDerivedFrom` | sí |
| Modelo o anotador | `prov:wasAssociatedWith` / `prov:wasAttributedTo` → `prov:SoftwareAgent` o `prov:Person` | sí |
| Prompt o guía | `prov:qualifiedAssociation` → `prov:Association` + `prov:hadPlan` → `prov:Plan` | sí |
| Validador humano | `prov:Activity` (validación) + `prov:used` (grafo) + `prov:wasAssociatedWith` (persona) | sí |

## Tesauro SKOS (T)

Contiene 12 esquemas y 157 conceptos (`ontologia/tesauro.ttl`):

* actuaciones (17)
* roles (26)
* condiciones (11)
* cargos (34)
* entidades (12)
* atributos (27)
* polaridades (2)
* fundamentos (8)
* fuerzas (6)
* creencias (6)
* documentos (8)
* anotación (1)

Las alineaciones con PiCo están en `ontologia/ohac.ttl` (`skos:closeMatch` / `skos:relatedMatch`).

## Lo que OHAC añade

**Nada en la T-Box.** El análisis de carencias de `docs/C_modelo.md` §6 no encontró ninguna necesidad sin término estándar. OHAC se reduce a:

* el encabezado con las importaciones fijadas;
* el tesauro (datos);
* las formas SHACL (reglas del perfil);
* las alineaciones.
