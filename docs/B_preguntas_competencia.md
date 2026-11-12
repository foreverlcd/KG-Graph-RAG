# B · Preguntas de competencia (PC)

> Redactadas **antes** de modelar (rama `docs/preguntas-competencia`). El modelo de `docs/C_modelo.md` es el mínimo que
> las responde; la matriz de trazabilidad PC → término → consulta → prueba está en `docs/C_trazabilidad.md`.
>
> **Respuestas de referencia.** Las respuestas de abajo son **provisionales del modelador**, extraídas de la
> transcripción con su tramo. No sustituyen a las que debe fijar un historiador **antes** de construir el grafo
> (criterio de aceptación 3). Para eso está la plantilla `docs/B_respuestas_referencia.csv`: el historiador escribe su
> respuesta sin ver la del modelador, y después se comparan.

## Método

Las preguntas siguen la práctica de Grüninger & Fox (1995): preguntas en lenguaje natural que la ontología debe poder
responder, convertidas después en consultas SPARQL que actúan como pruebas de aceptación. Cada PC se clasifica por:

* **Capa** que la responde: 1 documento · 2 menciones · 3 afirmaciones · 4 reconstrucción · P procedencia del dato.
* **Forma de respuesta**: `D` dato documental · `A` lista de afirmaciones atribuidas · `DISPUTA` («X lo afirma, Y lo niega») · `NC` («el expediente no lo dice») · `R` reconstrucción con autor.
* **Alcance**: `E` este expediente · `S` la serie (Tomo I, a nivel de ficha de catálogo).

Seis preguntas tienen como respuesta correcta `DISPUTA` o `NC` (PC09–PC14); la solicitud pedía al menos cinco.

## Las 20 preguntas

| PC | Pregunta (como la formularía un historiador del Cusco colonial) | Capa | Forma | Alc. |
|---|---|---|---|---|
| PC01 | ¿Qué piezas forman el expediente, en qué orden físico, de qué tipo es cada actuación y qué fecha lleva? | 1+3 | D | E |
| PC02 | La declaración del 23 de septiembre remite a «la certificación De folio 4». ¿Qué pieza es esa, dónde está en la transcripción y quién la firma? | 1+2 | D | E |
| PC03 | ¿Qué otros expedientes del Tomo I mencionan a Andrés Chuquitapa, a Manuel Guancachoque o al pueblo de Tinta, según el catálogo? | 1+3 | A | S |
| PC04 | En la sección Causas Criminales, ¿en qué expedientes de 1805–1807 aparece como demandado un cacique, recaudador o alcalde de indios, según la ficha del catálogo? | 1+3 | A | S |
| PC05 | ¿Con qué grafías aparece el denunciante, en qué tramos y dentro de qué pieza (escrita por quién)? | 2 | D | E |
| PC06 | ¿Qué menciones de personas no se pueden identificar con seguridad con una persona, y por qué? | 2+4 | R | E |
| PC07 | ¿Qué lugares se mencionan (pueblos, ayllus, edificios) y con qué identificador de HGIS de las Indias? | 2+4 | D | E |
| PC08 | Para cada testigo de agosto: ¿qué afirmó en su certificación y qué en su declaración jurada de septiembre sobre los mismos hechos? | 3 | A | E |
| PC09 | ¿Fue Andrés Chuquitapa coronel de Túpac Amaru en la rebelión? | 3 | **DISPUTA** | E |
| PC10 | ¿Quién redactó las certificaciones de agosto? | 3 | **DISPUTA** | E |
| PC11 | ¿Cuánto tiempo estuvo preso Huancachoque? | 3 | **DISPUTA** | E |
| PC12 | ¿Se sacó finalmente a Huancachoque de la matrícula de tributarios? | 3 | **NC** | E |
| PC13 | ¿Qué castigo concreto se ejecutó contra Huancachoque tras el auto del 26 de noviembre de 1806? | 3 | **NC** | E |
| PC14 | ¿A qué hora fue el alboroto ante la cárcel y cuántos indios participaron? | 3 | **DISPUTA** | E |
| PC15 | ¿Qué autoridades actuaron, en qué tipo de actuación, en qué fecha, quién escribió y quién firmó cada una, y en qué orden circuló el expediente (Cusco–Sicuani–Tinta–Cusco)? | 1+3 | A | E |
| PC16 | ¿Qué resolvió la autoridad sobre la queja y en qué afirmaciones previas se apoyó? | 3 | A | E |
| PC17 | ¿Qué condición fiscal y social se atribuye a Huancachoque (originario, miliciano, tributario, hijo de quién) y quién la atribuye? | 3 | A | E |
| PC18 | ¿Qué cargos ejercía Andrés Chuquitapa, sobre qué ayllus, con qué vigencia conocida y según qué afirmaciones? | 3+4 | R | E |
| PC19 | ¿Son la misma persona el «Mariano Casorla» que declara en septiembre y el «Martin Cazorla» que firma la certificación de agosto? ¿Quién lo propone y con qué evidencia? | 2+4 | R | E |
| PC20 | Este dato concreto, ¿de qué versión de la transcripción procede, qué proceso lo extrajo (modelo, prompt) y quién lo validó? | P | D | E |

