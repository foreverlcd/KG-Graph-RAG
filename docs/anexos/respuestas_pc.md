# Respuestas del grafo a las preguntas de competencia

> Generado por `scripts/responder_pc.py` a partir de `datos/grafo/cc-14-18.trig`. No editar a mano.

## PC01

```text
PREGUNTA: ¿Qué piezas forman el expediente, en qué orden, de qué tipo y con qué fecha?
RESPUESTA (D): 33 piezas en orden físico de la transcripción; 11 incoherencias de fecha señaladas.

  P00 [carátula] Carátula del expediente — fecha escrita: «Agosto 26 de 1806»
  P01 [certificación] Certificación del sargento Isidro Cano — fecha escrita: «en primero de agosto de 1806»
  P02 [certificación] Certificación del sargento primero Santiago Cazorla — fecha escrita: «agosto cinco de mil ochocientos seis años»
  P03 [certificación] Certificación a nombre del teniente alguacil Juan Quiñones, firmada Juan Cazorla — sin fecha escrita
  P04 [certificación] Certificación a nombre del cabo primero Fernando Orue — sin fecha escrita
  P05 [certificación] Certificación a nombre del soldado granadero Martín Cazorla — sin fecha escrita
  P06 [petición] Escrito de Manuel Huancachoque al Fiscal Protector General de Naturales — fecha escrita: «CUSCO AGOSTO 22 DE 1806»
  P07 [vista fiscal] Vista del fiscal al Presidente — fecha escrita: «Cusco y Agosto 21 de 1806»
  P08 [notificación] Notificación del decreto al fiscal — fecha escrita: «En el Cusco y Agosto veinte y tres de ochocientos seis»
  P09 [reconocimiento y ratificación] Reconocimiento y ratificación del escrito por Huancachoque ante el teniente asesor — fecha escrita: «en trece días del mees de Agosto de mil ochocientos seis años»
  P10 [auto] Auto del 27 de agosto que remite al subdelegado — fecha escrita: «Agosto 27 de 1806»
  P11 [notificación] Notificación del auto al fiscal — fecha escrita: «En el Cuzco en veinte y siete días del mes de Agosto de mil ocho = Cientos seis años»
  P12 [notificación] Notificación del auto a Huancachoque — fecha escrita: «En dicho día mes y año»
  P13 [oficio] Oficio del Presidente al subdelegado de Tinta — fecha escrita: «Cusco y Agosto 28 de 1806»
  P14 [decreto] Providencia del subdelegado en Sicuani: desglose y orden de información — fecha escrita: «Setiembre. 17 de 1806»
  P15 [desglose y agregación] Nota de desglose de las dos fojas de denuncia — fecha escrita: «Tinta 23. de Septiembre de 1806»
  P16 [auto cabeza de proceso] Auto cabeza de la información y orden de retiro de Chuquitapa — sin fecha escrita
  P17 [notificación] Notificación a Chuquitapa — sin fecha escrita
  P18 [declaración jurada] Declaración jurada de Isidro Cano — fecha escrita: «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»
  P19 [declaración jurada] Declaración jurada sobre la certificación firmada Martín Cazorla (declarante mencionado como Mariano Casorla) — fecha escrita: «Ynmediatamente»
  P20 [declaración jurada] Declaración jurada de Santiago Cazorla — fecha escrita: «en veinti quatro dias del mes de setiembre de mil ochocientos seis años»
  P21 [declaración jurada] Declaración jurada de Fernando Orue — fecha escrita: «Seguidamente»
  P22 [oficio] Oficio del subdelegado al cura interino pidiendo informe — fecha escrita: «setiembre 24 de 1806»
  P23 [informe] Informe del cura interino sobre la conducta de Huancachoque — fecha escrita: «Noviembre 26 de 1806»
  P24 [decreto] Decreto: se espera a Juan Cazorla para recibirle declaración — sin fecha escrita
  P25 [decreto] Decreto de remisión de lo actuado al Presidente (fecha de data ambigua: puede cerrar P24) — fecha escrita: «Sicuani Noviembre 8 de 1806»
  P26 [decreto] Decreto de vista al fiscal — fecha escrita: «Cuzco noviembre 18 de noviembre de 1806»
  P27 [informe] Informe del subdelegado Pedro de la Mata al Presidente — fecha escrita: «Siquani Noviembre 8 de 1806»
  P28 [auto] Auto del 26 de noviembre (decreto marginal) de conformidad con el fiscal — fecha escrita: «Cusco y noviembre 26 de 1806»
  P29 [vista fiscal] Vista del fiscal sobre el informe del subdelegado — fecha escrita: «Noviembre 20 de 1806»
  P30 [notificación] Notificación del auto al fiscal — fecha escrita: «en veinte y seis de noviembre de mil ochocientos seis»
  P31 [notificación] Notificación del auto (persona notificada no expresa) — fecha escrita: «veinte y tres de Diciembre de mil ochocientos 10 años»
  P32 [certificación] Comienzo de una certificación notarial republicana ajena al expediente — sin fecha escrita

Control de secuencia (fechas normalizadas en capa 4 frente al orden físico):
  P06 (1806-08-22) antes que P07 (1806-08-21): orden físico contra fecha
  P06 (1806-08-22) antes que P09 (1806-08-13): orden físico contra fecha
  P07 (1806-08-21) antes que P09 (1806-08-13): orden físico contra fecha
  P08 (1806-08-23) antes que P09 (1806-08-13): orden físico contra fecha
  P23 (1806-11-26) antes que P25 (1806-11-08): orden físico contra fecha
  P23 (1806-11-26) antes que P26 (1806-11-18): orden físico contra fecha
  P23 (1806-11-26) antes que P27 (1806-11-08): orden físico contra fecha
  P23 (1806-11-26) antes que P29 (1806-11-20): orden físico contra fecha
  P26 (1806-11-18) antes que P27 (1806-11-08): orden físico contra fecha
  P28 (1806-11-26) antes que P29 (1806-11-20): orden físico contra fecha
  P31 (1810-12-23): año fuera del expediente
```

