"""Anotación del expediente, lote C: tramos UT15, UT16.a, UT16.b, UT17, UT18, UT19 y UT20.

Completa lo que el hilo central (hilo_central.py) no anotó en esos tramos: menciones de todas las personas, grupos,
lugares y cosas; participantes procesales de cada pieza (firmante, destinatario, fedatario, notificado, testigos);
y afirmaciones (condiciones, cargos, calificaciones de conducta, hechos narrados, órdenes, solicitudes, dictamen y
auto). Mismo esquema plano y mismas convenciones que hilo_central.py. Ordinales 801–999 en cada tramo.
Las ocurrencias ya anotadas en hilo_central se reutilizan por su id (nunca se duplican).
El final de UT20 (P32, notario Matías Ugarte) es ajeno al expediente: solo se anotan sus participantes y no se
relaciona con la causa de 1806.

Anotador: Claude Opus 5.5, 2026-11-13. Lote: anotacion-expediente-c-v1.
Ejecutar: python datos/registros/expediente_c.py  -> escribe expediente_c.jsonl
"""
import json
from pathlib import Path

M = []  # menciones
A = []  # afirmaciones


def m(id, tramo, pieza, clase, texto, cita, rol=None, tipo=None):
    M.append(dict(tipo_registro="mencion", id=id, tramo=tramo, pieza=pieza, clase=clase, texto=texto,
                  rol_en_pieza=rol, tipo_entidad=tipo, cita=cita))


def a(id, tramo, pieza, afirmante, rol_afirmante, sujeto, atributo, valor, cita, polaridad="afirma",
      fundamento="no-indica", rol_en_hecho=None, nota=None, responde_a=None, segun=None, otra=False,
      distribuida=False):
    A.append(dict(tipo_registro="afirmacion", id=id, tramo=tramo, pieza=pieza, afirmante=afirmante,
                  rol_afirmante=rol_afirmante, sujeto=sujeto, atributo=atributo, valor=valor,
                  rol_en_hecho=rol_en_hecho, polaridad=polaridad, fundamento=fundamento, cita=cita,
                  responde_a=responde_a, segun=segun, afirmante_de_otra_pieza=otra, distribuida=distribuida,
                  nota=nota))


# ───────────── P21 · Final de la declaración de Fernando Orue · UT15 ─────────────
# Ya anotadas: M-UT15-001 (Chiquitas), M-UT15-002 (chuquitapa); declarante M-UT14-001; juez M-UT14-004.
m("M-UT15-801", "UT15", "P21", "persona", "el declarante", "q el declarante no queria certificar ni meterse en nada", rol="declarante")
m("M-UT15-802", "UT15", "P21", "persona", "la mujer de Chiquitas", "pero que la mujer de Chiquitas habla contra el que declara")
m("M-UT15-803", "UT15", "P21", "persona", "guancachay", "motivo a decirle a guancachay q pusiera en la certificaz")
m("M-UT15-804", "UT15", "P21", "persona", "un hijo suyo", "sino mando que un hijo suyo lo hicieron")
m("M-UT15-805", "UT15", "P21", "persona", "su mujer", "ni de boca tan mordaz como la spa su mujer")
m("M-UT15-806", "UT15", "P21", "persona", "conmigo", "y lo firmo juntamente conmigo y testigos de mi asistencia", rol="firmante")
m("M-UT15-807", "UT15", "P21", "grupo", "testigos de mi asistencia", "juntamente conmigo y testigos de mi asistencia a falta de escribano",
  rol="testigo-de-asistencia")
m("M-UT15-808", "UT15", "P21", "cosa", "la certificaz", "q pusiera en la certificaz lo q quisiese")

a("A-UT15-801", "UT15", "P21", "M-UT14-001", "declarante", {"pieza": "P21"},
  "ratifica-contenido", {"mencion": "M-UT14-001"}, "y ratifica dijo ser verdad",
  nota="Ratificación de la propia declaración leída «de principio a fin» (final de UT14).")
a("A-UT15-802", "UT15", "P21", "M-UT14-001", "declarante", {"mencion": "M-UT14-001"},
  "edad", {"literal": "treinta y quatro años"}, "dijo ser verdad de treinta y quatro años")
a("A-UT15-803", "UT15", "P21", "M-UT14-001", "declarante", {"mencion": "M-UT14-001"},
  "generales-de-la-ley", {"literal": "le compredenden los grales de la ley"}, "q no le compredenden los grales de la ley",
  polaridad="niega")
a("A-UT15-804", "UT15", "P21", "M-UT14-001", "declarante", {"mencion": "M-UT15-801"},
  "dijo", {"literal": "no queria certificar ni meterse en nada"}, "q el declarante no queria certificar ni meterse en nada")
a("A-UT15-805", "UT15", "P21", "M-UT14-001", "declarante", {"mencion": "M-UT15-802"},
  "calificacion-de-conducta", {"literal": "habla contra el que declara y su familia"},
  "la mujer de Chiquitas habla contra el que declara y su familia")
a("A-UT15-806", "UT15", "P21", "M-UT14-001", "declarante", {"pieza": "P04"},
  "redacto", {"mencion": "M-UT15-803"}, "motivo a decirle a guancachay q pusiera en la certificaz lo q quisiese",
  nota="Orue dice que autorizó a «guancachay» a poner en la certificación lo que quisiese; se registra como redacción "
       "atribuida (cf. A-UT14-002 «un hijo suyo» y A-UT14-003 en la misma declaración).")
a("A-UT15-807", "UT15", "P21", "M-UT14-001", "declarante", {"pieza": "P04"},
  "firmo", {"mencion": "M-UT14-001"}, "q el lo firmaria aunque no lo hise", polaridad="niega",
  nota="Ofreció firmarla pero niega haberlo hecho; la firma la atribuye a un hijo suyo (A-UT15-002).")
a("A-UT15-808", "UT15", "P21", "M-UT14-001", "declarante", {"pieza": "P04"},
  "firmo", {"mencion": "M-UT15-804"}, "aunque no lo hise sino mando que un hijo suyo lo hicieron",
  nota="Misma afirmación que A-UT15-002 (valor literal), aquí con valor mención para poder responder «quién firmó».")
a("A-UT15-809", "UT15", "P21", "M-UT14-001", "declarante", {"mencion": "M-UT15-805"},
  "calificacion-de-conducta", {"literal": "de boca tan mordaz"}, "que chuquitapa no es tan malo ni de boca tan mordaz como la spa su mujer",
  nota="Calificación comparativa: la mujer de Chuquitapa es más mordaz que él. «la spa» es lectura dudosa de la transcripción.")
a("A-UT15-811", "UT15", "P21", "M-UT14-004", "fedatario", {"pieza": "P21"},
  "firmo", {"mencion": "M-UT15-801"}, "y lo firmo juntamente conmigo y testigos de mi asistencia",
  nota="El sujeto de «lo firmo» es elíptico en el texto (el declarante); contrasta con «no obstante que sabe firmar el "
       "declarante no quiso hacerlo» (UT14, A-UT14-001), que el hilo central refiere a la certificación P04.")
a("A-UT15-812", "UT15", "P21", "M-UT14-004", "fedatario", {"pieza": "P21"},
  "firmo", {"mencion": "M-UT15-806"}, "y lo firmo juntamente conmigo y testigos de mi asistencia a falta de escribano",
  nota="El juez comisionado actúa con testigos de asistencia «a falta de escribano».")

