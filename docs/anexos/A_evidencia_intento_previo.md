# Evidencia sobre el intento previo: Grafo-Conocimiento-Cusco

Auditoría de solo lectura de `/home/foreverlcd/Projects/University/Grafo-Conocimiento-Cusco`. No se modificó nada del proyecto. Todo lo que se generó está en `/tmp/claude-1000/-home-foreverlcd-Projects-University-LAAD/39f471f8-392b-47e0-b3bb-24c96a07370e/scratchpad/diag/`.

Fuente de verdad usada: `/home/foreverlcd/Projects/University/LAAD/corpus/Transcripcion_CC_L14E18.txt` (334 líneas). Es idéntica en contenido a `corpus/Transcripcion_CC_L14E18.txt` del proyecto; solo cambian los finales de línea (CRLF frente a LF). Comprobado con `cmp` después de quitar `\r`. Pasa lo mismo con `corpus_modernizado.txt`. Las referencias «L<n>» de este informe son líneas de esa transcripción.

## 0. Ramas, commits y el «intento 2»

- Ramas: `main`, `linux`, `feature/chat-local-gemini` (HEAD = `32d1e2e`), `origin/main`, `origin/linux`, `origin/stats`, `fork/main` y `fork/feature/chat-local-gemini`. Hay además 45 commits «Agent host session f1fb69f7…» (de `8b244b7` a `4e1f1b9`, del 5 al 7 de octubre de 2026). El árbol de `4e1f1b9` es idéntico al de HEAD (`git diff --stat HEAD 4e1f1b9` sale vacío).
- Los datos `extracciones.jsonl` y `segmentos.jsonl` tienen el mismo blob (`cc7c537…` y `b516eae…`) en todas las ramas. `grafo.json` solo cambia entre `main`/`fork/main` (`5ba5ca5`) y el resto (`c2e4202`). La diferencia se reduce a que `graph_builder` añade `lugar_alegado`; los recuentos son iguales: 259 nodos y 574 aristas.
- **«Intento 2 / Ontología del Expediente CC L14E18»: NO EXISTE** en este repositorio. La lista completa de archivos de todo el historial (`git log --all --name-only`) tiene 32 rutas y ninguna es `.ttl`, `.owl` ni un `.md` de ontología. `git grep -i "Ontolog[ií]a del Expediente|intento 2|\.ttl|\.owl|turtle|rdflib"` sobre todos los commits no da ninguna coincidencia útil: las únicas son rutas al archivo `Transcripcion_CC_L14E18.txt`. No hay stash. Tampoco lo encontré en `~/Projects`, `~/Downloads`, `~/Documents` ni `~/Desktop` (búsqueda de texto «Ontología del Expediente» y de nombres `*L14E18*`). Lo único que apareció es una copia de la transcripción en `~/Downloads/Transcripcion_CC_L14E18.txt`. `LAAD/ontologia/` está vacía.

---

## 1. Roles modelados como tipos o propiedades de la persona

El modelo sí tiene una participación n-aria: `ontology/models.py:102-108` define la clase `Participacion` con `rol: str`. Pero el rol es una **cadena libre sin vocabulario** (`models.py:107`: `rol: str = Field(..., description="Rol específico (ej. 'Denunciante', 'Denunciado', 'Victima', 'Testigo', 'Agresor_Alegado', 'Juez_Subdelegado', 'Escribano')")`). Además, los roles procesales también se guardan **en la persona**:

- `models.py:92-95`: `cargos_mencionados: List[str]`, sin restricción. El LLM metió ahí roles procesales:
  - `extracciones.jsonl` línea 11, `actor_manuel_guancachoque`: `cargos=['Denunciante']`.
  - Línea 5, `actor_manuel_huancachoque`: `['Denunciante']`.
  - Línea 2, `persona_guancachoque`: `['Denunciante Mayor']`.
  - Línea 13, `persona_ysidro_cano`: `['Testigo']`.
  - Línea 12, `persona_mariano_figueroa`: `['Testigo a falta de escribano']`.
