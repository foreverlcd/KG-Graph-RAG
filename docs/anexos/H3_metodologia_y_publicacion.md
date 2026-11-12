# H3 · Metodología citable, evaluación con un solo validador y dónde publicar

> Informe de búsqueda del 2026-11-12. Cada afirmación lleva una marca:
> * **VERIFICADO**: comprobado en la fuente primaria (página de la revista o del congreso, registro DOI/DBLP/editorial) durante esta búsqueda.
> * **NO VERIFICADO**: procede de fuentes secundarias o no se pudo abrir la fuente primaria. Hay que comprobarlo antes de citarlo o de decidir.
>
> Las fechas de 2027 solo se dan si se publicaron. Si no, se usa la edición de 2026 como indicio y se marca.

## 1. Metodología de ingeniería ontológica que conviene citar y seguir

### 1.1 Qué hizo el proyecto y con qué marco encaja

Lo que el proyecto ya hizo:

* PC redactadas antes de modelar (`docs/B_preguntas_competencia.md`).
* Reutilización sin clases nuevas.
* Pruebas automáticas por PC.
* Formas SHACL con mutaciones negativas.
* Razonador y OOPS!

Este recorrido coincide casi paso a paso con **LOT (Linked Open Terms)**:

1. Especificación de requisitos: ORSD y PC.
2. Implementación con reutilización y pruebas.
3. Publicación: w3id, documentación HTML y metadatos FAIR.
4. Mantenimiento.

Recomendación:

* Declarar **LOT** como metodología seguida.
* Citar **NeOn** por el escenario de *reutilización y reingeniería de recursos ontológicos*. NeOn es el antecedente de LOT, y el escenario es exactamente lo que hace un perfil de aplicación sin clases nuevas.
* Mencionar **eXtreme Design (XD)** y los **patrones de diseño (ODP)** solo si se describen las decisiones como patrones (por ejemplo, el patrón afirmación–afirmante–fuente). No hay que declarar XD si no se siguió.

| Referencia | Datos | Estado |
|---|---|---|
| LOT | Poveda-Villalón, M.; Fernández-Izquierdo, A.; Fernández-López, M.; García-Castro, R. (2022). «LOT: An industrial oriented ontology engineering framework». *Engineering Applications of Artificial Intelligence* 111: 104755. DOI 10.1016/j.engappai.2022.104755. Sitio: https://lot.linkeddata.es | VERIFICADO (DBLP, Scilit) |
| NeOn | Suárez-Figueroa, M. C.; Gómez-Pérez, A.; Fernández-López, M. (2015). «The NeOn Methodology framework: A scenario-based methodology for ontology development». *Applied Ontology* 10(2): 107–145. DOI 10.3233/AO-150145 | VERIFICADO (IOS Press) |
| ORSD | Suárez-Figueroa, M. C.; Gómez-Pérez, A.; Villazón-Terrazas, B. (2009). «How to Write and Use the Ontology Requirements Specification Document». OTM 2009, LNCS 5871, pp. 966–982. DOI 10.1007/978-3-642-05151-7_16 | VERIFICADO (Springer, DBLP) |
| XD | Blomqvist, E.; Hammar, K.; Presutti, V. (2016). «Engineering Ontologies with Patterns – The eXtreme Design Methodology». En Hitzler, P. et al. (eds.), *Ontology Engineering with Ontology Design Patterns*, Studies on the Semantic Web 25, IOS Press, pp. 23–50. ISBN 978-1-61499-675-0 | VERIFICADO (DBLP; libro en IOS Press). DOI del capítulo NO VERIFICADO |
| ODP | Gangemi, A.; Presutti, V. (2009). «Ontology Design Patterns». En Staab, S.; Studer, R. (eds.), *Handbook on Ontologies*, 2.ª ed., Springer, pp. 221–243. DOI 10.1007/978-3-540-92673-3_10 | VERIFICADO (RePEc, IRIS Unibo) |

### 1.2 Preguntas de competencia (PC)

* **Fuente clásica.** Grüninger, M.; Fox, M. S. (1995). «Methodology for the Design and Evaluation of Ontologies». IJCAI-95 Workshop on Basic Ontological Issues in Knowledge Sharing, Montreal. Ya está en el anexo F. Es actas de taller y no tiene DOI.
* **PC → SPARQL.** Wiśniewski et al. 2019, *J. Web Semantics*, DOI 10.1016/j.websem.2019.100534. Ya está en el anexo F.
* **Autoría guiada por PC.** Ren, Y.; Parvizi, A.; Mellish, C.; Pan, J. Z.; van Deemter, K.; Stevens, R. (2014). «Towards Competency Question-Driven Ontology Authoring». ESWC 2014, LNCS 8465, pp. 752–767. DOI 10.1007/978-3-319-07443-6_50. **VERIFICADO** (DBLP, OUCI).
* **Tipos de PC.** Keet, C. M.; Khan, Z. C. (2024). «Discerning and Characterising Types of Competency Questions for Ontologies». arXiv:2412.13688.
  * Propone cinco tipos: *scoping*, *validating*, *foundational*, *relationship* y *metaproperty*.
  * Sirve para clasificar nuestras 20 PC, porque las 6 de DISPUTA/NC son PC de validación.
  * **VERIFICADO** como preprint. No encontré la versión publicada: el título «On the roles of competency questions…» que se había sugerido **no se localizó**, así que no se cita.