## PC02

```text
PREGUNTA: ¿Qué pieza es la «certificación De folio 4» y dónde está?
RESPUESTA (D): El expediente se refiere a sus propias fojas; esa foliación es una afirmación del documento, no una marca del transcriptor. P05 → «De folio 4»; P03 → «a folios 2». En la transcripción esas piezas no tienen marca de folio (folio no consta).

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT12a-003: la pieza está en tal folio (autorreferencia del expediente) → De folio 4
    «De folio 4 su firma Martin casorla»
    Afirmante: «ante mi» (fedatario) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; declaración jurada P19, fecha escrita «Ynmediatamente»; ante: ante mi; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT12.a, folio no consta en la transcripción
AFIRMACIÓN A-UT17-004: la pieza está en tal folio (autorreferencia del expediente) → a folios 2
    «la Certificación a folios 2 extendida a nombre del teniente Alguacil»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P24, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
```

## PC03

```text
PREGUNTA: PC03
RESPUESTA (PENDIENTE): Requiere extraer las fichas del catálogo como capa 3 (afirmante: catalogadores).
```

## PC04

```text
PREGUNTA: PC04
RESPUESTA (PENDIENTE): Ídem PC03, a escala de serie.
```

## PC05

```text
PREGUNTA: ¿Con qué grafías aparece el denunciante y dónde?
RESPUESTA (D): 7 grafías en 9 menciones anotadas: Guancachoque, MANUEL HUANCACHOQQUE, Manuel Guamanchoque, Manuel Guancachoque, Manuel Guancoichoque, Manuel Huancachoque, guasscachoque. (Agrupadas por la reconstrucción R-huancachoque; ver capa 4.)

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Manuel Huancachoque (Guancachoque), denunciante» — creencia: probable; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT01-002 mencion/M-UT02-003 mencion/M-UT05-001 mencion/M-UT06-002 mencion/M-UT14-003 mencion/M-UT16a-001 mencion/M-UT17-004 mencion/M-UT17-005 mencion/M-UT19-001
    Argumento: Menciones del denunciante en las certificaciones, su escrito, su firma, la declaración de Orue, los informes y la vista fiscal. «Manuel Guamanchoque» (P02) se incluye por el nombre de pila y porque la certificación de su servicio militar coincide con lo que alega en su escrito (no había tributado por servir en las milicias).

  «Guancachoque» — UT01, pieza P01 (certificación), mención M-UT01-002
  «Manuel Guamanchoque» — UT02, pieza P02 (certificación), mención M-UT02-003
  «Manuel Huancachoque» — UT05, pieza P06 (petición), mención M-UT05-001
  «MANUEL HUANCACHOQQUE» — UT06, pieza P06 (petición), mención M-UT06-002
  «guasscachoque» — UT14, pieza P21 (declaración jurada), mención M-UT14-003
  «Manuel Guancachoque» — UT16.a, pieza P23 (informe), mención M-UT16a-001
  «Manuel Guancachoque» — UT17, pieza P27 (informe), mención M-UT17-004
  «Guancachoque» — UT17, pieza P27 (informe), mención M-UT17-005
  «Manuel Guancoichoque» — UT19, pieza P29 (vista fiscal), mención M-UT19-001
```

## PC06

```text
PREGUNTA: ¿Qué menciones no se pueden identificar con seguridad y por qué?
RESPUESTA (R): 6 reconstrucciones de identidad con creencia posible o indeterminada.

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Andrés Chuquitapa, alcalde mayor» — creencia: posible; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: afirmacion/A-UT16b-002
    Argumento: Solo lo afirma el informe del cura, hostil al denunciante y favorable al cacique.
RECONSTRUCCIÓN «El declarante de P19 es un Mariano Casorla distinto de Martín (hipótesis B)» — creencia: posible; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT12.a-005
    Argumento: La transcripción lo llama «el Gobernador Señor Don Mariano Casorla». Si fuera otra persona, el expediente no recogería la declaración de Martín Cazorla, pero el declarante habla de la certificación como propia. Se mantiene como alternativa hasta cotejar la imagen.
RECONSTRUCCIÓN «San Pedro de Cacha (pueblo)» — creencia: posible; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT02-006
    Argumento: HGIS registra «San Pedro» (src_id 6000358, WHG 177061) en la jurisdicción de Tinta, entre Tinta y Sicuani; la equivalencia con San Pedro de Cacha se apoya en nombre, jurisdicción y coordenadas, sin confirmación documental.
RECONSTRUCCIÓN ««Chiquitas», marido de la mujer que habla contra Orue (¿Chuquitapa?)» — creencia: posible; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT15-001
    Argumento: En la misma declaración Orue dice que Chuquitapa «no es tan malo ni de boca tan mordaz como la spa su mujer», lo que sugiere que «Chiquitas» es Chuquitapa; se deja como reconstrucción separada hasta que un historiador lo confirme.
RECONSTRUCCIÓN ««Don Juan Quiñones», teniente alguacil (existencia en disputa)» — creencia: indeterminado; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT02-001 mencion/M-UT17-002
    Argumento: La certificación P03 está extendida a su nombre, pero el juez afirma que «no hay tal hombre en el pueblo de Tinta» (A-UT17-002) y que la firmó Juan Cazorla. No se fusiona con Juan Cazorla.
RECONSTRUCCIÓN ««[María Rubrica]» es la rúbrica del subdelegado Mata» — creencia: posible; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT17-003 mencion/M-UT18-001
    Argumento: Los decretos de UT17 los dicta el juez de la causa en Sicuani el mismo 8 de noviembre en que Mata firma el informe; «María Rubrica» parece una mala lectura de «Mata [rúbrica]». Hay que cotejarlo con la imagen.
```

