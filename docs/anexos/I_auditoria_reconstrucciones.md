# Anexo I · Auditoría independiente de las reconstrucciones (capa 4)

> Auditor: Claude Opus 5.5, en el papel de revisor escéptico independiente. Fecha: 2026-11-13.
> Objeto: las 26 reconstrucciones de `datos/reconstrucciones.jsonl` y las 23 fechas de `datos/fechas_normalizadas.csv`.
> Fuentes: solo `corpus/Transcripcion_CC_L14E18.txt`, leída por tramos con `laad.fuente.tramo`, y los registros de capas 2–3 de
> `datos/registros/hilo_central.jsonl`. **No** se ha usado `corpus/corpus_modernizado.txt`.
> Identificadores externos: comprobados el 2026-11-13 en la API de Wikidata (`wbgetentities`) y en la API de lugares de WHG
> (`/api/place/<id>/`). Las fichas de Getty TGN no respondieron a la consulta automática; los TGN de Tinta, Sicuani y Cusco se
> dan por buenos porque coinciden con la propiedad P1667 de su elemento de Wikidata.
> Convenciones: «…» es cita literal de la transcripción, con los espacios colapsados (la única normalización que admite
> `docs/01_materiales.md` §3). **[inferencia]** marca lo que deduce el auditor y que el texto no dice.
> La tabla de propuestas en formato de máquina está en `datos/auditoria_reconstrucciones.csv`.

## 0. Resumen

| Veredicto | N | Reconstrucciones |
|---|---|---|
| sostenida | 8 | R-cano, R-orue, R-martin-cazorla, R-cura-valdes, R-tinta, R-prision, R-cusco, R-ayllu-ucho |
| sostenida-con-correcciones | 17 | R-chuquitapa, R-chiquitas, R-huancachoque, R-declarante-p19-es-martin, R-mata, R-rubrica-es-mata, R-quinones, R-juan-cazorla, R-tupac-amaru, R-alboroto-carcel, R-sicuani, R-san-pedro-cacha, R-ayllu-tinta, R-fiscal-del-rio, R-cargo-chuquitapa-recaudador, R-cargo-chuquitapa-cacique, R-cargo-chuquitapa-alcalde-mayor |
| debil | 1 | R-declarante-p19-es-mariano |
| incorrecta | 0 | — |

Ninguna fusión de menciones es errónea. Los problemas son de otro tipo:

1. **Calibración demasiado baja.** Hay correferencias seguras («la firma Que dice Isidro Cano es suya propia», el «único Fiscal»)
   que quedaron en `probable`. Se propone subir 12 valores y bajar uno (hipótesis B de P19).
2. **Argumentos con una base equivocada.** El caso más claro es R-rubrica-es-mata: «[María Rubrica]» se lee mejor como la nota del
   transcriptor «[Media rúbrica]» que como «Mata [rúbrica]». En R-cargo-chuquitapa-cacique, la vigencia atribuye a las
   certificaciones algo que no dicen.
3. **Mucho texto sin anotar.** Muchas menciones evidentes no existen en la capa 2 (p. ej. «Ortis o Guancachoque», «Pedro de la
   Mara», «Siquani», «Ayllos Tinta, y Ucho»), así que no se pueden enlazar. Se listan para la próxima anotación.
4. **Faltan hipótesis rivales.** Se proponen siete: el Chuquitapa de 1780 como homónimo o pariente; «Gobernador» como mala lectura
   de «granadero»; Juan Cazorla igual a Juan de Dios Cazorla; Antonio Valdés como cura propietario; Quiñones como persona real no
   residente; el alias «Ortiz» del denunciante; «Noviembre» como mala lectura de «7bre» en P23.
5. **Fechas.** Las 23 fechas reproducen bien lo escrito. Faltan **P19** (23-09-1806) y **P21** (24-09-1806), que se infieren de
   «Ynmediatamente» y «Seguidamente». Para las fechas imposibles (P07, P09, P23, P31) se propone un intervalo plausible, sin tocar
   el valor literal.

---

## 1. Personas

### 1.1 R-chuquitapa — Andrés Chuquitapa · **sostenida-con-correcciones** · probable → probable

**Menciones.** Las diez menciones son correctas. Casi todas llevan anáfora explícita («dicho Chuquiitapa», «dicho Chuquitapa»,
«Don Andres Choquitapa», «Son Andres Chuquitapa», «Don Andres Chuquitapa», «andres chuquitaza»). En la intención de los
hablantes, la correferencia es segura.

**Lo que el argumento no dice.** M-UT01-004 («En tiempo del señor corregidor don Antonio Reparas, mando dicho Chuquitapa»),
M-UT03-002 y M-UT14-002 atribuyen al mismo individuo actos de antes de 1780 y el cargo de «coronel, comecionado» de Túpac Amaru.
Eso supone una carrera de más de 26 años, con un oficial rebelde que vuelve a ser cacique y recaudador tras la represión de
1781–1784. **[inferencia]** No es imposible, pero es lo bastante llamativo para registrar una hipótesis rival: que los testigos,
hostiles al cacique, atribuyan a Andrés los hechos de un pariente homónimo, quizá su padre. Además, Cano rebaja en su declaración
lo dicho en su certificación: «fue Comisionado por este y no coronel como expone en su certificación» (UT11). El argumento dice
que todas las menciones aparecen «en el mismo contexto procesal», lo que no es exacto: dos de ellas están en relatos del pasado.