* **PC y LLM** (relevante, porque el proyecto usa un LLM como modelador):
  * Rebboud, Y.; Tailhardat, L.; Lisena, P.; Troncy, R. (2024). «Can LLMs Generate Competency Questions?». ESWC 2024 Satellite Events, LNCS. DOI 10.1007/978-3-031-78952-6_7. **VERIFICADO** (EURECOM). El número de volumen LNCS no está verificado.
  * Zhang, B.; Carriero, V. A.; Schreiberhuber, K.; Tsaneva, S.; Sánchez González, L.; Kim, J.; de Berardinis, J. (2024). «OntoChat: a Framework for Conversational Ontology Engineering using Language Models». ESWC 2024, Special Track LLMs for KE. arXiv:2403.05921. **VERIFICADO** (programa ESWC 2024, arXiv). El DOI de las actas no está verificado.
  * Lippolis, A. S.; Ragagni, M.; Ciancarini, P.; Nuzzolese, A. G.; Presutti, V. (2025). «Bench4KE: Benchmarking Automated Competency Question Generation». arXiv:2505.24554. **VERIFICADO** como preprint. Ojo: la v3 cambia el estándar de oro de 4 a 17 proyectos, así que hay que citar la versión concreta.
* **Encuesta de práctica.** Quirino, Salamon y Barcellos (2023) encuestan a 63 ingenieros de ontologías sobre el uso de PC. **NO VERIFICADO**: solo se vio el PDF de NEMO/UFES, sin datos de publicación.

**Punto a favor que hay que hacer explícito en el artículo.** Las PC se redactaron *antes* de modelar y la hipótesis de las líneas base se registró antes de medir (`docs/B_preguntas_competencia.md`, `docs/G_evaluacion.md` §7). Esto es un **prerregistro** y conviene llamarlo así.

### 1.3 Evaluación: herramientas y marcos

| Herramienta / marco | Referencia | Estado | Uso en el proyecto |
|---|---|---|---|
| OOPS! | Poveda-Villalón, Gómez-Pérez, Suárez-Figueroa (2014), *IJSWIS* 10(2), DOI 10.4018/ijswis.2014040102 | Ya en el anexo F | Hecho (0 críticas) |
| FOOPS! (FAIR) | Garijo, D.; Corcho, O.; Poveda-Villalón, M. (2021). «FOOPS!: An Ontology Pitfall Scanner for the FAIR principles». ISWC 2021 Posters, Demos and Industry Tracks, CEUR-WS Vol-2980, paper 321. Servicio: https://w3id.org/foops | VERIFICADO (CEUR, repositorio oeg-upm/fair_ontologies) | **Pendiente.** Requiere publicar en w3id con metadatos. El número de pruebas varía según la versión (24 en 2021, 33 en 2024): hay que dar la versión usada |
| FAIR para ontologías | Poveda-Villalón, M.; Espinoza-Arias, P.; Garijo, D.; Corcho, O. (2020). «Coming to Terms with FAIR Ontologies». EKAW 2020, LNCS 12387, pp. 255–270. DOI 10.1007/978-3-030-61244-3_18 | VERIFICADO (DBLP) | Marco de la sección de disponibilidad |
| Buenas prácticas FAIR | Garijo, D.; Poveda-Villalón, M. (2020). «Best Practices for Implementing FAIR Vocabularies and Ontologies on the Web». arXiv:2003.13084 | VERIFICADO (arXiv). La versión en libro de IOS Press no está verificada | Lista de metadatos |
| FAIR (origen) | Wilkinson, M. D. et al. (2016). «The FAIR Guiding Principles for scientific data management and stewardship». *Scientific Data* 3: 160018. DOI 10.1038/sdata.2016.18 | VERIFICADO | — |
| OntoMetrics | Lantow, B. (2016). «OntoMetrics: Putting Metrics into Use for Ontology Evaluation». KEOD 2016 (IC3K), vol. 2, pp. 186–191. DOI 10.5220/0006084601860191 | VERIFICADO | **Poco útil.** Un perfil sin clases propias da métricas triviales. Si se usa, que sea solo como descripción |
| Pruebas unitarias de ontologías | Vrandečić, D.; Gangemi, A. (2006). «Unit Tests for Ontologies». OTM 2006 Workshops, LNCS 4278, pp. 1012–1020. DOI 10.1007/11915072_2 | VERIFICADO | Antecedente de las pruebas por PC y de las mutaciones |
| Themis | Fernández-Izquierdo, A.; García-Castro, R. (2019). «How to Validate Ontologies with Themis». ESWC 2019 Satellite Events, LNCS 11762. DOI 10.1007/978-3-030-32327-1_11 | VERIFICADO (DOI). El artículo SEKE 2019 «Themis: a tool…» existe, pero su DOI **NO** está verificado | Validación a partir de requisitos |
| Encuesta de evaluación | McDaniel, M.; Storey, V. C. (2019). «Evaluating Domain Ontologies: Clarification, Classification, and Challenges». *ACM Computing Surveys* 52(4): 70:1–70:44. DOI 10.1145/3329124 | VERIFICADO (DBLP) | Para situar los criterios (*task-ontology fit*) |
| SHACL | W3C Recommendation, 20 julio 2017, «Shapes Constraint Language (SHACL)», https://www.w3.org/TR/shacl/ | Conocido, no se volvió a abrir | — |

**Aportación metodológica propia que conviene destacar.** Ninguna de las referencias anteriores propone las **pruebas de mutación sobre formas SHACL**: exigir que cada forma con nombre dispare ante al menos una mutación. Es lo que detectó que `ActuacionForma` aprobaba en vacío. Es un detalle concreto y verificable que el artículo debe contar como contribución menor. No busqué a fondo si existe un precedente publicado de «mutation testing for SHACL», así que **NO VERIFICADO** que sea inédito: hay que hacer una búsqueda antes de reclamar novedad.

### 1.4 Publicación: identificadores, documentación y DOI

