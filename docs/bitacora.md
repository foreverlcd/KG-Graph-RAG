# Bitácora de trabajo

> Registro cronológico de hechos, incidencias y correcciones, para la reproducibilidad y para el futuro artículo.
> Fecha de todas las entradas: 2026-11-12. La rama git indica dónde quedó cada cambio.

## Organización del trabajo

* **Ramas.** Cada entregable se integra en `main` con merge `--no-ff`:
  * `fuente/indice` (capa 0);
  * `docs/preguntas-competencia` (B);
  * `docs/diagnostico` (A);
  * `ontologia/modelo` (C, D, E y datos);
  * `docs/documentacion` (C–G, bitácora e índice).
* **Subagentes.** Las tareas acotadas se delegaron y sus resultados se comprobaron por muestreo:
  1. Auditoría del intento previo.
  2. Descarga y verificación de especificaciones en `vendor/`.
  3. Precedentes y literatura.
  4. Búsqueda de skills: ninguna adecuada; se adoptó a mano el patrón «PC como prueba SPARQL + matriz de trazabilidad».
  5. Pruebas negativas SHACL, términos y mapeo.
  6. Revisión independiente del modelo, sin acceso a `docs/` para no anclarse en la justificación del autor.

## Hallazgos sobre los materiales

1. **El «intento 2» no existe** en disco ni en git; el marcador `[Pegar aquí…]` de la solicitud llegó vacío. El «intento 1» es el proyecto hermano `../Grafo-Conocimiento-Cusco`.
2. **La transcripción no marca recto ni vuelto** y solo tiene 4 marcas de folio explícitas (20, 28, 33 y 34). El catálogo dice 19 folios (K3). Unidad adoptada: el tramo.
3. **El corpus modernizado resuelve variantes sin avisar:** 1809 → 1805, Mara → Mata, Guancachoque → Huancachoque. Queda excluido de la capa 2.
4. **El final de UT20 es un documento republicano ajeno** (notario Ugarte). Se modela como pieza P32 marcada como ajena.

## Incidencias técnicas y correcciones (en orden)

