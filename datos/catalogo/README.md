# Fichas del catálogo para PC03 y PC04

Fuente: `archivos/Catálogo Intendencia I CO y CC.pdf` (547 pp.; Archivo Regional del Cusco, Fondo
Intendencia, Tomo I: Causas Ordinarias y Causas Criminales). Todo lo que hay en
`fichas_pc03_pc04.jsonl` es **lo que dice el catálogo** («según el catálogo»), no hechos del
expediente. La transcripción y el catálogo difieren (véase `docs/01_materiales.md`, §4.2, K1–K5).

## Estructura del catálogo

- Jerarquía: **Sección** (Causas Ordinarias, Causas Criminales) › **Serie** (Cusco, Provincias) ›
  **Legajo n** › **Expediente n. Año(s): …** › resumen › **Folios: n.**
- Páginas PDF: Causas Ordinarias, Cusco, pp. 18–340; Provincias, pp. 341–383; Causas Criminales,
  Cusco, pp. 386–468; Provincias, pp. 469–482; código de índices, p. 483; Índice Onomástico,
  pp. 484–533; Índice Toponímico, pp. 534–547.
- Página impresa = página PDF − 3. Se comprobó en todas las páginas con folio impreso de la 16 a la 547.
- Signatura de los índices: `COc`, `COp`, `CCc`, `CCp` + `legajo (expediente)`, por ejemplo
  `CCc 14 (18)`.
- Los índices están a dos columnas. `pdftotext -layout` las pone una al lado de la otra. Las
  entradas que pasan de una columna o de una página a otra se han unido a mano (está anotado en `dudas`).

## Método

1. `pdftotext -layout -f p -l p` de cada página (1–547). El PDF tiene capa de texto (PDFium); no se
   hizo OCR nuevo.
2. Script de análisis (en el scratchpad, no en el repositorio). Lee las pp. 16–483, sigue
   las cabeceras `Sección:`, `Serie:` y `Legajo n`, y corta cada ficha en `Expediente n.`. Salen
   3672 fichas: COc 2573, COp 335, CCc 656 y CCp 108. Quita las líneas que son solo el número de página impresa.
3. Búsqueda con expresiones regulares, sin distinguir mayúsculas, en el texto de las fichas y en las
   páginas de los índices (pp. 484–547).
4. PC04: se leyeron a mano **todas** las fichas de Causas Criminales (Cusco y Provincias) cuyo
   intervalo de años toca 1805–1807 (50 fichas). Cuenta lo que dice la ficha sobre el acusado o
   demandado, no sobre el demandante.
5. `texto_literal` guarda las líneas tal como las da `pdftotext`, unidas con `\n` y con el espaciado
   del modo layout normalizado. `pagina_pdf` es la página donde empieza la ficha; `paginas_pdf` y
   `paginas_impresas` dan el intervalo completo.

## Términos buscados

- Chuquitapa: `quitap`, `qetap`, `quetap`, `kitap`, `chiquitas` (cubre Chuquitapa, Chuquiitapa,
  Choquitapa, Choquetapa, Chukitapa, Chuquitape, Chiquitas).
- Guancachoque: `[gh]uanca\w*`, `\b[gh]uanca\b`, `choq|choc|chok` (cubre Guancachoque,
  Huancachoque, Mancachoque, Guamanchoque, Guancoichoque y otras formas con -choque).
- Tinta: `\btinta\b` y variantes de OCR `t[il1í]n[tl]a` (no hubo más resultados). Se descartan
  `distintas`, `extinta` y `Tintaya`, que es un apellido (COp 11 (10)).
- Personas relacionadas, como control: `cazorla|casorla|casola`.
- PC04: lectura a mano. Términos de control: cacique, casique, recaudador, alcalde (de indios /
  mayor / de españoles), gobernador.

## Resultados

### PC03

