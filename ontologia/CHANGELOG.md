# Registro de cambios del perfil OHAC y de su tesauro

Una sola versión para todo `ontologia/` (tesauro, formas y encabezado del perfil), en `owl:versionInfo` de cada
esquema de `tesauro.ttl` y de `ohac.ttl`. Qué sube cada cifra y cómo se cambia el vocabulario: [README.md](README.md).
Los conceptos **candidatos** (`candidatos.ttl`) no tienen versión: entran en una cuando se aprueban.

## [0.2.0] — 2026-11-14

Crecimiento controlado del vocabulario. Ningún concepto existente cambia de IRI ni de significado.

### Añadido
- **Conceptos candidatos**: `datos/candidatos_tesauro.csv` → `candidatos.ttl` (`scripts/candidatos.py`). Cada
  candidato es un `skos:Concept` de su esquema, miembro de la colección `tes:candidatos`, con definición, ejemplo,
  proponente, fecha y expediente. 19 candidatos pendientes: 7 cargos, 8 tipos de entidad, 2 atributos, 1 rol y
  1 condición.
- **Dominio y rango de cada atributo**: `datos/atributos.csv` → `formas_atributos.ttl` (`scripts/atributos.py`), una
  forma por atributo (32: los 30 del tesauro y los 2 candidatos).
- Formas `ohac:ConceptoCandidatoForma` (aviso, `sh:Warning`: nodos que usan un candidato) y
  `ohac:ConceptoRetiradoForma` (violación: nodos que usan un concepto `owl:deprecated`).
- Versión del tesauro: `owl:versionInfo` y `dct:modified` en cada esquema; sección generada «APROBADOS» en
  `tesauro.ttl` para los candidatos que se aprueben.
- Consulta con nombre `consultas/candidatos_en_uso.rq`.

### Cambiado
- `atr:ordena`: el sujeto puede ser la cosa afectada por una orden impersonal («desglósese», «agréguese»).
  Ampliación de la definición; lo anotado antes sigue siendo válido.
- `atr:folio-de-pieza`: el sujeto puede ser la mención de un documento que no es una pieza del expediente.
  Ampliación de la definición; lo anotado antes sigue siendo válido.

### Retirado
- Nada.

## [0.1.0] — 2026-11-13

Estado anterior al registro de cambios: tesauro de 12 esquemas y 164 conceptos, formas SHACL de las capas 1–4 y de procedencia, y encabezado del perfil. Sin candidatos, sin
dominio ni rango comprobados y sin política de cambios escrita.
