# Respuestas del grafo a las preguntas de competencia

> Generado por `scripts/responder_pc.py` a partir de `datos/grafo/*.trig` (expediente piloto: `cc-14-18`). No editar a mano.

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
RESPUESTA (D): El expediente se refiere a sus propias fojas; esa foliación es una afirmación del documento, no una marca del transcriptor. P06 → «de folio»; un expediente → «En folio 10»; Expediente → «en folio 10»; P06 → «al fin de el en folio 2»; P05 → «De folio 4»; P03 → «a folios 2». En la transcripción esas piezas no tienen marca de folio (folio no consta).

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT08-219: la pieza está en tal folio (autorreferencia del expediente) → de folio
    «leído se le su escrito de folio dijo»
    Afirmante: «Escribano mayor de Gobierno» (fedatario) [= «el presente Escribano mayor de Gobierno» que da fe en P09 es el escribano Chacón, según reconstrucción]; reconocimiento y ratificación P09, fecha escrita «en trece días del mees de Agosto de mil ochocientos seis años»; ante: Don Manuel Galeano; redacta: no consta; firma la pieza: Don Valencia / Galeano / Juan Clemente Jordan / Manuel Guancachoque / Marcos Salcedo
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT08, folio no consta en la transcripción
AFIRMACIÓN A-UT09-517: la pieza está en tal folio (autorreferencia del expediente) → En folio 10
    «En folio 10 remito a vuestra Merced un expediente»
    Afirmante: «Ruiz de Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; oficio P13, fecha escrita «Cusco y Agosto 28 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Ruiz de Castilla
    Fundamento invocado: no lo indica; fuerza institucional: informativa; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT10-501: la pieza está en tal folio (autorreferencia del expediente) → en folio 10
    «con el Expediente en folio 10 que la acompaña»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-502: la pieza está en tal folio (autorreferencia del expediente) → al fin de el en folio 2
    «la denuncia que se halla al fin de el en folio 2»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT12a-003: la pieza está en tal folio (autorreferencia del expediente) → De folio 4
    «De folio 4 su firma Martin casorla»
    Afirmante: «ante mi» (fedatario) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; declaración jurada P19, fecha escrita «Ynmediatamente»; ante: ante mi; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT12.a, folio no consta en la transcripción
AFIRMACIÓN A-UT17-004: la pieza está en tal folio (autorreferencia del expediente) → a folios 2
    «la Certificación a folios 2 extendida a nombre del teniente Alguacil»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la nota del transcriptor «[Media rúbrica]» y no nombra a ninguna María | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P24, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
```

## PC03

```text
PREGUNTA: ¿Qué otros expedientes del Tomo I mencionan a Andrés Chuquitapa, a Manuel Guancachoque o al pueblo de Tinta, según el catálogo?
RESPUESTA (A): Según el catálogo, Chuquitapa y Guancachoque solo constan en CCc 14 (18) (0 otras fichas los nombran); 3 otras fichas nombran el «pueblo de Tinta» y 55 más nombran Tinta en otro sentido.

Respuesta según el catálogo del ARC (afirmaciones de los catalogadores, no hechos del modelo), extraída de la capa de texto del PDF sin cotejo de imágenes; la pertinencia la marcó el extractor (nota con motivo y dudas).

Índices del catálogo:
  Índice Onomástico: entrada (pp. impresas 493; pp. del PDF 496): «Chuquitapa Andrés: CCc 14 (18)» — entrada de índice
  Índice Onomástico: entrada (pp. impresas 502; pp. del PDF 505): «Guancachoque, Manuel: CCc 14 (18)» — entrada de índice
  Índice Toponímico: entrada (pp. impresas 542, 543; pp. del PDF 545, 546): «Tinta : COc 2 (8); 3 (1); 10 (9); 16 (10); 21 (6), (25); 23 (10); 26 (19); 33 (24); 36 (4); 39 (25); 55 (24); 56 (32); 59 (2); 59 (27); 63 (9); 65 (3); 66 (7); 67 (16); 67 (32); 67 (39); 69 (15); 73 (01); 76 (04); 88 (25); 90 (5), (7), (10), (31); 91 (13); 93 (37), (42); : COp 1 (17); 2 (6),(21); 3 (2), (13); 4 (14); 14 (27); : CCC, 14 (18); 19 (24); 20 (12); CCP, 2 (2), (3), (5); doctrina: COc 1 (13); 26 (18); partido: COc 51 (28); 54 (15); 74 (23); 93 (37); CCc 6 (30); pueblo: COc 1 (13)» — entrada de índice

Fichas que nombran «pueblo de Tinta» (otros expedientes):
  Ficha del catálogo CCc 19 (24) (pp. impresas 462; pp. del PDF 465): «Expediente 24. Años: 1820-1825. Doña María Mercedes Rodríguez, vecina del pueblo de Tinta, contra Don Vicente Berros y Villarrica con tropa de soldados, quienes por orden del alcalde ordinario de españoles le mando a su conducción al pueblo de Sicuani y en caso oponerse pagar 12 pesos a cada uno y estando en la pobreza le quitaron los pocos bienes que tenía llevándola al calabozo. Folios: 9.» — PC03: menciona Tinta; calificador(es): pueblo
  Ficha del catálogo COc 1 (13) (pp. impresas 16; pp. del PDF 19): «Expediente 13. Años: 1784-1821. Don Miguel Paiva, quien es administrador general de reales rentas menciona que en la doctrina de Tinta existen dos haciendas nombradas Talle y Chachacure con molinos para sus productos. Siendo repartidas por los indios del Pueblo de Tinta y Combapata, dichas tierras donadas por don Antonio García Valdez, se presentan diferentes documentos en favor de los indios. Folios: 197» — PC03: menciona Tinta; calificador(es): doctrina; pueblo
  Ficha del catálogo COc 3 (1) (pp. impresas 20; pp. del PDF 23): «Expediente 1. Años: 1785-1786. Don Juan Antonio de Figueroa, sargento mayor, recibió la cantidad de 13000 pesos de a 8 reales por parte de Doña María Ana de Altolaguirre Elorduy, dinero destinado para la construcción de tres puentes en los pueblos de Tinta, Yauri y Checa, tras la muerte del capitán don Juan Antonio Reparaz. Dicho Juan Antonio de Figueroa acepta que recibió el dinero e hipotecó la hacienda de Quipococha, situada en el partido de Quispicanchis. Folios 85.» — PC03: menciona Tinta; calificador(es): pueblo

Otras 55 fichas nombran Tinta como partido, provincia, doctrina o regimiento (no consta que se refieran al pueblo):
  Ficha del catálogo CCc 20 (12)
  Ficha del catálogo CCc 6 (30)
  Ficha del catálogo CCp 2 (2)
  Ficha del catálogo CCp 2 (3)
  Ficha del catálogo CCp 2 (5)
  Ficha del catálogo COc 10 (9)
  Ficha del catálogo COc 16 (10)
  Ficha del catálogo COc 17 (4)
  Ficha del catálogo COc 2 (8)
  Ficha del catálogo COc 21 (25)
  Ficha del catálogo COc 21 (6)
  Ficha del catálogo COc 23 (10)
  Ficha del catálogo COc 25 (19)
  Ficha del catálogo COc 26 (18)
  Ficha del catálogo COc 26 (19)
  Ficha del catálogo COc 29 (22)
  Ficha del catálogo COc 33 (24)
  Ficha del catálogo COc 36 (4)
  Ficha del catálogo COc 39 (25)
  Ficha del catálogo COc 42 (37)
  Ficha del catálogo COc 43 (10)
  Ficha del catálogo COc 51 (28)
  Ficha del catálogo COc 54 (15)
  Ficha del catálogo COc 55 (24)
  Ficha del catálogo COc 56 (32)
  Ficha del catálogo COc 57 (38)
  Ficha del catálogo COc 59 (2)
  Ficha del catálogo COc 59 (27)
  Ficha del catálogo COc 63 (9)
  Ficha del catálogo COc 65 (3)
  Ficha del catálogo COc 66 (7)
  Ficha del catálogo COc 67 (16)
  Ficha del catálogo COc 67 (32)
  Ficha del catálogo COc 67 (39)
  Ficha del catálogo COc 69 (15)
  Ficha del catálogo COc 73 (1)
  Ficha del catálogo COc 74 (23)
  Ficha del catálogo COc 76 (4)
  Ficha del catálogo COc 88 (25)
  Ficha del catálogo COc 90 (10)
  Ficha del catálogo COc 90 (31)
  Ficha del catálogo COc 90 (5)
  Ficha del catálogo COc 90 (7)
  Ficha del catálogo COc 90 (8)
  Ficha del catálogo COc 90 (9)
  Ficha del catálogo COc 91 (13)
  Ficha del catálogo COc 93 (37)
  Ficha del catálogo COc 93 (42)
  Ficha del catálogo COp 1 (17)
  Ficha del catálogo COp 14 (27)
  Ficha del catálogo COp 2 (21)
  Ficha del catálogo COp 2 (6)
  Ficha del catálogo COp 3 (13)
  Ficha del catálogo COp 3 (2)
  Ficha del catálogo COp 4 (14)
```

## PC04

```text
PREGUNTA: En Causas Criminales, ¿qué expedientes de 1805–1807 tienen como demandado a un cacique, recaudador o alcalde de indios, según la ficha?
RESPUESTA (A): Según el catálogo: 2 seguros (CCc 14 (18), CCc 14 (21)) y 3 dudosos.

Respuesta según el catálogo del ARC (afirmaciones de los catalogadores, no hechos del modelo), extraída de la capa de texto del PDF sin cotejo de imágenes; la pertinencia la marcó el extractor (nota con motivo y dudas).

Seguros (la ficha nombra el cargo del demandado):
  Ficha del catálogo CCc 14 (18) (pp. impresas 435, 436; pp. del PDF 438, 439): «Expediente 18. Año: 1806. El indio Manuel Guancachoque, por los maltratos y atropellos por parte del cacique Don Andrés Chuquitapa, hecho que sucedió en el pueblo de Tinta. El expediente inicia con dos cartas de testigos, uno es de Juan Casola quien está a favor del indio y otro es de Andrés Chuquitapa quien está a favor del cacique, que dice que los indios causan alboroto Folios: 19.» — PC03: menciona «Andrés Chuquitapa»; PC03: menciona «Manuel Guancachoque»; PC03: menciona Tinta; calificador(es): pueblo; PC04 (seguro): Acusado: «el cacique Don Andrés Chuquitapa» (maltratos y atropellos al indio Manuel Guancachoque)
  Ficha del catálogo CCc 14 (21) (pp. impresas 436; pp. del PDF 439): «Expediente 21. Años: 1806-1807. Iniciado por los indios: Fernando Carrasco, Sebastián Paucar, Eusebio Yanqui, Ignacio Huallpa y Francisco Champi, piden una sanción y exigen que se le separe de su cargo de recaudador a Don Agustín Brabo porque este los maltrata, comete excesos, los mencionados ya lo han denunciado con los jueces de su jurisdicción, pero Don Agustín les hace regalos. Folios: 13.» — PC04 (seguro): Acusado: «su cargo de recaudador a Don Agustín Brabo»; los indios piden sanción y separación del cargo

Dudosos (la ficha no dice si el alcalde es de indios):
  Ficha del catálogo CCc 14 (14) (pp. impresas 435; pp. del PDF 438): «Expediente 14. Año: 1806. Don Domingo Gamarra, hacia Don Juan Villafuerte, alcalde de Acomayo, por haberle obligado a entregar 170 ovejas y los fletes de la mula, por ser la autoridad. En el expediente se muestras notas donde se da a conocer los excesos que este tuvo con él, ya que el señor Juan lo tildo de ladrón y este se robó 800 mil pesos junto con Juan de la Torre Cosió. Folios: 4.» — PC04 (dudoso): Acusado: «Don Juan Villafuerte, alcalde de Acomayo» [duda: La ficha no dice si es alcalde de indios, de españoles u ordinario; el tratamiento «Don» no basta para decidir. El mismo Juan Villafuerte es acusado en CCc 14 (5) sin cargo.]
  Ficha del catálogo CCc 14 (22) (pp. impresas 436; pp. del PDF 439): «Expediente 22. Años: 1806-1807. Doña Lorena de la Peña, viuda de Don Mariano Perales contra Miguel Guambo, alcalde de Yanatili, quien recibió la mula robada por Marcos Acero en calidad de embargo, quien no devolvió sino más bien lo oculto sin embargo testigos que informaron que la mula había sido vendida, Lorena de la Peña exige la devolución de su mula o que se le pague los 80 pesos. Folios: 20.» — PC04 (dudoso): Acusado: «Miguel Guambo, alcalde de Yanatili» (retuvo una mula embargada) [duda: La ficha no especifica el tipo de alcaldía; el apellido y la falta de «Don» sugieren alcalde de indios, pero es [inferencia].]
  Ficha del catálogo CCc 15 (5) (pp. impresas 438; pp. del PDF 441): «Expediente 5. Año: 1807. El sargento Evaristo Cortes de Yábar, denuncia a Don Pascual Pareja, alcalde mayor de la parroquia de san Jerónimo, ya que el acusado es acostumbrado a dichas injurias, es por ello que pide que se le aplique la ley y que este sea castigado, para poder ratificar dicha culpa se tomó la declaración a Don pascual. Folios: 9.» — PC04 (dudoso): Acusado: «Don Pascual Pareja, alcalde mayor de la parroquia de san Jerónimo» (injurias) [duda: «Alcalde mayor» de una parroquia de indios del Cusco puede ser cargo indígena, pero la ficha no lo dice; [inferencia].]
```

## PC05

```text
PREGUNTA: ¿Con qué grafías aparece el denunciante y dónde?
RESPUESTA (D): 30 grafías en 62 menciones anotadas: Guancachoque, MANUEL HUANCACHOQQUE, Manuel Guamanchoque, Manuel Guancacho que, Manuel Guancachoque, Manuel Guancoichoque, Manuel Huancachoque, Manuel Mancachoque, Ortis, al suplicante, aquel, denunciante, dicho Guancachoque, dicho denunciante, dicho querello, el citado Guancachoque, el denunciante, el mismo denunciador Guancachoque, el mismo denunciante, el querello, el suplicante, gancahoque, guancachay, guancachoque, guarcachoque, guasscachoque, indio, manuel guancachoque, su feligrés Guancachoque, yndio Guancachoque. (Agrupadas por la reconstrucción R-huancachoque; ver capa 4.)

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Manuel Huancachoque (Guancachoque), denunciante» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT00-201 cc-14-18/mencion/M-UT01-002 cc-14-18/mencion/M-UT01-207 cc-14-18/mencion/M-UT02-003 cc-14-18/mencion/M-UT02-206 cc-14-18/mencion/M-UT02-215 cc-14-18/mencion/M-UT03-205 cc-14-18/mencion/M-UT03-209 cc-14-18/mencion/M-UT04-201 cc-14-18/mencion/M-UT04-209 cc-14-18/mencion/M-UT05-001 cc-14-18/mencion/M-UT06-002 cc-14-18/mencion/M-UT07-204 cc-14-18/mencion/M-UT07-214 cc-14-18/mencion/M-UT07-215 cc-14-18/mencion/M-UT07-216 cc-14-18/mencion/M-UT08-203 cc-14-18/mencion/M-UT08-216 cc-14-18/mencion/M-UT08-231 cc-14-18/mencion/M-UT09-506 cc-14-18/mencion/M-UT09-508 cc-14-18/mencion/M-UT09-511 cc-14-18/mencion/M-UT09-523 cc-14-18/mencion/M-UT09-528 cc-14-18/mencion/M-UT10-505 cc-14-18/mencion/M-UT10-510 cc-14-18/mencion/M-UT10-521 cc-14-18/mencion/M-UT10-522 cc-14-18/mencion/M-UT10-527 cc-14-18/mencion/M-UT10-530 cc-14-18/mencion/M-UT10-533 cc-14-18/mencion/M-UT11-516 cc-14-18/mencion/M-UT11-520 cc-14-18/mencion/M-UT12.a-502 cc-14-18/mencion/M-UT12.b-501 cc-14-18/mencion/M-UT12.b-508 cc-14-18/mencion/M-UT12.b-509 cc-14-18/mencion/M-UT13-504 cc-14-18/mencion/M-UT13-508 cc-14-18/mencion/M-UT13-510 cc-14-18/mencion/M-UT14-003 cc-14-18/mencion/M-UT14-503 cc-14-18/mencion/M-UT14-505 cc-14-18/mencion/M-UT14-512 cc-14-18/mencion/M-UT15-803 cc-14-18/mencion/M-UT15-811 cc-14-18/mencion/M-UT16a-001 cc-14-18/mencion/M-UT16a-801 cc-14-18/mencion/M-UT16a-804 cc-14-18/mencion/M-UT16b-811 cc-14-18/mencion/M-UT16b-813 cc-14-18/mencion/M-UT16b-814 cc-14-18/mencion/M-UT17-004 cc-14-18/mencion/M-UT17-005 cc-14-18/mencion/M-UT17-828 cc-14-18/mencion/M-UT18-804 cc-14-18/mencion/M-UT18-814 cc-14-18/mencion/M-UT18-817 cc-14-18/mencion/M-UT19-001 cc-14-18/mencion/M-UT19-804 cc-14-18/mencion/M-UT19-820 cc-14-18/mencion/M-UT19-821
    Argumento: Menciones del denunciante en la carátula, las certificaciones, su escrito, su firma ante el teniente asesor, los autos y notificaciones, la declaración de Orue («guasscachoque», «guancachay»), los informes y la vista fiscal. El cura lo llama «Ortis o Guancachoque» (P23, UT16.b) tras presentarlo como «hijo Espurio de Antolin Ortiz» (UT16.a): lo designa con el apellido del padre que le atribuye (ver R-huancachoque-alias-ortiz). No se añaden «Maldonado Ortiz» ni «las Guamcachoque» de la frase «la aminocidad y altenencia de Maldonado Ortiz a las Guamcachoque»: la construcción es ambigua (puede nombrar a otra persona o a la familia) y «Maldonado» no se explica en el texto. «Manuel Guamanchoque» (P02) se incluye por el nombre de pila y porque la certificación de su servicio militar coincide con lo que alega en su escrito («por haber estado empleado en las milicias de aquella provincia, hasta aquí no había tributado», UT06); es la única fusión no segura y la que mantiene la reconstrucción en probable. Revisada tras la auditoría I (2026-11-13). Ampliada el 2026-11-14 (claude-fable-5-2): se añaden 34 menciones. Con nombre (grafías Huancachoque, Guancachoque, «Guancacho que», guarcachoque, gancahoque) en las certificaciones P03–P05, las declaraciones P18–P21, el informe del cura, el de Mata, el auto P28 y la vista P29; todas en la misma causa y con los mismos hechos (prisión, denuncia). Designaciones por papel procesal con antecedente expreso en la misma pieza: «dicho denunciante» (P01, tras «al denunciante mayor Guancachoque»; P04, tras «contra Manuel Huancachoque»), «denunciante» (P05, tras «Manuel Huancachoque, denunciante»), «el suplicante» ×3 (P07, tras «el antecedente escrito que le ha presentado Manuel Guancachoque»), «el querello», «dicho querello» y «el denunciante» (P10, auto sobre «su escrito»), «el mismo denunciante» (P14, tras «el Indio Manuel Guancachoque»). Dos anáforas sin nombre: «aquel» de P07 (M-UT07-216: «este y sus parciales … precurado matarlo … estando aquel en la carcel», donde «este» es el recaudador y «aquel» el preso) y «al indio» de P27 (M-UT18-804: «acometieron contra el, de suerte, que si yo no salgo al indio lo hubieran en tropeado … lo mande llevar a la cárcel»). No se añaden «desvalido» (P05, sintaxis ambigua), «las Guamcachoque» ni «Maldonado Ortiz» (P23). Reconstrucción propuesta originalmente por claude-opus-5-5 el 2026-11-13.

  «Manuel Mancachoque» — UT00, pieza P00 (carátula), mención M-UT00-201
  «Guancachoque» — UT01, pieza P01 (certificación), mención M-UT01-002
  «dicho denunciante» — UT01, pieza P01 (certificación), mención M-UT01-207
  «Manuel Guamanchoque» — UT02, pieza P02 (certificación), mención M-UT02-003
  «Manuel Huancachoque» — UT02, pieza P03 (certificación), mención M-UT02-206
  «dicho Guancachoque» — UT02, pieza P03 (certificación), mención M-UT02-215
  «Manuel Huancachoque» — UT03, pieza P04 (certificación), mención M-UT03-205
  «dicho denunciante» — UT03, pieza P04 (certificación), mención M-UT03-209
  «Manuel Huancachoque» — UT04, pieza P05 (certificación), mención M-UT04-201
  «denunciante» — UT04, pieza P05 (certificación), mención M-UT04-209
  «Manuel Huancachoque» — UT05, pieza P06 (petición), mención M-UT05-001
  «MANUEL HUANCACHOQQUE» — UT06, pieza P06 (petición), mención M-UT06-002
  «Manuel Guancachoque» — UT07, pieza P07 (vista fiscal), mención M-UT07-204
  «el suplicante» — UT07, pieza P07 (vista fiscal), mención M-UT07-214
  «al suplicante» — UT07, pieza P07 (vista fiscal), mención M-UT07-215
  «aquel» — UT07, pieza P07 (vista fiscal), mención M-UT07-216
  «el suplicante» — UT08, pieza P07 (vista fiscal), mención M-UT08-203
  «Manuel Guancachoque» — UT08, pieza P09 (reconocimiento y ratificación), mención M-UT08-216
  «Manuel Guancachoque» — UT08, pieza P09 (reconocimiento y ratificación), mención M-UT08-231
  «el querello» — UT09, pieza P10 (auto), mención M-UT09-506
  «dicho querello» — UT09, pieza P10 (auto), mención M-UT09-508
  «el denunciante» — UT09, pieza P10 (auto), mención M-UT09-511
  «Manuel Guancachoque» — UT09, pieza P12 (notificación), mención M-UT09-523
  «Manuel Guancachoque» — UT09, pieza P13 (oficio), mención M-UT09-528
  «Manuel Guancachoque» — UT10, pieza P14 (decreto), mención M-UT10-505
  «el mismo denunciante» — UT10, pieza P14 (decreto), mención M-UT10-510
  «Manuel Guancachoque» — UT10, pieza P14 (decreto), mención M-UT10-521
  «el citado Guancachoque» — UT10, pieza P14 (decreto), mención M-UT10-522
  «Manuel Guancachoque» — UT10, pieza P15 (desglose y agregación), mención M-UT10-527
  «Manuel Guancachoque» — UT10, pieza P16 (auto cabeza de proceso), mención M-UT10-530
  «Guancachoque» — UT10, pieza P16 (auto cabeza de proceso), mención M-UT10-533
  «Guancachoque» — UT11, pieza P18 (declaración jurada), mención M-UT11-516
  «Guancachoque» — UT11, pieza P18 (declaración jurada), mención M-UT11-520
  «Manuel Guancachoque» — UT12.a, pieza P18 (declaración jurada), mención M-UT12.a-502
  «Manuel Guancacho que» — UT12.b, pieza P19 (declaración jurada), mención M-UT12.b-501
  «Guancachoque» — UT12.b, pieza P19 (declaración jurada), mención M-UT12.b-508
  «Guancachoque» — UT12.b, pieza P19 (declaración jurada), mención M-UT12.b-509
  «manuel guancachoque» — UT13, pieza P20 (declaración jurada), mención M-UT13-504
  «guarcachoque» — UT13, pieza P20 (declaración jurada), mención M-UT13-508
  «guancachoque» — UT13, pieza P20 (declaración jurada), mención M-UT13-510
  «guasscachoque» — UT14, pieza P21 (declaración jurada), mención M-UT14-003
  «gancahoque» — UT14, pieza P20 (declaración jurada), mención M-UT14-503
  «guancachoque» — UT14, pieza P20 (declaración jurada), mención M-UT14-505
  «guancachoque» — UT14, pieza P21 (declaración jurada), mención M-UT14-512
  «guancachay» — UT15, pieza P21 (declaración jurada), mención M-UT15-803
  «Manuel Guancachoque» — UT15, pieza P22 (oficio), mención M-UT15-811
  «Manuel Guancachoque» — UT16.a, pieza P23 (informe), mención M-UT16a-001
  «Manuel Guancachoque» — UT16.a, pieza P23 (informe), mención M-UT16a-801
  «dicho Guancachoque» — UT16.a, pieza P23 (informe), mención M-UT16a-804
  «Guancachoque» — UT16.b, pieza P23 (informe), mención M-UT16b-811
  «Ortis» — UT16.b, pieza P23 (informe), mención M-UT16b-813
  «Guancachoque» — UT16.b, pieza P23 (informe), mención M-UT16b-814
  «Manuel Guancachoque» — UT17, pieza P27 (informe), mención M-UT17-004
  «Guancachoque» — UT17, pieza P27 (informe), mención M-UT17-005
  «el mismo denunciador Guancachoque» — UT17, pieza P27 (informe), mención M-UT17-828
  «indio» — UT18, pieza P27 (informe), mención M-UT18-804
  «su feligrés Guancachoque» — UT18, pieza P27 (informe), mención M-UT18-814
  «Guancachoque» — UT18, pieza P27 (informe), mención M-UT18-817
  «Manuel Guancoichoque» — UT19, pieza P29 (vista fiscal), mención M-UT19-001
  «yndio Guancachoque» — UT19, pieza P28 (auto), mención M-UT19-804
  «yndio Guancachoque» — UT19, pieza P29 (vista fiscal), mención M-UT19-820
  «dicho Guancachoque» — UT19, pieza P29 (vista fiscal), mención M-UT19-821
