# 01 · Materiales, capa de fuente y contradicciones de los materiales

> Estado: verificado contra `corpus/Transcripcion_CC_L14E18.txt` (sha256 `bd945513…afaafe`) y contra el
> catálogo (`archivos/Catálogo Intendencia I CO y CC.pdf`, pp. 434–435 del PDF impreso). Toda afirmación de este
> documento sobre el expediente lleva el **tramo** (`UTnn[.x]`) donde se comprueba. Lo inferido se marca **[inferencia]**.

## 1. Inventario y orden de autoridad

| # | Material | Uso permitido | Observaciones verificadas |
|---|----------|---------------|---------------------------|
| 1 | Imágenes de los folios | Fuente de verdad (cotejo de folio y recto/vuelto) | **No están en el proyecto.** Sin ellas, no se puede fijar recto ni vuelto (ver §3). |
| 1 | `corpus/Transcripcion_CC_L14E18.txt` | Única fuente citable | UTF-8 con BOM y saltos CRLF; 334 líneas; 20 separadores `#` → 21 unidades. |
| 2 | `corpus/corpus_modernizado.txt` | Lectura y búsqueda; **nunca se cita** | Segmenta distinto (19 `#`) y resuelve variantes sin avisar (§4.3). |
| 3 | Ficha del catálogo ARC (Tomo I) | Dato a contrastar | Difiere de la transcripción en grafía, contenido y número de folios (§4.2). |
| 3b | `archivos/La_organizacion_y_catalogacion_del_Fondo_Intendenc.pdf` | Contexto de la organización del fondo | Artículo sobre la catalogación; no describe el expediente. |
| 4 | Intento previo (`../Grafo-Conocimiento-Cusco`) | Objeto de diagnóstico | Ver `docs/A_diagnostico.md`. El "intento 2" no se pegó en la solicitud: el marcador `[Pegar aquí…]` llegó vacío. |

## 2. Unidades de transcripción y tramos

Implementado en `src/laad/fuente.py`; índice generado en `fuente/tramos.csv` (`scripts/indice_fuente.py`).

* **UT (unidad de transcripción)**: bloque entre dos líneas `#`. **[inferencia]** Lo más probable es que cada UT sea una imagen o una cara del original. Prueba de que no equivale a un folio: dentro de la UT12 y de la UT16 aparecen marcas de folio a mitad de frase.
* **Tramo**: parte de una UT delimitada por una marca de folio explícita del transcriptor. Las cuatro marcas se verificaron a mano:

| Tramo | Marca exacta | Folio | Contexto |
|---|---|---|---|
| UT12.b | `Folio 20` | 20 | A mitad de la declaración sobre la certificación firmada «Martin casorla» |
| UT16.b | `folio 28` | 28 | A mitad del informe del cura |
| UT19 | `Folio 33` | 33 | Auto del 26 de noviembre de 1806 |
| UT20 | `[Folio 34 ]` | 34 | Final de la vista fiscal |

Las referencias que el documento hace a sí mismo («a folios 2», «De folio 4», «En folio 10», «en folio 2») **no** son marcas del transcriptor. Se modelan como afirmaciones del documento sobre su propia foliación. Que las dos foliaciones coincidan es una cuestión abierta: por ejemplo, la certificación «De folio 4» firmada por Martín Cazorla está en la UT04.

Tramos sin marca → folio **«no consta en la transcripción»**. Recto/vuelto → **no consta en ningún tramo**.

## 3. Consecuencia para el criterio «cita con folio y recto/vuelto»

El criterio de la solicitud no puede cumplirse completo con los materiales actuales. Se divide en dos partes:

1. **Cita ↔ tramo (comprobable hoy, umbral 100 %)**: la cita debe ser subcadena exacta del tramo indicado. La única normalización admitida es colapsar espacios en blanco, porque la transcripción corta frases entre líneas. Se conservan mayúsculas, acentos, grafías y errores. Implementado en `verificar_cita` y en `scripts/verificar_citas.py`.
2. **Tramo ↔ folio y recto/vuelto (pendiente de las imágenes)**: tabla de cotejo `fuente/folios_cotejo.csv`, que debe rellenar una persona con las imágenes delante. Mientras tanto, toda respuesta dice «folio no consta en la transcripción; UTnn».

## 4. Contradicciones de los materiales (enumeradas, no resueltas)

Cada contradicción es candidata a modelarse como afirmaciones en conflicto (capa 3), no como errores que haya que corregir. Si una corrección es plausible, se anota como **[inferencia]** con su autor, nunca sobre el texto.

### 4.1 Dentro de la transcripción paleográfica

**Fechas de secuencia imposible o dudosa**

