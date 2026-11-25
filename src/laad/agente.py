"""Agente de consulta (harness, etapa 2): un modelo de lenguaje responde preguntas libres usando SOLO las
herramientas de laad.herramientas, y su respuesta se verifica antes de darla por buena.

El agente no depende del proveedor del modelo. Cada proveedor (laad.proveedores) es un adaptador pequeño que
guarda la conversación en su formato nativo y traduce turnos; aquí viven el bucle, las reglas y la verificación:

1. la pregunta va al modelo con las instrucciones versionadas (prompts/agente_consulta_v<N>.md) y las
   herramientas del registro (nombre, descripción, JSON Schema);
2. cada llamada a herramienta se ejecuta con herramientas.usar; un parámetro inválido vuelve al modelo como error
   para que corrija la llamada (no se repara a mano);
3. la respuesta final se verifica con herramientas.verificar contra TODAS las filas devueltas en la conversación:
   una cita entre comillas o un id de afirmación que no esté en ellas devuelve la respuesta al modelo para que la
   corrija (una vez); si sigue fallando, la respuesta se entrega marcada como NO VERIFICADA, nunca como buena;
4. el modelo declara la forma de su respuesta (FORMA: …), que el banco de pruebas compara con la referencia.
"""
from __future__ import annotations

import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol

from . import herramientas as H
from .evaluacion_harness import Ejecucion

RAIZ = Path(__file__).resolve().parents[2]
PROMPT = RAIZ / "prompts" / "agente_consulta_v2.md"
FORMAS = ("D", "A", "DISPUTA", "NC", "R", "P")
_FORMA = re.compile(r"^\s*FORMA:\s*(D|A|DISPUTA|NC|R|P)\s*$", re.M)


# ───────────────────────── lo que intercambian el agente y el proveedor ─────────────────────────

@dataclass
class Llamada:
    """Una llamada a herramienta pedida por el modelo."""
    id: str
    nombre: str
    parametros: dict


@dataclass
class ResultadoLlamada:
    llamada: Llamada
    texto: str
    es_error: bool = False


@dataclass
class Turno:
    """Lo que devuelve el modelo en un turno. `fin`: «herramientas» (pide llamadas), «respuesta» (terminó),
    «rechazo» (el modelo o el proveedor se negó), «corte» (se agotó el límite de salida)."""
    texto: str
    llamadas: list[Llamada]
    fin: str
    tokens_entrada: int = 0
    tokens_salida: int = 0


class Proveedor(Protocol):
    nombre: str
    modelo: str

    def iniciar(self, sistema: str, herramientas: list[dict]) -> None:
        """Empieza una conversación nueva. `herramientas`: [{nombre, descripcion, parametros (JSON Schema)}]."""

    def enviar(self, texto: str) -> Turno:
        """Añade un mensaje del usuario y devuelve el turno del modelo."""

    def devolver(self, resultados: list[ResultadoLlamada]) -> Turno:
        """Devuelve al modelo los resultados de TODAS las llamadas de su último turno, juntos."""


# ───────────────────────── resultado del agente ─────────────────────────

@dataclass
class RespuestaAgente:
    pregunta: str
    texto: str
    forma: str | None
    verificacion: dict[str, list[str]]
    ejecucion: Ejecucion
    estado: str                        # «verificada», «no verificada», «rechazo», «corte», «límite de pasos»
    pasos: int = 0
    tokens_entrada: int = 0
    tokens_salida: int = 0
    segundos: float = 0.0
    traza: list[str] = field(default_factory=list)

    @property
    def verificada(self) -> bool:
        return self.estado == "verificada"


def instrucciones(ruta: Path = PROMPT) -> str:
    return ruta.read_text(encoding="utf-8")


def declaraciones() -> list[dict]:
    """Las herramientas del registro en forma neutra (cada proveedor las traduce a su formato)."""
    return [{"nombre": h.nombre, "descripcion": h.descripcion, "parametros": h.parametros} for h in H.HERRAMIENTAS]