**Menciones que faltan en la capa 2** (no tienen ID y hay que anotarlas): «D. Andres Chuquitapa» (UT00, carátula); «don Andrés
Chukitapa» (UT02, P03); «Chuquitapa» ×3 (UT06); «Recaudado Don Andrés Chuquitapa» y «Don Andrés Choquetapa» (UT09); «Dn Andres
Chuquitapa» (UT10); «Chuquitapa», «D. Andre S. Chuquitape» (UT11); «parien tes de Chuquitapa» (UT12.b); «Ayllus de
Chuquitapa», «inferidos por Chuquitapa» (UT18); «Don Andres Chuquitapa», «Andres chuquitapa» (UT19).

**Cambios.** En el argumento, sustituir la lista de grafías por las reales («Chuquiitapa», «Chuquitapa», «Choquitapa»,
«chuquitaza», «chuquitapa») y separar las menciones del pleito de 1806 de las que se refieren a hechos de antes de 1780. Crear
`R-chuquitapa-1780-pariente` (posible), con M-UT03-002 y M-UT14-002 como menciones discutidas.

### 1.2 R-chiquitas — «Chiquitas» · **sostenida-con-correcciones** · posible → probable

Texto (UT15): «la mujer de Chiquitas habla contra el que declara y su familia, lo que le encolerizo … que chuquitapa no es tan
malo ni de boca tan mordaz como la spa su mujer». Dentro de un mismo período, «su mujer» remite a la mujer de Chuquitapa, y la
frase presenta la mordacidad de esa mujer como el motivo del enojo. Las dos cláusulas hablan de la misma mujer.
**[inferencia]** Este tramo es de los peor transcritos («guancachay», «santiago cacerola», «chuquitaza», «fernando ore»), así que
«Chiquitas» por «Chuquitapa» es una mala lectura muy verosímil.

El argumento cita con exactitud. La prudencia de no fusionar es razonable mientras no se coteje la imagen, pero `posible`
infravalora la evidencia. Cambios: subir a `probable` y añadir al argumento la observación sobre la calidad del tramo. Si el
cotejo la confirma, fusionar M-UT15-001 en R-chuquitapa.

### 1.3 R-huancachoque — Manuel Huancachoque · **sostenida-con-correcciones** · probable → probable

Todas las menciones enlazadas son correctas. La de M-UT14-003, «como ha puesto guasscachoque en la citada certificacion», se
refiere al denunciante: Orue le atribuye la redacción.

M-UT02-003 («Manuel Guamanchoque ha estado soldado en mi compañía», P02) es la única fusión que no es segura. El argumento la
justifica bien. El escrito dice «por haber estado empleado en las milicias de aquella provincia, hasta aquí no había tributado»
(UT06), y P02 añade «quien padece de sus enemigos por ser leal», que es el discurso del denunciante. Esa mención es la que
mantiene la reconstrucción en `probable`. Para el resto (escrito firmado, ratificación, informes) sería `verdadero`.

**Falta un alias importante.** En P23 (UT16.b) el cura escribe «la aminocidad y altenencia de Maldonado Ortiz a las
Guamcachoque» y «representaciones o diosas de Ortis o Guancachoque». Antes lo ha llamado «hijo Espurio de Antolin Ortiz». El
cura designa al denunciante con el apellido del padre que le atribuye. Hay que anotar esas menciones y enlazarlas. «Maldonado» no
se explica en el texto: **[inferencia]** puede ser una mala lectura de otro nombre o un segundo apellido; se deja como variante
sin resolver.

**Otras menciones sin ID:** «Manuel Mancachoque» (UT00); «Manuel Guancachoque» ×2 (UT07–UT08, incluida la firma de P09);
«Manuel Guancachoque» (UT09, ×3); UT10–UT11 passim; «guancachay» (UT15).

**Cambios.** Anotar y añadir las menciones del alias Ortiz. En el argumento, añadir: «En P23 el cura lo nombra "Ortis o
Guancachoque"».

### 1.4 R-cano — Isidro Cano · **sostenida** · probable → verdadero

Texto (UT11): «siendole manifestado la certificación De esta forma prima de este Expediente dijo que la firma Que dice Isidro
Cano es suya propia y la que acostum bra hacer». Hay reconocimiento expreso de la firma ante el juez, con nombre idéntico y en la
misma causa: la correferencia es segura. La premisa A-UT11-001 está bien elegida. El cargo de la etiqueta («sargento») es literal
en P01. Santiago Cazorla lo llama «primer sargento ysidro cano» (UT13), mención que aún no está anotada; hay que añadirla cuando
lo esté. Advertencia para la capa 3, no para la identidad: en su declaración, Cano llama al corregidor «Don Andres ……», no
Reparaz (N8).

### 1.5 R-orue — Fernando Orue · **sostenida** · probable → verdadero

Texto (UT14): «siendole preguntado si la firma q dise fernando orue presenta en la certificacion de este expediente es echa con
puño y letra». Orue responde sobre esa certificación en primera persona: «no obstante que sabe firmar el declarante no quiso
hacerlo». La correferencia de M-UT03-001, M-UT03-004 y M-UT14-001 es segura. El argumento distingue bien entre el nombre escrito
(M-UT03-004) y la autoría material de la firma, que según UT14–UT15 fue de un hijo suyo.