## PC07

```text
PREGUNTA: ¿Qué lugares y ayllus se mencionan y con qué identificador de HGIS?
RESPUESTA (R): 6 lugares o grupos reconstruidos; 4 con identificador HGIS. Sin entrada en HGIS: Ayllu Tinta, Ayllu Uchu / Ucho.

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Ayllu Tinta» — creencia: probable; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT05-003
    Argumento: Ayllu del pueblo de Tinta donde se denunciaron 44 tributarios ocultos. Sin entrada en HGIS (que no registra ayllus).
RECONSTRUCCIÓN «Ayllu Uchu / Ucho» — creencia: probable; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT05-004 mencion/M-UT17-007
    Argumento: «Ayllu nominado Uchu» (escrito del denunciante) y «Ayllus Tinta y Ucho» (informe del subdelegado) designan el mismo ayllu del pueblo de Tinta; variante gráfica u/o.
RECONSTRUCCIÓN «Cusco (ciudad), sede de la Real Audiencia y la Intendencia» — creencia: verdadero; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT05-005
    Argumento: «CUSCO» en la data del escrito presentado ante el Fiscal Protector General. HGIS src_id 6000002 (WHG 176704).
RECONSTRUCCIÓN «San Pedro de Cacha (pueblo)» — creencia: posible; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT02-006
    Argumento: HGIS registra «San Pedro» (src_id 6000358, WHG 177061) en la jurisdicción de Tinta, entre Tinta y Sicuani; la equivalencia con San Pedro de Cacha se apoya en nombre, jurisdicción y coordenadas, sin confirmación documental.
RECONSTRUCCIÓN «Sicuani (pueblo), residencia del subdelegado» — creencia: probable; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT10-001
    Argumento: Pueblo del partido de Tinta donde el subdelegado data sus providencias e informe. HGIS src_id 6000365 (WHG 177068).
RECONSTRUCCIÓN «Tinta (pueblo)» — creencia: probable; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT01-007
    Argumento: Pueblo de Tinta, cabecera del partido homónimo. HGIS de las Indias src_id 6000357 (World Historical Gazetteer place 177060; -71.406, -14.145). Se descartan los homónimos Tinta de Cajatambo (6000993) y Tintay.

  Cusco (ciudad), sede de la Real Audiencia y la Intendencia: HGIS:6000002 https://whgazetteer.org/places/176704/detail
  San Pedro de Cacha (pueblo): HGIS:6000358 https://whgazetteer.org/places/177061/detail
  Sicuani (pueblo), residencia del subdelegado: HGIS:6000365 https://whgazetteer.org/places/177068/detail
  Tinta (pueblo): HGIS:6000357 https://whgazetteer.org/places/177060/detail
```

## PC08

```text
PREGUNTA: ¿Qué afirmó cano en su certificación de agosto y qué en su declaración de septiembre?
RESPUESTA (A): 11 afirmaciones en certificación, declaración jurada.

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT01-001: ejerce o ejerció un cargo → coronel (de Túpac Amaru) (sujeto elíptico resuelto por el anotador)
    «lo mismo en el tiempo del rebelde. Tupa Amaro fue complice y coronel»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-002: ejerce o ejerció un cargo → cómplice (de Túpac Amaru) (sujeto elíptico resuelto por el anotador)
    «lo mismo en el tiempo del rebelde. Tupa Amaro fue complice y coronel»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-003: fecha u hora del hecho → a media noche
    «esa noche todos los indios se alzaron a media noche todos con garrotes»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-004: participa en un hecho → H-p01-alboroto
    «llevamos hasta hoy dia suspecha de la traicion de la orden del dicho Chuquiitapa»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: sospecha; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT11-001: la firma es suya → Ysidro Cano
    «dijo que la firma Que dice Isidro Cano es suya propia»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: YSIDRO CANO / PEDRO DE LA MATA
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-002: se ratifica en el contenido → Ysidro Cano
    «preso ser cierto todo lo que en ella dice que le consta solo»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: YSIDRO CANO / PEDRO DE LA MATA
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-003: ejerce o ejerció un cargo → comisionado (de Túpac Amaru) (sujeto elíptico resuelto por el anotador)
    «en tiempo del rebelde Tupa amaro fue Comisionado por este»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: YSIDRO CANO / PEDRO DE LA MATA; responde a A-UT01-001
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-004 [NIEGA]: ejerce o ejerció un cargo → coronel (de Túpac Amaru) (sujeto elíptico resuelto por el anotador)
    «Comisionado por este y no coronel como expone en su certificación»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: YSIDRO CANO / PEDRO DE LA MATA; responde a A-UT01-001
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-005: fecha u hora del hecho → a media noche
    «se alzaron a media noche armados con garrotes para acabar con este, y hacer matalo de los españoles poniendo guardias a las puertas de estos no le cons ta al que declara si no porque se lo dijo su segundo sargento Santiago Casorla»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: YSIDRO CANO / PEDRO DE LA MATA; responde a A-UT01-003; según lo que le dijo «Santiago Casorla» (discurso referido)
    Fundamento invocado: de oídas; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT12a-001: motivo o causa del hecho → este fue a su casa suplicandole
    «dijo que la dado porque este fue a su casa supli candole»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: YSIDRO CANO / PEDRO DE LA MATA
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT12.a, folio no consta en la transcripción
AFIRMACIÓN A-UT12a-002 [NIEGA]: le comprenden (o no) las generales de la ley → le comprenden los Generales de la Ley
    «que no le comprenden. los Generales de la Ley»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: YSIDRO CANO / PEDRO DE LA MATA
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT12.a, folio no consta en la transcripción

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Isidro Cano, sargento de milicias, vecino español de Tinta» — creencia: probable; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT01-001 mencion/M-UT01-006 mencion/M-UT11-001 mencion/M-UT12.a-001
    Argumento: En su declaración (P18) reconoce como propia la firma de la certificación P01.
```