def forma_declarada(texto: str) -> str | None:
    m = list(_FORMA.finditer(texto))
    return m[-1].group(1) if m else None


def _sin_forma(texto: str) -> str:
    return _FORMA.sub("", texto).rstrip()


def _ejecutar(ll: Llamada, ej: Ejecucion) -> ResultadoLlamada:
    t = time.perf_counter()
    try:
        r = H.usar(ll.nombre, **(ll.parametros or {}))
    except H.ErrorHerramienta as e:
        ej.errores.append(f"{ll.nombre}: {e}")
        return ResultadoLlamada(ll, f"ERROR: {e}", True)
    except TypeError as e:                          # parámetro desconocido que el esquema no cubrió
        ej.errores.append(f"{ll.nombre}: {e}")
        return ResultadoLlamada(ll, f"ERROR: parámetros no válidos para {ll.nombre}: {e}", True)
    ej.tiempos.append((ll.nombre, time.perf_counter() - t))
    ej.resultados.append(r)
    return ResultadoLlamada(ll, r.texto)


def _correccion(v: dict[str, list[str]]) -> str:
    partes = []
    if v["citas"]:
        partes.append("estas citas no están, literalmente, en lo que devolvieron las herramientas: "
                      + "; ".join(f"«{c}»" for c in v["citas"]))
    if v["ids"]:
        partes.append("estos ids de afirmación no aparecen en lo devuelto: " + ", ".join(v["ids"]))
    return ("Tu respuesta no pasó la verificación: " + " | ".join(partes) + ". Reescríbela usando solo texto "
            "copiado literalmente de los resultados (o quita las comillas si no es una cita) y solo ids que "
            "aparezcan en ellos. Puedes volver a consultar. Termina con la línea FORMA.")


def preguntar(pregunta: str, proveedor: Proveedor, *, max_pasos: int = 12, correcciones: int = 1,
              sistema: str | None = None) -> RespuestaAgente:
    """Responde una pregunta con el proveedor dado. Nunca lanza por un error de herramienta: lo devuelve al
    modelo. `max_pasos` limita los turnos del modelo (protege del bucle y del gasto)."""
    inicio = time.perf_counter()
    ej = Ejecucion()
    traza: list[str] = []
    proveedor.iniciar(sistema or instrucciones(), declaraciones())
    turno = proveedor.enviar(pregunta)
    pasos, ent, sal = 1, turno.tokens_entrada, turno.tokens_salida
    restantes = correcciones

    def fin(estado: str, texto: str) -> RespuestaAgente:
        v = H.verificar(texto, ej.filas) if texto else {"citas": [], "ids": []}
        return RespuestaAgente(pregunta, _sin_forma(texto), forma_declarada(texto), v, ej, estado, pasos, ent, sal,
                               time.perf_counter() - inicio, traza)

    while True:
        if turno.fin in ("rechazo", "corte"):
            traza.append(f"el modelo terminó por {turno.fin}")
            return fin(turno.fin, turno.texto)
        if turno.llamadas:
            if pasos >= max_pasos:
                traza.append(f"límite de {max_pasos} pasos alcanzado")
                return fin("límite de pasos", turno.texto)
            resultados = []
            for ll in turno.llamadas:
                r = _ejecutar(ll, ej)
                traza.append(f"{H.cabecera(ll.nombre, ll.parametros or {})}" + (" → ERROR" if r.es_error else ""))
                resultados.append(r)
            turno = proveedor.devolver(resultados)
        else:
            v = H.verificar(turno.texto, ej.filas)
            if not (v["citas"] or v["ids"]):
                return fin("verificada", turno.texto)
            if restantes <= 0 or pasos >= max_pasos:
                traza.append("la respuesta sigue sin pasar la verificación")
                return fin("no verificada", turno.texto)
            restantes -= 1
            traza.append("verificación fallida: se pide corrección")
            turno = proveedor.enviar(_correccion(v))
        pasos += 1
        ent += turno.tokens_entrada
        sal += turno.tokens_salida