* **w3id.org.**
  * Se pide un *fork* de `github.com/perma-id/w3id.org`, se añade una carpeta `laad/` con un `.htaccess` y se abre un *pull request*. Al aceptarlo, entra en vigor de inmediato.
  * Se espera un compromiso de duración de más de 20 años y un contacto responsable.
  * **VERIFICADO** en los README del repositorio y en la guía de OBO Academy.
  * El espacio `w3id.org/laad` está hoy **solo declarado** (`docs/C_modelo.md` l. 44). Es requisito duro para ESWC/ISWC, que piden PURL, DOI o w3id.
* **WIDOCO.** Garijo, D. (2017). «WIDOCO: A Wizard for Documenting Ontologies». ISWC 2017, LNCS 10588, pp. 94–102. DOI 10.1007/978-3-319-68204-4_9. **VERIFICADO.** Ganó el premio al mejor artículo del Resources Track. El software tiene su propio DOI en Zenodo: 10.5281/zenodo.591294. Genera HTML, negociación de contenido y la evaluación OOPS! integrada.
* **LODE.** Peroni, S.; Shotton, D.; Vitali, F. (2012). «The Live OWL Documentation Environment: A Tool for the Automatic Generation of Ontology Documentation». EKAW 2012, LNCS 7603, pp. 398–412. DOI 10.1007/978-3-642-33876-2_35. **VERIFICADO.** Cuidado: el DOI que termina en `_37` es otro artículo («Latest Developments to LODE»).
* **pyLODE.**
  * Car, N. et al., pyLODE, RDFLib, licencia BSD-3, https://github.com/RDFLib/pyLODE. **VERIFICADO** (GitHub, PyPI).
  * Se cita como software, con la versión exacta. Soporta perfiles OWL y SKOS, así que viene bien para el tesauro.
  * **Recomendación:** pyLODE para el tesauro y la ontología (proyecto en Python) y WIDOCO si se quiere la página completa con negociación de contenido.
* **Zenodo.**
  * Usar la integración GitHub → Zenodo para que cada *release* tenga un DOI de versión y además un *concept DOI* para todas las versiones.
  * Añadir `CITATION.cff` en la raíz del repositorio.
  * La «cita canónica» del recurso es el concept DOI.
  * NO VERIFICADO en esta búsqueda: es práctica conocida y no se volvió a abrir la documentación de Zenodo.

## 2. Cómo evaluar con rigor teniendo un solo validador humano

### 2.1 Qué dice la literatura

* **No hay sustituto pleno del acuerdo entre anotadores.**
  * Artstein y Poesio (2008), ya en el anexo F, explican por qué la repetición por la misma persona no equivale a otro anotador: recuerda lo que hizo.
  * Krippendorff, K. (2018). *Content Analysis: An Introduction to Its Methodology*, 4.ª ed., SAGE, ISBN 978-1-5063-9566-1. **VERIFICADO** (ISBN y edición). Esta es la edición que conviene citar en lugar de la 2.ª (2004) que menciona `G_evaluacion.md` §4. Los umbrales α ≥ 0,800 y ≥ 0,667 aparecen en todas las ediciones, pero la página exacta **NO** está verificada.
* **Acuerdo intra-anotador como medida de estabilidad.** Abercrombie, G.; Dinkar, T.; Cercas Curry, A.; Rieser, V.; Hovy, D. (2023). «Consistency is Key: Disentangling Label Variation in Natural Language Processing with Intra-Annotator Agreement». arXiv:2301.10684 (aceptado en NLPerspectives).
  * Encuentran que los anotadores se contradicen consigo mismos en torno al 25 % de las veces.
  * Proponen informar el acuerdo intra-anotador junto al inter-anotador.
  * **VERIFICADO** en arXiv. Los datos de las actas no están verificados.
* **Un LLM como «anotador alternativo».** Calderon, N.; Reichart, R.; Dror, R. (2025). «The Alternative Annotator Test for LLM-as-a-Judge: How to Statistically Justify Replacing Human Annotators with LLMs». ACL 2025 (Long Papers), pp. 16051–16081. DOI 10.18653/v1/2025.acl-long.782. **VERIFICADO.**
  * El *alt-test* **exige varios anotadores humanos** (compara el LLM con cada humano, dejando uno fuera).
  * Con un solo validador no se puede aplicar tal cual.
  * Sirve para justificar que el LLM *no* puede usarse como segundo anotador sin al menos un pequeño subconjunto doblemente anotado.
* **Gilardi, F.; Alizadeh, M.; Kubli, M. (2023).** «ChatGPT outperforms crowd workers for text-annotation tasks». *PNAS* 120(30): e2305016120. DOI 10.1073/pnas.2305016120. **VERIFICADO.** Solo vale para tareas de clasificación sencillas, no para paleografía ni atribución jurídica. Se cita para acotar, no para respaldar.
* **Criterio de las revistas.**
  * SWJ, para las descripciones de ontologías, pide «convincing evidence» de calidad y relevancia, no acuerdo entre anotadores. **VERIFICADO** en la página «For Authors».
  * La evidencia de **uso por terceros** es lo que más pesa (FAQ 20: impacto I > II > III). **VERIFICADO.**
  * Conclusión: en un *resource paper* el estándar de oro de dos anotadores no es obligatorio. Lo que se exige es calidad demostrable, reutilizabilidad y disponibilidad.

### 2.2 Diseño recomendado con un solo validador (por orden de valor)

1. **Separar dos afirmaciones del artículo:**
   * **(a)** «El modelo puede representar X»: es verificable mecánicamente con PC, SHACL, razonador y el segundo expediente sin clases nuevas.
   * **(b)** «La extracción es correcta»: requiere un humano.

   El artículo de recurso se apoya en (a). Para (b), el texto debe decir que es **evaluación preliminar con un solo validador**, sin α.
