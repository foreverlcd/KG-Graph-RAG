# H2 · Alternativas para las capas 1 y 2, lugares, tiempo y vocabularios

> **Fecha de la búsqueda:** 2026-11-12.
>
> **Alcance:** qué otras ontologías, formatos y proyectos podrían sustituir o complementar lo que el modelo usa hoy en
> la capa 1 (documento: RiC-O 1.1 + CRM), la capa 2 (menciones: PiCo/ROAR + Web Annotation), los lugares (HGIS/WHG),
> el tiempo (E52 + fecha escrita) y el tesauro SKOS. No repite lo que ya está en `docs/F_precedentes.md` ni en
> `docs/anexos/F_informe_precedentes_y_literatura.md` (FPO, PiCo, ROAR, Enslaved, Wikibase, CRMinf, STAR, Candela
> et al. 2023); solo los cita cuando hace falta.
>
> **Marcas de verificación:**
> * **VERIFICADO**: lo comprobé en la fuente primaria. Abrí la página o el archivo de la especificación, resolví el
>   DOI en Crossref o consulté el servicio (SPARQL de Getty, API de Dataverse o de Wikidata).
> * **VERIFICADO (indirecto)**: solo vi el fragmento de la fuente primaria que devolvió el buscador, no la página entera.
> * **NO VERIFICADO**: no pude comprobarlo.

---

## 0. Recomendación en una página

**No hay que cambiar ninguna de las piezas principales.** Nada de lo que hay a finales de 2026 cubre mejor las capas 1
y 2 que la combinación actual.

* **RiC-O 1.1 sigue siendo la última versión.** No existe una 1.2.
* **CRM 7.1.3 sigue siendo la versión ISO.** Las 7.3.x siguen en borrador.
* **Ninguna ontología jurídica sirve** para un expediente colonial.

Sí conviene hacer **siete ajustes pequeños**. Ninguno añade términos propios a OHAC.

1. **Matizar el defecto D5.** RiC-O 1.1 sí permite expresar la *extensión* de un expediente o pieza en folios
   (`rico:CarrierExtent` / `rico:InstantiationExtent` + `rico:hasUnitOfMeasurement` + `rico:quantity`). Lo que no
   tiene es un folio individual direccionable. El defecto real es más estrecho de lo que dice `C_modelo.md` §7.
2. **Enlazar los conceptos documentales del tesauro con el AAT de Getty** mediante `skos:closeMatch`:
   * `doc:folio` → `aat:300189604` *folios (leaves)*;
   * `doc:recto` → `aat:300078817` *rectos*;
   * `doc:verso` → `aat:300010292` *versos*;
   * la sección judicial → `aat:300027883` *criminal court records*.
3. **Añadir `oa:prefix` y `oa:suffix` al `TextQuoteSelector`.** Hoy solo lleva `oa:exact` (`src/laad/mapeo.py`, ~l. 138).
   Es lo que recomienda el modelo de Web Annotation para volver a anclar la cita si la transcripción cambia, y es
   barato.
4. **Lugares: multiplicar los identificadores sin fusionar.**
   * Mantener HGIS como `E42` (sus URI no resuelven).
   * Añadir el DOI del conjunto de datos en Dataverse como fuente del identificador.
   * Añadir TGN y Wikidata como `rdfs:seeAlso`, por ejemplo Tinta = `tgn:9227290` = `wd:Q2435935`.
   * **No copiar geometrías ni atributos de HGIS.** Su licencia es CC BY-NC-SA 4.0 y «contagiaría» al grafo.
5. **Tesauro: alineaciones externas con `skos:closeMatch` o `skos:relatedMatch`, nunca `exactMatch` por etiqueta.**
   Wikidata da un caso real del riesgo: la etiqueta quechua «ayllu» está puesta en los ítems *family* (Q8436) y
   *community* (Q177634). El ítem correcto es Q793079.
   * Etiquetas quechuas con `@quz` (Cusco Quechua) o `@qu`, **solo cuando la forma esté atestiguada en quechua**.
   * Grafías coloniales como `skos:hiddenLabel` o `skos:altLabel`.
6. **Tiempo: no adoptar OWL-Time.** Su última versión sigue siendo el borrador CRD de 2022, y en 1806 ya regía el
   calendario gregoriano. Se mantiene E52 + P82a/P82b en la capa 4.
   * Como forma de intercambio puede añadirse el literal EDTF (ISO 8601-2:2019), que RiC-O usa en sus ejemplos de
     `rico:normalizedDateValue`.
7. **En el artículo, posicionarse frente a CourtDocs (Vafaie et al. 2023) y frente a EHRI-KG.** Son los precedentes
   más cercanos en combinación (RiC-O + CRM + PROV). CourtDocs usa PROV-O para el *proceso judicial*, que es
   justamente lo que nuestro principio 6 prohíbe. La diferencia es citable.

**Para considerar, sin adoptar todavía:**

* **CRMtex 2.0 para el acto de transcribir** (`TX6 Transliteration ⊑ E65 Creation`), si llegan las imágenes y la
  paleografía se vuelve objeto de estudio.
* **`crm:E22_Human-Made_Object` + `P46` para el original y sus folios**, como tipado paralelo que facilitaría el
  consumo por herramientas de Linked Art.
* **IIIF Presentation 3.0** (no la 4.0, que sigue en borrador) para anclar regiones de imagen cuando las haya.

**Hueco confirmado:**

* No encontré ningún grafo de conocimiento ni publicación LOD del Archivo Regional del Cusco.
* No encontré ningún grafo de expedientes judiciales coloniales andinos con afirmaciones atribuidas.
* No encontré ningún modelado formal de cacicazgos.

Esto refuerza la originalidad, pero es una afirmación negativa: **NO VERIFICADO de forma exhaustiva** (§7).

---

## 1. Capa 1: documento

### 1.1 Tabla de alternativas

