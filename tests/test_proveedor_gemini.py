"""Adaptador Gemini (laad.proveedores.gemini) con un cliente falso: sin red, sin clave y sin coste.

Comprueba la traducción de turnos (llamadas, resultados, errores, tokens, motivos de fin) y que el historial se
reenvía con el contenido del modelo intacto. Las respuestas falsas se construyen con los tipos reales del SDK."""
import os

import pytest

types = pytest.importorskip("google.genai.types")

from laad import agente as AG  # noqa: E402
from laad import proveedores  # noqa: E402
from laad.agente import Llamada, ResultadoLlamada  # noqa: E402
from laad.proveedores.gemini import Gemini  # noqa: E402


def _resp(partes, fin="STOP", ent=100, sal=10):
    return types.GenerateContentResponse(
        candidates=[types.Candidate(content=types.Content(role="model", parts=partes), finish_reason=fin)],
        usage_metadata=types.GenerateContentResponseUsageMetadata(prompt_token_count=ent, candidates_token_count=sal,
                                                                  thoughts_token_count=1))


def _llamada(nombre, args, id_=None):
    return types.Part(function_call=types.FunctionCall(name=nombre, args=args, id=id_))


class _Modelos:
    def __init__(self, respuestas):
        self.respuestas, self.peticiones = list(respuestas), []

    def generate_content(self, model, contents, config):
        self.peticiones.append({"model": model, "contents": list(contents), "config": config})
        r = self.respuestas.pop(0)
        if isinstance(r, Exception):
            raise r
        return r


class _Cliente:
    def __init__(self, respuestas):
        self.models = _Modelos(respuestas)


def _gemini(respuestas, **kw):
    c = _Cliente(respuestas)
    g = Gemini("modelo-prueba", cliente=c, espera=0, **kw)
    g.iniciar("sistema", AG.declaraciones())
    return g, c.models


def test_declara_las_herramientas_con_su_esquema_y_desactiva_la_ejecucion_automatica():
    g, m = _gemini([_resp([types.Part(text="Hola.\nFORMA: NC")])])
    g.enviar("¿?")
    cfg = m.peticiones[0]["config"]
    nombres = [d.name for d in cfg.tools[0].function_declarations]
    assert "buscar" in nombres and len(nombres) == len(AG.declaraciones())
    assert cfg.tools[0].function_declarations[0].parameters_json_schema["type"] == "object"
    assert cfg.automatic_function_calling.disable and cfg.system_instruction == "sistema"
    assert m.peticiones[0]["model"] == "modelo-prueba"


def test_traduce_llamadas_tokens_y_devuelve_resultados_y_errores_juntos():
    g, m = _gemini([_resp([_llamada("buscar", {"nombre": "Cano"}, "x1"), _llamada("vocabulario", {"esquema": "roles"})]),
                    _resp([types.Part(text="Listo.\nFORMA: R")])])
    t = g.enviar("¿Quién es Cano?")
    assert t.fin == "herramientas" and [ll.nombre for ll in t.llamadas] == ["buscar", "vocabulario"]
    assert t.llamadas[0].id == "x1" and t.llamadas[0].parametros == {"nombre": "Cano"}
    assert t.tokens_entrada == 100 and t.tokens_salida == 11
    t2 = g.devolver([ResultadoLlamada(t.llamadas[0], "filas…"), ResultadoLlamada(t.llamadas[1], "ERROR: x", True)])
    assert t2.fin == "respuesta" and t2.texto.startswith("Listo.")
    hist = m.peticiones[1]["contents"]
    assert [c.role for c in hist] == ["user", "model", "user"]         # el turno del modelo se reenvía intacto
    partes = hist[2].parts
    assert partes[0].function_response.response == {"resultado": "filas…"} and partes[0].function_response.id == "x1"
    assert partes[1].function_response.response == {"error": "ERROR: x"} and partes[1].function_response.id is None


def test_el_texto_de_pensamiento_no_llega_a_la_respuesta():
    g, _ = _gemini([_resp([types.Part(text="pienso…", thought=True), types.Part(text="No consta.\nFORMA: NC")])])
    assert g.enviar("¿?").texto == "No consta.\nFORMA: NC"