2. **Validador ciego y respuestas fijadas antes de ver el grafo.** Ya está diseñado en `G_evaluacion.md` §3. Con un solo historiador se mantiene igual: es una **evaluación por experto**, no un estándar de oro, y se informa el número de aciertos por PC con el razonamiento de cada fallo.
3. **Acuerdo intra-anotador.** El validador vuelve a anotar a ciegas un subconjunto, por ejemplo el 20 % de las afirmaciones, elegido con una semilla fija, tras un intervalo de al menos 2–4 semanas.
   * Se informa α intra (Abercrombie et al. 2023) **llamándolo estabilidad, no fiabilidad**.
   * Se declaran las amenazas: memoria y fatiga (Artstein y Poesio 2008).
   * La duración del intervalo no tiene norma aceptada: hay que justificarla.
4. **Comprobaciones deterministas como «segundo juez» donde se puede.**
   * Cita literal al 100 %: ya está.
   * Desplazamientos de tramo.
   * Cotejo con el catálogo del ARC (criterio 6).

   Estas medidas no dependen de nadie y deben ocupar el primer lugar en la tabla de evaluación.
5. **Triangulación con fuentes independientes** (criterio 6): el catálogo, HGIS y la bibliografía son «jueces» externos para parte de las afirmaciones.
6. **LLM como segundo anotador, solo como diagnóstico.**
   * Puede servir para localizar desacuerdos que el validador revisa.
   * **No** se informa como acuerdo entre anotadores.
   * Sin al menos dos humanos no puede validarse con el *alt-test* (Calderon et al. 2025).
7. **Paquete de reproducibilidad.**
   * *Release* con DOI de Zenodo.
   * N-Quads ordenado (ya existe, commit `e5b2cb8`).
   * Semillas, versiones de las dependencias y de los estándares importados, y respuestas de OOPS! guardadas.
   * Prompts y modelo del LLM.
   * Hoja de anotación del validador.
8. **Invitar a la revisión abierta.** SWJ publica los manuscritos y las revisiones (**VERIFICADO**, FAQ Q1). Un historiador externo puede comentar sin ser coautor. Esto no sustituye la anotación, pero aumenta el escrutinio.

**Precedentes.** No encontré un artículo de ontología de patrimonio que justifique de forma explícita una evaluación con un solo experto como diseño aceptado. **NO VERIFICADO** que exista. Lo habitual en los *resource tracks* es apoyarse en pruebas automáticas, PC y casos de uso, y las convocatorias no exigen IAA (ESWC 2026, criterios **VERIFICADOS**). Por tanto, lo honesto y suficiente es declarar la limitación en «Limitations» y no presentar la parte (b) como resultado principal.

## 3. Dónde publicar

### 3.1 Tabla de sedes