## Respuestas provisionales del modelador (a validar)

Cada respuesta indica el tramo. Lo que es inferencia del modelador va marcado **[inferencia]**.

**PC01.** La carátula (UT00) y las certificaciones de agosto: Isidro Cano, 1 de agosto (UT01); Santiago Cazorla, 5 de agosto, y Juan Quiñones/Juan Cazorla, sin fecha (UT02); Fernando Orue, sin fecha (UT03); Martín Cazorla, sin fecha (UT04). Siguen el escrito de Huancachoque al Fiscal protector, «CUSCO AGOSTO 22 DE 1806» (UT05–06); la vista fiscal, «Agosto 21» (UT07–08, F1); la notificación al fiscal, 23 de agosto (UT08); la ratificación, «trece» de agosto (UT08, F2); el auto, 27 de agosto, y sus notificaciones (UT09); y el oficio al subdelegado, 28 de agosto (UT09). Después: la providencia de Sicuani del 17 de septiembre (UT10); la nota de desglose, Tinta, 23 de septiembre (UT10); el auto cabeza de la información y su notificación a Chuquitapa (UT10–11); las declaraciones de Cano, el 23 de septiembre (UT11–12.a), del declarante de UT12, «inmediatamente» (UT12), de Santiago Cazorla, el 24 de septiembre (UT13–14), y de Orue, «seguidamente» (UT14–15); el oficio al cura, 24 de septiembre (UT15); el informe del cura, «Noviembre 26» (UT16, F5); los decretos de Sicuani del 8 de noviembre (UT17); el informe del subdelegado, 8 de noviembre (UT17–18); el auto del 26 de noviembre (UT19); la vista fiscal del 20 de noviembre (UT19–20); y las notificaciones del 26 de noviembre y del «23 de diciembre de 1810» (UT20, F6). Al final, el comienzo de un documento ajeno (UT20).

**PC02.** La declaración de UT12.a muestra al declarante «la certificación De folio 4 su firma Martin casorla». En la transcripción, la certificación firmada «Martin Cazorla» está en UT04. La correspondencia con el folio 4 la afirma el documento; la transcripción no la marca.

**PC03.** El índice onomástico del catálogo trae «Chuquitapa Andrés: CCc 14 (18)» y «Guancachoque, Manuel: CCc 14 (18)», es decir, solo este expediente. Tinta aparece en otras fichas (pendiente de extracción a nivel de ficha). La respuesta es **según el catálogo**, que es una afirmación de los catalogadores.

**PC04.** Pendiente de extracción a nivel de ficha. Solo se responde con afirmaciones del catálogo.

**PC05.** Ver `docs/01_materiales.md`, N1. Hay al menos once grafías distintas; dentro del texto de la autoridad (UT07, UT09–UT20) domina «Guancachoque».

**PC06.** Las menciones sin identificar son: «don Juan Quiñones» y el firmante «Juan Cazorla» (UT02, UT17); «el Gobernador Señor Don Mariano Casorla» (UT12.a); el corregidor «Don Andres ……» (UT11); el firmante de «[María Rubrica]» (UT17), **[inferencia]** probablemente Mata; y «la mujer de Chiquitas» (UT15).

**PC07.** Pueblo de Tinta; Sicuani (UT10, UT17, UT18); Cusco (passim); San Pedro de Cacha (UT02); los ayllus Tinta (UT03, UT05, UT17) y Uchu (UT05) o Ucho (UT17–18); la cárcel de Tinta; el partido de Tinta; la provincia de Urubamba (UT20, documento ajeno). Identificadores de HGIS: ver `docs/C_modelo.md` §Lugares.

**PC08.** Ver `docs/E_prueba_hilo_central.md`. En resumen:

* **Cano.** En agosto afirma que Chuquitapa fue «complice y coronel» de Túpac Amaru y que los indios se alzaron a media noche (UT01). En septiembre se ratifica, pero precisa «Comisionado por este y no coronel». Del alzamiento dice que «no le consta» y que lo sabe porque se lo contó Santiago Cazorla (UT11).
* **Declarante de UT12** (certificación de Martín Cazorla). No sabe escribir; mandó a Simón Arce poner lo que relataba. No sabe quién transcribió ni firmó su nombre. Las expresiones sobre el alzamiento y «el Rebelde» no son suyas; vio a «quatro o seis Yndios» (UT12.b).
* **Santiago Cazorla.** Su certificación de agosto solo dice que Huancachoque fue soldado durante más de cinco años (UT02). En septiembre declara sobre lo que le contaron de madrugada (UT13–14).
* **Orue.** No firmó; lo escribió un hijo suyo. La hora no fue la que dice la certificación. Mantiene «coronel y comisionado». Actuó por enemistad con la mujer de Chuquitapa (UT14–15).
* **Juan Quiñones/Juan Cazorla.** No declaró: estaba ausente (UT17).

**PC09.** **DISPUTA.**