```

## PC06

```text
PREGUNTA: ¿Qué menciones no se pueden identificar con seguridad y por qué?
RESPUESTA (R): 19 reconstrucciones de identidad con creencia posible o indeterminada.

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Ataque nocturno de indios a la casa de Miguel Orey en tiempo del corregidor Reparaz, como hecho distinto del motín que narra Orue (hipótesis de dos episodios)» — creencia: posible; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/hecho/H-p01-alzamiento-orey cc-14-18/hecho/H-p03-alzamiento-orey cc-14-18/hecho/H-p04-alzamiento-reparas
    Argumento: Hipótesis rival de R-tumulto-tiempo-reparaz; la creencia se refiere a la agrupación. P01 (Cano): «En tiempo del señor corregidor don Antonio Reparas, mando dicho Chuquitapa» y «se alzaron contra el capitan don Miguel Orey a las ocho de la noche con pedradas palos cerca de sesenta indios», «pedrearon su tienda hasta quebrar la puerta», «escapo por una ventana». P03 (a nombre de Quiñones): «muy antes de la rebelion. Este mismo cacique invento el alzamiento contra don Miguel Orey», «a su casa hicieron pedazos la puerta», «escaparon por una ventana con toda su familia». P04 (a nombre de Orue): «primero hizo en tiempo del señor corregidor Don Juan Antonio Reparas». Las tres certificaciones usan la misma fórmula acusatoria («no es la primera») y dependen del denunciante, que según Mata (P27) las hizo él mismo; P03 dice «Esto es lo que vi de con mis ojos», pero Mata afirma que de Quiñones «no hay tal hombre en el pueblo de Tinta» (A-UT17-002) y el firmante Juan Cazorla no compareció. Bajo juramento: Cano (P18) ratifica «ser cierto todo lo que en ella dice que le consta solo el porque sucedió en tiempo de corregidor Don Andres ……» (A-UT11-002; el nombre del corregidor no coincide o está mal leído); Orue (P21) narra que «en tiempo del sor corregidor d juan antonio repuras», tras mandar Chuquitapa a la cárcel a su sobrino Diego Orue, «esa misma noche se juntaronmosos indios» y «se amotinaron contra el corregidor y contra el padre del que declara q era cobrador del departamento», «refugiandose todos en casa del corregidor». Orue es testigo interesado: declara que conservó «siempre este agravio y perjuicio que han ocasionado a toda su familia» (A-UT14-536). Nadie lo niega en el expediente, pero tampoco se oye a Chuquitapa, y ni Mata ni el fiscal entran en ello. Que P01 y P03 hablen del mismo suceso es seguro (misma víctima, la puerta hecha astillas «que hasta hoy» se ve, la huida por la ventana), aunque no son dos testimonios sino dos textos del mismo origen. P04 se une a ellos porque repite su fórmula y su corregidor. Lo propio de esta hipótesis es dejar fuera H-p21-motin: el motín de P21 se dirige contra el corregidor y el padre de Orue, nace de la prisión de un muchacho y acaba con todos refugiados en casa del corregidor, mientras que el de P01 y P03 es contra un capitán que huye por una ventana; en los años de Reparaz pudo haber más de un tumulto. En contra: Orue no narra otro suceso de ese tiempo y lo cuenta precisamente para explicar su certificación. Si esta hipótesis fuera la buena, H-p04-alzamiento-reparas podría corresponder también al motín de P21 y no al de Orey; el texto no lo decide.
RECONSTRUCCIÓN «El agitador de tiempos de Reparaz y coronel o comisionado de Túpac Amaru es un pariente homónimo de Andrés Chuquitapa» — creencia: posible; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-004 cc-14-18/mencion/M-UT02-222 cc-14-18/mencion/M-UT03-002 cc-14-18/mencion/M-UT14-002 cc-14-18/mencion/M-UT14-523 cc-14-18/mencion/M-UT14-532
    Argumento: Hipótesis rival de R-chuquitapa para las tres menciones que atribuyen al cacique hechos anteriores a 1780. Que el mismo individuo fuera agitador antes de la rebelión, coronel o comisionado de Túpac Amaru y, 26 años después, cacique y recaudador tras la represión de 1781–1784 no es imposible, pero es llamativo; los testigos son hostiles al cacique y Cano rebaja su propia certificación («Comisionado por este y no coronel», UT11). El texto no nombra a ningún pariente: es una inferencia, no un dato. Creada tras la auditoría I (2026-11-13), como propuesta del modelo. Ampliada el 2026-11-14 (claude-fable-5-2): se añaden tres menciones que también atribuyen hechos anteriores a 1780: «Este mismo cacique invento el alzamiento contra don Miguel Orey» («muy antes de la rebelion», P03) y, en P21, el episodio «en tiempo del sor corregidor d juan antonio repuras» («corral de chuquitapa», «el dicho chuquitapa»). Siguen también en R-chuquitapa, de la que esta es rival. La lectura «Don Andres» de P18 como Chuquitapa (R-don-andres-p18-es-chuquitapa) se apoya en M-UT01-004, que está en ambas. Reconstrucción propuesta originalmente por claude-opus-5-5 el 2026-11-13.
RECONSTRUCCIÓN «El declarante de P19 es un Mariano Casorla distinto de Martín (hipótesis B)» — creencia: improbable; autor: claude-opus-5-5; fecha: 2026-11-13
    Deriva de: cc-14-18/mencion/M-UT12.a-005
    Argumento: Único apoyo: la lectura literal «el Gobernador Señor Don Mariano Casorla», con un tratamiento que es anómalo por sí mismo (un «Gobernador» vecino español y analfabeto). En contra: el declarante habla en primera persona de la certificación de Martín («mando el que declara a Simon Arce»), dice que no sabe quién «firmo su nombre», declara 28 años y no sabe escribir. La variante más defendible de esta hipótesis sería un pariente que responde por Martín, pero choca con esos mismos datos. No se ha cotejado la imagen del folio; la conclusión queda sujeta a ese cotejo. Revisada tras la auditoría I (2026-11-13).
RECONSTRUCCIÓN «El firmante Juan Cazorla es el Juan de Dios Cazorla mencionado en P20» — creencia: posible; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT02-002 cc-14-18/mencion/M-UT13-514 cc-14-18/mencion/M-UT14-509 cc-14-18/mencion/M-UT17-001 cc-14-18/mencion/M-UT17-806
    Argumento: En P20 aparece «mi hermano juan de dios casorlas» (UT13) y «mi hermano Juan se Dios cazorla» (UT14, la misma frase repetida), en el relato de la amenaza de los indios la noche de la prisión: mismo nombre de pila y apellido, de la familia de Santiago Cazorla. Así se explicaría que P03 nombre la puerta de Santiago Cazorla como la segunda en recibir guardia. Nada en el texto identifica expresamente a uno con otro. Creada tras la auditoría I (2026-11-13), como propuesta del modelo. Ampliada el 2026-11-14 (claude-fable-5-2): la identidad de las dos menciones de P20 entre sí está ahora en R-juan-de-dios-cazorla; esta hipótesis solo añade que ese hombre es el firmante de P03 (R-juan-cazorla). Reconstrucción propuesta originalmente por claude-opus-5-5 el 2026-11-13.
RECONSTRUCCIÓN «El padre de Fernando Orue, «cobrador», es el capitán Miguel Orey de P01 y P03 (Orey por Orue)» — creencia: posible; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-213 cc-14-18/mencion/M-UT01-216 cc-14-18/mencion/M-UT02-223 cc-14-18/mencion/M-UT14-529
    Argumento: Orue declara (P21) que «en tiempo del sor corregidor d juan antonio repuras», por un incidente con Chuquitapa, los indios «se amotinaron contra el corregidor y contra el padre del que declara q era cobrador», de noche, «refugiandose todos en casa del corregidor». P01 y P03 sitúan en tiempo del corregidor Reparaz un alzamiento nocturno, movido por Chuquitapa, «contra el capitan don Miguel Orey», que escapó «con toda su familia». Coinciden tiempo, instigador, carácter del hecho y un apellido casi igual (Orey/Orue); P04, la certificación a nombre de Orue, alude al mismo alzamiento. Difieren el oficio (capitán / cobrador) y el detalle (ventana / casa del corregidor), y ningún texto dice que Orey sea el padre de Orue. Se apoya en R-miguel-orey y R-orue; pueden ser dos episodios o dos personas. No hay imagen del folio para cotejar «Orey».
RECONSTRUCCIÓN «El tío Antonio Valdés es el cura propietario ausente de Tinta» — creencia: posible; autor: claude-opus-5-5; fecha: 2026-11-13
    Deriva de: cc-14-18/mencion/M-UT15-813 cc-14-18/mencion/M-UT15-814
    Argumento: P22: «como parroco interino de esta doctrina por hallarse ausente el señor cura propietario de ella; pues aunque interino ha venido en compañía de su tio el Doctor Don Antonio Valdes algun tiempo». La concesiva («aunque interino») y la compañía del tío sugieren que el interino lleva tiempo en la doctrina con el titular; el texto no dice que el tío sea el propietario. Creada tras la auditoría I (2026-11-13), como propuesta del modelo.
RECONSTRUCCIÓN «Golpes a Huancachoque durante su conducción a la cárcel, como hecho distinto de la acometida en la casa de la matrícula (hipótesis de dos episodios)» — creencia: posible; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/hecho/H-p01-maltrato cc-14-18/hecho/H-p03-maltrato cc-14-18/hecho/H-p04-maltrato cc-14-18/hecho/H-p05-maltrato cc-14-18/hecho/H-p06-maltrato cc-14-18/hecho/H-p07-maltrato cc-14-18/hecho/H-p18-golpes
    Argumento: Hipótesis rival de R-agresion-dia-prision. La correferencia de los siete relatos entre sí es segura: todos hablan de golpes de indios a Huancachoque mientras lo llevan a la cárcel (P06 «me hicieron llegar al lugar de la cárcel»; P03 «de los pelos nomás llevaron a la cárcel»; P04 «llevaron de su pelo dando trompadas patadas»; P05 «estiraron a golpes de los pelos pusieron a la cárcel»; P18 «le siguieron pegando los Yndios hasta que lo» «pusieron en la Real cárcel»; P07 resume P06; P01 no da lugar). Lo que esta hipótesis añade es que H-p27-acometida queda fuera: Mata sitúa la acometida dentro de la casa donde se matriculaba, antes de ordenar la prisión, y dice haberla impedido («si yo no salgo al indio lo hubieran en tropeado»); no menciona golpe alguno en el trayecto. Serían entonces dos momentos: uno en la casa, cortado por el juez, y otro en la calle, que Mata calla o no vio. En contra: los agresores son los mismos (alcaldes y segundas en P06 y en P27), la tarde es la misma y Cano habla de continuidad («le siguieron pegando»). Las certificaciones P01, P03, P04 y P05 no son independientes del denunciante: según Mata (P27) «fueron hechos por el mismo Guancachoque haciéndolos firmar a los sujetos que los subscriben», y lo confirman en parte Orue (P21) y el declarante de P19 (auditoría I, §3.1). Mata es el juez que ordenó la prisión y tiene interés en reducir el suceso. Queda en posible.
RECONSTRUCCIÓN «Incidente de falta de respeto de Huancachoque al recaudador alegado ante el subdelegado, causa inmediata de la orden de prisión (hecho mínimo que reúne el insulto según Mata y la queja según el denunciante)» — creencia: posible; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/hecho/H-p06-queja cc-14-18/hecho/H-p23-escandalo cc-14-18/hecho/H-p27-insulto
    Argumento: Hipótesis rival de R-insulto-al-recaudador: la «queja» de P06 y el «insulto» de P27 serían dos versiones del mismo suceso. Mata (P27), que estaba presente y es el juez que ordenó la prisión: «una tarde en la casa en donde estabamos matriculando a los indios el revisitador , y Yo, concluida el dia anterior la numeración de los Ayllos Tinta, y Ucho» Huancachoque «tubo el atrevimiento de insultar al Recaudador con palabras injuriosas, y de manos». El cura interino (P23), en un informe que le pidió el propio Mata (P22) y que se dirige a él: «aquel hecho escandaloso que ocasiono, hallandose vuestra presente en este pueblo , como juegos Real y el señor Agustin Fiscal Don Althamacio Zotelo , pues tuvo» «osadia que acometen a su casique y alcalde mayor Don Andres Chuquitapa». El denunciante (P06) no narra insulto alguno: dice que Chuquitapa, «ansioso de tomar de mi venganza, al siguiente día que prove la ocultación de Indios, dio queja al subdelegado, protestando le había yo perdido el respeto». Ningún testigo jurado fue preguntado por esto. A favor: los dos relatos lo ponen el día siguiente a la numeración o a la prueba de la ocultación, ante el subdelegado, y como causa inmediata de la orden («ordeno se me llevase a la cárcel», P06; «por cuyo insulto, y atropellamiento, en mi misma casa, lo mande llevar a la cárcel», P27); y el contenido de la queja, haber «perdido el respeto», es el insulto de la otra versión. En contra: son actos de sujetos distintos, una queja de Chuquitapa frente a una agresión de Huancachoque, y en el relato de Mata no hace falta queja alguna, porque él mismo lo presenció. El denunciante ni afirma ni niega haber insultado: lo presenta como alegación de su enemigo y como venganza. Queda en posible; sirve para comparar las dos versiones de la causa de la prisión (R-prision).
RECONSTRUCCIÓN «Incitación de los indios de los ayllus contra el recaudador Chuquitapa atribuida a Huancachoque (conducta imputada, sin fecha)» — creencia: posible; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/hecho/H-p23-confabulacion cc-14-18/hecho/H-p27-intento-sublevacion
    Argumento: La creencia se refiere a la agrupación, no a que Huancachoque incitara a nadie. Mata (P27) lo refiere de oídas: en una diligencia hecha al día siguiente de la prisión, el común y principales de los ayllus Tinta y Ucho «lo convencieron de falsedad exponiendo que el había querido conmover y sublevar a todos los Indios contra su recaudador del que no tenían queja alguna». El cura interino (P23): «el no se cansa en estas aduciendo a sus confidencias y los demas ayllu a hacer efectiva sus miras en la ruina de bien de su casique». Los dos atribuyen a Huancachoque mover a los indios de los ayllus contra Chuquitapa. No son independientes: el cura informa a petición de Mata, y Mata se apoya en ese informe (A-UT18-814). La diligencia con el común no está en el expediente y ningún testigo jurado habla de ello. El denunciante cuenta lo contrario: que los indios de Chuquitapa se movieron contra él. Queda en posible porque P27 habla de un intento concreto, declarado en una diligencia, y P23 de una conducta habitual en presente («no se cansa»): pueden ser la misma imputación o dos imputaciones parecidas. La alternativa no necesita registro propio: si no fueran lo mismo, los dos hechos quedarían sin enlazar.
RECONSTRUCCIÓN «La «compañía de Tinta» de Cano y Orue es la «primera compañía» de Santiago Cazorla» — creencia: posible; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-201 cc-14-18/mencion/M-UT02-202 cc-14-18/mencion/M-UT02-203 cc-14-18/mencion/M-UT03-201 cc-14-18/mencion/M-UT13-503
    Argumento: Hipótesis de fusión de R-compania-tinta y R-compania-santiago-cazorla. A favor: Cano llama a Santiago Cazorla «su segundo sargento» (UT11) y este declara sobre «asi primer sargento ysidro cano» (UT13), lo que los pone en una misma compañía; y Huancachoque sirvió en la de Cazorla (UT02). En contra: Cazorla se titula «sargento primero» (UT02), no segundo, y un regimiento tiene varias compañías; nada dice que la «de Tinta» sea la «primera».
RECONSTRUCCIÓN ««Don Andres ……» (P18) es Andrés Chuquitapa, sujeto de la frase que sigue a «en tiempo de corregidor»» — creencia: posible; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-004 cc-14-18/mencion/M-UT11-514
    Argumento: La frase de P01 que Cano ratifica es «En tiempo del señor corregidor don Antonio Reparas, mando dicho Chuquitapa»: en P18, «en tiempo de corregidor Don Andres ……» puede haber perdido el nombre del corregidor y conservar el del sujeto, Don Andrés [Chuquitapa]; el único Andrés de la causa es él y la frase siguiente habla de él («en tiempo del rebelde Tupa amaro fue Comisionado»). Rival de R-don-andres-p18-es-reparaz; ver R-chuquitapa (y su rival R-chuquitapa-1780-pariente, que comparte M-UT01-004) y R-reparaz. No hay imagen del folio: la laguna impide decidir.
RECONSTRUCCIÓN ««Don Antonio Chacón» (P10) es un escribano distinto de Agustín Chacón y Becerra» — creencia: improbable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT09-514
    Argumento: Hipótesis rival de R-chacon-escribano. Único apoyo: la lectura literal de dos nombres de pila, «Antonio» (27 de agosto) y «Agustin» (noviembre). En contra: mismo apellido, misma función junto al presidente y las mismas firmas abreviadas «Chacón» en las notificaciones de agosto y de noviembre. Si fuera cierta, las firmas «Chacón» de agosto (P08, P11, P12) serían de Antonio y no de Agustín. No hay imagen del folio; un cotejo de las firmas lo resolvería. M-UT09-514 sirve también de ancla en R-escribano-mayor-p09-es-chacon.
RECONSTRUCCIÓN ««Don Juan Quiñones» es un nombre puesto por quien redactó la certificación P03 (H1)» — creencia: posible; autor: claude-opus-5-5; fecha: 2026-11-13
    Deriva de: cc-14-18/mencion/M-UT02-001 cc-14-18/mencion/M-UT17-002
    Argumento: Según el subdelegado, «no hay tal hombre en el pueblo de Tinta» y los documentos «fueron hechos por el mismo Guancachoque» (P27); el fiscal atribuye también al denunciante los documentos (P29). Ambos son parte interesada en desacreditar las certificaciones. La auditoría no propone un valor para H1; se le da posible, simétrico de H2, porque R-quinones es indeterminado. Creada tras la auditoría I (2026-11-13), como propuesta del modelo.
RECONSTRUCCIÓN ««Don Juan Quiñones» es una persona real que no reside en Tinta (H2)» — creencia: posible; autor: claude-opus-5-5; fecha: 2026-11-13
    Deriva de: cc-14-18/mencion/M-UT02-001 cc-14-18/mencion/M-UT17-002
    Argumento: El juez, parte interesada, solo dice que «no hay tal hombre en el pueblo de Tinta», lo que no excluye a alguien de fuera del pueblo. A favor de un autor distinto de Santiago Cazorla: P03 distingue «mi puerta» de «la puerta de don Santiago Cazorla» (UT02). Creada tras la auditoría I (2026-11-13), como propuesta del modelo.
RECONSTRUCCIÓN ««Don Juan Quiñones», teniente alguacil: existencia de la persona (en disputa)» — creencia: indeterminado; autor: claude-opus-5-5; fecha: 2026-11-13
    Deriva de: cc-14-18/mencion/M-UT02-001 cc-14-18/mencion/M-UT17-002
    Argumento: La certificación P03 está extendida a su nombre, pero el juez afirma que «no hay tal hombre en el pueblo de Tinta» (A-UT17-002). El juez no dice que la firmara Juan Cazorla en P24 («Juan Cazorla de quien aparece firmada la Certificación»); la atribución expresa está en P25 («Juan Cazorla que suscribió el documento de 2 fojas»). Esta reconstrucción trata solo de la existencia; que las dos menciones designan el mismo nombre está en R-quinones-nombre. Hipótesis rivales: R-quinones-nombre-puesto-por-redactor (H1) y R-quinones-real-no-residente (H2). No se fusiona con Juan Cazorla. Revisada tras la auditoría I (2026-11-13).
RECONSTRUCCIÓN ««aquel Regio sonado» (P23) es la Real Audiencia del Cusco» — creencia: posible; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT05-208 cc-14-18/mencion/M-UT08-208 cc-14-18/mencion/M-UT16b-812
    Argumento: Hipótesis. El cura pide que su informe se «pueda exponer a aquel Regio sonado nodudando y como oraculos de la ley sabran comtrapesar … as representaciones o diosas de Ortis o Guancachoque» (UT16.b). «Regio sonado» se lee como «Regio Senado», tratamiento usual de una Audiencia, y lo de oráculos de la ley conviene a sus ministros; el asunto se ventila ante el presidente y el fiscal de «esta Real Audiencia» (UT05, UT08). Pero la lectura es conjetural y la causa se tramita en rigor en el Gobierno e Intendencia (R-gobierno-cusco), no en la sala de la Audiencia: queda en «posible».
RECONSTRUCCIÓN ««corregidor Don Andres ……» (P18) es el corregidor Reparaz, con el nombre mal leído o truncado» — creencia: posible; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-211 cc-14-18/mencion/M-UT11-514
    Argumento: Cano ratifica su certificación P01 y dice que le consta «porque sucedió en tiempo de corregidor Don Andres ……» (UT11), con laguna a continuación. P01 dice «En tiempo del señor corregidor don Antonio Reparas»: si «Don Andres» va con «corregidor», es el mismo corregidor con el nombre de pila mal leído (Antonio/Andres) y el apellido perdido en la laguna. Rival de R-don-andres-p18-es-chuquitapa; ver R-reparaz y R-chuquitapa. No hay imagen del folio: la laguna impide decidir.