@pytest.mark.parametrize("fin,esperado", [("MAX_TOKENS", "corte"), ("SAFETY", "rechazo"), ("STOP", "respuesta")])
def test_motivos_de_fin(fin, esperado):
    g, _ = _gemini([_resp([types.Part(text="x")], fin=fin)])
    assert g.enviar("¿?").fin == esperado


def test_una_llamada_mal_formada_se_pide_rehacer_una_vez():
    g, m = _gemini([_resp([], fin="MALFORMED_FUNCTION_CALL"), _resp([_llamada("buscar", {"nombre": "Cano"})])])
    t = g.enviar("¿?")
    assert t.fin == "herramientas" and t.tokens_entrada == 200
    assert "mal formada" in m.peticiones[1]["contents"][-1].parts[0].text


def test_cuota_agotada_se_reintenta():
    from google.genai.errors import ClientError
    err = ClientError(429, {"error": {"code": 429, "message": "cuota", "status": "RESOURCE_EXHAUSTED"}})
    g, m = _gemini([err, _resp([types.Part(text="ok")])])
    assert g.enviar("¿?").texto == "ok" and len(m.peticiones) == 2


def test_una_clave_invalida_no_se_reintenta():
    from google.genai.errors import ClientError
    err = ClientError(400, {"error": {"code": 400, "message": "API key not valid", "status": "INVALID_ARGUMENT"}})
    g, m = _gemini([err, _resp([types.Part(text="ok")])])
    with pytest.raises(ClientError):
        g.enviar("¿?")
    assert len(m.peticiones) == 1


def test_bucle_completo_del_agente_con_gemini_falso():
    """La respuesta del modelo cita literalmente lo que devolvió la herramienta → verificada."""
    g, _ = _gemini([_resp([_llamada("afirmaciones", {"entidad": "R-chuquitapa", "atributo": "ejerce-cargo",
                                                       "valor": ["coronel"]})]),
                    _resp([types.Part(text="Cano lo niega (A-UT11-004): «Comisionado por este y no coronel».\n"
                                           "FORMA: DISPUTA")])])
    g.iniciar = lambda *a: None                                    # ya iniciado con el cliente falso
    r = AG.preguntar("¿Fue coronel?", g)
    assert r.estado == "verificada" and r.forma == "DISPUTA" and r.pasos == 2


def test_cargar_env_no_pisa_variables_y_devuelve_solo_nombres(tmp_path, monkeypatch):
    f = tmp_path / ".env"
    f.write_text("# comentario\nLAAD_PRUEBA_A='uno'\nexport LAAD_PRUEBA_B=dos\nLAAD_PRUEBA_C=tres\n", encoding="utf-8")
    monkeypatch.setenv("LAAD_PRUEBA_C", "previa")
    monkeypatch.delenv("LAAD_PRUEBA_A", raising=False)
    monkeypatch.delenv("LAAD_PRUEBA_B", raising=False)
    assert proveedores.cargar_env(f) == ["LAAD_PRUEBA_A", "LAAD_PRUEBA_B"]
    assert os.environ["LAAD_PRUEBA_A"] == "uno" and os.environ["LAAD_PRUEBA_C"] == "previa"


def test_sin_clave_falla_con_mensaje_claro(monkeypatch):
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    with pytest.raises(EnvironmentError, match="GOOGLE_API_KEY"):
        Gemini().cliente
    with pytest.raises(ValueError):
        proveedores.crear("otro")


def test_llamada_sin_id_recibe_uno_local_que_no_se_envia():
    g, _ = _gemini([_resp([_llamada("buscar", {"nombre": "Cano"})])])
    t = g.enviar("¿?")
    assert t.llamadas[0].id.startswith("gemini-")
    assert isinstance(t.llamadas[0], Llamada)


def test_la_cuota_diaria_no_se_reintenta():
    from google.genai.errors import ClientError
    from laad.proveedores.gemini import CuotaDiaria
    err = ClientError(429, {"error": {"code": 429, "status": "RESOURCE_EXHAUSTED",
                                      "message": "quotaId GenerateRequestsPerDayPerProjectPerModel-FreeTier"}})
    g, m = _gemini([err, _resp([types.Part(text="ok")])])
    with pytest.raises(CuotaDiaria):
        g.enviar("¿?")
    assert len(m.peticiones) == 1