| Alternativa | Estado a 2026-11 | Madurez | Encaje con un expediente colonial | ¿Adoptar o cambiar? |
|---|---|---|---|---|
| **RiC-O 1.1** (ICA-EGAD) | Última versión publicada: 1.1, de mayo de 2025. El repositorio no menciona ninguna 1.2 ni 2.0 y declara que la 1.1 es «fully compliant with RiC-CM 1.0». **VERIFICADO** (README de github.com/ICA-EGAD/RiC-O) | Alta: estándar ICA, implementado en los Archives nationales de France y en EHRI | Alto para la jerarquía y las instanciaciones. Le faltan legajo, sección y folio individual | **Mantener.** Matizar D5 (§1.2) |
| **RiC-CM 1.0** | Publicado por ICA el 30-11-2023 junto con RiC-FAD 1.0. RiC-O 1.0 siguió en diciembre de 2023. **VERIFICADO (indirecto)** (ica.org). ICA anuncia que en 2025 salió RiC-AG, la cuarta parte; otra fuente habla de una 0.1 en octubre de 2025: **NO VERIFICADO** cuál es correcta | Alta | Es el modelo conceptual del que deriva RiC-O. No aporta clases nuevas | Citar como base conceptual |
| **EAD3 / EAD4** (SAA TS-EAS) | EAD3 1.1.2 vigente. Existe un documento *Editorial Changes in EAD 4.0* y la revisión está aprobada por el SAA Council, pero **no encontré la publicación de EAD4**. **NO VERIFICADO** su estado final | Alta (EAD3) | Es XML de instrumentos de descripción. No es RDF y no modela afirmaciones | **No.** Solo como formato de importación desde catálogos (RiC-O Converter convierte EAD 2002 y EAC-CPF a RiC-O; Francart, Clavaud y Charbonnier 2021, CEUR 3019:30–36, **VERIFICADO**) |
| **EAC-CPF 2.0** | Publicado en agosto de 2022. Hay una versión menor 2.0.1. **VERIFICADO (indirecto)** (SAA y Staatsbibliothek Berlin) | Alta | Son registros de autoridad: personas ya fusionadas | **No.** Contradice la capa 2 (sin fusión). Solo serviría para exportar reconstrucciones de la capa 4 |
| **NEDA-MC** (CNEDA, España) | Modelo conceptual de 2012 (entidades) y 2017 (atributos). **VERIFICADO (indirecto)** (ica.org, iberarchivos.org). No encontré ninguna ontología RDF publicada | Media | Es el contexto archivístico hispano (PARES). No tiene RDF | No. Mencionarlo como norma nacional española paralela a RiC |
| **CIDOC CRM 7.1.3 / 7.3.x** | ISO 21127:2023 corresponde a la 7.1.3. Las 7.3 (2024), 7.3.1 (mayo de 2025) y 7.3.2 (marzo de 2026) figuran como *Draft*. **VERIFICADO (indirecto)** (cidoc-crm.org/versions-of-the-cidoc-crm) | Alta | Ya se usa | **Mantener la 7.1.3** (versión ISO). Revisar la 7.3.x cuando sea oficial |
| **LRMoo 1.0** (IFLA + CIDOC) | Aprobado en abril de 2024 y alineado con CRM 7.1.3. El repositorio de IFLA lista una versión 2 de 2026-03-18 y marca la de 2024 como *superseded*. **VERIFICADO** (repository.ifla.org). Autores de la versión 1: T. Aalberg, P. Riva, M. Žumer | Alta | Obra, expresión, manifestación e ítem están pensados para publicaciones. Un expediente manuscrito único colapsa en F5 Item / F2 Expression sin ganar nada | **No.** Serviría solo si se quisiera modelar la transcripción como una «expresión» de la «obra» |
| **CRMtex 2.0** | Aprobada por CRM-SIG en junio de 2023. Mantenida por F. Murano, A. Felicetti y P. Fafalios. Hay RDF y OWL publicados. **VERIFICADO** (PDF y página del modelo) | Media (comunidad epigráfica y papirológica) | `TX6 Transliteration ⊑ E65 Creation` cubre explícitamente la «transcription… re-encoding a text using the same writing system», es decir, la transcripción paleográfica. `TXP11 transcribed` → `TX12 Grapheme Sequence`. `TX14 Reading ⊑ I1 Argumentation` (la lectura como argumentación). `TX7 Written Text Segment ⊑ TX1` (segmento físico) | **No por ahora.** Candidata para tipar el acto de transcribir (quién y cuándo) si llegan las imágenes. Hoy ese dato está en PROV (capa P) y basta |
| **CRMdig** | La 4.0 está etiquetada como «unstable» (2022-12-08). El issue 708 del SIG (agosto de 2025) anuncia una 5.0. **VERIFICADO (indirecto)** | Media-baja | Trata de la procedencia de la digitalización (escaneo) | No. Solo cuando haya imágenes; PROV cubre lo mismo hoy |
| **DoCO / FaBiO** (SPAR) | DoCO: Constantin et al. 2016. FaBiO: Peroni y Shotton 2012. **VERIFICADO** (Crossref) | Alta en publicaciones académicas | Componentes retóricos de artículos modernos (sección, párrafo). No conocen pieza, foja ni actuación | No |
| **Linked Art 1.0** | Publicado el 19-02-2025. Usa un subconjunto de CRM 7.1.3. La jerarquía archivística se modela como `Set` + `member_of`, sin límite de profundidad, con los niveles tipados por AAT («Archival Grouping» `aat:300404022`, «SubGrouping» `aat:300404023`). La propia especificación dice que no intenta ser completa en archivos. No cubre folios. **VERIFICADO** (linked.art/model y /model/archives) | Alta en museos, media en archivos | Compatible en espíritu (CRM). No modela afirmaciones ni menciones | No como núcleo. **Opcional:** tipar el original como `crm:E22` y los folios como partes (`crm:P46`) para que lo consuman herramientas Linked Art |
| **ArCo** (MiC, Italia) | Red de 7 ontologías y 169 M de tripletas. Carriero et al. 2019. **VERIFICADO** (Crossref) | Alta, pero ligada al catálogo italiano ICCD | Bienes culturales, no expedientes. Usa `owl:sameAs` hacia otros LOD (VERIFICADO (indirecto)), que es lo que evitamos | No. Citar como ejemplo de KG nacional |
| **EHRI-KG** | Grafo LOD del portal EHRI (≈370 000 descripciones). García-González y Bryant, ISWC 2023. La página del proyecto dice que alinea con «RiC-CM 1.0.2» y que la ontología EHRI extiende RiC-O con schema.org (**VERIFICADO (indirecto)**; versión 0.1.0, NO VERIFICADO). El visor está en un dominio «test» | Media | Es descripción archivística a gran escala, no contenido aseverado | No. **Citar** como el despliegue más grande de RiC-O |
| **IIIF Presentation** | La 3.0 es la estable. La 4.0 figura como «4.0.0-draft» (alfa en 2025, sobre todo para 3D). **VERIFICADO** (iiif.io/api/presentation/4.0) | Alta (3.0) | Ancla regiones de imagen y transcripciones diplomáticas como anotaciones | Cuando haya imágenes: manifiesto 3.0 por expediente, un canvas por folio y recto/verso, y `oa:FragmentSelector` (xywh) junto al selector de texto |

