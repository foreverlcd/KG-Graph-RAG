# Visor del grafo

Un único archivo HTML, al estilo de Neo4j Browser, para explorar quién afirma qué sobre quién en el expediente.

    python scripts/visor.py        # lee el grafo construido y escribe visor/index.html desde visor/plantilla.html
    # abrir visor/index.html en el navegador (los datos van dentro; las bibliotecas del grafo se cargan de jsDelivr)

`plantilla.html` es la página; `index.html` es la plantilla con los datos incrustados (generado: no editar a mano).

## Qué muestra

* **Etiquetas de nodo**: Persona, Lugar, Grupo, Cosa, Hecho, Cargo (reconstrucciones de la capa 4), Pieza, Mención
  (sin identidad única: hipótesis rivales o sin reconstruir) y HechoNarrado. Borde oscuro = creencia «verdadero»;
  relleno pálido y borde discontinuo = «posible» o menos. El tamaño crece con las afirmaciones.
* **Tipos de relación**:
  * `AFIRMA` / `NIEGA`: afirmante → sujeto, una por atributo, rotulada con él (`ejerce-cargo ×2`);
  * `TIENE_VALOR`: sujeto → valor de una afirmación cuando el valor es otra entidad;
  * `HIPOTESIS_DE`: mención → cada reconstrucción que la reclama (si hay varias, son rivales);
  * `INTERVIENE_EN`: afirmante → pieza en que habla, con su papel (oculta al principio, como las piezas).
  En ámbar, las relaciones con afirmaciones en una disputa calculada.
* **Inspector** (derecha): propiedades, relaciones agrupadas por tipo, grafías en el texto y todas las afirmaciones
  con cita literal, pieza, tramo, fuerza y fundamento.

## Cómo se usa

* Las etiquetas y los tipos de relación de la izquierda son filtros: pulsarlos los oculta o muestra.
* Clic en un nodo o relación: inspector. Pasar el ratón: resalta los vecinos, rotula sus relaciones y muestra un resumen con citas.
* **Explorar vecindario** (o doble clic en un nodo): solo ese nodo y sus vecinos; cada doble clic en un vecino lo amplía.
  **Mostrar todo** vuelve al grafo completo.
* Búsqueda por nombre, grafía antigua o id (también de afirmación, `A-UT11-004`).
* **3D**: la misma red en tres dimensiones (los nombres, al pasar el ratón). Se carga solo al pedirla y el 2D se pausa;
  consume más GPU, así que conviene volver al 2D para leer.

Regla de identidad, la misma del harness: una mención se dibuja como su reconstrucción solo si pertenece a una; las
reclamadas por hipótesis rivales quedan como nodo propio. Las disputas se calculan con `laad.responder`, no se
almacenan (`tests/test_visor.py`).