- Hay actores cuya identidad *es* un rol, sin nombre propio. En `grafo.json` hay 12 nodos `Actor` de tipo `Persona` así: `persona_declarante_anonimo` («Declarante anónimo»), `actor_fiscal_declarante` («Fiscal Declarante (Anónimo)»), `persona_informante_comisionado` («Comisionado Informante», variante `'Yo'`), `actor_cacique_anonimo`, `persona_subdelegado`, `persona_subdelegado_tinta`, `actor_subdelegado_tinta`, `persona_fiscal_sm`, `actor_fiscal_protector`, `persona_presidente_intendente`, `actor_presidente_intendencia` y `persona_parroco_interino`.
- La «condición» mezcla estatus fiscal, estamento y oficio: `models.py:88-91` define `Literal["IndioOriginario","IndioForastero","IndioTributario","Reservado","EspanolVecino","Mestizo","Noble_Cacique","Eclesiástico","Desconocido"]`. Ejemplo: `actor_fiscal_declarante` tiene `condicion: "Eclesiástico"` y `cargos: ["Fiscal"]`.
- `graph_builder.py:7-13` y `:451-464` tipan el **evento** según su estatus epistémico, con dos etiquetas: `:EventoInstitucional` («Hecho procesal verificado») y `:EventoTestimoniado` («puede ser falso»).
- Los roles se usan sin control. En `grafo.json`, `rol` toma 25 valores distintos: `Agresor_Alegado` 24, `Victima` 23, `Denunciado` 21, `Denunciante` 20, `Juez_Subdelegado` 16, `Testigo` 16, `Escribano` 7, `Fiscal` 5, `Declarante` 3, `ProtectorDeNaturales` 2, `Subdelegado` 2, y uno de cada uno de `Corregidor`, `Soldado`, `Sargento`, `Acusado`, `Líder Rebelde`, `Solicitante`, `Certificante`, `Escribiente`, `Padre_Allegado`, `Madre_Allegada`, `Ausente`, `Agresor_Alegato` (errata), `Notificado` y `Notario`. Los roles mal asignados son absurdos:
  - `institucion_real_hacienda` —PARTICIPA_EN→ `evento_apertura_expediente_1806` con `rol: "Juez_Subdelegado"`.
  - `persona_ruiz_de_castilla` (presidente), `persona_francisco_munoz`, `persona_munoz`, `actor_lucio_gonzalo_del_rio` (fiscal) y `actor_manuel_galeano` (teniente asesor) también aparecen todos con `rol: "Juez_Subdelegado"`.

## 2. Predicados propios de este caso: tipos de arista y frecuencia

En `data/grafo.json` (HEAD; los recuentos son iguales en `main`) hay **8 tipos distintos y 574 aristas**:

| Tipo | Frecuencia |
|---|---|
| MENCIONADO_EN | 193 |
| ROL_EN_EVENTO | 106 |
| OCURRE_EN | 60 |
| DECLARO | 49 |
| DESCRIBE_EVENTO | 49 |
| EXTRAIDO_DE | 49 |
| PARTICIPA_EN | 47 |
| INVOLUCRA_BIEN | 21 |

- Hay tipos declarados que no aparecen en los datos. `graph_builder.py:15-26` documenta además `CONTRADICE`, `RATIFICA`, `ALEGADO_EN` y `MIEMBRO_DE`, y `graph_builder.py:164` crea `DOCUMENTADO_EN` (solo en Neo4j). En el JSON hay **0** `CONTRADICE` y **0** `RATIFICA`: las 49 afirmaciones tienen `contradice_afirmacion_ids=[]` y `ratifica_afirmacion_ids=[]`. Lo confirma `reporte_calidad.md:105-106`. `ALEGADO_EN` y `MIEMBRO_DE` no se generan nunca, y `extracciones_a_grafo_json` (`graph_builder.py:404-482`) no emite `DOCUMENTADO_EN`.
- Todos los predicados son nombres en mayúsculas inventados, sin correspondencia con propiedades de CIDOC, PROV ni RiC (por ejemplo `DECLARO` en lugar de `prov:wasAttributedTo`, y `ROL_EN_EVENTO {rol}` en lugar de `crm:P11_had_participant` + `P14.1_in_the_role_of`). Además, `tipo_evento` es texto libre (`models.py:117`). En los datos aparecen tipos a medida como `ServicioMilitar`, `Ratificacion_Escrito`, `Comparecencia_Juramento`, `Solicitud_Certificacion`, `Certificacion_Testigo`, `Compraventa` y `Administrativo_Politico` (este último es una categoría usada como tipo).

## 3. Clases mezcladas con individuos

- En `ontology/standards.py:111-122`, `CondicionTributaria` y `CargoVirreinal` tienen `"padre": "skos:Concept"` y una lista `"valores": [...]` de cadenas (`"IndioOriginario"`, `"Subdelegado"`…). Esas cadenas nunca llegan a ser `skos:Concept` con IRI: son literales de un `Literal[...]` de Pydantic (`models.py:88-91`) o texto libre en `cargos_mencionados`.
- **«Subdelegado» aparece a la vez como valor de vocabulario, como rol de participación y como individuo Persona:**
  - Como valor: `standards.py:121`.
  - Como rol: `extracciones.jsonl` línea 11, `('actor_pedro_de_la_mara','Subdelegado')`; línea 20, `('persona_subdelegado_tinta','Subdelegado')`.
  - Como cargo: `persona_pedro_de_la_mata.cargos=['Subdelegado']`.
  - Como actor-persona: `persona_subdelegado_tinta` (`nombre: "Subdelegado del Partido de Tinta"`, `tipo: "Persona"`), además de `persona_subdelegado` y `actor_subdelegado_tinta`.
- Pasa lo mismo con «Fiscal» (`persona_fiscal_sm`, `actor_fiscal_protector`, `actor_fiscal_declarante`, rol `Fiscal` y cargo `Fiscal`) y con «Presidente» (`persona_presidente_intendente`, `actor_presidente_intendencia`).
- Los ayllus son a la vez agente y lugar. Como `Actor` de tipo `Ayllu_Comunidad`: `ayllu_tinta`, `ayllu_ucho` y `ayllu_chuquitapa`. Como `Lugar` de tipo `Ayllu_Territorio`: `lugar_ayllu_tinta` y `lugar_ayllu_uchu`. Son nodos distintos y no hay ninguna arista que los una.
- Un concepto colectivo se trata como individuo: `actor_indios_comunidad` («Indios sublevados») es `Ayllu_Comunidad` con `condicion: IndioOriginario`, y `colectivo_indios_tinta` tiene `condicion: IndioTributario`.
- Un documento o un derecho se trata como bien: `objeto_objeto_certificacion_f2`, `objeto_objeto_documentos_falsos` y `objeto_objeto_robo_cacique` (un «robo» tipado como `Dinero_Tributo`) son `ObjetoBien`.