RECONSTRUCCIÓN ««el Gobernador Señor Don Mariano Casorla» (P19) es una mala lectura de «el granadero … Martin Casorla»» — creencia: posible; autor: claude-opus-5-5; fecha: 2026-11-13
    Deriva de: cc-14-18/mencion/M-UT04-001 cc-14-18/mencion/M-UT12.a-005
    Argumento: Hipótesis paleográfica que refuerza R-declarante-p19-es-martin: P05 presenta a Martín Cazorla como «soldado granadero» (A-UT04-201); un «Gobernador» analfabeto (A-UT12b-001), de 28 años y vecino español, es anómalo en un pueblo de indios; abreviaturas como «Gran.ro» y «Mart.n» pudieron leerse «Gobernador» y «Mariano». No se ha cotejado la imagen del folio; la conclusión queda sujeta a ese cotejo. Creada tras la auditoría I (2026-11-13), como propuesta del modelo.
RECONSTRUCCIÓN ««las milicias de aquella provincia» (P06) son el regimiento de Tinta» — creencia: posible; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-202 cc-14-18/mencion/M-UT02-201 cc-14-18/mencion/M-UT06-206
    Argumento: Hipótesis de fusión sobre R-regimiento-tinta. Huancachoque alega «haber estado empleado en las milicias de aquella provincia» (UT06) y Santiago Cazorla certifica que «ha estado soldado en mi compañía más de cinco años», compañía del «regimiento de Tinta» (UT02). El servicio es el mismo, pero «las milicias de aquella provincia» puede designar el conjunto de las milicias del partido y no un regimiento determinado: «posible».
```

## PC07

```text
PREGUNTA: ¿Qué lugares y ayllus se mencionan y con qué identificador de HGIS?
RESPUESTA (R): 33 lugares o grupos reconstruidos; 15 con identificador HGIS. Sin entrada en HGIS: América meridional (América del Sur), Ayllu Tinta, Ayllu Uchu / Ucho, Casa del subdelegado en Tinta donde se matriculaba a los indios, Casa o tienda del capitán Miguel Orey, apedreada en tiempos de Reparaz, Casas de la morada del fiscal Gómez / Gonzalo del Río en el Cusco, Compañía de Tinta (milicias) de Isidro Cano y Fernando Orue, Cárcel del pueblo de Tinta (1806), Cárcel donde el corregidor hizo poner a Diego Orue en tiempos de Reparaz, Doctrina (parroquia) de Tinta, Gobierno (superior gobierno e intendencia) del Cusco, a cargo del presidente, Intérpretes generales que asisten a la ratificación de Huancachoque, La «compañía de Tinta» de Cano y Orue es la «primera compañía» de Santiago Cazorla, Los 51 indios tributarios ocultos denunciados por Huancachoque, Los alcaldes (de indios) que acometieron a Huancachoque al ser preso, Los españoles (vecinos españoles) del pueblo de Tinta, Plaza del pueblo de Tinta, Primera compañía del regimiento de Tinta, la de Santiago Cazorla, Provincia de Urubamba (república), Real Audiencia del Cusco, Real Hacienda, Regimiento de milicias del partido de Tinta, «aquel Regio sonado» (P23) es la Real Audiencia del Cusco, «aquella provincia» (P06) es el partido de Tinta, «este partido», «aquel partido», «partido de mi cargo» y «subdelegado de Tinta» designan el partido de Tinta, «este pueblo», «dicho Pueblo», «aquel Pueblo», «el pueblo» designan el pueblo de Tinta, «las milicias de aquella provincia» (P06) son el regimiento de Tinta.

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «América meridional (América del Sur)» — creencia: verdadero; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT16b-808
    Argumento: «de la chispa de vuestro Condorcanqui se hubo de a trasar casi toda la America meridional» (UT16.b): el cura alude a la extensión de la rebelión de 1780. Nombre corriente de la época para América del Sur; Wikidata Q18 («América del Sur», TGN 1000002 por P1667), comprobado en la API de Wikidata el 2026-11-14.
RECONSTRUCCIÓN «Ayllu Tinta» — creencia: verdadero; autor: claude-opus-5-5; fecha: 2026-11-13
    Deriva de: cc-14-18/mencion/M-UT00-202 cc-14-18/mencion/M-UT03-204 cc-14-18/mencion/M-UT05-003 cc-14-18/mencion/M-UT17-819 cc-14-18/mencion/M-UT17-826 cc-14-18/mencion/M-UT18-809
    Argumento: Ayllu del pueblo de Tinta donde la averiguación tuvo como resultado «el descubrimiento de cuarenta y cuatro tributarios en el Ayllu Tinta y siete en el Ayllu nominado Uchu» (UT05); los denunciados fueron 51 en total. Lo nombran también la carátula («casique del Ayllo Tinta»), la certificación de Orue («los Indios del Ayllu de tinta») y el informe del subdelegado («Ayllus Tinta y Ucho», «Ayllos Tinta, y Ucho», «citados Ayllos Tinta y Ucho»). No se fusiona con el pueblo, el partido ni la compañía de Tinta. Sin entrada en HGIS (que no registra ayllus). Revisada tras la auditoría I (2026-11-13).
RECONSTRUCCIÓN «Ayllu Uchu / Ucho» — creencia: verdadero; autor: claude-opus-5-5; fecha: 2026-11-13
    Deriva de: cc-14-18/mencion/M-UT05-004 cc-14-18/mencion/M-UT17-007 cc-14-18/mencion/M-UT17-827 cc-14-18/mencion/M-UT18-810
    Argumento: «Ayllu nominado Uchu» (escrito del denunciante) y «Ayllus Tinta y Ucho», «Ayllos Tinta, y Ucho» y «citados Ayllos Tinta y Ucho» (informe del subdelegado) aparecen en el contexto de la numeración de tributarios y designan el mismo ayllu del pueblo de Tinta; la alternancia u/o es la vacilación vocálica normal en la grafía colonial de voces quechuas. Revisada tras la auditoría I (2026-11-13).
RECONSTRUCCIÓN «Casa del subdelegado en Tinta donde se matriculaba a los indios» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT17-822 cc-14-18/mencion/M-UT18-805
    Argumento: En el informe del subdelegado: «una tarde en la casa en donde estabamos matriculando a los indios el revisitador» … «[Huancachoque] tubo el atrevimiento de insultar al Recaudador» (UT17) y, sobre el mismo incidente, «por cuyo insulto, y atropellamiento, en mi misma casa, lo mande llevar a la cárcel» (UT18). El insulto ocurre en la casa donde se matriculaba y el subdelegado lo sitúa «en mi misma casa»: una sola casa, su alojamiento en Tinta durante la revisita. Que fuera casa propia o posada no consta.
RECONSTRUCCIÓN «Casa o tienda del capitán Miguel Orey, apedreada en tiempos de Reparaz» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-215 cc-14-18/mencion/M-UT02-225
    Argumento: Cano: contra «el capitan don Miguel Orey … pedrearon su tienda hasta quebrar la puerta unas astillas que hasta hoy esta presente a las tejas hizo polvo» y Orey «escapo por una ventana» (UT01). Certificación a nombre de Quiñones: el alzamiento «contra don Miguel Orey … escaparon por una ventana … a su casa hicieron pedazos la puerta hecho una astilla, las tejas volvieron en tierra que hasta hoy se halla la dicha puerta, hecho astillas» (UT02). Mismo dueño, mismo hecho y mismos detalles (puerta en astillas que aún se ve, tejas, huida por la ventana): es el mismo inmueble, llamado «tienda» en una pieza y «casa» en otra. Las dos certificaciones no son independientes (el subdelegado las atribuye a un mismo redactor, UT17), lo que explica la coincidencia y no la invalida.
RECONSTRUCCIÓN «Casas de la morada del fiscal Gómez / Gonzalo del Río en el Cusco» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT08-209 cc-14-18/mencion/M-UT09-520
    Argumento: Dos notificaciones del escribano Chacón al fiscal, con cuatro días de diferencia: «al Señor Don Luis Gomez del Rio … estando en las casas de su morada» (23 de agosto, UT08) y «al -Señor Don Luis Gonsalo del Rio … estando en las casas de sus moradas» (27 de agosto, UT09). El notificado es la misma persona (R-fiscal-del-rio). No se incluye «estando en las casas de mi morada» (26 de noviembre, UT20): el posesivo «mi» remite literalmente al escribano; puede ser error por «su», pero no consta.
RECONSTRUCCIÓN «Compañía de Tinta (milicias) de Isidro Cano y Fernando Orue» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-201 cc-14-18/mencion/M-UT03-201
    Argumento: «Yo el sargento Don Isidro Cano de esta compañía de Tinta de Milicias de este cuerpo» (UT01) y «Yo el cabo primero en esta compañía de Tinta de este mismo cuerpo» (UT03, a nombre de Fernando Orue): mismo nombre y misma fórmula. La segunda calca la primera (el subdelegado atribuye las certificaciones a un mismo redactor, UT17), de modo que la coincidencia verbal no es prueba independiente: «probable». Es una compañía, no el pueblo ni el regimiento.
RECONSTRUCCIÓN «Cusco (ciudad), sede de la Real Audiencia y la Intendencia» — creencia: verdadero; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT05-005 cc-14-18/mencion/M-UT08-204 cc-14-18/mencion/M-UT08-205 cc-14-18/mencion/M-UT08-211 cc-14-18/mencion/M-UT08-232 cc-14-18/mencion/M-UT09-516 cc-14-18/mencion/M-UT09-534 cc-14-18/mencion/M-UT17-811 cc-14-18/mencion/M-UT19-801 cc-14-18/mencion/M-UT20-801 cc-14-18/mencion/M-UT20-803 cc-14-18/mencion/M-UT20-809 cc-14-18/mencion/M-UT20-811
    Argumento: «CUSCO» en la data del escrito presentado ante el Fiscal Protector General. HGIS src_id 6000002 (WHG 176704). Ampliada el 2026-11-14 (registro base de claude-opus-5-5, 2026-11-12) con las datas y localizaciones de las piezas de la capital: «Cusco y Agosto 21 de 1806», «En el Cusco y Agosto veinte y tres», «En la ciudad del Cuzco en trece días», «Cuzco» al pie de las firmas (UT08); «En el Cuzco en veinte y siete días», «Cusco y Agosto 28 de 1806» (UT09); «Cuzco noviembre 18» (UT17); «Cusco y noviembre 26 de 1806» (UT19); «Cuzco y Noviembre 20 de 1806», «En la Ciudad del Cuzco en veinte y seis de noviembre», «En el Cusco en veinte y tres de Diciembre» (UT20). «habiendo llegado a la ciudad» (UT20) se enlaza por antecedente explícito en la misma oración («En el Cusco … habiendo llegado a la ciudad»). La alternancia Cusco/Cuzco es solo gráfica.
RECONSTRUCCIÓN «Cárcel del pueblo de Tinta (1806)» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-205 cc-14-18/mencion/M-UT02-211 cc-14-18/mencion/M-UT02-214 cc-14-18/mencion/M-UT03-211 cc-14-18/mencion/M-UT03-212 cc-14-18/mencion/M-UT03-215 cc-14-18/mencion/M-UT04-206 cc-14-18/mencion/M-UT04-208 cc-14-18/mencion/M-UT05-214 cc-14-18/mencion/M-UT05-219 cc-14-18/mencion/M-UT07-209 cc-14-18/mencion/M-UT11-519 cc-14-18/mencion/M-UT12.a-501 cc-14-18/mencion/M-UT12.b-503 cc-14-18/mencion/M-UT12.b-510 cc-14-18/mencion/M-UT12.b-516 cc-14-18/mencion/M-UT13-505 cc-14-18/mencion/M-UT14-516 cc-14-18/mencion/M-UT18-806
    Argumento: La cárcel donde estuvo preso Huancachoque tras la numeración de los ayllus, en el pueblo de Tinta. Todas las menciones narran esa prisión o la noche siguiente: «lo pusieron a la carcel a esa noche» (UT01), «llevaron a la cárcel», «allegaron a la puerta de la cárcel» (UT02), «llevaron preso a la cárcel», «asumaron a la puerta de la cárcel» (UT03), «pusieron a la cárcel» (UT04), «ordeno se me llevase a la cárcel», «me hicieron llegar al lugar de la cárcel» (UT05), «estando aquel en la carcel» (UT07), «ponerlo en la caecel a Guancachoque» (UT11), «pusieron en la Real cárcel» (UT12.a), «lo llevaban preso ala cárcel», «en la puerta de la carcel con garrotes» (UT12.b), «la noche q manuel guancachoque estubo en la carcel» (UT13), «advirtió a la puerta de la carcel» (UT14), «lo mande llevar a la cárcel» (UT18). Ningún pasaje dice «cárcel de Tinta»: el pueblo lo fija el hecho narrado (R-prision, R-alboroto-carcel). «pidieron a la cárcel al denunciante» (UT04) es de lectura dudosa. Quedan fuera las dos menciones de la cárcel en tiempos del corregidor Reparaz (R-carcel-tiempo-reparaz). Sin identificador externo: HGIS no registra edificios.
RECONSTRUCCIÓN «Cárcel donde el corregidor hizo poner a Diego Orue en tiempos de Reparaz» — creencia: verdadero; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT14-524 cc-14-18/mencion/M-UT14-527
    Argumento: Dos menciones de la misma oración de Fernando Orue (UT14): a su sobrino Diego Orue «lo mando poner a la carcel con sus propios criados de lo q resulto q esa misma noche se juntaronmosos indios y lo votaron de la carcel». La correferencia entre ambas es segura. Es verosímil que sea la misma cárcel de Tinta de 1806 (R-carcel-tinta), pero el hecho es de «tiempo del sor corregidor d juan antonio repuras», anterior a 1780, y el texto no dice dónde ocurrió ni permite afirmar la continuidad del edificio: no se funden.
RECONSTRUCCIÓN «Doctrina (parroquia) de Tinta» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT15-812 cc-14-18/mencion/M-UT16a-802
    Argumento: El subdelegado pide informe al cura «como parroco interino de esta doctrina por hallarse ausente el señor cura propietario de ella» (UT15) y el cura responde invocando el «descanso comun de esta Doctrina» (UT16.a). El destinatario es Agustín Valdés, «cura interino de dicho -Pueblo» de Tinta (UT18): la doctrina es la de ese pueblo. Ninguna de las dos piezas la nombra. No se funde con el pueblo ni con el partido de Tinta. Sin identificador externo comprobado.
RECONSTRUCCIÓN «Gobierno (superior gobierno e intendencia) del Cusco, a cargo del presidente» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT19-807 cc-14-18/mencion/M-UT19-824
    Argumento: «Tomará el gobierno las más serias providencias. Muñoz [firma]» (auto del presidente, «Cusco y noviembre 26 de 1806») y «la prudente y celosa rectitud de este gobierno» (vista del fiscal al presidente, «Cuzco y Noviembre 20 de 1806»), ambas en UT19 y sobre el mismo asunto: la autoridad gubernativa que resuelve el expediente. Es el «Superior Govierno» que nombra el subdelegado (UT10, sin mención anotada) y el «Govierno e intendencia» de UT08 (mención de clase lugar, R-intendencia-cusco). No se le da identificador externo.
RECONSTRUCCIÓN «Gobierno e Intendencia del Cusco (territorio)» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT08-214
    Argumento: «El señor Don Manuel Galeano Teniente Asesor de este Govierno e intendencia» (UT08), en diligencia hecha «En la ciudad del Cuzco»: «este» remite al lugar de redacción, luego la Gobernación-Intendencia del Cusco. Mención única; se reconstruye para darle identificador. HGIS de las Indias (territorios) src_id PRPECU00 = WHG 140068 («Cuzco», Gobernación-Intendencia, 1784–1808) y Wikidata Q5918759 («Intendencia del Cuzco», 1784–1824), comprobados en las APIs de WHG y Wikidata el 2026-11-14. El texto no nombra la intendencia: de ahí «probable». La mención es de clase lugar; el gobierno como autoridad está en R-gobierno-cusco (clase grupo).
RECONSTRUCCIÓN «Intérpretes generales que asisten a la ratificación de Huancachoque» — creencia: verdadero; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT08-220 cc-14-18/mencion/M-UT08-226
    Argumento: Misma pieza (P09, UT08): el juramento se recibe «como presencia del Doctor Don Manuel Valencia Abogado protector … e interpretes generales» y el acta cierra «lo firmó con su Merced protector e interpretes de que doy fe». La segunda retoma a los de la primera; firman al pie Marcos Salcedo y Juan Clemente Jordan (su identificación como intérpretes corresponde a las reconstrucciones de personas).
RECONSTRUCCIÓN «La «compañía de Tinta» de Cano y Orue es la «primera compañía» de Santiago Cazorla» — creencia: posible; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-201 cc-14-18/mencion/M-UT02-202 cc-14-18/mencion/M-UT02-203 cc-14-18/mencion/M-UT03-201 cc-14-18/mencion/M-UT13-503
    Argumento: Hipótesis de fusión de R-compania-tinta y R-compania-santiago-cazorla. A favor: Cano llama a Santiago Cazorla «su segundo sargento» (UT11) y este declara sobre «asi primer sargento ysidro cano» (UT13), lo que los pone en una misma compañía; y Huancachoque sirvió en la de Cazorla (UT02). En contra: Cazorla se titula «sargento primero» (UT02), no segundo, y un regimiento tiene varias compañías; nada dice que la «de Tinta» sea la «primera».
RECONSTRUCCIÓN «Los 51 indios tributarios ocultos denunciados por Huancachoque» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT03-206 cc-14-18/mencion/M-UT05-206 cc-14-18/mencion/M-UT05-221 cc-14-18/mencion/M-UT07-206 cc-14-18/mencion/M-UT09-527 cc-14-18/mencion/M-UT10-506 cc-14-18/mencion/M-UT11-503 cc-14-18/mencion/M-UT19-814
    Argumento: El grupo denunciado: «aver denunciado cincuenta y un tributarios en la revisita» (UT07), «51 yndios tributarios que ha denunciado Manuel Guancachoque» (UT09), «cinquenta y un Indios que dice tener ocultos, y fuera de Matricula» (UT10): la cifra y el denunciante coinciden. Sin cifra, por descripción: «denuncie considerable número de Indios tributarios que … tenia ocultos el recaudaderor» (UT05); «declaro por los Indios ocultados» (UT03); «todos los Indios que manifiesta la denuncia ultima estan matriculados» (UT11); «los denuncios de Yndios tributarios que hizo» (UT19). «los que quedan ya matriculados» (UT05) cierra la frase «cuarenta y cuatro tributarios en el Ayllu Tinta y siete en el Ayllu nominado Uchu que son los mismos que precente … y los que quedan ya matriculados»: 44 + 7 = 51. No se incluye «cuarenta y cuatro tributarios» (UT05), que es solo la parte del ayllu Tinta. La providencia P14 dice que esta denuncia «es la misma que hizo en once de Febrero» anterior: si los denunciados entonces eran exactamente los mismos no consta; de ahí «probable».
RECONSTRUCCIÓN «Los alcaldes (de indios) que acometieron a Huancachoque al ser preso» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT05-216 cc-14-18/mencion/M-UT17-830
    Argumento: Las dos partes nombran a los alcaldes entre quienes agredieron al denunciante en el mismo incidente. Huancachoque: «ordeno se me llevase a la cárcel y aquí fue cuando los segundas, los alcaldes, sus parientes y demás dependientes suyos … me envistieron» (UT05). El subdelegado: «lo que visto por los Alcaldes. … Segundas, y Principales de los citados Ayllus de Chuquitapa acometieron contra el» (UT17–UT18). Coinciden hecho, momento y calidad. Las menciones «los segundas» (UT05) y «Segundas, y Principales» (UT18) no se enlazan entre sí porque la segunda abarca dos calidades. Orue dice en singular «los primeros ay el alcalde y segunda» (UT03, sin mención de grupo).
RECONSTRUCCIÓN «Los españoles (vecinos españoles) del pueblo de Tinta» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-208 cc-14-18/mencion/M-UT02-216 cc-14-18/mencion/M-UT02-217 cc-14-18/mencion/M-UT03-220 cc-14-18/mencion/M-UT11-518 cc-14-18/mencion/M-UT13-509 cc-14-18/mencion/M-UT14-504
    Argumento: El vecindario español de Tinta, contra el que según los certificantes se dirigía el alzamiento: «hacen una matanza a los españoles» (UT01); «despues pasar a los españoles», «todos los españoles tuvimos por bien hecho» (UT02); «ninguno estamos libres de su traición los españoles» (UT03). Las declaraciones repiten la frase de Cano al preguntar por ella: «hacer matalo de los españoles poniendo guardias» (UT11), «hace una matanza a contra los españoles poniendo guardias» (UT13), «haser matanza de los españoles poniendo guardias» (UT14). Los declarantes se dicen «vecino Español de este … pueblo». Es un colectivo de extensión imprecisa, no un cuerpo: «probable». «dos españoles» (UT02) queda fuera por ser un subconjunto indeterminado.
RECONSTRUCCIÓN «Partido de Tinta (subdelegación de la Intendencia del Cusco)» — creencia: verdadero; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT05-204 cc-14-18/mencion/M-UT07-212 cc-14-18/mencion/M-UT09-503 cc-14-18/mencion/M-UT19-803 cc-14-18/mencion/M-UT19-810
    Argumento: El partido, distinto del pueblo, la doctrina, la compañía y el ayllu homónimos: «vecino del pueblo de Tinta, partido de este nombre» (UT05), «subdelegado del partido de Tinta» (UT07), «Juez subdelegado del partido de Tinta» (UT09), «subdelegado del partido de tinta» y «oficio del subdelegado del partido de Tinta» (UT19). HGIS de las Indias (territorios) src_id JUPECUTI = WHG 139803, comprobado en la API de WHG el 2026-11-14: título «Tinta», nombres «Canas y Canchis» (corregimiento, 1701–1783) y «Tinta» (1784–1808), división política con polígono en torno a -71.0, -13.8; es el único territorio de ese nombre en el obispado del Cusco. No se añade Wikidata: Q84575363 («Provincia de Tinta») es la provincia republicana de 1825–1833, no el partido colonial.
RECONSTRUCCIÓN «Plaza del pueblo de Tinta» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-209 cc-14-18/mencion/M-UT02-208 cc-14-18/mencion/M-UT02-213 cc-14-18/mencion/M-UT02-219 cc-14-18/mencion/M-UT03-213
    Argumento: La plaza donde, según los certificantes, se juntaron los indios la noche de la prisión de Huancachoque: «estaba cubierto de indiada la plaza» (UT01); «cuasi lo acaban en las calles públicas y plaza», «se alzaron los indios en la plaza», «en cada esquina de esta plaza» (UT02); «todos ebrios al redor de la plaza» (UT03). Las certificaciones se dan en Tinta (UT01, UT02) y narran el mismo hecho; «esta plaza» supone que el certificante escribe en el pueblo. El texto no la nombra: «probable».
RECONSTRUCCIÓN «Primera compañía del regimiento de Tinta, la de Santiago Cazorla» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT02-202 cc-14-18/mencion/M-UT02-203 cc-14-18/mencion/M-UT13-503
    Argumento: «sargento primero del regimiento de Tinta de la primera compañía es cierto que Manuel Guamanchoque ha estado soldado en mi compañía» (UT02): las dos menciones son de la misma oración y del mismo certificante. En su declaración, Santiago Cazorla comparece como «… segundo en la compañia» (UT13, pasaje corrupto: «via en este partido feretro segundo en la compañia en este fue santiago cacerola»); se entiende la compañía en que sirve, pero la lectura es insegura y baja la creencia a «probable».