| ID | Dónde | Lo escrito | Problema |
|---|---|---|---|
| F1 | UT08 | vista fiscal «Cusco y Agosto 21 de 1806» | Es anterior al escrito que dictamina, datado «CUSCO AGOSTO 22 DE 1806» (UT05). |
| F2 | UT08 | ratificación «en trece días del mees de Agosto» | Es anterior al decreto que la manda (21 o 23 de agosto). |
| F3 | UT10 | «denuncia … hecha … en 27 de Agosto proximo pasado» | El escrito tiene fecha del 22 y la carátula del 26. |
| F4 | UT10 | primera denuncia «en once de Febrero del año pasado de 1809» | Es posterior al documento (1806). El corpus modernizado escribe 1805 sin indicarlo. |
| F5 | UT16.b | informe del cura «Noviembre 26 de 1806» | Lo pide el subdelegado el 24 de septiembre (UT15) y lo cita el informe del subdelegado del 8 de noviembre (UT18). |
| F6 | UT20 | notificación «veinte y tres de Diciembre de mil ochocientos 10 años» | 1810 no encaja; el corpus modernizado pone «[...]». |
| F7 | UT17 | «Cuzco noviembre 18 de noviembre de 1806 vista al señor» | Fecha de la remisión a vista. Es coherente con el informe del 8 y la vista del 20, pero la transcripción la escribe dos veces. |

**Nombres de personas: variantes o personas distintas (no se fusionan)**

| ID | Menciones (tramo) | Cuestión |
|---|---|---|
| N1 | «Mancachoque» (UT00); «Guancachoque» (passim); «Huancachoque» (UT02, UT03, UT04, UT05); «Guamanchoque» (UT02); «HUANCACHOQQUE» (UT06); «Guancoichoque» (UT19); «gancahoque», «guarcachoque», «guasscachoque», «guancachay» (UT14–15) | Variantes del denunciante; el catálogo usa «Guancachoque». |
| N2 | «Chuquiitapa» (UT01); «Chukitapa» (UT02); «Choquitapa» (UT05); «Choquetapa» (UT09); «Chuquitape» (UT11); «chuquitaza» (UT14); «Chiquitas» (UT15) | En UT15, «la mujer de Chiquitas» se refiere por contexto a Chuquitapa. **[inferencia]** |
| N3 | «teniente Alguacil, don Juan Quiñones» como autor y «Juan Cazorla» como firmante (UT02); «no hay tal hombre en el pueblo de Tinta» (UT17) | Disputa de identidad del autor de la certificación: dos menciones y ninguna fusión. |
| N4 | Certificación firmada «Martin Cazorla» (UT04); declarante «el Gobernador Señor Don Mariano Casorla» al que se muestra la certificación «De folio 4 su firma Martin casorla» (UT12.a) | La transcripción no aclara si el declarante es Martín, que dice que no sabe escribir y tiene 28 años. |
| N5 | «Pedro de la Mara» (UT10, UT11); «Pedro de la Mata» / «PEDRO DE LA MATA» (UT11, UT12.b, UT18); «pedro de Mata» (UT15); «[María Rubrica]» (UT17) | El subdelegado. El corpus modernizado unifica «Mata». |
| N6 | «Luis Gomez del Rio» (UT08); «Luis Gonsalo del Rio» (UT09); «Gonzalo del Rio» / «Lucio Gonzalo del Rio y Vial» (UT20) | El fiscal. |
| N7 | «Doctor Don Antonio Valdes», tío del cura interino (UT15); «Doctor Don Agustin Valdes», cura interino (UT18) | El texto los presenta como **dos personas**; fusionarlos sería un error. |
| N8 | Corregidor «don Antonio Reparas» (UT01); «Don Juan Antonio Reparas» (UT03); «corregidor Don Andres ……» (UT11, declaración de Cano); «d juan antonio repuras» (UT14) | Cano da un nombre distinto en su certificación y en su declaración. |
| N9 | Santiago Cazorla: «sargento primero» (UT02); «su segundo sargento Santiago Casorla» (UT11); «segundo … santiago cacerola» (UT13) | Grado discrepante. |
| N10 | «Ruiz de Castilla» (UT09), «Castilla» (UT09), «Muñoz» (UT19), «Don Francisco Muñoz y Señor Clemente» (UT18) | Firmantes con autoridad de presidente en agosto y noviembre. |

**Hechos narrados de forma incompatible** (son el núcleo de las preguntas de competencia «en disputa»)