- **Chuquitapa** y **Guancachoque**: según el catálogo, solo aparecen en CCc 14 (18), tanto en las
  fichas como en el índice onomástico. Entradas: «Chuquitapa Andrés: CCc 14 (18)» (p. PDF 496) y
  «Guancachoque, Manuel: CCc 14 (18)» (p. PDF 505). No hay entradas «Huancachoque», «Mancachoque»
  ni «Choquitapa». Tampoco aparece «Juan Casola» (CCc 14 (18)) en el índice onomástico.
  Falsos positivos descartados: «Guanca, Miguel» (COc 6 (14), una hacienda), «Huanca, Nicolás»
  (COc 83 (21)) y los apellidos Choque, Choquehuanca y Choquecahua.
- **Tinta**: 62 fichas lo nombran, contando CCc 14 (18). Ninguna otra ficha nombra a Chuquitapa ni a Guancachoque.
  - «Pueblo de Tinta» explícito en la ficha: COc 1 (13), COc 3 (1), CCc 14 (18) y CCc 19 (24).
  - El resto habla de partido, provincia, doctrina, cura, subdelegado o regimiento «de Tinta». Es una
    jurisdicción más amplia, o una institución, y no prueba que se trate del pueblo. Cada registro
    lo marca con `tinta_pueblo_explicito`.
  - Índice toponímico, entrada «Tinta» (pp. PDF 545–546): todas sus remisiones tienen ficha que
    nombra Tinta. Hay **8 fichas que nombran Tinta y no están en el índice**: COc 17 (4), 25 (19),
    29 (22), 42 (37), 43 (10), 57 (38), 90 (8) y 90 (9). El índice solo califica como «pueblo» a
    COc 1 (13); CCc 14 (18) aparece sin calificador. El campo `en_indice_toponimico_tinta` lo recoge.

### PC04 (Causas Criminales, 1805–1807, acusado cacique, recaudador o alcalde de indios)

- Seguros: **CCc 14 (18)** (1806, «el cacique Don Andrés Chuquitapa») y **CCc 14 (21)**
  (1806–1807, «su cargo de recaudador a Don Agustín Brabo»). En este último, la ficha no dice «de
  tributos».
- Dudosos, porque la ficha no especifica el tipo de alcalde: **CCc 14 (14)** («Don Juan
  Villafuerte, alcalde de Acomayo»), **CCc 14 (22)** («Miguel Guambo, alcalde de Yanatili») y
  **CCc 15 (5)** («Don Pascual Pareja, alcalde mayor de la parroquia de san Jerónimo»).
- Excluidos tras leerlos:
  - CCc 13 (10): el recaudador Valentín del Valle es el demandante.
  - CCc 14 (17): Andrés Mochongo es «alcalde de españoles».
  - CCc 14 (4): la denuncia se presenta «al alcalde mayor» y el acusado es un cura.
  - CCc 15 (6) y CCc 15 (10): el alcalde mayor es el denunciante.
  - CCc 14 (5): Juan Villafuerte es el acusado, pero la ficha no le da cargo.
  - CCp 7 (10): Agustín Bravo es el denunciante, y nada en la ficha lo identifica con el
    recaudador de CCc 14 (21).
  - CCc 17 (4): el año impreso es «1817-1718», una errata, y queda fuera del intervalo.

## Límites

- Se busca en una capa de texto que ya existía. No se revisaron a ojo las imágenes de las páginas,
  así que puede faltar alguna grafía que el texto haya estropeado.
- Los años se toman de la cabecera de la ficha. Se aceptan los intervalos que tocan 1805–1807,
  aunque solo sea en parte (por ejemplo, 1804–1805).
- El rol procesal («acusado») se deduce de la redacción del resumen, que es irregular.
- El Tomo II (Gobierno, Real Hacienda) no está en el PDF y no se consultó.
- Discrepancia con `docs/01_materiales.md`: la ficha CCc 14 (18) está en las pp. PDF 438–439, que
  son las pp. impresas 435–436, y no en las «pp. 434–435».
