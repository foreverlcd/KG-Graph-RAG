# Guion de la charla de avances (unos 10 minutos)

Diapositivas: `avances.pdf` (12 páginas). Respaldo con todo el detalle, por si preguntan: `proyecto.pdf`.
Las cifras citadas aquí son las del grafo al 25-11-2026 (`docs/cifras.md`).

## 0. Antes de empezar: qué es el proyecto y cómo nombrarlo

Hemos usado varios nombres y conviene no mezclarlos en la charla:

| Nombre | Qué es | Cómo usarlo |
|---|---|---|
| **LAAD** | El laboratorio | «Laboratorio LAAD». No es el nombre del proyecto |
| **OHAC** | La ontología (técnicamente, un *perfil de aplicación*): cuatro capas, tesauro y reglas | «la ontología OHAC». Es lo que presenta el artículo |
| **El grafo** | Los datos: el expediente piloto representado con OHAC | «el grafo del expediente de Tinta» |
| **KG-Graph-RAG** | El nombre del repositorio en GitHub | Solo describe una parte (ver abajo) |

**El proyecto, en una frase:** construimos un grafo de conocimiento de expedientes judiciales coloniales del Fondo
Intendencia, con una ontología (OHAC) que guarda quién afirmó qué, y lo usamos para responder preguntas citando el
expediente.

**¿Y lo de «Graph RAG»?** RAG es que un modelo de lenguaje responda apoyándose en datos que recupera. Nuestro agente de
consulta hace eso sobre el grafo, así que el nombre del repositorio no es falso. Pero describe solo la tercera pieza (el
uso), no la principal (la ontología y el grafo). Para la charla, mejor no usarlo.

**Pendiente de decidir:** la sigla OHAC no está desarrollada en ningún documento del repositorio. Si alguien pregunta
qué significa, hay que tener la respuesta decidida. Si no está decidida, decir: «es el nombre del perfil; su sigla la
estamos fijando».

## 1. Guion por diapositiva

**1. Título (10 s).** Presentarse y decir el tema: la ontología, el tesauro y cómo va el grafo.

**2. Qué estamos construyendo (1 min).**
- Tres piezas: la ontología (cómo se representa), el grafo (el expediente de Tinta representado así) y su uso.
- La idea central: un expediente no registra hechos, registra voces. Nuestro grafo guarda quién afirmó qué, ante quién y
  con qué fuerza, y calcula dónde chocan las voces. No decide quién tiene razón.
- Ellos conocen el expediente: no contar el caso, solo recordarlo con el ejemplo de Cano.

**3. Cuatro capas (1 min 30 s). La diapositiva más importante.** Recorrer la tabla de arriba abajo:
- **Documento:** el papel, es decir, piezas y actuaciones.
- **Mención:** el nombre tal como está escrito, sin corregirlo ni unirlo a otro.
- **Afirmación:** quién dijo qué de quién.
- **Reconstrucción:** lo que propone un investigador, con su grado de creencia.
- Tres reglas que conviene recordar:
  - las capas no se mezclan;
  - en las capas 1 a 3 no hay verdadero ni falso;
  - solo la capa 4 tiene creencias, y siempre con autor.

**4. Un ejemplo que atraviesa las capas (1 min 30 s).** Señalar de abajo arriba:
- La pieza P18 (declaración jurada).
- Las menciones «Isidro Cano» y «Andres Chuquitapa».
- La afirmación A-UT11-004: Cano **niega** que Chuquitapa fuera coronel, y responde a lo que él mismo afirmó en agosto.
- Arriba, las personas reconstruidas: Chuquitapa reúne 45 grafías.
- Cierre: «el grafo no dice si fue coronel; dice quién lo afirmó y quién lo negó, y de ahí calcula la disputa».

**5. La afirmación por dentro (1 min).**
- Cada afirmación guarda nueve cosas. Destacar tres: la polaridad (afirma o niega), el fundamento (de vista, de oídas) y
  la cita exacta.
- La fuerza no la decide nadie: sale del tipo de actuación.
- La frase clave: un auto obliga en el proceso, pero no hace verdadero lo resuelto ni implica que se cumpliera.

**6. Identidades (1 min).**
- Las grafías nunca se fusionan. Decir que son la misma persona es una hipótesis con autor, premisas, argumento y
  creencia.
- Ejemplo de Casorla: dos hipótesis rivales, y el grafo guarda las dos.
- Decirlo con honestidad: las 118 reconstrucciones las propuso un modelo de lenguaje y nadie las ha validado.