Hay que ajustar la cita de la premisa: P21 contiene tres atribuciones de autoría incompatibles entre sí («bajo a un hijo suyo q la
pusieron»; «como ha puesto guasscachoque»; «mando que un hijo suyo lo hicieron»). Mención sin ID: «la firma q dise fernando
orue» (UT14). Dato de contexto que conviene registrar en capa 3: Guancachoque «es ahijado del hermano mayor del q declaro»
(UT14).

### 1.6 R-martin-cazorla — Martín Cazorla · **sostenida** · probable → verdadero

Las tres menciones son el mismo nombre, ligado a la misma certificación («De folio 4 su firma Martin casorla», UT12.a). Que el nombre
designe a la persona en cuyo nombre se extiende P05 es seguro. Lo dudoso es quién declara en P19, y eso lo tratan las dos
reconstrucciones siguientes. El argumento es exacto.

### 1.7 R-declarante-p19-es-martin — hipótesis A · **sostenida-con-correcciones** · probable → probable

**Lo que dice el texto** (UT12.a–UT12.b): «Parecio ante mi el Gobernador Señor Don Mariano Casorla vecino Español de este pueblo
de Tinta … siendole manifestado la certificación De folio 4 su firma Martin casorla dijo que el [Folio 20] No sabe escribir … que
con efecto mando el que declara a Simon Arce que pusiere en un papelito lo mismo que relata en la citada certificación que no sabe
quien lo transcribio ni firmo **su nombre** en el papel que se le ha manifestado». Y en UT13: «comprendo ser en edad en veinte y
ocho años».

El dato más fuerte a favor de A es «firmo su nombre»: el nombre que figura en la certificación es el del declarante. Esta
afirmación (A-UT12b-003) **no** está entre las premisas y debe añadirse. La aritmética del argumento es correcta (28 años en 1806,
nacido hacia 1778), aunque «muchacho» para un niño de dos o tres años es una lectura algo forzada.

**Nueva evidencia a favor de A [inferencia paleográfica].** Un «Gobernador Señor Don», analfabeto, de 28 años y «vecino Español»
es anómalo: en un pueblo de indios el gobernador era indio. En cambio, P05 lo presenta como «soldado granadero». Una abreviatura
del tipo «Gran.ro» o «Grad.o» leída como «Gobernador», y «Mrn.» o «Mart.n» leída como «Mariano», explicarían las dos anomalías a
la vez. La lectura «Mariano» pudo verse favorecida por el testigo de asistencia «MARIANO FIGUEROA», que aparece en la línea
anterior. Hay que comprobarlo en la imagen.

**Cambios.** Añadir la premisa A-UT12b-003. Añadir al argumento la hipótesis «Gobernador» = «granadero». Mantener `probable`
hasta el cotejo, que sería decisivo.

### 1.8 R-declarante-p19-es-mariano — hipótesis B · **debil** · posible → improbable

El argumento no aporta ninguna razón a favor de B. La frase «el declarante habla de la certificación como propia» es un argumento
**contra** B. El único apoyo es la lectura literal del nombre y del tratamiento, y ese tratamiento es anómalo por sí mismo (véase
1.7). Si se mantiene B, la variante más defendible es otra: un pariente que responde por Martín. Pero choca con el uso de la
primera persona («mando el que declara») y con «firmo su nombre». Cambios: bajar a `improbable` y reescribir el argumento con los
apoyos reales (la lectura literal) y los contrarios (primera persona, «su nombre», edad, analfabetismo).

### 1.9 R-mata — Pedro de la Mata · **sostenida-con-correcciones** · probable → probable

Las cinco menciones son correctas. Las tres de tipo «ante mi» (M-UT12.a-007 y M-UT14-004, «comparecio ante mi el grl. sub
delegado») corresponden al juez de una información que Mata dirige sin escribano («a falta de Escribano», UT11, UT12.a). El
argumento dice bien que «Pedro de la Mara» no está anotado.

**Falta una mención anotada:** M-UT19-003 («librese la correspondiente orden al subdelegado del partido de tinta», P28,
26-11-1806). **[inferencia]** Lo más probable es que siga siendo Mata (firmó el informe del 8 de noviembre), pero es una
referencia al cargo. Se añade con esa reserva, y por eso no se sube la reconstrucción a `verdadero`.

**Sin ID:** «Pedro de la Mara» (UT10, P14; UT11, P16); «pedro de Mata[Firma]» (UT15, P22); «Al subdelegado de Tinta» (UT09,
P13); «se me remitio ami el subdelegado» (UT10). Matiz para la etiqueta: el texto no dice «subdelegado» junto al nombre en UT11
(«D.Pedro de la Mata………. de este partido»: la palabra omitida es probablemente «Subdelegado» **[inferencia]**). El cargo sí
consta en «la tranquilidad publica del partido de mi cargo» (UT18).

### 1.10 R-rubrica-es-mata — «[María Rubrica]» · **sostenida-con-correcciones** · posible → probable