# ───────────── P22 · Oficio del subdelegado al cura interino (24 de septiembre) · UT15 ─────────────
# Ya anotada: M-UT15-003 (parroco interino, destinatario).
m("M-UT15-809", "UT15", "P22", "persona", "Rey", "y al mejor servicio del Rey el que me expnga")
m("M-UT15-810", "UT15", "P22", "lugar", "este pueblo", "que ha tenido en este pueblo Manuel Guancachoque", tipo="pueblo")
m("M-UT15-811", "UT15", "P22", "persona", "Manuel Guancachoque", "en este pueblo Manuel Guancachoque Oriundo de el")
m("M-UT15-812", "UT15", "P22", "lugar", "esta doctrina", "como parroco interino de esta doctrina", tipo="doctrina")
m("M-UT15-813", "UT15", "P22", "persona", "el señor cura propietario", "por hallarse ausente el señor cura propietario de ella")
m("M-UT15-814", "UT15", "P22", "persona", "el Doctor Don Antonio Valdes", "en compañía de su tio el Doctor Don Antonio Valdes")
m("M-UT15-815", "UT15", "P22", "persona", "pedro de Mata", "setiembre 24 de 1806 pedro de Mata[Firma]", rol="firmante")

a("A-UT15-813", "UT15", "P22", "M-UT15-815", "resolutor", {"mencion": "M-UT15-003"},
  "solicita", {"literal": "exponerme a continuacion lo que separa y le conste"},
  "se hade servir exponerme a continuacion lo que separa y le conste como parroco interino de esta doctrina",
  nota="Petición de informe sobre la conducta y manejo de Guancachoque; el afirmante es el firmante del oficio.")
a("A-UT15-814", "UT15", "P22", "M-UT15-815", "resolutor", {"mencion": "M-UT15-811"},
  "tiene-condicion", {"literal": "Oriundo de el"}, "en este pueblo Manuel Guancachoque Oriundo de el",
  nota="«Oriundo» (natural del pueblo) no equivale con seguridad a la condición fiscal «originario»; se deja literal.")
a("A-UT15-815", "UT15", "P22", "M-UT15-815", "resolutor", {"mencion": "M-UT15-003"},
  "ejerce-cargo", {"concepto": "cura-interino"}, "le conste como parroco interino de esta doctrina")
a("A-UT15-816", "UT15", "P22", "M-UT15-815", "resolutor", {"mencion": "M-UT15-813"},
  "ejerce-cargo", {"concepto": "cura-propio"}, "por hallarse ausente el señor cura propietario de ella")
a("A-UT15-817", "UT15", "P22", "M-UT15-815", "resolutor", {"mencion": "M-UT15-813"},
  "se-hallaba", {"literal": "ausente"}, "por hallarse ausente el señor cura propietario de ella", polaridad="niega",
  nota="«ausente»: no se hallaba en la doctrina.")
a("A-UT15-818", "UT15", "P22", "M-UT15-815", "resolutor", {"mencion": "M-UT15-003"},
  "parentesco", {"mencion": "M-UT15-814"}, "pues aunque interino ha venido en compañía de su tio el Doctor Don Antonio Valdes",
  nota="Tipo de parentesco escrito: «tio». El texto distingue a Antonio Valdes (tío) del cura interino (ver N7).")

# ───────────── P23 · Informe del cura interino (fechado 26 de noviembre) · UT16.a–UT16.b ─────────────
# Ya anotadas: M-UT16a-001..004, M-UT16b-001. Afirmante: M-UT15-003 (NOTA_CURA del hilo central).
NOTA_CURA = ("El informe no lleva nombre en la transcripción; el afirmante es la mención del destinatario del oficio P22 "
             "(«parroco interino»). El informe de Mata (P27) lo atribuye a «Doctor Don Agustin Valdes».")
m("M-UT16a-801", "UT16.a", "P23", "persona", "Manuel Guancachoque", "sobre las operaciones de Manuel Guancachoque debo decir")
m("M-UT16a-802", "UT16.a", "P23", "lugar", "esta Doctrina", "y descanso comun de esta Doctrina", tipo="doctrina")
m("M-UT16a-803", "UT16.a", "P23", "persona", "vuestra", "para que quede vuestra inteligencia contratante", rol="destinatario")
m("M-UT16a-804", "UT16.a", "P23", "persona", "dicho Guancachoque", "las Ofensas codiciosas y altaneras d dicho Guancachoque")
m("M-UT16a-805", "UT16.a", "P23", "persona", "el padre", "pues lo que haria el padre hiso este")
m("M-UT16a-806", "UT16.a", "P23", "persona", "su propio madre", "ponerñle hermanos a su propio madre")
m("M-UT16a-807", "UT16.a", "P23", "persona", "su natural madre", "andas fecundas de su natural madre")
m("M-UT16a-808", "UT16.a", "P23", "persona", "vuestra", "hallandose vuestra presente en este pueblo")
m("M-UT16a-809", "UT16.a", "P23", "lugar", "este pueblo", "vuestra presente en este pueblo , como juegos Real", tipo="pueblo")
m("M-UT16a-810", "UT16.a", "P23", "persona", "el señor Agustin Fiscal Don Althamacio Zotelo",
  "como juegos Real y el señor Agustin Fiscal Don Althamacio Zotelo")
m("M-UT16b-801", "UT16.b", "P23", "persona", "su casique", "el rio que a tomado a su casique complacable")
m("M-UT16b-802", "UT16.b", "P23", "grupo", "sus confidencias", "aduciendo a sus confidencias y los demas ayllu")
m("M-UT16b-803", "UT16.b", "P23", "grupo", "los demas ayllu", "a sus confidencias y los demas ayllu a hacer efectiva", tipo="ayllu")
m("M-UT16b-804", "UT16.b", "P23", "persona", "su casique", "en la ruina de bien de su casique")
m("M-UT16b-805", "UT16.b", "P23", "lugar", "el partido", "vuestro vien conoce el partido nos hallamos", tipo="partido")
m("M-UT16b-806", "UT16.b", "P23", "persona", "un insurgente", "el trabajo de un insurgente")
m("M-UT16b-807", "UT16.b", "P23", "persona", "vuestro Condorcanqui", "de la chispa de vuestro Condorcanqui")
m("M-UT16b-808", "UT16.b", "P23", "lugar", "la America meridional", "a trasar casi toda la America meridional")
m("M-UT16b-809", "UT16.b", "P23", "persona", "Maldonado Ortiz", "la aminocidad y altenencia de Maldonado Ortiz a las Guamcachoque")
m("M-UT16b-810", "UT16.b", "P23", "persona", "Guamcachoque", "altenencia de Maldonado Ortiz a las Guamcachoque Es quanto")
m("M-UT16b-811", "UT16.b", "P23", "persona", "Guancachoque", "en las operaciones de Guancachoque y que le pueda exponer")
m("M-UT16b-812", "UT16.b", "P23", "grupo", "aquel Regio sonado", "que le pueda exponer a aquel Regio sonado nodudando")
m("M-UT16b-813", "UT16.b", "P23", "persona", "Ortis", "representaciones o diosas de Ortis o Guancachoque")
m("M-UT16b-814", "UT16.b", "P23", "persona", "Guancachoque", "o diosas de Ortis o Guancachoque Dios que a vuestro")
m("M-UT16b-815", "UT16.b", "P23", "persona", "Firma", "Dios que a vuestro muchos años Firma Noviembre 26 de 1806", rol="firmante")

kw = dict(nota=NOTA_CURA, otra=True)
a("A-UT16a-801", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-004"},
  "tiene-condicion", {"concepto": "indio"}, "su Madre Agustina Falcon India Ordinaria y pleveya", fundamento="notoriedad", **kw)
