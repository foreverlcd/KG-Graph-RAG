# Visor del grafo

Página interactiva para explorar quién afirma qué sobre quién en el expediente.

    python scripts/visor.py        # regenera visor/datos.js a partir del grafo construido
    # abrir visor/index.html en el navegador (necesita conexión: la biblioteca vis-network se carga de jsDelivr)

* **Nodos**: reconstrucciones de la capa 4 (color por clase; borde grueso = creencia «verdadero», discontinuo =
  «posible» o menos), piezas, menciones que no pertenecen a una sola reconstrucción y hechos narrados sueltos.
* **Aristas**: «afirma sobre» (afirmante → sujeto; roja si contiene una negación, ámbar si está en una disputa
  calculada), «hipótesis» (mención → cada reconstrucción que la reclama) y «valor» (desactivada por defecto).
* **Ficha**: al pulsar un nodo o una arista, sus menciones y todas sus afirmaciones con cita literal, pieza, tramo,
  fuerza y fundamento. Búsqueda por nombre, grafía o id (incluidos los de afirmación, `A-UT11-004`).

Regla de identidad, la misma del harness: una mención se dibuja como su reconstrucción solo si pertenece a una; las
reclamadas por hipótesis rivales quedan como nodo propio. Las disputas se calculan con `laad.responder`, no se
almacenan. `datos.js` es generado: no se edita a mano (`tests/test_visor.py`).