## PC09

```text
PREGUNTA: ¿Fue Andrés Chuquitapa coronel de Túpac Amaru en la rebelión?
RESPUESTA (DISPUTA): Está en disputa («coronel (de Túpac Amaru)»). Lo afirman: «Isidro Cano» [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción] (certificación P01, UT01); «Fernando Orue» [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción] (certificación P04, UT03); «fernando ore» [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción] (declaración jurada P21, UT14). Lo niegan: «Ysidro Cano» [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción] (declaración jurada P18, UT11).

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT01-001: ejerce o ejerció un cargo → coronel (de Túpac Amaru) (sujeto elíptico resuelto por el anotador)
    «lo mismo en el tiempo del rebelde. Tupa Amaro fue complice y coronel»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT03-001: ejerce o ejerció un cargo → coronel (de Túpac Amaru)
    «en tiempo de su pariente Tupaamaro fue coronel, comecionado»
    Afirmante: «Fernando Orue» (certificante) [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción]; certificación P04, sin fecha escrita; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Fernando Orue
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT03, folio no consta en la transcripción
AFIRMACIÓN A-UT11-004 [NIEGA]: ejerce o ejerció un cargo → coronel (de Túpac Amaru) (sujeto elíptico resuelto por el anotador)
    «Comisionado por este y no coronel como expone en su certificación»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: YSIDRO CANO / PEDRO DE LA MATA; responde a A-UT01-001
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT14-006: ejerce o ejerció un cargo → coronel (de Túpac Amaru)
    «con motibo de saber q de andres chuquitaza fue en tiempo del rebelde tupa-amaru coronel y comisionado»
    Afirmante: «fernando ore» (declarante) [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción]; declaración jurada P21, fecha escrita «Seguidamente»; ante: el grl. sub delegado; redacta: no consta; firma la pieza: no consta; responde a A-UT03-001
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT14, folio no consta en la transcripción

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Andrés Chuquitapa, cacique y recaudador de tributos de Tinta» — creencia: probable; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT01-003 mencion/M-UT01-004 mencion/M-UT03-002 mencion/M-UT05-002 mencion/M-UT06-001 mencion/M-UT07-001 mencion/M-UT14-002 mencion/M-UT15-002 mencion/M-UT16b-001 mencion/M-UT17-006
    Argumento: Todas las menciones designan al cacique o recaudador de Tinta contra quien se dirige la queja; las grafías (Chuquiitapa, Chuquitapa, chuquitaza, chuquitapa) difieren en una o dos letras y aparecen en el mismo contexto procesal. No se incluye «Chiquitas» (ver R-chiquitas).

Afirmaciones relacionadas (no forman la disputa):
  A-UT01-002: «Isidro Cano» [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción] (certificación P01, UT01) → cómplice (de Túpac Amaru) (afirma) «lo mismo en el tiempo del rebelde. Tupa Amaro fue complice y coronel»
  A-UT03-002: «Fernando Orue» [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción] (certificación P04, UT03) → comisionado (de Túpac Amaru) (afirma) «en tiempo de su pariente Tupaamaro fue coronel, comecionado»
  A-UT05-001: «Manuel Huancachoque» [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción] (petición P06, UT05) → recaudador de tributos (afirma) «tenia ocultos el recaudaderor Don Andres Choquitapa»
  A-UT07-001: «Gómez del Rio» [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción] (vista fiscal P07, UT07) → recaudador de tributos (afirma) «contra el Recaudador de Tributos Son Andres Chuquitapa»
  A-UT11-003: «Ysidro Cano» [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción] (declaración jurada P18, UT11) → comisionado (de Túpac Amaru) (afirma) «en tiempo del rebelde Tupa amaro fue Comisionado por este»
  A-UT14-007: «fernando ore» [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción] (declaración jurada P21, UT14) → comisionado (de Túpac Amaru) (afirma) «con motibo de saber q de andres chuquitaza fue en tiempo del rebelde tupa-amaru coronel y comisionado»
  A-UT16b-001: «parroco interino» [= Agustín Valdés, cura interino de Tinta, según reconstrucción] (informe P23, UT16.b) → cacique (afirma) «su casique y alcalde mayor Don Andres Chuquitapa»
  A-UT16b-002: «parroco interino» [= Agustín Valdés, cura interino de Tinta, según reconstrucción] (informe P23, UT16.b) → alcalde mayor (de indios) (afirma) «su casique y alcalde mayor Don Andres Chuquitapa»
  A-UT17-003: «Pedro de la Mata» [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción] (informe P27, UT17) → recaudador de tributos (afirma) «recaudador de tributos de los Ayllus Tinta y Ucho Don Andres Chuquitapa»
Ninguna actuación de fuerza dictaminadora o resolutiva se pronuncia sobre este punto.
```

