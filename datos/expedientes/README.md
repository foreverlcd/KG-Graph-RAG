# Manifiestos de expediente: cómo añadir un expediente nuevo

Cada archivo `datos/expedientes/<id>.json` es el **manifiesto** de un expediente: la única fuente de su
configuración. El código no contiene ningún identificador de expediente; añadir uno es añadir su manifiesto y
sus datos. `scripts/construir.py` construye el corpus con todos los manifiestos de esta carpeta que no estén en
`"estado": "borrador"`.

## Pasos

1. **Copiar la transcripción paleográfica** a `corpus/` (`.txt` o `.md`). No se edita después: su `sha256`
   identifica la versión citada y cada cita se verifica contra ella carácter por carácter.
2. **Crear el esqueleto y mirar la segmentación**:

   ```bash
   # solo ver cómo se corta, sin escribir nada (repetir hasta que la tabla sea la esperada)
   .venv/bin/python scripts/nuevo_expediente.py co-70-15 corpus/Transcripcion_CO_L70E15.md --formato markdown --solo-ver
   # crear el manifiesto (borrador) y datos/co-70-15/
   .venv/bin/python scripts/nuevo_expediente.py co-70-15 corpus/Transcripcion_CO_L70E15.md --formato markdown
   ```

   El guion imprime una fila por tramo (identificador, líneas, folio, número de caracteres y primeras palabras),
   crea `datos/expedientes/<id>.json`, `datos/<id>/piezas.jsonl` y `datos/<id>/registros/anotacion.jsonl`
   (vacíos) y **nunca sobrescribe**: si el manifiesto o la carpeta existen, termina con error.
3. **Curar el manifiesto a mano** (todo lo marcado `POR CURAR`; ver «Qué se cura a mano»).
4. **Fijar el índice de tramos** y revisarlo contra la transcripción:
   `.venv/bin/python scripts/indice_fuente.py <id>` escribe `fuente/<id>/tramos.csv`.
   Los identificadores de tramo (`UT03`, `UT12.b`) son las anclas de todas las citas: si después cambia el
   `formato` o las `marcas_folio`, cambian los tramos y hay que rehacer piezas y registros.
5. **Describir las piezas** (capa 1) en `datos/<id>/piezas.jsonl` y **anotar** menciones y afirmaciones
   (capas 2–3) en `datos/<id>/registros/*.jsonl`. Esquema de los registros: `src/laad/esquema.py`; vocabulario
   y conceptos candidatos: `ontologia/`.
6. **Verificar las citas** (umbral exigido: 100 %):
   `.venv/bin/python scripts/verificar_citas.py --expediente <id> datos/<id>/registros/*.jsonl`
7. **Incorporar el expediente al corpus**: quitar `"estado": "borrador"` del manifiesto y validar el lote junto
   con el resto del corpus, sin escribir el grafo:
   `.venv/bin/python scripts/validar_lote.py <id>`
8. **Construir**: `.venv/bin/python scripts/construir.py` escribe `datos/grafo/<id>.trig` y `.nq` (capas 1–3
   del expediente) y regenera `comun.trig`/`comun.nq`; valida SHACL. Después, `.venv/bin/python -m pytest -q`.
9. **Consultar**: `.venv/bin/python scripts/servir.py piezas expediente=<id>` (y el resto de consultas con
   nombre de `consultas/`).
10. Opcional, capa 4: las reconstrucciones (`datos/reconstrucciones.jsonl`) son comunes al corpus y citan los
    registros como `<id>:M-UT01-003`; una reconstrucción puede reunir menciones de varios expedientes.

## Qué se cura a mano

Nada de esto lo decide el código:

- la **segmentación**: que cada unidad y cada tramo de la tabla correspondan a lo que el transcriptor separó;
- las **marcas de folio**: cuáles son marcas del transcriptor y cuáles referencias internas del documento
  («a folios 2», «En folio 10» no son marcas). Si se usa `formato.marca_folio`, revisar una por una las filas con
  folio de la tabla;
- la **jerarquía archivística** (fondo › sección › serie › legajo › expediente), la `descripcion`, la
  `signatura_catalogo` y la `extension` (dato del catálogo, con su fuente);
- el `lote`: quién anotó, cuándo y con qué plan (procedencia PROV de las capas 2–3);
- las **piezas** y todos los **registros** (cada uno con su cita literal), y las **fechas normalizadas** con el
  argumento de la lectura;
- las **reconstrucciones** (capa 4) y su argumento.

## Claves del manifiesto