| Sede | Encaje | Idioma | Plantilla / extensión | Plazos y costes | Estado |
|---|---|---|---|---|---|
| **ESWC 2027 – Resources Track** (24.ª ESWC, Limassol, Chipre, 23–27 may 2027) | Alto. Acepta explícitamente «ontologies, vocabularies… with papers describing the modeling process» (convocatoria 2026) | Solo inglés | LNCS (`llncs`), máx. **15 pp.** sin referencias; PDF o HTML | Resumen **10 dic 2026**, artículo **17 dic 2026**, réplica 26–29 ene, notificación 19 feb, versión final 18 mar 2027. Revisión con autores visibles para los revisores (*single-anonymous*). Hay que inscribirse y asistir. Hay que declarar el uso de IA generativa (política ACM) | Fechas, formato e idioma VERIFICADOS en la convocatoria general de 2027. Los criterios del Resources Track 2027 no estaban publicados; se usan los de 2026 (VERIFICADOS): URI persistente (PURL/DOI/w3id), licencia, registro en LOV/Zenodo, plan de sostenibilidad y enlaces del recurso tras el resumen |
| **ISWC 2027 – Resources Track** | Alto, mismos criterios | Inglés | LNCS, 15 pp. (ediciones anteriores) | La sede de 2027 no estaba publicada; las fechas de 2026 eran en mayo | NO VERIFICADO para 2027. La declaración de disponibilidad de recursos (*Resource Availability Statement*) antes de las referencias, que cuenta en las 15 pp., está VERIFICADA para 2024 |
| **SWODCH 2027** (taller de ontologías para patrimonio, junto a ISWC) | **Muy alto** en tema: diseño de ontologías para humanidades digitales, análisis de CIDOC CRM, FAIR, ingeniería ontológica asistida por IA | Inglés | CEUR-ART una columna; completo 10–12 pp. y corto 6–8 pp., **referencias incluidas** | 2026: plazo 26 jun, junto a ISWC (Bari). 2027 no publicado | VERIFICADO para 2026. Es un taller (CEUR): pesa menos, pero es plazo realista y da comunidad |
| **Semantic Web Journal** (IOS Press/Sage) | Alto. Tipo «Ontology description» (diseño, metodología, comparación, ejemplos) | Inglés (de hecho) | Plantilla LaTeX de **Sage** (no la antigua de IOS Press); sin límite fijo para las descripciones de ontologías («brief»). Hay que entregar los datos en un archivo con README en una URL estable (Zenodo/GitHub/Figshare), sin cambios durante la revisión | APC **2100 USD** (envíos desde 1 sep 2024). Revisión abierta. Pesa mucho la **evidencia de uso por terceros** (FAQ 20) | VERIFICADO (For Authors, FAQ). El número especial sobre ontologías para patrimonio (2025) exigía **estimar el coste energético y la huella de carbono** si se usan LLM; puede repetirse |
| **ACM JOCCH** | Alto en tema (precedente: Candela et al. 2023, anexo F) | Inglés | `acmart`; la documentación de acmart asigna JOCCH al formato `acmlarge`. No encontré límite de páginas | Desde 2026, ACM es totalmente de acceso abierto: APC, ACM Open o exención | Formato VERIFICADO en la documentación de acmart (CTAN). La cuantía del APC, la exención para Perú y si UNSAAC está en ACM Open están **NO VERIFICADOS**: preguntar a la biblioteca |
| **Digital Scholarship in the Humanities** (OUP) | Medio: público de humanidades digitales, menos interés en SHACL | **Solo inglés** | Completo ≤ 9000 palabras; corto ≤ 5000; resumen estructurado ≤ 250; Word o LaTeX OUP (Harvard); sección «Data availability» obligatoria | Acceso abierto opcional con pago | VERIFICADO |
| **Digital Humanities Quarterly** | Alto para la tesis humanística (disputa, atribución, «no lo dice») | Inglés, **español**, francés y portugués | Sin límite indicado en el FAQ | **Sin cargos**; revisión de 2–4 meses; CC BY-ND | VERIFICADO (FAQ, DOAJ) |
| **Revista de Humanidades Digitales** (UNED) | Alto, en español | Preferente **español**; también PT, EN, FR, IT | Artículo ≤ 10 000 palabras; nota ≤ 7000; plantilla .docx de la revista; APA 7; 5 palabras clave de TaDiRAH; ORCID | No se mencionan cargos (DOAJ: sin APC) | VERIFICADO (normas de la revista; APC según DOAJ) |
| **Journal of Web Semantics** (Elsevier) | Medio | Inglés | `elsarticle`. Una fuente antigua dice 6–8 pp. a doble columna para artículos de ontología | Acceso abierto con APC (~1730 USD según una ficha de 2026) | **NO VERIFICADO**: no se pudo abrir la guía de Elsevier |
| **Applied Ontology** (IOS Press/Sage) | Medio. Tiene el tipo **«Brief Ontology Report»**, pero la revista es fuerte en formalización y un perfil sin clases nuevas puede parecer poco | Inglés | LaTeX de Sage | APC no encontrado | Tipos y plantilla VERIFICADOS (Sage). APC NO VERIFICADO |
| **TGDK** (Dagstuhl) | Bajo por ahora: los artículos de recurso exigen «already had significant impact» | Inglés | — | **Acceso abierto diamante** (sin cargos); consulta previa de ≤ 500 palabras | VERIFICADO (convocatoria de recursos). Opción para dentro de 1–2 años |
| **Journal of Open Humanities Data** | Medio: artículo de datos breve sobre el grafo y la transcripción | Solo inglés | Artículo de datos 1000–1500 palabras; artículo de discusión 3000–5000 | APC **1070 £** (exención a petición) | VERIFICADO |
| **Data Intelligence** | Acepta «data articles» (grafos de conocimiento, ontologías) | Inglés | — | La editorial y el APC de 2026 no están claros | **NO VERIFICADO** |
| **Inteligencia Artificial** (rev. iberoamericana, IBERAMIA) | Bajo/medio: perfil de IA general | Español o portugués con metadatos en inglés | — | Acceso abierto | Idioma VERIFICADO (página de envíos) |
| **CLEI** (conferencia latinoamericana) | Medio, regional | Español, portugués o inglés | Completo ≤ 10 pp.; en curso ≤ 4 pp. (2026, Ciudad de México, 7–11 sep) | IEEE Xplore en 2025; para 2026 y 2027 no verificado | Datos de 2026 VERIFICADOS; 2027 sin convocatoria |
| **SIMBig** (Perú) | Medio, regional, CCIS de Springer | Inglés | — | 2026: Arequipa, 28–30 oct; plazo 7 ago (cerrado) | VERIFICADO para 2026; 2027 sin convocatoria |
| **KGSWC** | Bajo/medio | Inglés | LNCS (pendiente de aprobación), 12–15 pp. | 2026 en Belgrado (no iberoamericana) | VERIFICADO para 2026 |

### 3.2 Recomendación

**Objetivo principal: ESWC 2027, Resources Track, en inglés, con `llncs`, 15 páginas más referencias.**

Por qué:
* Es el tipo de artículo que mejor recibe lo que el proyecto tiene de sólido: perfil reutilizable, PC prerregistradas como pruebas, mutaciones SHACL, razonador con un defecto real encontrado en ROAR (D1) y reproducibilidad.
* No exige estándar de oro de dos anotadores.
* La revisión con autores visibles no penaliza el ser estudiantes.
* Publica en LNCS y es de acceso abierto en versión preliminar.

Condiciones duras antes del **10 dic 2026** (resumen) y el **17 dic 2026** (artículo):
1. Registrar `w3id.org/laad` (*pull request* aceptado).
2. *Release* con DOI de Zenodo y licencia: CC BY 4.0 para la ontología y los datos, MIT o Apache-2.0 para el código.
3. Documentación HTML con pyLODE o WIDOCO.
4. FOOPS! ejecutado e informado.
5. Registro en LOV si es posible (dicen «community registries»).
6. Declaración de uso de IA generativa. El LLM es el modelador, así que el texto debe explicarlo con detalle; los revisores de recursos valoran la transparencia.

El riesgo es el plazo: unas 5 semanas. La escasa evidencia de adopción externa se compensa con la reutilización explícita de 8 estándares y con el segundo expediente elegido a ciegas.

**Alternativa A (si no se llega a diciembre o se rechaza): SWODCH 2027** junto a ISWC 2027, en CEUR-ART, 10–12 pp. con referencias. Encaje temático máximo. El taller acepta artículos rechazados de las sedes principales si encajan en el tema; así lo hacía Sci-K en 2026, pero en SWODCH **NO está verificado**. Después se amplía a **SWJ, «Ontology description»**, cuando haya validación del historiador y algún uso externo, porque SWJ pesa mucho el impacto. Además, el APC de 2100 USD exige buscar financiación o exención.