## 4. Estados de verdad que dan por hecho la resolución de una autoridad

La definición del prompt ya convierte la autoridad en verdad. `pipeline/extractor.py:73-77`:
> «Confirmado_Oficial: Una resolución posterior lo confirma como verdadero. / Desmentido_Falso: Una resolución lo declara falso o fabricado.»

Las 49 afirmaciones extraídas se reparten así: 43 `Alegato_No_Comprobado`, **4 `Confirmado_Oficial`**, **1 `Desmentido_Falso`** y 1 `En_Disputa`. En `grafo.json`, después de las colisiones del punto 13, quedan 28, 4, 1 y 1. Los 5 casos:

| Id (línea de extracciones.jsonl) | Declarante | Estado | Qué se toma como verdad |
|---|---|---|---|
| `afirmacion_01` (línea 20, folio 33) | `persona_fiscal_sm` | **Desmentido_Falso** | La opinión del fiscal: «resultando de este ser menos conforme a la verdad las quejas dadas por Manuel Guancoichoque…» (L328). Es un dictamen, no una prueba. |
| `afirmacion_01_falsedad_documentos` (línea 18) | `persona_informante_comisionado` | **Confirmado_Oficial** | El *informe* del subdelegado Pedro de la Mata (L306-320) según el cual los documentos de Huancachoque «fueron hechos por el mismo Guancachoque». Es parte interesada, no una resolución. |
| `afirmacion_exp18_f10_01` (línea 12) | `persona_pedro_de_la_mata` | **Confirmado_Oficial** | Una orden: «haga de Saber a Chuquitapa se retire… quatro leguas». Una orden no es una afirmación verificable. |
| `afirmacion_notificacion_1806` (línea 21) | `actor_agustin_chacon` | **Confirmado_Oficial** | La diligencia del escribano. |
| `afirmacion_certificacion_ugarte` (línea 21) | `actor_matias_ugarte` | **Confirmado_Oficial** | La certificación republicana de una «venta», ajena al expediente de 1806 (ver el punto 8). |

- El test lo consagra. `tests/test_ontology.py:125-154`: «Verifica que la resolución del Subdelegado Pedro de la Mata pueda enlazar y contradecir directamente las afirmaciones iniciales de agresión», con `estado_epistemologico="Confirmado_Oficial"` y `contradice_afirmacion_ids=["afirmacion_cano_folio_01"]`. Además usa `folio=30`, un folio inventado.
- La evaluación del chat también lo exige. En `tests/test_chat_evaluation.py:33-39` (caso `tinta-1806`) y `:93-100` (caso `resolucion-quejas`), `required_state="Desmentido_Falso"` y la respuesta tiene que contener «desment», «no eran» o «falso». `OBSERVACIONES_CHAT_LOCAL.md:95-97`: «las quejas aparecen acompañadas por resoluciones clasificadas como `Desmentido_Falso`; la respuesta debe conservar esa diferencia».

## 5. PROV-O: atribución histórica en lugar de procedencia del dato

- `ontology/standards.py:82-85` dice: `"wasAttributedTo": {... "descripcion": "Actor histórico o testigo que emitió la declaración."}`. `models.py:138` dice: `declarante_id: str = Field(..., description="prov:wasAttributedTo: ID del actor que formula la declaración")`. Es decir, `prov:wasAttributedTo` se reserva para **quién lo dijo en 1806**, no para el agente que generó el dato.
- `wasDerivedFrom` se aplica a la cita (`models.py:150`) y a la arista `EXTRAIDO_DE` hacia un fragmento cuyo folio es inventado (ver el punto 9).
- **No se registra ni modelo, ni prompt, ni versión, ni fecha de extracción.** Las claves de cada registro de `extracciones.jsonl` son solo `unidad_archivistica`, `actores`, `lugares`, `objetos`, `afirmaciones` y `eventos_institucionales_probados`. `unidad_archivistica` tiene `fondo, serie, legajo, expediente, folio, fragmento_id, texto_original, texto_modernizado`. No hay `prov:Activity`, ni agente de software, ni hash de la transcripción, ni marca de tiempo.
- El modelo solo figura como constante en el código (`extractor.py:35`, `MODELO_ID = "gemini-3.6-flash"`, igual en todos los commits) y se imprime en consola (`:187`).
- El extractor reutiliza extracciones antiguas por `fragmento_id` (`extractor.py:196-225`), así que el JSONL puede mezclar ejecuciones distintas sin dejar rastro.
- `confianza_extraccion` vale 1.0 en 47 de las 49 afirmaciones y 0.95 en 2. Es una cifra que inventa el propio LLM, no un dato de validación.
- `texto_original` lo **re-emite el LLM** y no se copia por código (`extractor.py:101`, «texto_original: (el texto completo del segmento, tal cual)»). En 10 de 21 registros no coincide con el segmento. En el segmento 20 mide 2111 caracteres frente a 2239, y el LLM añadió un `texto_modernizado` que nadie pidió.

