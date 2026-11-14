# Observaciones sobre la capa 3 al agrupar hechos narrados (propuesta de capa 4)

> Autor: claude-fable-5-2 · Fecha: 2026-11-14 · Expediente: cc-14-18
> Acompaña a `datos/propuestas/hechos.jsonl` y `datos/propuestas/hechos_sin_enlazar.csv`.
> Fuente: la transcripción leída por tramos con `laad.fuente.tramo` y los registros de `datos/registros/`. No se ha usado
> `corpus/corpus_modernizado.txt` ni hay imágenes de los folios. «…» es cita literal con los espacios colapsados.
> **[inferencia]** marca lo que no dice el texto. Aquí solo se anotan los problemas; no se ha corregido nada.

## 1. Resultado

| | Antes | Propuesta |
|---|---|---|
| Hechos narrados | 61 | 61 |
| Agrupados en alguna reconstrucción | 13 | 46 |
| Sin enlazar | 48 | 15 (con motivo en el CSV) |
| Reconstrucciones de hecho | 2 | 13 (2 modificadas, 11 nuevas) |

Pares rivales (cada uno nombra al otro en su argumento y comparten hechos):

| Un episodio | Dos episodios | Qué se discute |
|---|---|---|
| R-agresion-dia-prision (probable) | R-golpes-conduccion-carcel (posible) | Si la acometida que Mata dice haber cortado en la casa (H-p27-acometida) es el mismo suceso que los golpes camino de la cárcel |
| R-tumulto-tiempo-reparaz (probable) | R-alzamiento-orey (posible) | Si el motín que narra Orue (H-p21-motin) es el «alzamiento contra don Miguel Orey» de P01 y P03 |
| R-incidente-previo-a-prision (posible) | R-insulto-al-recaudador (probable) | Si la «queja» de Chuquitapa según el denunciante (H-p06-queja) y el «insulto» según Mata son dos versiones del mismo incidente |

En las dos reconstrucciones modificadas (R-alboroto-carcel, R-prision) se ha conservado el autor original
(«claude-opus-5-5») y su argumento; la ampliación va al final, firmada y fechada, y el campo `fecha` pasa a 2026-11-14. El
esquema solo admite un autor: quien integre la propuesta debe decidir si lo cambia.

El esquema no tiene un campo para declarar hipótesis rivales; la rivalidad solo consta en el texto del argumento
(«Rival: R-…»). El validador de esta propuesta la detecta así. Convendría un campo propio (`rival_de`).

## 2. Dos sucesos bajo un mismo identificador de hecho

1. **H-p04-maltrato (P04).** Reúne «he visto con mis ojos, mortales el alboroto que hicieron los Indios del Ayllu de tinta
   contra Manuel Huancachoque» (A-UT03-203, A-UT03-204) y «los indios llevaron preso a la cárcel maltratando cruelmente»
   (A-UT03-207). La primera frase es la entrada general de la certificación y puede abarcar también el alboroto nocturno
   («peor alboroto», H-p04-alboroto). El «vista» de A-UT03-203 queda así atribuido a los golpes de la conducción, cuando el
   texto lo dice de «el alboroto» en general.
2. **H-p21-motin (P21).** Junta dos momentos: «se juntaronmosos indios y lo votaron de la carcel» (reunión ante la cárcel; el
   objeto de «lo votaron» es dudoso, quizá Diego Orue) y «se amotinaron contra el corregidor y contra el padre del que
   declara» con el refugio en casa del corregidor. El pasaje «en cuya noche le vaguear y maltrataron sin casa» no tiene
   lugar ni víctima anotados. **[inferencia]** Puede leerse «le saquearon y maltrataron su casa», lo que lo acercaría al
   ataque a la casa de Orey de P01 y P03.
3. **H-p06-averiguacion (P06).** Mezcla la orden del presidente (ordenante) con la averiguación que hizo el apoderado fiscal.
   En P14 la orden está aparte (H-p14-remision-primera-denuncia). Por eso R-averiguacion-ocultacion queda en probable.
