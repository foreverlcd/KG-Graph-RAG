"""Mide si las citas (cita_textual_evidencia) de extracciones.jsonl son subcadenas
exactas de la transcripción paleográfica o del corpus modernizado.
Uso: python3 -I medir_citas.py extracciones.jsonl paleografica.txt modernizado.txt"""
import json, re, sys, unicodedata

def leer(p):
    return open(p, encoding='utf-8-sig').read().replace('\r\n', '\n').replace('\r', '\n')

def ws(s):  # colapsa espacios/saltos
    return re.sub(r'\s+', ' ', s).strip()

def suave(s):  # espacios + minúsculas + sin tildes
    s = unicodedata.normalize('NFD', ws(s).lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')

ext_path, pal_path, mod_path = sys.argv[1:4]
pal, mod = leer(pal_path), leer(mod_path)
P = {'raw': pal, 'ws': ws(pal), 'suave': suave(pal)}
M = {'raw': mod, 'ws': ws(mod), 'suave': suave(mod)}
citas = []
for n, line in enumerate(open(ext_path, encoding='utf-8'), 1):
    e = json.loads(line)
    for a in e['afirmaciones']:
        citas.append((n, a['id'], a['cita_textual_evidencia']))
tot = len(citas)
cont = {k: 0 for k in ['pal_raw', 'pal_ws', 'pal_suave', 'mod_raw', 'mod_ws', 'mod_suave', 'ninguno_ws', 'ninguno_suave']}
fallos = []
for n, aid, c in citas:
    pr, pw, ps = c in P['raw'], ws(c) in P['ws'], suave(c) in P['suave']
    mr, mw, ms = c in M['raw'], ws(c) in M['ws'], suave(c) in M['suave']
    cont['pal_raw'] += pr; cont['pal_ws'] += pw; cont['pal_suave'] += ps
    cont['mod_raw'] += mr; cont['mod_ws'] += mw; cont['mod_suave'] += ms
    if not (pw or mw): cont['ninguno_ws'] += 1
    if not (ps or ms):
        cont['ninguno_suave'] += 1
        fallos.append((n, aid, c))
print(f'Total de citas: {tot}')
for k, v in cont.items():
    print(f'  {k:14s}: {v:3d}  ({100*v/tot:5.1f} %)')
print('\nCitas que no aparecen en ninguno de los dos textos (ni normalizando espacios, mayúsculas y tildes):')
for n, aid, c in fallos:
    # localizar el prefijo más largo que sí aparece en la paleográfica
    s = suave(c); k = len(s)
    while k > 0 and s[:k] not in P['suave']: k -= 1
    print(f'  - línea {n} de extracciones.jsonl, {aid}: coincide solo el prefijo de {k}/{len(s)} car.\n      «{c[:200]}»')
