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
- **Consultas.** Tres consultas con nombre de `consultas/`, tal como están, sobre el expediente original:
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

## Lectura

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
4. Por tanto, la cifra que puede darse hoy es: **carga y almacenamiento comprobados hasta 1 000 expedientes
   sintéticos (60 millones de cuádruplas); consultas con nombre interactivas hasta unas decenas de
   expedientes.** Para llegar más lejos hay que reescribir las consultas (restricción al expediente como patrón,
   subconsultas correlacionadas con el expediente), no cambiar de almacén.

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