**Artículo complementario en español** (otro énfasis, sin duplicar): **DHQ** (sin cargos, acepta español) o **Revista de Humanidades Digitales** (UNED; español preferente; sin APC según DOAJ).
* Enfoque: el problema historiográfico de modelar testimonio en disputa, el «no lo dice» y la atribución, con el grafo como instrumento.
* Debe citar el artículo técnico y no repetir su evaluación.
* No conviene llevar el artículo técnico a sedes en español: el público de ingeniería ontológica y los criterios de recurso están en inglés.

**No recomendado ahora:**
* TGDK: exige impacto ya demostrado.
* JOHD y DSH: solo inglés y con APC (JOHD) o público menos técnico (DSH).
* JWS: datos no verificados.
* JOCCH: buen encaje, pero hay que aclarar antes el APC de ACM Open para UNSAAC. Si la universidad tiene acuerdo o hay exención geográfica, JOCCH pasa a ser la mejor revista para la versión ampliada.

## 4. Estructura típica de un artículo de recurso u ontología sólido

Basada en las convocatorias de recursos de ESWC 2026 e ISWC (2017, 2019, 2024), en los requisitos de SWJ para descripciones de ontologías y en el formato de TGDK. Todas VERIFICADAS.

0. **Resumen y, justo debajo, el bloque «Resource»**: tipo, licencia, DOI y URL (ESWC 2026 lo pide tras el resumen).
1. **Introducción**: problema (testimonio judicial colonial en disputa), brecha y contribuciones numeradas.
2. **Trabajos relacionados y recursos similares**: RiC-O, CRM/CRMinf, PiCo, ROAR, Golden Agents y Candela et al. 2023. Comparación explícita: qué aporta frente a lo que ya existe.
3. **Requisitos**: ORSD resumido (propósito, alcance, usuarios, requisitos no funcionales) y las 20 PC clasificadas, con mención al prerregistro.
4. **Metodología**: LOT, con el escenario de reutilización de NeOn, y el papel del LLM como modelador (con la declaración de IA).
5. **El modelo**: las cuatro capas, el patrón afirmación–afirmante–fuente, un diagrama, correspondencias con los estándares y decisiones con sus alternativas descartadas.
6. **Implementación y uso**: transformación, consultas con nombre y un ejemplo de PC de DISPUTA de principio a fin.
7. **Evaluación**:
   * (a) verificación: PC como pruebas, SHACL con mutaciones, razonador (D1 de ROAR), OOPS! y FOOPS!;
   * (b) generalización: segundo expediente a ciegas;
   * (c) validación por experto (un solo validador, declarado) y estabilidad intra-anotador.
8. **Disponibilidad, reutilización y sostenibilidad**:
   * w3id y Zenodo (concept DOI = **cita canónica**).
   * Licencias.
   * Documentación HTML.
   * Registro en LOV.
   * Versionado semántico.
   * Plan de mantenimiento: quién, cómo, issues en GitHub, y qué pasa al acabar el curso o la tesis.
9. **Limitaciones**:
   * un solo expediente;
   * un solo validador;
   * OWL RL no completo;
   * CRM en RDFS;
   * dependencia de un LLM;
   * folios r/v sin cotejar.
10. **Conclusiones y trabajo futuro.**
11. **Declaración de disponibilidad de recursos** (*Resource Availability Statement*), antes de las referencias (ISWC: cuenta para el límite de páginas).
12. Reconocimientos (incluido el uso de IA si la sede lo pide ahí, como SWJ) y referencias.

**Cita canónica:** una sola entrada BibTeX del recurso con el concept DOI de Zenodo, más el `CITATION.cff` del repositorio. ISWC 2017 pedía «canonical citation» explícitamente (VERIFICADO en el resumen de búsqueda de la convocatoria de 2017).

## 5. BibTeX (solo entradas VERIFICADAS)

