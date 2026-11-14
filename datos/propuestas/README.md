# Propuestas de conectividad (2026-11-14)

Lo que tres agentes (claude-fable-5-2) propusieron para conectar el grafo del expediente `cc-14-18`, tal como lo
entregaron. Se conserva como registro: lo integrado vive en `datos/reconstrucciones.jsonl`, en los generadores de
`datos/registros/` y en `datos/candidatos_tesauro.csv`.

| Archivo | Contenido |
|---|---|
| `personas.jsonl` | 40 reconstrucciones de identidad de personas (11 ampliadas, 29 nuevas) |
| `personas_sin_enlazar.csv` | 22 menciones de persona que se dejan sin enlazar, con su motivo |
| `entidades.jsonl` | 45 reconstrucciones de grupos, lugares y cosas (2 ampliadas, 43 nuevas) |
| `entidades_sin_enlazar.csv` | 80 menciones sin enlazar, con su motivo |
| `tipos_entidad.csv` | tipo de entidad propuesto, con concepto existente, para 7 menciones |
| `candidatos_propuestos.csv` | 7 conceptos candidatos nuevos y las menciones que los usan |
| `hechos.jsonl` | 13 reconstrucciones de hechos (2 ampliadas, 11 nuevas) |
| `hechos_sin_enlazar.csv` | 15 hechos narrados sin agrupar, con su motivo |
| `hechos_observaciones.md` | problemas de anotación de la capa 3 detectados al agrupar hechos (no corregidos) |

Integración: `python scripts/integrar_propuestas.py` (idempotente; `--comprobar` dice si falta algo). Después,
los generadores de registros, `scripts/candidatos.py`, `scripts/construir.py`, `scripts/razonar.py` y
`scripts/cifras.py`. Decisión y límites: `docs/anexos/K_conectividad.md` y ADR-044.