**La base del argumento es dudosa.** En la transcripción aparece dos veces «[ María Rubrica]» / «[María Rubrica]», entre
corchetes, que es la convención del transcriptor para sus notas («[Firma]», «[Folio 34 ]», «[Firma Chacon]»).
**[inferencia paleográfica]** Lo más verosímil es que sea la nota **«[Media rúbrica]»**, fórmula diplomática habitual para los
decretos que se autorizan con media firma o rúbrica. «María» sería un error del transcriptor o de un corrector automático. No es
probable que sea «Mata [rúbrica]», como sostiene el argumento: el nombre de la persona no estaría dentro del corchete.

**La conclusión se sostiene por otra vía.** Los dos decretos de UT17 los dicta el juez comisionado: espera a Juan Cazorla «para
recibirle la declaración Respectiva» y luego ordena «diríjase con lo actuado y el correspondiente Informe al Muy Ilustrísima Señor
Padre» (léase Presidente). Ese juez es Mata, que fecha su informe en Sicuani el mismo 8 de noviembre. Con esta base, `probable` es
adecuado.

**Cambio de argumento propuesto:** «"[María Rubrica]" es con toda probabilidad la nota del transcriptor "[Media rúbrica]". Los
decretos de UT17 los dicta el juez comisionado de la información, que reúne lo actuado y lo remite con su informe al Presidente;
ese juez es Pedro de la Mata (P16, P18, P27). Cotejar con la imagen.»

### 1.11 R-quinones — «Don Juan Quiñones» · **sostenida-con-correcciones** · indeterminado → indeterminado (dividir)

La reconstrucción mezcla dos proposiciones distintas:

* (a) **M-UT02-001 y M-UT17-002 designan el mismo nombre o persona.** Es seguro: el juez se refiere a «la Certificación a folios 2
  extendida a nombre del teniente Alguacil Don Juan Quiñones». Valor: `verdadero`.
* (b) **Esa persona existe.** Esto sí está en disputa: el juez dice «que no hay tal hombre en el pueblo de Tinta». Valor:
  `indeterminado`.

**Corrección del argumento.** Dice que el juez afirma que «la firmó Juan Cazorla». El texto de P24 dice «Juan Cazorla de quien
aparece firmada la Certificación». En P25 sí dice «Juan Cazorla que suscribió el documento de 2 fojas», pero esa mención no está
anotada.

**Hipótesis rivales que conviene registrar.** H1: Quiñones es un nombre puesto por quien redactó el papel (según Mata, el propio
Guancachoque: «fueron hechos por el mismo Guancachoque», UT17). H2: es una persona real que no reside en Tinta; el juez es parte
interesada y su «no hay tal hombre» puede ser exagerado. **[inferencia]** A favor de la existencia de un autor distinto de
Santiago Cazorla: el texto distingue «mi puerta» de «la puerta de don Santiago Cazorla» (UT02).

### 1.12 R-juan-cazorla — Juan Cazorla · **sostenida-con-correcciones** · probable → probable

Las menciones son correctas. Hay que corregir el argumento: el juez no lo identifica como firmante en P24 («de quien aparece
firmada»), sino en P25 («que suscribió el documento de 2 fojas»), cuya mención falta.

**Hipótesis rival (posible).** En P20 aparece «mi hermano juan de dios casorlas» y «mi hermano Juan se Dios cazorla» (UT13–UT14),
en el relato de la amenaza de los indios aquella noche. **[inferencia]** El Juan Cazorla firmante podría ser ese Juan de Dios
Cazorla, de la misma familia que Santiago. Así se explicaría que P03 nombre la puerta de Santiago Cazorla como segunda en
recibir guardia. Propuesta: `R-juan-cazorla-es-juan-de-dios` (posible), pendiente de anotar las menciones de UT13–UT14.

### 1.13 R-tupac-amaru — José Gabriel Condorcanqui, Túpac Amaru · **sostenida-con-correcciones** · probable → verdadero

«Joseph Condorcanqui alias Tupac Amaro» (UT16.a) es inequívoco. «Tupa Amaro» y «Tupaamaro», junto a «el rebelde», «el
insurgente» y en el contexto de Tinta (su antiguo cacicazgo y escenario de 1780), también lo son. El argumento atribuye al texto
«el rebelde» y «el insurgente», y es correcto («en el tiempo del rebelde. Tupa Amaro», UT01; «a favor del insurgente,
Tupaamaro», UT03). La única alternativa teórica es Diego Cristóbal Túpac Amaru, que dirigió la rebelión tras abril de 1781, y en
este contexto es `improbable`. Nota: «Gabriel» no está en el texto; procede del conocimiento externo y así debe decirlo la
etiqueta. Identificador externo: Wikidata **Q315937** (Túpac Amaru II, 1738–1781; comprobado).

**Sin ID:** «Tupa amaro» y «Comisionado por este» (UT11); «tupa-amaru», «insurgente tupa» (UT14); «vuestro Condorcanqui» (UT16.b);
«el Rebelde» (UT12.b).

### 1.14 R-cura-valdes — Agustín Valdés, cura interino · **sostenida** · probable → probable

