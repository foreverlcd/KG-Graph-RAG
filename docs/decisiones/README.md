# Registro de decisiones de diseño (ADR resumidos)

> Formato: contexto → decisión → consecuencias. Las más extensas están argumentadas en `docs/C_modelo.md`.

| ADR | Decisión | Contexto | Consecuencias | Dónde |
|---|---|---|---|---|
| 001 | **La unidad citable es el tramo**, no el folio | La transcripción no marca recto ni vuelto y solo tiene 4 marcas de folio; las imágenes no están disponibles | La cita se verifica al 100 % contra el tramo; el folio se coteja después con las imágenes | `docs/01_materiales.md` §2–3, `src/laad/fuente.py` |
| 002 | **Única normalización de citas: colapsar espacios** | La transcripción parte frases entre líneas; plegar grafías borraría la evidencia | «Huancachoque» en lugar de «Guancachoque» se rechaza (prueba) | `fuente.verificar_cita` |
| 003 | **El corpus modernizado no alimenta el grafo** | Resuelve variantes en silencio (1809 → 1805, Mara → Mata) | Solo sirve para la lectura humana | `docs/01_materiales.md` §4.3 |
| 004 | **Cuatro capas como grafos nombrados**, más la de procedencia y la de argumentación | Separar lo que es papel, texto, afirmación y reconstrucción | Las pruebas de capas comprueban qué tipo de nodo vive en qué grafo | `docs/C_modelo.md` §2 |
| 005 | **Patrón STAR sobre E13** para toda afirmación, incluidas las resoluciones | Las resoluciones no son hechos | Sin valores de verdad en las capas 1–3; la fuerza institucional va como tipo | §3.3–3.4 |
| 006 | **Facetas de la actuación por `P9i`**: ante quién, quién escribe, quién firma, fecha | Evitar propiedades propias | La faceta se infiere de la actuación; «no consta» si la fuente calla | §3.3 |
| 007 | **Menciones sin fusión y sin afirmar existencia** (PiCo/ROAR, no E21) | «No hay tal hombre en el pueblo de Tinta» | Las identidades son reconstrucciones con creencia; las hipótesis pueden competir | §3.2, revisión I3 |
| 008 | **Lo andino y lo procesal en SKOS** | Encargo; generalidad | Ampliar el vocabulario no cambia el núcleo | §4 |
| 009 | **OHAC no declara términos** | Análisis de carencias | OHAC es un perfil: tesauro, formas, alineaciones e importaciones | §6 |
| 010 | **RDF nativo**, con vista de grafo de propiedades generada | Uso real de los estándares, SHACL, grafos nombrados | Consultas más verbosas | §9 |
| 011 | **El LLM llena un esquema plano y cerrado**; el mapeo es determinista | Literatura 2024–2026; fallos 2.1, 2.3 y 2.4 del intento previo | El LLM no decide identidad, verdad, folio ni tipo de actuación | `docs/D_extraccion_consulta.md` |
| 012 | **El tipo de actuación de cada pieza se cura a mano** | Fallo 2.4 (subcadenas) | `datos/piezas.jsonl` es una entrada humana | §3.1 |
| 013 | **Las disputas se calculan, no se almacenan** | Fallo 1.2: `CONTRADICE` tenía 0 instancias | `consultas/disputas.rq`, `disputas_firma.rq`; `responde_a` explícito | `docs/E_prueba_hilo_central.md` |
| 014 | **Hechos narrados por pieza (E89)**; la correferencia de eventos va a la capa 4 | No decidir identidades de evento en la extracción | Comparar relatos exige una reconstrucción de evento | L7 |
| 015 | **Las observaciones ROAR usan `roar:documentedIn`**, no `prov:hadPrimarySource` | Defecto D1 hallado por el razonador | Consistencia OWL RL; se informan las inferencias espurias | §7 |
| 016 | **Argumentación CRMinf en un grafo propio** | La creencia no debe formar parte de la proposición evaluada | Dos grafos por reconstrucción | revisión I4 |
| 017 | **Manifiesto por expediente**, con el expediente como variable de contexto | Revisión C2 | El segundo expediente entra sin tocar el código | `datos/expedientes/` |
| 018 | **El cargo es un E7 con el cargo como rol (P14.1)** y vigencia E52 | Revisión C1 | La vigencia atestiguada se separa de la desconocida (nota) | §3.5 |
| 019 | **Segundo expediente sorteado a ciegas con semilla fija** antes de leer su ficha | Criterio 5 | CO Cusco L70 E15 | `docs/G_evaluacion.md` §5 |
| 020 | **Revisión independiente sin acceso a la documentación** | Evitar el anclaje en la justificación del autor | 3 críticos y 8 importantes, atendidos o documentados | §10 |