a("A-UT16a-802", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-004"},
  "tiene-condicion", {"concepto": "ordinario"}, "su Madre Agustina Falcon India Ordinaria y pleveya", fundamento="notoriedad", **kw)
a("A-UT16a-803", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-001"},
  "tiene-condicion", {"concepto": "hijo-espurio"}, "Es notorio que Manuel Guancachoque es hijo Espurio", fundamento="notoriedad", **kw)
a("A-UT16a-804", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-804"},
  "calificacion-de-conducta", {"literal": "Ofensas codiciosas y altaneras"},
  "las Ofensas codiciosas y altaneras d dicho Guancachoque en todo an sido , sino inguales aun mayores", **kw)
a("A-UT16a-805", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-804"},
  "participa-en-hecho", {"hecho": "H-p23-maltrato-madre"},
  "tuvo valor de ponerñle hermanos a su propio madre de tal modo , que la estropio e inhabilito por bastante tiempo",
  rol_en_hecho="agresor",
  nota="Sujeto elíptico (el texto sigue tratando de «dicho Guancachoque»). «ponerñle hermanos» se lee probablemente "
       "como «ponerle las manos» (lectura dudosa de la transcripción). " + NOTA_CURA, otra=True)
a("A-UT16a-806", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-806"},
  "participa-en-hecho", {"hecho": "H-p23-maltrato-madre"}, "a su propio madre de tal modo , que la estropio e inhabilito por bastante tiempo",
  rol_en_hecho="victima", **kw)
a("A-UT16a-807", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-804"},
  "calificacion-de-conducta", {"literal": "suspivas , altanero"}, "El es suspivas , altanero",
  nota="Sujeto «El» = dicho Guancachoque. " + NOTA_CURA, otra=True)
a("A-UT16a-808", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-804"},
  "calificacion-de-conducta",
  {"literal": "ni el sagrado de personas , ni los que se hallaban autorizados con la justicia ordinaria han estado libres de que , les ponga las manos violentas"},
  "sus ajustimientos han sido grandes que ni el sagrado de personas , ni los que se hallaban autorizados con la justicia ordinaria han estado libres de que , les ponga las manos violentas",
  nota="«sus» = dicho Guancachoque. " + NOTA_CURA, otra=True)
a("A-UT16a-809", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-804"},
  "calificacion-de-conducta", {"literal": "aquel audaz dispuesto que tiene para todo"},
  "con aquel audaz dispuesto que tiene para todo", **kw)
a("A-UT16a-810", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-804"},
  "participa-en-hecho", {"hecho": "H-p23-escandalo"}, "aquel hecho escandaloso que ocasiono", rol_en_hecho="agresor",
  nota="Sujeto elíptico (dicho Guancachoque). El hecho continúa en UT16.b: «osadia que acometen a su casique y alcalde "
       "mayor Don Andres Chuquitapa». " + NOTA_CURA, otra=True)
a("A-UT16a-811", "UT16.a", "P23", "M-UT15-003", "informante", {"hecho": "H-p23-escandalo"},
  "lugar-del-hecho", {"mencion": "M-UT16a-809"}, "aquel hecho escandaloso que ocasiono, hallandose vuestra presente en este pueblo", **kw)
a("A-UT16a-812", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-808"},
  "se-hallaba", {"literal": "presente en este pueblo"}, "hallandose vuestra presente en este pueblo",
  fundamento="no-indica", **kw)
a("A-UT16a-813", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-810"},
  "se-hallaba", {"literal": "presente en este pueblo"},
  "hallandose vuestra presente en este pueblo , como juegos Real y el señor Agustin Fiscal Don Althamacio Zotelo",
  nota="Pasaje defectuoso («como juegos Real y el señor Agustin Fiscal»); quizá «como Juez Real y el señor Agente Fiscal». "
       "No se asigna cargo. " + NOTA_CURA, otra=True)
a("A-UT16b-801", "UT16.b", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16b-001"},
  "participa-en-hecho", {"hecho": "H-p23-escandalo"}, "osadia que acometen a su casique y alcalde mayor Don Andres Chuquitapa",
  rol_en_hecho="victima", **kw)
a("A-UT16b-802", "UT16.b", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16b-811"},
  "calificacion-de-conducta", {"literal": "no conoce el patron que le reduzca el rebaño ni oye mija ni menos cumple con los propocitos de su magestad"},
  "el no conoce el patron que le reduzca el rebaño ni oye mija ni menos cumple con los propocitos de su magestad",
  nota="Sujeto «el» = Guancachoque (mención posterior en el mismo tramo). «oye mija» se lee probablemente «oye misa». " + NOTA_CURA,
  otra=True)
a("A-UT16b-803", "UT16.b", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16b-811"},
  "calificacion-de-conducta", {"literal": "su corazon duro y obstinado"}, "por tomar su corazon duro y obstinado", **kw)
a("A-UT16b-804", "UT16.b", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16b-811"},
  "motivo", {"literal": "por tomar venganza"},
  "luego me hace crecer que por tomar venganza con un indio talvez padezca en este pueblo algun indio",
  nota="Temor del informante (no un hecho ocurrido). " + NOTA_CURA, otra=True)
a("A-UT16b-805", "UT16.b", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16b-802"},
  "participa-en-hecho", {"hecho": "H-p23-confabulacion"},
  "el no se cansa en estas aduciendo a sus confidencias y los demas ayllu a hacer efectiva sus miras en la ruina de bien de su casique",
  rol_en_hecho="participante-en-hecho", **kw)
a("A-UT16b-806", "UT16.b", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16b-811"},
  "participa-en-hecho", {"hecho": "H-p23-confabulacion"},
  "el no se cansa en estas aduciendo a sus confidencias y los demas ayllu", rol_en_hecho="instigador",
  nota="Sujeto «el» = Guancachoque. " + NOTA_CURA, otra=True)
a("A-UT16b-807", "UT16.b", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16b-804"},
  "participa-en-hecho", {"hecho": "H-p23-confabulacion"}, "a hacer efectiva sus miras en la ruina de bien de su casique",
  rol_en_hecho="victima", **kw)
a("A-UT16b-808", "UT16.b", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16b-806"},
  "participa-en-hecho", {"hecho": "H-p23-rebelion"}, "el partido nos hallamos que fue en otro tiempo el trabajo de un insurgente",
  rol_en_hecho="instigador", fundamento="notoriedad", **kw)
a("A-UT16b-809", "UT16.b", "P23", "M-UT15-003", "informante", {"hecho": "H-p23-rebelion"},
  "lugar-del-hecho", {"mencion": "M-UT16b-805"}, "vuestro vien conoce el partido nos hallamos que fue en otro tiempo el trabajo de un insurgente",
  fundamento="notoriedad", **kw)
a("A-UT16b-810", "UT16.b", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16b-809"},
  "calificacion-de-conducta", {"literal": "aminocidad y altenencia"}, "se sugente la aminocidad y altenencia de Maldonado Ortiz a las Guamcachoque",
  nota="«Maldonado Ortiz a las Guamcachoque» parece designar al denunciante por el apellido del padre (cf. «Ortis o Guancachoque»); "
       "la identidad es cuestión de capa 4. " + NOTA_CURA, otra=True)
a("A-UT16b-811", "UT16.b", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-803"},
  "solicita", {"literal": "se tome la rienda y se sugente la aminocidad y altenencia"},
  "por lo que me parece se tome la rienda y se sugente la aminocidad y altenencia de Maldonado Ortiz", **kw)
a("A-UT16b-812", "UT16.b", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-803"},
  "solicita", {"literal": "queda sancionado en las operaciones de Guancachoque"},
  "a fin de que queda sancionado en las operaciones de Guancachoque", **kw)