Mata dirige el oficio de P22 al «parroco interino de esta doctrina» y en P27 dice: «Por el informe que le pedí al cura interino de
dicho Pueblo Doctor Don Agustin Valdes». La identificación es directa, del mismo autor. El argumento distingue bien a Antonio
Valdés. Se mantiene `probable` (y no `verdadero`) porque la única fuente es Mata y la firma del informe no está transcrita
(«Firma»). A eso se suma el problema de fecha F5 (véase §4), que hace que convenga cotejar que el informe citado es este.

**Hipótesis complementaria (posible):** el tío «Doctor Don Antonio Valdes» es el «señor cura propietario» ausente. Texto: «como
parroco interino de esta doctrina por hallarse ausente el señor cura propietario de ella; pues aunque interino ha venido en
compañía de su tio el Doctor Don Antonio Valdes algun tiempo». **[inferencia]** La concesiva («aunque interino») y la compañía del
tío sugieren que el interino lleva tiempo en la doctrina con el titular.

### 1.15 R-fiscal-del-rio — el fiscal de la Audiencia · **sostenida-con-correcciones** · probable → verdadero

El argumento pasa por alto el dato decisivo: UT09 lo llama «su único Fiscal en esta Real Audiencia». Si el fiscal es único, las
firmas de agosto y noviembre son de la misma persona. La variación «Gómez» / «Gonzalo» / «Gonsalo» y «Luis» / «Lucio» se explica
bien como lectura distinta de una abreviatura (**[inferencia]**: «Glz.», «Gonz.o», «L.s»). Queda sin resolver el nombre, no la
identidad.

**Sin ID:** «Señor Don Luis Gomez del Rio» (UT08, P08); «Señor Don Luis Gonsalo del Rio» (UT09, P11); «don Lucio Gonzalo del Rio
y Vial» (UT20, P30); «El fiscal de su Majestad» (UT07). **[inferencia]** P06 va dirigido al «SEÑOR FISCAL PROTECTOR GENERAL DE
NATURALES» y lo presenta «El fiscal de su Majestad … el antecedente escrito que le ha presentado»: el fiscal hace también de
protector general. No hay que confundirlo con el «Doctor Don Manuel Valencia Abogado protector partidario de naturales» (UT08).

## 2. Lugares y grupos

Comprobaciones externas (2026-11-13):

| Reconstrucción | WHG / HGIS (API) | Wikidata (API) | TGN |
|---|---|---|---|
| R-tinta | 177060 = «Tinta», src_id 6000357, (-71.406341, -14.144732), Tinta (Jurisdicción) 1701–1808 ✔ | Q2435935 «Tinta, village in Cusco, Peru», (-14.1444, -71.4056) ✔ | 9227290 = P1667 de Q2435935 ✔ |
| R-sicuani | 177068 = «Sicuani», 6000365, (-71.226594, -14.273289), Tinta (Jurisdicción) ✔ | Q4419079 «Sicuani, town in Peru» ✔ | 1024771 = P1667 ✔ |
| R-cusco | 176704 = «El Cuzco», 6000002, (-71.97888, -13.516718) ✔ | Q5582862 «Cusco, historic city…» ✔ | 7005819 = P1667 ✔ |
| R-san-pedro-cacha | 177061 = «San Pedro», 6000358, **variante «Cacha»**, Tinta (Jurisdicción) ✔ | Q13190677 «San Pedro, town in Cusco», P131 Q3313072, (-14.1865, -71.3434), mismo punto que HGIS ✔; sin P1667 | 8712075 figura en `alineaciones_lugares.csv` pero **no** en `ver_tambien`; no verificado por el auditor |

### 2.1 R-tinta · **sostenida** · probable → verdadero

M-UT01-007 («En el pueblo de Tinta, en primero de agosto de 1806») es el pueblo y no el partido. Los identificadores son correctos y
se descartan bien los homónimos. El único candidato del partido es inequívoco, así que procede `verdadero`. Advertencia para la
anotación futura: el texto usa «Tinta» con cuatro referentes que no deben fusionarse. Son el pueblo; el partido («partido de este
nombre», UT05; «partido de Tinta», UT07; HGIS JUPECUTI); la «compañía de Tinta de Milicias» y el «regimiento de Tinta»; y el
«Ayllu Tinta».

### 2.2 R-sicuani · **sostenida-con-correcciones** · probable → verdadero

Identificadores correctos. La etiqueta dice «residencia del subdelegado», pero el texto solo prueba que fecha allí sus actos
(«Sicuani Setiembre. 17 de 1806», UT10; «Sicuani Noviembre 8 de 1806», UT17; «Siquani Noviembre 8 de 1806», UT18). Se propone la
etiqueta «Sicuani (pueblo), lugar de data de las providencias e informe del subdelegado». **[inferencia]** Que fuera su residencia
es plausible, pero no consta. Menciones sin ID: las dos de noviembre.

### 2.3 R-cusco · **sostenida** · verdadero → verdadero

Correcto. Que «CUSCO AGOSTO 22 DE 1806» sea la data del escrito y no una nota de presentación no cambia la identidad del lugar.
La mención de la Audiencia en la etiqueta es contexto externo (la Audiencia del Cusco empezó a funcionar en 1788), coherente con
el periodo HGIS «Cuzco (Audiencia) 1788–1808».

### 2.4 R-san-pedro-cacha · **sostenida-con-correcciones** · posible → probable