RECONSTRUCCIÓN «Provincia de Urubamba (república)» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT20-817
    Argumento: «El ciudadano Matias Ugarte = Notario Público de la provincia de Urubamba» (UT20), en la certificación notarial republicana ajena al expediente (P32): «ciudadano» y «provincia» son usos posteriores a la independencia. Wikidata Q1771879 («provincia de Urubamba», provincia del departamento del Cusco; -13.31, -72.12), comprobado en la API de Wikidata el 2026-11-14. No se usa el registro HGIS JUPECUUR (WHG 139804), que es el corregimiento y la subdelegación coloniales de Urubamba (hasta 1808), no la provincia republicana. La pieza no lleva fecha: «probable».
RECONSTRUCCIÓN «Real Audiencia del Cusco» — creencia: verdadero; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT05-208 cc-14-18/mencion/M-UT08-208
    Argumento: «de orden del muy ilustre señor presidente que esta Real Audiencia» (escrito datado «CUSCO», UT05) y «su fiscal en esta Real Audiencia» (notificación hecha «En el Cusco», UT08): «esta» remite al lugar de redacción de ambas piezas, la ciudad sede del tribunal. Wikidata Q2134673 («Real Audiencia del Cuzco», alto tribunal español), comprobado en la API de Wikidata el 2026-11-14. HGIS registra el distrito de la Audiencia (AUCU0000, WHG 139281, 1788–1808), que es un territorio y no el tribunal: no se usa como identificador de este grupo.
RECONSTRUCCIÓN «Real Hacienda» — creencia: verdadero; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT00-205 cc-14-18/mencion/M-UT02-218 cc-14-18/mencion/M-UT04-202 cc-14-18/mencion/M-UT04-211 cc-14-18/mencion/M-UT04-212
    Argumento: El fisco real, nombrado siempre igual: «Instancia Real Hacienda» (ramo anotado en la carátula, UT00); «haver manifestado el robo a favor de la Real Hacienda» (UT02); «denunciante a favor de la Real Hacienda», «condolían por a favor de la Real Hacienda», «Sintiéndonos a favor de la Real Hacienda» (UT04). Wikidata Q140402469 («Real Hacienda de Indias», sistema de administración fiscal de la Monarquía en la América española), comprobado en la API de Wikidata el 2026-11-14: coincide el concepto, no una caja concreta. Las «reales arcas» son menciones de clase cosa y van en R-reales-arcas.
RECONSTRUCCIÓN «Regimiento de milicias del partido de Tinta» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-202 cc-14-18/mencion/M-UT02-201
    Argumento: Cano es sargento «de esta compañía de Tinta de Milicias de este cuerpo, del regimiento de este partido» (UT01, datada en el pueblo de Tinta) y Santiago Cazorla «sargento primero del regimiento de Tinta de la primera compañía» (UT02, datada en Tinta). Según el propio Cano, Santiago Cazorla es «su segundo sargento» (UT11): sirven en el mismo cuerpo, y «este partido» es el de Tinta (R-partido-tinta-deicticos). No se funde con la compañía.
RECONSTRUCCIÓN «San Pedro de Cacha (pueblo)» — creencia: probable; autor: claude-opus-5-5; fecha: 2026-11-13
    Deriva de: cc-14-18/mencion/M-UT02-006
    Argumento: «soldado del pueblo de San Pedro de Cacha» (P03). El registro WHG 177061 / HGIS 6000358 («San Pedro», jurisdicción de Tinta) incluye la variante «Cacha»: la equivalencia es una coincidencia de nombre registrada por el propio gazetteer, y las coordenadas de Wikidata Q13190677 (San Pedro, distrito de San Pedro, Canchis) coinciden con las de HGIS. TGN 8712075 se enlaza solo como rdfs:seeAlso: su etiqueta preferida es «San Pedro de Cacha», su nota lo sitúa junto a las ruinas de Raqchi y sus coordenadas (-14.166, -71.333) distan unos 2 km del punto de HGIS, pero su jerarquía lo pone por error bajo Pasco (tgn:1000726); comprobado en el SPARQL de Getty el 2026-11-13. No confundir a «don Javier Aparicio», el soldado de San Pedro de Cacha, con el testigo «CELEDONIO APARICIO» (P18). Revisada tras la auditoría I (2026-11-13).
RECONSTRUCCIÓN «Sicuani (pueblo), lugar de data de las providencias e informe del subdelegado» — creencia: verdadero; autor: claude-opus-5-5; fecha: 2026-11-13
    Deriva de: cc-14-18/mencion/M-UT10-001 cc-14-18/mencion/M-UT17-804 cc-14-18/mencion/M-UT18-819
    Argumento: Pueblo del partido de Tinta donde el subdelegado data sus providencias e informe («Sicuani Setiembre. 17 de 1806», «Sicuani Noviembre 8 de 1806», «Siquani Noviembre 8 de 1806»); que fuera su residencia no consta. HGIS src_id 6000365 (WHG 177068), Wikidata Q4419079 y TGN 1024771, verificados por la auditoría I. Revisada tras la auditoría I (2026-11-13).
RECONSTRUCCIÓN «Tinta (pueblo)» — creencia: verdadero; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-007 cc-14-18/mencion/M-UT02-204 cc-14-18/mencion/M-UT05-203 cc-14-18/mencion/M-UT07-205 cc-14-18/mencion/M-UT08-217 cc-14-18/mencion/M-UT09-529 cc-14-18/mencion/M-UT10-508 cc-14-18/mencion/M-UT10-520 cc-14-18/mencion/M-UT10-528 cc-14-18/mencion/M-UT11-512 cc-14-18/mencion/M-UT12.a-505 cc-14-18/mencion/M-UT17-803 cc-14-18/mencion/M-UT17-805 cc-14-18/mencion/M-UT17-814 cc-14-18/mencion/M-UT19-812
    Argumento: Pueblo de Tinta, cabecera del partido homónimo («En el pueblo de Tinta, en primero de agosto de 1806»). HGIS de las Indias src_id 6000357 (WHG 177060; -71.406, -14.145; jurisdicción de Tinta 1701–1808), Wikidata Q2435935 y TGN 9227290 (P1667 del elemento de Wikidata), verificados por la auditoría I. Se descartan los homónimos Tinta de Cajatambo (6000993) y Tintay. El texto usa «Tinta» con cuatro referentes que no deben fusionarse con este: el pueblo; el partido («partido de este nombre», «partido de Tinta»; WHG 139803); la «compañía de Tinta de Milicias» o «regimiento de Tinta»; y el «Ayllu Tinta». Revisada tras la auditoría I (2026-11-13). Ampliada el 2026-11-14 (registro base de claude-opus-5-5, 2026-11-13): se añaden solo las menciones que NOMBRAN el pueblo: «vecino del pueblo de Tinta» (UT05), «indio del Pueblo de Tinta» (UT07), «yndio originario del Pueblo de Tinta» (UT08), «yndio del Pueblo de Tinta» (UT09), «fuera de Matricula en el pueblo de Tinta» y «practicar en el Pueblo de Tinta» (UT10), «En el pueblo de Tinta, Veinte y tres dias» (UT11), «vecino Español de este pueblo de Tinta» (UT12.a), «no hay tal hombre en el pueblo de Tinta», «regresado … al pueblo de Tinta», «evacuarlo en el pueblo de Tinta» (UT17), «Yndio del Pueblo de Tinta» (UT19); y las dos datas «doy mi certificación en Tinta agosto cinco» (UT02) y «Tinta 23. de Septiembre de 1806» (UT10), donde «Tinta» a secas es lugar de data y el mismo día 23 otra pieza se data «En el pueblo de Tinta». Quedan fuera: «Al subdelegado de Tinta» (partido, R-partido-tinta-deicticos), «puesto de Tinta» (UT03, sin enlazar) y los deícticos «este pueblo», «dicho Pueblo» (R-tinta-deicticos).
RECONSTRUCCIÓN ««aquel Regio sonado» (P23) es la Real Audiencia del Cusco» — creencia: posible; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT05-208 cc-14-18/mencion/M-UT08-208 cc-14-18/mencion/M-UT16b-812
    Argumento: Hipótesis. El cura pide que su informe se «pueda exponer a aquel Regio sonado nodudando y como oraculos de la ley sabran comtrapesar … as representaciones o diosas de Ortis o Guancachoque» (UT16.b). «Regio sonado» se lee como «Regio Senado», tratamiento usual de una Audiencia, y lo de oráculos de la ley conviene a sus ministros; el asunto se ventila ante el presidente y el fiscal de «esta Real Audiencia» (UT05, UT08). Pero la lectura es conjetural y la causa se tramita en rigor en el Gobierno e Intendencia (R-gobierno-cusco), no en la sala de la Audiencia: queda en «posible».
RECONSTRUCCIÓN ««aquella provincia» (P06) es el partido de Tinta» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT05-204 cc-14-18/mencion/M-UT06-207
    Argumento: Hipótesis de identidad entre dos términos. Huancachoque, en el Cusco, dice no haber tributado «por haber estado empleado en las milicias de aquella provincia» (UT06); la misma pieza lo presenta como «vecino del pueblo de Tinta, partido de este nombre» (UT05). Sus certificantes sitúan ese servicio en el «regimiento de este partido» (UT01) o «regimiento de Tinta» (UT02: «ha estado soldado en mi compañía más de cinco años»). Tras 1784 los partidos eran las antiguas provincias o corregimientos y el uso de «provincia» persistió (conocimiento externo; HGIS registra el mismo territorio JUPECUTI como corregimiento de Canas y Canchis y luego subdelegación de Tinta). El texto no dice «provincia de Tinta»; por eso no se funde en R-partido-tinta.
RECONSTRUCCIÓN ««este partido», «aquel partido», «partido de mi cargo» y «subdelegado de Tinta» designan el partido de Tinta» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-203 cc-14-18/mencion/M-UT07-207 cc-14-18/mencion/M-UT09-503 cc-14-18/mencion/M-UT09-537 cc-14-18/mencion/M-UT13-502 cc-14-18/mencion/M-UT16b-805 cc-14-18/mencion/M-UT18-818
    Argumento: Subsidiaria de R-partido-tinta (comparte el ancla M-UT09-503). «del regimiento de este partido» (UT01): la pieza se data «En el pueblo de Tinta» y el sargento es de la «compañía de Tinta». «en la revisita de aquel partido» (UT07): el fiscal escribe en el Cusco sobre un «indio del Pueblo de Tinta» y pide luego orden al «subdelegado del partido de Tinta». «Al subdelegado de Tinta» (UT09): dirección del oficio; el auto de la víspera remite «al Juez subdelegado del partido de Tinta», de modo que aquí «Tinta» es el partido y no el pueblo. «via en este partido» (UT13, pasaje muy corrupto) y «comparecio ante mi D.Pedro de la Mata………. de este partido» (UT11) son del juez que actúa en el pueblo de Tinta. «vuestro vien conoce el partido nos hallamos» (UT16.b): el cura de Tinta al subdelegado. «la tranquilidad publica del partido de mi cargo» (UT18): lo firma Pedro de la Mata, cuyo oficio el fiscal llama «del subdelegado del partido de Tinta» (UT19). Ninguna nombra el partido: inferencia por lugar de redacción y cargo del autor.
RECONSTRUCCIÓN ««este pueblo», «dicho Pueblo», «aquel Pueblo», «el pueblo» designan el pueblo de Tinta» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-007 cc-14-18/mencion/M-UT06-201 cc-14-18/mencion/M-UT06-203 cc-14-18/mencion/M-UT11-501 cc-14-18/mencion/M-UT11-506 cc-14-18/mencion/M-UT15-810 cc-14-18/mencion/M-UT16a-809 cc-14-18/mencion/M-UT17-801 cc-14-18/mencion/M-UT17-818 cc-14-18/mencion/M-UT18-813 cc-14-18/mencion/M-UT18-816
    Argumento: Subsidiaria de R-tinta (comparte con ella el ancla M-UT01-007): reúne las menciones que no nombran el pueblo y cuyo referente lo fija un antecedente explícito o el lugar de redacción. (a) Antecedente en la misma pieza: P06 abre con «vecino del pueblo de Tinta» y sigue «a ser expelido del pueblo», «los alaridos aterrorizaron el pueblo» (UT06; en la segunda «el pueblo» vale también por sus habitantes); P24 «ausente de este pueblo Juan Cazorla … que no hay tal hombre en el pueblo de Tinta» (misma oración, UT17); P27 «evacuarlo en el pueblo de Tinta … a ver sucedido en Derechos [dicho] Pueblo», «cura interino de dicho -Pueblo», «esta expuesto aquel Pueblo» (UT17–UT18). (b) Lugar de redacción o antecedente de otra pieza: P16 «separarlo de este que Pueblo», «se retire, de este Pueblo» (UT11) no lleva data, pero ejecuta la providencia P14 («diligencias que se deben practicar en el Pueblo de Tinta»), sigue a la nota datada «Tinta 23. de Septiembre» y precede a la declaración tomada «En el pueblo de Tinta» ese mismo día; P22 «en este pueblo Manuel Guancachoque Oriundo de el» (UT15): Huancachoque es «Indio originario y vecino del pueblo de Tinta» (UT05); P23 «hallandose vuestra presente en este pueblo» (UT16.a): lo escribe el «cura interino de dicho -Pueblo» de Tinta (UT18). El grupo (b) es inferencia y por eso la creencia es «probable». Los identificadores externos están en R-tinta.
RECONSTRUCCIÓN ««las milicias de aquella provincia» (P06) son el regimiento de Tinta» — creencia: posible; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT01-202 cc-14-18/mencion/M-UT02-201 cc-14-18/mencion/M-UT06-206
    Argumento: Hipótesis de fusión sobre R-regimiento-tinta. Huancachoque alega «haber estado empleado en las milicias de aquella provincia» (UT06) y Santiago Cazorla certifica que «ha estado soldado en mi compañía más de cinco años», compañía del «regimiento de Tinta» (UT02). El servicio es el mismo, pero «las milicias de aquella provincia» puede designar el conjunto de las milicias del partido y no un regimiento determinado: «posible».

  Cusco (ciudad), sede de la Real Audiencia y la Intendencia: HGIS:6000002 http://vocab.getty.edu/tgn/7005819
  Cusco (ciudad), sede de la Real Audiencia y la Intendencia: HGIS:6000002 http://www.wikidata.org/entity/Q5582862
  Cusco (ciudad), sede de la Real Audiencia y la Intendencia: HGIS:6000002 https://whgazetteer.org/places/176704/detail
  Gobierno e Intendencia del Cusco (territorio): HGIS:PRPECU00 http://www.wikidata.org/entity/Q5918759
  Gobierno e Intendencia del Cusco (territorio): HGIS:PRPECU00 https://whgazetteer.org/places/140068/detail
  Partido de Tinta (subdelegación de la Intendencia del Cusco): HGIS:JUPECUTI https://whgazetteer.org/places/139803/detail
  San Pedro de Cacha (pueblo): HGIS:6000358 http://vocab.getty.edu/tgn/8712075
  San Pedro de Cacha (pueblo): HGIS:6000358 http://www.wikidata.org/entity/Q13190677
  San Pedro de Cacha (pueblo): HGIS:6000358 https://whgazetteer.org/places/177061/detail
  Sicuani (pueblo), lugar de data de las providencias e informe del subdelegado: HGIS:6000365 http://vocab.getty.edu/tgn/1024771
  Sicuani (pueblo), lugar de data de las providencias e informe del subdelegado: HGIS:6000365 http://www.wikidata.org/entity/Q4419079
  Sicuani (pueblo), lugar de data de las providencias e informe del subdelegado: HGIS:6000365 https://whgazetteer.org/places/177068/detail
  Tinta (pueblo): HGIS:6000357 http://vocab.getty.edu/tgn/9227290
  Tinta (pueblo): HGIS:6000357 http://www.wikidata.org/entity/Q2435935
  Tinta (pueblo): HGIS:6000357 https://whgazetteer.org/places/177060/detail
```

## PC08

```text
PREGUNTA: ¿Qué afirmó cano en su certificación de agosto y qué en su declaración de septiembre?
RESPUESTA (A): 54 afirmaciones en certificación, declaración jurada.

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
AFIRMACIÓN A-UT01-201: ejerce o ejerció un cargo → sargento (sin precisar)
    «Yo el sargento Don Isidro Cano de esta compañía»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-202: participa en un hecho → H-p01-maltrato
    «al denunciante mayor Guancachoque lo esta lo estropearon sus enemigos lo tendieron cuasi muerto»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-203: participa en un hecho → H-p01-maltrato
    «lo esta lo estropearon sus enemigos lo tendieron cuasi muerto»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-204: participa en un hecho → H-p01-prision
    «al denunciante mayor Guancachoque lo esta lo estropearon sus enemigos lo tendieron cuasi muerto y lo pusieron a la carcel»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-205: lugar del hecho → la carcel
    «lo pusieron a la carcel a esa noche»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-206: participa en un hecho → H-p01-alboroto
    «todos los indios se alzaron a media noche todos con garrotes a acabar al dicho denunciante»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-207: participa en un hecho → H-p01-alboroto
    «todos con garrotes a acabar al dicho denunciante»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-208: motivo o causa del hecho → a acabar al dicho denunciante
    «todos con garrotes a acabar al dicho denunciante»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-209: motivo o causa del hecho → hacen una matanza a los españoles
    «animados en animas conformes, hacen una matanza a los españoles»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-210: lugar del hecho → la plaza
    «porque estaba cubierto de indiada la plaza»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-211: participa en un hecho → H-p01-alzamiento-orey
    «mando dicho Chuquitapa cargando. [....] y Chicha ay se alzaron contra el capitan don Miguel Orey»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-212: fecha u hora del hecho → En tiempo del señor corregidor don Antonio Reparas
    «En tiempo del señor corregidor don Antonio Reparas, mando dicho Chuquitapa»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-213: ejerce o ejerció un cargo → corregidor
    «En tiempo del señor corregidor don Antonio Reparas»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-214: ejerce o ejerció un cargo → capitán
    «se alzaron contra el capitan don Miguel Orey»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-215: participa en un hecho → H-p01-alzamiento-orey
    «se alzaron contra el capitan don Miguel Orey»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-216: fecha u hora del hecho → a las ocho de la noche
    «don Miguel Orey a las ocho de la noche con pedradas»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-217: número de participantes → cerca de sesenta indios
    «con pedradas palos cerca de sesenta indios»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-218: participa en un hecho → H-p01-alzamiento-orey
    «con pedradas palos cerca de sesenta indios»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-219: fecha u hora del hecho → otra vuelta de dos horas
    «y otra vuelta de dos horas. Con mas aumento de indios»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-220: lugar del hecho → su tienda
    «pedrearon su tienda hasta quebrar la puerta»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-221: participa en un hecho → H-p01-alzamiento-orey
    «su mujer resien parida le causo un horror»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-222: participa en un hecho → H-p01-despojo
    «A los indios perjudica quitando sus chacras o tierras»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-223: participa en un hecho → H-p01-despojo (sujeto elíptico resuelto por el anotador)
    «A los indios perjudica quitando sus chacras o tierras»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-224: participa en un hecho → H-p01-faenas
    «y les harrea con fainas a los tributarios»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-225: participa en un hecho → H-p01-faenas (sujeto elíptico resuelto por el anotador)
    «y les harrea con fainas a los tributarios»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-226: calificación de conducta o carácter → no estamos libres de sus traiciones
    «porque no estamos libres de sus traiciones, del dicho alzado»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: lo vio; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-227: calificación de conducta o carácter → Nada respeta ni hace aprecio al señor gobernador, subdelegado (sujeto elíptico resuelto por el anotador)
    «Nada respeta ni hace aprecio al señor gobernador, subdelegado»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-228: ejerce o ejerció un cargo → gobernador (sin especificar)
    «ni hace aprecio al señor gobernador, subdelegado»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-229: ejerce o ejerció un cargo → subdelegado
    «ni hace aprecio al señor gobernador, subdelegado»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-230: solicita → pongan remedio
    «pongan remedio los señores jueces»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-231: presta juramento → una señal de cruz como fiel christiano
    «juro una señal de cruz como fiel christiano»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT01-232: participa en un hecho → H-p01-alboroto
    «hacen una matanza a los españoles»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT11-001: la firma es suya → Ysidro Cano
    «dijo que la firma Que dice Isidro Cano es suya propia»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-002: se ratifica en el contenido → Ysidro Cano
    «preso ser cierto todo lo que en ella dice que le consta solo»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-003: ejerce o ejerció un cargo → comisionado (de Túpac Amaru) (sujeto elíptico resuelto por el anotador)
    «en tiempo del rebelde Tupa amaro fue Comisionado por este»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO; responde a A-UT01-001
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-004 [NIEGA]: ejerce o ejerció un cargo → coronel (de Túpac Amaru) (sujeto elíptico resuelto por el anotador)
    «Comisionado por este y no coronel como expone en su certificación»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO; responde a A-UT01-001
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-005: fecha u hora del hecho → a media noche
    «se alzaron a media noche armados con garrotes para acabar con este, y hacer matalo de los españoles poniendo guardias a las puertas de estos no le cons ta al que declara si no porque se lo dijo su segundo sargento Santiago Casorla»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO; responde a A-UT01-003; según lo que le dijo «Santiago Casorla» (discurso referido)
    Fundamento invocado: de oídas; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-510: ejerce o ejerció un cargo → corregidor
    «sucedió en tiempo de corregidor Don Andres»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-511: participa en un hecho → H-p18-prision
    «de la noche que estuvo preso Guancachoque»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-512: participa en un hecho → H-p18-alboroto
    «todos los Yndios se alzaron a media noche armados con garrotes para acabar con este»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO; según lo que le dijo «Santiago Casorla» (discurso referido)
    Fundamento invocado: de oídas; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-513: participa en un hecho → H-p18-golpes
    «le siguieron pegando los Yndios hasta que lo»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-514: participa en un hecho → H-p18-golpes
    «le siguieron pegando los Yndios hasta que lo»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-515: participa en un hecho → H-p18-prision
    «habiendo mandado Esta ponerlo en la caecel a Guancachoque»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT12a-001: motivo o causa del hecho → este fue a su casa suplicandole
    «dijo que la dado porque este fue a su casa supli candole»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT12.a, folio no consta en la transcripción
AFIRMACIÓN A-UT12a-002 [NIEGA]: le comprenden (o no) las generales de la ley → le comprenden los Generales de la Ley
    «que no le comprenden. los Generales de la Ley»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT12.a, folio no consta en la transcripción
AFIRMACIÓN A-UT12a-501: lugar del hecho → la Real cárcel
    «pusieron en la Real cárcel que es cuando pude»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT12.a, folio no consta en la transcripción
AFIRMACIÓN A-UT12a-502: edad declarada → quarenta años
    «expreso ser de edad de quarenta años»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT12.a, folio no consta en la transcripción
AFIRMACIÓN A-UT12a-503: se ratifica en el contenido → Ysidro Cano
    «vajo del juramento dicho tiene en que se afirma y ratifica»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT12.a, folio no consta en la transcripción
AFIRMACIÓN A-UT12a-504: solicita → le diere la dicha Certificacion
    «este fue a su casa supli candole que respecto a que sabia todos los parajes que expone en ella le diere la dicha Certificacion»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO; según lo que le dijo «Manuel Guancachoque» (discurso referido)
    Fundamento invocado: de oídas; fuerza institucional: testimonial; UT12.a, folio no consta en la transcripción