## 6. ¿Se usan de verdad las cinco ontologías? ¿Hay RDF?

- **Nunca se emite RDF.** `requirements.txt` solo contiene pydantic, pytest, rapidfuzz, google-genai, google-generativeai y neo4j; no hay `rdflib`. Las salidas son `grafo.json` (`graph_builder.py:485-490`) y Cypher para Neo4j.
- `NAMESPACES` y los `*_MAPPING` (`standards.py:15-140`) **no los importa ningún módulo del pipeline**. Solo se reexportan en `ontology/__init__.py` y se comprueba que existan sus claves en `tests/test_ontology.py:28-33` (`assert "RecordSet" in RICO_MAPPING`, etc.).
- Recuento en `grafo.json` y `extracciones.jsonl`: `rico:` 0, `crm:` 0, `prov:` 0, `skos:` 0, `ohac:` 0, `http` 0, `E21` 0, `wasAttributedTo` 0. **Cero nodos y cero aristas llevan IRI.** Los identificadores son *slugs* locales (`persona_manuel_huancachoque`, `afirmacion_01`).
- Las ontologías aparecen solo en docstrings y comentarios (`models.py:1-10`, «Equivalente a crm:E21_Person…») y en el README (`README.md:26-33`, `:72`). El espacio de nombres `ohac` es un dominio inventado: `https://archivo-cusco.pe/ontology/ohac#` (`standards.py:20`).
- SKOS solo existe como dos listas: `nombre_principal` y `variantes_ortograficas`. No hay `skos:ConceptScheme`, ni `exactMatch`, ni conceptos.

## 7. Fechas imposibles o de secuencia imposible

Los dos primeros casos están en la propia transcripción. El fallo del pipeline es que **los copia como hechos, sin marcarlos**.

| Nodo (grafo.json) | Fecha | Problema |
|---|---|---|
| `evento_ratificacion_juramentada` (`grafo.json:1132`) y `evento_declaracion_guancachoque` (línea 9) | «13 de Agosto de 1806» | L76: «En la ciudad del Cuzco en trece días del mees de Agosto… En cumplimiento de lo mando en el Decreto marginal que antecede». El decreto que cumple está fechado «Cusco y Agosto 21 de 1806» (L70) y se notificó el 23 (L74). La ratificación no puede ser anterior. |
| `evento_emision_dictamen_1806` (`grafo.json:1959`) | «1806-11-26» | Es el informe del cura, el fragmento de L284-290 que termina en «Firma Noviembre 26 de 1806» (L290). Pero el informe de Pedro de la Mata del **8 de noviembre** (L315-320) ya lo cita: «Por el informe que le pedí al cura interino… Doctor Don Agustin Valdes». Además, el nodo se tipifica `ResolucionJudicial` de un «Fiscal Declarante». |
| `evento_notificacion_auto_1810` (`grafo.json:2330`), EventoInstitucional | «23 de Diciembre de 1810» | Sale de L334 («veinte y tres de Diciembre de mil ochocientos 10 años»). Una notificación de 1810 dentro de un expediente cerrado en noviembre de 1806, sin aviso. |
| `afirmacion_certificacion_ugarte` / `evento_certificacion_notarial` | sin fecha, folio 34 | Texto republicano («El ciudadano Matias Ugarte», L335) que se data implícitamente en 1806. |
| `evento_auto_subdelegado_sicuani` (17 de septiembre de 1806) | — | El texto en el que se basa (L125-126) dice que la denuncia «es la misma que hizo en once de Febrero del año pasado de **1809**». 1809 queda dentro de `texto_original` (`extracciones.jsonl` línea 11) y no se señala. No llega a `grafo.json`. |
| `evento_emision_certificacion_cazorla` | — | En la línea 3 tenía «5 de agosto de 1806», pero se pisa con la línea 5 (sin fecha). Ver el punto 13. |

## 8. Personas fusionadas o divididas sin prueba

Las variantes de `grafo.json` son las del **último** fragmento que menciona el id, porque `graph_builder.py:409-410` sobrescribe el diccionario.

