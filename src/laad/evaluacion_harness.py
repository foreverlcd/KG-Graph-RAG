"""Banco de pruebas del harness de consulta: las 20 preguntas de competencia redactadas como las escribiría un
historiador (datos/evaluacion/preguntas_harness.jsonl), cada una con un PLAN de llamadas a laad.herramientas, y un
comprobador que compara lo que el plan obtiene con la respuesta de referencia de laad.preguntas.pcNN().

El plan de cada línea lo escribió una persona; el agente LLM escribirá el suyo y se medirá con el MISMO comprobador
(comprobar). Formato de una línea:

    {"pc": "PC09", "pregunta": "…", "forma": "DISPUTA",
     "plan": [{"herramienta": "buscar", "parametros": {"nombre": "Andrés Chuquitapa"},
               "elegir": "R-chuquitapa", "como": "chuquitapa"},
              {"herramienta": "afirmaciones", "parametros": {"entidad": "$chuquitapa", "atributo": "ejerce-cargo"}}]}

* «elegir» (solo tras buscar): el id que el agente escoge entre los candidatos; debe estar entre ellos (como
  candidato, como rival o como mención que coincide). Queda en la variable «$<como>».
* «como» en otra herramienta guarda sus filas: «$<como>[campo]» es la lista de ese campo en ellas.
* «forma» es la forma que el agente declara (D, A, DISPUTA, NC, R, P).

Lo esencial que se comprueba (comprobar):
1. la forma declarada es la de la referencia, y está respaldada: DISPUTA exige que alguna herramienta haya
   calculado DISPUTA; NC, que alguna haya devuelto «no consta» (ninguna fila); las demás, que haya filas;
2. las afirmaciones de la referencia (por IRI) están entre las filas obtenidas, y también sus afirmantes;
3. las reconstrucciones de la referencia (por etiqueta) y sus participaciones (PC15, por mención) también;
4. toda cita entre comillas y todo id (A-…, M-…, pieza, HGIS, IRI) del texto de la referencia está en las filas
   obtenidas (herramientas.verificar y búsqueda de subcadena): lo que la referencia dice, el plan lo alcanzó. Una
   IRI de un registro (https://w3id.org/laad/id/…) cuenta si está su id local: el agente no maneja IRIs;
5. el texto compuesto por las herramientas supera verificar() con sus propias filas.
"""
from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, field
from pathlib import Path

from . import herramientas as H
from .consulta import ID
from .preguntas import PREGUNTAS
from .responder import Respuesta

RAIZ = Path(__file__).resolve().parents[2]
BANCO = RAIZ / "datos" / "evaluacion" / "preguntas_harness.jsonl"
FORMAS = ("D", "A", "DISPUTA", "NC", "R", "P")


@dataclass
class Ejecucion:
    resultados: list[H.Resultado] = field(default_factory=list)
    tiempos: list[tuple[str, float]] = field(default_factory=list)
    errores: list[str] = field(default_factory=list)

    @property
    def filas(self) -> list[dict]:
        return [f for r in self.resultados for f in r.filas]

    @property
    def texto(self) -> str:
        return "\n".join(r.texto for r in self.resultados)


def cargar(ruta: Path = BANCO) -> list[dict]:
    return [json.loads(x) for x in ruta.read_text(encoding="utf-8").splitlines() if x.strip()]


_VAR = re.compile(r"^\$(\w+)(?:\[(\w+)\])?$")


def _resolver(v, variables: dict):
    if isinstance(v, list):
        out = []
        for x in v:
            r = _resolver(x, variables)
            out.extend(r if isinstance(r, list) else [r])
        return out
    if isinstance(v, str) and (m := _VAR.match(v)):
        nombre, campo = m.groups()
        if nombre not in variables:
            raise H.ErrorHerramienta(f"variable ${nombre} sin definir en el plan")
        x = variables[nombre]
        if campo is None:
            return x
        return [f[campo] for f in x if f.get(campo) is not None]
    return v


def _candidatos(r: H.Resultado) -> set[str]:
    ids = set()
    for c in r.filas:
        ids.add(c["id"])
        ids.update(rv["id"] for rv in c.get("rivales", []))
        ids.update(c.get("menciones_coincidentes", []))
    return ids