| # | Incidencia | Causa | Corrección | Prueba que la fija |
|---|---|---|---|---|
| 1 | `fetch_vendor.sh` y `fuentes.sha256` «restaurados por un proceso externo» (lo informó el subagente de estándares) | Los `git add -A` del modelador al cambiar de rama capturaron versiones intermedias de archivos que el subagente estaba escribiendo | El subagente regeneró los archivos; `fetch_vendor.sh --check` da 49/49 OK. **Lección:** no hacer `git add -A` mientras un subagente escribe en el árbol; añadir rutas explícitas | — |
| 2 | Ids `M-UT12.a-001` rechazados | La regex de ids no admitía minúsculas | Patrón `[A-Za-z0-9.]` | `tests/test_mapeo.py` |
| 3 | pyshacl: «A SPARQL Constraint must not contain a VALUES clause» | Restricción de SHACL-SPARQL | Una restricción por esquema (polaridad, fundamento, fuerza) | `test_formas_negativas` |
| 4 | Validación SHACL de 6 min 49 s | Inferencia RDFS completa sobre RiC-O, CRM y otros | Grafo ontológico reducido a `rdfs:subClassOf` (lo que necesita `sh:class`); ahora ≈ 9 s | — |
| 5 | **La forma de procedencia aprobaba en vacío** | La IRI escapada `id:capa\/texto` dentro de SPARQL no casaba con nada en rdflib | IRIs completas; pruebas negativas por forma | `test_formas_negativas::lote-*` |
| 6 | **`ActuacionForma` aprobaba en vacío** si faltaba la fuerza (lo detectó la prueba negativa del subagente) | `COUNT … GROUP BY` sin `OPTIONAL`: con cero coincidencias no hay fila | Patrón `OPTIONAL` + `!BOUND(?n)` | `test_formas_negativas::actuacion-sin-fuerza` |
| 7 | **Razonador: 1 inconsistencia real** (defecto D1) | ROAR declara `prov:wasDerivedFrom rdfs:domain roar:Reconstruction`. Como `prov:hadPrimarySource ⊑ prov:wasDerivedFrom` y `roar:Observation ⊓ roar:Reconstruction = ∅`, una observación de lugar que cita su fuente con PROV es contradictoria | Las observaciones ROAR usan `roar:documentedIn`; el razonador informa además de las 50 tipificaciones espurias que el axioma sigue produciendo en observaciones PiCo | `scripts/razonar.py`, `datos/grafo/razonador.txt` |
| 8 | IRIs de roles PiCo divergentes | `pico.ttl` usa `picot_roles: …/roles/`; los conceptos publicados usan `…/ThesaurusHistorischePersoonsgegevens/NNN` | Se alinea con la IRI del concepto publicado; anotado en `ohac.ttl` (defecto D2) | `test_terminos_existen` |
| 9 | Consultas que devolvían afirmaciones sobre otras personas | `initBindings` sobre una variable dentro de `OPTIONAL` no filtra | Parámetros como bloque `VALUES` con IRIs validadas | `test_preguntas_competencia::pc09` |
| 10 | `disputas.rq`: 144 s y casos de piezas perdidos; tras reescribirla, 0 filas | (a) autounión anidada; (b) un `FILTER` dentro de un grupo de `UNION` solo ve las variables de ese grupo | Subconsultas que normalizan (entidad, atributo, clave de valor, polaridad) y `BIND(IF(…))` fuera de la unión: 1,7 s | `test_pc10`, `test_pc11`, `test_pc14` |
| 11 | La reconstrucción no aparecía en PC09 | En rdflib, `URIRef == str` devuelve False | `str(entidad)` | `test_pc09` |
| 12 | Avisos de obsolescencia de rdflib (1,5 M) que alargaban las pruebas | `Dataset.default_context` | Filtro en `pytest.ini` | — |
| 13 | OOPS!: «unexpected error» | El servicio intenta resolver los `owl:imports` nominales | Envío sin importaciones; resultado P34 como artefacto (docs/G §2) | `datos/evaluacion/oops_respuesta.xml` |
| 14 | Detalles de la literatura sin verificar | El resumen de Montenegro et al. (2026) no menciona RML ni los porcentajes de dominio–rango que da el informe del subagente | En D y G se separa lo verificado por el modelador (resumen) de lo verificado solo por el subagente (cuerpo del artículo) | — |
| 15 | Umbral de Krippendorff atribuido a un anexo que no lo contiene | Error del modelador | Corregido en G §4; queda pendiente añadir la referencia de Krippendorff (2004) | — |

## Decisiones tomadas durante la anotación del hilo central

* **Sujeto elíptico.** La declaración de Cano (P18) no nombra a Chuquitapa. El sujeto se resuelve a la mención de la certificación P01, se marca `anot:sujeto-eliptico` y se justifica en una nota.
* **Hechos narrados por pieza** (`H-p01-alboroto`…). La correferencia entre relatos es una reconstrucción (R-alboroto-carcel); de lo contrario, el extractor estaría decidiendo una identidad de evento.
* **Afirmaciones colectivas.** «Los Documentos que presentó…» se distribuye a cada certificación P01, P03, P04 y P05, con la misma cita. P02 se excluye y queda anotado.
* **Afirmante sin nombre.** El informe del cura (P23) no lleva firma en la transcripción. El afirmante es la mención «parroco interino» del oficio P22, y la nota remite a P27, donde Mata lo nombra.
* **Firma frente a negación de la firma.** La firma visible es capa 2 (mención con rol firmante); la negación de haber firmado es capa 3. La disputa entre ambas se calcula con `disputas_firma.rq`.
* **Segundo expediente** sorteado antes de leer su ficha: CO Cusco Leg. 70 Exp. 15 (semilla 18061806).
