# Prueba de escala del almacén de consulta (Oxigraph)

Medición hecha el 2026-11-14 con `pyoxigraph` 0.5.13. No es un resultado sobre el archivo real: es el grafo del
expediente piloto **replicado**. Sirve para saber cómo crecen la carga, la memoria y las consultas con el número
de expedientes, no para afirmar cuánto tardará el corpus definitivo.

## Método

- **Datos.** El grafo de `cc-14-18` (28 654 cuádruplas en `cc-14-18.nq` más 2 384 en `comun.nq`) se replica
  N − 1 veces sustituyendo el identificador del expediente por `zz-0001`, `zz-0002`, … en los N-Quads. Cada
  réplica recibe también una copia de las capas comunes (reconstrucciones, argumentación y procedencia) con IRIs
  propias para las entidades de la capa 4, de modo que son N expedientes independientes de igual tamaño y forma.
  El catálogo y el tesauro se cargan una sola vez. El expediente original se conserva y es el que se consulta.
- **Almacén.** Como en `laad.consulta`: cada tripleta se guarda en su grafo nombrado y, además, en el grafo por
  defecto (la unión). Por eso el número de cuádruplas almacenadas es aproximadamente el doble del de tripletas.
  - *En memoria*: carga transaccional de los N-Quads y unión con una actualización SPARQL
    (`laad.consulta._unir`), igual que el motor por defecto.
  - *En disco*: almacén persistente con la carga por lotes de Oxigraph (20 expedientes por llamada); la unión
    se carga como N-Triples (cada N-Quad sin su grafo) y al final se compacta el almacén. Es el procedimiento
    de `laad.consulta.nuevo_almacen(masivo=True)` y de `scripts/servir.py --volcar`.
- **Consultas.** Tres consultas con nombre de `consultas/`, tal como estaban ese día, sobre el expediente original:
  `piezas(expediente)`, `afirmaciones(expediente, filtroEntidad, atributo)` (la forma habitual de una pregunta
  de competencia) y `afirmaciones(expediente)` (las 505 afirmaciones con todas sus facetas); y `disputas()`, que
  recorre el corpus entero. Además, una **variante** de `piezas` que no es la consulta con nombre: la misma
  restricción al expediente escrita como patrón de tripletas en lugar de
  `FILTER (!BOUND(?expediente) || EXISTS { … })`.
- **Medida.** Mediana de tres ejecuciones (una sola si pasa de 20 s). Límite por consulta: 120 s; en disco,
  además, 3 GB de memoria por consulta. Memoria: máximo de memoria residente del proceso (incluye el intérprete
  de Python y las bibliotecas, unos 60 MB). El guion de la medición es desechable y no forma parte del
  repositorio.

## Resultados

| N expedientes | Almacén | Cuádruplas almacenadas | Carga | Memoria máx. (carga) | En disco |
|---:|---|---:|---:|---:|---:|
| 1 | memoria | 64 617 | 0,13 s | 81 MB | — |
| 10 | memoria | 605 148 | 1,3 s | 322 MB | — |
| 100 | memoria | 6 010 458 | 15,5 s | 2,6 GB | — |
| 100 | disco | 6 010 458 | 26 s | 1,1 GB | 1,4 GB |
| 1 000 | disco | 60 063 558 | 446 s | 1,4 GB | 8,2 GB |

Con 1 000 expedientes no se intentó el almacén en memoria: extrapolando, necesitaría unos 26 GB.

| N | Almacén | `piezas (expediente)` | variante de `piezas` con patrón | `afirmaciones (expediente, filtroEntidad, atributo)` | `afirmaciones (expediente)` | `disputas ()` |
|---:|---|---:|---:|---:|---:|---:|
| 1 | memoria | 0,002 s | 0,001 s | 0,026 s | 0,081 s | 0,35 s |
| 10 | memoria | 0,040 s | 0,001 s | 0,28 s | 3,5 s | 31 s |
| 100 | memoria | 3,7 s | 0,005 s | 3,4 s | > 120 s | no ejecutada |
| 100 | disco | 5,0 s | 0,014 s | 23 s | > 120 s | no ejecutada |
| 1 000 | disco | supera el límite | 0,21 s | supera el límite | no ejecutada | no ejecutada |

«Supera el límite»: más de 120 s o más de 3 GB de memoria. «No ejecutada»: una consulta más ligera ya había
superado el límite con ese tamaño.