```bibtex
@article{PovedaVillalon2022LOT,
  author  = {Poveda-Villal{\'o}n, Mar{\'i}a and Fern{\'a}ndez-Izquierdo, Alba and Fern{\'a}ndez-L{\'o}pez, Mariano and Garc{\'i}a-Castro, Ra{\'u}l},
  title   = {{LOT}: An industrial oriented ontology engineering framework},
  journal = {Engineering Applications of Artificial Intelligence},
  volume  = {111},
  pages   = {104755},
  year    = {2022},
  doi     = {10.1016/j.engappai.2022.104755}
}
@article{SuarezFigueroa2015NeOn,
  author  = {Su{\'a}rez-Figueroa, Mari Carmen and G{\'o}mez-P{\'e}rez, Asunci{\'o}n and Fern{\'a}ndez-L{\'o}pez, Mariano},
  title   = {The {NeOn} Methodology framework: A scenario-based methodology for ontology development},
  journal = {Applied Ontology},
  volume  = {10},
  number  = {2},
  pages   = {107--145},
  year    = {2015},
  doi     = {10.3233/AO-150145}
}
@inproceedings{SuarezFigueroa2009ORSD,
  author    = {Su{\'a}rez-Figueroa, Mari Carmen and G{\'o}mez-P{\'e}rez, Asunci{\'o}n and Villaz{\'o}n-Terrazas, Boris},
  title     = {How to Write and Use the Ontology Requirements Specification Document},
  booktitle = {On the Move to Meaningful Internet Systems: OTM 2009},
  series    = {LNCS},
  volume    = {5871},
  pages     = {966--982},
  publisher = {Springer},
  year      = {2009},
  doi       = {10.1007/978-3-642-05151-7_16}
}
@incollection{Blomqvist2016XD,
  author    = {Blomqvist, Eva and Hammar, Karl and Presutti, Valentina},
  title     = {Engineering Ontologies with Patterns -- The {eXtreme Design} Methodology},
  booktitle = {Ontology Engineering with Ontology Design Patterns},
  editor    = {Hitzler, Pascal and Gangemi, Aldo and Janowicz, Krzysztof and Krisnadhi, Adila and Presutti, Valentina},
  series    = {Studies on the Semantic Web},
  volume    = {25},
  pages     = {23--50},
  publisher = {IOS Press},
  year      = {2016},
  isbn      = {978-1-61499-675-0}
}
@incollection{Gangemi2009ODP,
  author    = {Gangemi, Aldo and Presutti, Valentina},
  title     = {Ontology Design Patterns},
  booktitle = {Handbook on Ontologies},
  editor    = {Staab, Steffen and Studer, Rudi},
  edition   = {2},
  pages     = {221--243},
  publisher = {Springer},
  year      = {2009},
  doi       = {10.1007/978-3-540-92673-3_10}
}
@inproceedings{Ren2014CQ,
  author    = {Ren, Yuan and Parvizi, Artemis and Mellish, Chris and Pan, Jeff Z. and van Deemter, Kees and Stevens, Robert},
  title     = {Towards Competency Question-Driven Ontology Authoring},
  booktitle = {The Semantic Web: Trends and Challenges (ESWC 2014)},
  series    = {LNCS},
  volume    = {8465},
  pages     = {752--767},
  publisher = {Springer},
  year      = {2014},
  doi       = {10.1007/978-3-319-07443-6_50}
}
@misc{Keet2024CQTypes,
  author        = {Keet, C. Maria and Khan, Zubeida Casmod},
  title         = {Discerning and Characterising Types of Competency Questions for Ontologies},
  year          = {2024},
  eprint        = {2412.13688},
  archivePrefix = {arXiv}
}
@inproceedings{Rebboud2024LLMCQ,
  author    = {Rebboud, Youssra and Tailhardat, Lionel and Lisena, Pasquale and Troncy, Rapha{\"e}l},
  title     = {Can {LLMs} Generate Competency Questions?},
  booktitle = {The Semantic Web: ESWC 2024 Satellite Events},
  series    = {LNCS},
  publisher = {Springer},
  year      = {2025},
  doi       = {10.1007/978-3-031-78952-6_7},
  note      = {Volumen LNCS por confirmar}
}
@misc{Zhang2024OntoChat,
  author        = {Zhang, Bohui and Carriero, Valentina Anita and Schreiberhuber, Katrin and Tsaneva, Stefani and S{\'a}nchez Gonz{\'a}lez, Luc{\'i}a and Kim, Jongmo and de Berardinis, Jacopo},
  title         = {{OntoChat}: a Framework for Conversational Ontology Engineering using Language Models},
  year          = {2024},
  eprint        = {2403.05921},
  archivePrefix = {arXiv},
  note          = {ESWC 2024, Special Track on LLMs for Knowledge Engineering}
}
@misc{Lippolis2025Bench4KE,
  author        = {Lippolis, Anna Sofia and Ragagni, Minh Davide and Ciancarini, Paolo and Nuzzolese, Andrea Giovanni and Presutti, Valentina},
  title         = {{Bench4KE}: Benchmarking Automated Competency Question Generation},
  year          = {2025},
  eprint        = {2505.24554},
  archivePrefix = {arXiv},
  note          = {Citar la versi{\'o}n (v3 cambia el est{\'a}ndar de oro); nombres de pila por confirmar}
}
@inproceedings{Garijo2021FOOPS,
  author    = {Garijo, Daniel and Corcho, Oscar and Poveda-Villal{\'o}n, Mar{\'i}a},
  title     = {{FOOPS!}: An Ontology Pitfall Scanner for the {FAIR} principles},
  booktitle = {Proceedings of the ISWC 2021 Posters, Demos and Industry Tracks},
  series    = {CEUR Workshop Proceedings},
  volume    = {2980},
  year      = {2021},
  url       = {https://ceur-ws.org/Vol-2980/paper321.pdf}
}
@inproceedings{PovedaVillalon2020FAIR,
  author    = {Poveda-Villal{\'o}n, Mar{\'i}a and Espinoza-Arias, Paola and Garijo, Daniel and Corcho, Oscar},
  title     = {Coming to Terms with {FAIR} Ontologies},
  booktitle = {Knowledge Engineering and Knowledge Management (EKAW 2020)},
  series    = {LNCS},
  volume    = {12387},
  pages     = {255--270},
  publisher = {Springer},
  year      = {2020},
  doi       = {10.1007/978-3-030-61244-3_18}
}
@misc{Garijo2020FAIRBP,
  author        = {Garijo, Daniel and Poveda-Villal{\'o}n, Mar{\'i}a},
  title         = {Best Practices for Implementing {FAIR} Vocabularies and Ontologies on the Web},
  year          = {2020},
  eprint        = {2003.13084},
  archivePrefix = {arXiv}
}
@article{Wilkinson2016FAIR,
  author  = {Wilkinson, Mark D. and others},
  title   = {The {FAIR} Guiding Principles for scientific data management and stewardship},
  journal = {Scientific Data},
  volume  = {3},
  pages   = {160018},
  year    = {2016},
  doi     = {10.1038/sdata.2016.18}
}
@inproceedings{Lantow2016OntoMetrics,
  author    = {Lantow, Birger},
  title     = {{OntoMetrics}: Putting Metrics into Use for Ontology Evaluation},
  booktitle = {Proceedings of the 8th International Joint Conference on Knowledge Discovery, Knowledge Engineering and Knowledge Management (IC3K 2016) -- Volume 2: KEOD},
  pages     = {186--191},
  publisher = {SciTePress},
  year      = {2016},
  doi       = {10.5220/0006084601860191}
}
@inproceedings{Vrandecic2006UnitTests,
  author    = {Vrande{\v{c}}i{\'c}, Denny and Gangemi, Aldo},
  title     = {Unit Tests for Ontologies},
  booktitle = {On the Move to Meaningful Internet Systems 2006: OTM 2006 Workshops},
  series    = {LNCS},
  volume    = {4278},
  pages     = {1012--1020},
  publisher = {Springer},
  year      = {2006},
  doi       = {10.1007/11915072_2}
}
@inproceedings{FernandezIzquierdo2019Themis,
  author    = {Fern{\'a}ndez-Izquierdo, Alba and Garc{\'i}a-Castro, Ra{\'u}l},
  title     = {How to Validate Ontologies with {Themis}},
  booktitle = {The Semantic Web: ESWC 2019 Satellite Events},
  series    = {LNCS},
  volume    = {11762},
  publisher = {Springer},
  year      = {2019},
  doi       = {10.1007/978-3-030-32327-1_11}
}
@article{McDaniel2019EvalOnt,
  author  = {McDaniel, Melinda and Storey, Veda C.},
  title   = {Evaluating Domain Ontologies: Clarification, Classification, and Challenges},
  journal = {ACM Computing Surveys},
  volume  = {52},
  number  = {4},
  pages   = {70:1--70:44},
  year    = {2019},
  doi     = {10.1145/3329124}
}
@inproceedings{Garijo2017WIDOCO,
  author    = {Garijo, Daniel},
  title     = {{WIDOCO}: A Wizard for Documenting Ontologies},
  booktitle = {The Semantic Web -- ISWC 2017},
  series    = {LNCS},
  volume    = {10588},
  pages     = {94--102},
  publisher = {Springer},
  year      = {2017},
  doi       = {10.1007/978-3-319-68204-4_9}
}
@inproceedings{Peroni2012LODE,
  author    = {Peroni, Silvio and Shotton, David and Vitali, Fabio},
  title     = {The Live {OWL} Documentation Environment: A Tool for the Automatic Generation of Ontology Documentation},
  booktitle = {Knowledge Engineering and Knowledge Management (EKAW 2012)},
  series    = {LNCS},
  volume    = {7603},
  pages     = {398--412},
  publisher = {Springer},
  year      = {2012},
  doi       = {10.1007/978-3-642-33876-2_35}
}
@book{Krippendorff2018,
  author    = {Krippendorff, Klaus},
  title     = {Content Analysis: An Introduction to Its Methodology},
  edition   = {4},
  publisher = {SAGE},
  address   = {Thousand Oaks, CA},
  year      = {2018},
  isbn      = {978-1-5063-9566-1}
}
@misc{Abercrombie2023Intra,
  author        = {Abercrombie, Gavin and Dinkar, Tanvi and Cercas Curry, Amanda and Rieser, Verena and Hovy, Dirk},
  title         = {Consistency is Key: Disentangling Label Variation in Natural Language Processing with Intra-Annotator Agreement},
  year          = {2023},
  eprint        = {2301.10684},
  archivePrefix = {arXiv}
}
@inproceedings{Calderon2025AltTest,
  author    = {Calderon, Nitay and Reichart, Roi and Dror, Rotem},
  title     = {The Alternative Annotator Test for {LLM}-as-a-Judge: How to Statistically Justify Replacing Human Annotators with {LLMs}},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages     = {16051--16081},
  year      = {2025},
  doi       = {10.18653/v1/2025.acl-long.782}
}
@article{Gilardi2023ChatGPT,
  author  = {Gilardi, Fabrizio and Alizadeh, Meysam and Kubli, Ma{\"e}l},
  title   = {{ChatGPT} outperforms crowd workers for text-annotation tasks},
  journal = {Proceedings of the National Academy of Sciences},
  volume  = {120},
  number  = {30},
  pages   = {e2305016120},
  year    = {2023},
  doi     = {10.1073/pnas.2305016120}
}
```

