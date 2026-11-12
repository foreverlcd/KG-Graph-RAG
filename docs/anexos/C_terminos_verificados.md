# Términos verificados en las especificaciones originales

Proyecto: modelo de datos para un expediente judicial colonial (Cusco, 1806). Fecha de verificación: 2026-11-12.

**Método.** Cada archivo se descargó con `scripts/fetch_vendor.sh` a `vendor/<estándar>/`, con sus sumas en `vendor/fuentes.sha256`.
Se parseó con rdflib (`.venv/bin/python -I`, script fuera de `vendor/`: `scratchpad/estandares/verificar.py`).
Un término cuenta como «verificado = sí» solo cuando su IRI aparece como sujeto en el grafo parseado del archivo descargado.
Dominio y rango son literales de `rdfs:domain`/`rdfs:range`; «(A ∪ B)» es un `owl:unionOf`. El extracto es el comienzo
literal de `skos:scopeNote` / `rdfs:comment` / `skos:definition`, en inglés, que es el idioma original.
La etiqueta «es:» es la `rdfs:label`/`skos:prefLabel` en castellano cuando el archivo la trae (solo RiC-O).

## Versiones obtenidas

| Estándar | Versión | Namespace exacto |
|---|---|---|
| RiC-O | 1.1, «Version 1.1 - 2025-05-22» | `https://www.ica.org/standards/RiC/ontology#` (vocabularios: `https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#`, `…/documentaryFormTypes#`) |
| CIDOC CRM | 7.1.3: es la última **oficial** con RDFS; 7.2.x–7.4 son borradores sin RDFS | `http://www.cidoc-crm.org/cidoc-crm/` (exactamente así: `http`, con `www`, barra final; los archivos lo fijan con `xml:base`). Términos como `…/cidoc-crm/E13_Attribute_Assignment` |
| CRMinf | 1.2.1 Stable (abril 2026) | `http://www.cidoc-crm.org/extensions/crminf/` |
| PROV-O | REC 2013-04-30 | `http://www.w3.org/ns/prov#` |
| SKOS | REC 2009 | `http://www.w3.org/2004/02/skos/core#` |
| SHACL | REC 2017 | `http://www.w3.org/ns/shacl#` (confirmado: `@prefix sh: <http://www.w3.org/ns/shacl#>` y `owl:Ontology` con esa IRI) |
| Web Annotation | REC 2017 (archivo 2016-11-12) | `http://www.w3.org/ns/oa#` |
| PiCo | 1.1.0 (2026-02-17) | modelo `https://personsincontext.org/model#` (prefijo `picom:`), más clases reutilizadas de `prov:`, `sdo:` (`https://schema.org/`) y `pnv:` |
| ROAR | 0.1 | `https://w3id.org/roar#` |

## Tablas por estándar

### ric-o

Tripletas parseadas: 16630. Ontologías declaradas: `https://www.ica.org/standards/RiC/ontology` ['Version 1.1 - 2025-05-22.'] ['https://www.ica.org/standards/RiC/ontology/1.1']

