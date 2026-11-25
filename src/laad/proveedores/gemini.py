"""Proveedor Gemini (API de Google, SDK google-genai) para laad.agente.

Mismo patrón que el prototipo anterior del proyecto (Grafo-Conocimiento-Cusco): genai.Client con la clave de
GOOGLE_API_KEY y api_version v1beta. Llamada a funciones manual: el SDK NO ejecuta las herramientas
(automatic_function_calling desactivado); las ejecuta laad.agente y aquí solo se traducen los turnos.

El historial se guarda como lista de types.Content y se reenvía entero en cada petición, incluido el contenido
del modelo tal como llegó (con sus firmas de pensamiento, que la API exige devolver intactas).

Aviso: en el nivel gratuito de Google AI Studio el contenido enviado puede usarse para mejorar los productos de
Google. Lo que se envía aquí son las preguntas y los resultados de las herramientas (texto del expediente, que es
público en el ARC Cusco), no datos personales del usuario.
"""
from __future__ import annotations

import os
import time

from ..agente import Llamada, ResultadoLlamada, Turno

MODELO = "gemini-3.6-flash"
_RECHAZO = {"SAFETY", "RECITATION", "BLOCKLIST", "PROHIBITED_CONTENT", "SPII", "LANGUAGE", "OTHER"}
_MAL_FORMADA = {"MALFORMED_FUNCTION_CALL", "UNEXPECTED_TOOL_CALL"}


class CuotaDiaria(RuntimeError):
    """La cuota diaria de peticiones del nivel gratuito se agotó (en 2026-11: 20 peticiones/día con
    gemini-3.6-flash; cada pregunta gasta una por turno del modelo)."""


class Gemini:
    nombre = "gemini"

    def __init__(self, modelo: str | None = None, *, cliente=None, reintentos: int = 4, espera: float = 20.0,
                 max_salida: int = 4096, pensamiento: str | None = None, limite_s: float = 90.0):
        self.modelo = modelo or os.environ.get("GEMINI_MODEL") or MODELO
        self._cliente = cliente
        self.reintentos, self.espera, self.max_salida = reintentos, espera, max_salida
        # nivel de pensamiento (MINIMAL, LOW, MEDIUM, HIGH; None = el del modelo) y límite por petición
        self.pensamiento = pensamiento or os.environ.get("GEMINI_PENSAMIENTO") or "LOW"
        self.limite_s = limite_s
        self.historial: list = []
        self._config = None
        self._ultimas: list[Llamada] = []

    # ── conexión ──
    @property
    def cliente(self):
        if self._cliente is None:
            from google import genai
            clave = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
            if not clave:
                raise EnvironmentError("Falta GOOGLE_API_KEY (variable de entorno o archivo .env; ver .env.example).")
            self._cliente = genai.Client(api_key=clave, http_options={"api_version": "v1beta",
                                                                          "timeout": int(self.limite_s * 1000)})
        return self._cliente

    # ── protocolo Proveedor ──
    def iniciar(self, sistema: str, herramientas: list[dict]) -> None:
        from google.genai import types
        decl = [types.FunctionDeclaration(name=h["nombre"], description=h["descripcion"],
                                          parameters_json_schema=h["parametros"]) for h in herramientas]
        self._config = types.GenerateContentConfig(
            system_instruction=sistema,
            tools=[types.Tool(function_declarations=decl)],
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
            temperature=0.0,
            max_output_tokens=self.max_salida,
            thinking_config=types.ThinkingConfig(thinking_level=self.pensamiento),
        )
        self.historial = []
        self._ultimas = []

    def enviar(self, texto: str) -> Turno:
        from google.genai import types
        self.historial.append(types.Content(role="user", parts=[types.Part.from_text(text=texto)]))
        return self._turno()

    def devolver(self, resultados: list[ResultadoLlamada]) -> Turno:
        from google.genai import types
        partes = []
        for r in resultados:
            p = types.Part.from_function_response(
                name=r.llamada.nombre, response={"error": r.texto} if r.es_error else {"resultado": r.texto})
            if r.llamada.id and not r.llamada.id.startswith("gemini-"):
                p.function_response.id = r.llamada.id
            partes.append(p)
        self.historial.append(types.Content(role="user", parts=partes))
        return self._turno()

    # ── interno ──
    def _generar(self):
        from google.genai.errors import APIError
        for intento in range(self.reintentos + 1):
            try:
                return self.cliente.models.generate_content(model=self.modelo, contents=self.historial,
                                                            config=self._config)
            except Exception as e:  # noqa: BLE001
                # 429 (cuota del nivel gratuito), 5xx (sobrecarga) y peticiones que superan limite_s se reintentan
                # con espera creciente; lo demás (clave inválida, petición mal formada) sube tal cual
                # la cuota DIARIA del nivel gratuito no es transitoria: esperar no sirve, se avisa enseguida
                if isinstance(e, APIError) and getattr(e, "code", None) == 429 and "PerDay" in str(e):
                    raise CuotaDiaria(f"cuota diaria del nivel gratuito agotada para {self.modelo}") from e
                transitorio = (isinstance(e, APIError) and getattr(e, "code", None) in (429, 500, 502, 503, 504)) \
                    or "Timeout" in type(e).__name__
                if not transitorio or intento == self.reintentos:
                    raise
                time.sleep(self.espera * (intento + 1))

    def _turno(self, reparar: int = 1) -> Turno:
        resp = self._generar()
        uso = resp.usage_metadata
        ent = (uso.prompt_token_count or 0) if uso else 0
        sal = ((uso.candidates_token_count or 0) + (uso.thoughts_token_count or 0)) if uso else 0
        if not resp.candidates:
            motivo = getattr(getattr(resp, "prompt_feedback", None), "block_reason", None)
            return Turno(f"(bloqueado: {motivo})", [], "rechazo", ent, sal)
        cand = resp.candidates[0]
        fin = getattr(cand.finish_reason, "name", str(cand.finish_reason or ""))
        contenido = cand.content
        partes = (contenido.parts or []) if contenido else []
        if fin in _MAL_FORMADA and reparar:
            from google.genai import types
            self.historial.append(types.Content(role="user", parts=[types.Part.from_text(
                text="Tu llamada a la herramienta estaba mal formada. Vuelve a hacerla con argumentos JSON válidos "
                     "según el esquema de la herramienta.")]))
            t = self._turno(reparar - 1)
            return Turno(t.texto, t.llamadas, t.fin, t.tokens_entrada + ent, t.tokens_salida + sal)
        if contenido and partes:
            self.historial.append(contenido)
        texto = "".join(p.text for p in partes if p.text and not p.thought)
        llamadas = [Llamada(p.function_call.id or f"gemini-{i}", p.function_call.name, dict(p.function_call.args or {}))
                    for i, p in enumerate(partes) if p.function_call]
        self._ultimas = llamadas
        if llamadas:
            return Turno(texto, llamadas, "herramientas", ent, sal)
        if fin == "MAX_TOKENS":
            return Turno(texto, [], "corte", ent, sal)
        if fin in _RECHAZO or fin in _MAL_FORMADA:
            return Turno(texto or f"(el proveedor terminó por {fin})", [], "rechazo", ent, sal)
        return Turno(texto, [], "respuesta", ent, sal)