**7. El tesauro (1 min 30 s). Aquí ellos pueden aportar más.**
- Lo andino y lo procesal van como vocabulario, no como estructura: si mañana aparece un cargo nuevo, se añade un
  concepto y nada se rompe.
- Mencionar las decisiones discutibles y preguntarles qué opinan:
  - «India Ordinaria» se guarda como *ordinario*, no como originaria;
  - el ayllu es un grupo, no un lugar;
  - «Gobernador» lleva una nota de referente dudoso.
- Cómo crece: lo nuevo entra como candidato (hoy 26) y un curador decide. Hay 22 definiciones «de trabajo» sin fuente.

**8. Estándares y cero términos propios (1 min).**
- OHAC no inventa clases ni propiedades: usa estándares reconocidos (archivos, museos, W3C). Lo local va al tesauro.
- Por qué: cualquiera que conozca esos estándares puede leer el grafo, y el trabajo no queda huérfano.
- 50 reglas lo hacen cumplir. Mencionar el hallazgo de la presunción de sinceridad: interesa a historiadores.

**9. Cómo se construye (1 min).**
- El modelo de lenguaje llena fichas con cita obligatoria; el código valida y convierte; una persona cura las piezas.
- El modelo propone, nunca decide.
- La validación se hace sin modelo: 1 049 citas exactas, 0 violaciones, 20/20 preguntas.

**10. Qué hacemos con el grafo (1 min).**
- Las consultas, las disputas calculadas y el visor (se puede mostrar en vivo, ver la sección 4).
- El agente, en una frase: responde usando solo el grafo, no inventa citas en 18,5 de 20 respuestas y es completo en lo
  esencial en 11.

**11. Estado y ayuda (1 min).**
- Lo hecho y los límites, sin adornos.
- Pedir ayuda concreta: los cinco puntos de la diapositiva.

**12. Cierre.** «El grafo guarda quién afirmó qué; no decide quién tiene razón.»

## 2. Lo que hay que saber explicar, en palabras simples

- **Ontología:** el modelo de cómo se describe algo (qué tipos de cosas hay y cómo se relacionan). **Grafo:** los datos
  concretos descritos con ese modelo. **Tesauro:** la lista controlada de palabras (cargos, roles, tipos de acto) que
  usan los datos.
- **RDF y tripleta:** cada dato es una frase de tres partes, sujeto, relación y objeto. Por ejemplo: «A-UT11-004 —
  polaridad — niega».
- **Grafo nombrado:** un compartimento del grafo. Cada capa va en el suyo, por eso no se mezclan.
- **Mención frente a persona:** la mención es el nombre escrito en un lugar del texto. La persona es una hipótesis que
  reúne menciones. Esto importa porque el juez dice de un certificante «no hay tal hombre»: si la mención fuera una
  persona, el grafo afirmaría que existió.
- **E13 (CIDOC CRM):** la forma estándar de decir «alguien atribuyó a algo un valor». Es justo una afirmación.
- **Fuerza institucional:** el peso procesal de la voz (testimonial, resolutiva…). Sale del tipo de actuación.
- **Creencia (CRMinf):** cuánto cree quien propone una reconstrucción que es cierta. Solo existe en la capa 4.
- **SHACL:** reglas que el grafo debe cumplir. Se comprueban solas; si alguien rompe el modelo, salta un error.
- **Perfil sin términos propios:** no inventamos vocabulario técnico. Combinamos estándares y ponemos lo local en el
  tesauro.
- **Disputa calculada:** no se guarda «esto contradice aquello»; la consulta lo detecta cuando una misma cosa se afirma y
  se niega, o recibe valores incompatibles.
- **El papel del modelo de lenguaje:**
  - al construir, propone fichas y el código las valida;
  - al consultar, el agente pone a prueba lo que se puede hacer con el grafo.
  - La calidad del grafo se valida sin modelos.

## 3. Preguntas probables

- **¿Por qué no deciden qué es verdad?** Porque el expediente no lo decide: son voces con distinta fuerza. Si guardáramos
  «verdades», guardaríamos la versión de la autoridad. Lo que sí hacemos es decir dónde hay desacuerdo y qué no consta.
- **¿Quién validó las anotaciones?** Nadie todavía, aparte de controles automáticos y algunas decisiones nuestras. Por eso
  pedimos su ayuda. El grafo lo declara: para cada dato dice qué proceso lo produjo y que no hay validación humana.
- **¿Un modelo de lenguaje anotó el expediente? ¿No inventa?** Propone fichas. Una cita que no sea copia exacta del texto
  invalida la ficha entera, y el modelo nunca decide identidades, folios ni tipos de acto. Todas las citas del grafo
  están comprobadas: 1 049 de 1 049.