# ───────────── P24 · Decreto: se espera a Juan Cazorla · UT17 ─────────────
# Ya anotadas: M-UT17-001 (Juan Cazorla), M-UT17-002 (Don Juan Quiñones), M-UT17-003 ([María Rubrica], firmante).
m("M-UT17-801", "UT17", "P24", "lugar", "este pueblo", "Respecto a hallarse ausente de este pueblo Juan Cazorla", tipo="pueblo")
m("M-UT17-802", "UT17", "P24", "cosa", "la Certificación", "de quien aparece firmada la Certificación a folios 2")
m("M-UT17-803", "UT17", "P24", "lugar", "el pueblo de Tinta", "que no hay tal hombre en el pueblo de Tinta esperece", tipo="pueblo")

a("A-UT17-801", "UT17", "P24", "M-UT17-003", "resolutor", {"mencion": "M-UT17-001"},
  "se-hallaba", {"literal": "ausente de este pueblo"}, "Respecto a hallarse ausente de este pueblo Juan Cazorla", polaridad="niega")
a("A-UT17-802", "UT17", "P24", "M-UT17-003", "resolutor", {"mencion": "M-UT17-002"},
  "ejerce-cargo", {"concepto": "teniente-alguacil"}, "extendida a nombre del teniente Alguacil Don Juan Quiñones",
  nota="El mismo decreto niega a continuación que exista tal hombre en Tinta (A-UT17-002): el cargo es el que consta en la certificación.")
a("A-UT17-803", "UT17", "P24", "M-UT17-003", "resolutor", {"mencion": "M-UT17-001"},
  "ordena", {"literal": "esperece su llegada para recibirle la declaración Respectiva sobre el Asunto"},
  "esperece su llegada para recibirle la declaración Respectiva sobre el Asunto",
  nota="Orden sin destinatario expreso; el sujeto es la persona afectada (Juan Cazorla).")

# ───────────── P25 · Decreto de remisión al Presidente (Sicuani, 8 de noviembre) · UT17 ─────────────
m("M-UT17-804", "UT17", "P25", "lugar", "Sicuani", "Sicuani Noviembre 8 de 1806 No habiendo", tipo="pueblo")
m("M-UT17-805", "UT17", "P25", "lugar", "pueblo de Tinta", "hasta esa fecha al pueblo de Tinta Juan Cazorla", tipo="pueblo")
m("M-UT17-806", "UT17", "P25", "persona", "Juan Cazorla", "al pueblo de Tinta Juan Cazorla que suscribió el documento")
m("M-UT17-807", "UT17", "P25", "cosa", "el documento de 2 fojas", "que suscribió el documento de 2 fojas de este expediente")
m("M-UT17-808", "UT17", "P25", "cosa", "el correspondiente Informe", "diríjase con lo actuado y el correspondiente Informe")
m("M-UT17-809", "UT17", "P25", "persona", "Muy Ilustrísima Señor Padre", "al Muy Ilustrísima Señor Padre para su determinación",
  rol="destinatario")
m("M-UT17-810", "UT17", "P25", "persona", "María Rubrica", "para su determinación [María Rubrica]", rol="firmante")

a("A-UT17-804", "UT17", "P25", "M-UT17-810", "resolutor", {"mencion": "M-UT17-806"},
  "se-hallaba", {"literal": "comparecido ... al pueblo de Tinta"},
  "No habiendo comparecido mi regresado hasta esa fecha al pueblo de Tinta Juan Cazorla", polaridad="niega",
  nota="Firmante transcrito como «[María Rubrica]», igual que en P24 (probablemente la rúbrica de Mata; inferencia, N5).")
a("A-UT17-805", "UT17", "P25", "M-UT17-810", "resolutor", {"pieza": "P03"},
  "firmo", {"mencion": "M-UT17-806"}, "Juan Cazorla que suscribió el documento de 2 fojas de este expediente",
  nota="«el documento de 2 fojas» se identifica con la certificación «a folios 2» de P24, es decir P03.")
a("A-UT17-806", "UT17", "P25", "M-UT17-810", "resolutor", {"mencion": "M-UT17-809"},
  "ordena", {"literal": "diríjase con lo actuado y el correspondiente Informe al Muy Ilustrísima Señor Padre para su determinación"},
  "diríjase con lo actuado y el correspondiente Informe al Muy Ilustrísima Señor Padre para su determinación",
  nota="Orden impersonal («diríjase»); el sujeto es el destinatario de la remisión (el Presidente). «Padre» es lectura de la "
       "transcripción, probablemente por «Presidente».")

# ───────────── P26 · Decreto de vista al fiscal (Cuzco, 18 de noviembre) · UT17 ─────────────
m("M-UT17-811", "UT17", "P26", "lugar", "Cuzco", "Cuzco noviembre 18 de noviembre de 1806 vista", tipo="ciudad")
m("M-UT17-812", "UT17", "P26", "persona", "señor", "de 1806 vista al señor Señor Capitan", rol="destinatario")
# Sin firmante ni autor escrito: no se crea afirmación de orden (no hay afirmante en la pieza).

# ───────────── P27 · Informe del subdelegado Pedro de la Mata (8 de noviembre) · UT17–UT18 ─────────────
# Ya anotadas: M-UT17-004..007, M-UT18-001 (Pedro de la Mata, informante), M-UT18-002 (Agustin Valdes).
m("M-UT17-813", "UT17", "P27", "persona", "Señor Capitan General", "vista al señor Señor Capitan General Habiendo evacuarlo",
  rol="destinatario")
m("M-UT17-814", "UT17", "P27", "lugar", "el pueblo de Tinta", "Habiendo evacuarlo en el pueblo de Tinta las diligencias", tipo="pueblo")
m("M-UT17-815", "UT17", "P27", "persona", "Vuestro señorío Muy Ilustre", "el oficio y Decreto de Vuestro señorío Muy Ilustre de 27 de Agosto")
m("M-UT17-816", "UT17", "P27", "cosa", "los Documentos", "Resulta de ellas que los Documentos que presento Manuel Guancachoque")
m("M-UT17-817", "UT17", "P27", "grupo", "Parcialidad", "sobre el bullicio, y asonada de Parcialidad", tipo="parcialidad")
m("M-UT17-818", "UT17", "P27", "lugar", "Derechos Pueblo", "a ver sucedido en Derechos Pueblo de Resultar", tipo="pueblo")
m("M-UT17-819", "UT17", "P27", "grupo", "Tinta", "de los Ayllus Tinta y Ucho Don Andres", tipo="ayllu")
m("M-UT17-820", "UT17", "P27", "grupo", "los sujetos", "haciéndolos firmar a los sujetos que los subscriben")
m("M-UT17-821", "UT17", "P27", "persona", "Vuestra Señoría muy Ilustrísima", "la justificación de Vuestra Señoría muy Ilustrísima")
m("M-UT17-822", "UT17", "P27", "lugar", "la casa en donde estabamos matriculando", "una tarde en la casa en donde estabamos matriculando a los indios",
  tipo="edificio")