## PC10

```text
PREGUNTA: ¿Quién redactó las certificaciones de agosto?
RESPUESTA (DISPUTA): Está en disputa en 4 piezas (P01, P03, P04, P05): el subdelegado atribuye la redacción al propio denunciante; los declarantes, a Simón Arce o a un hijo del declarante.

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT12b-002: redactó la pieza → Simon Arce
    «mando el que declara a Simon Arce que pusiere en un papelito lo mis mo que relata en la citada certificación»
    Afirmante: «Mariano Casorla» (declarante) [= El declarante de P19 es un Mariano Casorla distinto de Martín (hipótesis B) | El declarante de P19 es Martín Cazorla (hipótesis A), según reconstrucción]; declaración jurada P19, fecha escrita «Ynmediatamente»; ante: ante mi; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT12.b, folio 20
AFIRMACIÓN A-UT14-002: redactó la pieza → un hijo suyo
    «bajo a un hijo suyo q la pusieron»
    Afirmante: «fernando ore» (declarante) [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción]; declaración jurada P21, fecha escrita «Seguidamente»; ante: el grl. sub delegado; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT14, folio no consta en la transcripción
AFIRMACIÓN A-UT14-003: redactó la pieza → guasscachoque
    «como ha puesto guasscachoque en la citada certificacion»
    Afirmante: «fernando ore» (declarante) [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción]; declaración jurada P21, fecha escrita «Seguidamente»; ante: el grl. sub delegado; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT14, folio no consta en la transcripción
AFIRMACIÓN A-UT17-101: redactó la pieza → Guancachoque
    «fueron hechos por el mismo Guancachoque haciéndolos firmar a los sujetos que los subscriben sin saber lo mas de sus contenidos»
    Afirmante: «Pedro de la Mata» (informante) [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; informe P27, fecha escrita «Siquani Noviembre 8 de 1806»; ante: no consta; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: resulta de lo actuado; fuerza institucional: informativa; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT17-102: redactó la pieza → Guancachoque
    «fueron hechos por el mismo Guancachoque haciéndolos firmar a los sujetos que los subscriben sin saber lo mas de sus contenidos»
    Afirmante: «Pedro de la Mata» (informante) [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; informe P27, fecha escrita «Siquani Noviembre 8 de 1806»; ante: no consta; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: resulta de lo actuado; fuerza institucional: informativa; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT17-103: redactó la pieza → Guancachoque
    «fueron hechos por el mismo Guancachoque haciéndolos firmar a los sujetos que los subscriben sin saber lo mas de sus contenidos»
    Afirmante: «Pedro de la Mata» (informante) [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; informe P27, fecha escrita «Siquani Noviembre 8 de 1806»; ante: no consta; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: resulta de lo actuado; fuerza institucional: informativa; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT17-104: redactó la pieza → Guancachoque
    «fueron hechos por el mismo Guancachoque haciéndolos firmar a los sujetos que los subscriben sin saber lo mas de sus contenidos»
    Afirmante: «Pedro de la Mata» (informante) [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; informe P27, fecha escrita «Siquani Noviembre 8 de 1806»; ante: no consta; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: resulta de lo actuado; fuerza institucional: informativa; UT17, folio no consta en la transcripción

Disputa texto/afirmación: la pieza P04 muestra la firma «Fernando Orue» (M-UT03-004), y A-UT14-001 («fernando ore») lo niega: «no obstante que sabe firmar el declarante no quiso hacerlo»
```

## PC11

```text
PREGUNTA: ¿Cuánto tiempo estuvo preso Huancachoque?
RESPUESTA (DISPUTA): Está en disputa por valores incompatibles. «dos días»: lo afirman «Manuel Huancachoque» [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción] (petición P06, UT06) || «esa misma noche ... al otro dia por la tarde»: lo afirman «Pedro de la Mata» [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción] (informe P27, UT18)

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT06-001: duración del hecho → dos días
    «yo me mantuve dos días preso»
    Afirmante: «Manuel Huancachoque» (denunciante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; petición P06, fecha escrita «CUSCO AGOSTO 22 DE 1806»; ante: no consta; redacta: no consta; firma la pieza: MANUEL HUANCACHOQQUE
    Fundamento invocado: lo padeció o hizo él mismo; fuerza institucional: alegación de parte; UT06, folio no consta en la transcripción
AFIRMACIÓN A-UT18-001: duración del hecho → esa misma noche ... al otro dia por la tarde
    «que lo guardasen en ella esa misma noche, al que puse en libertad al otro dia por la tarde»
    Afirmante: «Pedro de la Mata» (informante) [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; informe P27, fecha escrita «Siquani Noviembre 8 de 1806»; ante: no consta; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: lo padeció o hizo él mismo; fuerza institucional: informativa; UT18, folio no consta en la transcripción

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Prisión de Huancachoque en la cárcel de Tinta tras la denuncia» — creencia: verdadero; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: hecho/H-p06-prision hecho/H-p27-prision
    Argumento: La afirman el denunciante y el subdelegado que la ordenó; discrepan en la duración (PC11), no en el hecho.
```

## PC12

```text
PREGUNTA: ¿Se sacó finalmente a Huancachoque de la matrícula de tributarios?
RESPUESTA (NC): El expediente no lo dice: ninguna afirmación dictaminadora o resolutiva se pronuncia sobre su condición tributaria ni sobre la matrícula; la petición se desglosó al expediente de la primera denuncia (P14–P15).

Pieza P15: Nota de desglose de las dos fojas de denuncia — fecha escrita «Tinta 23. de Septiembre de 1806»
Advertencia: «no lo dice» vale en la medida en que la extracción de afirmaciones resolutivas sea exhaustiva (exhaustividad medida contra el estándar de oro, docs/G_evaluacion.md).
```