**Fusiones sin prueba:**
- **Huancachoque con su presunto padre Ortiz.** `actor_manuel_huancachoque` (`grafo.json:295`) tiene `variantes: ['Manuel Guancachoque', 'Maldonado Ortiz a las Guamcachoque', 'Ortis o Guancachoque', 'Ortiz']`. Fuente, L285: «Manuel Guancachoque es hijo Espurio de Antolin Ortiz». Antolín Ortiz existe como nodo aparte (`actor_antolin_ortiz`).
- **Martín y Mariano Cazorla.** `persona_mariano_casorla` (`grafo.json:1461`) tiene `variantes: ['Don Mariano Casorla', 'Martin casorla']` y `cargos: ['Gobernador']`. Fuente: L219 dice «Parecio ante mi el Gobernador Señor Don Mariano Casorla» y L225 dice «De folio 4 su firma Martin casorla». A la vez existe `actor_martin_cazorla` (línea 5): está fusionado y dividido al mismo tiempo.
- **Pedro de la Mata y Pedro de la Mara.** `persona_pedro_de_la_mata` en la línea 12 tiene `['Pedro de la Mara','Pedro de la Mata']` (L153 «Pedro de la Mara», L164 «D.Pedro de la Mata»). Es probable, pero no queda rastro de la evidencia. Al mismo tiempo sigue **dividido** en `actor_pedro_de_la_mara` (línea 11), `persona_pedro_mata` (líneas 13 y 16) y `persona_informante_comisionado` (línea 18, el informe que L320 firma «Pedro de la Mata»).
- **Ruiz de Castilla con un título que no aparece.** `persona_ruiz_de_castilla` (`grafo.json:1156`) tiene `nombre: "Marqués de Selva Alegre / Ruiz de Castilla"`. «Selva» **no aparece** en la transcripción; solo «Firma Castilla» (L93) y «(CAV) Ruiz de Castilla» (L111).
- **Chuquitapa con «Chuquitaza».** `actor_andres_chuquitaza` (línea 15) tiene `variantes: ['andres chuquitaza','chuquitapa']` y un cargo que es una acusación: `cargos: ['Coronel y comisionado de Túpac Amaru']` (L270).
- `actor_manuel_huancachoque` (línea 3) incorpora `'Manuel Guamanchoque'` (L23) y le pone `cargos: ['Soldado']`.

**Divisiones (la misma persona en varios nodos):**
- Manuel Huancachoque: 6 ids (`actor_manuel_huancachoque`, `actor_manuel_guancachoque`, `persona_manuel_huancachoque`, `persona_manuel_guancachoque`, `persona_guancachoque` y `persona_manuel_mancachoque`). El propio informe de calidad lo demuestra: `reporte_calidad.md:120-128` pone «Manuel Huancachoque» tres veces y «Guancachoque» o «Manuel Guancachoque» dos veces más en el top 10. Aun así, `reporte_calidad.md:79` afirma una «unificación de variantes como *Huancachoque*, *Guancachoque*, *Mancachoque* en una sola entidad».
- Andrés Chuquitapa: 6 ids (`persona_andres_chuquitapa`, `actor_andres_chuquitapa`, `actor_andres_choquitapa`, `actor_andres_chukitapa`, `actor_andres_chuquitaza` y `persona_chuquitapa`).
- Túpac Amaru: 5 ids (`persona_tupa_amaro`, `persona_jose_gabriel_tupac_amaru`, `persona_tupac_amaru_ii`, `actor_tupac_amaru` y `actor_joseph_condorcanqui`).
- Corregidor Reparas: 3 ids (`persona_antonio_reparas`, `persona_juan_antonio_reparas` y `actor_juan_antonio_repuras`).
- Escribano Chacón: 3 ids (`actor_chacon`, `persona_antonio_chacon` y `actor_agustin_chacon`).
- Isidro Cano: 2 (`persona_isidro_cano`, `persona_ysidro_cano`). Santiago Cazorla: 2. Fernando Orue: 2. Miguel Orey: 2. Juan de Dios Cazorla: 2.
- Luis o Lucio Gómez o Gonzalo del Río: 3 ids **no fusionados** (`actor_luis_gomez_del_rio`, línea 9, L74; `persona_luis_gonzalo_del_rio`, línea 10, L98, «su único Fiscal»; `actor_lucio_gonzalo_del_rio`, línea 21, L333). No hay ninguna decisión registrada de si es la misma persona.
- Presidentes: Ruiz de Castilla y Muñoz **no se fusionan entre sí**. Pero «Don Francisco Muñoz y Señor Clemente» (L320) se parte en `persona_francisco_munoz` y **`persona_clemente`**, una persona inventada a partir del apellido compuesto. Además existen `persona_munoz`, `persona_presidente_intendente` y `actor_presidente_intendencia` sin resolver.
- Antonio y Agustín Valdés: **no se fusionan** (`persona_antonio_valdes` en la línea 16, L277, tío del interino; `persona_agustin_valdes` en la línea 19, L315). Pero el cura interino del pedimento (`persona_parroco_interino`, línea 16) no se vincula con Agustín Valdés, y su informe (línea 17) se atribuye a `actor_fiscal_declarante`.

**Juan Quiñones y Juan Cazorla:** no se fusionan. Sin embargo, L301 dice que la certificación firmada por Juan Cazorla se extendió «a nombre del teniente Alguacil Don Juan Quiñones, que no hay tal hombre en el pueblo de Tinta». Aun así, Quiñones figura como persona real en dos nodos (`actor_juan_quinones` y `persona_juan_quinones`, `Teniente Alguacil`, `EspanolVecino`). En la línea 3 es **declarante** de `afirmacion_agresion_huancachoque`, `afirmacion_tumulto_carcel` y `afirmacion_alzamiento_orey`, y en el grafo es `Testigo` de `evento_motin_carcel_tinta`. Ninguna arista dice que el autor real es Cazorla.