AFIRMACIÓN A-UT12a-505 [NIEGA]: motivo o causa del hecho → plata ni otro agasajo
    «y que nomledio ninguna plata ni otro agasajo alguno»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT12.a, folio no consta en la transcripción

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Isidro Cano, sargento de milicias, vecino español de Tinta» — creencia: verdadero; autor: claude-opus-5-5; fecha: 2026-11-13
    Deriva de: cc-14-18/mencion/M-UT01-001 cc-14-18/mencion/M-UT01-006 cc-14-18/mencion/M-UT11-001 cc-14-18/mencion/M-UT12.a-001 cc-14-18/mencion/M-UT13-506
    Argumento: En su declaración (P18) reconoce ante el juez la firma de la certificación P01: «la firma Que dice Isidro Cano es suya propia y la que acostumbra hacer» (UT11); nombre idéntico y misma causa. Santiago Cazorla lo llama «primer sargento ysidro cano» (P20, UT13). Revisada tras la auditoría I (2026-11-13).
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
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO; responde a A-UT01-001
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT14-006: ejerce o ejerció un cargo → coronel (de Túpac Amaru)
    «con motibo de saber q de andres chuquitaza fue en tiempo del rebelde tupa-amaru coronel y comisionado»
    Afirmante: «fernando ore» (declarante) [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción]; declaración jurada P21, fecha escrita «Seguidamente»; ante: el grl. sub delegado; redacta: no consta; firma la pieza: conmigo; responde a A-UT03-001
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT14, folio no consta en la transcripción

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Andrés Chuquitapa, cacique y recaudador de tributos de Tinta» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT00-203 cc-14-18/mencion/M-UT01-003 cc-14-18/mencion/M-UT01-004 cc-14-18/mencion/M-UT01-222 cc-14-18/mencion/M-UT02-210 cc-14-18/mencion/M-UT02-222 cc-14-18/mencion/M-UT02-230 cc-14-18/mencion/M-UT03-002 cc-14-18/mencion/M-UT04-204 cc-14-18/mencion/M-UT04-207 cc-14-18/mencion/M-UT05-002 cc-14-18/mencion/M-UT05-210 cc-14-18/mencion/M-UT05-212 cc-14-18/mencion/M-UT06-001 cc-14-18/mencion/M-UT06-205 cc-14-18/mencion/M-UT06-209 cc-14-18/mencion/M-UT06-215 cc-14-18/mencion/M-UT06-220 cc-14-18/mencion/M-UT07-001 cc-14-18/mencion/M-UT07-213 cc-14-18/mencion/M-UT09-504 cc-14-18/mencion/M-UT09-531 cc-14-18/mencion/M-UT10-509 cc-14-18/mencion/M-UT10-515 cc-14-18/mencion/M-UT10-532 cc-14-18/mencion/M-UT11-505 cc-14-18/mencion/M-UT11-510 cc-14-18/mencion/M-UT12.b-505 cc-14-18/mencion/M-UT12.b-511 cc-14-18/mencion/M-UT14-002 cc-14-18/mencion/M-UT14-523 cc-14-18/mencion/M-UT14-532 cc-14-18/mencion/M-UT15-002 cc-14-18/mencion/M-UT16b-001 cc-14-18/mencion/M-UT16b-801 cc-14-18/mencion/M-UT16b-804 cc-14-18/mencion/M-UT17-006 cc-14-18/mencion/M-UT17-829 cc-14-18/mencion/M-UT18-803 cc-14-18/mencion/M-UT18-807 cc-14-18/mencion/M-UT18-812 cc-14-18/mencion/M-UT19-805 cc-14-18/mencion/M-UT19-813 cc-14-18/mencion/M-UT19-815 cc-14-18/mencion/M-UT19-818
    Argumento: Todas las menciones designan al cacique y recaudador de Tinta contra quien se dirige la queja; casi todas llevan anáfora explícita («dicho Chuquiitapa», «dicho Chuquitapa») o nombre y tratamiento. Grafías reales: Chuquiitapa, Chuquitapa, Choquitapa, Choquetapa, Chukitapa, Chuquitape, chuquitaza, chuquitapa. Las menciones del pleito de 1806 deben separarse de las que le atribuyen hechos anteriores a 1780: M-UT01-004 (tiempo del corregidor Reparaz), M-UT03-002 y M-UT14-002 (coronel o comisionado de Túpac Amaru); Cano rebaja en su declaración lo dicho en su certificación («fue Comisionado por este y no coronel», UT11). Esas tres se mantienen aquí, pero se registra la hipótesis rival R-chuquitapa-1780-pariente. No se incluyen «Chiquitas» (ver R-chiquitas) ni «el dicho chuquitapa» y «corral de chuquitapa» de P21 (UT14), que pertenecen al relato del motín de tiempos de Reparaz, ni las descripciones sin nombre («el cacique», «dicho recaudador»). Revisada tras la auditoría I (2026-11-13). Ampliada el 2026-11-14 (claude-fable-5-2): se añaden 19 menciones. Con nombre: «corral de chuquitapa» y «el dicho chuquitapa» (P21). Por cargo y con antecedente expreso en la misma pieza: «Este mismo cacique» y «el robo. del cacique» (P03, tras «cacique don Andrés Chukitapa»), «el referido recaudador» (P07), «el citado re caudador» (P14), «Recaudador» y «su recaudador» (P27), «dicho recaudador» y «mencionado recaudador» (P29), «su casique» ×2 (P23, tras «su casique y alcalde mayor Don Andres Chuquitapa»), «recaudador» de P06 (M-UT05-210, tras «el recaudaderor Don Andres Choquitapa» en el mismo período). Por el hecho: «el total robo del cacique» y «el robo de mi cacique» (P05) y «el robo del cacique» (P19) no llevan nombre en su pieza, pero es el robo denunciado por Huancachoque, que la causa atribuye a Chuquitapa. Anáforas: «el denominado» (M-UT05-212, pasaje deteriorado: quien «dio queja al subdelegado» al día siguiente de probarse la ocultación; Mata confirma que el insultado fue «el Recaudador», P27), «aquel» de P06 (M-UT06-220: «ni por Chuquitapa ni por otros de su compañía … dinero que ha usurpado aquel») y «dicho alzado» (M-UT01-222: «no estamos libres de sus traiciones, del dicho alzado», en el párrafo sobre los agravios del cacique a los indios; lectura algo menos segura). M-UT02-222, M-UT14-523 y M-UT14-532 le atribuyen hechos anteriores a 1780 y entran también en la hipótesis rival R-chuquitapa-1780-pariente. «Don Andres» de P18 (M-UT11-514) no se añade aquí: tiene dos lecturas rivales, R-don-andres-p18-es-chuquitapa y R-don-andres-p18-es-reparaz. Reconstrucción propuesta originalmente por claude-opus-5-5 el 2026-11-13.

Afirmaciones relacionadas (no forman la disputa):
  A-UT01-002: «Isidro Cano» [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción] (certificación P01, UT01) → cómplice (de Túpac Amaru) (afirma) «lo mismo en el tiempo del rebelde. Tupa Amaro fue complice y coronel»
  A-UT02-304: «don Juan Quiñones» [= «Don Juan Quiñones» es un nombre puesto por quien redactó la certificación P03 (H1) | «Don Juan Quiñones» es una persona real que no reside en Tinta (H2) | «Don Juan Quiñones», teniente alguacil: existencia de la persona (en disputa) | «don Juan Quiñones» de P03 y de P24 son el mismo nombre (correferencia), según reconstrucción] (certificación P03, UT02) → cacique (afirma) «los indios del cacique don Andrés Chukitapa»
  A-UT03-002: «Fernando Orue» [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción] (certificación P04, UT03) → comisionado (de Túpac Amaru) (afirma) «en tiempo de su pariente Tupaamaro fue coronel, comecionado»
  A-UT05-001: «Manuel Huancachoque» [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción] (petición P06, UT05) → recaudador de tributos (afirma) «tenia ocultos el recaudaderor Don Andres Choquitapa»
  A-UT05-212: «Manuel Huancachoque» [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción] (petición P06, UT05) → recaudador de tributos (afirma) «a presencia del recaudador y juez subdelegado»
  A-UT07-001: «Gómez del Rio» [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción] (vista fiscal P07, UT07) → recaudador de tributos (afirma) «contra el Recaudador de Tributos Son Andres Chuquitapa»
  A-UT07-219: «Gómez del Rio» [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción] (vista fiscal P07, UT07) → recaudador de tributos (afirma) «el referido recaudador incomode»
  A-UT09-502: «Castilla» [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción] (auto P10, UT09) → recaudador de tributos (afirma) «notificando primero al Recaudado Don Andrés Chuquitapa»
  A-UT09-520: «Ruiz de Castilla» [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción] (oficio P13, UT09) → recaudador de tributos (afirma) «Don Andrés Choquetapa Recaudador de Reales Tributos de dicho Pueblo»
  A-UT10-506: «Pedro de la Mara» [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción] (decreto P14, UT10) → recaudador de tributos (afirma) «su recaudador de tributos Dn Andres Chuquitapa»
  A-UT10-518: «Pedro de la Mara» [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción] (auto cabeza de proceso P16, UT10) → recaudador de tributos (afirma) «notifiquese al recaudaor de tributos D. Andres Chuquitapa»
  A-UT11-003: «Ysidro Cano» [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción] (declaración jurada P18, UT11) → comisionado (de Túpac Amaru) (afirma) «en tiempo del rebelde Tupa amaro fue Comisionado por este»
  A-UT12b-505: «Mariano Casorla» [= El declarante de P19 es Martín Cazorla (hipótesis A) | El declarante de P19 es un Mariano Casorla distinto de Martín (hipótesis B) | «el Gobernador Señor Don Mariano Casorla» (P19) es una mala lectura de «el granadero … Martin Casorla», según reconstrucción] (declaración jurada P19, UT12.b) → cacique (afirma) «denunciado el robo del cacique , en favor de la Real hacienda»
  A-UT14-007: «fernando ore» [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción] (declaración jurada P21, UT14) → comisionado (de Túpac Amaru) (afirma) «con motibo de saber q de andres chuquitaza fue en tiempo del rebelde tupa-amaru coronel y comisionado»
  A-UT16b-001: «parroco interino» [= Agustín Valdés, cura interino de Tinta, según reconstrucción] (informe P23, UT16.b) → cacique (afirma) «su casique y alcalde mayor Don Andres Chuquitapa»
  A-UT16b-002: «parroco interino» [= Agustín Valdés, cura interino de Tinta, según reconstrucción] (informe P23, UT16.b) → alcalde mayor (de indios) (afirma) «su casique y alcalde mayor Don Andres Chuquitapa»
  A-UT17-003: «Pedro de la Mata» [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción] (informe P27, UT17) → recaudador de tributos (afirma) «recaudador de tributos de los Ayllus Tinta y Ucho Don Andres Chuquitapa»
  A-UT17-812: «Pedro de la Mata» [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción] (informe P27, UT17) → recaudador de tributos (afirma) «insultar al Recaudador con palabras injuriosas»
  A-UT18-812: «Pedro de la Mata» [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción] (informe P27, UT18) → recaudador de tributos (afirma) «sublevar a todos los Indios contra su recaudador»
  A-UT19-806: «Muñoz» [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción] (auto P28, UT19) → recaudador de tributos (afirma) «con el recaudador de tributos Don Andres Chuquitapa»
  A-UT19-809: «Gonzalo del Rio» [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción] (vista fiscal P29, UT19) → recaudador de tributos (afirma) «contra el recaudador de tributos Andres chuquitapa»
