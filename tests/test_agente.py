"""El bucle del agente (laad.agente) con un proveedor simulado: sin red, sin coste y sin modelo real.

Se comprueba la lógica que no depende del modelo: ejecutar las llamadas, devolver los errores al modelo, rechazar
citas inventadas, pedir una corrección y limitar los pasos."""
from laad import agente as AG
from laad.agente import Llamada, Turno


class Simulado:
    """Proveedor con turnos escritos de antemano. Guarda lo que el agente le envía."""
    nombre, modelo = "simulado", "guion"

    def __init__(self, turnos):
        self.turnos = list(turnos)
        self.enviados, self.devueltos, self.sistema, self.herramientas = [], [], None, None

    def iniciar(self, sistema, herramientas):
        self.sistema, self.herramientas = sistema, herramientas

    def _siguiente(self):
        t = self.turnos.pop(0)
        return t(self) if callable(t) else t

    def enviar(self, texto):
        self.enviados.append(texto)
        return self._siguiente()

    def devolver(self, resultados):
        self.devueltos.append(resultados)
        return self._siguiente()


def _llamar(*llamadas):
    return Turno("", [Llamada(f"c{i}", n, p) for i, (n, p) in enumerate(llamadas)], "herramientas", 10, 5)


def _responder(texto):
    return Turno(texto, [], "respuesta", 10, 5)


def _cita_de_coronel(prov):
    """Responde citando literalmente la negación de Cano que le devolvió la herramienta."""
    texto = prov.devueltos[-1][0].texto
    assert "Comisionado por este y no coronel" in texto
    return _responder("Isidro Cano lo niega en su declaración jurada (A-UT11-004): «Comisionado por este y no "
                      "coronel como expone en su certificación».\nFORMA: DISPUTA")


def test_el_agente_recibe_instrucciones_y_todas_las_herramientas():
    prov = Simulado([_responder("No consta.\nFORMA: NC")])
    AG.preguntar("¿Algo?", prov)
    assert "Solo sabes lo que te devuelven las herramientas" in prov.sistema
    nombres = {h["nombre"] for h in prov.herramientas}
    assert {"buscar", "afirmaciones"} <= nombres and "verificar" not in nombres
    assert all(h["parametros"]["type"] == "object" for h in prov.herramientas)


def test_respuesta_con_cita_literal_queda_verificada():
    prov = Simulado([_llamar(("afirmaciones", {"entidad": "R-chuquitapa", "atributo": "ejerce-cargo",
                                                "valor": ["coronel"]})),
                     _cita_de_coronel])
    r = AG.preguntar("¿Fue Chuquitapa coronel de Túpac Amaru?", prov)
    assert r.estado == "verificada" and r.verificada
    assert r.forma == "DISPUTA"
    assert "FORMA:" not in r.texto
    assert r.pasos == 2 and r.tokens_entrada == 20
    assert [x.herramienta for x in r.ejecucion.resultados] == ["afirmaciones"]


def test_una_cita_inventada_se_devuelve_para_corregir_y_luego_se_acepta():
    prov = Simulado([_llamar(("afirmaciones", {"entidad": "R-chuquitapa", "atributo": "ejerce-cargo",
                                                "valor": ["coronel"]})),
                     _responder("Cano dice «nunca fue coronel» (A-UT11-004).\nFORMA: DISPUTA"),
                     _responder("Cano lo niega (A-UT11-004): «Comisionado por este y no coronel».\nFORMA: DISPUTA")])
    r = AG.preguntar("¿Fue coronel?", prov)
    assert r.estado == "verificada"
    assert len(prov.enviados) == 2 and "nunca fue coronel" in prov.enviados[1]
    assert "verificación fallida: se pide corrección" in r.traza


def test_si_sigue_inventando_se_entrega_marcada_como_no_verificada():
    prov = Simulado([_responder("Dice «texto inventado».\nFORMA: A"), _responder("Dice «otro inventado».\nFORMA: A")])
    r = AG.preguntar("¿Algo?", prov)
    assert r.estado == "no verificada" and not r.verificada
    assert r.verificacion["citas"] == ["otro inventado"]


def test_un_id_de_afirmacion_inventado_tambien_se_rechaza():
    prov = Simulado([_responder("Lo afirma A-UT99-999.\nFORMA: A"), _responder("No consta.\nFORMA: NC")])
    r = AG.preguntar("¿Algo?", prov)
    assert r.estado == "verificada" and "A-UT99-999" in prov.enviados[1]


def test_un_parametro_invalido_vuelve_al_modelo_como_error_y_no_rompe_el_bucle():
    prov = Simulado([_llamar(("afirmaciones", {"entidad": "Chuquitapa"})),
                     _llamar(("herramienta_que_no_existe", {})),
                     _responder("No pude consultarlo.\nFORMA: NC")])
    r = AG.preguntar("¿Algo?", prov)
    errores = [res for lote in prov.devueltos for res in lote]
    assert all(e.es_error and e.texto.startswith("ERROR:") for e in errores)
    assert "buscar" in errores[0].texto                    # el mensaje le dice cómo corregirse
    assert len(r.ejecucion.errores) == 2 and r.ejecucion.resultados == []


def test_varias_llamadas_de_un_turno_se_devuelven_juntas():
    prov = Simulado([_llamar(("buscar", {"nombre": "Chuquitapa"}), ("buscar", {"nombre": "Huancachoque"})),
                     _responder("Hay candidatos para ambos.\nFORMA: R")])
    AG.preguntar("¿Quiénes son?", prov)
    assert len(prov.devueltos) == 1 and len(prov.devueltos[0]) == 2


def test_limite_de_pasos():
    prov = Simulado([_llamar(("vocabulario", {"esquema": "atributos"}))] * 5)
    r = AG.preguntar("¿Algo?", prov, max_pasos=3)
    assert r.estado == "límite de pasos" and r.pasos == 3


def test_rechazo_del_modelo():
    r = AG.preguntar("¿Algo?", Simulado([Turno("", [], "rechazo")]))
    assert r.estado == "rechazo" and not r.verificada


def test_forma_declarada():
    assert AG.forma_declarada("texto\nFORMA: NC") == "NC"
    assert AG.forma_declarada("texto sin forma") is None
    assert AG.forma_declarada("FORMA: A\n…\nFORMA: DISPUTA") == "DISPUTA"