**Notario Matías Ugarte y el texto republicano final: SÍ se integró** en el expediente de 1806 (fragmento `exp_ccc_14_18_f34_seg21`). Incluye `actor_matias_ugarte` («Notario Público»), `afirmacion_certificacion_ugarte` (**Confirmado_Oficial**), `evento_certificacion_notarial` con `tipo: "Compraventa"`, `lugar_urubamba` y `objeto_objeto_venta_otorgada` («Venta otorgada por la señora…», `Inmueble_Tierra`).

## 9. Cómo se asigna el folio: inventado o aproximado

Algoritmo (`pipeline/segmenter.py:116-150`):
- Parte el texto por `\n\s*#\s*\n` y descarta los bloques de menos de 80 caracteres.
- Busca el **primer** `\bfolio\s+(\d+)\b` del bloque (`:60-65`) **sin distinguir mayúsculas y aunque sea una referencia interna**.
- Si no lo encuentra, sube un contador (`folio_corriente += 1`) a cada bloque: `:119` «Folio estimado incremental cuando no hay marcador explícito».

Supuesto implícito: «'#' actúa como separador físico de folios» (`:7`). Ese valor se pasa al LLM como «Folio aproximado» (`extractor.py:84`) y se le ordena copiarlo (`:99`).

| Seg. | Líneas aprox. | Folio asignado | Qué dice la transcripción |
|---|---|---|---|
| 1-9 | L1-84 | 1, 2, 3 … 9 | **No hay ningún marcador.** Es solo el contador de bloques «#». |
| 10 | L91-112 | **10** | «En folio 10 remito a vuestra Merced un expediente» (L108): una referencia al expediente remitido, no un número de página. |
| 11 | L125-144 | **10** | «con el Expediente en folio 10» (L125). Otra vez una referencia, no un marcador. |
| 12 | L151-192 | 10 | Se repite sin marcador porque, al haber detectado uno, el contador no sube. |
| 13 | L197-257 | **4** (el folio retrocede) | Contiene «De folio 4 su firma Martin casorla» (L225), una referencia a la certificación del f. 4, y **«Folio 20» (L230), el marcador real, que se ignora** porque gana la primera coincidencia. |
| 14-16 | L268-277 | 4, 5, 6 | Contador a partir del 4 falso. Debería ser el f. 20 o posterior. |
| 17 | L284-290 | 28 | «folio 28» aparece en L289, a mitad de bloque; el texto de L284-288 es anterior. |
| 18 | L301-311 | 28 | Sin marcador. |
| 19 | L314-320 | 29 | Contador. |
| 20 | L323-329 | 33 | «Folio 33» (L323), correcto. |
| 21 | L331-335 | 34 | «[Folio 34 ]» (L331), correcto. Pero incluye el texto republicano de Ugarte. |

Solo 2 de los 21 folios (segmentos 20 y 21) salen de un marcador explícito correcto. En los fragmentos `exp_ccc_14_18_f04_seg13` y `f04_seg14`, el folio va hacia atrás (de 10 a 4). Las afirmaciones del segmento 13 llevan `folio=20` (lo decidió el LLM), mientras que su `unidad_archivistica.folio` es 4. `README.md:19` dice «19 folios», en contradicción con «[Folio 34 ]».

El `tipo_acto_procesal` también es una heurística de subcadena que falla (`segmenter.py:20-39` y `:84-90`):
- Al segmento 4, una certificación del cabo Orue, lo clasifica `Auto_Decreto_Judicial` porque contiene «he **visto** con mis ojos».
- Al segmento 17, el informe del cura, lo clasifica `Dictamen_Fiscal` porque contiene «el señor Agustin **Fiscal** Don Althamacio Zotelo». Esa etiqueta pasa al prompt (`extractor.py:85`) y el LLM crea `actor_fiscal_declarante` («Fiscal Declarante (Anónimo)», condición `Eclesiástico`).
- Al segmento 18 lo clasifica `Auto_Decreto_Judicial` por «lo que **visto** por los alcaldes».

## 10. ¿Las citas son subcadenas exactas?

Script: `/tmp/claude-1000/-home-foreverlcd-Projects-University-LAAD/39f471f8-392b-47e0-b3bb-24c96a07370e/scratchpad/diag/medir_citas.py`, ejecutado con `python3 -I`. Salida: `/tmp/claude-1000/-home-foreverlcd-Projects-University-LAAD/39f471f8-392b-47e0-b3bb-24c96a07370e/scratchpad/diag/medir_citas_salida.txt`.

Citas evaluadas: 49 (todas las `cita_textual_evidencia`).

| Criterio | Paleográfica | Modernizado |
|---|---|---|
| Subcadena exacta (byte a byte) | **32 (65,3 %)** | **1 (2,0 %)** |
| Igual tras colapsar espacios | 43 (87,8 %) | 1 (2,0 %) |
| Igual tras colapsar espacios, minúsculas y sin tildes | 43 (87,8 %) | 4 (8,2 %) |

- **En ninguno de los dos textos (ni con normalización): 6 (12,2 %).**
- Las citas vienen de la versión paleográfica. **El 34,7 % no es literal**, aunque la regla del prompt diga «Debe ser una cita literal» (`extractor.py:51-52`).

