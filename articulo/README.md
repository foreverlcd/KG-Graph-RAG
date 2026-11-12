# Artículo: perfil OHAC (solo ontología)

Borrador en castellano, plantilla LLNCS (Springer), pensado para traducirse al inglés si se envía a ESWC 2027
Resources Track (ver `docs/anexos/H3_metodologia_y_publicacion.md` §3).

Compilar: `latexmk -pdf main.tex` (BibTeX con `splncs04`). Limpiar: `latexmk -C`.

## Pendientes marcados en rojo en el PDF (`\pendiente{}`)

1. Licencia de datos y código (sugerencia: CC BY 4.0 para tesauro, formas y grafo; MIT o Apache-2.0 para el código).
2. Repositorio público y DOI de Zenodo (cita canónica = concept DOI).
3. Registro del espacio de nombres `https://w3id.org/laad/` (pull request a perma-id/w3id.org).
4. Declaración de uso de IA generativa, redactada por los autores.

## Revisión independiente (2026-11-12)

Un revisor sin acceso a `docs/` contrastó el borrador con el repositorio. Se atendió todo lo que no depende de los
autores: formas de respuesta calculadas (ADR-027), SHACL de relaciones de discurso (ADR-028), catálogo de
importaciones (ADR-029), D6 matizado y D7 nuevo (ADR-026), cifras corregidas (58 grafos, 23 tramos, 34 mutaciones,
95 conceptos sin definición), autoría de la capa 4 declarada, tabla comparativa, convención J4 → grafo nombrado y
limitaciones n=1. Se retiró la fila de OOPS! (poco informativa en un perfil sin clases propias; el resultado sigue en
`datos/evaluacion/oops_respuesta.xml`). FOOPS! requiere publicar el perfil en una URL: pendiente con el punto 2.

## Antes de enviar

* Ninguna cifra del texto se escribe a mano sin fuente: todas salen de `datos/grafo/razonador.txt`, de las pruebas
  (`pytest`) o de `docs/G_evaluacion.md`. Si se reconstruye el grafo, revisar §5–6 y la tabla de resultados.
* `referencias.bib`: entradas comprobadas contra doi.org o la página oficial; sin comprobar a fondo: `gruninger1995`
  (sin DOI) y autores/editores de las especificaciones W3C y CIDOC (`crminf121`, `crmtex2`, `provo`, `skos`,
  `shacl`, `webannotation`, `rdf12`, `noy2006nary`, `andrews2023star`).