### 1.2 Matiz al defecto D5 (RiC-O sin folio)

Busqué en `vendor/ric-o/RiC-O_1-1.rdf` (VERIFICADO con rdflib). Estos términos existen:

* `rico:CarrierExtent`: «Number of physical units and/or physical dimensions of the carrier of an Instantiation».
* `rico:InstantiationExtent`.
* `rico:quantity` y `rico:hasUnitOfMeasurement`.
* `rico:physicalCharacteristicsNote`.
* `rico:Proxy`: «represents a Record Resource as it exists in a specific other Record Resource».
* `rico:RecordPart`.

En cambio, **no** hay ninguna clase ni propiedad para una hoja o folio como unidad física direccionable, ni para recto
y verso. Por tanto:

* «El expediente tiene 23 fojas» **sí** se puede expresar en RiC-O puro: `rico:CarrierExtent` con `rico:quantity 23` y
  unidad «foja».
* «Este tramo está en el folio 4 vuelto» **no** se puede expresar sin un concepto propio. Es lo que hace hoy
  `rico:Instantiation` + `dct:type doc:folio`.

**Redacción propuesta para D5:** «RiC-O 1.1 permite expresar la extensión en folios, pero no el folio individual
direccionable, ni recto y verso, ni los niveles *sección* y *legajo* de la tradición hispana. Su vocabulario
DocumentaryFormTypes no tiene tipos judiciales.»

Para anclar el concepto propio, `doc:folio skos:closeMatch aat:300189604` (VERIFICADO en el SPARQL de Getty).

**`rico:Proxy`:** encaja si una misma pieza aparece en dos expedientes (por ejemplo, un testimonio copiado). No es el
caso hoy, pero conviene anotarlo para la fase de serie completa (L3).

### 1.3 Por qué no basta CRM solo (ni Linked Art) para la capa 1

* CRM y Linked Art modelan la jerarquía archivística como conjuntos genéricos (`E78 Curated Holding`, `Set`).
* Pierden los niveles de descripción con nombre (fondo, serie, expediente) y la relación entre documento e
  instanciación, que son el vocabulario de intercambio de la ICA.
* Vafaie et al. (2021, CEUR 2981) eligen RiC-O justamente porque modela los niveles jerárquicos como individuos con
  nombre, generalizables entre archivos (VERIFICADO en el texto de Vafaie 2024, CEUR 3884).

Nuestra elección (RiC-O para el papel, CRM para los actos) coincide con la de CourtDocs y con la del grafo
Wiedergutmachung (§4.2).

---

## 2. Capa 2: menciones y anclaje textual

### 2.1 Anclar las citas: Web Annotation sigue siendo la opción correcta

* El **modelo de Web Annotation** (W3C Recommendation, 23-02-2017) es el único estándar que permite apuntar a un pasaje
  de un recurso con varios selectores alternativos. Ya está en `vendor/oa/oa.ttl`.
* Hoy usamos `TextQuoteSelector` (solo `oa:exact`) y `TextPositionSelector`. La especificación prevé `oa:prefix` y
  `oa:suffix` para desambiguar citas repetidas («dies», «dicho Guancachoque») y para volver a anclar si cambia la
  transcripción.
* **Recomendación:** generar prefijo y sufijo (p. ej. 32 caracteres) en `_ancla` de `mapeo.py`. Es conforme a la
  especificación y no añade términos.
* `oa:hasState` / `oa:TimeState` permitirían fijar la versión del recurso. **No hace falta:** la versión ya está en la
  IRI del tramo (`transcripcion/<sha12>/…`) y en `dct:identifier "sha256:…"`.

### 2.2 TEI y RDF

* **No existe un estándar único TEI → RDF.** Las vías vivas son tres:
  * **Standoff con Web Annotation sobre TEI.** El modelo de texto de KNAW HuC usa `XPathSelector` sobre elementos TEI,
    serializado en JSON-LD. **VERIFICADO (indirecto)** (knaw-huc.github.io/ns/text_intro.html).
  * **Conversión con XTriples (LINCS).** Pasa TEI hecho con plantillas LEAF-Writer a CRM. Cubre personografías,
    placeografías, cartas y poemas. **VERIFICADO (indirecto)** (portal.lincsproject.ca/docs/tools/xtriples).
  * **Enfoques híbridos TEI/RDF** con referencias por `@xml:id`. Ogawa et al., TEI 2023, **VERIFICADO (indirecto)**.
* **Para LAAD:** la transcripción es texto plano con hash, no TEI. Si algún día se codifica en TEI (abreviaturas,
  `<choice>`, `<sic>`/`<corr>`, saltos de folio `<pb n="4v"/>`), conviene añadir un tercer selector `oa:XPathSelector`
  o `oa:RangeSelector`, sin quitar los de texto.
* **Ventaja de TEI para L1:** `<pb/>` resolvería de forma nativa el problema del folio de cada tramo.