m("M-UT17-823", "UT17", "P27", "grupo", "los indios", "estabamos matriculando a los indios el revisitador")
m("M-UT17-824", "UT17", "P27", "persona", "el revisitador", "matriculando a los indios el revisitador , y Yo")
m("M-UT17-825", "UT17", "P27", "persona", "Yo", "el revisitador , y Yo, concluida el dia anterior")
m("M-UT17-826", "UT17", "P27", "grupo", "Ayllos Tinta", "la numeración de los Ayllos Tinta, y Ucho que presencio", tipo="ayllu")
m("M-UT17-827", "UT17", "P27", "grupo", "Ucho", "los Ayllos Tinta, y Ucho que presencio", tipo="ayllu")
m("M-UT17-828", "UT17", "P27", "persona", "el mismo denunciador Guancachoque", "que presencio el mismo denunciador Guancachoque tubo el atrevimiento")
m("M-UT17-829", "UT17", "P27", "persona", "Recaudador", "tubo el atrevimiento de insultar al Recaudador con palabras injuriosas")
m("M-UT17-830", "UT17", "P27", "grupo", "los Alcaldes", "lo que visto por los Alcaldes.")
m("M-UT18-801", "UT18", "P27", "grupo", "Segundas, y Principales", "Segundas, y Principales de los citados Ayllus de Chuquitapa")
m("M-UT18-802", "UT18", "P27", "grupo", "los citados Ayllus", "Principales de los citados Ayllus de Chuquitapa acometieron", tipo="ayllu")
m("M-UT18-803", "UT18", "P27", "persona", "Chuquitapa", "de los citados Ayllus de Chuquitapa acometieron contra el")
m("M-UT18-804", "UT18", "P27", "persona", "indio", "si yo no salgo al indio lo hubieran en tropeado")
m("M-UT18-805", "UT18", "P27", "lugar", "mi misma casa", "insulto, y atropellamiento, en mi misma casa, lo mande llevar", tipo="edificio")
m("M-UT18-806", "UT18", "P27", "lugar", "la cárcel", "lo mande llevar a la cárcel , y que lo guardasen", tipo="carcel")
m("M-UT18-807", "UT18", "P27", "persona", "Chuquitapa", "de agravios inferidos por Chuquitapa a nombre del común")
m("M-UT18-808", "UT18", "P27", "grupo", "común y Principales", "a nombre del común y Principales de los citados Ayllos Tinta y Ucho")
m("M-UT18-809", "UT18", "P27", "grupo", "Ayllos Tinta", "de los citados Ayllos Tinta y Ucho en la que", tipo="ayllu")
m("M-UT18-810", "UT18", "P27", "grupo", "Ucho", "citados Ayllos Tinta y Ucho en la que lo convencieron", tipo="ayllu")
m("M-UT18-811", "UT18", "P27", "grupo", "todos los Indios", "conmover y sublevar a todos los Indios contra su recaudador")
m("M-UT18-812", "UT18", "P27", "persona", "su recaudador", "todos los Indios contra su recaudador del que no tenían queja")
m("M-UT18-813", "UT18", "P27", "lugar", "dicho -Pueblo", "cura interino de dicho -Pueblo Doctor", tipo="pueblo")
m("M-UT18-814", "UT18", "P27", "persona", "su feligrés Guancachoque", "la conducta y manejo de su feligrés Guancachoque")
m("M-UT18-815", "UT18", "P27", "persona", "Vuestro Señoría Muy Ilustre", "se inteligenciara Vuestro Señoría Muy Ilustre de la pésima")
m("M-UT18-816", "UT18", "P27", "lugar", "aquel Pueblo", "esta expuesto aquel Pueblo( en el que aun puede", tipo="pueblo")
m("M-UT18-817", "UT18", "P27", "persona", "Guancachoque", "Chispa soplada por Guancachoque que perjudicque")
m("M-UT18-818", "UT18", "P27", "lugar", "partido de mi cargo", "la tranquilidad publica del partido de mi cargo", tipo="partido")
m("M-UT18-819", "UT18", "P27", "lugar", "Siquani", "muchos años Siquani Noviembre 8 de 1806", tipo="pueblo")
m("M-UT18-820", "UT18", "P27", "persona", "Don Francisco Muñoz y Señor Clemente",
  "Muy Ylustre Señor presidente Don Francisco Muñoz y Señor Clemente", rol="destinatario")

a("A-UT17-807", "UT17", "P27", "M-UT18-001", "informante", {"mencion": "M-UT17-828"},
  "participa-en-hecho", {"hecho": "H-p27-insulto"},
  "el mismo denunciador Guancachoque tubo el atrevimiento de insultar al Recaudador con palabras injuriosas, y de manos",
  rol_en_hecho="agresor", fundamento="experiencia-propia",
  nota="Ocurrió en casa del informante, que estaba presente («estabamos matriculando… el revisitador, y Yo»).")
a("A-UT17-808", "UT17", "P27", "M-UT18-001", "informante", {"mencion": "M-UT17-829"},
  "participa-en-hecho", {"hecho": "H-p27-insulto"}, "insultar al Recaudador con palabras injuriosas, y de manos",
  rol_en_hecho="victima", fundamento="experiencia-propia")
a("A-UT17-809", "UT17", "P27", "M-UT18-001", "informante", {"hecho": "H-p27-insulto"},
  "lugar-del-hecho", {"mencion": "M-UT17-822"}, "una tarde en la casa en donde estabamos matriculando a los indios",
  fundamento="experiencia-propia")
a("A-UT17-810", "UT17", "P27", "M-UT18-001", "informante", {"hecho": "H-p27-insulto"},
  "fecha-del-hecho", {"literal": "una tarde"}, "Lo que hay de cierto en el asunto es; que una tarde en la casa",
  fundamento="experiencia-propia", responde_a="A-UT06-002",
  nota="Frente a «a las nueve de la noche» del escrito de Huancachoque (P06): Mata da otra versión del origen del conflicto (H6).")
a("A-UT17-811", "UT17", "P27", "M-UT18-001", "informante", {"hecho": "H-p27-insulto"},
  "fecha-del-hecho", {"literal": "concluida el dia anterior la numeración de los Ayllos Tinta, y Ucho"},
  "concluida el dia anterior la numeración de los Ayllos Tinta, y Ucho", fundamento="experiencia-propia")
a("A-UT17-812", "UT17", "P27", "M-UT18-001", "informante", {"mencion": "M-UT17-829"},
  "ejerce-cargo", {"concepto": "recaudador-de-tributos"}, "insultar al Recaudador con palabras injuriosas")
a("A-UT17-813", "UT17", "P27", "M-UT18-001", "informante", {"mencion": "M-UT17-824"},
  "ejerce-cargo", {"concepto": "revisitador"}, "estabamos matriculando a los indios el revisitador , y Yo")
a("A-UT17-814", "UT17", "P27", "M-UT18-001", "informante", {"mencion": "M-UT17-828"},
  "se-hallaba", {"literal": "presencio ... la numeración"}, "la numeración de los Ayllos Tinta, y Ucho que presencio el mismo denunciador Guancachoque",
  fundamento="experiencia-propia")
a("A-UT17-817", "UT17", "P27", "M-UT18-001", "informante", {"pieza": "P06"},
  "veracidad", {"literal": "estas falsedades"},
  "por sorprender como estas falsedades la justificación de Vuestra Señoría muy Ilustrísima", fundamento="actuado",
  nota="«estas falsedades» se refiere a los documentos presentados y a la denuncia del bullicio; se ancla al escrito P06.")
a("A-UT17-818", "UT17", "P27", "M-UT18-001", "informante", {"mencion": "M-UT17-004"},
  "motivo", {"literal": "por sorprender como estas falsedades la justificación de Vuestra Señoría"},
  "por sorprender como estas falsedades la justificación de Vuestra Señoría muy Ilustrísima", fundamento="actuado")
a("A-UT18-801", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT18-801"},
  "participa-en-hecho", {"hecho": "H-p27-acometida"}, "Segundas, y Principales de los citados Ayllus de Chuquitapa acometieron contra el",
  rol_en_hecho="agresor", fundamento="experiencia-propia",
  nota="La frase empieza en UT17: «lo que visto por los Alcaldes.» (M-UT17-830), también agresores.")