## 6. Pendientes que deja este informe

* Confirmar la convocatoria específica del Resources Track de ESWC 2027 en cuanto se publique: criterios y si exige HTML o PDF.
* Preguntar a la biblioteca de UNSAAC por ACM Open y por exenciones de APC (JOCCH, SWJ, JOHD).
* Buscar un precedente de pruebas de mutación sobre SHACL antes de reclamar novedad.
* Registrar `w3id.org/laad` (requisito bloqueante de cualquier sede de recursos).
* Sustituir Krippendorff 2004 por la 4.ª ed. (2018) en `G_evaluacion.md` §4, o verificar la 2.ª ed. si se mantiene.

## Fuentes principales consultadas

* ESWC 2027, convocatoria general: https://2027.eswc-conferences.org/calls/contributions-eswc
* ESWC 2026 Resources Track: https://2026.eswc-conferences.org/calls/papers-resource-track
* ISWC, guía de la declaración de disponibilidad de recursos: https://iswc.umbc.edu/authors/resources-availability-statement-guide/
* SWJ For Authors y FAQ: https://semantic-web-journal.net/authors, https://semantic-web-journal.net/faq
* Número especial de SWJ sobre ontologías para patrimonio: https://lists.w3.org/Archives/Public/semantic-web/2024Oct/0001.html
* SWODCH 2026: https://www.loa.istc.cnr.it/?p=1251
* DSH: https://academic.oup.com/dsh/pages/general_instructions
* DHQ FAQ: https://dhq.digitalhumanities.org/about/faq.html
* RHD (UNED): https://revistas.uned.es/index.php/RHD/about/submissions
* JOHD: https://openhumanitiesdata.metajnl.com/about/submissions
* TGDK, convocatoria de recursos: https://lists.w3.org/Archives/Public/semantic-web/2024Mar/0040.html
* Applied Ontology (Sage): https://journals.sagepub.com/author-instructions/APO
* CLEI 2026: https://clei.org/site/wp-content/uploads/2026/03/CFP-CLEI2026_v1_English-1.pdf
* Calderon et al. 2025: https://aclanthology.org/2025.acl-long.782
* Abercrombie et al. 2023: https://arxiv.org/abs/2301.10684