## PC13

```text
PREGUNTA: ¿Qué castigo concreto se ejecutó contra Huancachoque tras el auto del 26 de noviembre?
RESPUESTA (NC): El expediente no lo dice: consta la orden de «contener los excesos», no su ejecución. Una orden no implica su cumplimiento (tes:atributo/ordena).

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT19-003: ordena o manda → contener los excesos y enemistad del yndio Guancachoque
    «a fin de contener los excesos y enemistad del yndio Guancachoque»
    Afirmante: «Muñoz» (autoridad que resuelve); auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
```

## PC14

```text
PREGUNTA: ¿A qué hora fue el alboroto ante la cárcel y cuántos indios participaron?
RESPUESTA (DISPUTA): Está en disputa por valores incompatibles. «a las dies de la noche»: nadie lo afirma; lo niegan «fernando ore» [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción] (declaración jurada P21, UT14) || «a las dies o a las once»: lo afirman «don Juan Quiñones» [= «Don Juan Quiñones», teniente alguacil (existencia en disputa), según reconstrucción] (certificación P03, UT02) || «a las diez de la noche»: lo afirman «Fernando Orue» [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción] (certificación P04, UT03) || «a las nueve de la noche»: lo afirman «Manuel Huancachoque» [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción] (petición P06, UT06) || «a media noche»: lo afirman «Isidro Cano» [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción] (certificación P01, UT01); «Ysidro Cano» [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción] (declaración jurada P18, UT11) || «el primer puesto del gallo»: lo afirman «fernando ore» [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción] (declaración jurada P21, UT14)

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT01-003: fecha u hora del hecho → a media noche
    «esa noche todos los indios se alzaron a media noche todos con garrotes»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT02-001: fecha u hora del hecho → a las dies o a las once
    «Esa misma noche a las dies o a las once se alzaron los indios en la plaza»
    Afirmante: «don Juan Quiñones» (certificante) [= «Don Juan Quiñones», teniente alguacil (existencia en disputa), según reconstrucción]; certificación P03, sin fecha escrita; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Juan Cazorla
    Fundamento invocado: lo vio; fuerza institucional: testimonial; UT02, folio no consta en la transcripción
AFIRMACIÓN A-UT03-004: fecha u hora del hecho → a las diez de la noche
    «a las diez de la noche, peor alboroto»
    Afirmante: «Fernando Orue» (certificante) [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción]; certificación P04, sin fecha escrita; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Fernando Orue
    Fundamento invocado: lo vio; fuerza institucional: testimonial; UT03, folio no consta en la transcripción
AFIRMACIÓN A-UT06-002: fecha u hora del hecho → a las nueve de la noche
    «pero a las nueve de la noche se apareció una caterva de indios»
    Afirmante: «Manuel Huancachoque» (denunciante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; petición P06, fecha escrita «CUSCO AGOSTO 22 DE 1806»; ante: no consta; redacta: no consta; firma la pieza: MANUEL HUANCACHOQQUE
    Fundamento invocado: lo padeció o hizo él mismo; fuerza institucional: alegación de parte; UT06, folio no consta en la transcripción
AFIRMACIÓN A-UT11-005: fecha u hora del hecho → a media noche
    «se alzaron a media noche armados con garrotes para acabar con este, y hacer matalo de los españoles poniendo guardias a las puertas de estos no le cons ta al que declara si no porque se lo dijo su segundo sargento Santiago Casorla»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: YSIDRO CANO / PEDRO DE LA MATA; responde a A-UT01-003; según lo que le dijo «Santiago Casorla» (discurso referido)
    Fundamento invocado: de oídas; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT14-004: fecha u hora del hecho → el primer puesto del gallo
    «no fue a las dies de la noche como ha puesto guasscachoque en la citada certificacion, sino el primer puesto del gallo»
    Afirmante: «fernando ore» (declarante) [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción]; declaración jurada P21, fecha escrita «Seguidamente»; ante: el grl. sub delegado; redacta: no consta; firma la pieza: no consta; responde a A-UT03-004
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT14, folio no consta en la transcripción
AFIRMACIÓN A-UT14-005 [NIEGA]: fecha u hora del hecho → a las dies de la noche
    «no fue a las dies de la noche como ha puesto guasscachoque en la citada certificacion»
    Afirmante: «fernando ore» (declarante) [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción]; declaración jurada P21, fecha escrita «Seguidamente»; ante: el grl. sub delegado; redacta: no consta; firma la pieza: no consta; responde a A-UT03-004
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT14, folio no consta en la transcripción
AFIRMACIÓN A-UT12b-006: número de participantes → quatro o seis Yndios
    «vio a quatro o seis Yndios en la puerta de la carcel con garrotes»
    Afirmante: «Mariano Casorla» (declarante) [= El declarante de P19 es un Mariano Casorla distinto de Martín (hipótesis B) | El declarante de P19 es Martín Cazorla (hipótesis A), según reconstrucción]; declaración jurada P19, fecha escrita «Ynmediatamente»; ante: ante mi; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: lo vio; fuerza institucional: testimonial; UT12.b, folio 20

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Alboroto de indios ante la cárcel de Tinta la noche de la prisión de Huancachoque» — creencia: probable; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: hecho/H-p01-alboroto hecho/H-p03-alboroto hecho/H-p04-alboroto hecho/H-p06-alboroto hecho/H-p18-alboroto hecho/H-p19-alboroto hecho/H-p21-alboroto
    Argumento: Siete relatos sitúan el hecho la noche de la prisión del denunciante ante la cárcel o en la plaza. Discrepan en la hora y en el número de participantes (ver PC14), pero no en que ocurrió algo; incluso el declarante de P19 dice haber visto «quatro o seis Yndios … con garrotes».
```