## Tras reescribir las consultas (2026-11-14)

Las consultas con nombre se reescribieron después de la medición anterior (`consultas/*.rq`, mecanismo en
`laad.consulta`):

- **El parámetro opcional ya no es un filtro.** `FILTER (!BOUND(?expediente) || EXISTS { … })` se sustituye por
  bloques `#SI expediente … #FIN` que solo forman parte de la consulta cuando llega el parámetro; con él, la
  consulta parte del expediente (expediente → transcripción → tramos → piezas) por índice.
- **El orden de evaluación está escrito en la consulta.** Cada paso es un `LATERAL { … }` que parte de un nodo ya
  ligado, y cada faceta opcional un `LATERAL { OPTIONAL { … } }`. Sin eso el optimizador de Oxigraph, que no tiene
  estadísticas, resuelve cada `OPTIONAL` y cada `EXISTS` de dos tripletas recorriendo el corpus. `LATERAL` no es
  SPARQL 1.1: para rdflib, `laad.consulta.sin_lateral` lo reescribe con `OPTIONAL` + `BOUND`.
- **Sin subconsultas sobre el corpus entero.** `afirmaciones` agrega sus listas en un `GROUP BY` final;
  `disputas` recorre las afirmaciones una vez y busca por índice las de la misma entidad y atributo, en vez de
  combinar dos subconsultas del corpus.

Método: el mismo (réplicas del piloto, almacén en memoria, mediana de tres ejecuciones; una sola si pasa de 5 s),
con el grafo de hoy, que es algo mayor que el de la primera medición (70 321 cuádruplas almacenadas con un
expediente, frente a 64 617; 505 filas de `afirmaciones`, 118 reconstrucciones). Por eso se repitieron también
las consultas **anteriores** sobre las mismas réplicas, con 1 y 10 expedientes. Las filas devueltas por las
consultas nuevas y las anteriores sobre el piloto son las mismas (salvo el orden de las filas que empatan en el
`ORDER BY`).

| Consulta (sobre el expediente original) | N = 1 antes | N = 1 ahora | N = 10 antes | N = 10 ahora | N = 100 ahora |
|---|---:|---:|---:|---:|---:|
| `piezas (expediente)` | 0,001 s | 0,001 s | 0,038 s | 0,001 s | 0,001 s |
| `afirmaciones (expediente, filtroEntidad, atributo)` | 0,030 s | 0,014 s | 0,27 s | 0,024 s | 0,029 s |
| `afirmaciones (expediente)` | 0,085 s | 0,13 s | 3,5 s | 0,16 s | 0,15 s |
| `participantes (expediente)` | 0,007 s | 0,004 s | 0,25 s | 0,006 s | 0,005 s |
| `control_secuencia (expediente)` | 0,002 s | 0,007 s | 0,037 s | 0,008 s | 0,008 s |
| `menciones_de (expediente, filtroEntidad)` | 0,003 s | 0,002 s | 0,013 s | 0,002 s | 0,002 s |
| `reconstrucciones ()` — todo el corpus | 0,12 s | 0,004 s | 11,8 s | 0,048 s | 1,2 s |
| `disputas ()` — todo el corpus | 1,1 s | 0,17 s | > 90 s (interrumpida) | 1,7 s | 29 s |

Carga en memoria de estas réplicas: 0,15 s y 88 MB (N = 1), 1,5 s y 343 MB (N = 10), 15,8 s y 2,8 GB (N = 100;
6 558 880 cuádruplas almacenadas).

Qué dice la tabla:

- **Las consultas restringidas a un expediente ya no dependen del tamaño del corpus**: entre 1 y 100 expedientes
  el tiempo no cambia (`afirmaciones (expediente)`: 0,13–0,16 s; en la primera medición superaba 120 s con 100).
  Con un solo expediente dos de ellas son algo más lentas que antes (`afirmaciones (expediente)`,
  `control_secuencia`): el recorrido paso a paso cuesta más que una combinación en bloque cuando el corpus es un
  expediente.