### 2.3 Herramientas de anotación con gazetteer

* Recogito y Recogito Studio (Pelagios) producen anotaciones Web Annotation enlazadas a gazetteers.
* El proyecto LatAm (Pelagios, 2018–2019) cargó HGIS de las Indias como gazetteer opcional en Recogito y casó 2539
  entradas de Alcedo (1786) con HGIS. **VERIFICADO (indirecto)** (informes de Pelagios en Medium; la página dio 403).
* Es un candidato natural para la anotación manual del estándar de oro: exporta Web Annotation, que es nuestro
  formato de ancla. **NO VERIFICADO:** que Recogito Studio exporte hoy `TextPositionSelector` con el mismo cómputo de
  posiciones (puntos de código Unicode) que `mapeo.py`.

### 2.4 Alternativas para la mención misma

* PiCo, ROAR y FPO ya están evaluados en F.
* La única novedad es **BZKO** (Yargan, Waitelonis, Vafaie y Sack; arXiv 2608.06918, agosto de 2026, aceptado en el
  Ontology Showcase de FOIS 2026 / JOWO). Es un fichero de la posguerra alemana, con dos capas (semántica BFO frente a
  extensiones de interoperabilidad), que **reutiliza RiC-O, PROV-O y PiCo**. **VERIFICADO** (resumen en arXiv).
* Confirma que PiCo empieza a reutilizarse fuera de los Países Bajos. No aporta términos que nos falten.

---

## 3. Ontologías jurídicas y procesales

| Alternativa | Estado | Qué modela | Encaje con un pleito criminal de 1806 | Decisión |
|---|---|---|---|---|
| **LKIF-Core** (Hoekstra, Breuker, Di Bello y Boer) | OWL DL de 2007–2009 (proyecto Estrella), 15 módulos. Sin mantenimiento activo conocido. **VERIFICADO** (Crossref, DOI del capítulo IOS Press 2009) | Normas, acciones, roles y procesos jurídicos abstractos | Bajo. Categorías del derecho positivo moderno, sin documento ni testimonio | No. Citar como ontología jurídica nuclear |
| **LegalRuleML Core 1.0** | OASIS Standard del 30-08-2021. XML y Relax NG. **VERIFICADO (indirecto)** (oasis-open.org) | Reglas derrotables, deónticas y jurisdicción | Nulo: no hay normas que formalizar | No |
| **Akoma Ntoso 1.0** (OASIS LegalDocML) | OASIS Standard, partes 1 y 2, 29-08-2018. **VERIFICADO (indirecto)** | Marcado XML de leyes, debates y sentencias (estructura de la sentencia moderna) | Bajo. Un expediente es un *dossier* de piezas heterogéneas, no una sentencia estructurada | No |
| **ELI / ECLI** | Identificadores europeos de legislación y jurisprudencia | URI de normas y resoluciones contemporáneas | Nulo para 1806 | No |
| **OPJK** (Casanovas et al. 2007) | Ontología del conocimiento judicial profesional (jueces españoles, Iuriservice). **VERIFICADO** (Crossref) | Preguntas frecuentes de jueces noveles | Nulo en el dominio, pero es metodológicamente afín: se construyó desde ~800 preguntas de competencia sacadas de la práctica | Citar en el apartado de método (preguntas de competencia) |
| **UFO-L / OntoUML + BPMN** (Costa, Guizzardi y Almeida 2022, recurso brasileño) | Artículo académico. **VERIFICADO (indirecto)** | Roles y fases de un recurso de apelación actual | Bajo | No |
| **CourtDocs Ontology** (Vafaie, Bruns, Pilz, Waitelonis y Sack; K-CAP 2023, pp. 175–179) | Trabajo en curso. **No encontré el repositorio de la ontología** (NO VERIFICADO que sea pública). **VERIFICADO** (Crossref) | Procedimientos judiciales históricos (Wiedergutmachung): jerarquía con RiC-O, **proceso judicial con PROV-O**, biografías con CRM (Vafaie 2024, CEUR 3884, VERIFICADO en el texto) | **El precedente más cercano en combinación de estándares** | **Citar y contrastar.** Usar PROV-O para el proceso mezcla «quién lo dijo en 1946» con la procedencia del dato, justo lo que nuestro principio 6 separa. Además no separa la mención de la persona ni la afirmación de la reconstrucción |

**Conclusión.** Ninguna ontología jurídica modela el expediente de Antiguo Régimen: actuaciones, fuerza institucional,
juramento, fórmulas de escribano, firma a ruego. Todas presuponen derecho codificado contemporáneo o sentencias
estructuradas.

La solución actual (tipos de actuación, roles y fuerza como SKOS con `P2_has_type` y `P14.1_in_the_role_of`) es la
recomendada por CRM para la especialización local, y además es reversible: si mañana apareciera una ontología procesal
histórica, bastaría con alinear conceptos (`skos:closeMatch`).

Hay términos del AAT de Getty con los que conviene alinear los tipos de pieza (todos **VERIFICADOS** en el SPARQL de
Getty el 2026-11-12):

* *depositions* `aat:300027862`;
* *petitions* `aat:300027219`;
* *affidavits* `aat:300027594`;
* *criminal court records* `aat:300027883`;
* *judicial records* `aat:300027850`;
* *legal documents* `aat:300027590`.

---

## 4. Lugares

### 4.1 Tabla de alternativas