Causas de las 6 que no aparecen:
- Elisiones con «...» que pegan pasajes separados: línea 7, `afirmacion_01_encarcelamiento_agresion`; línea 15, `afirmacion_orue_disputa_firma`.
- Palabras partidas por un salto de línea («Guancacho/que», «parien/tes») que el LLM recompone: línea 13, `afirmacion_01` y `afirmacion_02`.
- Expansión de abreviaturas («se q todos» pasa a «que todos»): línea 14, `afirmacion_01`.
- Un final reescrito: línea 12, `afirmacion_exp18_f10_03`.

El informe propio del proyecto da el mismo 65,3 % de exactas, pero lo maquilla. Con `fuzz.partial_ratio >= 85` cuenta un 98 % de «anclaje alto» (`stats/metrics.py:265-279`) y 0 % de riesgo de alucinación (`reporte_calidad.md:60-65`). Así llega a un «KGCQ 94,1 / 100, A+».

## 11. Prompts del LLM

**Extractor** (`pipeline/extractor.py:35`): modelo `gemini-3.6-flash`, `temperature=0.1` y `response_mime_type="application/json"` (`:122-130`). El JSON se valida con Pydantic `ExtraccionFolio`, con hasta 4 reintentos.
- `SYSTEM_PROMPT` (`:41-78`):
  - «Eres un experto historiador… período virreinal tardío, 1780-1824».
  - Regla 1: «NUNCA registres acusaciones… como hechos verificados… encapsularse en un objeto "AfirmacionHistorica"».
  - Regla 2: «La cita_textual_evidencia es OBLIGATORIA. Debe ser una cita literal… de al menos 10 caracteres».
  - Regla 3: «Los nombres de personas tienen ortografía muy inestable en el siglo XIX colonial. Registra TODAS las variantes». Ojo: dice «siglo XIX», no XVIII.
  - Después da listas cerradas de condiciones y cargos, de tipos de declaración y de estados epistemológicos (las definiciones de autoridad citadas en el punto 4).
- `construir_prompt_usuario` (`:81-104`): «Analiza el siguiente fragmento… Folio aproximado {folio_estimado}. Tipo de acto identificado: {tipo_acto_procesal}». Luego el texto y «Devuelve UN ÚNICO objeto JSON que valide contra este esquema: {schema_json}». Obliga a copiar `folio`, `fragmento_id` y `texto_original`.
- **¿Pide producir CIDOC directamente?** No pide RDF ni clases CIDOC. Le pide **llenar directamente el esquema Pydantic «OHAC»**, cuyas descripciones de campo llevan las equivalencias (`"crm:P11_had_participant: …"`, `"prov:wasAttributedTo: …"`, `"skos:altLabel: …"`, en `models.py:79-83`, `:122-124`, `:138` y `:150`). Por tanto, en un solo paso el LLM decide la identidad canónica (`id_canonico`), el tipo de declaración, el **estado de verdad**, los roles y las fechas, sin ninguna capa de normalización ni revisión humana. Además se le dan, como si fueran datos, un folio y un tipo de acto heurísticos y erróneos.

**Chat** (`chat/local_chat.py`): modelo `gemini-3.1-flash-lite`, con respaldo `gemini-flash-lite-latest` (`:196-197` y `:301-304`).
- `PLANNER_SYSTEM` (`:44-54`) clasifica en `actor|acusado|afirmacion|evento|lugar|general` y devuelve un `termino`.
- `ANSWER_SYSTEM` (`:56-63`): «Responde en español usando solo la evidencia entregada… Distingue siempre Alegato_No_Comprobado, Confirmado_Oficial, Desmentido_Falso y En_Disputa… Menciona folio, expediente y cita literal».
- La recuperación usa Cypher fijo por intención (`:76-180`), con `CONTAINS` sobre nombre, cita o tipo y un límite de 20 resultados.

## 12. Preguntas que fallaron

`tests/test_chat_evaluation.py:31-109` define 10 casos: `tinta-1806`, `principal-acusado`, `tributarios-ocultos`, `manuel-huancachoque`, `ataque-orey`, `denunciante`, `ayllu-tinta`, `isidro-cano`, `resolucion-quejas` y `cuarenta-cuatro`.

- **Recuperación (solo Neo4j): «10 passed»** (`OBSERVACIONES_CHAT_LOCAL.md:37-41`).
- **Respuesta con el LLM real: «4 casos aprobados / 6 casos fallidos»** (`:65-70`). **El documento no nombra los 6 casos.** Solo da categorías (`:72-80`): «Clasificación de preguntas sobre tributarios», «Preguntas sobre el Ayllu Tinta», «Resoluciones oficiales», «Cantidades como los 44 tributarios», «Actores recuperados como menciones sin suficiente contexto narrativo» y «Respuestas que omitieron nombres o hechos centrales». No hay log ni salida guardada en ningún commit.

