# `ontologia/` — el perfil OHAC, su tesauro y cómo crece

OHAC no declara ninguna clase ni propiedad. Todo lo propio del dominio es **dato**: un tesauro SKOS y unas formas
SHACL. Por eso añadir un expediente nuevo nunca obliga a tocar el modelo; a lo sumo, a ampliar el vocabulario. Este
documento dice cómo se amplía sin romper lo ya anotado.

## Archivos

| Archivo | Qué es | Se edita |
|---|---|---|
| `ohac.ttl` | Encabezado del perfil: importaciones con versión fijada y alineaciones | a mano |
| `tesauro.ttl` | El tesauro: esquemas y conceptos **aprobados**, con su versión | a mano, salvo las secciones marcadas `>>> … <<<` |
| `candidatos.ttl` | Conceptos **candidatos** (pendientes) y candidatos rechazados | **generado** por `scripts/candidatos.py` desde `datos/candidatos_tesauro.csv` |
| `formas.ttl` | Formas SHACL del perfil | a mano |
| `formas_atributos.ttl` | Dominio y rango de cada atributo | **generado** por `scripts/atributos.py` desde `datos/atributos.csv` |
| `alineaciones.ttl` | Correspondencias con vocabularios externos | generado por `scripts/alineaciones.py` |
| `CHANGELOG.md` | Registro de cambios | a mano, en cada versión |

Las secciones generadas de `tesauro.ttl` son dos: `DEFINICIONES` (`scripts/definiciones.py`) y `APROBADOS`
(`scripts/candidatos.py`). Las pruebas fallan si algo generado no coincide con su CSV.

## Estados de un concepto

| Estado | Dónde está | En RDF | ¿Se puede usar en un registro? |
|---|---|---|---|
| **candidato** | `candidatos.ttl` | `skos:Concept` en su esquema, miembro de `tes:candidatos` | Sí. La validación lo señala con un **aviso** (`sh:Warning`); el grafo conforma |
| **aprobado** | `tesauro.ttl` | `skos:Concept` en su esquema | Sí, sin aviso |
| **retirado** | donde estaba | además, `owl:deprecated true` y, si lo hay, `dct:isReplacedBy` | **No**: es un error en los registros y una violación SHACL |

Un candidato rechazado es un concepto retirado que nunca llegó a aprobarse. Solo se usa vocabulario estándar: SKOS,
DCTERMS (`dct:created`, `dct:source`, `dct:isReplacedBy`, `dct:modified`), OWL (`owl:deprecated`, `owl:versionInfo`)
y PROV (`prov:wasAttributedTo`).

## Regla de oro: una IRI no se borra ni cambia de significado

Los grafos publicados, las reconstrucciones y el trabajo de otros citan las IRI del tesauro. Por eso:

- **Nunca se borra** un concepto. Lo que deja de usarse se **retira**.
- **Nunca se renombra** una IRI. Si el nombre local era malo, se crea un concepto nuevo y el viejo se retira con
  `dct:isReplacedBy` hacia el nuevo.
- **Nunca se reutiliza** una IRI retirada para otra cosa (`scripts/candidatos.py` rechaza un candidato cuyo nombre
  ya existe).
- La **etiqueta** (`skos:prefLabel`) y la **definición** sí pueden corregirse, siempre que el concepto siga
  significando lo mismo. Si cambia lo que significa, es un concepto nuevo.

## Procedimientos

### Proponer un candidato

Quien anota (una persona o un modelo de lenguaje) y encuentra algo que el tesauro no tiene **no lo descarta ni lo
aproxima con una nota**: lo propone y lo usa.

```
python scripts/candidatos.py --proponer cargos pregonero "pregonero" \
    "Oficial que publica los bandos en la plaza." \
    --expediente cc-14-18 --ejemplo "UT07: «por voz de pregonero»" \
    --broader oficial-real --por "anotadora-x (lote d)"
```

Añade una fila a `datos/candidatos_tesauro.csv` y regenera `candidatos.ttl` y `formas_atributos.ttl`. Son
obligatorios el esquema, el nombre local (minúsculas, cifras y guiones), la etiqueta, la **definición**, el
**expediente**, un **ejemplo** literal con su tramo, **quién** lo propone y la **fecha** (por defecto, hoy).
`--broader` es opcional y debe ser un concepto vigente del mismo esquema.

Desde ese momento el concepto está en las listas cerradas de `laad.esquema` y los registros pueden usarlo. Si el
candidato es un **atributo**, conviene añadir su fila a `datos/atributos.csv`; mientras no la tenga, sus
afirmaciones se aceptan con un aviso y no se comprueban su sujeto ni su valor.

La lista de trabajo del curador es `consultas/candidatos_en_uso.rq` (candidatos con el número de nodos que los
usan) y el recuento de avisos que imprime `scripts/construir.py`.