| Fuente | URI / LOD | Licencia | Cobertura para Tinta (1806) | Uso recomendado |
|---|---|---|---|---|
| **HGIS de las Indias** (W. Stangl, Graz; continuado como «Indias HGIS 2.0» en Yale) | **Sin LOD propio.** El sitio (hgis-indias.net → /index.php/en/) no menciona URI, RDF ni API; solo descargas en Dataverse «for non-commercial use». **VERIFICADO** | Dataverse: **CC BY-NC-SA 4.0** para *Places gazetteer* (doi:10.7910/DVN/FUSJD3, v3.0, 2023-10-25) y *Territorial gazetteer* (doi:10.7910/DVN/YPEU5E, v4.0, 2023-10-26). **VERIFICADO** (API de Dataverse) | La mejor fuente para la geografía administrativa de 1701–1808 (partidos, doctrinas, pueblos) | **Mantener** como `crm:P48` → `E42` con el identificador literal y una referencia al DOI del conjunto de datos. **No incorporar geometrías ni atributos**: el NC-SA obligaría a licenciar así el grafo |
| **World Historical Gazetteer** | Recoge HGIS en Linked Places Format. El conjunto «HGIS de las Indias territorios» (WHG 15) tiene 892 registros, subidos el 12-04-2019 y modificados el 03-09-2025; licencia del aportante CC BY-NC-SA 4.0, añadidos de WHG CC BY 4.0. **VERIFICADO** (whgazetteer.org/datasets/15). Las páginas de lugar individuales devolvieron 403 a peticiones automáticas: **NO VERIFICADO** por máquina que `places/177060` siga resolviendo | Ídem | Tinta = WHG 177060 (según F) | **Mantener** `rdfs:seeAlso` hacia WHG |
| **Linked Places Format** | v1.3 (24-06-2024): `fclasses` obligatorio. WHG acepta v1.2.2 en la carga y su API devuelve v1.1. **VERIFICADO** (README de LinkedPasts) | — | Cada topónimo lleva cita y `when`, que es nuestra filosofía | **Formato de exportación** si se aportan lugares nuevos (ayllus Tinta y Uchu) a WHG. No sustituye a ROAR en el grafo |
| **Getty TGN** | LOD estable (`vocab.getty.edu/tgn/…`). **ODC-By 1.0**. **VERIFICADO (indirecto)** | Permisiva | Tinta = `tgn:9227290` («Cuzco, Peru»). **VERIFICADO** (SPARQL de Getty) | **Añadir** como `rdfs:seeAlso` (o un segundo E42) en la reconstrucción de lugar |
| **Wikidata** | LOD, CC0 | Permisiva | Tinta = `Q2435935` («village in Cusco, Peru»). Intendencia del Cusco = `Q5918759`. **VERIFICADO** (API de Wikidata) | **Añadir** como `rdfs:seeAlso`. Sirve de puente a VIAF y GeoNames |
| **GeoNames** | LOD, CC BY 4.0. **VERIFICADO** (geonames.org/about) | Permisiva | Geografía actual, sin tiempo | Solo de forma indirecta, vía Wikidata o WHG |
| **Pleiades** | Mundo antiguo mediterráneo. **VERIFICADO (indirecto)** | CC BY | Ninguna | No |

**Patrón recomendado** para una `roar:LocationReconstruction ∧ crm:E53_Place`, sin `owl:sameAs` y sin geometría
importada:

* `crm:P48_has_preferred_identifier` → E42 «HGIS 6000357», con `dct:source <https://doi.org/10.7910/DVN/FUSJD3>`.
* `crm:P1_is_identified_by` → otros E42 («TGN 9227290», «Wikidata Q2435935»).
* `rdfs:seeAlso` hacia WHG, TGN y Wikidata.

`dct:source` ya está en el vocabulario usado (DCTerms). Si se quiere el tipo del identificador, va con `P2_has_type`
→ un concepto `doc:` nuevo (dato, no T-Box).

**Lugares sin entrada (ayllus):** se quedan como reconstrucciones propias. Si se publican, LPF v1.3 es el formato para
aportarlos a WHG, con la cita del expediente en `citations`.

### 4.2 PeriodO

PeriodO (Rabinowitz et al. 2016) es el gazetteer de periodos. Sería útil solo si se nombran periodos («tiempo de la
rebelión», «antes de la revisita»). Hoy no hace falta.

---

## 5. Tiempo

| Opción | Estado | Encaje | Decisión |
|---|---|---|---|
| **CRM E52 + P82a/P82b + E41 (fecha escrita)** | Ya se usa | Separa la fecha escrita (capa 1) de la normalizada (capa 4) y admite intervalos difusos | **Mantener** |
| **EDTF** (ISO 8601-2:2019, perfil de la LoC) | Estable, con niveles 0–2 (incierto `?`, aproximado `~`, intervalos abiertos). **VERIFICADO (indirecto)** (loc.gov). **Sin tipo de dato RDF registrado**: el borrador EDTF-OWL de PeriodO deja la correspondencia con CRM como trabajo futuro (VERIFICADO (indirecto)). RiC-O 1.1 usa ejemplos EDTF en `rico:normalizedDateValue`: su *changeNote* de 2024-09-02 dice «Fixed a typo in two of the EDTF examples» (**VERIFICADO** en `vendor/ric-o`) | Bueno como forma compacta de intercambio («1806-08~», «1806-09/1806-10») | **Opcional en la capa 4**: además de P82a/P82b, un literal EDTF como `P3_has_note` o `E41` con `P2_has_type` EDTF. **Nunca en la capa 1** (FechaEscritaForma) |
| **OWL-Time** (W3C/OGC) | Recomendación de 2017. La versión vigente es el **Candidate Recommendation Draft del 15-11-2022**, que relaja el supuesto gregoriano. **VERIFICADO** (w3.org/TR/owl-time) | Útil para calendarios no gregorianos y razonamiento de Allen | **No.** En 1806 el Perú ya usaba el calendario gregoriano (vigente en los dominios hispanos desde 1582–1584; dato historiográfico común, no verificado aquí). Duplicaría E52 |
| **Fechas litúrgicas y horas de la época** («primer puesto del gallo», «día de San Juan») | — | Son literales de la capa 1 | Normalizarlas solo en la capa 4 (L2), con autor |

---

## 6. SKOS: buenas prácticas para un esquema histórico y multilingüe

Estado del tesauro (`ontologia/tesauro.ttl`, comprobado): 266 literales `@es`, **0** `@qu` y **0** correspondencias
(`*Match`) externas.