## PC15

```text
PREGUNTA: PC15
RESPUESTA (PENDIENTE): Requiere anotar receptor, escribano y firmantes de todas las actuaciones.
```

## PC16

```text
PREGUNTA: ¿Qué resolvió la autoridad sobre la queja y en qué se apoyó?
RESPUESTA (A): Son afirmaciones con fuerza dictaminadora o resolutiva, no hechos: el fiscal califica las quejas de «menos conforme a la verdad» y el auto se conforma con la vista fiscal; ambas se apoyan en el informe del subdelegado (parte en la prisión del denunciante).

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT07-001: ejerce o ejerció un cargo → recaudador de tributos
    «contra el Recaudador de Tributos Son Andres Chuquitapa»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT17-001: firmó la pieza → Juan Cazorla
    «Juan Cazorla de quien aparece firmada la Certificación a folios 2»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P24, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT17-002 [NIEGA]: existe tal persona en el lugar → en el pueblo de Tinta
    «que no hay tal hombre en el pueblo de Tinta»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P24, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT17-004: la pieza está en tal folio (autorreferencia del expediente) → a folios 2
    «la Certificación a folios 2 extendida a nombre del teniente Alguacil»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P24, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT19-003: ordena o manda → contener los excesos y enemistad del yndio Guancachoque
    «a fin de contener los excesos y enemistad del yndio Guancachoque»
    Afirmante: «Muñoz» (autoridad que resuelve); auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-004: se conforma con (adopta) un dictamen → P29
    «Visto de conformidad con lo supuesto por el señor Fiscal»
    Afirmante: «Muñoz» (autoridad que resuelve); auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-001: veracidad de un escrito o queja → menos conforme a la verdad
    «resultando de este ser menos conforme a la verdad las quejas dadas por Manuel Guancoichoque»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-002: calificación de conducta o carácter → mala conducta y genio discolo y arreva
    «por la mala conducta y genio discolo y arreva que se nota»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT19, folio 33
```

## PC17

```text
PREGUNTA: ¿Qué condición fiscal y social se atribuye a Huancachoque y quién la atribuye?
RESPUESTA (A): 6 atribuciones, cada una de quien la hace (ninguna es un hecho).

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT05-003: tiene una condición → originario
    «Manuel Huancachoque Indio originario y vecino del pueblo de Tinta»
    Afirmante: «Manuel Huancachoque» (denunciante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; petición P06, fecha escrita «CUSCO AGOSTO 22 DE 1806»; ante: no consta; redacta: no consta; firma la pieza: MANUEL HUANCACHOQQUE
    Fundamento invocado: no lo indica; fuerza institucional: alegación de parte; UT05, folio no consta en la transcripción
AFIRMACIÓN A-UT06-004: tiene una condición → miliciano
    «por haber estado empleado en las milicias de aquella provincia, hasta aquí no había tributado»
    Afirmante: «Manuel Huancachoque» (denunciante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; petición P06, fecha escrita «CUSCO AGOSTO 22 DE 1806»; ante: no consta; redacta: no consta; firma la pieza: MANUEL HUANCACHOQQUE
    Fundamento invocado: no lo indica; fuerza institucional: alegación de parte; UT06, folio no consta en la transcripción
AFIRMACIÓN A-UT06-005: tiene una condición → tributario
    «conseguido también el que se me matricule»
    Afirmante: «Manuel Huancachoque» (denunciante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; petición P06, fecha escrita «CUSCO AGOSTO 22 DE 1806»; ante: no consta; redacta: no consta; firma la pieza: MANUEL HUANCACHOQQUE
    Fundamento invocado: no lo indica; fuerza institucional: alegación de parte; UT06, folio no consta en la transcripción
AFIRMACIÓN A-UT02-002: ejerce o ejerció un cargo → soldado
    «Manuel Guamanchoque ha estado soldado en mi compañía más de cinco años»
    Afirmante: «yo sargento primero» (certificante); certificación P02, fecha escrita «agosto cinco de mil ochocientos seis años»; ante: no consta; redacta: no consta; firma la pieza: Santiago Cazorla
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT02, folio no consta en la transcripción
AFIRMACIÓN A-UT16a-001: es hijo/a de → Antolin Ortiz
    «Es notorio que Manuel Guancachoque es hijo Espurio de Antolin Ortiz»
    Afirmante: «parroco interino» (informante) [= Agustín Valdés, cura interino de Tinta, según reconstrucción]; informe P23, fecha escrita «Noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: notoriedad; fuerza institucional: informativa; UT16.a, folio no consta en la transcripción
AFIRMACIÓN A-UT16a-004: es hijo/a de → Agustina Falcon
    «su Madre Agustina Falcon India Ordinaria y pleveya»
    Afirmante: «parroco interino» (informante) [= Agustín Valdés, cura interino de Tinta, según reconstrucción]; informe P23, fecha escrita «Noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: notoriedad; fuerza institucional: informativa; UT16.a, folio no consta en la transcripción

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Manuel Huancachoque (Guancachoque), denunciante» — creencia: probable; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT01-002 mencion/M-UT02-003 mencion/M-UT05-001 mencion/M-UT06-002 mencion/M-UT14-003 mencion/M-UT16a-001 mencion/M-UT17-004 mencion/M-UT17-005 mencion/M-UT19-001
    Argumento: Menciones del denunciante en las certificaciones, su escrito, su firma, la declaración de Orue, los informes y la vista fiscal. «Manuel Guamanchoque» (P02) se incluye por el nombre de pila y porque la certificación de su servicio militar coincide con lo que alega en su escrito (no había tributado por servir en las milicias).
```

