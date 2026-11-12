"""Verifica que cada cita de los registros de afirmación sea subcadena exacta del tramo indicado.

Uso: python scripts/verificar_citas.py datos/registros/*.jsonl
Sale con código 1 si alguna cita falla (umbral exigido: 100 %).
"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from laad.fuente import verificar_cita

total = malas = 0
for ruta in sys.argv[1:]:
    for n, linea in enumerate(open(ruta, encoding="utf-8"), 1):
        if not linea.strip():
            continue
        reg = json.loads(linea)
        for campo in ("cita", "cita_firma"):
            if reg.get(campo):
                total += 1
                r = verificar_cita(reg[campo], reg["tramo"])
                if not r.valida:
                    malas += 1
                    print(f"FALLA {ruta}:{n} {reg.get('id')} [{campo}] {r.motivo}")
pct = 100 * (total - malas) / total if total else 0
print(f"citas verificadas: {total - malas}/{total} ({pct:.1f} %)")
sys.exit(1 if malas or not total else 0)