**Dato nuevo:** el registro WHG 177061 / HGIS 6000358 incluye la variante **«Cacha»** y está en la jurisdicción de Tinta. Eso
convierte la equivalencia, que el argumento presenta como «sin confirmación», en una coincidencia de nombre registrada por el
propio gazetteer. Las coordenadas de Wikidata Q13190677 coinciden al metro con las de HGIS. Procede `probable`, y `verdadero`
sería defendible.

**Incoherencia entre ficheros:** `alineaciones_lugares.csv` da TGN 8712075 y advierte de que su jerarquía en TGN es errónea
(Pasco), pero `ver_tambien` no lo incluye. Hay que decidir y unificar. Se recomienda no enlazarlo hasta revisarlo, o enlazarlo con
una nota. No hay que confundir a «don Javier Aparicio», el soldado de San Pedro de Cacha (UT02), con el testigo «CELEDONIO
APARICIO» (UT12.a).

### 2.5 R-ayllu-tinta · **sostenida-con-correcciones** · probable → verdadero

La identidad es trivial y segura. Hay que precisar el argumento: el texto no dice que se «denunciaron» 44 en el ayllu Tinta, sino
que la averiguación tuvo como consecuencia «el descubrimiento de cuarenta y cuatro tributarios en el Ayllu Tinta y siete en el
Ayllu nominado Uchu» (UT05). Los denunciados fueron 51 en total (UT07, UT09). **Sin ID:** «casique del Ayllo Tinta» (UT00); «los
Indios del Ayllu de tinta» (UT03); «Tinta» en «Ayllus Tinta y Ucho» (UT17), donde M-UT17-007 solo cubre «Ucho»; «Ayllos Tinta,
y Ucho» ×2 (UT17–UT18). La falta del ayllu en HGIS es correcta.

### 2.6 R-ayllu-ucho · **sostenida** · probable → verdadero

«Ayllu nominado Uchu» (UT05) y «Ayllus Tinta y Ucho» (UT17) aparecen ambas en el contexto de la numeración de tributarios. La
alternancia u/o es la vacilación vocálica normal en la grafía colonial de voces quechuas. **Sin ID:** «Ayllos Tinta, y Ucho»
(UT17, UT18) y «citados Ayllos Tinta y Ucho» (UT18).

## 3. Hechos y cargos

### 3.1 R-alboroto-carcel · **sostenida-con-correcciones** · probable → probable (con etiqueta mínima)

Los siete hechos enlazados son correctos. La cita «quatro o seis Yndios … con garrotes» es fiel («vio a quatro o seis Yndios en la
puerta de la carcel con garrotes», UT12.b). Pero el argumento se queda corto en dos puntos:

1. **Los relatos no son independientes.** P01, P03 y P04 son certificaciones que, según Mata, Orue y el declarante de P19,
   redactó o inspiró el propio denunciante. Orue: «le dijo a guancachay q pusiera en la certificaz lo q quisiese q el lo firmaria».
   El declarante de P19 niega haber dicho que «se alzaron los Yndios todos con barrotes armados a dar muerte». P18 es de oídas
   («no le consta al que declara si no porque se lo dijo su segundo sargento Santiago Casorla»). Los testimonios jurados que
   sostienen algún hecho son pocos: P19 («quatro o seis Yndios … con garrotes») y P21 («el aboroto … a la puerta de la carcel y q
   estaban ebrios … el primer puesto del gallo»).
2. **Falta la versión contraria.** Mata (P27) concluye que los documentos sobre «el bullicio, y asonada» «fueron hechos por el
   mismo Guancachoque», y el fiscal (P29) que las quejas son «menos conformes a la verdad». No dicen expresamente que no hubiera
   nada, pero no lo reconocen.

Con eso, `probable` solo se justifica para el **hecho mínimo**: unos pocos indios, algunos ebrios y con garrotes, junto a la puerta
de la cárcel aquella noche. No para «alboroto» ni «alzamiento». Cambios: etiqueta «Presencia nocturna de indios con garrotes ante
la cárcel de Tinta la noche de la prisión de Huancachoque (hecho mínimo)». En el argumento, citar P19 y P21 como apoyo
independiente, señalar la dependencia de P01, P03 y P04 y registrar P27 y P29 como evidencia contraria. Si se anotan, añadir
H-p05 (P05: «Esa misma noche se alzaron los Indios todos con garrotes») y el relato de P20.

### 3.2 R-prision · **sostenida** · verdadero → verdadero

Bien calibrada: la afirman el denunciante («yo me mantuve dos días preso», UT06) y el subdelegado que la ordenó («lo mande llevar
a la cárcel», UT18). La corroboran también P07, P18 («habiendo mandado Esta ponerlo en la caecel a Guancachoque») y P19 («estando
en la carcel aquel»). Sugerencia menor para la etiqueta: «tras la denuncia» → «al día siguiente de concluir la numeración de los
ayllus». Las dos partes coinciden en esa cronología («al siguiente día que prove la ocultación», UT05; «concluida el dia anterior
la numeración», UT17). En la causa de la prisión discrepan: la venganza según el denunciante, el insulto al recaudador según Mata.

### 3.3 R-cargo-chuquitapa-recaudador · **sostenida-con-correcciones** · verdadero → verdadero