1. **Etiquetas por lengua (BCP 47).**
   * `@es` para el castellano del documento.
   * `@quz` (ISO 639-3 «Cusco Quechua», miembro de la macrolengua `qu`; **VERIFICADO** en iso639-3.sil.org) para
     formas quechuas **atestiguadas**. Si no se sabe la variedad, `@qu`.
   * No existe subetiqueta BCP 47 para el «castellano colonial». Para marcar la época basta `skos:historyNote` o
     `dct:temporal` en el concepto, no la etiqueta.
   * «ayllu» o «curaca» dentro de un documento castellano son préstamos: van `@es`. Añadir `@quz` solo si se quiere
     la forma quechua de referencia (p. ej. *kuraka*), indicando la fuente en `skos:editorialNote`.
2. **Grafías del documento.**
   * En el tesauro van como `skos:altLabel` («casique») o `skos:hiddenLabel` si solo sirven para la búsqueda.
   * Las grafías de **personas** nunca van aquí (capa 2), como ya prescribe el modelo.
   * **SKOS-XL** (`skosxl:Label` con procedencia propia) solo si hace falta citar dónde aparece cada grafía de un
     concepto. Añadiría una dependencia que no está en `vendor/`; hoy no compensa.
3. **Notas.** `skos:definition` (definición de trabajo), `skos:scopeNote` (cuándo usarlo), `skos:historyNote` (cambio
   de significado: p. ej. el *cacique recaudador* después de 1780) y `skos:editorialNote` (pendiente de revisión por
   historiadores). Es lo que ya se hace; falta completar unas 100 definiciones (L9).
4. **Correspondencias externas, con prudencia.**
   * `skos:closeMatch` o `skos:relatedMatch` hacia el AAT y Wikidata. **Nunca `skos:exactMatch` por coincidencia de
     etiqueta.**
   * Ejemplos comprobados el 2026-11-12:
     * `cargo:cacique` → `aat:300379207` *caciques (rulers)* (closeMatch). Wikidata `Q599898` *cacique* se define como
       «Hispanic term for Indigenous Caribbean chief» (sentido taíno): solo `relatedMatch`. `Q2513785` *Kuraka*
       («official of the Inca Empire»): `relatedMatch`.
     * `cargo:corregidor` → `aat:300311300` *corregidores*.
     * `ent:ayllu` → `wd:Q793079` (*ayllu*, «traditional community in the Andes»). **Trampa:** la etiqueta quechua
       «ayllu» también está en `Q8436` (*family*) y `Q177634` (*community*). Un enlazado automático por etiqueta
       fallaría, y es un buen ejemplo para el artículo.
     * Sin equivalente en el AAT (búsqueda sin resultados): *ayllu*, *kuraka*.
5. **Antecedentes con los que dialogar.**
   * El proyecto CAAPT (E. Canning, Oxford) modela terminología colonial problemática con CRM, OntoLex y SKOS (ESWC y
     LDL 2024). **VERIFICADO (indirecto)**.
   * Para un futuro diccionario quechua colonial en LOD, el modelo sería **OntoLex-Lemon** con su módulo lexicográfico
     (W3C CG 2019). **No encontré** González Holguín (1608) ni Santo Tomás (1560) publicados como LLOD (NO VERIFICADO
     de forma exhaustiva).

---

## 7. Proyectos LOD de la América colonial y de los Andes