a("A-UT18-802", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT18-804"},
  "participa-en-hecho", {"hecho": "H-p27-acometida"}, "si yo no salgo al indio lo hubieran en tropeado",
  rol_en_hecho="victima", fundamento="experiencia-propia")
a("A-UT18-803", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT18-804"},
  "participa-en-hecho", {"hecho": "H-p27-prision"}, "por cuyo insulto, y atropellamiento, en mi misma casa, lo mande llevar a la cárcel",
  rol_en_hecho="preso", fundamento="experiencia-propia")
a("A-UT18-804", "UT18", "P27", "M-UT18-001", "informante", {"hecho": "H-p27-prision"},
  "motivo", {"literal": "por cuyo insulto, y atropellamiento, en mi misma casa"},
  "por cuyo insulto, y atropellamiento, en mi misma casa, lo mande llevar a la cárcel", fundamento="experiencia-propia")
a("A-UT18-805", "UT18", "P27", "M-UT18-001", "informante", {"hecho": "H-p27-prision"},
  "lugar-del-hecho", {"mencion": "M-UT18-806"}, "lo mande llevar a la cárcel , y que lo guardasen en ella", fundamento="experiencia-propia")
a("A-UT18-806", "UT18", "P27", "M-UT18-001", "informante", {"hecho": "H-p27-prision"},
  "motivo", {"literal": "con motivo de practicar otra diligencia sobre presentaciones que hiso de agravios"},
  "al que puse en libertad al otro dia por la tarde con motivo de practicar otra diligencia sobre presentaciones que hiso de agravios",
  fundamento="experiencia-propia", nota="Motivo de la puesta en libertad (no de la prisión).")
a("A-UT18-807", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT18-804"},
  "participa-en-hecho", {"hecho": "H-p27-presentacion-agravios"},
  "presentaciones que hiso de agravios inferidos por Chuquitapa a nombre del común y Principales",
  rol_en_hecho="participante-en-hecho", fundamento="actuado",
  nota="El sujeto de «hiso» es elíptico en la cita (el indio Guancachoque, antecedente inmediato).")
a("A-UT18-808", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT18-807"},
  "participa-en-hecho", {"hecho": "H-p27-presentacion-agravios"}, "de agravios inferidos por Chuquitapa a nombre del común",
  rol_en_hecho="agresor", fundamento="actuado",
  nota="Agravios que Guancachoque atribuyó a Chuquitapa en nombre del común; Mata los reporta como denuncia luego desmentida.")
a("A-UT18-809", "UT18", "P27", "M-UT18-001", "informante", {"hecho": "H-p27-presentacion-agravios"},
  "veracidad", {"literal": "lo convencieron de falsedad"}, "en la que lo convencieron de falsedad", fundamento="oidas",
  segun="M-UT18-808", nota="Según el común y Principales, en la diligencia que practicó Mata.")
a("A-UT18-810", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT18-804"},
  "participa-en-hecho", {"hecho": "H-p27-intento-sublevacion"},
  "exponiendo que el había querido conmover y sublevar a todos los Indios contra su recaudador",
  rol_en_hecho="instigador", fundamento="oidas", segun="M-UT18-808")
a("A-UT18-811", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT18-808"},
  "dijo", {"literal": "no tenían queja alguna"}, "contra su recaudador del que no tenían queja alguna",
  fundamento="oidas", segun="M-UT18-808")
a("A-UT18-812", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT18-812"},
  "ejerce-cargo", {"concepto": "recaudador-de-tributos"}, "sublevar a todos los Indios contra su recaudador")
a("A-UT18-813", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT18-002"},
  "ejerce-cargo", {"concepto": "cura-interino"}, "al cura interino de dicho -Pueblo Doctor Don Agustin Valdes")
a("A-UT18-814", "UT18", "P27", "M-UT18-001", "informante", {"pieza": "P23"},
  "redacto", {"mencion": "M-UT18-002"},
  "Por el informe que le pedí al cura interino de dicho -Pueblo Doctor Don Agustin Valdes", fundamento="actuado",
  nota="Atribución de autoría del informe P23 (que no lleva nombre); el redactor material no consta.")
a("A-UT18-815", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT18-002"},
  "solicita", {"literal": "el informe que le pedí"}, "Por el informe que le pedí al cura interino de dicho -Pueblo Doctor Don Agustin Valdes", fundamento="experiencia-propia")
a("A-UT18-816", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT18-815"},
  "solicita", {"literal": "se le aflija con el condigno castigo que merece"},
  "condiciones todas dignas de que se le aflija con el condigno castigo que merece")
a("A-UT18-817", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT18-817"},
  "calificacion-de-conducta", {"literal": "alguna Chispa soplada por Guancachoque que perjudicque la tranquilidad publica"},
  "a encenderse alguna Chispa soplada por Guancachoque que perjudicque la tranquilidad publica del partido de mi cargo",
  nota="Riesgo futuro alegado por Mata, ligado a «las cenisas calientes de la pesada Revelion» (H5); no es un hecho ocurrido.")
a("A-UT18-818", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT18-820"},
  "ejerce-cargo", {"concepto": "presidente-audiencia"}, "Muy Ylustre Señor presidente Don Francisco Muñoz y Señor Clemente")
a("A-UT18-819", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT18-001"},
  "ejerce-cargo", {"concepto": "subdelegado"}, "la tranquilidad publica del partido de mi cargo",
  nota="Cargo implícito en «partido de mi cargo»; el informe se dirige como subdelegado de Tinta (P13, P14).")
a("A-UT18-820", "UT18", "P27", "M-UT18-001", "informante", {"pieza": "P27"},
  "firmo", {"mencion": "M-UT18-001"}, "Siquani Noviembre 8 de 1806 Muy Ylustre señor Firma Pedro de la Mata",
  nota="«Firma» es indicación del transcriptor; la mención M-UT18-001 lleva rol informante en el hilo central.")

# ───────────── P28 · Auto del 26 de noviembre · UT19 ─────────────
# Ya anotadas: M-UT19-002 (Muñoz, firmante), M-UT19-003 (subdelegado del partido de tinta, destinatario).
m("M-UT19-801", "UT19", "P28", "lugar", "Cusco", "Folio 33 Cusco y noviembre 26 de 1806", tipo="ciudad")
m("M-UT19-802", "UT19", "P28", "persona", "señor Fiscal", "con lo supuesto por el señor Fiscal librese")
m("M-UT19-803", "UT19", "P28", "lugar", "partido de tinta", "al subdelegado del partido de tinta para que tome", tipo="partido")
m("M-UT19-804", "UT19", "P28", "persona", "yndio Guancachoque", "los excesos y enemistad del yndio Guancachoque paso")
m("M-UT19-805", "UT19", "P28", "persona", "Don Andres Chuquitapa", "con el recaudador de tributos Don Andres Chuquitapa hasiendole")
m("M-UT19-806", "UT19", "P28", "grupo", "los superiores", "que debe observar en lo sucesivo con los superiores bajo")
m("M-UT19-807", "UT19", "P28", "grupo", "el gobierno", "Tomará el gobierno las más serias providencias")

a("A-UT19-801", "UT19", "P28", "M-UT19-002", "resolutor", {"mencion": "M-UT19-003"},
  "ordena", {"literal": "tome las providencias que estaba oportunas"},
  "librese la correspondiente orden al subdelegado del partido de tinta para que tome las providencias que estaba oportunas")