La calibración es correcta: lo dicen tres actores de intereses distintos, y lo repiten el auto, el oficio, la providencia, la vista
y el auto final (UT09, UT10, UT19). Hay dos problemas:

* **La vigencia.** `inicio: 1806-08` puede leerse como inicio del cargo. El propio denunciante dice que los tributarios los «tenia
  ocultos … de muchos años atrás» el recaudador (UT05). P14 remite a una primera denuncia «en once de Febrero del año pasado de
  1809» (léase probablemente 1805, F4), que ya iba contra él como recaudador. Propuesta: renombrar los campos a
  `atestiguado_desde` y `atestiguado_hasta`, o añadir al argumento «ejercía ya, según el denunciante, "de muchos años atrás"; y en
  febrero de [1805]».
* **Faltan premisas.** Hay que anotar «Recaudado Don Andrés Chuquitapa» (UT09, P10), «Recaudador de Reales Tributos de dicho
  Pueblo» (UT09, P13), «su recaudador de tributos Dn Andres Chuquitapa» (UT10) y «recaudador de tributos Don Andres Chuquitapa»
  (UT19, P28).

### 3.4 R-cargo-chuquitapa-cacique · **sostenida-con-correcciones** · probable → verdadero

**La `vigencia_literal` es inexacta.** Dice que «las certificaciones lo sitúan ya como cacique en tiempos del corregidor
Reparaz». No es así. P01 («En tiempo del señor corregidor don Antonio Reparas, mando dicho Chuquitapa cargando») y P04 no lo llaman
cacique. P03 dice «Este mismo cacique invento el alzamiento contra don Miguel Orey»: lo llama cacique **en presente** y le atribuye
un hecho pasado («muy antes de la rebelion»), sin decir que entonces lo fuera.

**Calibración.** En 1806 el título lo dan partes enfrentadas: las certificaciones favorables al denunciante («los indios del
cacique don Andrés Chukitapa», P03; «el robo de mi cacique», P05), el cura favorable al cacique (P23) y la carátula (UT00). Procede
`verdadero` para «era llamado y tratado como cacique en 1806». **[inferencia histórica]** Si era cacique de sangre o
cacique-recaudador nombrado tras las reformas de la década de 1780 no consta, y el argumento ya lo advierte con acierto.

**Cambios.** `vigencia_literal`: «Consta en 1806 (carátula; certificación P03; informe del cura). Ninguna pieza dice que lo fuera
en tiempos de Reparaz.» Añadir premisas cuando se anoten P03 y UT00.

### 3.5 R-cargo-chuquitapa-alcalde-mayor · **sostenida-con-correcciones** · posible → probable

Solo lo dice el cura: «acometen a su casique y alcalde mayor Don Andres Chuquitapa» (UT16.b). El argumento descarta la fuente por
hostil. Esa hostilidad pesa en sus juicios sobre la conducta del denunciante, no en un título de tratamiento que nadie discute y
que no le aporta nada. Además, encaja con la jerarquía que describen otras piezas: «los segundas, los alcaldes, sus parientes y
demás dependientes suyos» (UT05) y «los Alcaldes. Segundas, y Principales de los citados Ayllus de Chuquitapa» (UT17–UT18). Se
propone `probable`.

**Precisión conceptual [inferencia histórica].** Aquí «alcalde mayor» no es el alcalde mayor español (magistrado provincial),
sino el alcalde mayor de naturales o del cabildo indígena del pueblo. Si el concepto `alcalde-mayor` del tesauro no hace la
distinción, hay que añadirla en su definición o crear `alcalde-mayor-de-naturales`.

## 4. Fechas normalizadas (`fechas_normalizadas.csv`)

Se han cotejado las 23 filas con lo escrito. **Todas reproducen bien el valor literal.** Las observaciones siguientes son de
cobertura y de interpretación.