| Proyecto | Qué hay | Relevancia | Estado |
|---|---|---|---|
| **Candela et al. 2023** (Relaciones Geográficas de México y Guatemala, LLILAS Benson) | Método para pasar colecciones a LOD, enriquecidas con Getty, Wikidata y GeoNames | Hispano colonial, pero a nivel de metadatos de colección (ya descartado en F) | VERIFICADO (Crossref, JOCCH 16(4)) |
| **LatAm gazetteer** (Pelagios, 2018–2019: CAICYT, LLILAS Benson, WHG, HGIS de las Indias, Brumfield Labs) | Alcedo (1786) y Thompson (1812) enlazados con HGIS e ingeridos en WHG | Lugares coloniales en LOD. Repositorio `hdcaicyt/Alcedo` en GitHub | VERIFICADO (indirecto) |
| **PARES / AGI** | Portal con ~8,6 M de registros (2016). Planes de *linked data* para autoridades (ICARUS 2016; artículo en *Revista de la Universidad de Pachuca* sobre autoridades de PARES) | **No encontré** ningún punto SPARQL, volcado RDF ni RiC-O de PARES o del AGI | NO VERIFICADO (ausencia) |
| **AGN Perú / AGN México** | Catálogos en línea (Perú sí, México no, según Iberarchivos 2025) | Sin LOD encontrado | VERIFICADO (indirecto) / ausencia NO VERIFICADA |
| **Archivo Regional del Cusco** | La guía del AGN (2012) lista la sección «Intendencia (1783–1825)». Hay catálogos parciales en PDF (mapapape.agn.gob.pe) | **Ningún KG ni LOD encontrado** | Ausencia NO VERIFICADA de forma exhaustiva |
| **EAP (British Library)** | EAP767 (archivos audiovisuales andinos, Cusco); EAP234 (registros coloniales; Perú, 46 ítems) | Imágenes, no datos estructurados | VERIFICADO (indirecto) |
| **Caciques y cacicazgo** | Abundante historiografía (Ramos, Saignes, O'Phelan…) | **No encontré** ninguna base prosopográfica ni modelo formal de cacicazgo | Ausencia NO VERIFICADA |
| **«Nothing to Link to»** (Nijman y Flora, DH2024) | Señala la falta de vocabularios para entidades del archivo colonial | Argumento de apoyo para nuestro tesauro propio | VERIFICADO (indirecto) |

**Lectura para el artículo:**

* El espacio andino colonial no tiene, que sepamos, ningún grafo con afirmaciones atribuidas ni con separación entre
  mención y reconstrucción.
* Las infraestructuras disponibles son geográficas (HGIS, WHG, LatAm) o de metadatos (Candela 2023).
* El modelo de cacicazgo como **ejercicio de cargo con vigencia** (E7 + PC14 + E52, capa 4) parece no tener
  precedente formal. Conviene presentarlo como contribución, con la cautela de que la ausencia no está probada.

---

## 8. Cambios propuestos, por prioridad

| # | Cambio | Capa | ¿T-Box nueva? | Coste | Prioridad |
|---|---|---|---|---|---|
| 1 | Reescribir D5 (`C_modelo.md` §7 y `C_correspondencias.md`): la extensión en folios sí existe (`rico:CarrierExtent`) y lo que falta es el folio individual | Docs | No | Bajo | Alta |
| 2 | `oa:prefix` / `oa:suffix` en el `TextQuoteSelector`, con su prueba | 2–3 | No | Bajo | Alta |
| 3 | E42 adicionales (TGN, Wikidata) y `dct:source` → DOI de Dataverse en las reconstrucciones de lugar. Documentar la restricción NC-SA de HGIS | 4 | No | Bajo | Alta |
| 4 | `skos:closeMatch` / `skos:relatedMatch` hacia el AAT y Wikidata en `doc:`, `act:`, `cargo:` y `ent:`, revisados a mano, con una prueba que prohíba `skos:exactMatch` hacia fuera | T | No | Medio | Media |
| 5 | Extensión del expediente y de cada pieza en folios con `rico:CarrierExtent` (cuando haya imágenes o catálogo) | 1 | No | Bajo | Media |
| 6 | Etiquetas `@quz` / `@qu` atestiguadas y `skos:historyNote` en los conceptos andinos | T | No | Medio (requiere historiador) | Media |
| 7 | Literal EDTF opcional en R-fechas-normalizadas | 4 | No | Bajo | Baja |
| 8 | Si llegan las imágenes: manifiesto IIIF 3.0, `oa:FragmentSelector` por folio y, opcionalmente, `crmtex:TX6` para el acto de transcribir y `crm:E22` + `P46` para el original | 1–2 | Importa CRMtex | Medio | Futura |

---

## 9. Referencias (datos para BibTeX)

**Especificaciones y vocabularios**

1. ICA-EGAD. *Records in Contexts – Ontology (RiC-O)*, versión 1.1. International Council on Archives, mayo de 2025.
   https://github.com/ICA-EGAD/RiC-O · https://www.ica.org/standards/RiC/ontology. **VERIFICADO**.
2. ICA-EGAD. *Records in Contexts – Conceptual Model (RiC-CM)*, versión 1.0. ICA, 30-11-2023.
   https://www.ica.org/en/records-in-contexts-conceptual-model. **VERIFICADO (indirecto)**.
3. Clavaud, F.; Wildi, T. «ICA Records in Contexts-Ontology (RiC-O): a Semantic Framework for Describing Archival
   Resources». En *Proc. Linked Archives International Workshop 2021*, CEUR-WS vol. 3019, pp. 79–92, 2021.
   https://ceur-ws.org/Vol-3019/. **VERIFICADO**.
4. Francart, T.; Clavaud, F.; Charbonnier, P. «RiC-O Converter: a Software to Convert EAC-CPF and EAD 2002 XML Files to
   RDF Datasets Conforming to Records in Contexts Ontology». CEUR-WS vol. 3019, pp. 30–36, 2021. **VERIFICADO**.
5. CIDOC CRM SIG. *Definition of the CIDOC Conceptual Reference Model*, versión 7.1.3 (= ISO 21127:2023); borradores
   7.3–7.3.2. https://cidoc-crm.org/versions-of-the-cidoc-crm. **VERIFICADO (indirecto)**.
6. Murano, F.; Felicetti, A.; Fafalios, P. (mantenedores); Doerr, M.; Velios, A.; Tsouloucha, E. (colaboradores).
   *Definition of the CRMtex: An Extension of CIDOC CRM to Model Textual Entities*, versión 2.0. CIDOC CRM-SIG, junio
   de 2023. https://cidoc-crm.org/sites/default/files/CRMtex_v2.0_June_2023.pdf; RDF:
   https://cidoc-crm.org/extensions/crmtex/rdfs/2.0/CRMtex_v2.0.rdf. **VERIFICADO**.
7. IFLA LRMoo Working Group; CIDOC CRM SIG. *LRMoo: object-oriented definition and mapping from the IFLA Library
   Reference Model*, v1.0 (2024; autores Aalberg, T.; Riva, P.; Žumer, M.); versión 2 en el repositorio de IFLA,
   18-03-2026. https://repository.ifla.org/items/94aedb49-2d6e-4a6d-9974-f33abb7e3c0e. **VERIFICADO**.
8. FORTH / CIDOC CRM SIG. *Definition of CRMdig*, v4.0 (2022-12-08, «unstable»).
   https://cidoc-crm.org/crmdig. **VERIFICADO (indirecto)**.
9. Linked Art Editorial Board. *Linked Art Model 1.0* (CC BY 4.0), 19-02-2025. https://linked.art/model/ ;
   https://linked.art/model/archives/. **VERIFICADO**.
10. Sanderson, R.; Ciccarese, P.; Young, B. (eds.). *Web Annotation Data Model*. W3C Recommendation, 23-02-2017.
    https://www.w3.org/TR/annotation-model/. **VERIFICADO** (términos en `vendor/oa`).
11. IIIF Consortium. *IIIF Presentation API 3.0* (estable) y *4.0.0-draft*. https://iiif.io/api/presentation/4.0/.
    **VERIFICADO**.
12. Cox, S.; Little, C. (eds.). *Time Ontology in OWL*. W3C/OGC, Candidate Recommendation Draft, 15-11-2022.
    https://www.w3.org/TR/owl-time/. **VERIFICADO**.
13. Library of Congress. *Extended Date/Time Format (EDTF) Specification* (= ISO 8601-2:2019).
    https://www.loc.gov/standards/datetime/. **VERIFICADO (indirecto)**.
14. Grossner, K. et al. *Linked Places Format*, v1.3 (24-06-2024). https://github.com/LinkedPasts/linked-places-format.
    **VERIFICADO**.
15. Palmirani, M.; Governatori, G.; Athan, T.; Boley, H.; Paschke, A.; Wyner, A. (eds.). *LegalRuleML Core
    Specification Version 1.0*. OASIS Standard, 30-08-2021.
    https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/. **VERIFICADO (indirecto)**.
16. OASIS LegalDocML TC. *Akoma Ntoso Version 1.0*, Parts 1–2. OASIS Standard, 29-08-2018.
    https://docs.oasis-open.org/legaldocml/akn-core/v1.0/. **VERIFICADO (indirecto)**.
17. SAA TS-EAS. *EAC-CPF 2.0* (2022). https://eac.staatsbibliothek-berlin.de/. **VERIFICADO (indirecto)**.

**Datos geográficos**

18. Stangl, W. *Data: Places gazetteer of Spanish America, 1701–1808*. Harvard Dataverse, v3.0, 2023.
    doi:10.7910/DVN/FUSJD3. Licencia CC BY-NC-SA 4.0. **VERIFICADO**.
19. Stangl, W. *Data: Territorial gazetteer for Spanish America, 1701–1808*. Harvard Dataverse, v4.0, 2023.
    doi:10.7910/DVN/YPEU5E. CC BY-NC-SA 4.0. **VERIFICADO**.
20. World Historical Gazetteer. *HGIS de las Indias territorios* (dataset 15). https://whgazetteer.org/datasets/15/places.
    **VERIFICADO**.
21. J. Paul Getty Trust. *Getty Thesaurus of Geographic Names* y *Art & Architecture Thesaurus*, LOD, ODC-By 1.0.
    https://vocab.getty.edu/ (tgn:9227290; aat:300189604, 300078817, 300010292, 300027883, 300379207, 300311300).
    **VERIFICADO**.
22. Rabinowitz, A.; Shaw, R.; Buchanan, S.; Golden, P.; Kansa, E. «Making Sense of the Ways We Make Sense of the Past:
    The PeriodO Project». *Bulletin of the Institute of Classical Studies* 59(2): 42–55, 2016.
    doi:10.1111/j.2041-5370.2016.12037.x. **VERIFICADO**.

**Artículos**

23. Vafaie, M.; Bruns, O.; Pilz, N.; Waitelonis, J.; Sack, H. «CourtDocs Ontology: Towards a Data Model for
    Representation of Historical Court Proceedings». En *Proc. 12th Knowledge Capture Conference (K-CAP '23)*, ACM,
    pp. 175–179, 2023. doi:10.1145/3587259.3627562. **VERIFICADO**.
24. Vafaie, M. «German National Socialist Injustice on the Semantic Web: from Archival Records to a Knowledge Graph».
    *Doctoral Consortium at ISWC 2024*, CEUR-WS vol. 3884, 2024. https://ceur-ws.org/Vol-3884/paper8.pdf.
    **VERIFICADO**.
25. Vafaie, M.; Bruns, O.; Pilz, N.; Dessì, D.; Sack, H. «Modelling Archival Hierarchies in Practice: Key Aspects and
    Lessons Learned». *HistoInformatics 2021*, CEUR-WS vol. 2981, 2021. **VERIFICADO**.
26. Yargan, D.; Waitelonis, J.; Vafaie, M.; Sack, H. «BZKO: An Ontology for the Card Index of German Post-War
    Compensation Records». arXiv:2608.06918, 2026 (FOIS 2026 Ontology Showcase / JOWO). **VERIFICADO**.
27. García-González, H.; Bryant, M. «The Holocaust Archival Material Knowledge Graph». En *The Semantic Web – ISWC
    2023*, LNCS, Springer, pp. 362–379, 2023. doi:10.1007/978-3-031-47243-5_20. **VERIFICADO**.
28. Carriero, V. A.; Gangemi, A.; Mancinelli, M. L.; Marinucci, L.; Nuzzolese, A. G.; Presutti, V.; Veninata, C.
    «ArCo: The Italian Cultural Heritage Knowledge Graph». En *The Semantic Web – ISWC 2019*, LNCS, pp. 36–52, 2019.
    doi:10.1007/978-3-030-30796-7_3. **VERIFICADO**.
29. Constantin, A.; Peroni, S.; Pettifer, S.; Shotton, D.; Vitali, F. «The Document Components Ontology (DoCO)».
    *Semantic Web* 7(2): 167–181, 2016. doi:10.3233/SW-150177. **VERIFICADO**.
30. Peroni, S.; Shotton, D. «FaBiO and CiTO: Ontologies for describing bibliographic resources and citations».
    *Journal of Web Semantics* 17: 33–43, 2012. doi:10.1016/j.websem.2012.08.001. **VERIFICADO**.
31. Hoekstra, R.; Breuker, J.; Di Bello, M.; Boer, A. «LKIF Core: Principled Ontology Development for the Legal
    Domain». En *Law, Ontologies and the Semantic Web*, Frontiers in AI and Applications 188, IOS Press, 2009,
    pp. 21–52. doi:10.3233/978-1-58603-942-4-21. **VERIFICADO**.
32. Casanovas, P.; Casellas, N.; Tempich, C.; Vrandečić, D.; Benjamins, R. «OPJK and DILIGENT: ontology modeling in a
    distributed environment». *Artificial Intelligence and Law* 15(2): 171–186, 2007. doi:10.1007/s10506-007-9036-2.
    **VERIFICADO**.
33. Candela, G.; Pereda, J.; Sáez, D.; Escobar, P.; Sánchez, A.; Villa Torres, A.; Palacios, A. A.; McDonough, K.;
    Murrieta-Flores, P. «An Ontological Approach for Unlocking the Colonial Archive». *Journal on Computing and
    Cultural Heritage* 16(4): 1–18, 2023. doi:10.1145/3594727. **VERIFICADO**.
34. Woltjer, P. E. et al. «Persons in Context. A Model to Represent Observations and Reconstructions of Historical
    Persons in Linked Data». *Historical Life Course Studies* 14: 105–125, 2024. doi:10.51964/hlcs19312.
    **VERIFICADO**.
