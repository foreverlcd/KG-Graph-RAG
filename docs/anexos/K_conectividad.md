# Anexo K. Conectividad del grafo: enlaces de la capa 4 (2026-11-14)

> Las cifras variables están en `docs/cifras.md`. Las de este anexo son las del día de la integración.

## Por qué

La capa 2 no fusiona nada: cada aparición escrita es un nodo. Lo que conecta el grafo son las reconstrucciones de
la capa 4. Tras anotar el expediente completo solo 123 de 545 menciones y 13 de 61 hechos narrados pertenecían a
alguna reconstrucción, y 135 de las 260 menciones que no son de persona no tenían tipo de entidad. Un grafo así
responde las preguntas de competencia, pero no permite recorrerlo de una persona a todo lo que se dice de ella.

## Qué se hizo

Tres agentes (modelo de lenguaje, `claude-fable-5-2`) leyeron la transcripción original y los registros, y
propusieron reconstrucciones en `datos/propuestas/`. Reglas que se les dieron: no tocar las capas 1–3; toda
reconstrucción lleva argumento con cita literal comprobada contra la transcripción; lo dudoso se propone como
hipótesis rival con su grado de creencia, no se resuelve; lo que no se puede enlazar se lista con su motivo.
`scripts/integrar_propuestas.py` las integró.

| Clase | Enlazadas antes | Enlazadas después | Total |
|---|---:|---:|---:|
| Menciones de persona | 107 | 263 | 285 |
| Menciones de lugar | 6 | 91 | 98 |
| Menciones de grupo | 10 | 47 | 105 |
| Menciones de cosa | 0 | 42 | 57 |
| Hechos narrados | 13 | 46 | 61 |

Las reconstrucciones pasan de 35 a 118. Menciones sin tipo de entidad: de 135 a 77, con 7 tipos asignados con
conceptos existentes y 7 conceptos candidatos nuevos (`documento`, `expediente`, `dinero`, `tierra`,
`bien-mueble`, `region`, `comun`), que SHACL señala con un aviso hasta que se aprueben o se rechacen.

## Lo que no se resolvió, y cómo queda

* **Hipótesis rivales.** 58 menciones pertenecen a más de una reconstrucción a propósito: son lecturas
  incompatibles o subsidiarias que coexisten. Ejemplos: el «corregidor Don Andres» de P18 como Reparaz o como
  Chuquitapa (ambas *posible*); «Antonio» y «Agustin» Chacón como un escribano (*probable*) o dos (*improbable*);
  el motín que narra Orue como el alzamiento contra Orey o como otro tumulto; los deícticos («este pueblo»,
  «aquella provincia») en reconstrucciones subsidiarias *probable*. El esquema no tiene un campo que declare la
  rivalidad: cada reconstrucción nombra a su rival en el argumento. **Límite:** una consulta no puede distinguir
  hoy una rival de una subsidiaria sin leer el argumento.
* **Sin enlazar.** 22 menciones de persona, 80 de grupo, lugar o cosa y 15 hechos, con su motivo en los
  `*_sin_enlazar.csv`: colectivos indeterminados («los indios»), pronombres y tratamientos truncados, menciones
  únicas de quien no actúa, pasajes estropeados o ambiguos, actos procesales que no son hechos narrados.
* **Autoría.** Una reconstrucción ampliada queda a nombre de quien la amplió, con la fecha de la ampliación, y su
  argumento nombra al autor original (ADR-044).
* **Sin auditar.** La auditoría del anexo I cubrió las 35 reconstrucciones del 2026-11-13. Las 83 nuevas y las 15
  ampliadas no han pasado ninguna auditoría, y ninguna reconstrucción tiene validación humana. `docs/cifras.md` cuenta
  además como no auditadas las 6 hipótesis rivales que añadió la propia auditoría: 104 de 118 en total. Los propios agentes
  marcaron como dudosos: los enlaces por anáfora («aquel», «el denominado», «dicho alzado», «al indio», «Yo»,
  «su Merced»); los tratamientos enlazados al cargo («vuestra Merced» → Mata, «vuestro señor» → fiscal, «Vuestra
  Señoría» → Muñoz); el reparto de «señor presidente» por fecha (agosto → Ruiz de Castilla, noviembre → Muñoz);
  Santiago Cazorla sargento «primero» en P02 y «segundo» en P18 y P20; los deícticos de P16, P22 y P23 enlazados a
  Tinta; y el tipo `parcialidad` de M-UT17-817, donde la palabra significa «facción».
* **Identificadores externos** comprobados por los agentes contra las API públicas: partido de Tinta (HGIS
  JUPECUTI), intendencia del Cusco (HGIS PRPECU00, Wikidata Q5918759), provincia de Urubamba (Q1771879), Real
  Audiencia del Cuzco (Q2134673), Real Hacienda (Q140402469). Van como identificadores y `rdfs:seeAlso`, nunca
  `owl:sameAs`. No se han vuelto a comprobar de forma independiente.

## Problemas de anotación detectados (no corregidos)

Al agrupar hechos apareció que la capa 3 tiene defectos propios, detallados en
`datos/propuestas/hechos_observaciones.md`: cuatro identificadores de hecho que cubren dos ocurrencias distintas
(`H-p04-maltrato`, `H-p21-motin`, `H-p06-averiguacion` y la liberación dentro de `H-p27-prision`); hechos narrados
que no se anotaron como tales (la numeración o revisita, que es el ancla cronológica; el relato de los golpes en
P19; el de Cano en P20); y `A-UT12b-502`, donde «no sabia haber preso a Guancachoque» está anotado con polaridad
*afirma*. No se han corregido porque cambian la capa 3 y deben revisarse con la transcripción delante.