def ejecutar_plan(plan: list[dict]) -> Ejecucion:
    """Ejecuta los pasos en orden con herramientas.usar. Un error de herramienta se anota y el plan sigue (un
    agente corregiría la llamada; aquí cuenta como fallo)."""
    ej, variables = Ejecucion(), {}
    for i, paso in enumerate(plan, 1):
        nombre = paso["herramienta"]
        try:
            params = {k: _resolver(v, variables) for k, v in paso.get("parametros", {}).items()}
            t = time.perf_counter()
            r = H.usar(nombre, **params)
            ej.tiempos.append((f"{i}. {nombre}", time.perf_counter() - t))
        except H.ErrorHerramienta as e:
            ej.errores.append(f"paso {i} ({nombre}): {e}")
            continue
        ej.resultados.append(r)
        if "elegir" in paso:
            if paso["elegir"] not in _candidatos(r):
                ej.errores.append(f"paso {i}: «{paso['elegir']}» no está entre los candidatos de buscar")
                continue
            if "como" in paso:
                variables[paso["como"]] = paso["elegir"]
        elif "como" in paso:
            variables[paso["como"]] = r.filas
    return ej


_OTROS_IDS = re.compile(r"(?<![\w-])(?:M-[A-Za-z0-9.-]*[A-Za-z0-9]|P\d+[a-z]?(?![\w-])|HGIS:[^\s,;)]+)"
                        r"|https?://[^\s,;)»]+")


def _sin_pregunta(texto: str) -> str:
    return texto.split("\n", 1)[1] if texto.startswith("PREGUNTA:") else texto


def comprobar(referencia: Respuesta, ej: Ejecucion, forma: str) -> list[str]:
    """Fallos de una ejecución frente a la respuesta de referencia (lista vacía = PC alcanzada)."""
    fallos = list(ej.errores)
    filas = ej.filas
    if forma != referencia.forma:
        fallos.append(f"forma declarada {forma}, la referencia es {referencia.forma}")
    calculadas = [r.forma for r in ej.resultados]
    if forma == "DISPUTA" and "DISPUTA" not in calculadas:
        fallos.append("forma DISPUTA sin respaldo: ninguna herramienta calculó una disputa")
    elif forma == "NC" and "NC" not in calculadas:
        fallos.append("forma NC sin respaldo: todas las herramientas devolvieron filas")
    elif forma not in ("DISPUTA", "NC") and not filas:
        fallos.append(f"forma {forma} sin filas que la respalden")
    obtenidas = {f["a"] for f in filas if "a" in f and "aid" in f}
    faltan = [f["aid"] for f in referencia.afirmaciones if f["a"] not in obtenidas]
    if faltan:
        fallos.append(f"faltan {len(faltan)} afirmaciones de la referencia: {', '.join(sorted(set(faltan))[:10])}")
    afirmantes = {f["afirmante"] for f in filas if "aid" in f}
    faltan = sorted({f["afirmante"] for f in referencia.afirmaciones} - afirmantes)
    if faltan:
        fallos.append(f"faltan afirmantes: {', '.join(faltan)}")
    etiquetas = {f.get("label") or f.get("etiqueta") for f in filas}
    faltan = sorted({r["label"] for r in referencia.reconstrucciones} - etiquetas)
    if faltan:
        fallos.append(f"faltan {len(faltan)} reconstrucciones: {'; '.join(faltan[:5])}")
    mids = {f["mid"] for f in filas if "rol" in f and "mid" in f}
    faltan = sorted({p["mid"] for p in referencia.participaciones} - mids)
    if faltan:
        fallos.append(f"faltan {len(faltan)} participaciones: {', '.join(faltan[:10])}")
    texto_ref = _sin_pregunta(referencia.texto())
    v = H.verificar(texto_ref, filas)
    if v["citas"]:
        fallos.append(f"{len(v['citas'])} citas de la referencia no están en las filas: "
                      + "; ".join(f"«{c[:60]}»" for c in v["citas"][:5]))
    if v["ids"]:
        fallos.append(f"ids de afirmación de la referencia que no están en las filas: {', '.join(v['ids'][:10])}")
    unidos = "\n".join(H.valores(filas))
    faltan = sorted({x for x in _OTROS_IDS.findall(texto_ref) if x not in unidos
                     and not (x.startswith(ID) and x.rsplit("/", 1)[-1] in unidos)})
    if faltan:
        fallos.append(f"{len(faltan)} ids de la referencia que no están en las filas: {', '.join(faltan[:10])}")
    propio = H.verificar(ej.texto, filas)
    if propio["citas"] or propio["ids"]:
        fallos.append(f"el texto de las herramientas no supera verificar(): {propio}")
    return fallos