4. **H-p05-maltrato y H-p05-prision (P05).** El texto cuenta dos veces la conducción («estiraron a golpes de los pelos
   pusieron a la cárcel» y «El siguiente día de la revisita pidieron a la cárcel al denunciante, maltratando cruelmente»).
   La anotación reparte las frases entre «maltrato» y «prisión» por orden de aparición, no por suceso: la fecha «El siguiente
   día de la revisita» solo consta en la prisión y el segundo «maltratando cruelmente» queda en la cita de la prisión.
5. **H-p27-prision (P27).** La puesta en libertad («al que puse en libertad al otro dia por la tarde») está anotada como
   duración y como «motivo» de la prisión (A-UT18-806; la nota ya advierte que es el motivo de la libertad). Es otro suceso.

## 3. Sucesos narrados en el texto que no están anotados como hecho

1. **La numeración o revisita de los ayllus Tinta y Ucho.** Es el ancla de toda la cronología («El siguiente día de la
   revisita», P05; «al siguiente día que prove la ocultación de Indios», P06; «concluida el dia anterior la numeración de los
   Ayllos Tinta, y Ucho», P27; «matriculados en la nueba revisita», P16) y no existe como hecho. Tampoco la presentación de
   los 51 tributarios ante el juez («los mismos que precente a presencia del recaudador y juez subdelegado», P06), a la que
   puede aludir el «en la revisita» de H-p07-denuncia.
2. **Los golpes según el declarante de P19.** «los Yndios que lo llevaban preso ala cárcel o alguno parien tes de Chuquitapa
   lo golpeaban con puñadas y patadas» solo figura como objeto de «solicita» (A-UT12b-501). Es la única confirmación jurada
   del contenido de P05 sobre los golpes y no se puede enlazar con R-agresion-dia-prision.
3. **El relato de Cano que repite Santiago Cazorla en P20.** «todos los indios alzaron a media noche armados con garrotes»
   está solo como «dijo» (A-UT13-505). Ya lo señaló la auditoría I. Además, Santiago Cazorla no confirma haber contado eso a
   Cano, como dice este en P18 («se lo dijo su segundo sargento Santiago Casorla»): cuenta otra cosa (H-p20-visita). Esa
   discrepancia entre P18 y P20 no se puede representar hoy.
4. **Las guardias en las puertas de los españoles.** P03 las tiene como hecho propio (H-p03-guardias); en P01 («con guardias
   nuestras. puertas») no están anotadas, y en P18 («poniendo guardias a las puertas de estos») van dentro de la cita de
   H-p18-alboroto. Con una granularidad pareja habría tres relatos que comparar.
5. **Detalles de la noche en P06 y P03.** El intento de forzar la puerta («no pudiesen deserrajar la cerradura de la puerta»,
   P06; «si esa noche parece la llave de la carcel, lo matan», P03) y «los alaridos aterrorizaron el pueblo» no son atributos
   de H-p06-alboroto ni de H-p03-alboroto. Son el núcleo de lo que el hecho mínimo de R-alboroto-carcel deja fuera.
6. **La orden de no pegarle (P18).** «habiendo mandado Esta ponerlo en la caecel a Guancachoque y que se contuvieran en no
   darles puñadas después que se separo dicho …..» no tiene ordenante ni está anotada la orden de contenerse. Es la frase
   que une la versión de Mata con la del denunciante (véase R-agresion-dia-prision).
7. **La diligencia con el común y principales (P27).** «otra diligencia sobre presentaciones que hiso de agravios», donde
   «lo convencieron de falsedad», no es un hecho; solo aparece como valor de veracidad y de motivo.
8. **La matrícula del denunciante según el fiscal (P07).** «averse matriculado en clase de tributario» está como condición
   (A-UT07-213), no como hecho, y H-p06-matricula se queda sin par.