a("A-UT19-802", "UT19", "P28", "M-UT19-002", "resolutor", {"mencion": "M-UT19-003"},
  "ordena", {"literal": "hasiendole asi mismo extender la subordinación y respeto que debe observar en lo sucesivo con los superiores"},
  "hasiendole asi mismo extender la subordinación y respeto que debe observar en lo sucesivo con los superiores")
a("A-UT19-803", "UT19", "P28", "M-UT19-002", "resolutor", {"mencion": "M-UT19-804"},
  "ordena", {"literal": "bajo apersivimiento ... Tomará el gobierno las más serias providencias"},
  "bajo apersivimiento de que en el caso de residencia To- Tomará el gobierno las más serias providencias",
  nota="Apercibimiento dirigido al indio Guancachoque (persona afectada), a quien el subdelegado debe hacer guardar subordinación.")
a("A-UT19-804", "UT19", "P28", "M-UT19-002", "resolutor", {"mencion": "M-UT19-804"},
  "tiene-condicion", {"concepto": "indio"}, "los excesos y enemistad del yndio Guancachoque")
a("A-UT19-805", "UT19", "P28", "M-UT19-002", "resolutor", {"mencion": "M-UT19-804"},
  "calificacion-de-conducta", {"literal": "excesos y enemistad"}, "a fin de contener los excesos y enemistad del yndio Guancachoque paso con el recaudador")
a("A-UT19-806", "UT19", "P28", "M-UT19-002", "resolutor", {"mencion": "M-UT19-805"},
  "ejerce-cargo", {"concepto": "recaudador-de-tributos"}, "con el recaudador de tributos Don Andres Chuquitapa")
a("A-UT19-807", "UT19", "P28", "M-UT19-002", "resolutor", {"mencion": "M-UT19-003"},
  "ejerce-cargo", {"concepto": "subdelegado"}, "al subdelegado del partido de tinta para que tome")

# ───────────── P29 · Vista fiscal (20 de noviembre) · UT19–UT20 ─────────────
# Ya anotadas: M-UT19-001 (Manuel Guancoichoque), M-UT20-001 (Gonzalo del Rio, firmante; afirmante dictaminador).
m("M-UT19-808", "UT19", "P29", "persona", "El fiscal", "Muñoz [firma] El fiscal del Señor Muy en vista", rol="dictaminador")
m("M-UT19-809", "UT19", "P29", "persona", "subdelegado del partido de Tinta", "antecedente oficio del subdelegado del partido de Tinta , y del")
m("M-UT19-810", "UT19", "P29", "lugar", "partido de Tinta", "oficio del subdelegado del partido de Tinta , y del Expediente", tipo="partido")
m("M-UT19-811", "UT19", "P29", "cosa", "Expediente", "y del Expediente que le acompaña Dice")
m("M-UT19-812", "UT19", "P29", "lugar", "Pueblo de Tinta", "Guancoichoque Yndio del Pueblo de Tinta contra", tipo="pueblo")
m("M-UT19-813", "UT19", "P29", "persona", "Andres chuquitapa", "contra el recaudador de tributos Andres chuquitapa y demás")
m("M-UT19-814", "UT19", "P29", "grupo", "Yndios tributarios", "en odio de los denuncios de Yndios tributarios que hizo")
m("M-UT19-815", "UT19", "P29", "persona", "dicho recaudador", "que hizo contra dicho recaudador por la malicia")
m("M-UT19-816", "UT19", "P29", "cosa", "dicha queja", "aver formado dicha queja y los documentos que presento")
m("M-UT19-817", "UT19", "P29", "cosa", "los documentos", "dicha queja y los documentos que presento en su calificación")
m("M-UT19-818", "UT19", "P29", "persona", "mencionado recaudador", "profesarle al mencionado recaudador, y por la mala")
m("M-UT19-819", "UT19", "P29", "persona", "el subdelegado territorial", "mui conveniente que el subdelegado territorial tome las providencias")
m("M-UT19-820", "UT19", "P29", "persona", "yndio Guancachoque", "a efecto de corregir y contener del yndio Guancachoque y evitar")
m("M-UT19-821", "UT19", "P29", "persona", "dicho Guancachoque", "la conducta y operaciones de dicho Guancachoque En cuio")
m("M-UT19-822", "UT19", "P29", "persona", "vuestro", "En cuio a tener podrá vuestro si es servido", rol="destinatario")
m("M-UT19-823", "UT19", "P29", "persona", "mencionado .Subdelegado", "la conducente orden al mencionado .Subdelegado a este efecto")
m("M-UT19-824", "UT19", "P29", "grupo", "este gobierno", "la prudente y celosa rectitud de este gobierno")
m("M-UT20-801", "UT20", "P29", "lugar", "Cuzco", "circuntancia de este asunto Cuzco y Noviembre 20 de 1806", tipo="ciudad")

a("A-UT19-808", "UT19", "P29", "M-UT20-001", "dictaminador", {"mencion": "M-UT19-001"},
  "tiene-condicion", {"concepto": "indio"}, "Manuel Guancoichoque Yndio del Pueblo de Tinta")
a("A-UT19-809", "UT19", "P29", "M-UT20-001", "dictaminador", {"mencion": "M-UT19-813"},
  "ejerce-cargo", {"concepto": "recaudador-de-tributos"}, "contra el recaudador de tributos Andres chuquitapa")
a("A-UT19-810", "UT19", "P29", "M-UT20-001", "dictaminador", {"mencion": "M-UT19-809"},
  "ejerce-cargo", {"concepto": "subdelegado"}, "antecedente oficio del subdelegado del partido de Tinta")
a("A-UT19-811", "UT19", "P29", "M-UT20-001", "dictaminador", {"pieza": "P06"},
  "motivo", {"literal": "en odio de los denuncios de Yndios tributarios que hizo contra dicho recaudador"},
  "en odio de los denuncios de Yndios tributarios que hizo contra dicho recaudador", fundamento="actuado",
  nota="Lo que la queja de Guancachoque alega como causa de los agravios (prisión, maltrato, injurias), según el fiscal.")
a("A-UT19-812", "UT19", "P29", "M-UT20-001", "dictaminador", {"pieza": "P06"},
  "veracidad", {"literal": "la malicia con que aparece aver formado dicha queja"},
  "por la malicia con que aparece aver formado dicha queja y los documentos que presento en su calificación", fundamento="actuado")
for i, p in enumerate(["P01", "P03", "P04", "P05"], 1):
    a(f"A-UT19-{820 + i:03d}", "UT19", "P29", "M-UT20-001", "dictaminador", {"pieza": p},
      "redacto", {"mencion": "M-UT19-001"},
      "por la malicia con que aparece aver formado dicha queja y los documentos que presento en su calificación",
      fundamento="actuado", distribuida=True,
      nota="«los documentos que presento en su calificación» se distribuye a cada certificación (mismo reparto que A-UT17-10x); "
           "«aparece aver formado» atribuye la formación de los documentos a Guancachoque. P02 se excluye.")
a("A-UT19-813", "UT19", "P29", "M-UT20-001", "dictaminador", {"mencion": "M-UT19-001"},
  "motivo", {"literal": "los enemistad que se advierte profesarle al mencionado recaudador"},
  "por los enemistad que se advierte profesarle al mencionado recaudador", fundamento="actuado")
a("A-UT19-814", "UT19", "P29", "M-UT20-001", "dictaminador", {"mencion": "M-UT19-822"},
  "solicita", {"literal": "tome las providencias que según su prudencia y conocimientos en el asunto estime mas oportuno y conducentes a efecto de corregir y contener del yndio Guancachoque"},
  "parece consiguiente y mui conveniente que el subdelegado territorial tome las providencias que según su prudencia y conocimientos en el asunto estime mas oportuno y conducentes a efecto de corregir y contener del yndio Guancachoque",
  nota="Propuesta del fiscal (vista), no orden: la fuerza dictaminadora se deriva de la actuación.")
