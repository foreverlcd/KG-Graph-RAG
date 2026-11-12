"""Anotación manual del hilo central (docs/E_prueba_hilo_central.md).

Registros de capa 2 (menciones) y capa 3 (afirmaciones) en el MISMO esquema plano que llenará el LLM
(src/laad/esquema.py). Sirven de ejemplo trabajado y de semilla del estándar de oro; no sustituyen la
anotación independiente de dos personas (docs/G_evaluacion.md).

Anotador: el modelador (Claude Opus 5.5), 2026-11-12. Lote: anotacion-manual-hilo-central-v1.
Ejecutar: python datos/registros/hilo_central.py  -> escribe hilo_central.jsonl
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


# ───────────── P01 · Certificación de Isidro Cano (1 de agosto) · UT01 ─────────────
m("M-UT01-001", "UT01", "P01", "persona", "Isidro Cano", "Yo el sargento Don Isidro Cano de esta compañía", rol="certificante")
m("M-UT01-002", "UT01", "P01", "persona", "Guancachoque", "al denunciante mayor Guancachoque", rol="denunciante")
m("M-UT01-003", "UT01", "P01", "persona", "Chuquiitapa", "suspecha de la traicion de la orden del dicho Chuquiitapa")
m("M-UT01-004", "UT01", "P01", "persona", "Chuquitapa", "mando dicho Chuquitapa cargando")
m("M-UT01-005", "UT01", "P01", "persona", "Tupa Amaro", "en el tiempo del rebelde. Tupa Amaro fue complice y coronel")
m("M-UT01-006", "UT01", "P01", "persona", "Isidro Cano", "como fiel christiano. Isidro Cano.", rol="firmante")
m("M-UT01-007", "UT01", "P01", "lugar", "Tinta", "En el pueblo de Tinta, en primero de agosto de 1806", tipo="pueblo")

a("A-UT01-001", "UT01", "P01", "M-UT01-001", "certificante", {"mencion": "M-UT01-004", "eliptico": True},
  "ejerce-cargo", {"concepto": "coronel-rebelde"}, "lo mismo en el tiempo del rebelde. Tupa Amaro fue complice y coronel",
  nota="Sujeto elíptico. La puntuación del transcriptor («rebelde. Tupa Amaro fue») admite leer a Túpac Amaru como sujeto; "
       "se resuelve a Chuquitapa porque el párrafo trata de sus acciones y porque el propio Cano, en su declaración (P18), "
       "dice «fue Comisionado por este y no coronel como expone en su certificación».")
a("A-UT01-002", "UT01", "P01", "M-UT01-001", "certificante", {"mencion": "M-UT01-004", "eliptico": True},
  "ejerce-cargo", {"concepto": "complice-rebelde"}, "lo mismo en el tiempo del rebelde. Tupa Amaro fue complice y coronel",
  nota="Mismo sujeto elíptico que A-UT01-001.")
a("A-UT01-003", "UT01", "P01", "M-UT01-001", "certificante", {"hecho": "H-p01-alboroto"},
  "fecha-del-hecho", {"literal": "a media noche"}, "esa noche todos los indios se alzaron a media noche todos con garrotes")
a("A-UT01-004", "UT01", "P01", "M-UT01-001", "certificante", {"mencion": "M-UT01-003"},
  "participa-en-hecho", {"hecho": "H-p01-alboroto"}, "llevamos hasta hoy dia suspecha de la traicion de la orden del dicho Chuquiitapa",
  fundamento="sospecha", rol_en_hecho="instigador")

# ───────────── P03 · Certificación a nombre de Juan Quiñones, firmada Juan Cazorla · UT02 ─────────────
m("M-UT02-001", "UT02", "P03", "persona", "don Juan Quiñones", "El teniente Alguacil, don Juan Quiñones, certifico", rol="certificante")
m("M-UT02-002", "UT02", "P03", "persona", "Juan Cazorla", "los señores jueces pongan remedio. Juan Cazorla.", rol="firmante")
m("M-UT02-003", "UT02", "P02", "persona", "Manuel Guamanchoque", "es cierto que Manuel Guamanchoque ha estado soldado en mi compañía")
m("M-UT02-004", "UT02", "P02", "persona", "Santiago Cazorla", "quien padece de sus enemigos por ser leal. Santiago Cazorla", rol="firmante")
m("M-UT02-005", "UT02", "P02", "persona", "yo sargento primero", "como yo sargento primero del regimiento de Tinta", rol="certificante")

a("A-UT02-001", "UT02", "P03", "M-UT02-001", "certificante", {"hecho": "H-p03-alboroto"},
  "fecha-del-hecho", {"literal": "a las dies o a las once"}, "Esa misma noche a las dies o a las once se alzaron los indios en la plaza",
  fundamento="vista", nota="El certificante declara «Esto es lo que vi de con mis ojos».")
a("A-UT02-002", "UT02", "P02", "M-UT02-005", "certificante", {"mencion": "M-UT02-003"},
  "ejerce-cargo", {"concepto": "soldado"}, "Manuel Guamanchoque ha estado soldado en mi compañía más de cinco años")

# ───────────── P04 · Certificación a nombre de Fernando Orue · UT03 ─────────────
m("M-UT03-001", "UT03", "P04", "persona", "Fernando Orue", "del puesto de Tinta Fernando Orue, vecino", rol="certificante")
m("M-UT03-002", "UT03", "P04", "persona", "Chuquitapa", "Como está hecho de hacer alzamiento a dicho Chuquitapa")
m("M-UT03-003", "UT03", "P04", "persona", "Tupaamaro", "en tiempo de su pariente Tupaamaro fue coronel")
m("M-UT03-004", "UT03", "P04", "persona", "Fernando Orue", "ser mi verdad de Fernando Orue", rol="firmante")

a("A-UT03-001", "UT03", "P04", "M-UT03-001", "certificante", {"mencion": "M-UT03-002"},
  "ejerce-cargo", {"concepto": "coronel-rebelde"}, "en tiempo de su pariente Tupaamaro fue coronel, comecionado")
a("A-UT03-002", "UT03", "P04", "M-UT03-001", "certificante", {"mencion": "M-UT03-002"},
  "ejerce-cargo", {"concepto": "comisionado-rebelde"}, "en tiempo de su pariente Tupaamaro fue coronel, comecionado")
a("A-UT03-003", "UT03", "P04", "M-UT03-001", "certificante", {"mencion": "M-UT03-002"},
  "parentesco", {"mencion": "M-UT03-003"}, "en tiempo de su pariente Tupaamaro", nota="Tipo de parentesco escrito: «pariente».")
a("A-UT03-004", "UT03", "P04", "M-UT03-001", "certificante", {"hecho": "H-p04-alboroto"},
  "fecha-del-hecho", {"literal": "a las diez de la noche"}, "a las diez de la noche, peor alboroto", fundamento="vista",
  nota="El certificante declara «he visto con mis ojos, mortales el alboroto».")

# ───────────── P05 · Certificación a nombre de Martín Cazorla · UT04 ─────────────
m("M-UT04-001", "UT04", "P05", "persona", "Martin Cazorla", "Yo el soldado granadero Martin Cazorla digo y certifico", rol="certificante")
m("M-UT04-002", "UT04", "P05", "persona", "Martin Cazorla", "fe ser mi verdad. Martin Cazorla", rol="firmante")

a("A-UT04-001", "UT04", "P05", "M-UT04-001", "certificante", {"mencion": "M-UT04-001"},
  "dijo", {"literal": "abra nuevamente porque es desde el rebelde"}, "abra nuevamente porque es desde el rebelde",
  nota="Enunciado de la propia certificación; se registra para poder contrastarlo con la negación de P19.")
a("A-UT04-002", "UT04", "P05", "M-UT04-001", "certificante", {"mencion": "M-UT04-001"},
  "dijo", {"literal": "se alzaron los Indios todos con garrotes, armados a dar muerte"},
  "Esa misma noche se alzaron los Indios todos con garrotes, armados a dar muerte")

# ───────────── P06 · Escrito de Huancachoque (22 de agosto) · UT05–UT06 ─────────────
m("M-UT05-001", "UT05", "P06", "persona", "Manuel Huancachoque", "Manuel Huancachoque Indio originario y vecino del pueblo de Tinta", rol="denunciante")
m("M-UT06-001", "UT06", "P06", "persona", "Chuquitapa", "a quienes había entregado Chuquitapa", )
m("M-UT06-002", "UT06", "P06", "persona", "MANUEL HUANCACHOQQUE", "que ello consta a vuestra… MANUEL HUANCACHOQQUE", rol="firmante")

a("A-UT06-001", "UT06", "P06", "M-UT05-001", "denunciante", {"hecho": "H-p06-prision"},
  "duracion", {"literal": "dos días"}, "yo me mantuve dos días preso", fundamento="experiencia-propia")
a("A-UT06-002", "UT06", "P06", "M-UT05-001", "denunciante", {"hecho": "H-p06-alboroto"},
  "fecha-del-hecho", {"literal": "a las nueve de la noche"}, "pero a las nueve de la noche se apareció una caterva de indios",
  fundamento="experiencia-propia")
a("A-UT06-003", "UT06", "P06", "M-UT05-001", "denunciante", {"mencion": "M-UT06-001"},
  "participa-en-hecho", {"hecho": "H-p06-alboroto"}, "se apareció una caterva de indios, a quienes había entregado Chuquitapa",
  rol_en_hecho="instigador", fundamento="experiencia-propia")

# ───────────── P18 · Declaración jurada de Isidro Cano (23 de septiembre) · UT11–UT12.a ─────────────
m("M-UT11-001", "UT11", "P18", "persona", "Ysidro Cano", "la persona de D. Ysidro Cano vecino Español", rol="declarante")
m("M-UT11-002", "UT11", "P18", "persona", "Pedro de la Mata", "comparecio ante mi D.Pedro de la Mata", rol="juez-comisionado")
m("M-UT11-003", "UT11", "P18", "persona", "Santiago Casorla", "se lo dijo su segundo sargento Santiago Casorla")
m("M-UT12.a-001", "UT12.a", "P18", "persona", "YSIDRO CANO", "PEDRO DE LA MATA YSIDRO CANO", rol="firmante")
m("M-UT12.a-002", "UT12.a", "P18", "persona", "PEDRO DE LA MATA", "PEDRO DE LA MATA YSIDRO CANO", rol="firmante")
m("M-UT12.a-003", "UT12.a", "P18", "persona", "MARIANO FIGUEROA", "MARIANO FIGUEROA CELEDONIO APARICIO", rol="testigo-de-asistencia")
m("M-UT12.a-004", "UT12.a", "P18", "persona", "CELEDONIO APARICIO", "MARIANO FIGUEROA CELEDONIO APARICIO", rol="testigo-de-asistencia")

a("A-UT11-001", "UT11", "P18", "M-UT11-001", "declarante", {"pieza": "P01"},
  "autenticidad-firma", {"mencion": "M-UT11-001"}, "dijo que la firma Que dice Isidro Cano es suya propia")
a("A-UT11-002", "UT11", "P18", "M-UT11-001", "declarante", {"pieza": "P01"},
  "ratifica-contenido", {"mencion": "M-UT11-001"}, "preso ser cierto todo lo que en ella dice que le consta solo",
  nota="Ratificación con salvedades: la continúan A-UT11-003, A-UT11-004 y A-UT11-005.")
a("A-UT11-003", "UT11", "P18", "M-UT11-001", "declarante", {"mencion": "M-UT01-004", "eliptico": True},
  "ejerce-cargo", {"concepto": "comisionado-rebelde"}, "en tiempo del rebelde Tupa amaro fue Comisionado por este", responde_a="A-UT01-001",
  nota="Sujeto elíptico: la declaración versa sobre la certificación P01 («como expone en su certificación»); se remite a la mención de Chuquitapa en P01.")
a("A-UT11-004", "UT11", "P18", "M-UT11-001", "declarante", {"mencion": "M-UT01-004", "eliptico": True},
  "ejerce-cargo", {"concepto": "coronel-rebelde"}, "Comisionado por este y no coronel como expone en su certificación",
  polaridad="niega", responde_a="A-UT01-001", nota="Sujeto elíptico (ver A-UT11-003). Niega expresamente lo afirmado en A-UT01-001.")
a("A-UT11-005", "UT11", "P18", "M-UT11-001", "declarante", {"hecho": "H-p18-alboroto"},
  "fecha-del-hecho", {"literal": "a media noche"},
  "se alzaron a media noche armados con garrotes para acabar con este, y hacer matalo de los españoles poniendo guardias a las puertas de estos no le cons ta al que declara si no porque se lo dijo su segundo sargento Santiago Casorla",
  fundamento="oidas", segun="M-UT11-003", responde_a="A-UT01-003")
a("A-UT12a-001", "UT12.a", "P18", "M-UT11-001", "declarante", {"pieza": "P01"},
  "motivo", {"literal": "este fue a su casa suplicandole"}, "dijo que la dado porque este fue a su casa supli candole")

# ───────────── P19 · Declaración sobre la certificación «Martin casorla» · UT12.a–UT13 ─────────────
m("M-UT12.a-005", "UT12.a", "P19", "persona", "Mariano Casorla", "el Gobernador Señor Don Mariano Casorla", rol="declarante")
m("M-UT12.a-006", "UT12.a", "P19", "persona", "Martin casorla", "De folio 4 su firma Martin casorla")
m("M-UT12.b-001", "UT12.b", "P19", "persona", "Simon Arce", "mando el que declara a Simon Arce")

a("A-UT12b-001", "UT12.b", "P19", "M-UT12.a-005", "declarante", {"mencion": "M-UT12.a-005"},
  "sabe-firmar", {"literal": "sabe escribir"}, "No sabe escribir que es cierto", polaridad="niega")
a("A-UT12b-002", "UT12.b", "P19", "M-UT12.a-005", "declarante", {"pieza": "P05"},
  "redacto", {"mencion": "M-UT12.b-001"},
  "mando el que declara a Simon Arce que pusiere en un papelito lo mis mo que relata en la citada certificación")
a("A-UT12b-003", "UT12.b", "P19", "M-UT12.a-005", "declarante", {"pieza": "P05"},
  "firmo", {"literal": "no sabe quien"}, "no sabe quien lo transcribio ni firmo su nombre en el papel que se le ha manifestado",
  fundamento="no-consta")
a("A-UT12b-004", "UT12.b", "P19", "M-UT12.a-005", "declarante", {"mencion": "M-UT12.a-005"},
  "dijo", {"literal": "se alzaron los Yndios todos con barrotes armados a dar muerte"},
  "Que las expresiones de que esa misma noche se alzaron los Yndios todos con barrotes armados a dar muerte a los que cuando favor de la Real Hacienda ,no los puso el en el papelito",
  polaridad="niega", responde_a="A-UT04-002")
a("A-UT12b-005", "UT12.b", "P19", "M-UT12.a-005", "declarante", {"mencion": "M-UT12.a-005"},
  "dijo", {"literal": "porque es desde el Rebelde"},
  "porque es desde el Rebelde ……tampoco las dijo el que declara porque en aquel entonces era muchacho",
  polaridad="niega", responde_a="A-UT04-001")
a("A-UT12b-006", "UT12.b", "P19", "M-UT12.a-005", "declarante", {"hecho": "H-p19-alboroto"},
  "numero-de-participantes", {"literal": "quatro o seis Yndios"}, "vio a quatro o seis Yndios en la puerta de la carcel con garrotes",
  fundamento="vista")
a("A-UT13-001", "UT13", "P19", "M-UT12.a-005", "declarante", {"mencion": "M-UT12.a-005"},
  "edad", {"literal": "veinte y ocho años"}, "comprendo ser en edad en veinte y ocho años")

# ───────────── P21 · Declaración jurada de Fernando Orue (24 de septiembre) · UT14–UT15 ─────────────
m("M-UT14-001", "UT14", "P21", "persona", "fernando ore", "el soldado fernando ore vecino español", rol="declarante")
m("M-UT14-004", "UT14", "P21", "persona", "el grl. sub delegado", "comparecio ante mi el grl. sub delegado el soldado fernando ore", rol="juez-comisionado")
m("M-UT13-001", "UT13", "P20", "persona", "santiago cacerola", "segundo en la compañia en este fue santiago cacerola", rol="declarante")
m("M-UT14-002", "UT14", "P21", "persona", "andres chuquitaza", "con motibo de saber q de andres chuquitaza fue")
m("M-UT14-003", "UT14", "P21", "persona", "guasscachoque", "como ha puesto guasscachoque en la citada certificacion")
m("M-UT15-001", "UT15", "P21", "persona", "Chiquitas", "la mujer de Chiquitas habla contra el que declara")
m("M-UT15-002", "UT15", "P21", "persona", "chuquitapa", "que chuquitapa no es tan malo")

a("A-UT14-001", "UT14", "P21", "M-UT14-001", "declarante", {"pieza": "P04"},
  "firmo", {"mencion": "M-UT14-001"}, "no obstante que sabe firmar el declarante no quiso hacerlo", polaridad="niega")
a("A-UT14-002", "UT14", "P21", "M-UT14-001", "declarante", {"pieza": "P04"},
  "redacto", {"literal": "un hijo suyo"}, "bajo a un hijo suyo q la pusieron")
a("A-UT14-003", "UT14", "P21", "M-UT14-001", "declarante", {"pieza": "P04"},
  "redacto", {"mencion": "M-UT14-003"}, "como ha puesto guasscachoque en la citada certificacion",
  nota="Afirmación implícita en la fórmula «como ha puesto guasscachoque»; contradice A-UT14-002 en la misma declaración.")
a("A-UT14-004", "UT14", "P21", "M-UT14-001", "declarante", {"hecho": "H-p21-alboroto"},
  "fecha-del-hecho", {"literal": "el primer puesto del gallo"},
  "no fue a las dies de la noche como ha puesto guasscachoque en la citada certificacion, sino el primer puesto del gallo",
  responde_a="A-UT03-004")
a("A-UT14-005", "UT14", "P21", "M-UT14-001", "declarante", {"hecho": "H-p21-alboroto"},
  "fecha-del-hecho", {"literal": "a las dies de la noche"},
  "no fue a las dies de la noche como ha puesto guasscachoque en la citada certificacion", polaridad="niega",
  responde_a="A-UT03-004", nota="Niega la hora de su propia certificación (P04: «a las diez de la noche»); «dies»/«diez» es variante gráfica.")
a("A-UT14-006", "UT14", "P21", "M-UT14-001", "declarante", {"mencion": "M-UT14-002"},
  "ejerce-cargo", {"concepto": "coronel-rebelde"},
  "con motibo de saber q de andres chuquitaza fue en tiempo del rebelde tupa-amaru coronel y comisionado",
  responde_a="A-UT03-001")
a("A-UT14-007", "UT14", "P21", "M-UT14-001", "declarante", {"mencion": "M-UT14-002"},
  "ejerce-cargo", {"concepto": "comisionado-rebelde"},
  "con motibo de saber q de andres chuquitaza fue en tiempo del rebelde tupa-amaru coronel y comisionado")
a("A-UT15-001", "UT15", "P21", "M-UT14-001", "declarante", {"pieza": "P04"},
  "motivo", {"literal": "la mujer de Chiquitas habla contra el que declara y su familia"},
  "la mujer de Chiquitas habla contra el que declara y su familia, lo que le encolerizo")
a("A-UT15-002", "UT15", "P21", "M-UT14-001", "declarante", {"pieza": "P04"},
  "firmo", {"literal": "un hijo suyo"}, "aunque no lo hise sino mando que un hijo suyo lo hicieron")
a("A-UT15-003", "UT15", "P21", "M-UT14-001", "declarante", {"mencion": "M-UT15-002"},
  "calificacion-de-conducta", {"literal": "no es tan malo"}, "que chuquitapa no es tan malo ni de boca tan mordaz")

# ───────────── P22–P23 · Oficio al cura e informe del cura · UT15–UT16 ─────────────
m("M-UT15-003", "UT15", "P22", "persona", "parroco interino", "le conste como parroco interino de esta doctrina", rol="destinatario")
m("M-UT16a-001", "UT16.a", "P23", "persona", "Manuel Guancachoque", "Es notorio que Manuel Guancachoque es hijo Espurio")
m("M-UT16a-002", "UT16.a", "P23", "persona", "Antolin Ortiz", "hijo Espurio de Antolin Ortiz , Sanbo cerros")
m("M-UT16a-003", "UT16.a", "P23", "persona", "Joseph Condorcanqui alias Tupac Amaro", "el interprete Joseph Condorcanqui alias Tupac Amaro")
m("M-UT16a-004", "UT16.a", "P23", "persona", "Agustina Falcon", "su Madre Agustina Falcon India Ordinaria")

NOTA_CURA = ("El informe no lleva nombre en la transcripción; el afirmante es la mención del destinatario del oficio P22 "
             "(«parroco interino»). El informe de Mata (P27) lo atribuye a «Doctor Don Agustin Valdes».")
a("A-UT16a-001", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-001"},
  "filiacion", {"mencion": "M-UT16a-002"}, "Es notorio que Manuel Guancachoque es hijo Espurio de Antolin Ortiz",
  fundamento="notoriedad", nota=NOTA_CURA, otra=True)
a("A-UT16a-002", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-002"},
  "ejerce-cargo", {"concepto": "caudillo-rebelde"},
  "unos de los mas sangriento caudillo que tuvo el interprete Joseph Condorcanqui alias Tupac Amaro",
  fundamento="notoriedad", nota=NOTA_CURA, otra=True)
a("A-UT16a-003", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-002"},
  "tiene-condicion", {"concepto": "zambo"}, "hijo Espurio de Antolin Ortiz , Sanbo cerros", fundamento="notoriedad", nota=NOTA_CURA, otra=True)
a("A-UT16a-004", "UT16.a", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16a-001"},
  "filiacion", {"mencion": "M-UT16a-004"}, "su Madre Agustina Falcon India Ordinaria y pleveya", fundamento="notoriedad", nota=NOTA_CURA, otra=True)

# ───────────── P24 · Decreto: «no hay tal hombre» · UT17 ─────────────
m("M-UT17-001", "UT17", "P24", "persona", "Juan Cazorla", "Juan Cazorla de quien aparece firmada la Certificación")
m("M-UT17-002", "UT17", "P24", "persona", "Don Juan Quiñones", "a nombre del teniente Alguacil Don Juan Quiñones")
m("M-UT17-003", "UT17", "P24", "persona", "María Rubrica", "sobre el Asunto[ María Rubrica]", rol="firmante")

a("A-UT17-001", "UT17", "P24", "M-UT17-003", "resolutor", {"pieza": "P03"},
  "firmo", {"mencion": "M-UT17-001"}, "Juan Cazorla de quien aparece firmada la Certificación a folios 2",
  nota="Firmante tal como lo transcribe el transcriptor: «[ María Rubrica]». Probablemente la rúbrica de Mata (inferencia; ver docs/01_materiales.md N5).")
a("A-UT17-002", "UT17", "P24", "M-UT17-003", "resolutor", {"mencion": "M-UT17-002"},
  "existe-persona", {"literal": "en el pueblo de Tinta"}, "que no hay tal hombre en el pueblo de Tinta", polaridad="niega")

# ───────────── P27 · Informe del subdelegado Pedro de la Mata (8 de noviembre) · UT17–UT18 ─────────────
m("M-UT17-004", "UT17", "P27", "persona", "Manuel Guancachoque", "los Documentos que presento Manuel Guancachoque")
m("M-UT17-005", "UT17", "P27", "persona", "Guancachoque", "fueron hechos por el mismo Guancachoque")
m("M-UT18-001", "UT18", "P27", "persona", "Pedro de la Mata", "Siquani Noviembre 8 de 1806 Muy Ylustre señor Firma Pedro de la Mata", rol="informante")
m("M-UT18-002", "UT18", "P27", "persona", "Doctor Don Agustin Valdes", "cura interino de dicho -Pueblo Doctor Don Agustin Valdes")

CITA_MATA = ("fueron hechos por el mismo Guancachoque haciéndolos firmar a los sujetos que los subscriben "
             "sin saber lo mas de sus contenidos")
for i, p in enumerate(["P01", "P03", "P04", "P05"], 1):
    a(f"A-UT17-{100 + i:03d}", "UT17", "P27", "M-UT18-001", "informante", {"pieza": p},
      "redacto", {"mencion": "M-UT17-005"}, CITA_MATA, fundamento="actuado",
      distribuida=True,
      nota="«Los Documentos que presento» se distribuye a cada certificación. P02 (Santiago Cazorla) se excluye: solo certifica el servicio militar.")
    a(f"A-UT17-{110 + i:03d}", "UT17", "P27", "M-UT18-001", "informante", {"pieza": p},
      "conoce-contenido", {"literal": "sin saber lo mas de sus contenidos"}, CITA_MATA, polaridad="niega", fundamento="actuado",
      distribuida=True, nota="Mismo reparto que A-UT17-10x.")
a("A-UT18-001", "UT18", "P27", "M-UT18-001", "informante", {"hecho": "H-p27-prision"},
  "duracion", {"literal": "esa misma noche ... al otro dia por la tarde"},
  "que lo guardasen en ella esa misma noche, al que puse en libertad al otro dia por la tarde", fundamento="experiencia-propia")
a("A-UT18-002", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT18-001"},
  "participa-en-hecho", {"hecho": "H-p27-prision"}, "lo mande llevar a la cárcel", rol_en_hecho="ordenante", fundamento="experiencia-propia")
a("A-UT18-003", "UT18", "P27", "M-UT18-001", "informante", {"mencion": "M-UT17-005"},
  "calificacion-de-conducta", {"literal": "falta de Religion, altanería , enemigo de la paz y sosiego"},
  "falta de Religion, altanería , enemigo de la paz y sosiego", fundamento="actuado",
  nota="Mata atribuye esta calificación al informe del cura («se inteligenciara… de la pésima que se le ha observado»).")

# ───────────── P28–P29 · Vista fiscal (20 nov.) y auto (26 nov.) · UT19–UT20 ─────────────
m("M-UT19-001", "UT19", "P29", "persona", "Manuel Guancoichoque", "las quejas dadas por Manuel Guancoichoque")
m("M-UT20-001", "UT20", "P29", "persona", "Gonzalo del Rio", "[Firma Gonzalo del Rio]", rol="firmante")
m("M-UT19-002", "UT19", "P28", "persona", "Muñoz", "Tomará el gobierno las más serias providencias. Muñoz", rol="firmante")

a("A-UT19-001", "UT19", "P29", "M-UT20-001", "dictaminador", {"pieza": "P06"},
  "veracidad", {"literal": "menos conforme a la verdad"},
  "resultando de este ser menos conforme a la verdad las quejas dadas por Manuel Guancoichoque", fundamento="actuado")
a("A-UT19-002", "UT19", "P29", "M-UT20-001", "dictaminador", {"mencion": "M-UT19-001"},
  "calificacion-de-conducta", {"literal": "mala conducta y genio discolo y arreva"},
  "por la mala conducta y genio discolo y arreva que se nota", fundamento="actuado")
m("M-UT19-003", "UT19", "P28", "persona", "subdelegado del partido de tinta", "librese la correspondiente orden al subdelegado del partido de tinta", rol="destinatario")
a("A-UT19-003", "UT19", "P28", "M-UT19-002", "resolutor", {"mencion": "M-UT19-003"},
  "ordena", {"literal": "contener los excesos y enemistad del yndio Guancachoque"},
  "a fin de contener los excesos y enemistad del yndio Guancachoque")
a("A-UT19-004", "UT19", "P28", "M-UT19-002", "resolutor", {"mencion": "M-UT19-002"},
  "se-conforma-con", {"pieza": "P29"}, "Visto de conformidad con lo supuesto por el señor Fiscal")


# ───────────── Revisión 1 · cargos de Chuquitapa según cuatro afirmantes (PC18) ─────────────
m("M-UT05-002", "UT05", "P06", "persona", "Don Andres Choquitapa", "tenia ocultos el recaudaderor Don Andres Choquitapa")
a("A-UT05-001", "UT05", "P06", "M-UT05-001", "denunciante", {"mencion": "M-UT05-002"},
  "ejerce-cargo", {"concepto": "recaudador-de-tributos"}, "tenia ocultos el recaudaderor Don Andres Choquitapa")
m("M-UT07-001", "UT07", "P07", "persona", "Son Andres Chuquitapa", "contra el Recaudador de Tributos Son Andres Chuquitapa")
m("M-UT08-001", "UT08", "P07", "persona", "Gómez del Rio", "Firma de Gómez del Rio", rol="firmante")
a("A-UT07-001", "UT07", "P07", "M-UT08-001", "dictaminador", {"mencion": "M-UT07-001"},
  "ejerce-cargo", {"concepto": "recaudador-de-tributos"}, "contra el Recaudador de Tributos Son Andres Chuquitapa")
m("M-UT17-006", "UT17", "P27", "persona", "Don Andres Chuquitapa", "recaudador de tributos de los Ayllus Tinta y Ucho Don Andres Chuquitapa")
a("A-UT17-003", "UT17", "P27", "M-UT18-001", "informante", {"mencion": "M-UT17-006"},
  "ejerce-cargo", {"concepto": "recaudador-de-tributos"}, "recaudador de tributos de los Ayllus Tinta y Ucho Don Andres Chuquitapa")
m("M-UT16b-001", "UT16.b", "P23", "persona", "Don Andres Chuquitapa", "su casique y alcalde mayor Don Andres Chuquitapa")
a("A-UT16b-001", "UT16.b", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16b-001"},
  "ejerce-cargo", {"concepto": "cacique"}, "su casique y alcalde mayor Don Andres Chuquitapa", nota=NOTA_CURA, otra=True)
a("A-UT16b-002", "UT16.b", "P23", "M-UT15-003", "informante", {"mencion": "M-UT16b-001"},
  "ejerce-cargo", {"concepto": "alcalde-mayor"}, "su casique y alcalde mayor Don Andres Chuquitapa", nota=NOTA_CURA, otra=True)

# ───────────── Revisión 1 · lugares y ayllus (PC07) ─────────────
m("M-UT05-003", "UT05", "P06", "grupo", "Ayllu Tinta", "cuarenta y cuatro tributarios en el Ayllu Tinta", tipo="ayllu")
m("M-UT05-004", "UT05", "P06", "grupo", "Ayllu nominado Uchu", "siete en el Ayllu nominado Uchu", tipo="ayllu")
m("M-UT05-005", "UT05", "P06", "lugar", "CUSCO", "CUSCO AGOSTO 22 DE 1806", tipo="ciudad")
m("M-UT17-007", "UT17", "P27", "grupo", "Ucho", "de los Ayllus Tinta y Ucho", tipo="ayllu")
m("M-UT02-006", "UT02", "P03", "lugar", "San Pedro de Cacha", "soldado del pueblo de San Pedro de Cacha", tipo="pueblo")
m("M-UT10-001", "UT10", "P14", "lugar", "Sicuani", "Sicuani Setiembre. 17 de 1806", tipo="pueblo")
a("A-UT05-002", "UT05", "P06", "M-UT05-001", "denunciante", {"mencion": "M-UT05-002"},
  "cantidad-denunciada", {"literal": "cuarenta y cuatro tributarios en el Ayllu Tinta y siete en el Ayllu nominado Uchu"},
  "el descubrimiento de cuarenta y cuatro tributarios en el Ayllu Tinta y siete en el Ayllu nominado Uchu")

# ───────────── Revisión 1 · condición atribuida al denunciante (PC17) ─────────────
a("A-UT05-003", "UT05", "P06", "M-UT05-001", "denunciante", {"mencion": "M-UT05-001"},
  "tiene-condicion", {"concepto": "originario"}, "Manuel Huancachoque Indio originario y vecino del pueblo de Tinta")
a("A-UT06-004", "UT06", "P06", "M-UT05-001", "denunciante", {"mencion": "M-UT05-001"},
  "tiene-condicion", {"concepto": "miliciano"},
  "por haber estado empleado en las milicias de aquella provincia, hasta aquí no había tributado")
a("A-UT06-005", "UT06", "P06", "M-UT05-001", "denunciante", {"mencion": "M-UT05-001"},
  "tiene-condicion", {"concepto": "tributario"}, "conseguido también el que se me matricule",
  nota="Afirma que se le ha matriculado (como tributario) y pide salir de la matrícula; no que sea tributario por derecho.")

# ───────────── Revisión 1 · fórmulas procesales (juramento, generales, firma a ruego) ─────────────
a("A-UT11-006", "UT11", "P18", "M-UT11-002", "fedatario", {"mencion": "M-UT11-001"},
  "presta-juramento", {"literal": "a Dios nuestro Señor y ….. Señal"}, "Le recibe juramento que lo hizo a Dios nuestro Señor")
a("A-UT12a-002", "UT12.a", "P18", "M-UT11-001", "declarante", {"mencion": "M-UT11-001"},
  "generales-de-la-ley", {"literal": "le comprenden los Generales de la Ley"}, "que no le comprenden. los Generales de la Ley",
  polaridad="niega")
m("M-UT12.a-007", "UT12.a", "P19", "persona", "ante mi", "Parecio ante mi el Gobernador Señor Don Mariano Casorla", rol="juez-comisionado")
a("A-UT13-002", "UT13", "P19", "M-UT12.a-005", "declarante", {"mencion": "M-UT12.a-005"},
  "generales-de-la-ley", {"literal": "la comprenden los grales"}, "q la comprenden los grales",
  nota="A diferencia de Cano (P18) y Orue (P21), este declarante dice que SÍ le comprenden las generales de la ley (posible tacha); la transcripción es defectuosa en este pasaje.")
a("A-UT13-003", "UT13", "P19", "M-UT12.a-007", "fedatario", {"pieza": "P19"},
  "firma-a-ruego", {"literal": "firma p no vaber, ruego"}, "y yo firma p no vaber, ruego",
  nota="Pasaje defectuoso en la transcripción; indica firma a ruego del juez por no saber firmar el declarante.")

# ───────────── Revisión 1 · autorreferencias de foliación (PC02) ─────────────
a("A-UT12a-003", "UT12.a", "P19", "M-UT12.a-007", "fedatario", {"pieza": "P05"},
  "folio-de-pieza", {"literal": "De folio 4"}, "De folio 4 su firma Martin casorla")
a("A-UT17-004", "UT17", "P24", "M-UT17-003", "resolutor", {"pieza": "P03"},
  "folio-de-pieza", {"literal": "a folios 2"}, "la Certificación a folios 2 extendida a nombre del teniente Alguacil")


if __name__ == "__main__":
    out = Path(__file__).with_suffix(".jsonl")
    with out.open("w", encoding="utf-8") as f:
        for r in M + A:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{len(M)} menciones, {len(A)} afirmaciones -> {out}")