### Aprobar

```
python scripts/candidatos.py --aprobar cargos/pregonero
```

El concepto pasa a la sección `APROBADOS` de `tesauro.ttl`, sale de `tes:candidatos` y deja de producir avisos. Su
IRI no cambia, así que **ningún registro se toca**. Un concepto aprobado no puede colgar (`skos:broader`) de un
candidato pendiente: se aprueba antes el padre. Aprobar es un cambio **MENOR**: hay que subir la versión y anotarlo
en `CHANGELOG.md` (véase «Publicar una versión»).

### Rechazar

```
python scripts/candidatos.py --rechazar cargos/pregonero --reemplazo escribano
```

El concepto se queda en `candidatos.ttl` con `owl:deprecated true` y, si se indica, `dct:isReplacedBy`. Desde ese
momento **usarlo es un error**: `scripts/validar_lote.py` y `scripts/construir.py` fallan y dicen cuál usar en su
lugar. Antes de dar el rechazo por cerrado se corrigen los registros que lo usaban (en los `.py` generadores de
`datos/registros/`). Rechazar un candidato no cambia la versión: nunca formó parte del tesauro.

### Retirar un concepto aprobado

Se añade a mano, en `tesauro.ttl`, junto al concepto:

```turtle
cargo:viejo owl:deprecated true ; dct:isReplacedBy cargo:nuevo ;
    skos:historyNote "Retirado en 0.3.0: se confundía con cargo:nuevo."@es .
```

El concepto conserva su etiqueta, su definición y su esquema. Se corrigen los registros y reconstrucciones que lo
usaban. Retirar es un cambio **MAYOR**.

### Renombrar

No se renombra. Se propone y aprueba el concepto nuevo y se retira el viejo con `dct:isReplacedBy` hacia él (dos
pasos anteriores). Corregir solo la etiqueta no es renombrar: es un **PARCHE**.

### Cambiar el dominio o el rango de un atributo

`datos/atributos.csv` dice, para cada atributo, qué puede ser su sujeto y su valor: `persona`, `grupo`, `lugar`,
`cosa` (clases de mención), `pieza`, `hecho`, `afirmacion`, `concepto` y `literal`. Se comprueba dos veces: al cargar
los registros (`laad.esquema`, `laad.registros`) y en el grafo (`formas_atributos.ttl`). Tras editar el CSV:

```
python scripts/atributos.py
```

**Ampliar** una fila (admitir un tipo más) exige decir por qué en la columna `nota`, con el registro que lo motiva,
y es un cambio MENOR. **Restringirla** invalida registros existentes: es un cambio MAYOR. El grafo no distingue
`grupo` de `cosa` (los dos son `roar:Observation`); esa diferencia solo la comprueban los registros.

## Qué sube cada cifra de la versión

`MAYOR.MENOR.PARCHE`, una sola versión para todo `ontologia/`.

| Cifra | Cuándo | Efecto sobre lo ya anotado |
|---|---|---|
| **MAYOR** | Se retira un concepto aprobado; cambia el significado de uno; se restringe el dominio o el rango de un atributo; se endurece una forma SHACL; se quita o reorganiza un esquema | Registros o grafos válidos pueden dejar de serlo: hay que migrarlos |
| **MENOR** | Se aprueba un candidato; se añade un esquema o un concepto; se amplía el dominio o el rango de un atributo; se añade una forma que lo existente ya cumple | Todo lo anterior sigue siendo válido |
| **PARCHE** | Se corrige una etiqueta, una definición, una nota, un `skos:altLabel` o una alineación sin cambiar el significado | Ninguno |

Proponer o rechazar un candidato **no** cambia la versión. Mientras la versión sea `0.x`, el tesauro es de trabajo y
sus definiciones están pendientes de revisión por historiadores; la primera revisión completa será la `1.0.0`.

## Publicar una versión

1. Cambiar `owl:versionInfo` y `dct:modified` en **todas** las líneas del bloque §0 de `tesauro.ttl` y en `ohac.ttl`.
2. Añadir la entrada al principio de `CHANGELOG.md` (Añadido / Cambiado / Retirado), con las IRI afectadas.
3. Regenerar y comprobar:

```
python scripts/candidatos.py        # candidatos.ttl, sección APROBADOS y formas_atributos.ttl
python scripts/construir.py         # debe imprimir «SHACL conforma: True» y el número de avisos
python -m pytest -q
```

Las pruebas comprueban que la versión de todos los esquemas es la misma y la de la última entrada del registro
(`tests/test_tesauro_version.py`), que lo generado coincide con los CSV, que todo candidato está documentado y que
nada usa un concepto retirado (`tests/test_candidatos.py`), y que cada forma detecta su violación
(`tests/test_formas_negativas.py`).