| ID | Tema | Versiones (tramo) |
|---|---|---|
| H1 | Hora del alboroto ante la cárcel | «a media noche» (Cano, UT01); «a las dies o a las once» (Quiñones/J. Cazorla, UT02); «a las diez de la noche» (Orue, UT03); «a las nueve de la noche» (Huancachoque, UT06); «no fue a las dies de la noche … sino el primer puesto del gallo» (Orue, UT14) |
| H2 | Duración de la prisión | «dos días preso» (Huancachoque, UT06); «esa misma noche … puse en libertad al otro dia por la tarde» (Mata, UT18) |
| H3 | Quién redactó las certificaciones | Las hizo el propio Guancachoque y otros las firmaron sin saber lo que decían (Mata, UT17); las redactó Simón Arce por encargo (declarante de UT12.b); las escribió un hijo del declarante (Orue, UT14); la firma es suya (Cano, UT11–12.a) |
| H4 | Papel de Chuquitapa en 1780 | «Tupa Amaro fue complice y coronel» (Cert. Cano, UT01); «en tiempo de su pariente Tupaamaro fue coronel, comecionado» (Cert. Orue, UT03); «Comisionado por este y no coronel» (Decl. Cano, UT11); «fue en tiempo del rebelde tupa-amaru coronel y comisionado» (Decl. Orue, UT14); el declarante de UT12.b niega haber dicho «porque es desde el Rebelde» porque «era muchacho» |
| H5 | Imputación de 1780 contra el denunciante | «hijo Espurio de Antolin Ortiz, Sanbo cerros unos de los mas sangriento caudillo que tuvo … Tupac Amaro» (cura, UT16.a); «Chispa soplada por Guancachoque» (Mata, UT18) |
| H6 | Origen del tumulto | Venganza de Chuquitapa por la denuncia (Huancachoque, UT05–06; certificaciones UT01–04); insulto de palabra y obra al recaudador (Mata, UT17) |
| H7 | Condición del denunciante | «Indio originario y vecino del pueblo de Tinta» (UT05); «hasta aquí no había tributado» por servir en milicias (UT06); «soldado en mi compañía más de cinco años» (UT02); hijo de «Agustina Falcon India Ordinaria» (UT16.a) |

**Material ajeno al expediente**: el final de UT20, «El ciudadano Matias Ugarte = Notario Público de la provincia de Urubamba…», usa «ciudadano», un tratamiento republicano. **[inferencia]** Es el comienzo de otro documento, capturado en la misma imagen o secuencia. Se modela como `rico:Record` aparte, sin relación con el expediente.

**Repetición**: UT13 y UT14 contienen dos veces, con ligeras variantes, la declaración de Santiago Cazorla («a las dos o tres de la madrugada» / «a los dos o tres dias»). No se sabe si el original la repite o si es un error de transcripción: hay que cotejarlo con la imagen.

### 4.2 Transcripción frente a ficha del catálogo (CC, Serie Cusco, Legajo 14, Expediente 18, pp. 434–435)

| ID | Catálogo | Transcripción |
|---|---|---|
| K1 | Índice onomástico: «Guancachoque, Manuel: CCc 14 (18)» | La carátula dice «Mancachoque» (UT00); la forma mayoritaria es «Guancachoque». |
| K2 | «dos cartas de testigos, uno es de Juan Casola quien está a favor del indio y otro es de Andrés Chuquitapa quien está a favor del cacique» | No hay ningún escrito de Chuquitapa. Hay cuatro piezas de certificación con cinco firmantes (UT01–UT04). «Juan Casola» no aparece; sí «Juan Cazorla» (UT02). |
| K3 | «Folios: 19.» | Hay marcas de fol. 20, 28, 33 y 34. **[inferencia]** O el catálogo cuenta otra cosa, o las marcas siguen una foliación distinta. |
| K4 | Jerarquía: Sección Causas Criminales › Serie Cusco › Legajo 14 › Expediente 18 | La solicitud habla de «serie Causas Criminales»; en el catálogo, Causas Criminales es una **sección**. El modelo sigue al catálogo (capa 1). |
| K5 | La ficha no menciona Real Hacienda | La carátula lleva «Instancia … Real Hacienda» (UT00). |

### 4.3 Corpus modernizado frente a transcripción (resoluciones silenciosas)

| Paleográfica | Modernizado |
|---|---|
| «Guancachoque» (32 ocurrencias) | «Huancachoque» (45 en total) |
| «1809» (UT10) | «1805» |
| «Pedro de la Mara» | «Pedro de la Mata» |
| «Mariano Casorla» | «Mariano Cazorla» |
| «mil ochocientos 10 años» | «mil ochocientos [...] años» |
| «Reparas» | «Reparaz» |

Por eso el modernizado no puede alimentar la capa 2: borraría justo la variación que el modelo debe conservar.