| término | IRI | tipo | dominio → rango | extracto nota de alcance | verificado |
|---|---|---|---|---|---|
| RecordSet | `https://www.ica.org/standards/RiC/ontology#RecordSet` | Class (⊑ RecordResource; es: «Agrupación documental») | — → — | «Record set is a kind of Record Resource. The member records in a Record Set may physically reside together, though physical proximity is not essential. In a particular context, an Agent (for example, administrator, records manager…» | sí |
| Record | `https://www.ica.org/standards/RiC/ontology#Record` | Class (⊑ RecordResource; es: «Documento») | — → — | «Record is a kind of Record Resource. A Record may itself contain one or more Records, or may consist of one or more Record Parts. A Record must have or have had at least one Instantiation. A Record may have more than one Instantia…» | sí |
| RecordPart | `https://www.ica.org/standards/RiC/ontology#RecordPart` | Class (⊑ RecordResource; es: «Componente documental») | — → — | «Record Part is a kind of Record Resource. A Record Part may itself have Record Parts.» | sí |
| Instantiation | `https://www.ica.org/standards/RiC/ontology#Instantiation` | Class (⊑ Thing; es: «Instanciación») | — → — | «A Record or Record Part must have been instantiated at least once, though this instantiation may no longer exist at the moment of description. An instantiation might also exist at the moment of description, but be destroyed at a l…» | sí |
| RecordSetType | `https://www.ica.org/standards/RiC/ontology#RecordSetType` | Class (⊑ Type; es: «Tipo de agrupación documental») | — → — | «Four instances of Record Set Type are included for now in RiC-O; they also are instances of skos:Concept and, as such, part of a SKOS vocabulary. Record Set Type may also be used (or extended) to categorize types of Record Set tha…» | sí |
| DocumentaryFormType | `https://www.ica.org/standards/RiC/ontology#DocumentaryFormType` | Class (⊑ Type; es: «Tipo documental») | — → — | «Documentary Form Type plays an important role in determining the type of information a Record may comprise, its status of perfection, and its authenticity and reliability. Documentary form types exist in a specific social and cult…» | sí |
| Identifier | `https://www.ica.org/standards/RiC/ontology#Identifier` | Class (⊑ Appellation; es: «Identificador») | — → — | «Can include Global Persistent Identifiers (globally unique and persistently resolvable identifier for the entity) and/or Local Identifiers. Both the domain within which the identifier is unique, and the rules used in forming the i…» | sí |
| Agent | `https://www.ica.org/standards/RiC/ontology#Agent` | Class (⊑ Thing; es: «Agente») | — → — | «An Agent may have one or more identities; an identity is a constellation of properties or relations that together “identify” the Agent. A Person or Group commonly has one identity, though each also may have one or more alternative…» | sí |
| Person | `https://www.ica.org/standards/RiC/ontology#Person` | Class (⊑ Agent; es: «Persona») | — → — | «Person is a kind of Agent. Most commonly, a human being (biological person) has a single socially constructed identity or persona. Less common though not rare, one or more personae in addition to the original persona which emerges…» | sí |
| Place | `https://www.ica.org/standards/RiC/ontology#Place` | Class (⊑ Thing; es: «Lugar») | — → — | «A jurisdiction is the bounded geographic area within which an Agent has the authority to perform specified activities constrained by rules. Jurisdictions, man-made structures, and natural features are historical entities. A Place …» | sí |
| Activity | `https://www.ica.org/standards/RiC/ontology#Activity` | Class (⊑ Event; es: «Actividad») | — → — | «Activity is a kind of Event. Activity is specifically used to designate purposeful human activity. Activity may be understood from two perspectives. First it can be understood as leading to an end. The end is the purpose of the Ac…» | sí |
| isOrWasIncludedIn | `https://www.ica.org/standards/RiC/ontology#isOrWasIncludedIn` | ObjectProperty (subPropertyOf isOrWasPartOf,isRecordResourceAssociatedWithRecordResource; inversa includesOrIncluded; es: «está o estaba incluido en») | (Record ∪ RecordSet) → RecordSet | «Inverse of 'includes or included' object property.» | sí |
| includesOrIncluded | `https://www.ica.org/standards/RiC/ontology#includesOrIncluded` | ObjectProperty (subPropertyOf hasOrHadPart,isRecordResourceAssociatedWithRecordResource; inversa isOrWasIncludedIn; es: «incluye o incluía») | RecordSet → (Record ∪ RecordSet) | «A Record or Record Set can be aggregated in one or many Record Sets simultaneously or through time.» | sí |
| hasOrHadConstituent | `https://www.ica.org/standards/RiC/ontology#hasOrHadConstituent` | ObjectProperty (subPropertyOf hasOrHadPart,isRecordResourceAssociatedWithRecordResource; inversa isOrWasConstituentOf; es: «tiene o tenía como elemento constitutivo») | (Record ∪ RecordPart) → (Record ∪ RecordPart) | «Connects a Record or Record Part to a Record or Record part that is or was a constituent of that Record or Record Part.» | sí |
| isOrWasConstituentOf | `https://www.ica.org/standards/RiC/ontology#isOrWasConstituentOf` | ObjectProperty (subPropertyOf isOrWasPartOf,isRecordResourceAssociatedWithRecordResource; inversa hasOrHadConstituent; es: «es o era elemento constitutivo de») | (Record ∪ RecordPart) → (Record ∪ RecordPart) | «Inverse of 'has or had constituent' object property.» | sí |
| hasOrHadPart | `https://www.ica.org/standards/RiC/ontology#hasOrHadPart` | ObjectProperty (subPropertyOf isRelatedTo; inversa isOrWasPartOf; es: «tiene o tenía como parte») | Thing → Thing | «Use to connect a Thing to another Thing that is or was a part of the whole Thing only if it is not possible to use a narrower, more specific whole/part relation, for example has or had constituent. The end of existence of a whole/…» | sí |
| isOrWasPartOf | `https://www.ica.org/standards/RiC/ontology#isOrWasPartOf` | ObjectProperty (subPropertyOf isRelatedTo; inversa hasOrHadPart; es: «es o era parte de») | Thing → Thing | «Inverse of 'has or had part' relation.» | sí |
| hasInstantiation | — | — | — | NO EXISTE en el archivo. Candidatos: ninguno | no |
| hasRecordSetType | `https://www.ica.org/standards/RiC/ontology#hasRecordSetType` | ObjectProperty (subPropertyOf hasOrHadType; inversa isRecordSetTypeOf; es: «tiene como tipo de agrupación documental») | RecordSet → RecordSetType | «Connects a Record Set to a Record Set Type that categorizes it.» | sí |
| hasDocumentaryFormType | `https://www.ica.org/standards/RiC/ontology#hasDocumentaryFormType` | ObjectProperty (subPropertyOf hasOrHadType; inversa isDocumentaryFormTypeOf; es: «tiene como tipo documental») | (Record ∪ RecordPart) → DocumentaryFormType | «Connects a Record or Record Part to its Documentary Form Type.» | sí |
| hasOrHadIdentifier | `https://www.ica.org/standards/RiC/ontology#hasOrHadIdentifier` | ObjectProperty (subPropertyOf hasOrHadAppellation; inversa isOrWasIdentifierOf; es: «tiene o tenía como identificador») | Thing → Identifier | «Connects a Thing to one of its past or present Identifiers.» | sí |
| identifier | `https://www.ica.org/standards/RiC/ontology#identifier` | DatatypeProperty (es: «identificador») | Thing → Literal | «Use only if you don't use Identifier class for handling identifiers. Within a given domain (a closed system), identifiers are used to uniquely reference instances of an entity. Identifiers are instruments of control that facilitat…» | sí |
| hasCreationDate | `https://www.ica.org/standards/RiC/ontology#hasCreationDate` | ObjectProperty (subPropertyOf hasBeginningDate,hasOrganicProvenanceDate; inversa isCreationDateOf; es: «tiene como fecha de creación») | (Instantiation ∪ RecordResource) → Date | «Inverse of 'is creation date of' object property» | sí |
| hasOrHadSubject | `https://www.ica.org/standards/RiC/ontology#hasOrHadSubject` | ObjectProperty (subPropertyOf isRelatedTo; inversa isOrWasSubjectOf; es: «tiene o tenía como materia») | RecordResource → Thing | «The subject of a Record Set may be affected if the Record Set loses some of the Records.» | sí |
| hasCreator | `https://www.ica.org/standards/RiC/ontology#hasCreator` | ObjectProperty (subPropertyOf hasOrganicProvenance; inversa isCreatorOf; es: «tiene como creador a») | (Instantiation ∪ RecordResource) → Agent | «Covers the definition of author in diplomatics, and any contribution to the intellectual content of a Record Resource.» | sí |
| title | `https://www.ica.org/standards/RiC/ontology#title` | DatatypeProperty (subPropertyOf name; es: «título») | (Instantiation ∪ RecordResource ∪ Rule) → Literal | «Use only if you don't use Title class for handling titles.» | sí |
| hasExtent | `https://www.ica.org/standards/RiC/ontology#hasExtent` | ObjectProperty (subPropertyOf isRelatedTo; inversa isExtentOf; es: «tiene como extensión») | Thing → Extent | «Connects a Record Resource or Instantiation to an Extent» | sí |
| recordResourceExtent | `https://www.ica.org/standards/RiC/ontology#recordResourceExtent` | DatatypeProperty (subPropertyOf physicalOrLogicalExtent; es: «soporte de recurso documental») | RecordResource → Literal | «Use if you don't use RecordResourceExtent class and its properties for handling such information. Record resource extent should not be confused with instantiation extent or carrier extent. The number, size or duration of the infor…» | sí |
| followsInSequence | — | — | — | NO EXISTE en el archivo. Candidatos: directlyFollowsInSequence, followsInSequenceTransitive, proxyDirectlyFollowsInSequence, proxyFollowsInSequence | no |
| precedesInSequence | — | — | — | NO EXISTE en el archivo. Candidatos: directlyPrecedesInSequence, precedesInSequenceTransitive, proxyDirectlyPrecedesInSequence, proxyPrecedesInSequence | no |
| hasOrHadHolder | `https://www.ica.org/standards/RiC/ontology#hasOrHadHolder` | ObjectProperty (subPropertyOf hasOrHadManager; inversa isOrWasHolderOf; es: «tiene o tenía como conservador a») | (Instantiation ∪ RecordResource) → Agent | «Inverse of 'is or was holder of' object property.» | sí |
| isOrWasHolderOf | `https://www.ica.org/standards/RiC/ontology#isOrWasHolderOf` | ObjectProperty (subPropertyOf isOrWasManagerOf; inversa hasOrHadHolder; es: «es o era conservador de») | Agent → (Instantiation ∪ RecordResource) | «Connects an Agent to a Record Resource or Instantiation that the Agent holds or held.» | sí |
| hasOrHadLocation | `https://www.ica.org/standards/RiC/ontology#hasOrHadLocation` | ObjectProperty (subPropertyOf isAssociatedWithPlace; inversa isOrWasLocationOf; es: «tiene o tenía como localización») | Thing → Place | «Inverse of 'is or was location of' object property.» | sí |
| hasOrHadInstantiation | `https://www.ica.org/standards/RiC/ontology#hasOrHadInstantiation` | ObjectProperty (subPropertyOf isRelatedTo; inversa isOrWasInstantiationOf; es: «tiene o tenía como instanciación») | RecordResource → Instantiation | «In some situations, it may be useful or necessary to connect a record resource to an instantiation that no longer exists or or has been lost, when some of its characteristics are known from some source, like an old finding aid.» | sí |
| isOrWasInstantiationOf | `https://www.ica.org/standards/RiC/ontology#isOrWasInstantiationOf` | ObjectProperty (subPropertyOf isRelatedTo; inversa hasOrHadInstantiation; es: «es o era instanciación de») | Instantiation → RecordResource | «Inverse of 'has or had instantiation' object property.» | sí |
| directlyFollowsInSequence | `https://www.ica.org/standards/RiC/ontology#directlyFollowsInSequence` | ObjectProperty (subPropertyOf followsInSequenceTransitive; inversa directlyPrecedesInSequence; es: «sigue directamente en la secuencia») | Thing → Thing | «Inverse of 'directly precedes in sequence' object property.» | sí |
| directlyPrecedesInSequence | `https://www.ica.org/standards/RiC/ontology#directlyPrecedesInSequence` | ObjectProperty (subPropertyOf precedesInSequenceTransitive; inversa directlyFollowsInSequence; es: «precede directamente en la secuencia») | Thing → Thing | «Connects a Thing to a Thing that it precedes directly in some sequence (not necessarily defined or characterised chronologically).» | sí |
| followsInSequenceTransitive | `https://www.ica.org/standards/RiC/ontology#followsInSequenceTransitive` | ObjectProperty,TransitiveProperty (subPropertyOf followsOrFollowed; inversa precedesInSequenceTransitive; es: «sigue en la secuencia transitivo») | Thing → Thing | «Inverse of 'precedes in sequence transitive' object property.» | sí |
| precedesInSequenceTransitive | `https://www.ica.org/standards/RiC/ontology#precedesInSequenceTransitive` | ObjectProperty,TransitiveProperty (subPropertyOf precedesOrPreceded; inversa followsInSequenceTransitive; es: «precede secuencialmente a transitivo») | Thing → Thing | «Connects a Thing to a Thing that follows it directly or indirectly in some sequence (not necessarily defined or characterised chronologically). This is a transitive relation.» | sí |
| rankInSequence | `https://www.ica.org/standards/RiC/ontology#rankInSequence` | DatatypeProperty (subPropertyOf textualValue; es: «rango en la secuencia») | (RecordResource ∪ Proxy) → int | «The object property rico:precedesOrPreceded or one of its sub-properties should always be used to express sequences in RiC-O. The rico:rankInSequence datatype property should only be used in addition (never independently), for con…» | sí |
| physicalOrLogicalExtent | `https://www.ica.org/standards/RiC/ontology#physicalOrLogicalExtent` | DatatypeProperty (es: «soporte físico o lógico») | (Instantiation ∪ RecordResource) → Literal | «Provided for usability reasons. Use only if you cannot use the subproperties (particularly if the same free text is being used in your current metadata for describing the record resource, carrier and instantiation extent).» | sí |
| RecordResourceExtent | `https://www.ica.org/standards/RiC/ontology#RecordResourceExtent` | Class (⊑ Extent; es: «Extensión de recurso documental») | — → — | «The method and precision of expressing the quantity of information represented in a Record Resource will vary according to the kind of record resource being described, processing economy constraints, etc. For Record Sets, quantity…» | sí |
| hasOrHadPhysicalLocation | `https://www.ica.org/standards/RiC/ontology#hasOrHadPhysicalLocation` | ObjectProperty (subPropertyOf isPlaceAssociatedWith; inversa isOrWasPhysicalLocationOf; es: «tiene o tenía como localización física») | Place → PhysicalLocation | «Connects a Place to one of its past or present Physical Location.» | sí |
| PhysicalLocation | `https://www.ica.org/standards/RiC/ontology#PhysicalLocation` | Class (⊑ Thing; es: «Localización física de lugar») | — → — | «Used to describe basic human-readable text such as an address, a cadastral reference, or less precise information found in a record. Use the coordinates datatype property, or the Coordinates class to capture the geographical coord…» | sí |
| location | `https://www.ica.org/standards/RiC/ontology#location` | DatatypeProperty (es: «localización») | Place → Literal | «Use only if you don't use PhysicalLocation class with Place. Use the geographicalCoordinates property, or the Coordinates class, to record the geographical coordinates of the Place. Use the spatial relations (particularly 'has or …» | sí |
| isOrWasSubjectOf | `https://www.ica.org/standards/RiC/ontology#isOrWasSubjectOf` | ObjectProperty (subPropertyOf isRelatedTo; inversa hasOrHadSubject; es: «es o era materia de») | Thing → RecordResource | «Inverse of 'has or had subject' object property.» | sí |
| hasOrHadCreator | — | — | — | NO EXISTE en el archivo. Candidatos: ninguno | no |
| creationDate | `https://www.ica.org/standards/RiC/ontology#creationDate` | DatatypeProperty (subPropertyOf beginningDate; es: «fecha de creación») | (Instantiation ∪ RecordResource) → Literal | «Provided for usability reasons. May be deprecated and removed later on. Use only if you don't use Date classes for handling dates.» | sí |
| date | `https://www.ica.org/standards/RiC/ontology#date` | DatatypeProperty (es: «fecha») | Thing → Literal | «Provided for usability reasons, like its subproperties. May be deprecated and removed later on. Use only if you don't use Date classes for handling dates.» | sí |
| RecordState | `https://www.ica.org/standards/RiC/ontology#RecordState` | Class (⊑ Type; es: «Estado de documento») | — → — | «Can refer both to a record's stage of creation (for example "draft") and its form of transmission when the record was received (for example "copy").» | sí |

#### Todos los términos declarados (ric-o)

| término | IRI | tipo | dominio → rango | extracto nota de alcance | verificado |
|---|---|---|---|---|---|
| authority record | `https://www.ica.org/standards/RiC/vocabularies/documentaryFormTypes#AuthorityRecord` | Concept,DocumentaryFormType,NamedIndividual (es: «registro de autoridad») | — → — | «This category can be used for records that describe an entity.» | sí |
| finding aid | `https://www.ica.org/standards/RiC/vocabularies/documentaryFormTypes#FindingAid` | Concept,DocumentaryFormType,NamedIndividual (es: «instrumento de descripción») | — → — | «This documentary form type can be used for records that aggregate and organizes metadata on some record(s) or record set(s).» | sí |
| IIIF manifest | `https://www.ica.org/standards/RiC/vocabularies/documentaryFormTypes#IIIFManifest` | Concept,DocumentaryFormType,NamedIndividual | — → — | «Can be used to categorize records which describe collections of cultural heritage objects, or of a single cultural object, and whose instantiations are compliant to the IIIF Presentation API.» | sí |
| collection | `https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#Collection` | Concept,NamedIndividual,RecordSetType (es: «colección») | — → — | «An artificial assemblage of documents accumulated on the basis of some common characteristic without regard to the provenance of those documents. Not to be confused with an archival fonds. (From ICA ISAD(G))» | sí |
| file | `https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#File` | Concept,NamedIndividual,RecordSetType (es: «expediente») | — → — | «An organized unit of documents grouped together either for current use by the creator or in the process of archival arrangement, because they relate to the same subject, activity, or transaction. A file is usually the basic unit w…» | sí |
| fonds | `https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#Fonds` | Concept,NamedIndividual,RecordSetType (es: «fondo») | — → — | «The whole of the records, regardless of form or medium, organically created and/or accumulated and used by a particular person, family, or corporate body in the course of that creator's activities and functions. (From ICA ISAD(G))» | sí |
| series | `https://www.ica.org/standards/RiC/vocabularies/recordSetTypes#Series` | Concept,NamedIndividual,RecordSetType (es: «serie») | — → — | «Documents arranged in accordance with a filing system or maintained as a unit because they result from the same accumulation or filing process, or the same activity; have a particular form; or because of some other relationship ar…» | sí |

### crm

Tripletas parseadas: 4425. Ontologías declaradas: `http://www.cidoc-crm.org/cidoc-crm/` ['RDFs Implementation (February 2024) of CIDOC-CRM 7.1.3'] ['http://www.cidoc-crm.org/cidoc-crm/7.1.3/']

| término | IRI | tipo | dominio → rango | extracto nota de alcance | verificado |
|---|---|---|---|---|---|
| E1 | `http://www.cidoc-crm.org/cidoc-crm/E1_CRM_Entity` | Class | — → — | «Scope note: This class comprises all things in the universe of discourse of the CIDOC Conceptual Reference Model. It is an abstract concept providing for three general properties: - Identification by name or appellation, and in pa…» | sí |
| E5_Event | `http://www.cidoc-crm.org/cidoc-crm/E5_Event` | Class (⊑ E4_Period) | — → — | «Scope note: This class comprises distinct, delimited and coherent processes and interactions of a material nature, in cultural, social or physical systems, involving and affecting instances of E77 Persistent Item in a way characte…» | sí |
| E7_Activity | `http://www.cidoc-crm.org/cidoc-crm/E7_Activity` | Class (⊑ E5_Event) | — → — | «Scope note: This class comprises actions intentionally carried out by instances of E39 Actor that result in changes of state in the cultural, social, or physical systems documented. This notion includes complex, composite, and lon…» | sí |
| E13_Attribute_Assignment | `http://www.cidoc-crm.org/cidoc-crm/E13_Attribute_Assignment` | Class (⊑ E7_Activity) | — → — | «Scope note: This class comprises the actions of making assertions about one property of an object or any single relation between two items or concepts. The type of the property asserted to hold between two items or concepts can be…» | sí |
| E21_Person | `http://www.cidoc-crm.org/cidoc-crm/E21_Person` | Class (⊑ E20_Biological_Object,E39_Actor) | — → — | «Scope note: This class comprises real persons who live or are assumed to have lived. Legendary figures that may have existed, such as Ulysses and King Arthur, fall into this class if the documentation refers to them as historical …» | sí |
| E31_Document | `http://www.cidoc-crm.org/cidoc-crm/E31_Document` | Class (⊑ E73_Information_Object) | — → — | «Scope note: This class comprises identifiable immaterial items that make propositions about reality. These propositions may be expressed in text, graphics, images, audiograms, videograms, or by other similar means. Documentation d…» | sí |
| E33_Linguistic_Object | `http://www.cidoc-crm.org/cidoc-crm/E33_Linguistic_Object` | Class (⊑ E73_Information_Object) | — → — | «Scope note: This class comprises identifiable expressions in natural language or languages. Instances of E33 Linguistic Object can be expressed in many ways: e.g. as written texts, recorded speech, or sign language. However, the C…» | sí |
| E39_Actor | `http://www.cidoc-crm.org/cidoc-crm/E39_Actor` | Class (⊑ E77_Persistent_Item) | — → — | «Scope note: This class comprises people, either individually or in groups, who have the potential to perform intentional actions of kinds for which they can be held responsible. Examples: - London and Continental Railways (E74) - …» | sí |
| E41_Appellation | `http://www.cidoc-crm.org/cidoc-crm/E41_Appellation` | Class (⊑ E90_Symbolic_Object) | — → — | «Scope note: This class comprises all signs, either meaningful or not, or arrangements of signs following a specific syntax, that are used or can be used to refer to and identify a specific instance of some class within a certain c…» | sí |
| E42_Identifier | `http://www.cidoc-crm.org/cidoc-crm/E42_Identifier` | Class (⊑ E41_Appellation) | — → — | «Scope note: This class comprises strings or codes assigned to instances of E1 CRM Entity in order to identify them uniquely and permanently within the context of one or more organisations. Such codes are often known as inventory n…» | sí |
| E52_Time-Span | `http://www.cidoc-crm.org/cidoc-crm/E52_Time-Span` | Class (⊑ E1_CRM_Entity) | — → — | «Scope note: This class comprises abstract temporal extents, in the sense of Galilean physics, having a beginning, an end, and a duration. Instances of E52 Time-Span have no semantic connotations about phenomena happening within th…» | sí |
| E53_Place | `http://www.cidoc-crm.org/cidoc-crm/E53_Place` | Class (⊑ E1_CRM_Entity) | — → — | «Scope note: This class comprises extents in the natural space where people live, in particular on the surface of the Earth, in the pure sense of physics: independent from temporal phenomena and matter. They may serve describing th…» | sí |
| E55_Type | `http://www.cidoc-crm.org/cidoc-crm/E55_Type` | Class (⊑ E28_Conceptual_Object) | — → — | «Scope note: This class comprises concepts denoted by terms from thesauri and controlled vocabularies used to characterize and classify instances of CIDOC CRM classes. Instances of E55 Type represent concepts, in contrast to instan…» | sí |
| E65_Creation | `http://www.cidoc-crm.org/cidoc-crm/E65_Creation` | Class (⊑ E63_Beginning_of_Existence,E7_Activity) | — → — | «Scope note: This class comprises events that result in the creation of conceptual items or immaterial products, such as legends, poems, texts, music, images, movies, laws, types, etc. Examples: - the framing of the U.S. Constituti…» | sí |
| E73_Information_Object | `http://www.cidoc-crm.org/cidoc-crm/E73_Information_Object` | Class (⊑ E89_Propositional_Object,E90_Symbolic_Object) | — → — | «Scope note: This class comprises identifiable immaterial items, such as poems, jokes, data sets, images, texts, multimedia objects, procedural prescriptions, computer program code, algorithm or mathematical formulae, that have an …» | sí |
| E74_Group | `http://www.cidoc-crm.org/cidoc-crm/E74_Group` | Class (⊑ E39_Actor) | — → — | «Scope note: This class comprises any gatherings or organizations of human individuals or groups that act collectively or in a similar way due to any form of unifying relationship. In the wider sense this class also comprises offic…» | sí |
| E89_Propositional_Object | `http://www.cidoc-crm.org/cidoc-crm/E89_Propositional_Object` | Class (⊑ E28_Conceptual_Object) | — → — | «Scope note: This class comprises immaterial items, including but not limited to stories, plots, procedural prescriptions, algorithms, laws of physics or images that are, or represent in some sense, sets of propositions about real …» | sí |
| E90_Symbolic_Object | `http://www.cidoc-crm.org/cidoc-crm/E90_Symbolic_Object` | Class (⊑ E28_Conceptual_Object,E72_Legal_Object) | — → — | «Scope note: This class comprises identifiable symbols and any aggregation of symbols, such as characters, identifiers, traffic signs, emblems, texts, data sets, images, musical scores, multimedia objects, computer program code, or…» | sí |
| P1_is_identified_by | `http://www.cidoc-crm.org/cidoc-crm/P1_is_identified_by` | Property (inversa P1i_identifies) | E1_CRM_Entity → E41_Appellation | «Quantification: many to many (0,n:0,n) Scope note: This property describes the naming or identification of any real-world item by a name or any other identifier. This property is intended for identifiers in general use, which form…» | sí |
| P2_has_type | `http://www.cidoc-crm.org/cidoc-crm/P2_has_type` | Property (inversa P2i_is_type_of) | E1_CRM_Entity → E55_Type | «Quantification: many to many (0,n:0,n) Scope note: This property allows sub-typing of CIDOC CRM entities –a form of specialisation – through the use of a terminological hierarchy, or thesaurus. The CIDOC CRM is intended to focus o…» | sí |
| P3_has_note | `http://www.cidoc-crm.org/cidoc-crm/P3_has_note` | Property | E1_CRM_Entity → Literal | «Quantification: one to many (0,n:0,1) Scope note: This property is a container for all informal descriptions about an object that have not been expressed in terms of CIDOC CRM constructs. In particular, it captures the characteris…» | sí |
| P4_has_time-span | `http://www.cidoc-crm.org/cidoc-crm/P4_has_time-span` | Property (inversa P4i_is_time-span_of) | E2_Temporal_Entity → E52_Time-Span | «Quantification: many to one, necessary (1,1:0,n) Scope note: This property associates an instance of E2 Temporal Entity with the instance of E52 Time-Span during which it was on-going. The associated instance of E52 Time-Span is u…» | sí |
| P7_took_place_at | `http://www.cidoc-crm.org/cidoc-crm/P7_took_place_at` | Property (inversa P7i_witnessed) | E4_Period → E53_Place | «Quantification: many to many, necessary (1,n:0,n) Scope note: This property describes the spatial location of an instance of E4 Period. The related instance of E53 Place should be seen as a wider approximation of the geometric are…» | sí |
| P11_had_participant | `http://www.cidoc-crm.org/cidoc-crm/P11_had_participant` | Property (subPropertyOf P12_occurred_in_the_presence_of; inversa P11i_participated_in) | E5_Event → E39_Actor | «Quantification: many to many (0,n:0,n) Scope note: This property describes the active or passive participation of instances of E39 Actors in an instance of E5 Event. It documents known events in which an instance of E39 Actor has …» | sí |
| P14_carried_out_by | `http://www.cidoc-crm.org/cidoc-crm/P14_carried_out_by` | Property (subPropertyOf P11_had_participant; inversa P14i_performed) | E7_Activity → E39_Actor | «Quantification: many to many, necessary (1,n:0,n) Scope note: This property describes the active participation of an instance of E39 Actor in an instance of E7 Activity. It implies causal or legal responsibility. The P14.1 in the …» | sí |
| P14.1_in_the_role_of | `http://www.cidoc-crm.org/cidoc-crm/P14.1_in_the_role_of` | Property | PC14_carried_out_by → E55_Type | «» | sí |
| PC14_carried_out_by | `http://www.cidoc-crm.org/cidoc-crm/PC14_carried_out_by` | Class (⊑ PC0_Typed_CRM_Property) | — → — | «This class is the representation of the n-ary relationship form of the property 'P14 carried out by'. This property describes the active participation of an instance of E39 Actor in an instance of E7 Activity. It implies causal or…» | sí |
| P01_has_domain | `http://www.cidoc-crm.org/cidoc-crm/P01_has_domain` | Property (inversa P01i_is_domain_of) | PC0_Typed_CRM_Property → E1_CRM_Entity | «This property associates an instance of a property class with an instance of the property's domain class. For example, it links an instance of 'PC14 carried out by' (the property class of 'P14 carried out by') with an instance of …» | sí |
| P02_has_range | `http://www.cidoc-crm.org/cidoc-crm/P02_has_range` | Property (inversa P02i_is_range_of) | PC0_Typed_CRM_Property → E1_CRM_Entity | «This property associates an instance of a property class with an instance of the property's range class. For example, it links an instance of 'PC14 carried out by' (the property class of 'P14 carried out by') with an instance of '…» | sí |
| P67_refers_to | `http://www.cidoc-crm.org/cidoc-crm/P67_refers_to` | Property (inversa P67i_is_referred_to_by) | E89_Propositional_Object → E1_CRM_Entity | «Quantification: many to many (0,n:0,n) Scope note: This property documents that an instance of E89 Propositional Object makes a statement about an instance of E1 CRM Entity. P67 refers to (is referred to by) has the P67.1 has type…» | sí |
| P70_documents | `http://www.cidoc-crm.org/cidoc-crm/P70_documents` | Property (subPropertyOf P67_refers_to; inversa P70i_is_documented_in) | E31_Document → E1_CRM_Entity | «Quantification: many to many, necessary (1,n:0,n) Scope note: This property describes the CRM Entities documented as instances of E31 Document. Documents may describe any conceivable entity, hence the link to the highest-level ent…» | sí |
| P82a_begin_of_the_begin | `http://www.cidoc-crm.org/cidoc-crm/P82a_begin_of_the_begin` | Property (subPropertyOf P82_at_some_time_within) | E52_Time-Span → Literal | «» | sí |
| P82b_end_of_the_end | `http://www.cidoc-crm.org/cidoc-crm/P82b_end_of_the_end` | Property (subPropertyOf P82_at_some_time_within) | E52_Time-Span → Literal | «» | sí |
| P94_has_created | `http://www.cidoc-crm.org/cidoc-crm/P94_has_created` | Property (subPropertyOf P92_brought_into_existence; inversa P94i_was_created_by) | E65_Creation → E28_Conceptual_Object | «Quantification: one to many, necessary, dependent (1,n:1,1) Scope note: This property links an instance of E65 Creation to the instance of E28 Conceptual Object created by it. It represents the act of conceiving the intellectual c…» | sí |
| P106_is_composed_of | `http://www.cidoc-crm.org/cidoc-crm/P106_is_composed_of` | Property (inversa P106i_forms_part_of) | E90_Symbolic_Object → E90_Symbolic_Object | «Quantification: many to many (0,n:0,n) Scope note: This property associates an instance of E90 Symbolic Object with a part of it that is by itself an instance of E90 Symbolic Object, such as fragments of texts or clippings from an…» | sí |
| P129_is_about | `http://www.cidoc-crm.org/cidoc-crm/P129_is_about` | Property (subPropertyOf P67_refers_to; inversa P129i_is_subject_of) | E89_Propositional_Object → E1_CRM_Entity | «Quantification: many to many (0,n:0,n) Scope note: This property documents that an instance of E89 Propositional Object has as subject an instance of E1 CRM Entity. This differs from P67 refers to (is referred to by), which refers…» | sí |
| P140_assigned_attribute_to | `http://www.cidoc-crm.org/cidoc-crm/P140_assigned_attribute_to` | Property (inversa P140i_was_attributed_by) | E13_Attribute_Assignment → E1_CRM_Entity | «Quantification: many to many (0,n:0,n) Scope note: This property associates an instance of E13 Attribute Assignment with the instance of E1 CRM Entity about which it made an attribution. The instance of E1 CRM Entity plays the rol…» | sí |
| P141_assigned | `http://www.cidoc-crm.org/cidoc-crm/P141_assigned` | Property (inversa P141i_was_assigned_by) | E13_Attribute_Assignment → E1_CRM_Entity | «Quantification: many to many (0,n:0,n) Scope note: This property associates an instance of E13 Attribute Assignment with the instance of E1 CRM Entity used in the attribution. The instance of E1 CRM Entity here plays the role of t…» | sí |
| P177_assigned_property_of_type | `http://www.cidoc-crm.org/cidoc-crm/P177_assigned_property_of_type` | Property (subPropertyOf P2_has_type; inversa P177i_is_type_of_property_assigned) | E13_Attribute_Assignment → E55_Type | «Quantification: many to many, necessary (1,n:0,n) Scope note: This property associates an instance of E13 Attribute Assignment with the type of property or relation that this assignment maintains to hold between the item to which …» | sí |
| P190_has_symbolic_content | `http://www.cidoc-crm.org/cidoc-crm/P190_has_symbolic_content` | Property (subPropertyOf P3_has_note) | E90_Symbolic_Object → Literal | «Quantification: many to many (0,n:0,n) Scope note: This property associates an instance of E90 Symbolic Object with a complete, identifying representation of its content in the form of an instance of E62 String. This property only…» | sí |
| P17_was_motivated_by | `http://www.cidoc-crm.org/cidoc-crm/P17_was_motivated_by` | Property (subPropertyOf P15_was_influenced_by; inversa P17i_motivated) | E7_Activity → E1_CRM_Entity | «Quantification: many to many (0,n:0,n) Scope note: This property describes an item or items that are regarded as a reason for carrying out the instance of E7 Activity. For example, the discovery of a large hoard of treasure may ca…» | sí |
| P107_has_current_or_former_member | `http://www.cidoc-crm.org/cidoc-crm/P107_has_current_or_former_member` | Property (inversa P107i_is_current_or_former_member_of) | E74_Group → E39_Actor | «Quantification: many to many (0,n:0,n) Scope note: This property associates an instance of E74 Group with an instance of E39 Actor that is or has been a member thereof. Instances of E74 Group and E21 Person may all be members of i…» | sí |

### crminf

Tripletas parseadas: 419. Ontologías declaradas: `http://www.cidoc-crm.org/extensions/crminf/` ['CRMinf 1.2.1 (Stable) (April, 2026) including references to CIDOC-CRM 7.1.3 and CRMsci 3.2'] ['http://www.cidoc-crm.org/extensions/crminf/1.2.1/']

| término | IRI | tipo | dominio → rango | extracto nota de alcance | verificado |
|---|---|---|---|---|---|
| I1_Argumentation | `http://www.cidoc-crm.org/extensions/crminf/I1_Argumentation` | Class (⊑ E7_Activity) | — → — | «Scope note: This class comprises the activity of making honest inferences or observations. An honest inference or observation is one, in which the E39 Actor carrying out the I1 Argumentation justifies and believes that the I6 Beli…» | sí |
| I3_Inference_Logic | `http://www.cidoc-crm.org/extensions/crminf/I3_Inference_Logic` | Class (⊑ E89_Propositional_Object) | — → — | «Scope note: This class comprises the rules used as inputs to I5 Inference Making. In this context, the term “logic” is used in the most general sense of the Greek term, and not in the mathematical sense only. Examples are the dire…» | sí |
| J3_applied | `http://www.cidoc-crm.org/extensions/crminf/J3_applied` | Property (subPropertyOf P16_used_specific_object; inversa J3i_was_applied_by) | I5_Inference_Making → I3_Inference_Logic | «Quantification: many to many, necessary (1,n:0,n) Scope note: This property associates an instance of I3 Inference Logic with the instance of I5 Inference Making that used it to draw its conclusion. Examples: - the gender classifi…» | sí |
| I2_Belief | `http://www.cidoc-crm.org/extensions/crminf/I2_Belief` | Class (⊑ E2_Temporal_Entity) | — → — | «Scope note: This class comprises the notion that the associated I4 Proposition Set is to have a particular I6 Belief Value by a particular E39 Actor. This can be understood as the period of time that an individual group holds a pa…» | sí |
| I4_Proposition_Set | `http://www.cidoc-crm.org/extensions/crminf/I4_Proposition_Set` | Class (⊑ E89_Propositional_Object) | — → — | «Scope note: This class comprises sets of unambiguous propositions that are, or could, in principle, be, encoded in a knowledge representation language. These propositions should be factual, i.e., each proposition should pertain to…» | sí |
| I5_Inference_Making | `http://www.cidoc-crm.org/extensions/crminf/I5_Inference_Making` | Class (⊑ I1_Argumentation) | — → — | «Scope note: This class comprises the action of making honest propositions and statements about particular states of affairs in reality or possible realities, or categorical descriptions of reality by using inferences from other st…» | sí |
| I6_Belief_Value | — | — | — | NO EXISTE en el archivo. Candidatos: ninguno | no |
| I7_Belief_Adoption | `http://www.cidoc-crm.org/extensions/crminf/I7_Belief_Adoption` | Class (⊑ I1_Argumentation) | — → — | «Scope note: This class comprises the action of an E39 Actor adopting propositions taken from an interpretation of the intended meaning of an instance of E73 Information Object as being true, or in some way likely to be true. The a…» | sí |
| J1_used_as_premise | `http://www.cidoc-crm.org/extensions/crminf/J1_used_as_premise` | Property (subPropertyOf P17_was_motivated_by; inversa J1i_was_premise_for) | I5_Inference_Making → I2_Belief | «Quantification: many to many, necessary (1,n:0,n) Scope note: This property associates an instance of I2 Belief with the instance of I5 Inference Making that used it as a premise. Examples: - the gender classification of the skele…» | sí |
| J2_concluded_that | `http://www.cidoc-crm.org/extensions/crminf/J2_concluded_that` | Property (subPropertyOf P175_starts_before_or_with_the_start_of,P175i_starts_after_or_with_the_start_of,P185_ends_before_the_end_of; inversa J2i_was_concluded_by) | I1_Argumentation → I2_Belief | «Quantification: one to many, necessary, dependent (1,n:1,1) Scope note: This property associates an instance of I2 Belief with the instance of I1 Argumentation that concluded it. Examples: - Ian Hodder’s re-examination, in 1996, o…» | sí |
| J4_that | `http://www.cidoc-crm.org/extensions/crminf/J4_that` | Property (inversa J4i_is_subject_of) | I2_Belief → I4_Proposition_Set | «Quantification: many to one, necessary (1,1:0,n) Scope note: This property associates an instance of I4 Proposition Set with the instance of I2 Belief that holds an opinion about it. This property is part of the fully developed pa…» | sí |
| J5_holds_to_be | `http://www.cidoc-crm.org/extensions/crminf/J5_holds_to_be` | Property | I2_Belief → Literal | «Quantification: many to one, necessary (1,1:0,n) Scope note: This property associates an instance of I2 Belief with the I6 Belief Value that reflects the opinion of a particular E39 Actor about the truth of the associated I4 Propo…» | sí |
| J6_adopted | — | — | — | NO EXISTE en el archivo. Candidatos: ninguno | no |
| J7 | `http://www.cidoc-crm.org/extensions/crminf/J7i_is_evidence_for` | Property (subPropertyOf P16i_was_used_for; inversa J7_is_based_on_evidence_from) | E73_Information_Object → I7_Belief_Adoption | «Quantification of the inverse property: many to many, necessary (1,n:0,n) Scope note of the inverse property: This property associates an instance of I7 Belief Adoption with the instance of E73 Information Object that is a source …» | sí |
| J7 | `http://www.cidoc-crm.org/extensions/crminf/J7_is_based_on_evidence_from` | Property (subPropertyOf P16_used_specific_object; inversa J7i_is_evidence_for) | I7_Belief_Adoption → E73_Information_Object | «Quantification: many to many, necessary (1,n:0,n) Scope note: This property associates an instance of I7 Belief Adoption with the instance of E73 Information Object that is a source of evidence for the I4 Proposition Set that was …» | sí |

### prov

Tripletas parseadas: 1146. Ontologías declaradas: `http://www.w3.org/ns/prov#` [] []; `http://www.w3.org/ns/prov-o#` ['Recommendation version 2013-04-30'] ['http://www.w3.org/ns/prov-o-20130430']

| término | IRI | tipo | dominio → rango | extracto nota de alcance | verificado |
|---|---|---|---|---|---|
| Entity | `http://www.w3.org/ns/prov#Entity` | Class | — → — | «» | sí |
| Activity | `http://www.w3.org/ns/prov#Activity` | Class | — → — | «» | sí |
| Agent | `http://www.w3.org/ns/prov#Agent` | Class | — → — | «» | sí |
| SoftwareAgent | `http://www.w3.org/ns/prov#SoftwareAgent` | Class (⊑ Agent) | — → — | «» | sí |
| Person | `http://www.w3.org/ns/prov#Person` | Class (⊑ Agent) | — → — | «» | sí |
| Plan | `http://www.w3.org/ns/prov#Plan` | Class (⊑ Entity) | — → — | «There exist no prescriptive requirement on the nature of plans, their representation, the actions or steps they consist of, or their intended goals. Since plans may evolve over time, it may become necessary to track their provenan…» | sí |
| wasDerivedFrom | `http://www.w3.org/ns/prov#wasDerivedFrom` | ObjectProperty (subPropertyOf wasInfluencedBy) | Entity → Entity | «The more specific subproperties of prov:wasDerivedFrom (i.e., prov:wasQuotedFrom, prov:wasRevisionOf, prov:hadPrimarySource) should be used when applicable.» | sí |
| wasGeneratedBy | `http://www.w3.org/ns/prov#wasGeneratedBy` | ObjectProperty (subPropertyOf wasInfluencedBy) | Entity → Activity | «» | sí |
| used | `http://www.w3.org/ns/prov#used` | ObjectProperty (subPropertyOf wasInfluencedBy) | Activity → Entity | «A prov:Entity that was used by this prov:Activity. For example, :baking prov:used :spoon, :egg, :oven .» | sí |
| wasAssociatedWith | `http://www.w3.org/ns/prov#wasAssociatedWith` | ObjectProperty (subPropertyOf wasInfluencedBy) | Activity → Agent | «An prov:Agent that had some (unspecified) responsibility for the occurrence of this prov:Activity.» | sí |
| qualifiedAssociation | `http://www.w3.org/ns/prov#qualifiedAssociation` | ObjectProperty (subPropertyOf qualifiedInfluence) | Activity → Association | «If this Activity prov:wasAssociatedWith Agent :ag, then it can qualify the Association using prov:qualifiedAssociation [ a prov:Association; prov:agent :ag; :foo :bar ].» | sí |
| hadPlan | `http://www.w3.org/ns/prov#hadPlan` | ObjectProperty | Association → Plan | «The _optional_ Plan adopted by an Agent in Association with some Activity. Plan specifications are out of the scope of this specification.» | sí |
| wasAttributedTo | `http://www.w3.org/ns/prov#wasAttributedTo` | ObjectProperty (subPropertyOf wasInfluencedBy) | Entity → Agent | «Attribution is the ascribing of an entity to an agent.» | sí |
| generatedAtTime | `http://www.w3.org/ns/prov#generatedAtTime` | DatatypeProperty | Entity → dateTime | «The time at which an entity was completely created and is available for use.» | sí |
| wasRevisionOf | `http://www.w3.org/ns/prov#wasRevisionOf` | AnnotationProperty,ObjectProperty (subPropertyOf wasDerivedFrom) | Entity → Entity | «A revision is a derivation that revises an entity into a revised version.» | sí |
| hadPrimarySource | `http://www.w3.org/ns/prov#hadPrimarySource` | ObjectProperty (subPropertyOf wasDerivedFrom) | Entity → Entity | «» | sí |
| wasQuotedFrom | `http://www.w3.org/ns/prov#wasQuotedFrom` | ObjectProperty (subPropertyOf wasDerivedFrom) | Entity → Entity | «An entity is derived from an original entity by copying, or 'quoting', some or all of it.» | sí |

### skos

Tripletas parseadas: 252. Ontologías declaradas: `http://www.w3.org/2004/02/skos/core` [] []

| término | IRI | tipo | dominio → rango | extracto nota de alcance | verificado |
|---|---|---|---|---|---|
| ConceptScheme | `http://www.w3.org/2004/02/skos/core#ConceptScheme` | Class | — → — | «A concept scheme may be defined to include concepts from different sources.» | sí |
| Concept | `http://www.w3.org/2004/02/skos/core#Concept` | Class | — → — | «An idea or notion; a unit of thought.» | sí |
| prefLabel | `http://www.w3.org/2004/02/skos/core#prefLabel` | AnnotationProperty,Property (subPropertyOf label) | — → — | «A resource has no more than one value of skos:prefLabel per language tag, and no more than one value of skos:prefLabel without language tag.» | sí |
| altLabel | `http://www.w3.org/2004/02/skos/core#altLabel` | AnnotationProperty,Property (subPropertyOf label) | — → — | «The range of skos:altLabel is the class of RDF plain literals.» | sí |
| hiddenLabel | `http://www.w3.org/2004/02/skos/core#hiddenLabel` | AnnotationProperty,Property (subPropertyOf label) | — → — | «The range of skos:hiddenLabel is the class of RDF plain literals.» | sí |
| definition | `http://www.w3.org/2004/02/skos/core#definition` | AnnotationProperty,Property (subPropertyOf note) | — → — | «A statement or formal explanation of the meaning of a concept.» | sí |
| scopeNote | `http://www.w3.org/2004/02/skos/core#scopeNote` | AnnotationProperty,Property (subPropertyOf note) | — → — | «A note that helps to clarify the meaning and/or the use of a concept.» | sí |
| broader | `http://www.w3.org/2004/02/skos/core#broader` | ObjectProperty,Property (subPropertyOf broaderTransitive; inversa narrower) | — → — | «By convention, skos:broader is only used to assert an immediate (i.e. direct) hierarchical link between two conceptual resources.» | sí |
| narrower | `http://www.w3.org/2004/02/skos/core#narrower` | ObjectProperty,Property (subPropertyOf narrowerTransitive; inversa broader) | — → — | «By convention, skos:broader is only used to assert an immediate (i.e. direct) hierarchical link between two conceptual resources.» | sí |
| exactMatch | `http://www.w3.org/2004/02/skos/core#exactMatch` | ObjectProperty,Property,SymmetricProperty,TransitiveProperty (subPropertyOf closeMatch) | — → — | «skos:exactMatch is disjoint with each of the properties skos:broadMatch and skos:relatedMatch.» | sí |
| closeMatch | `http://www.w3.org/2004/02/skos/core#closeMatch` | ObjectProperty,Property,SymmetricProperty (subPropertyOf mappingRelation) | — → — | «skos:closeMatch is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications. In order to avoid the possibility of "compound errors" when combining map…» | sí |
| inScheme | `http://www.w3.org/2004/02/skos/core#inScheme` | ObjectProperty,Property | — → ConceptScheme | «A concept may be a member of more than one concept scheme.» | sí |
| hasTopConcept | `http://www.w3.org/2004/02/skos/core#hasTopConcept` | ObjectProperty,Property (inversa topConceptOf) | ConceptScheme → Concept | «Relates, by convention, a concept scheme to a concept which is topmost in the broader/narrower concept hierarchies for that scheme, providing an entry point to these hierarchies.» | sí |
| notation | `http://www.w3.org/2004/02/skos/core#notation` | DatatypeProperty,Property | — → — | «By convention, skos:notation is used with a typed literal in the object position of the triple.» | sí |
| historyNote | `http://www.w3.org/2004/02/skos/core#historyNote` | AnnotationProperty,Property (subPropertyOf note) | — → — | «A note about the past state/use/meaning of a concept.» | sí |
| editorialNote | `http://www.w3.org/2004/02/skos/core#editorialNote` | AnnotationProperty,Property (subPropertyOf note) | — → — | «A note for an editor, translator or maintainer of the vocabulary.» | sí |

### shacl

Tripletas parseadas: 1128. Ontologías declaradas: `http://www.w3.org/ns/shacl#` [] []

### oa

Tripletas parseadas: 334. Ontologías declaradas: `http://www.w3.org/ns/oa#` ['2016-11-12T21:28:11Z'] []

| término | IRI | tipo | dominio → rango | extracto nota de alcance | verificado |
|---|---|---|---|---|---|
| Annotation | `http://www.w3.org/ns/oa#Annotation` | Class | — → — | «The class for Web Annotations.» | sí |
| hasTarget | `http://www.w3.org/ns/oa#hasTarget` | Property | Annotation → — | «The relationship between an Annotation and its Target.» | sí |
| hasSource | `http://www.w3.org/ns/oa#hasSource` | Property | ResourceSelection → — | «The resource that the ResourceSelection, or its subclass SpecificResource, is refined from, or more specific than. Please note that the domain ( oa:ResourceSelection ) is not used directly in the Web Annotation model.» | sí |
| hasSelector | `http://www.w3.org/ns/oa#hasSelector` | Property | ResourceSelection → Selector | «The object of the relationship is a Selector that describes the segment or region of interest within the source resource. Please note that the domain ( oa:ResourceSelection ) is not used directly in the Web Annotation model.» | sí |
| TextQuoteSelector | `http://www.w3.org/ns/oa#TextQuoteSelector` | Class (⊑ Selector) | — → — | «The TextQuoteSelector describes a range of text by copying it, and including some of the text immediately before (a prefix) and after (a suffix) it to distinguish between multiple copies of the same sequence of characters.» | sí |
| exact | `http://www.w3.org/ns/oa#exact` | Property | — → string | «The object of the predicate is a copy of the text which is being selected, after normalization.» | sí |
| prefix | `http://www.w3.org/ns/oa#prefix` | Property | — → string | «The object of the property is a snippet of content that occurs immediately before the content which is being selected by the Selector.» | sí |
| suffix | `http://www.w3.org/ns/oa#suffix` | Property | — → string | «The snippet of text that occurs immediately after the text which is being selected.» | sí |
| TextPositionSelector | `http://www.w3.org/ns/oa#TextPositionSelector` | Class (⊑ Selector) | — → — | «The TextPositionSelector describes a range of text by recording the start and end positions of the selection in the stream. Position 0 would be immediately before the first character, position 1 would be immediately before the sec…» | sí |
| start | `http://www.w3.org/ns/oa#start` | Property | — → nonNegativeInteger | «The start position in a 0-based index at which a range of content is selected from the data in the source resource.» | sí |
| end | `http://www.w3.org/ns/oa#end` | Property | — → nonNegativeInteger | «The end property is used to convey the 0-based index of the end position of a range of content.» | sí |
| SpecificResource | `http://www.w3.org/ns/oa#SpecificResource` | Class (⊑ ResourceSelection) | — → — | «Instances of the SpecificResource class identify part of another resource (referenced with oa:hasSource), a particular representation of a resource, a resource with styling hints for renders, or any combination of these, as used w…» | sí |

### pico

Tripletas parseadas: 714. Ontologías declaradas: `https://personsincontext.org/model` ['1.1.0'] []

#### Todos los términos declarados (pico)

| término | IRI | tipo | dominio → rango | extracto nota de alcance | verificado |
|---|---|---|---|---|---|
| Activity | `http://www.w3.org/ns/prov#Activity` | Class | — → — | «A Person Reconstruction can either be created by a human researcher or by a software algorithm. In case of a human-made reconstruction, provide information about the time, place and knowledge- input. In case of a software algorith…» | sí |
| Agent | `http://www.w3.org/ns/prov#Agent` | Class | — → — | «The agent (person or organisation) that is responsible for the creation of a person reconstruction.» | sí |
| endedAtTime | `http://www.w3.org/ns/prov#endedAtTime` | DatatypeProperty | — → — | «The end time of the activity that generated a Person Reconstruction.» | sí |
| hadPrimarySource | `http://www.w3.org/ns/prov#hadPrimarySource` | ObjectProperty | — → — | «A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight. Because of the directness of primary s…» | sí |
| startedAtTime | `http://www.w3.org/ns/prov#startedAtTime` | DatatypeProperty | — → — | «The start time of the activity that generated a Person Reconstruction.» | sí |
| wasAssociatedWith | `http://www.w3.org/ns/prov#wasAssociatedWith` | DatatypeProperty | — → — | «Assignment of responsibility to an agent for the activity of creating a person reconstruction.» | sí |
| wasDerivedFrom | `http://www.w3.org/ns/prov#wasDerivedFrom` | ObjectProperty | — → — | «A PersonReconstruction is always derived from one or more PersonObservations. The wasDerivedFrom property is therefore required for PersonReconstructions.» | sí |
| wasGeneratedBy | `http://www.w3.org/ns/prov#wasGeneratedBy` | ObjectProperty | — → — | «Required for PersonReconstructions.» | sí |
| wasRevisionOf | `http://www.w3.org/ns/prov#wasRevisionOf` | ObjectProperty | — → — | «The wasRevisionOf property is used for modifications made on Person reconstructions. It can be qualified with a prov:Revision.» | sí |
| Persons in Context | `https://personsincontext.org/model` | Ontology | — → — | «Persons in Context, abbreviated as PiCo, is a knowledge model for annotating and publishing person observations from historical sources. A main characteristic of PiCo is the distinction between Person observations (person data as …» | sí |
| LifeEvent | `https://personsincontext.org/model#LifeEvent` | Class | — → — | «Life events in PiCo are used for modelling important events in the life of a Person, such as baptism, marriage or burial. Events are primarily used to identify a Person or provide a date and/or a location for a specific milestone …» | sí |
| Person | `https://personsincontext.org/model#Person` | Class (⊑ Entity,Person) | — → — | «Container class for Person observation and Person reconstruction. Not to be used directly in PiCo resources.» | sí |
| PersonObservation | `https://personsincontext.org/model#PersonObservation` | Class (⊑ Person) | — → — | «A person observation represents how a person is recorded on a Source. Therefore, it must always be related to a source. Person observations closely reflect data as it appears in the source, that is, with the age, occupation, and s…» | sí |
| PersonReconstruction | `https://personsincontext.org/model#PersonReconstruction` | Class (⊑ Person) | — → — | «A Person reconstruction must always refer to one or more Person observations. For this, the prov:wasDerivedFrom property is used. Information about the creation should be documented with the prov:wasGeneratedBy property. Informati…» | sí |
| deceased | `https://personsincontext.org/model#deceased` | DatatypeProperty | — → — | «Indication if a person is still alive or not at time of the source of the observation. Only used when deathDate is unknown. A person without a deathDate and without the property deceased set to true, will be considered alive. This…» | sí |
| eventDate | `https://personsincontext.org/model#eventDate` | DatatypeProperty | — → — | «The date of an event. A date value in ISO 8601 format should be used. Incomplete dates are allowed, but only when truncated from small to large. For example: "1970-08-15", "1970-08" and "1970" are all allowed, but "1970-00-15" or …» | sí |
| eventPlace | `https://personsincontext.org/model#eventPlace` | DatatypeProperty | — → — | «Preferably, use a link to an existing thesaurus like geonames or wikidata. If desired, both the literal place, as mentioned on the Source can be used together with the reconciled version.» | sí |
| eventType | `https://personsincontext.org/model#eventType` | CodedProperty,ObjectProperty | — → — | «Use a term from the PiCo Event Types thesaurus: https://terms.personsincontext.org/eventtypes» | sí |
| hasAge | `https://personsincontext.org/model#hasAge` | DatatypeProperty | — → — | «Only used for Person observations, in case the birth date is not known, but the age is. In combination with de date of the Source, a birth date range can be derived, which can be used in the process of creating a Person reconstruc…» | sí |
| hasAncestor | `https://personsincontext.org/model#hasAncestor` | ObjectProperty,TransitiveProperty (subPropertyOf relatedTo; inversa hasDescendant) | Person → Person | «hasAncestor is not meant to be used as a property for PersonObservations or PersonReconstructions. It is a superclass of sdo:Parent. Since hasAncestor is a owl:TransitiveProperty, this will make the parent of your parent into your…» | sí |
| hasChild-in-law | `https://personsincontext.org/model#hasChild-in-law` | ObjectProperty (subPropertyOf relatedTo; inversa hasParent-in-law) | Person → Person | «For Person observations, the hasChild-in-law property should always refer to another Person observation on the same Source.» | sí |
| hasCousin | `https://personsincontext.org/model#hasCousin` | ObjectProperty,SymmetricProperty (subPropertyOf relatedTo) | Person → Person | «For Person observations, the hasCousin property should always refer to another Person observation on the same Source.» | sí |
| hasCousin-in-law | `https://personsincontext.org/model#hasCousin-in-law` | ObjectProperty,SymmetricProperty (subPropertyOf relatedTo) | Person → Person | «For Person observations, the hasCousin-in-law property should always refer to another Person observation on the same Source.» | sí |
| hasDescendant | `https://personsincontext.org/model#hasDescendant` | ObjectProperty,TransitiveProperty (subPropertyOf relatedTo; inversa hasAncestor) | Person → Person | «hasDescendant is not meant to be used as a property for PersonObservations or PersonReconstructions. It is a superclass of sdo:Children. Since hasAncestor is a owl:TransitiveProperty, this will make the children of your children i…» | sí |
| hasFosterChild | `https://personsincontext.org/model#hasFosterChild` | ObjectProperty (subPropertyOf relatedTo; inversa hasFosterParent) | Person → Person | «For Person observations, the hasFosterChild property should always refer to another Person observation on the same Source.» | sí |
| hasFosterParent | `https://personsincontext.org/model#hasFosterParent` | ObjectProperty (subPropertyOf relatedTo; inversa hasFosterChild) | Person → Person | «For Person observations, the hasFosterParen property should always refer to another Person observation on the same Source.» | sí |
| hasGodchild | `https://personsincontext.org/model#hasGodchild` | ObjectProperty (subPropertyOf relatedTo; inversa hasGodparent) | Person → Person | «For Person observations, the hasGodchild property should always refer to another Person observation on the same Source.» | sí |
| hasGodparent | `https://personsincontext.org/model#hasGodparent` | ObjectProperty (subPropertyOf relatedTo; inversa hasGodchild) | Person → Person | «For Person observations, the hasGodparent property should always refer to another Person observation on the same Source.» | sí |
| hasGrandchild | `https://personsincontext.org/model#hasGrandchild` | ObjectProperty (subPropertyOf relatedTo; inversa hasGrandparent) | Person → Person | «For Person observations, the hasGrandchild property should always refer to another Person observation on the same Source.» | sí |
| hasGrandchild-in-law | `https://personsincontext.org/model#hasGrandchild-in-law` | ObjectProperty (subPropertyOf relatedTo; inversa hasGrandparent-in-law) | Person → Person | «For Person observations, the hasGrandchild-in-law property should always refer to another Person observation on the same Source.» | sí |
| hasGrandparent | `https://personsincontext.org/model#hasGrandparent` | ObjectProperty (subPropertyOf relatedTo; inversa hasGrandchild) | Person → Person | «For Person observations, the hasGrandparent property should always refer to another Person observation on the same Source.» | sí |
| hasGrandparent-in-law | `https://personsincontext.org/model#hasGrandparent-in-law` | ObjectProperty (subPropertyOf relatedTo; inversa hasGrandchild-in-law) | Person → Person | «For Person observations, the hasGrandparent-in-law property should always refer to another Person observation on the same Source.» | sí |
| hasGreat-grandchild | `https://personsincontext.org/model#hasGreat-grandchild` | ObjectProperty (subPropertyOf relatedTo; inversa hasGreat-grandparent) | Person → Person | «For Person observations, the hasGreat-grandchild property should always refer to another Person observation on the same Source.» | sí |
| hasGreat-grandparent | `https://personsincontext.org/model#hasGreat-grandparent` | ObjectProperty (subPropertyOf relatedTo; inversa hasGreat-grandchild) | Person → Person | «For Person observations, the hasGreat-grandparent property should always refer to another Person observation on the same Source.» | sí |
| hasHalf-sibling | `https://personsincontext.org/model#hasHalf-sibling` | ObjectProperty,SymmetricProperty (subPropertyOf relatedTo) | Person → Person | «For Person observations, the hasHalf-sibling property should always refer to another Person observation on the same Source.» | sí |
| hasLegitimizedChild | `https://personsincontext.org/model#hasLegitimizedChild` | ObjectProperty (subPropertyOf relatedTo; inversa isLegitimitezedChildOf) | Person → Person | «For Person observations, the hasLegitimizedChild property should always refer to another Person observation on the same Source.» | sí |
| hasLifeEvent | `https://personsincontext.org/model#hasLifeEvent` | ObjectProperty | Person → LifeEvent | «Relates a person to a life event that occurred in his biography.» | sí |
| hasNephew/Niece | `https://personsincontext.org/model#hasNephew_Niece` | ObjectProperty (subPropertyOf relatedTo; inversa hasUncle_Aunt) | Person → Person | «For Person observations, the hasNephew_Niece property should always refer to another Person observation on the same Source.» | sí |
| hasNephew-in-law/Niece-in-law | `https://personsincontext.org/model#hasNephew_Niece-in-law` | ObjectProperty (subPropertyOf relatedTo; inversa hasUncle_Aunt-in-law) | Person → Person | «For Person observations, the hasNephew_Niece-in-law property should always refer to another Person observation on the same Source.» | sí |
| hasParent-in-law | `https://personsincontext.org/model#hasParent-in-law` | ObjectProperty (subPropertyOf relatedTo; inversa hasChild-in-law) | Person → Person | «For Person observations, the hasNephew_Niece property should always refer to another Person observation on the same Source.» | sí |
| hasPreviousPartner | `https://personsincontext.org/model#hasPreviousPartner` | ObjectProperty,SymmetricProperty (subPropertyOf relatedTo) | Person → Person | «For Person observations, the hasPreviousPartner property should always refer to another Person observation on the same Source.» | sí |
| hasReligion | `https://personsincontext.org/model#hasReligion` | DatatypeProperty | — → — | «Religion as mentioned on the Source. If desired, a SKOS thesaurus can be used to annotate religion.» | sí |
| hasRole | `https://personsincontext.org/model#hasRole` | CodedProperty,ObjectProperty | — → — | «Use a term from the PiCo Roles thesaurus: https://terms.personsincontext.org/roles» | sí |
| hasSibling-in-law | `https://personsincontext.org/model#hasSibling-in-law` | ObjectProperty,SymmetricProperty (subPropertyOf relatedTo) | Person → Person | «For Person observations, the hasSibling-in-law property should always refer to another Person observation on the same Source.» | sí |
| hasStepchild | `https://personsincontext.org/model#hasStepchild` | ObjectProperty (subPropertyOf relatedTo; inversa hasStepparent) | Person → Person | «For Person observations, the hasStepchild property should always refer to another Person observation on the same Source.» | sí |
| hasStepchild-in-law | `https://personsincontext.org/model#hasStepchild-in-law` | ObjectProperty (subPropertyOf relatedTo; inversa hasStepparent-in-law) | Person → Person | «For Person observations, the hasStepchild-in-law property should always refer to another Person observation on the same Source.» | sí |
| hasStepparent | `https://personsincontext.org/model#hasStepparent` | ObjectProperty (subPropertyOf relatedTo; inversa hasStepchild) | Person → Person | «For Person observations, the hasStepparent property should always refer to another Person observation on the same Source.» | sí |
| hasStepparent-in-law | `https://personsincontext.org/model#hasStepparent-in-law` | ObjectProperty (subPropertyOf relatedTo; inversa hasStepchild-in-law) | Person → Person | «For Person observations, the hasStepparent-in-law property should always refer to another Person observation on the same Source.» | sí |
| hasStepsibling | `https://personsincontext.org/model#hasStepsibling` | ObjectProperty,SymmetricProperty (subPropertyOf relatedTo) | Person → Person | «For Person observations, the hasStepsibling property should always refer to another Person observation on the same Source.» | sí |
| hasUncle/Aunt | `https://personsincontext.org/model#hasUncle_Aunt` | ObjectProperty (subPropertyOf relatedTo; inversa hasNephew_Niece) | Person → Person | «For Person observations, the hasUncle_Aunt property should always refer to another Person observation on the same Source.» | sí |
| hasUncle/Aunt-in-law | `https://personsincontext.org/model#hasUncle_Aunt-in-law` | ObjectProperty (subPropertyOf relatedTo; inversa hasNephew_Niece-in-law) | Person → Person | «For Person observations, the hasUncle_Aunt-in-law property should always refer to another Person observation on the same Source.» | sí |
| isLegitimitezedChildOf | `https://personsincontext.org/model#isLegitimitezedChildOf` | ObjectProperty (subPropertyOf relatedTo; inversa hasLegitimizedChild) | Person → Person | «For Person observations, the isLegitimitezedChildOf property should always refer to another Person observation on the same Source.» | sí |
| isWidow/WidowerOf | `https://personsincontext.org/model#isWidOf` | ObjectProperty (subPropertyOf relatedTo) | Person → Person | «For Person observations, the isWidOf property should always refer to another Person observation on the same Source.» | sí |
| Source | `https://schema.org/ArchiveComponent` | Class (⊑ CreativeWork) | — → — | «Person observations can appear on many types of historical documents. The PiCo model does not aim to describe these sources, as excellent data models, such as Records in Contexts and Dublin Core, already exist within the heritage …» | sí |
| Scan | `https://schema.org/ImageObject` | Class (⊑ CreativeWork) | — → — | «A link to the location of the scan at the HoldingArchive. A link to scan as it can be displayed online and a link to a thumbnail (for search results) should be provided. Preferably a link to a IIIF manifest.» | sí |
| additionalName | `https://schema.org/additionalName` | ObjectProperty | — → — | «The name of a Person, annotated according to the Person Name Vocabulary.» | sí |
| additionalType | `https://schema.org/additionalType` | CodedProperty,ObjectProperty | — → — | «Use a term from the PiCo thesaurus for Source types: https://terms.personsincontext.org/sourcetypes» | sí |
| address | `https://schema.org/address` | DatatypeProperty | — → — | «Address of a Person as mentioned on the Source.» | sí |
| associatedMedia | `https://schema.org/associatedMedia` | ObjectProperty | — → — | «todo» | sí |
| birthDate | `https://schema.org/birthDate` | DatatypeProperty | — → — | «The birth date of a person. A date value in ISO 8601 format should be used. Incomplete dates are allowed, but only when truncated from small to large. For example: "1970-08-15", "1970-08" and "1970" are all allowed, but "1970-00-1…» | sí |
| birthPlace | `https://schema.org/birthPlace` | DatatypeProperty | — → — | «Preferably, use a link to an existing thesaurus like geonames or wikidata. If desired, both the literal place, as mentioned on the Source can be used together with the reconciled version.» | sí |
| children | `https://schema.org/children` | ObjectProperty (subPropertyOf hasDescendant,relatedTo; inversa parent) | — → — | «For Person observations, the child should always refer to another Person observation on the same Source.» | sí |
| contentLocation | `https://schema.org/contentLocation` | DatatypeProperty | — → — | «The location depicted or described in the content. For example, the geographic coverage of an archival record. Or the location in a photograph or painting.» | sí |
| dateCreated | `https://schema.org/dateCreated` | DatatypeProperty | — → — | «The date on which the Source was created.» | sí |
| deathDate | `https://schema.org/deathDate` | DatatypeProperty | — → — | «The death date of a person. A date value in ISO 8601 format should be used. Incomplete dates are allowed, but only when truncated from small to large. For example: "1970-08-15", "1970-08" and "1970" are all allowed, but "1970-00-1…» | sí |
| deathPlace | `https://schema.org/deathPlace` | DatatypeProperty | — → — | «Preferably, use a link to an existing thesaurus like geonames or wikidata. If desired, both the literal place, as mentioned on the Source can be used together with the reconciled version.» | sí |
| embedUrl | `https://schema.org/embedUrl` | ObjectProperty | — → — | «A URL pointing to a viewer for a specific scan.» | sí |
| familyName | `https://schema.org/familyName` | DatatypeProperty | — → — | «The use of sdo:givenName and sdo:familyName is the most straightforward method for describing person names. Use pnv:PersonName for more extensive name annotations.» | sí |
| gender | `https://schema.org/gender` | DatatypeProperty | — → — | «Use one of: sdo:Male or sdo:Female.» | sí |
| givenName (schema) | `https://schema.org/givenName` | DatatypeProperty | — → — | «The use of sdo:givenName and sdo:familyName is the preferred method for describing person names. Use pnv:PersonName for more extensive name annotations.» | sí |
| hasOccupation | `https://schema.org/hasOccupation` | DatatypeProperty | — → — | «Occupation as mentioned on the Source» | sí |
| holdingArchive | `https://schema.org/holdingArchive` | ObjectProperty | — → — | «Organization that holds, keeps or maintains the ArchiveComponent.» | sí |
| name | `https://schema.org/name` | DatatypeProperty | — → — | «For Persons: Use full name if the name can't be split into given name and family name. Otherwise use sdo:givenNamen and sdo:fullName or the more extensive pnv:PersonName.» | sí |
| parent | `https://schema.org/parent` | ObjectProperty (subPropertyOf hasAncestor,relatedTo; inversa children) | — → — | «For Person observations, the parent property should always refer to another Person observation on the same Source.» | sí |
| position | `https://schema.org/position` | DatatypeProperty | — → — | «The position defines the order in which scans are presented on the web. This feature is required when a Source has multiple scans.» | sí |
| sibling | `https://schema.org/sibling` | ObjectProperty,SymmetricProperty (subPropertyOf relatedTo) | — → — | «For Person observations, the sibling should always refer to another Person observation on the same Source.» | sí |
| spouse | `https://schema.org/spouse` | ObjectProperty,SymmetricProperty (subPropertyOf relatedTo) | — → — | «For Person observations, the spouse should always refer to another Person observation on the same Source.» | sí |
| thumbnail | `https://schema.org/thumbnail` | ObjectProperty | — → — | «Thumbnail image of the Scan.» | sí |
| url | `https://schema.org/url` | ObjectProperty | — → — | «For Sources: a link to the Source at the holding archive. Preferably a permalink.» | sí |
| Persons in Context eventType thesaurus | `https://terms.personsincontext.org/eventtypes/` | ConceptScheme | — → — | «» | sí |
| Persons in Context role thesaurus | `https://terms.personsincontext.org/roles/` | ConceptScheme | — → — | «» | sí |
| Persons in Context sourceType thesaurus | `https://terms.personsincontext.org/sourcetypes/` | ConceptScheme | — → — | «» | sí |
| PersonName | `https://w3id.org/pnv#PersonName` | Class | — → — | «In the Person Name Vocabulary, a name is considered to be a a resource type in its own right. A PersonName can consist of many different parts. The most common ones are mentioned here. See the full specification of the Person Name…» | sí |
| baseSurname | `https://w3id.org/pnv#baseSurname` | DatatypeProperty | — → — | «A Base surname is a family name without any prefixes, if those prefixes need to be ignored in sorting. If the family name is e.g. 'de Vries' and it needs to be sorted under 'V', the Base surname is 'Vries'. Base surname is equival…» | sí |
| givenName (pnv) | `https://w3id.org/pnv#givenName` | DatatypeProperty | — → — | «The given name of a pnv:PersonName. Designates the name(s) given to someone at birth or any other name-giving event.» | sí |
| initials | `https://w3id.org/pnv#initials` | DatatypeProperty | — → — | «An initial is the first letter of a person's given name (or sometimes a combination of letters). The Initials property can be used to separately record the initial(s) of a person's given name(s). Each initial should be followed by…» | sí |
| literalName | `https://w3id.org/pnv#literalName` | DatatypeProperty | — → — | «Literal name designates a full personal name. This property may only be left blank if a person's name was unknown or if a person was unnamed (e.g. a child that died shortly after being born), in which cases the property pnv:nameSp…» | sí |
| patronym | `https://w3id.org/pnv#patronym` | DatatypeProperty | — → — | «A Patronym is a name element based on the given name of one's father or grandfather. This is also the preferred property for a matronym (i.e. a name element based on the given name of one's mother or grandmother).» | sí |
| surnamePrefix | `https://w3id.org/pnv#surnamePrefix` | DatatypeProperty | — → — | «A2A:PersonNamePrefixLastName» | sí |

### roar

Tripletas parseadas: 246. Ontologías declaradas: `https://w3id.org/roar` ['0.1'] ['https://w3id.org/roar/0.1']

#### Todos los términos declarados (roar)

| término | IRI | tipo | dominio → rango | extracto nota de alcance | verificado |
|---|---|---|---|---|---|
| http://dbpedia.org/ontology/role | `http://dbpedia.org/ontology/role` | DatatypeProperty | — → — | «» | sí |
| http://purl.org/dc/elements/1.1/title | `http://purl.org/dc/elements/1.1/title` | AnnotationProperty | — → — | «» | sí |
| http://purl.org/pav/createdBy | `http://purl.org/pav/createdBy` | AnnotationProperty | — → — | «» | sí |
| bio:Birth | `http://purl.org/vocab/bio/0.1/Birth` | Class (⊑ Event) | — → — | «» | sí |
| bio:Death | `http://purl.org/vocab/bio/0.1/Death` | Class (⊑ Event) | — → — | «» | sí |
| bio:Event | `http://purl.org/vocab/bio/0.1/Event` | Class (⊑ Event) | — → — | «A life event from the bio vocabulary. It is recommended to include timestamp properties from the sem vocabulary. If the exact date is known, sem:hasTimeStamp can be used. If dates are uncertain, use the other properties: - sem:has…» | sí |
| bio:birth | `http://purl.org/vocab/bio/0.1/birth` | ObjectProperty (subPropertyOf 0.1) | Person → Birth | «Even if there is no specific birth date mentioned in the source, it is recommended to provide a Birth event and estimate the dates based on other (life) events around the person. A concrete example would be the mentioning of a Bap…» | sí |
| bio:death | `http://purl.org/vocab/bio/0.1/death` | ObjectProperty (subPropertyOf 0.1) | Person → Death | «Even if there is no specific death date mentioned in the source, it is recommended to provide a Death event and estimate the dates based on other (life) events around the person. A concrete example would be the mentioning of a Bur…» | sí |
| bio:event | `http://purl.org/vocab/bio/event/0.1` | ObjectProperty | Person → Event | «Use to connect life events to a Person. Use more specific events, such as `bio:birth` and `bio:death` for respectively Birth and Death events.» | sí |
| http://purl.org/vocab/vann/preferredNamespacePrefix | `http://purl.org/vocab/vann/preferredNamespacePrefix` | AnnotationProperty | — → — | «» | sí |
| http://purl.org/vocab/vann/preferredNamespaceUri | `http://purl.org/vocab/vann/preferredNamespaceUri` | AnnotationProperty | — → — | «» | sí |
| schema:CreativeWork | `http://schema.org/CreativeWork` | Class | — → — | «» | sí |
| schema:Person | `http://schema.org/Person` | Class | — → — | «» | sí |
| schema:Place | `http://schema.org/Place` | Class | — → — | «» | sí |
| sem:Event | `http://semanticweb.cs.vu.nl/2009/11/sem/Event` | Class | — → — | «» | sí |
| prov:Activity | `http://www.w3.org/ns/prov#Activity` | Class | — → — | «The Activity in which the Derivation and thereby the Reconstruction was made. Use `rdfs:comment` to specify what the Activity did.» | sí |
| prov:Agent | `http://www.w3.org/ns/prov#Agent` | Class | — → — | «The Person or Organisation that was involved in the Derivation. In other words, who made the Reconstruction?» | sí |
| prov:Association | `http://www.w3.org/ns/prov#Association` | Class | — → — | «» | sí |
| prov:Derivation | `http://www.w3.org/ns/prov#Derivation` | Class | — → — | «» | sí |
| prov:Entity | `http://www.w3.org/ns/prov#Entity` | Class | — → — | «» | sí |
| prov:Plan | `http://www.w3.org/ns/prov#Plan` | Class | — → — | «Use a `rdfs:comment` to describe the goal the Agent had in the Activity.» | sí |
| prov:agent | `http://www.w3.org/ns/prov#agent` | ObjectProperty | Association → Agent | «» | sí |
| prov:entity | `http://www.w3.org/ns/prov#entity` | ObjectProperty | Derivation → Entity | «» | sí |
| prov:hadActivity | `http://www.w3.org/ns/prov#hadActivity` | ObjectProperty | Derivation → Activity | «» | sí |
| prov:hadPlan | `http://www.w3.org/ns/prov#hadPlan` | ObjectProperty | Agent → Plan | «» | sí |
| prov:qualifiedAssociation | `http://www.w3.org/ns/prov#qualifiedAssociation` | ObjectProperty | Activity → Association | «» | sí |
| prov:qualifiedDerivation | `http://www.w3.org/ns/prov#qualifiedDerivation` | ObjectProperty | Reconstruction → Derivation | «» | sí |
| prov:wasAssociatedWith | `http://www.w3.org/ns/prov#wasAssociatedWith` | ObjectProperty | Activity → Agent | «» | sí |
| prov:wasDerivedFrom | `http://www.w3.org/ns/prov#wasDerivedFrom` | ObjectProperty | Reconstruction → Entity | «A Reconstruction is derived from one or several Observation(s) or Reconstruction(s). It is good practise to also specify the activity in which the derivation was made. This can be done by modelling a `prov:qualifiedDerivation` on …» | sí |
| http://xmlns.com/foaf/0.1/depiction | `http://xmlns.com/foaf/0.1/depiction` | AnnotationProperty | — → — | «» | sí |
| http://xmlns.com/foaf/0.1/logo | `http://xmlns.com/foaf/0.1/logo` | AnnotationProperty | — → — | «» | sí |
| pnv:PersonName | `https://w3id.org/pnv#PersonName` | Class | — → — | «» | sí |
| pnv:hasName | `https://w3id.org/pnv#hasName` | ObjectProperty | Person → PersonName | «» | sí |
| Reconstructions and Observations in Archival Resources | `https://w3id.org/roar` | Ontology | — → — | «Ontology to describe person, location etc. observations in archival resources. One or multiple observations can be bundled into a reconstruction that combines complementary (or sometimes conflicting) information from the observati…» | sí |
| Document | `https://w3id.org/roar#Document` | Class | — → — | «The source (e.g. document, act, legislation, text, picture, painting, recording, obelisk) in which some entity (e.g. Person or Location) can be observed. If the source that you are describing is not digitised or is not available a…» | sí |
| Entity | `https://w3id.org/roar#Entity` | Class | — → — | «Basic class to hold classes that can be combined with an Observation or Reconstruction class. Pre-modelled are Person and Location, but you are free to specify more types, such as Event or Organisation.» | sí |
| Location | `https://w3id.org/roar#Location` | Class (⊑ Entity) | — → — | «A Location can be any type of place where another entity can be located.» | sí |
| LocationObservation | `https://w3id.org/roar#LocationObservation` | Class (⊑ Observation) | — → — | «A LocationObservation is a location that can be observed in a `roar:Document`.» | sí |
| LocationReconstruction | `https://w3id.org/roar#LocationReconstruction` | Class (⊑ Location,Reconstruction) | — → — | «A LocationReconstruction is the result of modelling one or multiple LocationObservation(s) into a single resource.» | sí |
| Observation | `https://w3id.org/roar#Observation` | Class (⊑ Entity) | — → — | «Something of a type 'Observation' is something that is mentioned or described in a 'Document' (described by roar:inDocument). Two common subclasses are PersonObservation and LocationObservation, but one can also think about EventO…» | sí |
| Person | `https://w3id.org/roar#Person` | Class (⊑ Entity) | — → — | «A Person is a human being that is mentioned in a Document. This can be a direct mention (e.g. 'Aaltie Jans') or indirect (e.g. 'husband of Aaltie Jans'), in which a name might not be known.» | sí |
| PersonObservation | `https://w3id.org/roar#PersonObservation` | Class (⊑ Observation) | — → — | «A PersonObservation is a person that can be observed in a `roar:Document`.» | sí |
| PersonReconstruction | `https://w3id.org/roar#PersonReconstruction` | Class (⊑ Person,Reconstruction) | — → — | «A PersonReconstruction is the result of modelling one or multiple PersonObservation(s) into a single resource.» | sí |
| Reconstruction | `https://w3id.org/roar#Reconstruction` | Class (⊑ Entity) | — → — | «A 'Reconstruction' is a specific modelling of one or several entities of type 'Observation' into a single resource. The prov:wasDerivedFrom property is used to indicate on which Observations a Reconstruction was based. It is also …» | sí |
| documentedIn | `https://w3id.org/roar#documentedIn` | ObjectProperty | Entity → Document | «Refers to the Document (source, act, legislation etc.) in which the Observation is made. It is recommended to point to a resource (URI) provided by some institute/archive that hold key information on this source. You are, however,…» | sí |
| hasLocation | `https://w3id.org/roar#hasLocation` | ObjectProperty | Entity → Location | «Use to indicate that an Entity has a relation to a Location. Use a structured value to indicate a specific role of this Entity (e.g. Person) to the Location or to specify a temporal validity in which this Entity-Location relation …» | sí |
| hasPerson | `https://w3id.org/roar#hasPerson` | ObjectProperty | Entity → Person | «Use to indicate that an Entity has a relation to a Person. Use a structured value to indicate a specific role of this Entity (e.g. Location) to the Person or to specify a temporal validity in which this Entity-Person relation is v…» | sí |
| hasRelation | `https://w3id.org/roar#hasRelation` | ObjectProperty | Entity → Entity | «Relation to another person or organisation, defined by a structured value to indicate the kind of relation. *Example*: ```ttl :person1 a roar:Person ; schema:gender schema:Female ; roar:hasRelation [ rdf:value :person2 ; roar:rela…» | sí |
| locationInDocument | `https://w3id.org/roar#locationInDocument` | DatatypeProperty (subPropertyOf topDataProperty) | Observation → — | «The locationInDocument property can hold any location reference relative to the Document an Observation is in. This can be used to indicate a location in the source, even when the source has not yet been digitized (then a roar:onS…» | sí |
| onScan | `https://w3id.org/roar#onScan` | DatatypeProperty (subPropertyOf topDataProperty) | Observation → — | «This property can be used to indicate the location of the EntityObservation in the source, for instance if the roar:Document is too general (e.g. it refers to multiple pages). This should refer to a URI or filename and assumes the…» | sí |
| relationType | `https://w3id.org/roar#relationType` | DatatypeProperty (subPropertyOf topDataProperty) | — → — | «Used to specify the kind of relation (e.g. "patron") in a person to person relation as specified by `roar:hasRelation`.» | sí |
| role | `https://w3id.org/roar#role` | DatatypeProperty (subPropertyOf topDataProperty) | — → — | «Can be used to indicate the role of an entity in a `roar:hasLocation` or `roar:hasPerson` relation. In case of a Person to Location relation (through `roar:hasLocation`), the `roar:role` can for instance be 'inhabitant' or 'visito…» | sí |

## Notas por estándar

### RiC-O: tipos de conjunto documental y de forma documental
- `RiC_RecordSetTypes_vocabulary.rdf` define **solo cuatro** conceptos (`skos:Concept` y `rico:RecordSetType`):
  `…/recordSetTypes#Fonds` (es: «fondo»), `#Series`, `#File` y `#Collection`. **No existen Subfonds ni Subseries.**
  Para representarlos hay que usar `Fonds`/`Series` anidados mediante `rico:includesOrIncluded`, o bien un tipo propio.
- `RiC_DocumentaryFormTypes_vocabulary.rdf` define **solo tres** conceptos: `#AuthorityRecord`, `#FindingAid` y `#IIIFManifest`.
  No hay tipos judiciales (autos, petición, testimonio, sentencia…), así que hace falta un vocabulario SKOS propio
  enlazado con `rico:hasDocumentaryFormType`.
- Folio/página: RiC-O no tiene «folio». Las opciones que existen son estas: `rico:RecordPart` para la unidad intelectual;
  `rico:Instantiation` + `rico:hasOrHadInstantiation` para el soporte físico o la digitalización; extensión con `rico:hasExtent` → `rico:RecordResourceExtent`
  o el literal `rico:recordResourceExtent`; orden con `rico:directlyPrecedesInSequence`/`rico:directlyFollowsInSequence`
  (o el literal `rico:rankInSequence`, que el propio comentario desaconseja frente a las relaciones de secuencia).
  `rico:hasOrHadLocation` es Thing→Place (geográfico) y `rico:hasOrHadPhysicalLocation` es Place→PhysicalLocation. Ninguna de las dos sirve para «f. 12v».

### CIDOC CRM 7.1.3: P14.1 y las clases de propiedad (PC)
- El archivo separado `CIDOC_CRM_v7.1.3_PC.rdfs` declara `PC0_Typed_CRM_Property`, `PC14_carried_out_by` (rdfs:Class),
  `P01_has_domain`, `P02_has_range` y **`P14.1_in_the_role_of`**.
- En RDF, P14.1 se llama exactamente `http://www.cidoc-crm.org/cidoc-crm/P14.1_in_the_role_of` (con punto),
  con dominio `PC14_carried_out_by` y rango `E55_Type`. No es una propiedad de `E7`: se usa sobre el nodo PC14.
  Patrón literal del propio archivo: `:x a crm:PC14_carried_out_by ; crm:P01_has_domain <actividad> ; crm:P02_has_range <actor> ; crm:P14.1_in_the_role_of <tipo>`,
  con la regla `PC14(x) ∧ P01(x,a) ∧ P02(x,b) ∧ P14.1(x,c) ⇒ P14(a,b)`.
- `P82a_begin_of_the_begin` y `P82b_end_of_the_end` tienen rango `rdfs:Literal`, sin datatype fijado. Tampoco tienen nota en el RDFS.

### CRMinf 1.2.1
- La clase `E13_Attribute_Assignment` del CRM se declara `rdfs:subClassOf crminf:I1_Argumentation`, de modo que E13 puede llevar `J2_concluded_that`.
- Para la evidencia existe `J7_is_based_on_evidence_from` (I7_Belief_Adoption → E73_Information_Object) y su inversa `J7i_is_evidence_for`.
- Clases y propiedades nuevas que conviene conocer: `I12_Adopted_Belief`, `I13_Intended_Meaning_Belief`, `I16_Meaning_Comprehension`,
  `I17_One-Proposition_Set` con `J30_has_domain`/`J31_has_range`/`J32_has_property_type` y **`J33_assigned_propositions`
  (E13_Attribute_Assignment → I17_One-Proposition_Set)**. Esta última es la alternativa formal del propio CRMinf para reificar un E13.
  Además: `J13_adopted_interpretation` (I7→I12), `J14_adopted_interpretation_of` (I12→E73), `J24_held_at_least_for` (I11→E52),
  `J25_is_encoded_by` (I4→Literal), `J28_contains_entity_reference` (I4→E1) y `J29_contains_property_type` (I4→E55).

### PiCo 1.1.0: cómo vincula observación, reconstrucción, fuente y derivación
- `picom:PersonObservation` → **`prov:hadPrimarySource`** (obligatorio) → fuente `sdo:ArchiveComponent` (con `sdo:additionalType`
  del tesauro de tipos de fuente, `sdo:holdingArchive`, `sdo:associatedMedia` → `sdo:ImageObject` (scan)).
  El rol de la persona en la fuente va en `picom:hasRole` → concepto del tesauro de roles.
- `picom:PersonReconstruction` → **`prov:wasDerivedFrom`** (obligatorio, una o más PersonObservation) y `prov:wasGeneratedBy` → `prov:Activity`
  (`prov:wasAssociatedWith` → `prov:Agent`, `prov:startedAtTime`/`endedAtTime`). `prov:wasRevisionOf` se usa para las versiones.
  Según la especificación, `hadPrimarySource` y `hasRole` **no** se usan en la reconstrucción: se obtienen a través de las observaciones.
- Las dos clases son subclases de `picom:Person` (⊑ `prov:Entity`, `sdo:Person`). Los eventos van en `picom:LifeEvent` con `picom:hasLifeEvent`, `picom:eventType`, `picom:eventDate` y `picom:eventPlace`.
- Hay una anomalía en el archivo: `prov:wasAssociatedWith` aparece tipada como `owl:DatatypeProperty` en pico.ttl (en PROV-O es ObjectProperty).

#### Tesauro de roles de PiCo (32 conceptos descargados; etiquetas en/nl literales)

| en | nl | IRI | definición (extracto) | mapeos |
|---|---|---|---|---|
|  | schenker | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/65` |  |  |
| slave | slaaf | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/67` |  |  |
|  | gemanumitteerde | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/68` | Een gemanumiteerde is een voormalige slaaf die officieel werd vrijgelaten en wiens gegeven |  |
| applicant | aanvrager | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/70` | De persoon die formeel het verzoek heeft ingediend tot het verkrijgen van een document of  |  |
| beneficiary | begunstigde | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/71` | Degene die door een contract, wet of testament wordt aangewezen om een bepaald recht of vo |  |
| deceased person | overledene | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/479` | De persoon die is overleden, zoals vastgelegd in een overlijdensakte of begraafregister. |  |
| traveler | reiziger | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/482` | Een persoon die zich verplaatst van de ene plaats naar de andere, vaak vermeld in passagie |  |
| employee | werknemer / personeelslid | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/484` | Een persoon die in dienst is bij een werkgever, vermeld in arbeidsovereenkomsten of person |  |
| notary | notaris | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/485` | Een juridisch functionaris die verantwoordelijk is voor het opstellen en vastleggen van of |  |
| seller | verkoper | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/486` | De persoon die een eigendom of goed verkoopt aan een koper. |  |
| buyer | koper | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/487` | De persoon die een goed of eigendom koopt van een verkoper, vaak vermeld in koopakten of n |  |
| informant | aangever | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/489` | De persoon die aangifte doet van een belangrijke gebeurtenis, zoals een geboorte of overli |  |
| resident | bewoner | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/490` | De persoon die officieel geregistreerd staat als inwoner van een huis of gebouw, vaak verm |  |
| church member | lidmaat | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/492` | Een persoon die lid is van een kerkelijke gemeente, vaak vermeld in kerkelijke lidmatenreg |  |
| civil servant | ambtenaar | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/493` | Een functionaris die officieel belast is met de uitvoering van overheidstaken, zoals het r |  |
| military personnel | militair | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/494` | Een persoon die in dienst is van het leger of een andere krijgsmacht, bijvoorbeeld vermeld |  |
| debtor | schuldenaar | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/496` | A person obliged to repay a debt to a creditor. |  |
| creditor | schuldeiser | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/497` | A person entitled to the payment of a debt by a debtor. |  |
| tenant | huurder | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/503` | De persoon die een woning, gebouw of land huurt van een eigenaar of verhuurder. |  |
| defendant | gedaagde | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/507` | De persoon die in een rechtszaak is aangeklaagd en zich moet verweren tegen een vordering  |  |
| landlord | verhuurder | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/508` | De persoon die een eigendom verhuurt aan een huurder. |  |
| owner | eigenaar | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/509` | De persoon die officieel als bezitter van een onroerend goed of ander bezit staat geregist |  |
| heir | erfgenaam | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/510` | Een persoon die recht heeft op (een deel van) de nalatenschap van een overledene, vaak ver |  |
| testator | testateur | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/513` | Een persoon die een testament heeft opgemaakt om zijn of haar laatste wil vast te leggen. |  |
| eligable voter | kiesgerechtigde | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/514` | Een persoon die het recht heeft om te stemmen bij verkiezingen, zoals geregistreerd in een |  |
| detainee | arrestant | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/515` | Een persoon die gearresteerd is en mogelijk vastzit in verband met een strafbaar feit. |  |
| convicted | veroordeelde | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/516` | Een persoon die door een rechtbank schuldig is bevonden aan een misdrijf en een straf heef |  |
| taxpayer | patentplichtige / aangeslagene | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/517` | Een persoon die belasting moet betalen voor het uitoefenen van een bepaald beroep of het b |  |
| constituted party | geconstitueerde | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/518` | De persoon die door een ander wordt benoemd of gemachtigd om een bepaalde taak of functie  |  |
| witness | getuige | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/573` | Een persoon die aanwezig is bij een officiële handeling en die daar getuigenis van aflegt, |  |
| bride/groom | bruid/bruidegom | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/574` | De persoon die in een huwelijk treedt met een andere persoon, zoals vermeld in huwelijksak |  |
| newborn | kind | `https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/575` | Een persoon die als kind van de ouders wordt geregistreerd, bijvoorbeeld in een geboorteak |  |

Para un expediente judicial sirven `defendant` (507), `witness` (573), `detainee` (515), `convicted` (516), `notary` (485), `applicant` (70),
`creditor`/`debtor` y `civil servant` (493). **No hay** demandante/querellante, juez, escribano (distinto de notario), procurador, defensor ni intérprete.
Esos roles habría que añadirlos en un tesauro propio con `skos:closeMatch`.

### ROAR 0.1: patrón observación/reconstrucción
- `roar:Observation` ⊑ `roar:Entity`, con `roar:documentedIn` → `roar:Document` y la ubicación dentro de la fuente en
  `roar:locationInDocument` (literal, p. ej. folio) y `roar:onScan`.
- `roar:Reconstruction` ⊑ `roar:Entity`; `roar:PersonReconstruction` ⊑ `roar:Person`, `roar:Reconstruction`; ídem para `Location*`.
- La derivación se expresa con `prov:wasDerivedFrom` (dominio Reconstruction en ROAR). En la forma cualificada: `prov:qualifiedDerivation` → `prov:Derivation`
  (`prov:entity`, `prov:hadActivity` → `prov:Activity` → `prov:qualifiedAssociation` → `prov:Association` (`prov:agent`; `prov:hadPlan`, que ROAR declara —de forma atípica— con dominio `prov:Agent`)).
- Los roles van en el literal `roar:role` (sobre una relación estructurada `roar:hasPerson`/`roar:hasLocation`), y `roar:relationType` se usa con `roar:hasRelation`.
- Autores según la documentación: Menno den Engelse y Leon van Wissen. PiCo declara expresamente que su estructura básica se inspira en ROAR.

## Qué es el «patrón STAR»

Hay varias cosas con ese nombre en el ámbito del CIDOC CRM:

1. **STAR = STructured Assertion Record**. Es la que encaja. Autora: **Tara L. Andrews** (Universität Wien), dentro del proyecto ERC
   **RELEVEN** («Re-evaluating the eleventh century», acuerdo de subvención n.º 101002357). Documento: «The STructured Assertion Record (STAR) Model for
   Event-based Representation of Historical Information», GrapHNR 2023 (Graph Technologies in the Humanities, Maguncia).
   PDF: https://graphentechnologien.hypotheses.org/files/2023/05/GrapHNR-2023-32-Andrews-STAR.pdf (guardado en `vendor/star/`).
   Texto literal: «extend the linked open data model from a triple (subject, predicate, object) to a five-pointed structure (thus "STAR model")
   which includes subject, predicate, object, source, and authority… Its backbone is the CIDOC-CRM…, using the 'E13 Attribute Assignment' entity as
   the core of each assertion. The subject and object are then classes of E1 CRM Entity and the predicate is reified as an E55 Type; we then
   model the assertion as having been P17 motivated by the source… and P14 carried out by some actor, who functions as the authority.»
   Las fuentes textuales se describen con LRMoo. **No existe un OWL/TTL publicado del modelo**: en la organización GitHub `erc-releven`
   no hay repositorio de ontología STAR, solo código (PBWgraph, releven-backend…).
   El artículo **no nombra P140/P141/P177**. Que el sujeto vaya en `P140_assigned_attribute_to`, el objeto en `P141_assigned` y el predicado
   en `P177_assigned_property_of_type` → E55 es la lectura estándar de E13 en CRM 7.1.3, pero es una inferencia y no una cita del artículo.
   Hay otra publicación sobre STAR en el portal de la Universität Wien: «Byzantine Sigillography, Linked Open Data, and the Structured Assertion Record».
2. **STAR = «Semantic Technologies for Archaeological Resources»** (Univ. of Glamorgan / South Wales: Tudhope, Binding, May, con English Heritage, c. 2007-2010).
   Es un proyecto de mapeo de datos arqueológicos a CRM-EH. **No** es un patrón de afirmaciones sobre E13.
3. «RDF-star» (W3C) **no** es STAR: es un mecanismo de citación de tripletas que se ha discutido como alternativa a E13.

## HGIS de las Indias

- **Formato de identificadores** (observado en la API de World Historical Gazetteer, WHG):
  - **Lugares** (dataset WHG `lugares13k_rel`, ds 14): `src_id` numérico de 7–8 cifras. Los de Perú están en la serie 6000xxx (p. ej. 6000357).
    La URL estable de consulta es la de WHG: `https://whgazetteer.org/places/<place_id>/detail` (`place_id` es el ID interno de WHG, distinto de `src_id`).
  - **Territorios** (dataset `territorios892`, ds 15): código de 8 caracteres, p. ej. `JUPECUTI`. Por los ejemplos parece seguir el esquema
    nivel (JU=jurisdicción, PR=provincia/intendencia, OB=obispado, AU=audiencia, SU=superior gobierno) + PE + CU + TI, rellenado con «0». Esta descomposición es una **inferencia**.
    Las URI originales `http://www.hgis-indias.net/dokuwiki/doku.php?id=<código>` **devuelven 404** (2026-11-12).
  - Licencia en WHG: CC BY-NC-SA 4.0, titular Werner Stangl. Periodo del proyecto: 1701–1808.

| Entrada buscada | Encontrada como | src_id HGIS | place_id WHG / URL | Tipo | Coordenadas (lon, lat) | Periodo / jerarquía |
|---|---|---|---|---|---|---|
| Tinta (pueblo) | «Tinta» | 6000357 | 177060, https://whgazetteer.org/places/177060/detail | Pueblo | -71.406341, -14.144732 | 1701–1808; en Tinta (Jurisdicción) JUPECUTI 1701–1808, en Cuzco (Provincia) PRPECU00 1784–1808, en Lima (Provincia) 1701–1783 |
| Sicuani | «Sicuani» | 6000365 | 177068, https://whgazetteer.org/places/177068/detail | Pueblo | -71.226594, -14.273289 | 1701–1808; JUPECUTI |
| Checacupe | «Checacupe» | 6000360 | 177063, https://whgazetteer.org/places/177063/detail | Pueblo | -71.453426, -14.025768 | 1701–1808; JUPECUTI |
| San Pedro de Cacha | «San Pedro» (sin «de Cacha») | 6000358 | 177061, https://whgazetteer.org/places/177061/detail | Pueblo | -71.343317, -14.18654 | 1701–1808; JUPECUTI. La identificación con San Pedro de Cacha es **probable, no confirmada**: se apoya en el nombre, la jurisdicción de Tinta y las coordenadas (entre Tinta y Sicuani) |
| Cusco (ciudad) | «El Cuzco» | 6000002 | 176704, https://whgazetteer.org/places/176704/detail | Ciudad | -71.97888, -13.516718 | geometría «desde 1534» (minmax 1534); en Cuzco (Jurisdicción) JUPECUCU 1701–1808 y Cuzco (Provincia) PRPECU00 1784–1808 |
| Urubamba (pueblo) | «Urubamba» | 6000378 | 177081, https://whgazetteer.org/places/177081/detail | Pueblo | -72.115767, -13.305732 | 1701–1808; Urubamba (Jurisdicción) JUPECUUR 1741–1808; Marquesado de Oropesa (Señorío) SEPEMO00 1701–1740 |
| Partido de Tinta | «Tinta» (territorio) | JUPECUTI | 139803, https://whgazetteer.org/places/139803/detail | Corregimiento 1701–1783; Subdelegación 1784–1808 | polígonos (GeometryCollection, uno por periodo) | 1701–1808 |
| Partido de Urubamba | «Urubamba» (territorio) | JUPECUUR | 139804 | Corregimiento 1741–1783; Subdelegación 1784–1808 | polígonos | 1741–1808 |
| Intendencia del Cusco | «Cuzco» (territorio) | PRPECU00 | 140068, https://whgazetteer.org/places/140068/detail | «Gobernacion-Intendencia» | polígonos | 1784–1808 |
| (contexto) Obispado del Cuzco | «Cuzco» | OBPECU00 | 139986 | Obispado | polígono | 1701–1808 |
| (contexto) Audiencia del Cuzco | — | AUCU0000 | no consultado aparte (solo aparece como relación) | Audiencia | — | 1788–1808 |

No se halló como entrada propia de HGIS: «San Pedro de Cacha» con ese nombre exacto (ver arriba).
El partido de Quispicanchis y otros no se buscaron. La búsqueda «Tinta» sin filtro de dataset devuelve primero registros de Getty TGN: hay que filtrar con `dataset=lugares13k_rel` / `territorios892`.
Existen homónimos que **no** son los nuestros: «Tinta» 6000993 (Cajatambo), «Tintay» 6000543 (Lucanas), «Tintay» 6001507 (Aymaraes) y «Tierra de Tinta» 4000266 (Venezuela).
**Los datos HGIS no están en `vendor/`**: WHG responde «403 Bot access denied» a curl. Se consultaron con WebFetch sobre `https://whgazetteer.org/api/db/?name=<n>&dataset=<ds>` y `…/api/place/<id>`.

## Términos que NO existen o cambiaron de nombre

| Pedido | Situación en el archivo descargado | Usar en su lugar |
|---|---|---|
| `rico:hasInstantiation` | no existe | `rico:hasOrHadInstantiation` (RecordResource → Instantiation); inversa `rico:isOrWasInstantiationOf` |
| `rico:followsInSequence` | no existe | `rico:directlyFollowsInSequence` (directa) o `rico:followsInSequenceTransitive` (transitiva); superpropiedad `rico:followsOrFollowed` |
| `rico:precedesInSequence` | no existe | `rico:directlyPrecedesInSequence` o `rico:precedesInSequenceTransitive`; superpropiedad `rico:precedesOrPreceded` |
| `rico:hasOrHadCreator` (comprobado por si acaso) | no existe | `rico:hasCreator` (sí existe) |
| `rico:hasOrHadLocation` para folio | existe, pero es Thing → **Place** | ver «Folio/página» arriba |
| RecordSetType Subfonds / Subseries | no existen en el vocabulario | Fonds/Series anidados, o un concepto propio |
| `crminf:I6_Belief_Value` | no está declarada como clase en el RDF. Solo se nombra en notas de alcance | el rango de `J5_holds_to_be` es `rdfs:Literal` (p. ej. "TRUE"/"FALSE"/valores propios) |
| `crminf:J6_adopted` | no existe en 1.2.1 (solo se menciona en una fórmula de J5: «J5(x,y) ⇒ J6(y)», al parecer una errata) | para la adopción: `I7_Belief_Adoption` + `J2_concluded_that` (heredada de I1) o `J13_adopted_interpretation` → `I12_Adopted_Belief`; para la evidencia: `J7_is_based_on_evidence_from` |
| `crminf:J7` | existe con el nombre `J7_is_based_on_evidence_from` (dominio **I7**, no I5/I1) | — |
| `crm:E1` | el nombre completo es `E1_CRM_Entity` | — |
| `P14.1_in_the_role_of` | no está en el archivo principal del CRM, sino en el `_PC.rdfs` | usar sobre `PC14_carried_out_by` |

Todos los demás términos pedidos de CIDOC CRM, PROV-O, SKOS y `oa:` existen con el nombre exacto indicado.

## Dudas

1. **CIDOC CRM 7.1.3 frente a borradores.** cidoc-crm.org publica borradores hasta el 7.4 (agosto 2026), pero el único con RDFS y estado «Official» posterior a 7.1.2 es 7.1.3. Si el proyecto prefiere 7.3.x hay que confirmar que no han cambiado IRIs (por ejemplo, P177).
2. **`J2_concluded_that` aparece como `rdfs:subPropertyOf` de `P175`, `P175i` y `P185`** en el RDF de CRMinf 1.2.1. Es inusual, y un razonador inferiría relaciones temporales. Conviene no activar inferencia RDFS sobre CRMinf sin revisarlo.
3. **Licencias no declaradas en el archivo:** tesauro de roles de PiCo, PDF de STAR y el .ttl de ROAR (la licencia CC BY-SA 4.0 consta solo en la documentación HTML).
4. **PiCo `main` es posterior a la etiqueta v.1.1.0** (último commit 2026-09-14). Se fijó la release. Si se quiere lo más reciente hay que revisar el diff.
5. **Tesauro de roles de PiCo:** se recorrieron `hasTopConcept` y `narrower` y salieron 32 conceptos, pero no hay un volcado oficial único. Algún concepto sin enlace jerárquico podría faltar.
6. **RiC-O `rico:identifier` y otras propiedades de datos** («Provided for usability reasons. May be deprecated…»). En 1.1 no llevan `owl:deprecated`, pero la nota anuncia que podrían retirarse. Es más estable usar `rico:Identifier` + `rico:hasOrHadIdentifier`.
7. **SKOS core.rdf** es el archivo del namespace (2009, última modificación del servidor 2011). No tiene versionInfo; la versión se toma de la recomendación.
8. La identificación **San Pedro (6000358) = San Pedro de Cacha** y la descomposición de los códigos territoriales de HGIS son inferencias. Conviene confirmarlas con el WebGIS de hgis-indias.net o con su equipo.
9. Durante el trabajo, un proceso externo restauró `scripts/fetch_vendor.sh` y borró `vendor/fuentes.sha256` (a las 10:49:47). Se volvieron a aplicar los cambios y se regeneraron las sumas. Conviene revisar que nada más se haya revertido.