* Afirman que fue coronel: Cano en su certificación (UT01, «complice y coronel»), Orue en su certificación (UT03, «coronel, comecionado») y Orue en su declaración (UT14, «coronel y comisionado»).
* Lo niega en parte: Cano en su declaración jurada (UT11, «Comisionado por este y no coronel»).
* Ninguna autoridad se pronuncia sobre este punto. La vista fiscal de noviembre descalifica las quejas en general (UT19–20).

**PC10.** **DISPUTA.**

* El subdelegado Mata dice que las redactó el propio Guancachoque y que hizo firmar a otros sin que conocieran el contenido (UT17).
* El declarante de UT12.b dice que las redactó Simón Arce por encargo suyo.
* Orue dice que la suya la escribió un hijo suyo (UT14, UT15).
* Cano reconoce la firma como propia (UT11) y no dice quién redactó el texto.

**PC11.** **DISPUTA.** Huancachoque dice «dos días preso» (UT06). Mata dice una noche, libertad «al otro dia por la tarde» (UT18). El fiscal, en agosto, recoge su prisión sin duración (UT07).

**PC12.** **NC.** La petición de exención se mandó informar por separado (UT08, UT09). En Sicuani se ordenó desglosarla y agregarla al expediente de la primera denuncia (UT10). La nota de desglose consta (UT10). El expediente no contiene la resolución sobre la matrícula.

**PC13.** **NC.** El auto del 26 de noviembre ordena al subdelegado tomar «providencias … a fin de contener los excesos» (UT19). Hay notificaciones del 26 de noviembre y del «23 de diciembre de 1810» (UT20). No hay constancia de ejecución.

**PC14.** **DISPUTA.** Ver H1: nueve, diez, diez u once, media noche, «primer puesto del gallo». El número de indios va de «quatro o seis Yndios» (UT12.b) a «una caterva» (UT06) y «un montón» (UT02, UT03).

**PC15.** Ver PC01 y la tabla de actuaciones de `docs/E_prueba_hilo_central.md`. Intervienen el Fiscal protector y fiscal (del Río), el Presidente (Ruiz de Castilla en agosto; Muñoz en noviembre), el teniente asesor Galeano, el escribano Chacón, el subdelegado Mata/Mara, que actúa con testigos «a falta de Escribano», el cura interino y el protector partidario Valencia.

**PC16.** Es una afirmación con autoridad, no un hecho. La vista fiscal (UT19–20, fechada el 20 de noviembre) sostiene que las quejas resultan «menos conforme a la verdad» y que fueron formadas con «malicia». Se apoya en el informe del subdelegado (UT17–18), que a su vez remite al informe del cura (UT16) y a las declaraciones (UT11–15). El auto del 26 de noviembre (UT19) resuelve «de conformidad» con el fiscal.

**PC17.** «Indio originario y vecino del pueblo de Tinta» lo dice él mismo (UT05). Que no había tributado por servir en las milicias, también él (UT06). «Soldado en mi compañía más de cinco años», Santiago Cazorla (UT02). «Yndio originario», el escribano en la ratificación (UT08). Hijo espurio de Antolín Ortiz y de Agustina Falcón, «India Ordinaria y pleveya», el cura (UT16.a). Se le matriculó en clase de tributario: carátula (UT00) y escrito (UT06).

**PC18.** Los cargos atribuidos son: «casique del Ayllo Tinta» (UT00); «recaudaderor» y «Recaudador de Tributos» (UT05, UT07); «Recaudador de Reales Tributos de dicho Pueblo» (UT09); «recaudador de tributos de los Ayllus Tinta y Ucho» (UT17); «su casique y alcalde mayor» (UT16.b). La vigencia consta en 1806. El comienzo no consta. **[inferencia]** Que fuera cacique en tiempos del corregidor Reparaz lo afirman testigos, no la autoridad.

**PC19.** **R.** La hipótesis «el declarante de UT12 es Martín Cazorla» se apoya en que se le muestra su certificación de folio 4, habla de ella en primera persona, dice que no sabe escribir y que en 1780 «era muchacho». En contra pesa que el texto lo llama «Gobernador Señor Don Mariano Casorla». La reconstrucción debe registrarse con autor y fecha, y con las dos menciones sin fusionar.

**PC20.** **P.** Se responde con PROV-O: el `prov:Entity` del registro, `prov:wasGeneratedBy` la actividad de extracción, `prov:used` la transcripción con su sha256 y el prompt, y `prov:wasAssociatedWith` el modelo y la persona que validó.

## Qué preguntas solo puede ganar el grafo (hipótesis previa a la evaluación)

Se formulan ahora para no ajustarlas después. Son las que exigen **agregación con atribución** a través de piezas y
tramos: PC05, PC06, PC08, PC09, PC10, PC14, PC16, PC18 y PC19 (y PC03–PC04, a escala de serie). Un LLM con todo el
texto en contexto puede acertar PC09 o PC11 en prosa. Es probable que falle en la exhaustividad (todas las grafías,
todos los firmantes) y en distinguir quién lo afirma frente a quién lo resuelve. Un RAG vectorial simple tiende a
recuperar solo un lado de cada disputa. Ver `docs/G_evaluacion.md`.
