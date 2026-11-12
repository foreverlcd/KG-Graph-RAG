"""Genera docs/anexos/respuestas_pc.md con la respuesta del grafo a cada pregunta de competencia."""
import sys, pathlib
RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from laad.preguntas import PREGUNTAS

partes = ["# Respuestas del grafo a las preguntas de competencia\n",
          "> Generado por `scripts/responder_pc.py` a partir de `datos/grafo/hilo_central.trig`. No editar a mano.\n"]
for pc in sorted(PREGUNTAS):
    partes.append(f"## {pc}\n\n```text\n{PREGUNTAS[pc]().texto()}```\n")
out = RAIZ / "docs/anexos/respuestas_pc.md"
out.write_text("\n".join(partes), encoding="utf-8")
print(f"escrito {out}")