- **Lo que sigue sin escalar son las consultas sobre el corpus entero.** `disputas ()` ya no es cuadrática, pero
  crece con el corpus (×10 y ×17 en tiempo por cada ×10 en datos): 29 s con 100 expedientes y, por extrapolación,
  varios minutos con 1 000. Compara cada afirmación con las demás de su entidad y atributo y no tiene parámetro de
  expediente ni de entidad que la acote. `reconstrucciones ()` también crece más que los datos (×12 y ×25): no es
  interactiva más allá de unos cientos de expedientes. Las demás consultas sin parámetros (`afirmaciones ()`,
  `piezas ()`, `participantes ()`, `control_secuencia ()`, `cargos ()`) devuelven filas de todo el corpus y
  tardan al menos en proporción; solo se probaron con 1, 10 y 40 expedientes mientras se reescribían, sin
  medición sistemática. Para un corpus grande harán falta parámetros (entidad, atributo, expediente) o resultados
  precalculados.
- `afirmaciones (expediente, filtroEntidad, atributo)` crece un poco (0,014 → 0,029 s): su primer paso —elegir las
  afirmaciones a partir de varios parámetros a la vez— se deja al optimizador.

**Sin medir en esta segunda ronda:** el almacén en disco (100 y 1 000 expedientes) y cualquier tamaño por encima
de 100; las consultas anteriores con 100 expedientes (se conservan las cifras de la primera medición, arriba, con
un grafo algo menor); el motor rdflib sobre réplicas (solo se comprobó, sobre el piloto, que devuelve
las mismas filas que Oxigraph: `tests/test_motores.py`). Que el tiempo de las consultas por expediente sea plano
hasta 100 en memoria hace esperable lo mismo en disco, pero no está comprobado. Una sola medición por tamaño.

## Lectura (de la primera medición)

1. **La carga y el espacio crecen linealmente** con el número de expedientes: unos 26 MB de memoria, o unos
   8–14 MB de disco, por expediente del tamaño del piloto. Un corpus de 1 000 expedientes como el piloto
   (30 millones de tripletas) cabe en un almacén en disco de menos de 10 GB y se carga en minutos; en memoria
   deja de ser razonable entre 100 y 1 000 expedientes.
2. **El almacén responde por índice sin depender del tamaño del corpus** cuando la restricción al expediente es
   un patrón de tripletas: la variante de `piezas` pasa de 1 ms a 0,2 s entre 1 y 1 000 expedientes.
3. **Las consultas con nombre, tal como están escritas, no escalan.** `piezas(expediente)` crece de forma
   aproximadamente cuadrática (×25 y ×93 en tiempo por cada ×10 en datos) porque la restricción al expediente es un
   `FILTER … EXISTS` con una ruta de propiedades que se evalúa después de recorrer las piezas de todo el
   corpus. `afirmaciones` añade subconsultas con `GROUP BY` que se calculan para el corpus entero antes de
   filtrar, y `disputas` hace una autocombinación de todas las afirmaciones (0,35 s → 31 s entre 1 y 10
   expedientes). Con un expediente la diferencia no se nota; con cien, sí.
4. Por tanto, la cifra que podía darse antes de reescribir las consultas era: **carga y almacenamiento comprobados hasta 1 000 expedientes
   sintéticos (60 millones de cuádruplas); consultas con nombre interactivas hasta unas decenas de
   expedientes.** Para llegar más lejos hay que reescribir las consultas (restricción al expediente como patrón,
   subconsultas correlacionadas con el expediente), no cambiar de almacén.
5. **Después de la reescritura** (sección anterior): carga y almacenamiento, lo mismo; consultas con nombre
   restringidas a un expediente, de tiempo constante comprobado hasta 100 expedientes sintéticos en memoria;
   consultas sobre el corpus entero, crecientes con su tamaño (`disputas ()`: 29 s con 100 expedientes).

## Cautelas

- Las réplicas son copias: mismo vocabulario, mismas longitudes de texto, misma proporción de afirmaciones por
  pieza. Los expedientes reales varían mucho en extensión y un archivo real comparte personas, lugares y cargos
  entre expedientes (capa 4), lo que aquí no ocurre. Las cifras son un orden de magnitud.
- Los tiempos absolutos dependen del equipo (aquí, un único equipo de escritorio, sin otros clientes); lo que se
  puede trasladar son las **proporciones** entre tamaños y entre formas de escribir la consulta.
- La carga en disco y la carga en memoria no usan el mismo procedimiento para la unión (texto frente a
  actualización SPARQL): sus tiempos no son comparables entre sí como medida del almacén.
- No se midió la construcción del grafo (rdflib, validación SHACL) ni el razonador OWL RL, que siguen siendo
  por expediente y bastante más lentos que la consulta.
- Una sola medición por tamaño; no hay intervalos de confianza.