| Pieza | Valor | Lo escrito (tramo) | Juicio |
|---|---|---|---|
| P00 | 1806-08-26 | «Agosto 26 de 1806» (UT00) | ✔. Es la fecha de la carátula: probablemente de formación o registro del expediente, no un acto procesal. |
| P01 | 1806-08-01 | «en primero de agosto de 1806» (UT01) | ✔ |
| P02 | 1806-08-05 | «agosto cinco de mil ochocientos seis años» (UT02) | ✔ |
| P06 | 1806-08-22 | «CUSCO AGOSTO 22 DE 1806» (UT05) | ✔ |
| P07 | 1806-08-21 | «Cusco y Agosto 21 de 1806» (UT08) | Literal ✔, imposible (F1). Intervalo plausible: 1806-08-23/1806-08-27 (tras la diligencia del 23, antes del auto del 27, que se dicta «en conformidad a lo expuesta y pedido por el Señor Fiscal»). Añadir ese intervalo como fecha inferida. |
| P08 | 1806-08-23 | «Agosto veinte y tres de ochocientos seis» (UT08) | ✔ |
| P09 | 1806-08-13 | «en trece días del mees de Agosto de mil ochocientos seis años» (UT08) | Literal ✔, imposible (F2). Intervalo plausible: 1806-08-23/1806-08-27. |
| P10 | 1806-08-27 | «Agosto 27 de 1806» (UT09) | ✔ |
| P11 | 1806-08-27 | «en veinte y siete días del mes de Agosto de mil ocho = Cientos seis años» (UT09) | ✔ |
| P12 | 1806-08-27 | «En dicho día mes y año» (UT09) | ✔ |
| P13 | 1806-08-28 | «Cusco y Agosto 28 de 1806» (UT09) | Literal ✔. Choca con «mi Auto de esté día», que se refiere al auto del día 27. Anotar la discrepancia, sin cambiar el valor. |
| P14 | 1806-09-17 | «Sicuani Setiembre. 17 de 1806» (UT10) | ✔ |
| P15 | 1806-09-23 | «Tinta 23. de Septiembre de 1806» (UT10) | ✔ |
| P18 | 1806-09-23 | «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años» (UT11) | ✔ |
| **P19** | — | «Ynmediatamente» tras P18 (UT12.a) | **Falta.** Añadir `P19,1806-09-23,"«Ynmediatamente» tras P18"`. |
| P20 | 1806-09-24 | «en veinti quatro dias del mes de setiembre de mil ochocientos seis años» (UT13) | ✔ |
| **P21** | — | «Seguidamente comparecio» tras P20 (UT14) | **Falta.** Añadir `P21,1806-09-24,"«Seguidamente» tras P20"`. |
| P22 | 1806-09-24 | «firma y setiembre 24 de 1806» (UT15) | ✔. **[inferencia]** «firma» es probablemente «Tinta» mal leído. |
| P23 | 1806-11-26 | «Firma Noviembre 26 de 1806» (UT16.b) | Literal ✔, imposible (F5: P27 la cita el 8 de noviembre). **Hipótesis paleográfica:** en el original habría «7bre 26» (septiembre), leído como «9bre» (noviembre). Fecha inferida probable: **1806-09-26**, coherente con el oficio del 24 de septiembre. Intervalo seguro: 1806-09-24/1806-11-08. |
| P25 | 1806-11-08 | «Sicuani Noviembre 8 de 1806» (UT17) | ✔. La nota dice «posiblemente de P24», pero el formulario de los decretos lleva la data **delante** del texto («Sicuani Setiembre. 17 de 1806 Por recibida…», UT10), así que la línea encabeza P25. P24 queda sin fecha (entre 1806-09-24 y 1806-11-08). Invertir el peso de la nota. |
| P26 | 1806-11-18 | «Cuzco noviembre 18 de noviembre de 1806» (UT17) | ✔ (F7, repetición del mes). |
| P27 | 1806-11-08 | «Siquani Noviembre 8 de 1806» (UT18) | ✔ |
| P28 | 1806-11-26 | «Cusco y noviembre 26 de 1806» (UT19) | ✔ |
| P29 | 1806-11-20 | «Cuzco y Noviembre 20 de 1806» (UT20) | ✔ |
| P30 | 1806-11-26 | «en veinte y seis de noviembre de mil ochocientos seis» (UT20) | ✔ |
| P31 | 1810-12-23 | «veinte y tres de Diciembre de mil ochocientos 10 años» (UT20) | Literal ✔, dudosa (F6). **[inferencia]** Cuatro años para notificar un auto del 26-11-1806 es poco verosímil, aunque la parte diga que llega «a preguntar por el proveido». Fecha alternativa: 1806-12-23. Mantener la literal con la marca de dudosa y registrar la alternativa. |

Las piezas sin fecha propia (P03–P05, P16, P17, P24, P32) no están en el fichero, lo cual es correcto. Si se quiere, P03–P05 pueden
acotarse entre la prisión (anterior al 1-8-1806, porque P01 ya la narra) y el 22-8-1806, y P16–P17 entre el 17 y el 23-9-1806.

## 5. Hipótesis rivales propuestas (nuevas reconstrucciones)

| Id propuesto | Proposición | Creencia | Base |
|---|---|---|---|
| R-chuquitapa-1780-pariente | El «coronel, comecionado» de Túpac Amaru y el agitador de tiempos de Reparaz no es Andrés, sino un pariente homónimo | posible | Duración de la carrera; la rebaja de Cano en P18; los testigos son hostiles |
| R-declarante-p19-gobernador-es-granadero | «el Gobernador Señor Don Mariano Casorla» es una mala lectura de «el granadero … Martin Casorla» | posible (refuerza A) | P05 «soldado granadero»; anomalía de un «Gobernador» analfabeto de 28 años |
| R-rubrica-es-media-rubrica | «[María Rubrica]» = «[Media rúbrica]» | probable | Convención de corchetes del transcriptor; fórmula diplomática |
| R-juan-cazorla-es-juan-de-dios | El firmante Juan Cazorla es Juan de Dios Cazorla (P20) | posible | Mismo nombre de pila y apellido, misma familia |
| R-antonio-valdes-cura-propietario | El tío Antonio Valdés es el cura propietario ausente de Tinta | posible | Construcción de P22 |
| R-huancachoque-alias-ortiz | «Ortis o Guancachoque» / «Maldonado Ortiz» designa al denunciante | probable | P23, UT16.b |
| R-quinones-real-no-residente | Juan Quiñones existe pero no reside en Tinta | posible | El juez es parte interesada; P03 distingue «mi puerta» de la de Santiago Cazorla |
