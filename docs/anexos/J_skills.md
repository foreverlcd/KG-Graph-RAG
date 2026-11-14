# Anexo J · Búsqueda de «skills» para Claude Code

> Búsqueda hecha el 2026-11-14 de «skills» para Claude Code que pudieran servir al proyecto. Este anexo deja
> constancia del resultado; no recomienda instalar nada.

## Resultado

**Ninguna encaja de forma específica con ontologías de archivos históricos.** Las candidatas más cercanas fueron:

* **open-ontologies:** un servidor MCP que se distribuye con un binario.
* **claude-code-my-workflow:** un flujo de trabajo académico con LaTeX y Beamer; sería útil copiando piezas, no entero.
* **beamer-skill.**
* **ontocraft.**
* **academic-writing-skills.**

## Decisión

**No se instaló ninguna.** Ejecutar código de terceros y cambiar la configuración es una decisión del usuario.

## Cómo se cubre el control de calidad

Con pruebas propias del repositorio: formas SHACL con sus pruebas negativas y mutaciones
(`tests/test_formas_negativas.py`), razonador OWL RL (`scripts/razonar.py`) y cifras al día (`tests/test_cifras.py`).