Ninguna actuación de fuerza dictaminadora o resolutiva se pronuncia sobre este punto (calculado).
```

## PC10

```text
PREGUNTA: ¿Quién redactó las certificaciones de agosto?
RESPUESTA (DISPUTA): 6 piezas con redactor atribuido (P01: Guancachoque, Manuel Guancoichoque; P03: Guancachoque, Manuel Guancoichoque; P04: Guancachoque, Manuel Guancoichoque, guancachay, guasscachoque, un hijo suyo; P05: Guancachoque, Manuel Guancoichoque, Simon Arce; P06: al que se lo hizo; P23: Doctor Don Agustin Valdes); 2 firmas negadas.

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT08-216: redactó la pieza → al que se lo hizo
    «según las instrucciones que comunico al que se lo hizo»
    Afirmante: «Manuel Guancachoque» (declarante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; reconocimiento y ratificación P09, fecha escrita «en trece días del mees de Agosto de mil ochocientos seis años»; ante: Don Manuel Galeano; redacta: no consta; firma la pieza: Don Valencia / Galeano / Juan Clemente Jordan / Manuel Guancachoque / Marcos Salcedo
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT08, folio no consta en la transcripción
AFIRMACIÓN A-UT12b-002: redactó la pieza → Simon Arce
    «mando el que declara a Simon Arce que pusiere en un papelito lo mis mo que relata en la citada certificación»
    Afirmante: «Mariano Casorla» (declarante) [= El declarante de P19 es Martín Cazorla (hipótesis A) | El declarante de P19 es un Mariano Casorla distinto de Martín (hipótesis B) | «el Gobernador Señor Don Mariano Casorla» (P19) es una mala lectura de «el granadero … Martin Casorla», según reconstrucción]; declaración jurada P19, fecha escrita «Ynmediatamente»; ante: ante mi; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT12.b, folio 20
AFIRMACIÓN A-UT12b-508: redactó la pieza → Simon Arce
    «no los puso el en el papelito que mando hacer a Simon Arce»
    Afirmante: «Mariano Casorla» (declarante) [= El declarante de P19 es Martín Cazorla (hipótesis A) | El declarante de P19 es un Mariano Casorla distinto de Martín (hipótesis B) | «el Gobernador Señor Don Mariano Casorla» (P19) es una mala lectura de «el granadero … Martin Casorla», según reconstrucción]; declaración jurada P19, fecha escrita «Ynmediatamente»; ante: ante mi; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT12.b, folio 20
AFIRMACIÓN A-UT14-002: redactó la pieza → un hijo suyo
    «bajo a un hijo suyo q la pusieron»
    Afirmante: «fernando ore» (declarante) [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción]; declaración jurada P21, fecha escrita «Seguidamente»; ante: el grl. sub delegado; redacta: no consta; firma la pieza: conmigo
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT14, folio no consta en la transcripción
AFIRMACIÓN A-UT14-003: redactó la pieza → guasscachoque
    «como ha puesto guasscachoque en la citada certificacion»
    Afirmante: «fernando ore» (declarante) [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción]; declaración jurada P21, fecha escrita «Seguidamente»; ante: el grl. sub delegado; redacta: no consta; firma la pieza: conmigo
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT14, folio no consta en la transcripción
AFIRMACIÓN A-UT15-806: redactó la pieza → guancachay
    «motivo a decirle a guancachay q pusiera en la certificaz lo q quisiese»
    Afirmante: «fernando ore» (declarante) [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción]; declaración jurada P21, fecha escrita «Seguidamente»; ante: el grl. sub delegado; redacta: no consta; firma la pieza: conmigo
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT15, folio no consta en la transcripción
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
AFIRMACIÓN A-UT18-814: redactó la pieza → Doctor Don Agustin Valdes
    «Por el informe que le pedí al cura interino de dicho -Pueblo Doctor Don Agustin Valdes»
    Afirmante: «Pedro de la Mata» (informante) [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; informe P27, fecha escrita «Siquani Noviembre 8 de 1806»; ante: no consta; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: resulta de lo actuado; fuerza institucional: informativa; UT18, folio no consta en la transcripción
AFIRMACIÓN A-UT19-821: redactó la pieza → Manuel Guancoichoque
    «por la malicia con que aparece aver formado dicha queja y los documentos que presento en su calificación»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-822: redactó la pieza → Manuel Guancoichoque
    «por la malicia con que aparece aver formado dicha queja y los documentos que presento en su calificación»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-823: redactó la pieza → Manuel Guancoichoque
    «por la malicia con que aparece aver formado dicha queja y los documentos que presento en su calificación»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-824: redactó la pieza → Manuel Guancoichoque
    «por la malicia con que aparece aver formado dicha queja y los documentos que presento en su calificación»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT19, folio 33

Disputa texto/afirmación: la pieza P04 muestra la firma «Fernando Orue» (M-UT03-004), y A-UT14-001 («fernando ore») lo niega: «no obstante que sabe firmar el declarante no quiso hacerlo»
Disputa texto/afirmación: la pieza P04 muestra la firma «Fernando Orue» (M-UT03-004), y A-UT15-807 («fernando ore») lo niega: «q el lo firmaria aunque no lo hise»
```

## PC11

```text
PREGUNTA: ¿Cuánto tiempo estuvo preso Huancachoque?
RESPUESTA (DISPUTA): Está en disputa por valores incompatibles. «dos días»: lo afirman «Manuel Huancachoque» [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción] (petición P06, UT06) || «esa misma noche ... al otro dia por la tarde»: lo afirman «Pedro de la Mata» [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción] (informe P27, UT18)

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT06-001: duración del hecho → dos días
    «yo me mantuve dos días preso»
    Afirmante: «Manuel Huancachoque» (denunciante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; petición P06, fecha escrita «CUSCO AGOSTO 22 DE 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: MANUEL HUANCACHOQQUE
    Fundamento invocado: lo padeció o hizo él mismo; fuerza institucional: alegación de parte; UT06, folio no consta en la transcripción
AFIRMACIÓN A-UT18-001: duración del hecho → esa misma noche ... al otro dia por la tarde
    «que lo guardasen en ella esa misma noche, al que puse en libertad al otro dia por la tarde»
    Afirmante: «Pedro de la Mata» (informante) [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; informe P27, fecha escrita «Siquani Noviembre 8 de 1806»; ante: no consta; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: lo padeció o hizo él mismo; fuerza institucional: informativa; UT18, folio no consta en la transcripción

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Prisión de Huancachoque en la cárcel de Tinta al día siguiente de concluir la numeración de los ayllus» — creencia: verdadero; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/hecho/H-p01-prision cc-14-18/hecho/H-p03-prision cc-14-18/hecho/H-p04-prision cc-14-18/hecho/H-p05-prision cc-14-18/hecho/H-p06-prision cc-14-18/hecho/H-p07-prision cc-14-18/hecho/H-p18-prision cc-14-18/hecho/H-p19-prision cc-14-18/hecho/H-p20-prision cc-14-18/hecho/H-p27-prision
    Argumento: La afirman el denunciante («yo me mantuve dos días preso», UT06) y el subdelegado que la ordenó («lo mande llevar a la cárcel», UT18); la corroboran la vista fiscal (P07), Cano en P18 («ponerlo en la caecel a Guancachoque») y el declarante de P19 («estando en la carcel aquel»). Ambas partes coinciden en la cronología («al siguiente día que prove la ocultación», UT05; «concluida el dia anterior la numeración», UT17); discrepan en la duración (PC11) y en la causa (venganza según el denunciante, insulto al recaudador según Mata), no en el hecho. Revisada tras la auditoría I (2026-11-13). Ampliada el 2026-11-14 (claude-fable-5-2): se añaden los hechos de prisión de las certificaciones P01 («lo pusieron a la carcel»), P03 («de los pelos nomás llevaron a la cárcel»), P04 («los indios llevaron preso a la cárcel») y P05 («El siguiente día de la revisita pidieron a la cárcel al denunciante», A-UT04-210, que repite la cronología de las dos partes), y el de la declaración jurada de Santiago Cazorla, P20 («esa noche que estubo preso guancachoque», A-UT13-506). Las cuatro certificaciones atribuyen la conducción a «los indios» y callan la orden del subdelegado; no son independientes del denunciante (según Mata, P27, las hizo él mismo; auditoría I, §3.1). P20 sí es jurada e independiente en cuanto al hecho de la noche en la cárcel. Nadie niega la prisión. Este registro reúne el encierro; los golpes de la conducción van aparte (R-agresion-dia-prision y su rival R-golpes-conduccion-carcel) y la presencia nocturna ante la cárcel, en R-alboroto-carcel. Duración: «dos días» según el denunciante (A-UT06-001); una noche y hasta «al otro dia por la tarde» según Mata (A-UT18-001); Cano y Santiago Cazorla hablan de «la noche que estuvo preso». Reconstrucción propuesta originalmente por claude-opus-5-5 el 2026-11-13.
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
RESPUESTA (NC): El expediente no lo dice: constan 20 órdenes resolutivas y ninguna afirmación que responda a ellas (ejecución o cumplimiento).

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT09-504: ordena o manda → notificando primero al Recaudado Don Andrés Chuquitapa
    «para que notificando primero al Recaudado Don Andrés Chuquitapa como pide dicho Señor»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-505: ordena o manda → ceparandolo en caso necesario que altas leguas en contrario fuera del pueblo
    «ceparandolo en caso necesario que altas leguas en contrario fuera del pueblo»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-506: ordena o manda → proceda con la cautela y prudencia que exige el asunto
    «proceda con la cautela y prudencia que exige el asunto»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-507: ordena o manda → a recivido la sumaria informasion correspondiente
    «a recivido la sumaria informasion correspondiente bajo las formalidades de escrito»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-508: ordena o manda → que los cuyos otros se acompañan en las fojas antecedentes de ratifiquen y declaren
    «haciendo al mismo tiempo que los cuyos otros se acompañan en las fojas antecedentes de ratifiquen y declaren»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-509: ordena o manda → cuydando de que a dicho querello no se le incomode ni trate mal
    «cuydando de que a dicho querello no se le incomode ni trate mal»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-510: ordena o manda → lo remita con su informe
    «lo remita con su informe»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-511: ordena o manda → oyendo sobre ellos al Apoderado Fiscal ynforme por ceparado
    «por lo que toca a la denuncia de tributarios y solicitud del denunciante, oyendo sobre ellos al Apoderado Fiscal ynforme por ceparado»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT10-514: ordena o manda → Desglocese de este Expediente, y agreguese a el de la primera denuncia
    «Desglocese de este Expediente, y agreguese a el de la primera denuncia»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-515: ordena o manda → Procedase por mi à tomar la información Correspondiente
    «Procedase por mi à tomar la información Correspondiente sobre los hechos que ha expuesto el citado Guancachoque»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-516: ordena o manda → hagase el correspondiente. informe, y dese la Cuenta Ordenada
    «con lo que resulte hagase el correspondiente. informe, y dese la Cuenta Ordenada por . Decreto de 27 de Agosto»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-519: ordena o manda → que mi si mi por medio de otro alguno incomode ni infiera perjuicio, Guancachoque, en odio de su denuncia
    «notifiquese al recaudaor de tributos D. Andres Chuquitapa; que mi si mi por medio de otro alguno incomode ni infiera perjuicio, Guancachoque, en odio de su denuncia»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; auto cabeza de proceso P16, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT11-502: ordena o manda → se retire, de este Pueblo à distan. cia de quatro leguas
    «haga de Saber a Chuquitapa se retire, de este Pueblo à distan. cia de quatro leguas»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; auto cabeza de proceso P16, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-503: ordena o manda → haga de Saber a Chuquitapa se retire
    «haga de Saber a Chuquitapa se retire, de este Pueblo à distan. cia de quatro leguas (interin de»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; auto cabeza de proceso P16, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT17-803: ordena o manda → esperece su llegada para recibirle la declaración Respectiva sobre el Asunto
    «esperece su llegada para recibirle la declaración Respectiva sobre el Asunto»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la nota del transcriptor «[Media rúbrica]» y no nombra a ninguna María | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P24, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT17-806: ordena o manda → diríjase con lo actuado y el correspondiente Informe al Muy Ilustrísima Señor Padre para su determinación
    «diríjase con lo actuado y el correspondiente Informe al Muy Ilustrísima Señor Padre para su determinación»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la nota del transcriptor «[Media rúbrica]» y no nombra a ninguna María | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P25, fecha escrita «Sicuani Noviembre 8 de 1806»; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT19-003: ordena o manda → contener los excesos y enemistad del yndio Guancachoque
    «a fin de contener los excesos y enemistad del yndio Guancachoque»
    Afirmante: «Muñoz» (autoridad que resuelve) [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción]; auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-801: ordena o manda → tome las providencias que estaba oportunas
    «librese la correspondiente orden al subdelegado del partido de tinta para que tome las providencias que estaba oportunas»
    Afirmante: «Muñoz» (autoridad que resuelve) [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción]; auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-802: ordena o manda → hasiendole asi mismo extender la subordinación y respeto que debe observar en lo sucesivo con los superiores
    «hasiendole asi mismo extender la subordinación y respeto que debe observar en lo sucesivo con los superiores»
    Afirmante: «Muñoz» (autoridad que resuelve) [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción]; auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-803: ordena o manda → bajo apersivimiento ... Tomará el gobierno las más serias providencias
    «bajo apersivimiento de que en el caso de residencia To- Tomará el gobierno las más serias providencias»
    Afirmante: «Muñoz» (autoridad que resuelve) [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción]; auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
```

## PC14

```text
PREGUNTA: ¿A qué hora fue el alboroto ante la cárcel y cuántos indios participaron?
RESPUESTA (DISPUTA): Está en disputa por valores incompatibles. «Esa misma noche»: lo afirman «Martin Cazorla» [= El declarante de P19 es Martín Cazorla (hipótesis A) | Martín Cazorla, soldado granadero | «el Gobernador Señor Don Mariano Casorla» (P19) es una mala lectura de «el granadero … Martin Casorla», según reconstrucción] (certificación P05, UT04) || «a las dies de la noche»: nadie lo afirma; lo niegan «fernando ore» [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción] (declaración jurada P21, UT14) || «a las dies o a las once»: lo afirman «don Juan Quiñones» [= «Don Juan Quiñones» es un nombre puesto por quien redactó la certificación P03 (H1) | «Don Juan Quiñones» es una persona real que no reside en Tinta (H2) | «Don Juan Quiñones», teniente alguacil: existencia de la persona (en disputa) | «don Juan Quiñones» de P03 y de P24 son el mismo nombre (correferencia), según reconstrucción] (certificación P03, UT02) || «a las diez de la noche»: lo afirman «Fernando Orue» [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción] (certificación P04, UT03) || «a las nueve de la noche»: lo afirman «Manuel Huancachoque» [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción] (petición P06, UT06) || «a media noche»: lo afirman «Isidro Cano» [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción] (certificación P01, UT01); «Ysidro Cano» [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción] (declaración jurada P18, UT11) || «antes ayer»: lo afirman «Gómez del Rio» [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción] (vista fiscal P07, UT07) || «de noche»: lo afirman «Gómez del Rio» [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción] (vista fiscal P07, UT07) || «el primer puesto del gallo»: lo afirman «fernando ore» [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción] (declaración jurada P21, UT14)

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT01-003: fecha u hora del hecho → a media noche
    «esa noche todos los indios se alzaron a media noche todos con garrotes»
    Afirmante: «Isidro Cano» (certificante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; certificación P01, fecha escrita «en primero de agosto de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Isidro Cano
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT01, folio no consta en la transcripción
AFIRMACIÓN A-UT02-001: fecha u hora del hecho → a las dies o a las once
    «Esa misma noche a las dies o a las once se alzaron los indios en la plaza»
    Afirmante: «don Juan Quiñones» (certificante) [= «Don Juan Quiñones» es un nombre puesto por quien redactó la certificación P03 (H1) | «Don Juan Quiñones» es una persona real que no reside en Tinta (H2) | «Don Juan Quiñones», teniente alguacil: existencia de la persona (en disputa) | «don Juan Quiñones» de P03 y de P24 son el mismo nombre (correferencia), según reconstrucción]; certificación P03, sin fecha escrita; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Juan Cazorla
    Fundamento invocado: lo vio; fuerza institucional: testimonial; UT02, folio no consta en la transcripción
AFIRMACIÓN A-UT03-004: fecha u hora del hecho → a las diez de la noche
    «a las diez de la noche, peor alboroto»
    Afirmante: «Fernando Orue» (certificante) [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción]; certificación P04, sin fecha escrita; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Fernando Orue
    Fundamento invocado: lo vio; fuerza institucional: testimonial; UT03, folio no consta en la transcripción
AFIRMACIÓN A-UT04-212: fecha u hora del hecho → Esa misma noche
    «Esa misma noche se alzaron los Indios»
    Afirmante: «Martin Cazorla» (certificante) [= El declarante de P19 es Martín Cazorla (hipótesis A) | Martín Cazorla, soldado granadero | «el Gobernador Señor Don Mariano Casorla» (P19) es una mala lectura de «el granadero … Martin Casorla», según reconstrucción]; certificación P05, sin fecha escrita; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Martin Cazorla
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT04, folio no consta en la transcripción
AFIRMACIÓN A-UT06-002: fecha u hora del hecho → a las nueve de la noche
    «pero a las nueve de la noche se apareció una caterva de indios»
    Afirmante: «Manuel Huancachoque» (denunciante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; petición P06, fecha escrita «CUSCO AGOSTO 22 DE 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: MANUEL HUANCACHOQQUE
    Fundamento invocado: lo padeció o hizo él mismo; fuerza institucional: alegación de parte; UT06, folio no consta en la transcripción
AFIRMACIÓN A-UT07-209: fecha u hora del hecho → antes ayer
    «antes ayer precurado matarlo con alboroto de noche»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-210: fecha u hora del hecho → de noche
    «precurado matarlo con alboroto de noche»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT11-005: fecha u hora del hecho → a media noche
    «se alzaron a media noche armados con garrotes para acabar con este, y hacer matalo de los españoles poniendo guardias a las puertas de estos no le cons ta al que declara si no porque se lo dijo su segundo sargento Santiago Casorla»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, sargento de milicias, vecino español de Tinta, según reconstrucción]; declaración jurada P18, fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata; redacta: no consta; firma la pieza: PEDRO DE LA MATA / YSIDRO CANO; responde a A-UT01-003; según lo que le dijo «Santiago Casorla» (discurso referido)
    Fundamento invocado: de oídas; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT14-004: fecha u hora del hecho → el primer puesto del gallo
    «no fue a las dies de la noche como ha puesto guasscachoque en la citada certificacion, sino el primer puesto del gallo»
    Afirmante: «fernando ore» (declarante) [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción]; declaración jurada P21, fecha escrita «Seguidamente»; ante: el grl. sub delegado; redacta: no consta; firma la pieza: conmigo; responde a A-UT03-004
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT14, folio no consta en la transcripción
AFIRMACIÓN A-UT14-005 [NIEGA]: fecha u hora del hecho → a las dies de la noche
    «no fue a las dies de la noche como ha puesto guasscachoque en la citada certificacion»
    Afirmante: «fernando ore» (declarante) [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción]; declaración jurada P21, fecha escrita «Seguidamente»; ante: el grl. sub delegado; redacta: no consta; firma la pieza: conmigo; responde a A-UT03-004
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT14, folio no consta en la transcripción
AFIRMACIÓN A-UT02-316: número de participantes → en cada esquina de esta plaza hubo un montón de indios
    «en cada esquina de esta plaza hubo un montón de indios»
    Afirmante: «don Juan Quiñones» (certificante) [= «Don Juan Quiñones» es un nombre puesto por quien redactó la certificación P03 (H1) | «Don Juan Quiñones» es una persona real que no reside en Tinta (H2) | «Don Juan Quiñones», teniente alguacil: existencia de la persona (en disputa) | «don Juan Quiñones» de P03 y de P24 son el mismo nombre (correferencia), según reconstrucción]; certificación P03, sin fecha escrita; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Juan Cazorla
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT02, folio no consta en la transcripción
AFIRMACIÓN A-UT03-210: número de participantes → un montón de indios
    «un montón de indios asumaron a la puerta de la cárcel»
    Afirmante: «Fernando Orue» (certificante) [= Fernando Orue, cabo o soldado de milicias, vecino de Tinta, según reconstrucción]; certificación P04, sin fecha escrita; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Fernando Orue
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT03, folio no consta en la transcripción
AFIRMACIÓN A-UT12b-006: número de participantes → quatro o seis Yndios
    «vio a quatro o seis Yndios en la puerta de la carcel con garrotes»
    Afirmante: «Mariano Casorla» (declarante) [= El declarante de P19 es Martín Cazorla (hipótesis A) | El declarante de P19 es un Mariano Casorla distinto de Martín (hipótesis B) | «el Gobernador Señor Don Mariano Casorla» (P19) es una mala lectura de «el granadero … Martin Casorla», según reconstrucción]; declaración jurada P19, fecha escrita «Ynmediatamente»; ante: ante mi; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: lo vio; fuerza institucional: testimonial; UT12.b, folio 20

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Presencia nocturna de indios con garrotes ante la cárcel de Tinta la noche de la prisión de Huancachoque (hecho mínimo)» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/hecho/H-p01-alboroto cc-14-18/hecho/H-p03-alboroto cc-14-18/hecho/H-p04-alboroto cc-14-18/hecho/H-p05-alboroto cc-14-18/hecho/H-p06-alboroto cc-14-18/hecho/H-p07-alboroto cc-14-18/hecho/H-p18-alboroto cc-14-18/hecho/H-p19-alboroto cc-14-18/hecho/H-p21-alboroto
    Argumento: Probable solo como hecho mínimo: unos pocos indios, algunos ebrios y con garrotes, junto a la puerta de la cárcel aquella noche; no como «alboroto» ni «alzamiento». Los apoyos independientes y jurados son P19 («vio a quatro o seis Yndios en la puerta de la carcel con garrotes», A-UT12b-006) y P21 («el aboroto … a la puerta de la carcel y q estaban ebrios», «el primer puesto del gallo», A-UT14-004). P01, P03, P04 y P05 son certificaciones que, según Mata, Orue y el declarante de P19, redactó o inspiró el propio denunciante (A-UT17-101–104), y P06 es su escrito: no son independientes. P18 es de oídas («se lo dijo su segundo sargento Santiago Casorla»). Evidencia contraria: Mata (P27) concluye que los documentos sobre «el bullicio, y asonada» «fueron hechos por el mismo Guancachoque», y el fiscal (P29) que las quejas son «menos conforme a la verdad» (A-UT19-001); no niegan expresamente que hubiera algo, pero no lo reconocen. El relato de P20 (Cano, según Santiago Cazorla: «todos los indios alzaron a media noche») no está anotado como hecho narrado, solo como afirmación «dijo» (A-UT13-505), y no se enlaza. Discrepan en la hora y el número (ver PC14). Revisada tras la auditoría I (2026-11-13). Ampliada el 2026-11-14 (claude-fable-5-2): se añade H-p07-alboroto. La vista fiscal P07 resume el escrito P06 («antes ayer precurado matarlo con alboroto de noche, y estando aquel en la carcel») y remite a las certificaciones («este hecho parece que lo califican con las certificaciones de testigos», A-UT07-212): es el mismo suceso, pero no una fuente independiente, y su «antes ayer» choca con las fechas del escrito (F1). Se añade como premisa contraria la negación jurada del declarante de P19 de haber dicho que «se alzaron los Yndios todos con barrotes» (A-UT12b-004). No se enlazan H-p03-guardias (guardias en las puertas de los españoles: otro lugar y otras víctimas, solo anotado como hecho en P03) ni H-p20-visita (aviso de amenazas a Santiago Cazorla esa madrugada): son sucesos conexos de la misma noche, no el hecho mínimo ante la cárcel. Reconstrucción propuesta originalmente por claude-opus-5-5 el 2026-11-13.
```

## PC15

```text
PREGUNTA: ¿Qué autoridades actuaron, en qué actuación, en qué fecha, quién escribió y quién firmó cada una, y en qué orden circuló el expediente?
RESPUESTA (D): 31 de 33 piezas con participantes anotados (102 participaciones); 7 piezas sin firmante anotado.

  P00 [carátula]: no consta ningún participante con papel en la pieza.
  P01 [certificación] fecha escrita «en primero de agosto de 1806»; data «En el pueblo de Tinta»
      certificante: «Isidro Cano» [Isidro Cano, sargento de milicias, vecino español de Tinta]
      denunciante: «Guancachoque» [Manuel Huancachoque (Guancachoque), denunciante]
      destinatario: «los señores jueces»
      firmante: «Isidro Cano» [Isidro Cano, sargento de milicias, vecino español de Tinta]
  P02 [certificación] fecha escrita «agosto cinco de mil ochocientos seis años»; data «doy mi certificación en Tinta»
      certificante: «yo sargento primero» [Santiago Cazorla, sargento de milicias de Tinta]
      firmante: «Santiago Cazorla» [Santiago Cazorla, sargento de milicias de Tinta]
  P03 [certificación] fecha escrita «no consta»; data «no consta»
      certificante: «don Juan Quiñones» [«Don Juan Quiñones» es un nombre puesto por quien redactó la certificación P03 (H1)]; «don Juan Quiñones» [«don Juan Quiñones» de P03 y de P24 son el mismo nombre (correferencia)]; «don Juan Quiñones» [«Don Juan Quiñones» es una persona real que no reside en Tinta (H2)]; «don Juan Quiñones» [«Don Juan Quiñones», teniente alguacil: existencia de la persona (en disputa)]
      destinatario: «los señores jueces»
      firmante: «Juan Cazorla» [El firmante Juan Cazorla es el Juan de Dios Cazorla mencionado en P20]; «Juan Cazorla» [Juan Cazorla, firmante de la certificación P03]
  P04 [certificación] fecha escrita «no consta»; data «no consta»
      certificante: «Fernando Orue» [Fernando Orue, cabo o soldado de milicias, vecino de Tinta]
      firmante: «Fernando Orue» [Fernando Orue, cabo o soldado de milicias, vecino de Tinta]
  P05 [certificación] fecha escrita «no consta»; data «no consta»
      certificante: «Martin Cazorla» [El declarante de P19 es Martín Cazorla (hipótesis A)]; «Martin Cazorla» [«el Gobernador Señor Don Mariano Casorla» (P19) es una mala lectura de «el granadero … Martin Casorla»]; «Martin Cazorla» [Martín Cazorla, soldado granadero]
      destinatario: «los señores jueces»
      firmante: «Martin Cazorla» [El declarante de P19 es Martín Cazorla (hipótesis A)]; «Martin Cazorla» [Martín Cazorla, soldado granadero]
  P06 [petición] fecha escrita «CUSCO AGOSTO 22 DE 1806»; data «no consta»
      denunciante: «Manuel Huancachoque» [Manuel Huancachoque (Guancachoque), denunciante]
      destinatario: «SEÑOR FISCAL PROTECTOR GENERAL DE NATURALES» [Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco]
      firmante: «MANUEL HUANCACHOQQUE» [Manuel Huancachoque (Guancachoque), denunciante]
  P07 [vista fiscal] fecha escrita «Cusco y Agosto 21 de 1806»; data «no consta»
      destinatario: «Muy ilustre Señor Presidente» [Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806]
      dictaminador: «El fiscal de su Majestad» [Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco]
      firmante: «Gómez del Rio» [Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco]
  P08 [notificación] fecha escrita «En el Cusco y Agosto veinte y tres de ochocientos seis»; data «no consta»
      firmante: «Chacón» [Chacón (Agustín Chacón y Becerra; «Antonio» en P10), escribano que autoriza y notifica en el Cusco]
      notificado: «Don Luis Gomez del Rio» [Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco]
  P09 [reconocimiento y ratificación] fecha escrita «en trece días del mees de Agosto de mil ochocientos seis años»; data «En la ciudad del Cuzco»
      autoridad ante quien se actúa: «Don Manuel Galeano» [Manuel Galeano, teniente asesor del gobierno e intendencia del Cusco]
      declarante: «Manuel Guancachoque» [Manuel Huancachoque (Guancachoque), denunciante]
      fedatario: «Escribano mayor de Gobierno» [«el presente Escribano mayor de Gobierno» que da fe en P09 es el escribano Chacón]
      firmante: «Galeano» [Manuel Galeano, teniente asesor del gobierno e intendencia del Cusco]; «Don Valencia» [Manuel Valencia, abogado, protector partidario de naturales]; «Marcos Salcedo» [Marcos Salcedo, firmante de la diligencia de ratificación P09]; «Juan Clemente Jordan» [Juan Clemente Jordan, firmante de la diligencia de ratificación P09]; «Manuel Guancachoque» [Manuel Huancachoque (Guancachoque), denunciante]
      intérprete: «interpretes generales»
      protector de naturales (en la actuación): «Doctor Don Manuel Valencia» [Manuel Valencia, abogado, protector partidario de naturales]
  P10 [auto] fecha escrita «Agosto 27 de 1806»; data «no consta»
      destinatario: «Juez subdelegado del partido de Tinta» [Pedro de la Mata, subdelegado del partido de Tinta]
      firmante: «Castilla» [Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806]; «Don Antonio Chacón» [«Don Antonio Chacón» (P10) es un escribano distinto de Agustín Chacón y Becerra]; «Don Antonio Chacón» [Chacón (Agustín Chacón y Becerra; «Antonio» en P10), escribano que autoriza y notifica en el Cusco]; «Don Antonio Chacón» [«el presente Escribano mayor de Gobierno» que da fe en P09 es el escribano Chacón]
  P11 [notificación] fecha escrita «En el Cuzco en veinte y siete días del mes de Agosto de mil ocho = Cientos seis años»; data «no consta»
      fedatario: «Yo el escrivano» [Chacón (Agustín Chacón y Becerra; «Antonio» en P10), escribano que autoriza y notifica en el Cusco]
      firmante: «Chacón» [Chacón (Agustín Chacón y Becerra; «Antonio» en P10), escribano que autoriza y notifica en el Cusco]
      notificado: «Don Luis Gonsalo del Rio» [Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco]
  P12 [notificación] fecha escrita «En dicho día mes y año»; data «no consta»
      fedatario: «Yo el escrivano» [Chacón (Agustín Chacón y Becerra; «Antonio» en P10), escribano que autoriza y notifica en el Cusco]
      firmante: «Chacón» [Chacón (Agustín Chacón y Becerra; «Antonio» en P10), escribano que autoriza y notifica en el Cusco]
      notificado: «Manuel Guancachoque» [Manuel Huancachoque (Guancachoque), denunciante]
  P13 [oficio] fecha escrita «Cusco y Agosto 28 de 1806»; data «no consta»
      destinatario: «vuestra Merced» [Pedro de la Mata, subdelegado del partido de Tinta]; «subdelegado de Tinta» [Pedro de la Mata, subdelegado del partido de Tinta]
      firmante: «Ruiz de Castilla» [Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806]
  P14 [decreto] fecha escrita «Setiembre. 17 de 1806»; data «Sicuani Setiembre»
      firmante: «Pedro de la Mara» [Pedro de la Mata, subdelegado del partido de Tinta]
  P15 [desglose y agregación]: no consta ningún participante con papel en la pieza.
  P16 [auto cabeza de proceso] fecha escrita «no consta»; data «no consta»
      destinatario: «D. Andres Chuquitapa» [Andrés Chuquitapa, cacique y recaudador de tributos de Tinta]
      firmante: «Pedro de la Mara» [Pedro de la Mata, subdelegado del partido de Tinta]
      testigo de asistencia: «Mariano Figueroa» [Mariano Figueroa, testigo de asistencia del subdelegado y notificador]
  P17 [notificación] fecha escrita «no consta»; data «no consta»
      firmante: «Mariano Figueroa» [Mariano Figueroa, testigo de asistencia del subdelegado y notificador]
      notificado: «D. Andre S. Chuquitape» [Andrés Chuquitapa, cacique y recaudador de tributos de Tinta]
  P18 [declaración jurada] fecha escrita «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; data «En el pueblo de Tinta»
      declarante: «Ysidro Cano» [Isidro Cano, sargento de milicias, vecino español de Tinta]
      firmante: «YSIDRO CANO» [Isidro Cano, sargento de milicias, vecino español de Tinta]; «PEDRO DE LA MATA» [Pedro de la Mata, subdelegado del partido de Tinta]
      juez comisionado: «Pedro de la Mata» [Pedro de la Mata, subdelegado del partido de Tinta]
      testigo de asistencia: «MARIANO FIGUEROA» [Mariano Figueroa, testigo de asistencia del subdelegado y notificador]; «CELEDONIO APARICIO» [Celedonio Aparicio, testigo de asistencia en la declaración de Cano]
  P19 [declaración jurada] fecha escrita «Ynmediatamente»; data «no consta»
      declarante: «Mariano Casorla» [El declarante de P19 es un Mariano Casorla distinto de Martín (hipótesis B)]; «Mariano Casorla» [El declarante de P19 es Martín Cazorla (hipótesis A)]; «Mariano Casorla» [«el Gobernador Señor Don Mariano Casorla» (P19) es una mala lectura de «el granadero … Martin Casorla»]
      juez comisionado: «ante mi» [Pedro de la Mata, subdelegado del partido de Tinta]
  P20 [declaración jurada] fecha escrita «en veinti quatro dias del mes de setiembre de mil ochocientos seis años»; data «no consta»
      declarante: «santiago cacerola» [Santiago Cazorla, sargento de milicias de Tinta]
      juez comisionado: «ante mi» [Pedro de la Mata, subdelegado del partido de Tinta]
  P21 [declaración jurada] fecha escrita «Seguidamente»; data «no consta»
      declarante: «fernando ore» [Fernando Orue, cabo o soldado de milicias, vecino de Tinta]; «el declarante» [Fernando Orue, cabo o soldado de milicias, vecino de Tinta]
      firmante: «conmigo»
      juez comisionado: «el grl. sub delegado» [Pedro de la Mata, subdelegado del partido de Tinta]
      testigo de asistencia: «testigos de mi asistencia»
  P22 [oficio] fecha escrita «setiembre 24 de 1806»; data «no consta»
      destinatario: «parroco interino» [Agustín Valdés, cura interino de Tinta]
      firmante: «pedro de Mata» [Pedro de la Mata, subdelegado del partido de Tinta]
  P23 [informe] fecha escrita «Noviembre 26 de 1806»; data «no consta»
      destinatario: «vuestra»
      firmante: «Firma» [Agustín Valdés, cura interino de Tinta]
  P24 [decreto] fecha escrita «no consta»; data «no consta»
      firmante: «María Rubrica» [«[María Rubrica]» es la rúbrica del subdelegado Mata]; «María Rubrica» [«[María Rubrica]» es la nota del transcriptor «[Media rúbrica]» y no nombra a ninguna María]
  P25 [decreto] fecha escrita «Sicuani Noviembre 8 de 1806»; data «Sicuani Noviembre 8»
      destinatario: «Muy Ilustrísima Señor Padre» [Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806]
      firmante: «María Rubrica» [«[María Rubrica]» es la rúbrica del subdelegado Mata]; «María Rubrica» [«[María Rubrica]» es la nota del transcriptor «[Media rúbrica]» y no nombra a ninguna María]
  P26 [decreto] fecha escrita «Cuzco noviembre 18 de noviembre de 1806»; data «no consta»
      destinatario: «señor»
  P27 [informe] fecha escrita «Siquani Noviembre 8 de 1806»; data «Siquani Noviembre 8»
      destinatario: «Señor Capitan General» [Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806]; «Don Francisco Muñoz y Señor Clemente» [Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806]
      informante: «Pedro de la Mata» [Pedro de la Mata, subdelegado del partido de Tinta]; «Pedro de la Mata» [«[María Rubrica]» es la rúbrica del subdelegado Mata]
  P28 [auto] fecha escrita «Cusco y noviembre 26 de 1806»; data «no consta»
      destinatario: «subdelegado del partido de tinta» [Pedro de la Mata, subdelegado del partido de Tinta]
      firmante: «Muñoz» [Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806]
  P29 [vista fiscal] fecha escrita «Noviembre 20 de 1806»; data «no consta»
      destinatario: «vuestro»
      dictaminador: «El fiscal» [Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco]
      firmante: «Gonzalo del Rio» [Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco]
  P30 [notificación] fecha escrita «en veinte y seis de noviembre de mil ochocientos seis»; data «no consta»
      fedatario: «Yo el escribano» [Chacón (Agustín Chacón y Becerra; «Antonio» en P10), escribano que autoriza y notifica en el Cusco]
      firmante: «Chacon» [Chacón (Agustín Chacón y Becerra; «Antonio» en P10), escribano que autoriza y notifica en el Cusco]
      notificado: «don Lucio Gonzalo del Rio y Vial» [Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco]
  P31 [notificación] fecha escrita «veinte y tres de Diciembre de mil ochocientos 10 años»; data «no consta»
      fedatario: «Yo el escribano» [Chacón (Agustín Chacón y Becerra; «Antonio» en P10), escribano que autoriza y notifica en el Cusco]
      firmante: «Chacon» [Chacón (Agustín Chacón y Becerra; «Antonio» en P10), escribano que autoriza y notifica en el Cusco]
      notificado: «su persona»
  P32 [certificación] fecha escrita «no consta»; data «no consta»
      certificante: «Matias Ugarte» [Matías Ugarte, notario público de la provincia de Urubamba (pieza ajena, P32)]

Circulación según la data escrita de las piezas (solo donde consta):
  P01: En el pueblo de Tinta → P02: doy mi certificación en Tinta → P09: En la ciudad del Cuzco → P14: Sicuani Setiembre → P18: En el pueblo de Tinta → P25: Sicuani Noviembre 8 → P27: Siquani Noviembre 8

Piezas sin firmante anotado: P00, P15, P19, P20, P26, P27, P32
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
AFIRMACIÓN A-UT07-201: tiene una condición → indio
    «Manuel Guancachoque indio del Pueblo de Tinta»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-202: cantidad (de tributarios, dinero, etc.) → cincuenta y un tributarios
    «aver denunciado cincuenta y un tributarios en la revisita de aquel partido contra el Recaudador»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-203: participa en un hecho → H-p07-denuncia (sujeto elíptico resuelto por el anotador)
    «se queja de que en odio de aver denunciado cincuenta y un tributarios en la revisita de aquel partido»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-204: lugar del hecho → aquel partido
    «en la revisita de aquel partido contra»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-205: participa en un hecho → H-p07-maltrato
    «este y sus parciales amén de aver logrado su prision, lo han maltratado de obra, e injuriado de palabra»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-206: participa en un hecho → H-p07-maltrato (sujeto elíptico resuelto por el anotador)
    «este y sus parciales amén de aver logrado su prision, lo han maltratado de obra, e injuriado de palabra»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-207: participa en un hecho → H-p07-prision (sujeto elíptico resuelto por el anotador)
    «este y sus parciales amén de aver logrado su prision»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-208: participa en un hecho → H-p07-prision (sujeto elíptico resuelto por el anotador)
    «amén de aver logrado su prision»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-209: fecha u hora del hecho → antes ayer
    «antes ayer precurado matarlo con alboroto de noche»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-210: fecha u hora del hecho → de noche
    «precurado matarlo con alboroto de noche»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-211: lugar del hecho → la carcel
    «estando aquel en la carcel»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-212: veracidad de un escrito o queja → parece que lo califican con las certificaciones de testigos
    «este hecho parece que lo califican con las certificaciones de testigos que acompañan a su escrito»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-213: tiene una condición → tributario (sujeto elíptico resuelto por el anotador)
    «ampliando su queja al de averse matriculado en clase de tributario»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-214: solicita → se le exima en premio del servicio que ha hecho (sujeto elíptico resuelto por el anotador)
    «solicita se le exima en premio del servicio que ha hecho»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-215: solicita → reconociendo el suplicante su escrito en la forma acostumbrada
    «siendo servido mandar que reconociendo el suplicante su escrito en la forma acostumbrada»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-216: solicita → se dirija la respectiva orden del subdelegado del partido de Tinta
    «se dirija la respectiva orden del subdelegado del partido de Tinta»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-217: solicita → el referido recaudador incomode ni infiera perjuicio al suplicante
    «por medio de otro alguno el referido recaudador incomode ni infiera perjuicio al suplicante en odio de la denuncia»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-218: ejerce o ejerció un cargo → subdelegado
    «la respectiva orden del subdelegado del partido de Tinta»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-219: ejerce o ejerció un cargo → recaudador de tributos
    «el referido recaudador incomode»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-220: participa en un hecho → H-p07-alboroto
    «precurado matarlo con alboroto de noche, y estando aquel en la carcel»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT08-201: solicita → proceda a reesivir de oficio con la prudencia y reserva conducente la justificación correspondiente sobre el alboroto o exceso que se enuncia, y los principales que lo huviesen fomentado
    «proceda a reesivir de oficio con la prudencia y reserva conducente la justificación correspondiente sobre el alboroto o exceso que se enuncia, y los principales que lo huviesen fomentado»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT08, folio no consta en la transcripción
AFIRMACIÓN A-UT08-202: solicita → que informen el mismo Subdelegado, con el Apoderado Fiscal de la revisita, verificandolo por separado
    «que informen el mismo Subdelegado, con el Apoderado Fiscal de la revisita, verificandolo por separado»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT08, folio no consta en la transcripción
AFIRMACIÓN A-UT08-203: ejerce o ejerció un cargo → apoderado fiscal de la revisita
    «con el Apoderado Fiscal de la revisita»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT08, folio no consta en la transcripción
AFIRMACIÓN A-UT08-204: ejerce o ejerció un cargo → subdelegado
    «que informen el mismo Subdelegado»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT08, folio no consta en la transcripción
AFIRMACIÓN A-UT08-205: solicita → lo que en premio de ella solicita el suplicante
    «Y en quanto a la denuncia, y por lo que en premio de ella solicita el suplicante»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT08, folio no consta en la transcripción
AFIRMACIÓN A-UT09-501: se conforma con (adopta) un dictamen → P07
    «en conformidad a lo expuesta y pedido por el Señor Fiscal»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-502: ejerce o ejerció un cargo → recaudador de tributos
    «notificando primero al Recaudado Don Andrés Chuquitapa»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-503: ejerce o ejerció un cargo → subdelegado
    «remitame al Juez subdelegado del partido de Tinta»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-504: ordena o manda → notificando primero al Recaudado Don Andrés Chuquitapa
    «para que notificando primero al Recaudado Don Andrés Chuquitapa como pide dicho Señor»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-505: ordena o manda → ceparandolo en caso necesario que altas leguas en contrario fuera del pueblo
    «ceparandolo en caso necesario que altas leguas en contrario fuera del pueblo»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-506: ordena o manda → proceda con la cautela y prudencia que exige el asunto
    «proceda con la cautela y prudencia que exige el asunto»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-507: ordena o manda → a recivido la sumaria informasion correspondiente
    «a recivido la sumaria informasion correspondiente bajo las formalidades de escrito»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-508: ordena o manda → que los cuyos otros se acompañan en las fojas antecedentes de ratifiquen y declaren
    «haciendo al mismo tiempo que los cuyos otros se acompañan en las fojas antecedentes de ratifiquen y declaren»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-509: ordena o manda → cuydando de que a dicho querello no se le incomode ni trate mal
    «cuydando de que a dicho querello no se le incomode ni trate mal»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-510: ordena o manda → lo remita con su informe
    «lo remita con su informe»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-511: ordena o manda → oyendo sobre ellos al Apoderado Fiscal ynforme por ceparado
    «por lo que toca a la denuncia de tributarios y solicitud del denunciante, oyendo sobre ellos al Apoderado Fiscal ynforme por ceparado»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT10-501: la pieza está en tal folio (autorreferencia del expediente) → en folio 10
    «con el Expediente en folio 10 que la acompaña»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-502: la pieza está en tal folio (autorreferencia del expediente) → al fin de el en folio 2
    «la denuncia que se halla al fin de el en folio 2»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-503: fecha u hora del hecho → en 27 de Agosto proximo pasado
    «hecha por el.Indio Manuel Guancachoque en 27 de Agosto proximo pasado»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-504: tiene una condición → indio
    «hecha por el.Indio Manuel Guancachoque»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-505: cantidad (de tributarios, dinero, etc.) → cinquenta y un Indios
    «correspondiente de cinquenta y un Indios que dice tener ocultos, y fuera de Matricula en el pueblo de Tinta su recaudador de tributos Dn Andres Chuquitapa»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-506: ejerce o ejerció un cargo → recaudador de tributos
    «su recaudador de tributos Dn Andres Chuquitapa»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-507: fecha u hora del hecho → en once de Febrero del año pasado de 1809
    «es la misma que hizo en once de Febrero del año pasado de 1809, el mismo denunciante»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-508: fecha u hora del hecho → con fecha. 29 de mayo de este presente año
    «se me remitio ami el subdelegado, y al apoderado Fiscal de la presente Revicita por el mismo Sr. Presidente con fecha. 29 de mayo de este presente año»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-509: ejerce o ejerció un cargo → subdelegado
    «se me remitio ami el subdelegado»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-510: ejerce o ejerció un cargo → apoderado fiscal de la revisita
    «al apoderado Fiscal de la presente Revicita»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-511: ejerce o ejerció un cargo → presidente de la Real Audiencia
    «por el mismo Sr. Presidente con fecha. 29 de mayo»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-512: participa en un hecho → H-p14-defraudacion
    «el examen y Justificación de la defraudación que se hacia asu Magestad. cometida por el citado re caudador»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-513: participa en un hecho → H-p14-defraudacion
    «la defraudación que se hacia asu Magestad»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-514: ordena o manda → Desglocese de este Expediente, y agreguese a el de la primera denuncia
    «Desglocese de este Expediente, y agreguese a el de la primera denuncia»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-515: ordena o manda → Procedase por mi à tomar la información Correspondiente
    «Procedase por mi à tomar la información Correspondiente sobre los hechos que ha expuesto el citado Guancachoque»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-516: ordena o manda → hagase el correspondiente. informe, y dese la Cuenta Ordenada
    «con lo que resulte hagase el correspondiente. informe, y dese la Cuenta Ordenada por . Decreto de 27 de Agosto»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-517: se conforma con (adopta) un dictamen → P07
    «con arreglo à lo pedido por el Minis terio Fiscal»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-518: ejerce o ejerció un cargo → recaudador de tributos
    «notifiquese al recaudaor de tributos D. Andres Chuquitapa»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; auto cabeza de proceso P16, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-519: ordena o manda → que mi si mi por medio de otro alguno incomode ni infiera perjuicio, Guancachoque, en odio de su denuncia
    «notifiquese al recaudaor de tributos D. Andres Chuquitapa; que mi si mi por medio de otro alguno incomode ni infiera perjuicio, Guancachoque, en odio de su denuncia»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; auto cabeza de proceso P16, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-520: se conforma con (adopta) un dictamen → P10
    «en cumplimiento del . Auto que antecede»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; auto cabeza de proceso P16, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT11-501: tiene una condición → tributario
    «todos los Indios que manifiesta la denuncia ultima estan matriculados en la nueba revisita»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; auto cabeza de proceso P16, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-502: ordena o manda → se retire, de este Pueblo à distan. cia de quatro leguas
    «haga de Saber a Chuquitapa se retire, de este Pueblo à distan. cia de quatro leguas»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; auto cabeza de proceso P16, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-503: ordena o manda → haga de Saber a Chuquitapa se retire
    «haga de Saber a Chuquitapa se retire, de este Pueblo à distan. cia de quatro leguas (interin de»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; auto cabeza de proceso P16, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT11-504: firmó la pieza → Pedro de la Mara
    «Asi lo provey y mande y firme con testigos a falta de Escribano»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; auto cabeza de proceso P16, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT11, folio no consta en la transcripción
AFIRMACIÓN A-UT17-001: firmó la pieza → Juan Cazorla
    «Juan Cazorla de quien aparece firmada la Certificación a folios 2»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la nota del transcriptor «[Media rúbrica]» y no nombra a ninguna María | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P24, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT17-002 [NIEGA]: existe tal persona en el lugar → en el pueblo de Tinta
    «que no hay tal hombre en el pueblo de Tinta»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la nota del transcriptor «[Media rúbrica]» y no nombra a ninguna María | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P24, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT17-004: la pieza está en tal folio (autorreferencia del expediente) → a folios 2
    «la Certificación a folios 2 extendida a nombre del teniente Alguacil»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la nota del transcriptor «[Media rúbrica]» y no nombra a ninguna María | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P24, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT17-801 [NIEGA]: estaba presente o ausente → ausente de este pueblo
    «Respecto a hallarse ausente de este pueblo Juan Cazorla»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la nota del transcriptor «[Media rúbrica]» y no nombra a ninguna María | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P24, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT17-802: ejerce o ejerció un cargo → teniente alguacil
    «extendida a nombre del teniente Alguacil Don Juan Quiñones»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la nota del transcriptor «[Media rúbrica]» y no nombra a ninguna María | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P24, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT17-803: ordena o manda → esperece su llegada para recibirle la declaración Respectiva sobre el Asunto
    «esperece su llegada para recibirle la declaración Respectiva sobre el Asunto»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la nota del transcriptor «[Media rúbrica]» y no nombra a ninguna María | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P24, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT17-804 [NIEGA]: estaba presente o ausente → comparecido ... al pueblo de Tinta
    «No habiendo comparecido mi regresado hasta esa fecha al pueblo de Tinta Juan Cazorla»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la nota del transcriptor «[Media rúbrica]» y no nombra a ninguna María | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P25, fecha escrita «Sicuani Noviembre 8 de 1806»; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT17-805: firmó la pieza → Juan Cazorla
    «Juan Cazorla que suscribió el documento de 2 fojas de este expediente»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la nota del transcriptor «[Media rúbrica]» y no nombra a ninguna María | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P25, fecha escrita «Sicuani Noviembre 8 de 1806»; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT17-806: ordena o manda → diríjase con lo actuado y el correspondiente Informe al Muy Ilustrísima Señor Padre para su determinación
    «diríjase con lo actuado y el correspondiente Informe al Muy Ilustrísima Señor Padre para su determinación»
    Afirmante: «María Rubrica» (autoridad que resuelve) [= «[María Rubrica]» es la nota del transcriptor «[Media rúbrica]» y no nombra a ninguna María | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; decreto P25, fecha escrita «Sicuani Noviembre 8 de 1806»; ante: no consta; redacta: no consta; firma la pieza: María Rubrica
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT19-003: ordena o manda → contener los excesos y enemistad del yndio Guancachoque
    «a fin de contener los excesos y enemistad del yndio Guancachoque»
    Afirmante: «Muñoz» (autoridad que resuelve) [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción]; auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-004: se conforma con (adopta) un dictamen → P29
    «Visto de conformidad con lo supuesto por el señor Fiscal»
    Afirmante: «Muñoz» (autoridad que resuelve) [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción]; auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-801: ordena o manda → tome las providencias que estaba oportunas
    «librese la correspondiente orden al subdelegado del partido de tinta para que tome las providencias que estaba oportunas»
    Afirmante: «Muñoz» (autoridad que resuelve) [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción]; auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-802: ordena o manda → hasiendole asi mismo extender la subordinación y respeto que debe observar en lo sucesivo con los superiores
    «hasiendole asi mismo extender la subordinación y respeto que debe observar en lo sucesivo con los superiores»
    Afirmante: «Muñoz» (autoridad que resuelve) [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción]; auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-803: ordena o manda → bajo apersivimiento ... Tomará el gobierno las más serias providencias
    «bajo apersivimiento de que en el caso de residencia To- Tomará el gobierno las más serias providencias»
    Afirmante: «Muñoz» (autoridad que resuelve) [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción]; auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-804: tiene una condición → indio
    «los excesos y enemistad del yndio Guancachoque»
    Afirmante: «Muñoz» (autoridad que resuelve) [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción]; auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-805: calificación de conducta o carácter → excesos y enemistad
    «a fin de contener los excesos y enemistad del yndio Guancachoque paso con el recaudador»
    Afirmante: «Muñoz» (autoridad que resuelve) [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción]; auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-806: ejerce o ejerció un cargo → recaudador de tributos
    «con el recaudador de tributos Don Andres Chuquitapa»
    Afirmante: «Muñoz» (autoridad que resuelve) [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción]; auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-807: ejerce o ejerció un cargo → subdelegado
    «al subdelegado del partido de tinta para que tome»
    Afirmante: «Muñoz» (autoridad que resuelve) [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción]; auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-001: veracidad de un escrito o queja → menos conforme a la verdad
    «resultando de este ser menos conforme a la verdad las quejas dadas por Manuel Guancoichoque»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-002: calificación de conducta o carácter → mala conducta y genio discolo y arreva
    «por la mala conducta y genio discolo y arreva que se nota»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-808: tiene una condición → indio
    «Manuel Guancoichoque Yndio del Pueblo de Tinta»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-809: ejerce o ejerció un cargo → recaudador de tributos
    «contra el recaudador de tributos Andres chuquitapa»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-810: ejerce o ejerció un cargo → subdelegado
    «antecedente oficio del subdelegado del partido de Tinta»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-811: motivo o causa del hecho → en odio de los denuncios de Yndios tributarios que hizo contra dicho recaudador
    «en odio de los denuncios de Yndios tributarios que hizo contra dicho recaudador»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-812: veracidad de un escrito o queja → la malicia con que aparece aver formado dicha queja
    «por la malicia con que aparece aver formado dicha queja y los documentos que presento en su calificación»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-813: motivo o causa del hecho → los enemistad que se advierte profesarle al mencionado recaudador
    «por los enemistad que se advierte profesarle al mencionado recaudador»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-814: solicita → tome las providencias que según su prudencia y conocimientos en el asunto estime mas oportuno y conducentes a efecto de corregir y contener del yndio Guancachoque
    «parece consiguiente y mui conveniente que el subdelegado territorial tome las providencias que según su prudencia y conocimientos en el asunto estime mas oportuno y conducentes a efecto de corregir y contener del yndio Guancachoque»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-815: solicita → sujetándolo a la debida subordinación y correspondientes obligaciones
    «sujetándolo a la debida subordinación y correspondientes obligaciones»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-816: solicita → se libre la conducente orden al mencionado .Subdelegado a este efecto
    «podrá vuestro si es servido moidar se libre la conducente orden al mencionado .Subdelegado a este efecto»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-817: solicita → mui a la mira de la conducta y operaciones de dicho Guancachoque
    «mui a la mira de la conducta y operaciones de dicho Guancachoque»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-821: redactó la pieza → Manuel Guancoichoque
    «por la malicia con que aparece aver formado dicha queja y los documentos que presento en su calificación»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-822: redactó la pieza → Manuel Guancoichoque
    «por la malicia con que aparece aver formado dicha queja y los documentos que presento en su calificación»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-823: redactó la pieza → Manuel Guancoichoque
    «por la malicia con que aparece aver formado dicha queja y los documentos que presento en su calificación»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT19-824: redactó la pieza → Manuel Guancoichoque
    «por la malicia con que aparece aver formado dicha queja y los documentos que presento en su calificación»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT20-801: firmó la pieza → Gonzalo del Rio
    «Noviembre 20 de 1806.[Firma Gonzalo del Rio]»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT20, folio 34
```

## PC17

```text
PREGUNTA: ¿Qué condición fiscal y social se atribuye a Huancachoque y quién la atribuye?
RESPUESTA (A): 18 atribuciones, cada una de quien la hace (ninguna es un hecho).

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT05-003: tiene una condición → originario
    «Manuel Huancachoque Indio originario y vecino del pueblo de Tinta»
    Afirmante: «Manuel Huancachoque» (denunciante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; petición P06, fecha escrita «CUSCO AGOSTO 22 DE 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: MANUEL HUANCACHOQQUE
    Fundamento invocado: no lo indica; fuerza institucional: alegación de parte; UT05, folio no consta en la transcripción
AFIRMACIÓN A-UT05-201: tiene una condición → indio
    «Manuel Huancachoque Indio originario y vecino del pueblo de Tinta»
    Afirmante: «Manuel Huancachoque» (denunciante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; petición P06, fecha escrita «CUSCO AGOSTO 22 DE 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: MANUEL HUANCACHOQQUE
    Fundamento invocado: no lo indica; fuerza institucional: alegación de parte; UT05, folio no consta en la transcripción
AFIRMACIÓN A-UT05-202: tiene una condición → vecino
    «Manuel Huancachoque Indio originario y vecino del pueblo de Tinta»
    Afirmante: «Manuel Huancachoque» (denunciante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; petición P06, fecha escrita «CUSCO AGOSTO 22 DE 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: MANUEL HUANCACHOQQUE
    Fundamento invocado: no lo indica; fuerza institucional: alegación de parte; UT05, folio no consta en la transcripción
AFIRMACIÓN A-UT06-004: tiene una condición → miliciano
    «por haber estado empleado en las milicias de aquella provincia, hasta aquí no había tributado»
    Afirmante: «Manuel Huancachoque» (denunciante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; petición P06, fecha escrita «CUSCO AGOSTO 22 DE 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: MANUEL HUANCACHOQQUE
    Fundamento invocado: no lo indica; fuerza institucional: alegación de parte; UT06, folio no consta en la transcripción
AFIRMACIÓN A-UT06-005: tiene una condición → tributario
    «conseguido también el que se me matricule»
    Afirmante: «Manuel Huancachoque» (denunciante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; petición P06, fecha escrita «CUSCO AGOSTO 22 DE 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: MANUEL HUANCACHOQQUE
    Fundamento invocado: no lo indica; fuerza institucional: alegación de parte; UT06, folio no consta en la transcripción
AFIRMACIÓN A-UT07-201: tiene una condición → indio
    «Manuel Guancachoque indio del Pueblo de Tinta»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-213: tiene una condición → tributario (sujeto elíptico resuelto por el anotador)
    «ampliando su queja al de averse matriculado en clase de tributario»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: resulta de lo actuado; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT08-211: tiene una condición → indio
    «Manuel Guancachoque yndio originario del Pueblo de Tinta»
    Afirmante: «Escribano mayor de Gobierno» (fedatario) [= «el presente Escribano mayor de Gobierno» que da fe en P09 es el escribano Chacón, según reconstrucción]; reconocimiento y ratificación P09, fecha escrita «en trece días del mees de Agosto de mil ochocientos seis años»; ante: Don Manuel Galeano; redacta: no consta; firma la pieza: Don Valencia / Galeano / Juan Clemente Jordan / Manuel Guancachoque / Marcos Salcedo
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT08, folio no consta en la transcripción
AFIRMACIÓN A-UT08-212: tiene una condición → originario
    «Manuel Guancachoque yndio originario del Pueblo de Tinta»
    Afirmante: «Escribano mayor de Gobierno» (fedatario) [= «el presente Escribano mayor de Gobierno» que da fe en P09 es el escribano Chacón, según reconstrucción]; reconocimiento y ratificación P09, fecha escrita «en trece días del mees de Agosto de mil ochocientos seis años»; ante: Don Manuel Galeano; redacta: no consta; firma la pieza: Don Valencia / Galeano / Juan Clemente Jordan / Manuel Guancachoque / Marcos Salcedo
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT08, folio no consta en la transcripción
AFIRMACIÓN A-UT09-519: tiene una condición → indio
    «Manuel Guancachoque yndio del Pueblo de Tinta»
    Afirmante: «Ruiz de Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; oficio P13, fecha escrita «Cusco y Agosto 28 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Ruiz de Castilla
    Fundamento invocado: no lo indica; fuerza institucional: informativa; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT10-504: tiene una condición → indio
    «hecha por el.Indio Manuel Guancachoque»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT15-814: tiene una condición → oriundo
    «en este pueblo Manuel Guancachoque Oriundo de el»
    Afirmante: «pedro de Mata» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; oficio P22, fecha escrita «setiembre 24 de 1806»; ante: no consta; redacta: no consta; firma la pieza: pedro de Mata
    Fundamento invocado: no lo indica; fuerza institucional: informativa; UT15, folio no consta en la transcripción
AFIRMACIÓN A-UT16a-803: tiene una condición → hijo espurio
    «Es notorio que Manuel Guancachoque es hijo Espurio»
    Afirmante: «parroco interino» (informante) [= Agustín Valdés, cura interino de Tinta, según reconstrucción]; informe P23, fecha escrita «Noviembre 26 de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Firma
    Fundamento invocado: notoriedad; fuerza institucional: informativa; UT16.a, folio no consta en la transcripción
AFIRMACIÓN A-UT19-804: tiene una condición → indio
    «los excesos y enemistad del yndio Guancachoque»
    Afirmante: «Muñoz» (autoridad que resuelve) [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción]; auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-808: tiene una condición → indio
    «Manuel Guancoichoque Yndio del Pueblo de Tinta»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT19, folio 33
AFIRMACIÓN A-UT02-002: ejerce o ejerció un cargo → soldado
    «Manuel Guamanchoque ha estado soldado en mi compañía más de cinco años»
    Afirmante: «yo sargento primero» (certificante) [= Santiago Cazorla, sargento de milicias de Tinta, según reconstrucción]; certificación P02, fecha escrita «agosto cinco de mil ochocientos seis años»; ante: no consta; redacta: no consta; firma la pieza: Santiago Cazorla
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT02, folio no consta en la transcripción
AFIRMACIÓN A-UT16a-001: es hijo/a de → Antolin Ortiz
    «Es notorio que Manuel Guancachoque es hijo Espurio de Antolin Ortiz»
    Afirmante: «parroco interino» (informante) [= Agustín Valdés, cura interino de Tinta, según reconstrucción]; informe P23, fecha escrita «Noviembre 26 de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Firma
    Fundamento invocado: notoriedad; fuerza institucional: informativa; UT16.a, folio no consta en la transcripción
AFIRMACIÓN A-UT16a-004: es hijo/a de → Agustina Falcon
    «su Madre Agustina Falcon India Ordinaria y pleveya»
    Afirmante: «parroco interino» (informante) [= Agustín Valdés, cura interino de Tinta, según reconstrucción]; informe P23, fecha escrita «Noviembre 26 de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Firma
    Fundamento invocado: notoriedad; fuerza institucional: informativa; UT16.a, folio no consta en la transcripción

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Manuel Huancachoque (Guancachoque), denunciante» — creencia: probable; autor: claude-fable-5-2; fecha: 2026-11-14
    Deriva de: cc-14-18/mencion/M-UT00-201 cc-14-18/mencion/M-UT01-002 cc-14-18/mencion/M-UT01-207 cc-14-18/mencion/M-UT02-003 cc-14-18/mencion/M-UT02-206 cc-14-18/mencion/M-UT02-215 cc-14-18/mencion/M-UT03-205 cc-14-18/mencion/M-UT03-209 cc-14-18/mencion/M-UT04-201 cc-14-18/mencion/M-UT04-209 cc-14-18/mencion/M-UT05-001 cc-14-18/mencion/M-UT06-002 cc-14-18/mencion/M-UT07-204 cc-14-18/mencion/M-UT07-214 cc-14-18/mencion/M-UT07-215 cc-14-18/mencion/M-UT07-216 cc-14-18/mencion/M-UT08-203 cc-14-18/mencion/M-UT08-216 cc-14-18/mencion/M-UT08-231 cc-14-18/mencion/M-UT09-506 cc-14-18/mencion/M-UT09-508 cc-14-18/mencion/M-UT09-511 cc-14-18/mencion/M-UT09-523 cc-14-18/mencion/M-UT09-528 cc-14-18/mencion/M-UT10-505 cc-14-18/mencion/M-UT10-510 cc-14-18/mencion/M-UT10-521 cc-14-18/mencion/M-UT10-522 cc-14-18/mencion/M-UT10-527 cc-14-18/mencion/M-UT10-530 cc-14-18/mencion/M-UT10-533 cc-14-18/mencion/M-UT11-516 cc-14-18/mencion/M-UT11-520 cc-14-18/mencion/M-UT12.a-502 cc-14-18/mencion/M-UT12.b-501 cc-14-18/mencion/M-UT12.b-508 cc-14-18/mencion/M-UT12.b-509 cc-14-18/mencion/M-UT13-504 cc-14-18/mencion/M-UT13-508 cc-14-18/mencion/M-UT13-510 cc-14-18/mencion/M-UT14-003 cc-14-18/mencion/M-UT14-503 cc-14-18/mencion/M-UT14-505 cc-14-18/mencion/M-UT14-512 cc-14-18/mencion/M-UT15-803 cc-14-18/mencion/M-UT15-811 cc-14-18/mencion/M-UT16a-001 cc-14-18/mencion/M-UT16a-801 cc-14-18/mencion/M-UT16a-804 cc-14-18/mencion/M-UT16b-811 cc-14-18/mencion/M-UT16b-813 cc-14-18/mencion/M-UT16b-814 cc-14-18/mencion/M-UT17-004 cc-14-18/mencion/M-UT17-005 cc-14-18/mencion/M-UT17-828 cc-14-18/mencion/M-UT18-804 cc-14-18/mencion/M-UT18-814 cc-14-18/mencion/M-UT18-817 cc-14-18/mencion/M-UT19-001 cc-14-18/mencion/M-UT19-804 cc-14-18/mencion/M-UT19-820 cc-14-18/mencion/M-UT19-821
    Argumento: Menciones del denunciante en la carátula, las certificaciones, su escrito, su firma ante el teniente asesor, los autos y notificaciones, la declaración de Orue («guasscachoque», «guancachay»), los informes y la vista fiscal. El cura lo llama «Ortis o Guancachoque» (P23, UT16.b) tras presentarlo como «hijo Espurio de Antolin Ortiz» (UT16.a): lo designa con el apellido del padre que le atribuye (ver R-huancachoque-alias-ortiz). No se añaden «Maldonado Ortiz» ni «las Guamcachoque» de la frase «la aminocidad y altenencia de Maldonado Ortiz a las Guamcachoque»: la construcción es ambigua (puede nombrar a otra persona o a la familia) y «Maldonado» no se explica en el texto. «Manuel Guamanchoque» (P02) se incluye por el nombre de pila y porque la certificación de su servicio militar coincide con lo que alega en su escrito («por haber estado empleado en las milicias de aquella provincia, hasta aquí no había tributado», UT06); es la única fusión no segura y la que mantiene la reconstrucción en probable. Revisada tras la auditoría I (2026-11-13). Ampliada el 2026-11-14 (claude-fable-5-2): se añaden 34 menciones. Con nombre (grafías Huancachoque, Guancachoque, «Guancacho que», guarcachoque, gancahoque) en las certificaciones P03–P05, las declaraciones P18–P21, el informe del cura, el de Mata, el auto P28 y la vista P29; todas en la misma causa y con los mismos hechos (prisión, denuncia). Designaciones por papel procesal con antecedente expreso en la misma pieza: «dicho denunciante» (P01, tras «al denunciante mayor Guancachoque»; P04, tras «contra Manuel Huancachoque»), «denunciante» (P05, tras «Manuel Huancachoque, denunciante»), «el suplicante» ×3 (P07, tras «el antecedente escrito que le ha presentado Manuel Guancachoque»), «el querello», «dicho querello» y «el denunciante» (P10, auto sobre «su escrito»), «el mismo denunciante» (P14, tras «el Indio Manuel Guancachoque»). Dos anáforas sin nombre: «aquel» de P07 (M-UT07-216: «este y sus parciales … precurado matarlo … estando aquel en la carcel», donde «este» es el recaudador y «aquel» el preso) y «al indio» de P27 (M-UT18-804: «acometieron contra el, de suerte, que si yo no salgo al indio lo hubieran en tropeado … lo mande llevar a la cárcel»). No se añaden «desvalido» (P05, sintaxis ambigua), «las Guamcachoque» ni «Maldonado Ortiz» (P23). Reconstrucción propuesta originalmente por claude-opus-5-5 el 2026-11-13.
```

## PC18

```text
PREGUNTA: ¿Qué cargos ejercía Andrés Chuquitapa, con qué vigencia y según quién?
RESPUESTA (R): 17 afirmaciones de cargo (capa 3) y 3 ejercicios de cargo reconstruidos (capa 4). Los cargos en la rebelión de 1780 están en PC09.

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT02-304: ejerce o ejerció un cargo → cacique
    «los indios del cacique don Andrés Chukitapa»
    Afirmante: «don Juan Quiñones» (certificante) [= «Don Juan Quiñones» es un nombre puesto por quien redactó la certificación P03 (H1) | «Don Juan Quiñones» es una persona real que no reside en Tinta (H2) | «Don Juan Quiñones», teniente alguacil: existencia de la persona (en disputa) | «don Juan Quiñones» de P03 y de P24 son el mismo nombre (correferencia), según reconstrucción]; certificación P03, sin fecha escrita; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Juan Cazorla
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT02, folio no consta en la transcripción
AFIRMACIÓN A-UT05-001: ejerce o ejerció un cargo → recaudador de tributos
    «tenia ocultos el recaudaderor Don Andres Choquitapa»
    Afirmante: «Manuel Huancachoque» (denunciante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; petición P06, fecha escrita «CUSCO AGOSTO 22 DE 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: MANUEL HUANCACHOQQUE
    Fundamento invocado: no lo indica; fuerza institucional: alegación de parte; UT05, folio no consta en la transcripción
AFIRMACIÓN A-UT05-212: ejerce o ejerció un cargo → recaudador de tributos
    «a presencia del recaudador y juez subdelegado»
    Afirmante: «Manuel Huancachoque» (denunciante) [= Manuel Huancachoque (Guancachoque), denunciante, según reconstrucción]; petición P06, fecha escrita «CUSCO AGOSTO 22 DE 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: MANUEL HUANCACHOQQUE
    Fundamento invocado: no lo indica; fuerza institucional: alegación de parte; UT05, folio no consta en la transcripción
AFIRMACIÓN A-UT07-001: ejerce o ejerció un cargo → recaudador de tributos
    «contra el Recaudador de Tributos Son Andres Chuquitapa»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT07-219: ejerce o ejerció un cargo → recaudador de tributos
    «el referido recaudador incomode»
    Afirmante: «Gómez del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P07, fecha escrita «Cusco y Agosto 21 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gómez del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT07, folio no consta en la transcripción
AFIRMACIÓN A-UT09-502: ejerce o ejerció un cargo → recaudador de tributos
    «notificando primero al Recaudado Don Andrés Chuquitapa»
    Afirmante: «Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; auto P10, fecha escrita «Agosto 27 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Castilla / Don Antonio Chacón
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT09-520: ejerce o ejerció un cargo → recaudador de tributos
    «Don Andrés Choquetapa Recaudador de Reales Tributos de dicho Pueblo»
    Afirmante: «Ruiz de Castilla» (autoridad que resuelve) [= Ruiz de Castilla, presidente que firma el auto y el oficio de agosto de 1806, según reconstrucción]; oficio P13, fecha escrita «Cusco y Agosto 28 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Ruiz de Castilla
    Fundamento invocado: no lo indica; fuerza institucional: informativa; UT09, folio no consta en la transcripción
AFIRMACIÓN A-UT10-506: ejerce o ejerció un cargo → recaudador de tributos
    «su recaudador de tributos Dn Andres Chuquitapa»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; decreto P14, fecha escrita «Setiembre. 17 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT10-518: ejerce o ejerció un cargo → recaudador de tributos
    «notifiquese al recaudaor de tributos D. Andres Chuquitapa»
    Afirmante: «Pedro de la Mara» (autoridad que resuelve) [= Pedro de la Mata, subdelegado del partido de Tinta, según reconstrucción]; auto cabeza de proceso P16, sin fecha escrita; ante: no consta; redacta: no consta; firma la pieza: Pedro de la Mara
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT10, folio no consta en la transcripción
AFIRMACIÓN A-UT12b-505: ejerce o ejerció un cargo → cacique
    «denunciado el robo del cacique , en favor de la Real hacienda»
    Afirmante: «Mariano Casorla» (declarante) [= El declarante de P19 es Martín Cazorla (hipótesis A) | El declarante de P19 es un Mariano Casorla distinto de Martín (hipótesis B) | «el Gobernador Señor Don Mariano Casorla» (P19) es una mala lectura de «el granadero … Martin Casorla», según reconstrucción]; declaración jurada P19, fecha escrita «Ynmediatamente»; ante: ante mi; redacta: no consta; firma la pieza: no consta; según lo que le dijo «Guancachoque» (discurso referido)
    Fundamento invocado: de oídas; fuerza institucional: testimonial; UT12.b, folio 20
AFIRMACIÓN A-UT16b-001: ejerce o ejerció un cargo → cacique
    «su casique y alcalde mayor Don Andres Chuquitapa»
    Afirmante: «parroco interino» (informante) [= Agustín Valdés, cura interino de Tinta, según reconstrucción]; informe P23, fecha escrita «Noviembre 26 de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Firma
    Fundamento invocado: no lo indica; fuerza institucional: informativa; UT16.b, folio 28
AFIRMACIÓN A-UT16b-002: ejerce o ejerció un cargo → alcalde mayor (de indios)
    «su casique y alcalde mayor Don Andres Chuquitapa»
    Afirmante: «parroco interino» (informante) [= Agustín Valdés, cura interino de Tinta, según reconstrucción]; informe P23, fecha escrita «Noviembre 26 de 1806»; ante: no consta; redacta: no consta (la redacción de esta pieza está DISPUTADA: ver atributo «redactó la pieza»); firma la pieza: Firma
    Fundamento invocado: no lo indica; fuerza institucional: informativa; UT16.b, folio 28
AFIRMACIÓN A-UT17-003: ejerce o ejerció un cargo → recaudador de tributos
    «recaudador de tributos de los Ayllus Tinta y Ucho Don Andres Chuquitapa»
    Afirmante: «Pedro de la Mata» (informante) [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; informe P27, fecha escrita «Siquani Noviembre 8 de 1806»; ante: no consta; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: no lo indica; fuerza institucional: informativa; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT17-812: ejerce o ejerció un cargo → recaudador de tributos
    «insultar al Recaudador con palabras injuriosas»
    Afirmante: «Pedro de la Mata» (informante) [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; informe P27, fecha escrita «Siquani Noviembre 8 de 1806»; ante: no consta; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: no lo indica; fuerza institucional: informativa; UT17, folio no consta en la transcripción
AFIRMACIÓN A-UT18-812: ejerce o ejerció un cargo → recaudador de tributos
    «sublevar a todos los Indios contra su recaudador»
    Afirmante: «Pedro de la Mata» (informante) [= Pedro de la Mata, subdelegado del partido de Tinta | «[María Rubrica]» es la rúbrica del subdelegado Mata, según reconstrucción]; informe P27, fecha escrita «Siquani Noviembre 8 de 1806»; ante: no consta; redacta: no consta; firma la pieza: no consta
    Fundamento invocado: no lo indica; fuerza institucional: informativa; UT18, folio no consta en la transcripción
AFIRMACIÓN A-UT19-806: ejerce o ejerció un cargo → recaudador de tributos
    «con el recaudador de tributos Don Andres Chuquitapa»
    Afirmante: «Muñoz» (autoridad que resuelve) [= Francisco Muñoz y San Clemente («Muñoz y Señor Clemente»), presidente en noviembre de 1806, según reconstrucción]; auto P28, fecha escrita «Cusco y noviembre 26 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Muñoz
    Fundamento invocado: no lo indica; fuerza institucional: resolutiva; UT19, folio 33
AFIRMACIÓN A-UT19-809: ejerce o ejerció un cargo → recaudador de tributos
    «contra el recaudador de tributos Andres chuquitapa»
    Afirmante: «Gonzalo del Rio» (dictaminador) [= Luis (o Lucio) Gómez / Gonzalo del Río, fiscal de la Real Audiencia del Cusco, según reconstrucción]; vista fiscal P29, fecha escrita «Noviembre 20 de 1806»; ante: no consta; redacta: no consta; firma la pieza: Gonzalo del Rio
    Fundamento invocado: no lo indica; fuerza institucional: dictaminadora; UT19, folio 33

  EJERCICIO DE CARGO (capa 4): alcalde mayor (de indios) — vigencia: 1806-01-01 a 1806-12-31 (Consta en 1806 por una sola fuente.); creencia: probable; premisas: A-UT16b-002
  EJERCICIO DE CARGO (capa 4): cacique — vigencia: 1806-01-01 a 1806-12-31 (Consta en 1806 (carátula UT00; certificación P03: «los indios del cacique don Andrés Chukitapa»; informe del cura). Ninguna pieza dice que fuera cacique en tiempos de Reparaz: P03 lo llama cacique en presente y le atribuye un hecho pasado.); creencia: verdadero; premisas: A-UT02-304 A-UT16b-001
  EJERCICIO DE CARGO (capa 4): recaudador de tributos — vigencia: 1806-08-01 a 1806-11-30 (Inicio y fin son las fechas atestiguadas (agosto–noviembre de 1806), no el inicio ni el fin del cargo. Según el denunciante ocultaba tributarios «de muchos años atrás» (UT05), y P14 remite a una denuncia anterior «en once de Febrero del año pasado de 1809» (léase probablemente 1805, F4) que ya iba contra él como recaudador.); creencia: verdadero; premisas: A-UT05-001 A-UT07-001 A-UT09-502 A-UT09-520 A-UT10-506 A-UT17-003 A-UT19-806
```

## PC19

```text
PREGUNTA: ¿Son la misma persona «Mariano Casorla» (declarante) y «Martin Cazorla» (certificante)?
RESPUESTA (R): Hay 3 reconstrucciones en competencia; ninguna se impone en el grafo: «El declarante de P19 es Martín Cazorla (hipótesis A)» (probable); «El declarante de P19 es un Mariano Casorla distinto de Martín (hipótesis B)» (improbable); ««el Gobernador Señor Don Mariano Casorla» (P19) es una mala lectura de «el granadero … Martin Casorla»» (posible).

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «El declarante de P19 es Martín Cazorla (hipótesis A)» — creencia: probable; autor: claude-opus-5-5; fecha: 2026-11-13
    Deriva de: cc-14-18/mencion/M-UT04-001 cc-14-18/mencion/M-UT04-002 cc-14-18/mencion/M-UT12.a-005 cc-14-18/mencion/M-UT12.a-006
    Argumento: Al declarante se le muestra «la certificación De folio 4 su firma Martin casorla» y habla de ella en primera persona: mandó a Simón Arce ponerla por escrito, no sabe escribir y «no sabe quien lo transcribio ni firmo su nombre en el papel» (A-UT12b-003): el nombre escrito es el del declarante. En tiempos del Rebelde «era muchacho» (28 años en 1806, unos 2 o 3 en 1780, lectura algo forzada). Un «Gobernador Señor Don», analfabeto, de 28 años y «vecino Español» es anómalo; P05 lo presenta como «soldado granadero», y una abreviatura de «granadero» y «Martin» leída como «Gobernador» y «Mariano» explicaría ambas anomalías (ver R-declarante-p19-gobernador-es-granadero); el testigo «MARIANO FIGUEROA» de la línea anterior pudo favorecer esa lectura. Compite con R-declarante-p19-es-mariano. No se ha cotejado la imagen del folio; la conclusión queda sujeta a ese cotejo. Revisada tras la auditoría I (2026-11-13).
RECONSTRUCCIÓN «El declarante de P19 es un Mariano Casorla distinto de Martín (hipótesis B)» — creencia: improbable; autor: claude-opus-5-5; fecha: 2026-11-13
    Deriva de: cc-14-18/mencion/M-UT12.a-005
    Argumento: Único apoyo: la lectura literal «el Gobernador Señor Don Mariano Casorla», con un tratamiento que es anómalo por sí mismo (un «Gobernador» vecino español y analfabeto). En contra: el declarante habla en primera persona de la certificación de Martín («mando el que declara a Simon Arce»), dice que no sabe quién «firmo su nombre», declara 28 años y no sabe escribir. La variante más defendible de esta hipótesis sería un pariente que responde por Martín, pero choca con esos mismos datos. No se ha cotejado la imagen del folio; la conclusión queda sujeta a ese cotejo. Revisada tras la auditoría I (2026-11-13).
RECONSTRUCCIÓN ««el Gobernador Señor Don Mariano Casorla» (P19) es una mala lectura de «el granadero … Martin Casorla»» — creencia: posible; autor: claude-opus-5-5; fecha: 2026-11-13
    Deriva de: cc-14-18/mencion/M-UT04-001 cc-14-18/mencion/M-UT12.a-005
    Argumento: Hipótesis paleográfica que refuerza R-declarante-p19-es-martin: P05 presenta a Martín Cazorla como «soldado granadero» (A-UT04-201); un «Gobernador» analfabeto (A-UT12b-001), de 28 años y vecino español, es anómalo en un pueblo de indios; abreviaturas como «Gran.ro» y «Mart.n» pudieron leerse «Gobernador» y «Mariano». No se ha cotejado la imagen del folio; la conclusión queda sujeta a ese cotejo. Creada tras la auditoría I (2026-11-13), como propuesta del modelo.

Mención afectada: https://w3id.org/laad/id/cc-14-18/mencion/M-UT12.a-005
```

## PC20

```text
PREGUNTA: ¿De dónde procede el dato A-UT11-004?
RESPUESTA (P): Procedencia del dato (PROV-O), no del testimonio de 1806.

  grafo https://w3id.org/laad/grafo/cc-14-18/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/cc-14-18/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-13T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/cc-14-18/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/cc-14-18/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-13T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/cc-14-18/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/cc-14-18/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-13T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/cc-14-18/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/cc-14-18/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-13T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/cc-14-18/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/cc-14-18/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-13T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/cc-14-18/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/cc-14-18/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-13T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/cc-14-18/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/cc-14-18/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-13T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/cc-14-18/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/cc-14-18/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-13T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/cc-14-18/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/cc-14-18/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-13T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/cc-14-18/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/cc-14-18/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-13T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/cc-14-18/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/cc-14-18/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-13T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/cc-14-18/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/cc-14-18/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-13T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/cc-14-18/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/cc-14-18/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-13T00:00:00, validación humana: NO REGISTRADA
  grafo https://w3id.org/laad/grafo/cc-14-18/afirmaciones/anotacion-manual-expediente-v1 (afirmaciones): actividad https://w3id.org/laad/id/actividad/cc-14-18/anotacion-manual-expediente-v1, agente claude-opus-5-5 (SoftwareAgent), plan «anotacion-manual», transcripción sha256:bd945513f8e1d8c34dbdc980623bb5740e9077d35a802100f7464afb5dafaafe, fecha 2026-11-13T00:00:00, validación humana: NO REGISTRADA
```