- **¿Por qué no usar Neo4j, como el primer intento?** El problema no fue la herramienta, sino que nada obligaba a usar
  estándares ni a validar. El primer intento atribuyó la frase del fiscal a ocho declarantes. Con RDF y SHACL eso no
  pasa. El visor da la misma vista que daría Neo4j.
- **¿Sirve para otros expedientes?** Sí: cada expediente se declara en un archivo de configuración, sin tocar código. Lo
  probamos con un pleito civil de prueba, que no necesitó términos nuevos. Falta la transcripción del segundo expediente
  real.
- **¿Qué es OHAC?** La ontología del proyecto. Técnicamente es un perfil: combina estándares, un tesauro y reglas, sin
  vocabulario propio. Sobre la sigla, ver la sección 0.
- **¿Qué pasa con el folio?** Sin imágenes no podemos saber folio ni lado de cada pasaje: consta como «no consta». Citamos
  por tramo de la transcripción.
- **¿Cuánto acierta el agente?** No inventa citas en 18,5 de 20 respuestas, y es completo en lo esencial en 11 de 20. Con
  las herramientas usadas a mano se responden las 20, así que el límite está en el modelo pequeño y gratuito que
  usamos.

## 4. Si hay proyector y tiempo

Abrir `visor/index.html` en el navegador (necesita internet: carga la biblioteca de dibujo desde un CDN; probarlo
antes en la sala, y si no hay red usar la captura de la diapositiva 10) y escribir «Chuquitapa» en el buscador. Se ven sus 45
grafías, quién afirma qué de él y, en ámbar, lo que está en disputa.

## 5. Si se presenta solo con el visor (sin diapositivas)

El visor tiene tres pestañas: **Grafo**, **Ontología** y **Tesauro**. Recorrido de unos 10 minutos, en el mismo orden
que las diapositivas:

0. **Tres niveles (2 min), si hay que aclarar ontología frente a tesauro.** Pulsar los pasos 1, 2 y 3. La analogía:
   la ontología es el formulario (qué campos tiene una afirmación), el tesauro son las opciones de la lista desplegable
   (qué se puede poner en algunos campos) y el grafo es el formulario rellenado. Frase de cierre (está en la página): «la
   ontología dice que una afirmación tiene una polaridad; el tesauro dice cuáles existen; el grafo dice que esta niega».
1. **Ontología, arriba (1 min).** Leer la frase inicial y las cifras: 0 términos propios, 12 esquemas, 50 reglas,
   33 806 tripletas. «Esto es lo que estamos construyendo».
2. **Las cinco tarjetas de capa (2 min).** Pulsar cada una de arriba abajo y decir solo su pregunta: ¿qué papel es?,
   ¿qué está escrito?, ¿quién dijo qué de quién?, ¿qué propone el investigador? y ¿de dónde sale el dato? Pasar el
   ratón por una clase muestra qué significa.
3. **El ejemplo de Cano (2 min).** En la tarjeta 3, «Cano NIEGA que fuera coronel»: a la derecha salen sus tripletas
   reales en el compartimento azul «3 · Afirmación». Señalar `crm:P2_has_type → pol:niega` y `crm:P17 → A-UT01-001`
   (lo que él mismo afirmó en agosto). Pulsar el enlace de la mención para bajar a la capa 2, y en la tarjeta 4 abrir
   «Andrés Chuquitapa»: dos compartimentos, la proposición y, aparte, el argumento y la creencia «probable».
4. **Fuerza y principios (1 min).** Bajar a la tabla de fuerza (sale del tipo de actuación) y a los principios.
5. **Tesauro (2 min).** Abrir «Cargos, oficios y grados»: definición, fuente, «definición de trabajo», «cercano a»
   (AAT, Wikidata) y cuántas veces se usa. Buscar «ordinaria» para mostrar la decisión de «India Ordinaria» y
   preguntarles su opinión.
6. **Grafo (2 min).** Volver a la pestaña Grafo, buscar «Chuquitapa» y mostrar las disputas en ámbar. En una
   afirmación del inspector, «ver en RDF» devuelve a sus tripletas: lo que se ve en el dibujo está en el grafo.

Sin internet solo falta el dibujo de la pestaña Grafo (la biblioteca se carga de un CDN): la búsqueda, el inspector,
«ver en RDF» y las pestañas Ontología y Tesauro funcionan igual. Comprobado con la red bloqueada.