a("A-UT19-815", "UT19", "P29", "M-UT20-001", "dictaminador", {"mencion": "M-UT19-822"},
  "solicita", {"literal": "sujetándolo a la debida subordinación y correspondientes obligaciones"},
  "sujetándolo a la debida subordinación y correspondientes obligaciones")
a("A-UT19-816", "UT19", "P29", "M-UT20-001", "dictaminador", {"mencion": "M-UT19-822"},
  "solicita", {"literal": "se libre la conducente orden al mencionado .Subdelegado a este efecto"},
  "podrá vuestro si es servido moidar se libre la conducente orden al mencionado .Subdelegado a este efecto",
  nota="Lo que el fiscal propone al Presidente; el auto P28 se conforma con ello (A-UT19-004).")
a("A-UT19-817", "UT19", "P29", "M-UT20-001", "dictaminador", {"mencion": "M-UT19-822"},
  "solicita", {"literal": "mui a la mira de la conducta y operaciones de dicho Guancachoque"},
  "mui a la mira de la conducta y operaciones de dicho Guancachoque")
a("A-UT20-801", "UT20", "P29", "M-UT20-001", "dictaminador", {"pieza": "P29"},
  "firmo", {"mencion": "M-UT20-001"}, "Noviembre 20 de 1806.[Firma Gonzalo del Rio]",
  nota="«Firma» es indicación del transcriptor.")

# ───────────── P30 · Notificación del auto al fiscal (26 de noviembre) · UT20 ─────────────
m("M-UT20-802", "UT20", "P30", "persona", "Don Agustin Chacon y Becerra", "[Firma Gonzalo del Rio] Don Agustin Chacon y Becerra En la Ciudad")
m("M-UT20-803", "UT20", "P30", "lugar", "Ciudad del Cuzco", "En la Ciudad del Cuzco en veinte y seis de noviembre", tipo="ciudad")
m("M-UT20-804", "UT20", "P30", "persona", "Yo el escribano", "seis . Yo el escribano hacia presente el entendido", rol="fedatario")
m("M-UT20-805", "UT20", "P30", "cosa", "Auto marginal", "el entendido del Auto marginal presedente al señor")
m("M-UT20-806", "UT20", "P30", "persona", "don Lucio Gonzalo del Rio y Vial", "al señor don Lucio Gonzalo del Rio y Vial del Concejo",
  rol="notificado")
m("M-UT20-807", "UT20", "P30", "lugar", "las casas de mi morada", "estando en las casas de mi morada doy fe", tipo="edificio")
m("M-UT20-808", "UT20", "P30", "persona", "Chacon", "las casas de mi morada doy fe[ Firma Chacon]", rol="firmante")

a("A-UT20-802", "UT20", "P30", "M-UT20-804", "fedatario", {"mencion": "M-UT20-804"},
  "ejerce-cargo", {"concepto": "escribano"}, "Yo el escribano hacia presente el entendido del Auto marginal")
a("A-UT20-803", "UT20", "P30", "M-UT20-804", "fedatario", {"hecho": "H-p30-notificacion"},
  "lugar-del-hecho", {"mencion": "M-UT20-807"}, "estando en las casas de mi morada doy fe", fundamento="experiencia-propia",
  nota="Pasaje defectuoso («su final insesta por doña»); no queda claro de quién es la morada.")
a("A-UT20-804", "UT20", "P30", "M-UT20-804", "fedatario", {"mencion": "M-UT20-806"},
  "participa-en-hecho", {"hecho": "H-p30-notificacion"}, "hacia presente el entendido del Auto marginal presedente al señor don Lucio Gonzalo del Rio y Vial",
  rol_en_hecho="participante-en-hecho", fundamento="experiencia-propia",
  nota="Persona notificada del auto P28 (rol notificado en la mención).")
a("A-UT20-805", "UT20", "P30", "M-UT20-804", "fedatario", {"pieza": "P30"},
  "firmo", {"mencion": "M-UT20-808"}, "doy fe[ Firma Chacon]", nota="«Firma» es indicación del transcriptor.")

# ───────────── P31 · Notificación del auto (fecha «mil ochocientos 10 años») · UT20 ─────────────
m("M-UT20-809", "UT20", "P31", "lugar", "Cusco", "En el Cusco en veinte y tres de Diciembre", tipo="ciudad")
m("M-UT20-810", "UT20", "P31", "persona", "Yo el escribano", "10 años . Yo el escribano habiendo llegado", rol="fedatario")
m("M-UT20-811", "UT20", "P31", "lugar", "la ciudad", "habiendo llegado a la ciudad a preguntar", tipo="ciudad")
m("M-UT20-812", "UT20", "P31", "cosa", "el proveido antecedente", "a preguntar por el proveido antecedente hace saber")
m("M-UT20-813", "UT20", "P31", "cosa", "Auto de arriba", "el contento del Auto de arriba , en su persona")
m("M-UT20-814", "UT20", "P31", "persona", "su persona", "Auto de arriba , en su persona , doy fé", rol="notificado")
m("M-UT20-815", "UT20", "P31", "persona", "Chacon", "en su persona , doy fé [ Firma Chacon]", rol="firmante")

a("A-UT20-806", "UT20", "P31", "M-UT20-810", "fedatario", {"mencion": "M-UT20-810"},
  "ejerce-cargo", {"concepto": "escribano"}, "Yo el escribano habiendo llegado a la ciudad")
a("A-UT20-807", "UT20", "P31", "M-UT20-810", "fedatario", {"mencion": "M-UT20-814"},
  "participa-en-hecho", {"hecho": "H-p31-notificacion"}, "hace saber el contento del Auto de arriba , en su persona , doy fé",
  rol_en_hecho="participante-en-hecho", fundamento="experiencia-propia",
  nota="La persona notificada no se nombra («en su persona»).")
a("A-UT20-808", "UT20", "P31", "M-UT20-810", "fedatario", {"hecho": "H-p31-notificacion"},
  "fecha-del-hecho", {"literal": "veinte y tres de Diciembre de mil ochocientos 10 años"},
  "En el Cusco en veinte y tres de Diciembre de mil ochocientos 10 años", fundamento="experiencia-propia",
  nota="Fecha anómala (F6 en docs/01_materiales.md): 1810 no encaja con el expediente de 1806; se conserva tal como está escrita.")
a("A-UT20-809", "UT20", "P31", "M-UT20-810", "fedatario", {"pieza": "P31"},
  "firmo", {"mencion": "M-UT20-815"}, "doy fé [ Firma Chacon]", nota="«Firma» es indicación del transcriptor.")

# ───────────── P32 · Certificación notarial republicana AJENA al expediente · UT20 ─────────────
# Solo participantes de la pieza; sin afirmaciones ni relación alguna con la causa de 1806.
m("M-UT20-816", "UT20", "P32", "persona", "Matias Ugarte", "El ciudadano Matias Ugarte = Notario Público", rol="certificante")
m("M-UT20-817", "UT20", "P32", "lugar", "provincia de Urubamba", "Notario Público de la provincia de Urubamba certifica")
m("M-UT20-818", "UT20", "P32", "persona", "la señora", "la venta otorgada por la señora.")


if __name__ == "__main__":
    out = Path(__file__).with_suffix(".jsonl")
    with out.open("w", encoding="utf-8") as f:
        for r in M + A:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{len(M)} menciones, {len(A)} afirmaciones -> {out}")