9. **La notificación y el retiro de Chuquitapa (P16, P17).** «Inmediatamente le hize saber a D. Andre S. Chuquitape» y la
   orden de retirarse «à distan. cia de quatro leguas» están como «ordena» y «conoce-contenido». Las notificaciones de P30 y
   P31 sí son hechos. Con este criterio desigual, las órdenes ejecutadas no se pueden reconstruir como sucesos.
10. **Otras alusiones a la rebelión de 1780.** «lo mismo en el tiempo del rebelde. Tupa Amaro» (P01), «es desde el rebelde»
    (P05) y «cenisas calientes de la pesada Revelion» (P27) no tienen hecho. Solo lo tienen P04 y P23, con granularidad
    distinta: H-p04-alzamiento-1780 es «el otro alzamiento que hizo» Chuquitapa y H-p23-rebelion es la rebelión en general.

## 4. Afirmaciones que conviene revisar

1. **A-UT12b-502 (H-p19-prision).** «que el no sabia haber preso a Guancachoque» está con polaridad «afirma» y fundamento
   «no-consta» sobre la participación como preso. El declarante dice que no lo sabía; a la vez habla con él «estando en la
   carcel». Tal como está, cuenta como un testimonio a favor de la prisión.
2. **H-p19-castigo.** Solo tiene el motivo (A-UT12b-503), sin víctima ni agresor, y «lo castigaban» puede ser la prisión o
   los golpes. Por eso queda sin enlazar.
3. **H-p27-acometida.** La nota de A-UT18-801 dice que «los Alcaldes» (M-UT17-830) también son agresores, pero no hay
   afirmación que los una al hecho; solo constan «Segundas, y Principales».
4. **H-p06-queja.** El contenido de la queja («protestando le había yo perdido el respeto») está como «dijo» (A-UT05-218),
   sin vínculo con el hecho. Es lo que permite comparar con el insulto de P27.
5. **H-p01-prision, A-UT01-205.** La cita «lo pusieron a la carcel a esa noche» corta mal: «a esa noche» abre la frase
   siguiente («a esa noche todos los indios se alzaron a media noche»).
6. **A-UT01-219 (H-p01-alzamiento-orey).** «otra vuelta de dos horas» está como fecha del hecho; puede ser una segunda
   acometida o una duración (la nota ya lo dice). Si es una segunda acometida, serían dos momentos.
7. **H-p14-denuncia, A-UT10-503.** «en 27 de Agosto proximo pasado» coincide con la fecha del auto P10 y de su notificación
   al denunciante, no con la del escrito P06 (22 de agosto). **[inferencia]** Mata pudo tomar la fecha del decreto por la de
   la denuncia.
8. **H-p20-visita.** Las dos copias de la declaración dan fechas incompatibles («a las dos o tres de la madrugada de esa
   noche», UT13; «a los dos o tres dias desa noche», UT14). Si vale la segunda, la visita no es de la noche de la prisión.
9. **H-p23-escandalo, A-UT16a-810.** El pasaje está muy mal transcrito («juegos Real», «pues tuvo.» / «osadia que
   acometen»). El rol «agresor» de Huancachoque se apoya en una lectura reconstruida.

## 5. Nombres que afectan a las agrupaciones

* **«don Miguel Orey» (P01, P03) y el padre de Fernando Orue (P21).** **[inferencia]** Pueden ser la misma persona si
  «Orey» es grafía de «Orue»; de eso depende en buena parte R-tumulto-tiempo-reparaz. No hay reconstrucción de identidad
  para ninguno de los dos.
* **El corregidor.** «don Antonio Reparas» (P01), «Don Juan Antonio Reparas» (P04), «d juan antonio repuras» (P21) y
  «corregidor Don Andres ……» (P18, Cano bajo juramento). La auditoría I ya anotó esta última (N8).
* **El «revisitador» de Mata (P27), «el actual apoderado del fiscal» (P06) y «el señor Agustin Fiscal Don Althamacio
  Zotelo» (P23).** Las agrupaciones R-averiguacion-ocultacion y R-insulto-al-recaudador suponen que son la misma persona.