def evaluar_linea(linea: dict) -> dict:
    """Ejecuta el plan de una línea del banco y lo compara con preguntas.<pc>()."""
    if linea.get("forma") not in FORMAS:
        raise ValueError(f"{linea['pc']}: forma {linea.get('forma')!r} no válida ({', '.join(FORMAS)})")
    ej = ejecutar_plan(linea["plan"])
    referencia = PREGUNTAS[linea["pc"]]()
    fallos = comprobar(referencia, ej, linea["forma"])
    return {"pc": linea["pc"], "alcanzada": not fallos, "fallos": fallos, "forma": linea["forma"],
            "forma_referencia": referencia.forma, "llamadas": len(ej.tiempos), "tiempos": ej.tiempos,
            "ejecucion": ej}


def evaluar(ruta: Path = BANCO) -> list[dict]:
    return [evaluar_linea(x) for x in cargar(ruta)]


def _fraccion(alcanzados: int, total: int) -> float | None:
    return round(alcanzados / total, 2) if total else None


def cobertura(referencia: Respuesta, ej: Ejecucion) -> dict[str, float | None]:
    """Qué fracción de la respuesta de referencia alcanzó una ejecución: afirmaciones (por IRI), reconstrucciones
    (por etiqueta) y citas literales. Distingue una respuesta incompleta de una errónea; `comprobar` sigue siendo
    el criterio de «alcanzada» (todo o nada). None: la referencia no tiene elementos de ese tipo."""
    filas = ej.filas
    obtenidas = {f["a"] for f in filas if "a" in f and "aid" in f}
    ref_a = {f["a"] for f in referencia.afirmaciones}
    etiquetas = {f.get("label") or f.get("etiqueta") for f in filas}
    ref_r = {r["label"] for r in referencia.reconstrucciones}
    texto_ref = _sin_pregunta(referencia.texto())
    citas = H.citas(texto_ref)
    fallan = set(H.verificar(texto_ref, filas)["citas"])
    return {"afirmaciones": _fraccion(len(ref_a & obtenidas), len(ref_a)),
            "reconstrucciones": _fraccion(len(ref_r & etiquetas), len(ref_r)),
            "citas": _fraccion(len(set(citas) - fallan), len(set(citas)))}


def evaluar_respuesta(pc: str, llamadas: list[dict], respuesta: str) -> dict:
    """Evalúa una respuesta redactada fuera del bucle del agente (p. ej. por un modelo que hace de intermediario y
    consulta con scripts/preguntar.py): vuelve a ejecutar sus llamadas declaradas ([{herramienta, parametros}]),
    verifica la respuesta contra esas filas y la mide con comprobar() y cobertura(), como el banco del agente.
    Una llamada con error es un aviso, no un fallo (el intermediario la corrigió)."""
    from .agente import _sin_forma, forma_declarada
    ej, avisos = Ejecucion(), []
    for ll in llamadas:
        try:
            ej.resultados.append(H.usar(ll["herramienta"], **(ll.get("parametros") or {})))
        except (H.ErrorHerramienta, TypeError) as e:
            avisos.append(f"{ll['herramienta']}: {e}")
    forma = forma_declarada(respuesta) or "?"
    v = H.verificar(respuesta, ej.filas)
    referencia = PREGUNTAS[pc]()
    fallos = comprobar(referencia, ej, forma)
    if v["citas"] or v["ids"]:
        fallos.append(f"respuesta no verificada: {v}")
    return {"pc": pc, "alcanzada": not fallos, "forma": forma, "forma_referencia": referencia.forma,
            "verificada": not (v["citas"] or v["ids"]), "verificacion": v, "fallos": fallos,
            "cobertura": cobertura(referencia, ej), "avisos": avisos, "llamadas": len(llamadas),
            "respuesta": _sin_forma(respuesta)}