Correspondencia probable, deducida del código:
- `cuarenta-cuatro`: «44» solo existe en la descripción de `objeto_obj_tributarios_ocultados` («Cuarenta y cuatro tributarios en el Ayllu Tinta y siete en el Ayllu Uchu», que viene de L55). Ninguna consulta recupera `ObjetoBien` ni su descripción. La intención `afirmacion` (`local_chat.py:118-135`) busca en `cita` y ninguna cita contiene «cuarenta y cuatro».
- `ayllu-tinta`: la intención `lugar` (`:162-171`) devuelve solo `nombre` del lugar, sin cita ni estado. Además, el Ayllu como `Actor` (`ayllu_tinta`) y como `Lugar` (`lugar_ayllu_tinta`) están desconectados (punto 3).
- `tributarios-ocultos`: depende de que el planificador devuelva `afirmacion` y `tributarios`. Si elige otra intención, falla («Clasificación de preguntas sobre tributarios»).
- `resolucion-quejas`: la evidencia `ResolucionOficial` mezcla cinco «resoluciones», entre ellas la orden de retiro, la notificación y la venta de Ugarte, por la colisión del punto 13.
- Casos de actor (`manuel-huancachoque`, `denunciante`, `ataque-orey`): la intención `actor` devuelve `contexto = a.nombre` y, para las menciones, `cita = null` (`:77-94`). Eso coincide con «menciones sin suficiente contexto narrativo».

`reporte_calidad.md` y `estadisticas_calidad.json` no contienen preguntas: son métricas KGCQ.

## 13. Otros errores graves

1. **Colisión de ids de afirmación: el grafo atribuye frases a quien no las dijo.** `graph_builder.py:409-410` sobrescribe los nodos por id y `:466` añade un `DECLARO` por cada extracción. Hay 49 afirmaciones extraídas, pero solo 34 nodos `AfirmacionHistorica` y 49 aristas `DECLARO`. En Neo4j pasa lo mismo, porque `MERGE … SET` también se queda con el último valor (`graph_builder.py:258-266`). Casos:
   - `afirmacion_01` (`grafo.json:84`) conserva el contenido del **fiscal**: «Desmentido_Falso», folio 33, «resultando de este ser menos conforme a la verdad las quejas…». Sin embargo, tiene **8 declarantes**: `persona_manuel_mancachoque`, `persona_isidro_cano`, `actor_manuel_guancachoque`, `persona_mariano_casorla`, `persona_santiago_casorla`, `persona_declarante_anonimo`, `persona_pedro_de_la_mata` y `persona_fiscal_sm`. Y tiene 8 fuentes `EXTRAIDO_DE`. En el grafo, Manuel Huancachoque «declaró» que sus propias quejas son falsas.
   - `afirmacion_02`: 5 declarantes. `afirmacion_03`: 3. `afirmacion_04`: 2.
   - `afirmacion_exp18_f10_01` (`grafo.json:1327`): la denuncia de Guancachoque (línea 11) queda sustituida por la orden de Pedro de la Mata con `Confirmado_Oficial` (línea 12), y conserva los dos declarantes.
   - También colisionan eventos. `evento_emision_certificacion_cazorla` une la certificación de Santiago (línea 3, 5 de agosto) con la de Martín Cazorla (línea 5). `evento_ocultacion_tributarios_tinta` aparece en las líneas 10 y 11.
   - Las métricas no lo detectan: «Integridad Referencial 574 / 574» y «Conformidad Dominio / Rango 100 %» (`reporte_calidad.md:31-32`).
2. **Atribución equivocada del informe del cura.** Segmento 17 (L284-290): los insultos («hijo Espurio de Antolin Ortiz, Sanbo… su Madre Agustina Falcon India Ordinaria y pleveya») se atribuyen a `actor_fiscal_declarante` como `Acusacion`, y el evento se tipifica `ResolucionJudicial` del «Fiscal». A `actor_atanasio_sotelo` («Don Althamacio Zotelo») se le pone `cargos: ['Fiscal']` porque L288 dice «el señor Agustin Fiscal Don Althamacio Zotelo».
3. **Entidades inventadas o fuera de lugar:**
   - El título «Marqués de Selva Alegre» (no está en la fuente).
   - `persona_clemente`, que sale del apellido de Muñoz.
   - `persona_informante_comisionado` («Yo»), que en realidad es Pedro de la Mata.
   - Una `Compraventa` en Urubamba.
   - `lugar_america_meridional`, sacado de una frase retórica (L289).
   - `lugar_pueblo_unnamed`, `lugar_doctrina_unspecified` y `lugar_doctrina_pueblo`.
   - Dos cárceles distintas (`lugar_carcel` y `lugar_carcel_tinta`) más `lugar_real_carcel`.
   - Tres nodos para los 51 tributarios (`objeto_objeto_51_tributarios`, `objeto_objeto_51_indios_tributarios` y `objeto_obj_indios_ocultos_51`).
4. **El ejemplo del README no está en la fuente.** `README.md:141-150` ilustra el modelo con «Cita: 'mandó a medianoche a matarle...'» e «Intento_Homicidio» atribuidos a Isidro Cano. «matarle» no aparece en la transcripción.
5. **Métricas que no miden lo que dicen.** El «Factor de Consolidación 2.36x» (`reporte_calidad.md:79`) es `(actores + variantes) / actores` (`stats/metrics.py:345-346`), no un índice de fusión. La «Tasa de Reificación 100 %» y la «Conectividad 100 %» se cumplen por construcción.
6. No se encontraron ciclos (no hay aristas `CONTRADICE` ni `RATIFICA` que puedan formarlos), ni aristas duplicadas, ni aristas colgantes en `grafo.json`.