| Clave | Oblig. | Contenido |
|---|---|---|
| `id` | sí | Identificador del expediente (minúsculas, cifras y guiones: `cc-14-18`). Es el nombre del archivo, forma parte de las IRI (`…/id/<id>/mencion/…`) y de los grafos (`…/grafo/<id>/…`). No se cambia después. |
| `estado` | no | `"borrador"`: el expediente aún no entra en el corpus (lo deja así `nuevo_expediente.py`). Sus tramos y citas ya se pueden verificar por su identificador. Se quita la clave cuando el expediente está listo. |
| `descripcion` | sí | Referencia archivística legible (fondo, sección, serie, legajo, expediente, año). |
| `transcripcion` | sí | Ruta de la transcripción paleográfica, relativa a la raíz del repositorio (o absoluta). Única fuente citable del expediente. |
| `formato` | no | Convención de la transcripción (ver abajo). Sin esta clave rige la del piloto: unidades separadas por líneas `#`. |
| `marcas_folio` | sí (puede ser `[]`) | Marcas de folio verificadas a mano: lista de `[unidad, texto exacto de la marca, folio]`, p. ej. `["UT12", "Folio 20", "20"]`. Cada una corta su unidad en tramos (`UT12.a`, `UT12.b`) y da folio explícito al tramo que abre. Si el texto no aparece en la unidad, es un error. |
| `jerarquia` | sí | Niveles de descripción de mayor a menor: `{"id", "tipo", "titulo", "padre"}`. `tipo` es un concepto de tipo de conjunto documental con prefijo `rst:` o `doc:` (los que usa el piloto: `rst:Fonds`, `doc:seccion`, `rst:Series`, `doc:legajo`, `rst:File`); `padre` es el `id` del nivel superior (`null` en el primero). **El último nivel es el expediente**: su `id` da la IRI archivística con la que las consultas filtran (`?expediente`). Los niveles compartidos (fondo, sección, serie, legajo) deben llevar el mismo `id` en todos los manifiestos. |
| `extension` | no | Extensión según el catálogo: `{"cantidad", "unidad", "fuente", "nota"}`. |
| `piezas` | sí | Ruta del `.jsonl` de piezas (capa 1). |
| `registros` | sí | Lista de rutas de los `.jsonl` de menciones y afirmaciones (capas 2–3). |
| `fechas` | no (`null`) | Ruta del `.csv` de fechas normalizadas (`pieza,fecha,nota`); alimenta el control de secuencia. |
| `fechas_argumento` | no | Con qué criterio se normalizaron las fechas (se guarda como argumento de la reconstrucción). |
| `lote` | sí | Procedencia de la anotación: `{"nombre", "agente", "tipo_agente", "plan", "fecha"}` y, opcional, `"validado_por"`. `tipo_agente` es `SoftwareAgent` o `Person`; `fecha`, `AAAA-MM-DDThh:mm:ss`. |
| `signatura_catalogo` | no (`null`) | Signatura del expediente en los índices del catálogo (`CCc 14 (18)`): enlaza las fichas del catálogo con el expediente. |

## La clave `formato`

Describe cómo está escrita la transcripción para cortarla en **unidades de transcripción** (`UT00`, `UT01`, …) y
**tramos**. Todas sus claves son opcionales; las que faltan toman el valor por defecto. Una clave desconocida o
una expresión que no compila es un error. Las expresiones regulares son de Python y se aplican en modo
multilínea (`^` y `$` casan al comienzo y al final de cada línea); en JSON cada `\` se escribe `\\`.
La definición de referencia es `FORMATO_POR_DEFECTO` en `src/laad/fuente.py`.

| Clave | Por defecto | Significado |
|---|---|---|
| `codificacion` | `"utf-8-sig"` | Codificación del archivo (`utf-8-sig` lee UTF-8 con o sin BOM; `latin-1`, `cp1252`…). Los saltos CRLF se leen como LF. |
| `separador` | `"^[ \\t]*#[ \\t]*$"` | Línea que **separa** unidades. La línea casada no pertenece a ninguna unidad. `null`: no hay separadores. |
| `encabezado` | `null` | Línea que **inicia** una unidad y pertenece a ella (es citable). P. ej. `"^#{1,3} "` (títulos Markdown) o `"^\\[?[Ff]olio \\d+"`. Puede combinarse con `separador`. |
| `marca_folio` | `null` | Marca de folio detectada automáticamente: expresión con **un grupo que captura el folio** (o un grupo `(?P<folio>…)`), p. ej. `"^\\[f\\. ?(\\d+[rv]?)\\]"`. Cada coincidencia abre un tramo con ese folio, como una entrada de `marcas_folio` (las dos fuentes se suman; en la misma posición manda la escrita a mano). |
| `ignorar` | `null` | Texto **editorial** que no es transcripción: una expresión o una lista. P. ej. `"(?s)\\A---\\n.*?\\n---\\n"` (preámbulo YAML), `"(?s)<!--.*?-->"` (comentarios), `"^> .*$"` (notas del editor). |

Reglas de la segmentación:

- `UT00` es lo que hay antes del primer corte (la carátula en el piloto). Las unidades se numeran por orden de
  corte; una unidad sin texto no produce tramo, pero su número no se reutiliza (si el archivo empieza con un
  encabezado, la primera unidad es `UT01`).
- Una unidad sin marcas de folio es un solo tramo (`UT03`). Con marcas se parte en `UT12.a`, `UT12.b`, … (tras
  la `z`: `aa`, `ab`…). Solo el tramo que abre una marca tiene folio explícito; el resto queda «no consta».
- Lo que casa `ignorar` se sustituye por espacios en el texto citable: los desplazamientos y los números de
  línea siguen siendo los del archivo, ninguna cita puede contener ese texto, y no corta unidades ni cuenta como
  marca. Una cita sí puede continuar al otro lado de una línea ignorada, igual que al otro lado de un salto de
  línea.
- Una expresión de `marca_folio` poco estricta toma por marcas las referencias internas del documento.
  Ánclela al comienzo de línea y compruebe la tabla; en caso de duda, liste las marcas a mano en `marcas_folio`.

Ejemplos:

```json
"formato": {"separador": null, "encabezado": "^#{1,3} ",
            "ignorar": ["(?s)\\A---\\n.*?\\n---\\n", "(?s)<!--.*?-->"]}
```

Markdown: cada título inicia una unidad; el preámbulo YAML y los comentarios no son citables (es el preajuste
`--formato markdown` de `nuevo_expediente.py`).

```json
"formato": {"separador": null, "encabezado": "^\\[?[Ff]olio \\d+", "marca_folio": "^\\[?[Ff]olio (\\d+)\\]?"}
```

Texto corrido en el que cada marca «Folio n» al comienzo de línea inicia una unidad con ese folio.

El expediente piloto (`cc-14-18.json`) no declara `formato`: usa los valores por defecto y cuatro marcas de
folio escritas a mano.