## PC18

```text
PREGUNTA: ¿Qué cargos ejercía Andrés Chuquitapa, con qué vigencia y según quién?
RESPUESTA (R): 5 afirmaciones de cargo (capa 3) y 3 ejercicios de cargo reconstruidos (capa 4). Los cargos en la rebelión de 1780 están en PC09.

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT05-001: ejerce o ejerció un cargo → recaudador de tributos
    «tenia ocultos el recaudaderor Don Andres Choquitapa»
    Afirmante: «Manuel Huancachoque» (denunciante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; petición P06, fecha escrita «CUSCO AGOSTO 22 DE 1806»; ante: no consta; redacta: no consta; firma la pieza: MANUEL HUANCACHOQQUE
    Fundamento invocado: no lo indica; fuerza institucional: alegación de parte; UT05, folio no consta en la transcripción
AFIRMACIÓN A-UT07-001: ejerce o ejerció un cargo → recaudador de tributos
    «contra el Recaudador de Tributos Son Andres Chuquitapa»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT16b-001: ejerce o ejerció un cargo → cacique
    «su casique y alcalde mayor Don Andres Chuquitapa»
    Afirmante: «parroco interino» (informante) [= Agustín Valdés, cura interino de Tinta, según reconstrucción]; informe P23, fecha escrita «Noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: no lo indica; fuerza institucional: informativa; UT16.b, folio 28
AFIRMACIÓN A-UT16b-002: ejerce o ejerció un cargo → alcalde mayor (de indios)
    «su casique y alcalde mayor Don Andres Chuquitapa»
    Afirmante: «parroco interino» (informante) [= Agustín Valdés, cura interino de Tinta, según reconstrucción]; informe P23, fecha escrita «Noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: no lo indica; fuerza institucional: informativa; UT16.b, folio 28
AFIRMACIÓN A-UT17-003: ejerce o ejerció un cargo → recaudador de tributos
    «recaudador de tributos de los Ayllus Tinta y Ucho Don Andres Chuquitapa»
    Afirmante: «Pedro de la Mata» (informante) [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; informe P27, fecha escrita «Siquani Noviembre 8 de 1806»; ante: no consta; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: no lo indica; fuerza institucional: informativa; UT17, folio no consta en la transcripción

  EJERCICIO DE CARGO (capa 4): alcalde mayor (de indios) — vigencia: 1806-01-01 a 1806-12-31 (Consta en 1806 por una sola fuente.); creencia: posible; premisas: A-UT16b-002
  EJERCICIO DE CARGO (capa 4): cacique — vigencia: 1806-01-01 a 1806-12-31 (Consta en 1806 (informe del cura; carátula, no anotada). Las certificaciones lo sitúan ya como cacique en tiempos del corregidor Reparaz (afirmación de testigos, no anotada).); creencia: probable; premisas: A-UT16b-001
  EJERCICIO DE CARGO (capa 4): recaudador de tributos — vigencia: 1806-08-01 a 1806-11-30 (Consta en ejercicio de agosto a noviembre de 1806; el inicio no consta en el expediente.); creencia: verdadero; premisas: A-UT05-001 A-UT07-001 A-UT17-003
```

## PC19

```text
PREGUNTA: ¿Son la misma persona «Mariano Casorla» (declarante) y «Martin Cazorla» (certificante)?
RESPUESTA (R): Hay 2 reconstrucciones en competencia; ninguna se impone en el grafo: «El declarante de P19 es Martín Cazorla (hipótesis A)» (probable); «El declarante de P19 es un Mariano Casorla distinto de Martín (hipótesis B)» (posible).

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «El declarante de P19 es Martín Cazorla (hipótesis A)» — creencia: probable; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT04-001 mencion/M-UT04-002 mencion/M-UT12.a-005 mencion/M-UT12.a-006
    Argumento: Al declarante se le muestra «la certificación De folio 4 su firma Martin casorla» y habla de ella en primera persona: mandó a Simón Arce ponerla por escrito, no sabe escribir, y en tiempos del Rebelde «era muchacho» (28 años en 1806, unos 2 en 1780). La denominación «Gobernador Señor Don Mariano Casorla» puede ser un error del escribano o de la transcripción. Compite con R-declarante-p19-es-mariano.
RECONSTRUCCIÓN «El declarante de P19 es un Mariano Casorla distinto de Martín (hipótesis B)» — creencia: posible; autor: claude-opus-5-5; fecha: 2026-11-12
    Deriva de: mencion/M-UT12.a-005
    Argumento: La transcripción lo llama «el Gobernador Señor Don Mariano Casorla». Si fuera otra persona, el expediente no recogería la declaración de Martín Cazorla, pero el declarante habla de la certificación como propia. Se mantiene como alternativa hasta cotejar la imagen.

Mención afectada: https://w3id.org/laad/id/cc-14-18/mencion/M-UT12.a-005
```

## PC20

```text
PREGUNTA: ¿De dónde procede el dato A-UT11-004?
RESPUESTA (P): Procedencia del dato (PROV-O), no del testimonio de 1806.

  grafo https://w3id.org/laad/grafo/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-12T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-12T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-12T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-12T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-12T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-12T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-12T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-12T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-12T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-12T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-12T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-12T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-12T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-12T00:00:00, validación humana: NO REGISTRADA
```
