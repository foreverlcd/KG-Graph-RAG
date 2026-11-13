"""Anotación del expediente, lote B: tramos UT09, UT10, UT11, UT12.a, UT12.b, UT13 y UT14.

Completa lo que no anota el hilo central (hilo_central.py) en esos tramos: menciones de capa 2 (personas, grupos,
lugares y cosas tal como están escritos), participantes procesales de cada pieza (firmante, fedatario, receptor,
testigo de asistencia, notificado, destinatario…) y afirmaciones de capa 3. Las menciones ya anotadas en el hilo
central no se duplican: se reutilizan sus IDs. Ordinales 501–799 dentro de cada tramo.

Convenciones propias de este lote (además de las de hilo_central.py):
* «solicita»: el afirmante es quien lo cuenta; el sujeto es quien pide; el valor, lo pedido tal como se escribe.
* Las fórmulas de comparecencia («vecino Español», «el Gobernador…») y de juramento se atribuyen al juez que da
  fe (fedatario), no al declarante.
* Los anafóricos puros («dicho Señor», «vuestra Merced» repetido, «aquel») no se anotan como menciones, salvo la
  primera forma de tratamiento de un oficio y los sustantivos que nombran por función («el querello»).

Anotador: Claude Opus 5.5 (subagente), 2026-11-13. Lote: anotacion-manual-expediente-b-v1.
Ejecutar: python datos/registros/expediente_b.py  -> escribe expediente_b.jsonl
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


SOLICITA = ("Petición referida: el declarante es aquel a quien se pidió (sujeto, convención de atr:solicita) y refiere "
            "la súplica de Guancachoque (segun, fundamento oídas).")

# ───────────── P10 · Auto del 27 de agosto (Castilla, ante Chacón) · UT09 ─────────────
m("M-UT09-501", "UT09", "P10", "persona", "Señor Fiscal", "en conformidad a lo expuesta y pedido por el Señor Fiscal")
m("M-UT09-502", "UT09", "P10", "persona", "Juez subdelegado del partido de Tinta",
  "remitame al Juez subdelegado del partido de Tinta", rol="destinatario")
m("M-UT09-503", "UT09", "P10", "lugar", "partido de Tinta", "remitame al Juez subdelegado del partido de Tinta", tipo="partido")
m("M-UT09-504", "UT09", "P10", "persona", "Don Andrés Chuquitapa", "notificando primero al Recaudado Don Andrés Chuquitapa")
m("M-UT09-505", "UT09", "P10", "cosa", "su escrito", "sobre el bullicio azonada a parcialidad que expresa en su escrito el querello")
m("M-UT09-506", "UT09", "P10", "persona", "el querello", "que expresa en su escrito el querello haciendo al mismo tiempo")
m("M-UT09-507", "UT09", "P10", "cosa", "las fojas antecedentes", "se acompañan en las fojas antecedentes de ratifiquen")
m("M-UT09-508", "UT09", "P10", "persona", "dicho querello", "cuydando de que a dicho querello no se le incomode ni trate mal")
m("M-UT09-509", "UT09", "P10", "cosa", "la sumaria informasion", "a recivido la sumaria informasion correspondiente")
m("M-UT09-510", "UT09", "P10", "cosa", "su informe", "lo remita con su informe")
m("M-UT09-511", "UT09", "P10", "persona", "el denunciante", "la denuncia de tributarios y solicitud del denunciante")
m("M-UT09-512", "UT09", "P10", "persona", "Apoderado Fiscal", "oyendo sobre ellos al Apoderado Fiscal ynforme por ceparado")
m("M-UT09-513", "UT09", "P10", "persona", "Castilla", "Firma Castilla", rol="firmante")
m("M-UT09-514", "UT09", "P10", "persona", "Don Antonio Chacón", "Firma Don Antonio Chacón", rol="firmante")
m("M-UT09-515", "UT09", "P10", "cosa", "la denuncia de tributarios", "por lo que toca a la denuncia de tributarios y solicitud")

a("A-UT09-501", "UT09", "P10", "M-UT09-513", "resolutor", {"mencion": "M-UT09-513"},
  "se-conforma-con", {"pieza": "P07"}, "en conformidad a lo expuesta y pedido por el Señor Fiscal",
  nota="La pieza dictaminadora es la vista fiscal P07, la única del fiscal que antecede.")
a("A-UT09-502", "UT09", "P10", "M-UT09-513", "resolutor", {"mencion": "M-UT09-504"},
  "ejerce-cargo", {"concepto": "recaudador-de-tributos"}, "notificando primero al Recaudado Don Andrés Chuquitapa",
  nota="«Recaudado» por «Recaudador», tal como está escrito.")
a("A-UT09-503", "UT09", "P10", "M-UT09-513", "resolutor", {"mencion": "M-UT09-502"},
  "ejerce-cargo", {"concepto": "subdelegado"}, "remitame al Juez subdelegado del partido de Tinta")
a("A-UT09-504", "UT09", "P10", "M-UT09-513", "resolutor", {"mencion": "M-UT09-502"},
  "ordena", {"literal": "notificando primero al Recaudado Don Andrés Chuquitapa"},
  "para que notificando primero al Recaudado Don Andrés Chuquitapa como pide dicho Señor")
a("A-UT09-505", "UT09", "P10", "M-UT09-513", "resolutor", {"mencion": "M-UT09-502"},
  "ordena", {"literal": "ceparandolo en caso necesario que altas leguas en contrario fuera del pueblo"},
  "ceparandolo en caso necesario que altas leguas en contrario fuera del pueblo")
a("A-UT09-506", "UT09", "P10", "M-UT09-513", "resolutor", {"mencion": "M-UT09-502"},
  "ordena", {"literal": "proceda con la cautela y prudencia que exige el asunto"},
  "proceda con la cautela y prudencia que exige el asunto")
a("A-UT09-507", "UT09", "P10", "M-UT09-513", "resolutor", {"mencion": "M-UT09-502"},
  "ordena", {"literal": "a recivido la sumaria informasion correspondiente"},
  "a recivido la sumaria informasion correspondiente bajo las formalidades de escrito")
a("A-UT09-508", "UT09", "P10", "M-UT09-513", "resolutor", {"mencion": "M-UT09-502"},
  "ordena", {"literal": "que los cuyos otros se acompañan en las fojas antecedentes de ratifiquen y declaren"},
  "haciendo al mismo tiempo que los cuyos otros se acompañan en las fojas antecedentes de ratifiquen y declaren",
  nota="Orden de ratificar a los firmantes de las certificaciones (UT01–UT04) que acompañan el escrito.")
a("A-UT09-509", "UT09", "P10", "M-UT09-513", "resolutor", {"mencion": "M-UT09-502"},
  "ordena", {"literal": "cuydando de que a dicho querello no se le incomode ni trate mal"},
  "cuydando de que a dicho querello no se le incomode ni trate mal")
a("A-UT09-510", "UT09", "P10", "M-UT09-513", "resolutor", {"mencion": "M-UT09-502"},
  "ordena", {"literal": "lo remita con su informe"}, "lo remita con su informe")
a("A-UT09-511", "UT09", "P10", "M-UT09-513", "resolutor", {"mencion": "M-UT09-502"},
  "ordena", {"literal": "oyendo sobre ellos al Apoderado Fiscal ynforme por ceparado"},
  "por lo que toca a la denuncia de tributarios y solicitud del denunciante, oyendo sobre ellos al Apoderado Fiscal ynforme por ceparado")

# ───────────── P11 · Notificación del auto al fiscal · UT09 ─────────────
m("M-UT09-516", "UT09", "P11", "lugar", "Cuzco", "En el Cuzco en veinte y siete días del mes de Agosto", tipo="ciudad")
m("M-UT09-517", "UT09", "P11", "persona", "Yo el escrivano", "Cientos seis años. Yo el escrivano hice presente el auto que antecede",
  rol="fedatario")
m("M-UT09-518", "UT09", "P11", "persona", "Don Luis Gonsalo del Rio",
  "al -Señor Don Luis Gonsalo del Rio del Concejo de su Majestad", rol="notificado")
m("M-UT09-519", "UT09", "P11", "persona", "su Majestad", "del Concejo de su Majestad su único Fiscal")
m("M-UT09-520", "UT09", "P11", "lugar", "las casas de sus moradas", "estando en las casas de sus moradas doy fe", tipo="edificio")
m("M-UT09-521", "UT09", "P11", "persona", "Chacón", "doy fe .- Firma Chacón", rol="firmante")

a("A-UT09-512", "UT09", "P11", "M-UT09-517", "fedatario", {"mencion": "M-UT09-517"},
  "ejerce-cargo", {"concepto": "escribano"}, "Yo el escrivano hice presente el auto que antecede")
a("A-UT09-513", "UT09", "P11", "M-UT09-517", "fedatario", {"mencion": "M-UT09-518"},
  "ejerce-cargo", {"concepto": "fiscal-audiencia"}, "su único Fiscal en esta Real Audiencia")
a("A-UT09-514", "UT09", "P11", "M-UT09-517", "fedatario", {"mencion": "M-UT09-518"},
  "se-hallaba", {"mencion": "M-UT09-520"}, "estando en las casas de sus moradas doy fe", fundamento="vista")
a("A-UT09-515", "UT09", "P11", "M-UT09-517", "fedatario", {"mencion": "M-UT09-517"},
  "firmo", {"mencion": "M-UT09-521"}, "doy fe .- Firma Chacón",
  nota="La firma «Chacón» cierra la diligencia del escribano; se registra que la pieza la firma él.")

# ───────────── P12 · Notificación del auto a Guancachoque · UT09 ─────────────
m("M-UT09-522", "UT09", "P12", "persona", "Yo el escrivano", "En dicho día mes y año Yo el escrivano hice igual diligencia",
  rol="fedatario")
m("M-UT09-523", "UT09", "P12", "persona", "Manuel Guancachoque", "hice igual diligencia con Manuel Guancachoque en su persona",
  rol="notificado")
m("M-UT09-524", "UT09", "P12", "persona", "Chacón", "en su persona doy fe Firma Chacón", rol="firmante")

a("A-UT09-516", "UT09", "P12", "M-UT09-522", "fedatario", {"mencion": "M-UT09-523"},
  "se-hallaba", {"literal": "en su persona"}, "hice igual diligencia con Manuel Guancachoque en su persona doy fe",
  fundamento="vista", nota="Notificación personal: el notificado estaba presente.")

# ───────────── P13 · Oficio del Presidente al subdelegado (28 de agosto) · UT09 ─────────────
m("M-UT09-525", "UT09", "P13", "persona", "vuestra Merced", "En folio 10 remito a vuestra Merced un expediente", rol="destinatario")
m("M-UT09-526", "UT09", "P13", "cosa", "un expediente", "remito a vuestra Merced un expediente relativo a 51 yndios")
m("M-UT09-527", "UT09", "P13", "grupo", "51 yndios tributarios", "un expediente relativo a 51 yndios tributarios que ha denunciado")
m("M-UT09-528", "UT09", "P13", "persona", "Manuel Guancachoque", "que ha denunciado Manuel Guancachoque yndio del Pueblo de Tinta")
m("M-UT09-529", "UT09", "P13", "lugar", "Pueblo de Tinta", "yndio del Pueblo de Tinta te er ocultos", tipo="pueblo")
m("M-UT09-530", "UT09", "P13", "cosa", "matrícula", "te er ocultos y fuera de matrícula Don Andrés", tipo="matricula")
m("M-UT09-531", "UT09", "P13", "persona", "Don Andrés Choquetapa", "fuera de matrícula Don Andrés Choquetapa Recaudador de Reales Tributos")
m("M-UT09-532", "UT09", "P13", "cosa", "mi Auto de esté día", "evacue vuestra Merced quanto en mi Auto de esté día")
m("M-UT09-533", "UT09", "P13", "persona", "Señor Fiscal", "con arreglo a lo pedido por el Señor Fiscal se ordena")
m("M-UT09-534", "UT09", "P13", "lugar", "Cusco", "Cusco y Agosto 28 de 1806", tipo="ciudad")
m("M-UT09-535", "UT09", "P13", "persona", "Ruiz de Castilla", "(CAV) Ruiz de Castilla", rol="firmante")
m("M-UT09-536", "UT09", "P13", "persona", "subdelegado de Tinta", "Al subdelegado de Tinta", rol="destinatario")
m("M-UT09-537", "UT09", "P13", "lugar", "Tinta", "Al subdelegado de Tinta")

a("A-UT09-517", "UT09", "P13", "M-UT09-535", "resolutor", {"mencion": "M-UT09-526"},
  "folio-de-pieza", {"literal": "En folio 10"}, "En folio 10 remito a vuestra Merced un expediente",
  nota="Autorreferencia de foliación del expediente remitido (no es una pieza; el sujeto es la mención del expediente).")
a("A-UT09-518", "UT09", "P13", "M-UT09-535", "resolutor", {"mencion": "M-UT09-531"},
  "cantidad-denunciada", {"literal": "51 yndios tributarios"},
  "un expediente relativo a 51 yndios tributarios que ha denunciado Manuel Guancachoque yndio del Pueblo de Tinta te er ocultos y fuera de matrícula Don Andrés Choquetapa")
a("A-UT09-519", "UT09", "P13", "M-UT09-535", "resolutor", {"mencion": "M-UT09-528"},
  "tiene-condicion", {"concepto": "indio"}, "Manuel Guancachoque yndio del Pueblo de Tinta")
a("A-UT09-520", "UT09", "P13", "M-UT09-535", "resolutor", {"mencion": "M-UT09-531"},
  "ejerce-cargo", {"concepto": "recaudador-de-tributos"},
  "Don Andrés Choquetapa Recaudador de Reales Tributos de dicho Pueblo")
a("A-UT09-521", "UT09", "P13", "M-UT09-535", "resolutor", {"mencion": "M-UT09-525"},
  "ordena", {"literal": "evacue vuestra Merced quanto en mi Auto de esté día ... se ordena"},
  "a fin de que evacue vuestra Merced quanto en mi Auto de esté día y con arreglo a lo pedido por el Señor Fiscal se ordena")
a("A-UT09-522", "UT09", "P13", "M-UT09-535", "resolutor", {"mencion": "M-UT09-525"},
  "ordena", {"literal": "me de vuestra Merced cuenta de ellas"},
  "verificadas las diligencias correspondientes me de vuestra Merced cuenta de ellas")
a("A-UT09-523", "UT09", "P13", "M-UT09-535", "resolutor", {"mencion": "M-UT09-535"},
  "se-conforma-con", {"pieza": "P07"}, "con arreglo a lo pedido por el Señor Fiscal se ordena")

# ───────────── P14 · Providencia del subdelegado en Sicuani (17 de septiembre) · UT10 ─────────────
m("M-UT10-501", "UT10", "P14", "cosa", "la precedente Orden", "Por recibida la precedente Orden del muy ilustre señor presidente")
m("M-UT10-502", "UT10", "P14", "persona", "muy ilustre señor presidente", "la precedente Orden del muy ilustre señor presidente con el Expediente")
m("M-UT10-503", "UT10", "P14", "cosa", "Expediente", "con el Expediente en folio 10 que la acompaña")
m("M-UT10-504", "UT10", "P14", "cosa", "la denuncia", "respecto de que la denuncia que se halla al fin de el en folio 2")
m("M-UT10-505", "UT10", "P14", "persona", "Manuel Guancachoque", "hecha por el.Indio Manuel Guancachoque en 27 de Agosto")
m("M-UT10-506", "UT10", "P14", "grupo", "cinquenta y un Indios", "correspondiente de cinquenta y un Indios que dice tener ocultos")
m("M-UT10-507", "UT10", "P14", "cosa", "Matricula", "fuera de Matricula en el pueblo de Tinta", tipo="matricula")
m("M-UT10-508", "UT10", "P14", "lugar", "pueblo de Tinta", "fuera de Matricula en el pueblo de Tinta su recaudador", tipo="pueblo")
m("M-UT10-509", "UT10", "P14", "persona", "Dn Andres Chuquitapa", "su recaudador de tributos Dn Andres Chuquitapa, es la misma")
m("M-UT10-510", "UT10", "P14", "persona", "el mismo denunciante", "el mismo denunciante, y que se me remitio")
m("M-UT10-511", "UT10", "P14", "persona", "el subdelegado", "se me remitio ami el subdelegado, y al apoderado")
m("M-UT10-512", "UT10", "P14", "persona", "apoderado Fiscal de la presente Revicita",
  "y al apoderado Fiscal de la presente Revicita por el mismo")
m("M-UT10-513", "UT10", "P14", "persona", "Sr. Presidente", "por el mismo Sr. Presidente con fecha. 29 de mayo")
m("M-UT10-514", "UT10", "P14", "persona", "Magestad", "la defraudación que se hacia asu Magestad. cometida")
m("M-UT10-515", "UT10", "P14", "persona", "el citado re caudador", "cometida por el citado re caudador: Desglocese")
m("M-UT10-516", "UT10", "P14", "cosa", "este Expediente", "Desglocese de este Expediente, y agreguese")
m("M-UT10-517", "UT10", "P14", "cosa", "la primera denuncia", "agreguese a el de la primera denuncia, en el")
m("M-UT10-518", "UT10", "P14", "cosa", "el Informe", "eragua sea el Informe, que.se nos manda hacer")
m("M-UT10-519", "UT10", "P14", "persona", "M. Y. S. P.", "se devolvería a manos del M. Y. S. P. como lo tiene Ordenado")
m("M-UT10-520", "UT10", "P14", "lugar", "Pueblo de Tinta", "que se deben practicar en el Pueblo de Tinta con la cautela", tipo="pueblo")
m("M-UT10-521", "UT10", "P14", "persona", "Manuel Guancachoque", "el asunto que ha representado Manuel Guancachoque en aquel Superior Govierno")
m("M-UT10-522", "UT10", "P14", "persona", "el citado Guancachoque", "los hechos que ha expuesto el citado Guancachoque y con lo que resulte")
m("M-UT10-523", "UT10", "P14", "cosa", "Decreto de 27 de Agosto", "dese la Cuenta Ordenada por . Decreto de 27 de Agosto al presente año")
m("M-UT10-524", "UT10", "P14", "persona", "Pedro de la Mara", "Decreto de 27 de Agosto al presente año. Pedro de la Mara", rol="firmante")

MARA = "M-UT10-524"
a("A-UT10-501", "UT10", "P14", MARA, "resolutor", {"mencion": "M-UT10-503"},
  "folio-de-pieza", {"literal": "en folio 10"}, "con el Expediente en folio 10 que la acompaña",
  nota="Autorreferencia de foliación del expediente remitido; coincide con «En folio 10» del oficio P13.")
a("A-UT10-502", "UT10", "P14", MARA, "resolutor", {"pieza": "P06"},
  "folio-de-pieza", {"literal": "al fin de el en folio 2"}, "la denuncia que se halla al fin de el en folio 2",
  nota="«La denuncia… hecha por el Indio Manuel Guancachoque» se identifica con el escrito P06.")
a("A-UT10-503", "UT10", "P14", MARA, "resolutor", {"hecho": "H-p14-denuncia"},
  "fecha-del-hecho", {"literal": "en 27 de Agosto proximo pasado"},
  "hecha por el.Indio Manuel Guancachoque en 27 de Agosto proximo pasado",
  nota="Contradicción F3 (docs/01_materiales.md): el escrito P06 está datado el 22 de agosto y la carátula el 26.")
a("A-UT10-504", "UT10", "P14", MARA, "resolutor", {"mencion": "M-UT10-505"},
  "tiene-condicion", {"concepto": "indio"}, "hecha por el.Indio Manuel Guancachoque")
a("A-UT10-505", "UT10", "P14", MARA, "resolutor", {"mencion": "M-UT10-509"},
  "cantidad-denunciada", {"literal": "cinquenta y un Indios"},
  "correspondiente de cinquenta y un Indios que dice tener ocultos, y fuera de Matricula en el pueblo de Tinta su recaudador de tributos Dn Andres Chuquitapa")
a("A-UT10-506", "UT10", "P14", MARA, "resolutor", {"mencion": "M-UT10-509"},
  "ejerce-cargo", {"concepto": "recaudador-de-tributos"}, "su recaudador de tributos Dn Andres Chuquitapa")
a("A-UT10-507", "UT10", "P14", MARA, "resolutor", {"hecho": "H-p14-primera-denuncia"},
  "fecha-del-hecho", {"literal": "en once de Febrero del año pasado de 1809"},
  "es la misma que hizo en once de Febrero del año pasado de 1809, el mismo denunciante",
  nota="Contradicción F4: 1809 es posterior al documento (1806). Se conserva tal como está escrito.")
a("A-UT10-508", "UT10", "P14", MARA, "resolutor", {"hecho": "H-p14-remision-primera-denuncia"},
  "fecha-del-hecho", {"literal": "con fecha. 29 de mayo de este presente año"},
  "se me remitio ami el subdelegado, y al apoderado Fiscal de la presente Revicita por el mismo Sr. Presidente con fecha. 29 de mayo de este presente año")
a("A-UT10-509", "UT10", "P14", MARA, "resolutor", {"mencion": "M-UT10-511"},
  "ejerce-cargo", {"concepto": "subdelegado"}, "se me remitio ami el subdelegado")
a("A-UT10-510", "UT10", "P14", MARA, "resolutor", {"mencion": "M-UT10-512"},
  "ejerce-cargo", {"concepto": "apoderado-fiscal-revisita"}, "al apoderado Fiscal de la presente Revicita")
a("A-UT10-511", "UT10", "P14", MARA, "resolutor", {"mencion": "M-UT10-513"},
  "ejerce-cargo", {"concepto": "presidente-audiencia"}, "por el mismo Sr. Presidente con fecha. 29 de mayo",
  nota="«Presidente» sin más; se lee como presidente de la Real Audiencia del Cusco (el que firma P13).")
a("A-UT10-512", "UT10", "P14", MARA, "resolutor", {"mencion": "M-UT10-515"},
  "participa-en-hecho", {"hecho": "H-p14-defraudacion"},
  "el examen y Justificación de la defraudación que se hacia asu Magestad. cometida por el citado re caudador",
  rol_en_hecho="participante-en-hecho",
  nota="La defraudación es el objeto del examen encargado, no un hecho que el subdelegado dé por probado. "
       "El tesauro no tiene un rol de «autor» de un fraude; se usa el rol genérico.")
a("A-UT10-513", "UT10", "P14", MARA, "resolutor", {"mencion": "M-UT10-514"},
  "participa-en-hecho", {"hecho": "H-p14-defraudacion"}, "la defraudación que se hacia asu Magestad",
  rol_en_hecho="victima")
a("A-UT10-514", "UT10", "P14", MARA, "resolutor", {"mencion": "M-UT10-504"},
  "ordena", {"literal": "Desglocese de este Expediente, y agreguese a el de la primera denuncia"},
  "Desglocese de este Expediente, y agreguese a el de la primera denuncia",
  nota="Orden impersonal: el sujeto es la cosa afectada (la denuncia).")
a("A-UT10-515", "UT10", "P14", MARA, "resolutor", {"mencion": MARA},
  "ordena", {"literal": "Procedase por mi à tomar la información Correspondiente"},
  "Procedase por mi à tomar la información Correspondiente sobre los hechos que ha expuesto el citado Guancachoque")
a("A-UT10-516", "UT10", "P14", MARA, "resolutor", {"mencion": MARA},
  "ordena", {"literal": "hagase el correspondiente. informe, y dese la Cuenta Ordenada"},
  "con lo que resulte hagase el correspondiente. informe, y dese la Cuenta Ordenada por . Decreto de 27 de Agosto")
a("A-UT10-517", "UT10", "P14", MARA, "resolutor", {"mencion": MARA},
  "se-conforma-con", {"pieza": "P07"}, "con arreglo à lo pedido por el Minis terio Fiscal")

# ───────────── P15 · Nota de desglose (Tinta, 23 de septiembre) · UT10 ─────────────
m("M-UT10-525", "UT10", "P15", "cosa", "las dos fojas De denuncia y pedimiento", "Se agrego las dos fojas De denuncia y pedimiento")
m("M-UT10-526", "UT10", "P15", "cosa", "expediente de la primera denuncia",
  "al expediente de la primera denuncia que hiso Manuel Guancachoque")
m("M-UT10-527", "UT10", "P15", "persona", "Manuel Guancachoque", "la primera denuncia que hiso Manuel Guancachoque Tinta 23.")
m("M-UT10-528", "UT10", "P15", "lugar", "Tinta", "Manuel Guancachoque Tinta 23. de Septiembre de 1806")
# La nota no lleva firma ni nombre de quien la pone: sin afirmante posible en la pieza; no se crean afirmaciones.

# ───────────── P16 · Auto cabeza de la información (Mara, con testigos) · UT10–UT11 ─────────────
m("M-UT10-529", "UT10", "P16", "persona", "M. J. §. P.", "Información mandada ruenir pret M. J. §. P. sobre los hechos")
m("M-UT10-530", "UT10", "P16", "persona", "Manuel Guancachoque", "sobre los hechos que ha representado Manuel Guancachoque, y en cumplimiento")
m("M-UT10-531", "UT10", "P16", "cosa", "Auto que antecede", "en cumplimiento del . Auto que antecede, notifiquese")
m("M-UT10-532", "UT10", "P16", "persona", "D. Andres Chuquitapa", "notifiquese al recaudaor de tributos D. Andres Chuquitapa", rol="destinatario")
m("M-UT10-533", "UT10", "P16", "persona", "Guancachoque", "incomode ni infiera perjuicio, Guancachoque, en odio")
m("M-UT10-534", "UT10", "P16", "cosa", "su denuncia", "en odio de su denuncia bajose")
m("M-UT11-501", "UT11", "P16", "lugar", "Pueblo", "necerario separarlo de este que Pueblo interin se reune", tipo="pueblo")
m("M-UT11-502", "UT11", "P16", "cosa", "la expresada información", "interin se reune. la expresada información respecto.")
m("M-UT11-503", "UT11", "P16", "grupo", "todos los Indios", "A que todos los Indios que manifiesta la denuncia ultima")
m("M-UT11-504", "UT11", "P16", "cosa", "la denuncia ultima", "que manifiesta la denuncia ultima estan matriculados")
m("M-UT11-505", "UT11", "P16", "persona", "Chuquitapa", "haga de Saber a Chuquitapa se retire")
m("M-UT11-506", "UT11", "P16", "lugar", "este Pueblo", "se retire, de este Pueblo à distan.", tipo="pueblo")
m("M-UT11-507", "UT11", "P16", "persona", "Don Mariano Figueroa", "las diligencias que se van a practicar) por Don Mariano Figueroa")
m("M-UT11-508", "UT11", "P16", "persona", "Pedro de la Mara", "a falta de Escribano Pedro de la Mara", rol="firmante")
m("M-UT11-509", "UT11", "P16", "persona", "Mariano Figueroa", "Pedro de la Mara Mariano Figueroa", rol="testigo-de-asistencia")

MARA16 = "M-UT11-508"
a("A-UT10-518", "UT10", "P16", MARA16, "resolutor", {"mencion": "M-UT10-532"},
  "ejerce-cargo", {"concepto": "recaudador-de-tributos"}, "notifiquese al recaudaor de tributos D. Andres Chuquitapa")
a("A-UT10-519", "UT10", "P16", MARA16, "resolutor", {"mencion": "M-UT10-532"},
  "ordena", {"literal": "que mi si mi por medio de otro alguno incomode ni infiera perjuicio, Guancachoque, en odio de su denuncia"},
  "notifiquese al recaudaor de tributos D. Andres Chuquitapa; que mi si mi por medio de otro alguno incomode ni infiera perjuicio, Guancachoque, en odio de su denuncia",
  nota="Orden de no molestar al denunciante («que ni por sí ni por medio de otro», leído así; escrito «que mi si mi»).")
a("A-UT10-520", "UT10", "P16", MARA16, "resolutor", {"mencion": MARA16},
  "se-conforma-con", {"pieza": "P10"}, "en cumplimiento del . Auto que antecede",
  nota="«Auto que antecede»: se identifica con el auto del 27 de agosto (P10), que el oficio P13 manda evacuar.")
a("A-UT11-501", "UT11", "P16", MARA16, "resolutor", {"mencion": "M-UT11-503"},
  "tiene-condicion", {"concepto": "tributario"},
  "todos los Indios que manifiesta la denuncia ultima estan matriculados en la nueba revisita",
  nota="«Matriculados en la nueva revisita» se lee como inscritos en la matrícula de tributarios.")
a("A-UT11-502", "UT11", "P16", MARA16, "resolutor", {"mencion": "M-UT11-505"},
  "ordena", {"literal": "se retire, de este Pueblo à distan. cia de quatro leguas"},
  "haga de Saber a Chuquitapa se retire, de este Pueblo à distan. cia de quatro leguas")
a("A-UT11-503", "UT11", "P16", MARA16, "resolutor", {"mencion": "M-UT11-507"},
  "ordena", {"literal": "haga de Saber a Chuquitapa se retire"},
  "haga de Saber a Chuquitapa se retire, de este Pueblo à distan. cia de quatro leguas (interin de",
  nota="La notificación se encarga a Don Mariano Figueroa («por Don Mariano Figueroa»).")
a("A-UT11-504", "UT11", "P16", MARA16, "resolutor", {"pieza": "P16"},
  "firmo", {"mencion": MARA16}, "Asi lo provey y mande y firme con testigos a falta de Escribano")

# ───────────── P17 · Notificación a Chuquitapa (Figueroa) · UT11 ─────────────
m("M-UT11-510", "UT11", "P17", "persona", "D. Andre S. Chuquitape", "Inmediatamente le hize saber a D. Andre S. Chuquitape la procedencia",
  rol="notificado")
m("M-UT11-511", "UT11", "P17", "persona", "Mariano Figueroa", "lo que pongo por dirigido Mariano Figueroa.", rol="firmante")

a("A-UT11-505", "UT11", "P17", "M-UT11-511", "fedatario", {"pieza": "P16"},
  "conoce-contenido", {"mencion": "M-UT11-510"}, "en la persona que lo oyo y entendio el contenido de ella",
  fundamento="vista")
a("A-UT11-506", "UT11", "P17", "M-UT11-511", "fedatario", {"pieza": "P17"},
  "firmo", {"mencion": "M-UT11-510"}, "lo firmo con migo lo que pongo por dirigido",
  nota="La diligencia dice que el notificado firmó con el notificador, pero la transcripción solo trae la firma de Mariano Figueroa.")
a("A-UT11-507", "UT11", "P17", "M-UT11-511", "fedatario", {"pieza": "P17"},
  "firmo", {"mencion": "M-UT11-511"}, "lo firmo con migo lo que pongo por dirigido Mariano Figueroa.")

# ───────────── P18 · Declaración jurada de Isidro Cano (complemento) · UT11–UT12.a ─────────────
m("M-UT11-512", "UT11", "P18", "lugar", "pueblo de Tinta", "En el pueblo de Tinta, Veinte y tres dias del mes", tipo="pueblo")
m("M-UT11-513", "UT11", "P18", "cosa", "la certificación", "siendole manifestado la certificación De esta forma prima de este Expediente")
m("M-UT11-514", "UT11", "P18", "persona", "Don Andres", "sucedió en tiempo de corregidor Don Andres")
m("M-UT11-515", "UT11", "P18", "persona", "Tupa amaro", "en tiempo del rebelde Tupa amaro fue")
m("M-UT11-516", "UT11", "P18", "persona", "Guancachoque", "que estuvo preso Guancachoque de que todos los Yndios")
m("M-UT11-517", "UT11", "P18", "grupo", "todos los Yndios", "de que todos los Yndios se alzaron a media noche")
m("M-UT11-518", "UT11", "P18", "grupo", "los españoles", "hacer matalo de los españoles poniendo guardias")
m("M-UT11-519", "UT11", "P18", "lugar", "la caecel", "ponerlo en la caecel a Guancachoque", tipo="carcel")
m("M-UT11-520", "UT11", "P18", "persona", "Guancachoque", "ponerlo en la caecel a Guancachoque y que se")
m("M-UT11-521", "UT11", "P18", "grupo", "los Yndios", "le siguieron pegando los Yndios hasta que lo")
m("M-UT12.a-501", "UT12.a", "P18", "lugar", "la Real cárcel", "pusieron en la Real cárcel que es cuando pude", tipo="carcel")
m("M-UT12.a-502", "UT12.a", "P18", "persona", "Manuel Guancachoque", "sugerido de escuchado por Manuel Guancachoque para dar")
m("M-UT12.a-503", "UT12.a", "P18", "lugar", "su casa", "porque este fue a su casa supli candole", tipo="edificio")
m("M-UT12.a-504", "UT12.a", "P18", "cosa", "plata", "nomledio ninguna plata ni otro agasajo alguno")

CANO = "M-UT11-001"
MATA = "M-UT11-002"
a("A-UT11-508", "UT11", "P18", MATA, "fedatario", {"mencion": CANO},
  "tiene-condicion", {"concepto": "espanol"}, "la persona de D. Ysidro Cano vecino Español")
a("A-UT11-509", "UT11", "P18", MATA, "fedatario", {"mencion": CANO},
  "tiene-condicion", {"concepto": "vecino"}, "la persona de D. Ysidro Cano vecino Español de este amedicho pueblo")
a("A-UT11-510", "UT11", "P18", CANO, "declarante", {"mencion": "M-UT11-514"},
  "ejerce-cargo", {"concepto": "corregidor"}, "sucedió en tiempo de corregidor Don Andres",
  nota="Nombre truncado en la transcripción («Don Andres ……..»). Ver N8: otras piezas llaman al corregidor «Reparas».")
a("A-UT11-511", "UT11", "P18", CANO, "declarante", {"mencion": "M-UT11-516"},
  "participa-en-hecho", {"hecho": "H-p18-prision"}, "de la noche que estuvo preso Guancachoque", rol_en_hecho="preso")
a("A-UT11-512", "UT11", "P18", CANO, "declarante", {"mencion": "M-UT11-517"},
  "participa-en-hecho", {"hecho": "H-p18-alboroto"},
  "todos los Yndios se alzaron a media noche armados con garrotes para acabar con este",
  rol_en_hecho="agresor", fundamento="oidas", segun="M-UT11-003",
  nota="Cano dice que no le consta sino porque se lo dijo Santiago Casorla (ver A-UT11-005).")
a("A-UT11-513", "UT11", "P18", CANO, "declarante", {"mencion": "M-UT11-520"},
  "participa-en-hecho", {"hecho": "H-p18-golpes"}, "le siguieron pegando los Yndios hasta que lo",
  rol_en_hecho="victima", nota="El que recibe los golpes es Guancachoque (el «lo» de «hasta que lo pusieron en la Real cárcel»).")
a("A-UT11-514", "UT11", "P18", CANO, "declarante", {"mencion": "M-UT11-521"},
  "participa-en-hecho", {"hecho": "H-p18-golpes"}, "le siguieron pegando los Yndios hasta que lo", rol_en_hecho="agresor")
a("A-UT11-515", "UT11", "P18", CANO, "declarante", {"mencion": "M-UT11-520"},
  "participa-en-hecho", {"hecho": "H-p18-prision"}, "habiendo mandado Esta ponerlo en la caecel a Guancachoque",
  rol_en_hecho="preso", nota="Quién manda ponerlo en la cárcel («Esta») no se lee con claridad; no se anota ordenante.")
a("A-UT12a-501", "UT12.a", "P18", CANO, "declarante", {"hecho": "H-p18-golpes"},
  "lugar-del-hecho", {"mencion": "M-UT12.a-501"}, "pusieron en la Real cárcel que es cuando pude",
  nota="Los golpes duran hasta que lo meten en la Real cárcel (la frase empieza en UT11).")
a("A-UT12a-502", "UT12.a", "P18", CANO, "declarante", {"mencion": CANO},
  "edad", {"literal": "quarenta años"}, "expreso ser de edad de quarenta años")
a("A-UT12a-503", "UT12.a", "P18", CANO, "declarante", {"pieza": "P18"},
  "ratifica-contenido", {"mencion": CANO}, "vajo del juramento dicho tiene en que se afirma y ratifica")
a("A-UT12a-504", "UT12.a", "P18", CANO, "declarante", {"mencion": CANO},
  "solicita", {"literal": "le diere la dicha Certificacion"},
  "este fue a su casa supli candole que respecto a que sabia todos los parajes que expone en ella le diere la dicha Certificacion",
  segun="M-UT12.a-502", fundamento="oidas", nota=SOLICITA + " «Este» es Manuel Guancachoque, nombrado en la pregunta.")
a("A-UT12a-505", "UT12.a", "P18", CANO, "declarante", {"pieza": "P01"},
  "motivo", {"literal": "plata ni otro agasajo"}, "y que nomledio ninguna plata ni otro agasajo alguno",
  polaridad="niega", nota="Niega haber recibido dinero o agasajo por dar la certificación P01.")
a("A-UT12a-506", "UT12.a", "P18", MATA, "fedatario", {"pieza": "P18"},
  "firmo", {"mencion": "M-UT12.a-001"},
  "y lo firmo juntamente conmigo y testigos de mi asistencia a falta de Escribano")

# ───────────── P19 · Declaración sobre la certificación «Martin casorla» (complemento) · UT12.a–UT13 ─────────────
m("M-UT12.a-505", "UT12.a", "P19", "lugar", "pueblo de Tinta", "vecino Español de este pueblo de Tinta a quien", tipo="pueblo")
m("M-UT12.a-506", "UT12.a", "P19", "cosa", "la certificación", "siendole manifestado la certificación De folio 4")
m("M-UT12.b-501", "UT12.b", "P19", "persona", "Manuel Guancacho que", "es cierto que Manuel Guancacho que le suplico")
m("M-UT12.b-502", "UT12.b", "P19", "grupo", "los Yndios", "Certificacion de que los Yndios que lo llevaban preso")
m("M-UT12.b-503", "UT12.b", "P19", "lugar", "la cárcel", "que lo llevaban preso ala cárcel o alguno", tipo="carcel")
m("M-UT12.b-504", "UT12.b", "P19", "grupo", "alguno parien tes de Chuquitapa", "o alguno parien tes de Chuquitapa lo golpeaban")
m("M-UT12.b-505", "UT12.b", "P19", "persona", "Chuquitapa", "parien tes de Chuquitapa lo golpeaban con puñadas")
m("M-UT12.b-506", "UT12.b", "P19", "cosa", "un papelito", "que pusiere en un papelito lo mis mo")
m("M-UT12.b-507", "UT12.b", "P19", "cosa", "el papel", "firmo su nombre en el papel que se le ha manifestado")
m("M-UT12.b-508", "UT12.b", "P19", "persona", "Guancachoque", "se le castigaba a Guancachoque por haber denunciado")
m("M-UT12.b-509", "UT12.b", "P19", "persona", "Guancachoque", "sabia haber preso a Guancachoque,y que esto")
m("M-UT12.b-510", "UT12.b", "P19", "lugar", "la carcel", "porque estando en la carcel aquel dijo", tipo="carcel")
m("M-UT12.b-511", "UT12.b", "P19", "persona", "el cacique", "denunciado el robo del cacique , en favor de la Real hacienda")
m("M-UT12.b-512", "UT12.b", "P19", "grupo", "los Yndios", "esa misma noche se alzaron los Yndios todos con barrotes")
m("M-UT12.b-513", "UT12.b", "P19", "cosa", "el papelito", "no los puso el en el papelito que mando hacer")
m("M-UT12.b-514", "UT12.b", "P19", "persona", "Simon Arce", "que mando hacer a Simon Arce que es verdad")
m("M-UT12.b-515", "UT12.b", "P19", "grupo", "quatro o seis Yndios", "vio a quatro o seis Yndios en la puerta de la carcel")
m("M-UT12.b-516", "UT12.b", "P19", "lugar", "la carcel", "en la puerta de la carcel con garrotes", tipo="carcel")
m("M-UT12.b-517", "UT12.b", "P19", "grupo", "los SS Jueses", "re mediado ahora los SS Jueses habrá nuebamente")
m("M-UT12.b-518", "UT12.b", "P19", "persona", "el Rebelde", "porque es desde el Rebelde")

MC = "M-UT12.a-005"
ANTE19 = "M-UT12.a-007"
a("A-UT12a-507", "UT12.a", "P19", ANTE19, "fedatario", {"mencion": MC},
  "ejerce-cargo", {"concepto": "gobernador"}, "Parecio ante mi el Gobernador Señor Don Mariano Casorla",
  nota="Cargo tal como lo escribe la transcripción; ver N4 sobre la identidad del declarante.")
a("A-UT12a-508", "UT12.a", "P19", ANTE19, "fedatario", {"mencion": MC},
  "tiene-condicion", {"concepto": "espanol"}, "Don Mariano Casorla vecino Español de este pueblo de Tinta")
a("A-UT12a-509", "UT12.a", "P19", ANTE19, "fedatario", {"mencion": MC},
  "tiene-condicion", {"concepto": "vecino"}, "Don Mariano Casorla vecino Español de este pueblo de Tinta")
a("A-UT12a-510", "UT12.a", "P19", ANTE19, "fedatario", {"mencion": MC},
  "presta-juramento", {"literal": "a Dios Nuestro Señor y A una señal de cruz segun derecho"},
  "a quien le re iciere juramento que lo hiso a Dios Nuestro Señor y A una señal de cruz segun derecho")
a("A-UT12b-501", "UT12.b", "P19", MC, "declarante", {"mencion": MC},
  "solicita", {"literal": "le diere Certificacion de que los Yndios que lo llevaban preso ala cárcel o alguno parien tes de Chuquitapa lo golpeaban con puñadas y patadas"},
  "es cierto que Manuel Guancacho que le suplico le diere Certificacion de que los Yndios que lo llevaban preso ala cárcel o alguno parien tes de Chuquitapa lo golpeaban con puñadas y patadas",
  segun="M-UT12.b-501", fundamento="oidas", nota=SOLICITA + " Los golpes son el contenido pedido para la certificación, no algo que el declarante afirme haber visto.")
a("A-UT12b-502", "UT12.b", "P19", MC, "declarante", {"mencion": "M-UT12.b-509"},
  "participa-en-hecho", {"hecho": "H-p19-prision"}, "que el no sabia haber preso a Guancachoque",
  rol_en_hecho="preso", fundamento="no-consta",
  nota="El declarante dice que no sabía que Guancachoque estuviera preso; a la vez refiere que habló con él «estando en la carcel».")
a("A-UT12b-503", "UT12.b", "P19", MC, "declarante", {"hecho": "H-p19-castigo"},
  "motivo", {"literal": "por haber denunciado el robo del cacique , en favor de la Real hacienda"},
  "estando en la carcel aquel dijo que lo castigaban por haber denunciado el robo del cacique , en favor de la Real hacienda",
  fundamento="oidas", segun="M-UT12.b-509", nota="«Aquel» remite a Guancachoque, nombrado en la frase anterior (M-UT12.b-509).")
a("A-UT12b-504", "UT12.b", "P19", MC, "declarante", {"mencion": "M-UT12.b-511"},
  "participa-en-hecho", {"hecho": "H-p19-robo"}, "lo castigaban por haber denunciado el robo del cacique",
  rol_en_hecho="participante-en-hecho", fundamento="oidas", segun="M-UT12.b-509",
  nota="Discurso referido de Guancachoque: el cacique como autor del «robo» denunciado. El tesauro no tiene rol de autor de un robo.")
a("A-UT12b-505", "UT12.b", "P19", MC, "declarante", {"mencion": "M-UT12.b-511"},
  "ejerce-cargo", {"concepto": "cacique"}, "denunciado el robo del cacique , en favor de la Real hacienda",
  fundamento="oidas", segun="M-UT12.b-509")
a("A-UT12b-506", "UT12.b", "P19", MC, "declarante", {"hecho": "H-p19-alboroto"},
  "lugar-del-hecho", {"mencion": "M-UT12.b-516"}, "vio a quatro o seis Yndios en la puerta de la carcel con garrotes",
  fundamento="vista")
a("A-UT12b-507", "UT12.b", "P19", MC, "declarante", {"mencion": "M-UT12.b-515"},
  "participa-en-hecho", {"hecho": "H-p19-alboroto"}, "vio a quatro o seis Yndios en la puerta de la carcel con garrotes",
  rol_en_hecho="participante-en-hecho", fundamento="vista",
  nota="Solo dice que estaban con garrotes a la puerta; no les atribuye agresión.")
a("A-UT12b-508", "UT12.b", "P19", MC, "declarante", {"pieza": "P05"},
  "redacto", {"mencion": "M-UT12.b-514"}, "no los puso el en el papelito que mando hacer a Simon Arce",
  nota="Segunda atribución del «papelito» a Simón Arce (la primera es A-UT12b-002).")
a("A-UT12b-509", "UT12.b", "P19", MC, "declarante", {"mencion": MC},
  "edad", {"literal": "en aquel entonces era muchacho"}, "porque en aquel entonces era muchacho y no le consta nada de esto",
  nota="Edad relativa al tiempo de la rebelión de 1780; motivo por el que niega las expresiones de A-UT12b-005.")
a("A-UT13-501", "UT13", "P19", MC, "declarante", {"pieza": "P19"},
  "ratifica-contenido", {"mencion": MC}, "dijo la misma q acaba de haser en q se afirma y ratifica")

# ───────────── P20 · Declaración jurada de Santiago Cazorla (24 de septiembre) · UT13–UT14 ─────────────
m("M-UT13-501", "UT13", "P20", "persona", "ante mi", "comparecio ante mi, via en este partido", rol="juez-comisionado")
m("M-UT13-502", "UT13", "P20", "lugar", "este partido", "via en este partido feretro segundo", tipo="partido")
m("M-UT13-503", "UT13", "P20", "grupo", "la compañia", "feretro segundo en la compañia en este fue", tipo="compania-milicias")
m("M-UT13-504", "UT13", "P20", "persona", "manuel guancachoque", "la noche q manuel guancachoque estubo en la carcel")
m("M-UT13-505", "UT13", "P20", "lugar", "la carcel", "guancachoque estubo en la carcel asi primer sargento", tipo="carcel")
m("M-UT13-506", "UT13", "P20", "persona", "ysidro cano", "asi primer sargento ysidro cano, las palabras")
m("M-UT13-507", "UT13", "P20", "grupo", "todos los indios", "se q todos los indios alzaron a media noche")
m("M-UT13-508", "UT13", "P20", "persona", "guarcachoque", "armados con garrotes, guarcachoque hace una matanza")
m("M-UT13-509", "UT13", "P20", "grupo", "los españoles", "hace una matanza a contra los españoles poniendo guardias")
m("M-UT13-510", "UT13", "P20", "persona", "guancachoque", "de esa noche que estubo preso guancachoque vino a verlo")
m("M-UT13-511", "UT13", "P20", "persona", "madre rosa", "vino a verlo a madre rosa y esposa diciendo")
m("M-UT13-512", "UT13", "P20", "grupo", "los indios", "diciendo que los indios han dicho que quieren matar")
m("M-UT13-513", "UT13", "P20", "persona", "mi hijo", "quieren matar a mi hijo y a mi hermano")
m("M-UT13-514", "UT13", "P20", "persona", "juan de dios casorlas", "a mi hermano juan de dios casorlas cuyas expresiones")
m("M-UT13-515", "UT13", "P20", "persona", "sargento primero", "entrando sin sargento primero le dijo lo mismo")
m("M-UT13-516", "UT13", "P20", "grupo", "los indios", "si hubiera algun testamento de los indios si hubiera")
m("M-UT14-501", "UT14", "P20", "persona", "este hombre", "palabras q expreso este hombre declaracion")
m("M-UT14-502", "UT14", "P20", "grupo", "todos los indiosse", "de que todos los indiosse alzaron a media noche")
m("M-UT14-503", "UT14", "P20", "persona", "gancahoque", "escribir con gancahoque y haser matanza")
m("M-UT14-504", "UT14", "P20", "grupo", "los españoles", "haser matanza de los españoles poniendo guardias")
m("M-UT14-505", "UT14", "P20", "persona", "guancachoque", "desa noche que estubo preso guancachoque bino a verlo")
m("M-UT14-506", "UT14", "P20", "persona", "la madre", "bino a verlo la madre desay le expreso")
m("M-UT14-507", "UT14", "P20", "grupo", "los indios", "dise q los indios han dicho que quieren matar")
m("M-UT14-508", "UT14", "P20", "persona", "mi hijo", "quieren matar a mi hijo v. y a mi hermano")
m("M-UT14-509", "UT14", "P20", "persona", "Juan se Dios cazorla", "a mi hermano Juan se Dios cazorla cuyas expresiones")

SC = "M-UT13-001"
ANTE20 = "M-UT13-501"
NOTA_REP = ("UT13 y UT14 repiten la declaración con variantes (docs/01_materiales.md §4.1, «Repetición»); "
            "se anota cada ocurrencia sin fusionar.")
a("A-UT13-502", "UT13", "P20", ANTE20, "fedatario", {"mencion": SC},
  "presta-juramento", {"literal": "i dios, son ya una señal cruz"}, "quien le brindo juramento q lo hiso i dios, son ya una señal cruz")
a("A-UT13-503", "UT13", "P20", ANTE20, "fedatario", {"mencion": SC},
  "ejerce-cargo", {"concepto": "sargento-segundo"}, "feretro segundo en la compañia en este fue santiago cacerola",
  nota="Lectura dudosa: «feretro segundo en la compañia» se interpreta como «sargento segundo»; concuerda con "
       "«su segundo sargento Santiago Casorla» (UT11) y discrepa de «sargento primero» (UT02). Ver N9.")
a("A-UT13-504", "UT13", "P20", ANTE20, "fedatario", {"mencion": "M-UT13-506"},
  "ejerce-cargo", {"concepto": "sargento-primero"}, "asi primer sargento ysidro cano, las palabras",
  nota="En la pregunta del juez. Cano se llama a sí mismo «el sargento» (UT01).")
a("A-UT13-505", "UT13", "P20", ANTE20, "fedatario", {"mencion": "M-UT13-506"},
  "dijo", {"literal": "todos los indios alzaron a media noche armados con garrotes"},
  "las palabras q expresso este en declaración, se q todos los indios alzaron a media noche armados con garrotes",
  fundamento="actuado",
  nota="El juez resume, en la pregunta, lo que Cano declaró atribuyéndolo a Santiago Cazorla (A-UT11-005).")
a("A-UT13-506", "UT13", "P20", SC, "declarante", {"mencion": "M-UT13-510"},
  "participa-en-hecho", {"hecho": "H-p20-prision"}, "de esa noche que estubo preso guancachoque", rol_en_hecho="preso")
a("A-UT13-507", "UT13", "P20", SC, "declarante", {"hecho": "H-p20-visita"},
  "fecha-del-hecho", {"literal": "a las dos o tres de la madrugada de esa noche"},
  "que a las dos o tres de la madrugada de esa noche que estubo preso guancachoque vino a verlo",
  fundamento="experiencia-propia", nota=NOTA_REP)
a("A-UT13-508", "UT13", "P20", SC, "declarante", {"mencion": "M-UT13-511"},
  "dijo", {"literal": "los indios han dicho que quieren matar a mi hijo y a mi hermano juan de dios casorlas"},
  "vino a verlo a madre rosa y esposa diciendo que los indios han dicho que quieren matar a mi hijo y a mi hermano juan de dios casorlas",
  fundamento="oidas", segun="M-UT13-511",
  nota="Lectura dudosa de «a madre rosa y esposa» (¿su madre Rosa y su esposa?). " + NOTA_REP)
a("A-UT13-509", "UT13", "P20", SC, "declarante", {"mencion": SC},
  "dijo", {"literal": "no estamos en tierra de herejes"},
  "cuyas expresiones desaprecio diciendo q era en una definida q no estamos en tierra de herejes p q no maten como perros",
  fundamento="experiencia-propia")
a("A-UT13-510", "UT13", "P20", SC, "declarante", {"mencion": SC},
  "dijo", {"literal": "le dijo lo mismo"}, "entrando sin sargento primero le dijo lo mismo que lleva",
  responde_a="A-UT11-005", fundamento="experiencia-propia",
  nota="Lectura: «entrando su sargento primero le dijo lo mismo». Matiza A-UT11-005: lo que contó a Cano fue la "
       "amenaza referida por la madre, no que los indios se alzaran a media noche.")
a("A-UT14-501", "UT14", "P20", SC, "declarante", {"pieza": "P20"},
  "ratifica-contenido", {"mencion": SC}, "que acaba de haser es que se afirma y que justifica", nota=NOTA_REP)
a("A-UT14-502", "UT14", "P20", SC, "declarante", {"mencion": SC},
  "edad", {"literal": "sesenta años"}, "expresso ser en la edad de sesenta años", nota=NOTA_REP)
a("A-UT14-503", "UT14", "P20", SC, "declarante", {"hecho": "H-p20-visita"},
  "fecha-del-hecho", {"literal": "a los dos o tres dias desa noche"},
  "que a los dos o tres dias desa noche que estubo preso guancachoque bino a verlo",
  fundamento="experiencia-propia", nota="Variante de A-UT13-507 («de la madrugada» frente a «dias»). " + NOTA_REP)
a("A-UT14-504", "UT14", "P20", SC, "declarante", {"mencion": "M-UT14-505"},
  "participa-en-hecho", {"hecho": "H-p20-prision"}, "desa noche que estubo preso guancachoque", rol_en_hecho="preso",
  nota=NOTA_REP)
a("A-UT14-505", "UT14", "P20", SC, "declarante", {"mencion": "M-UT14-506"},
  "dijo", {"literal": "los indios han dicho que quieren matar a mi hijo v. y a mi hermano Juan se Dios cazorla"},
  "bino a verlo la madre desay le expreso diciendo que dise q los indios han dicho que quieren matar a mi hijo v. y a mi hermano Juan se Dios cazorla",
  fundamento="oidas", segun="M-UT14-506", nota=NOTA_REP)
a("A-UT14-506", "UT14", "P20", SC, "declarante", {"mencion": SC},
  "dijo", {"literal": "no estamos enn tierras de herejes"},
  "cuyas expresiones desaparecio diciendo esa es una bufanda no estamos enn tierras de herejes", fundamento="experiencia-propia",
  nota=NOTA_REP)
a("A-UT14-507", "UT14", "P20", SC, "declarante", {"pieza": "P20"},
  "ratifica-contenido", {"mencion": SC}, "cuando se haser se afirma y ratifica", nota=NOTA_REP)
a("A-UT14-508", "UT14", "P20", SC, "declarante", {"mencion": SC},
  "edad", {"literal": "sesenta años"}, "expreso ser de de edad de sesenta años", nota=NOTA_REP)
a("A-UT14-509", "UT14", "P20", SC, "declarante", {"mencion": SC},
  "generales-de-la-ley", {"literal": "lo comprenden los generales de la ley"}, "y que no lo comprenden los generales de la ley",
  polaridad="niega")
a("A-UT14-510", "UT14", "P20", ANTE20, "fedatario", {"pieza": "P20"},
  "firmo", {"mencion": SC}, "la forma juntamente conmigo y testigos de mi asistencia de escribano",
  nota="Se lee «la forma» como «la firma» (fórmula de cierre: firma con el juez y los testigos de asistencia "
       "a falta de escribano). La transcripción no trae las firmas.")

# ───────────── P21 · Declaración jurada de Fernando Orue (complemento) · UT14 ─────────────
m("M-UT14-510", "UT14", "P21", "persona", "fernando orue", "si la firma q dise fernando orue presenta en la certificacion")
m("M-UT14-511", "UT14", "P21", "cosa", "la certificacion de este expediente", "presenta en la certificacion de este expediente es echa")
m("M-UT14-512", "UT14", "P21", "persona", "guancachoque", "privado la prision de guancachoqueel q es ahijado")
m("M-UT14-513", "UT14", "P21", "persona", "hermano mayor del q declaro", "es ahijado del hermano mayor del q declaro le llebo")
m("M-UT14-514", "UT14", "P21", "persona", "un hijo suyo", "bajo a un hijo suyo q la pusieron")
m("M-UT14-515", "UT14", "P21", "grupo", "indios", "el aboroto q dise de indios advirtió")
m("M-UT14-516", "UT14", "P21", "lugar", "la carcel", "advirtió a la puerta de la carcel y q estaban ebrios", tipo="carcel")
m("M-UT14-517", "UT14", "P21", "persona", "tupa-amaru", "en tiempo del rebelde tupa-amaru coronel")
m("M-UT14-518", "UT14", "P21", "persona", "insurgente tupa", "a fabor del insurgente tupa aunque")
m("M-UT14-519", "UT14", "P21", "persona", "d juan antonio repuras", "del sor corregidor d juan antonio repuras haviendo")
m("M-UT14-520", "UT14", "P21", "persona", "Diego orue", "un muchacho Diego orue sobrino del q declaran")
m("M-UT14-521", "UT14", "P21", "cosa", "un caballo", "a vacar un caballo del corral de chuquitapa")
m("M-UT14-522", "UT14", "P21", "lugar", "corral de chuquitapa", "un caballo del corral de chuquitapa lo mando")
m("M-UT14-523", "UT14", "P21", "persona", "chuquitapa", "del corral de chuquitapa lo mando poner")
m("M-UT14-524", "UT14", "P21", "lugar", "la carcel", "lo mando poner a la carcel con sus propios criados", tipo="carcel")
m("M-UT14-525", "UT14", "P21", "grupo", "sus propios criados", "a la carcel con sus propios criados de lo q resulto")
m("M-UT14-526", "UT14", "P21", "grupo", "mosos indios", "se juntaronmosos indios y lo votaron")
m("M-UT14-527", "UT14", "P21", "lugar", "la carcel", "lo votaron de la carcel y q se amotinaron", tipo="carcel")
m("M-UT14-528", "UT14", "P21", "persona", "el corregidor", "se amotinaron contra el corregidor y contra el padre")
m("M-UT14-529", "UT14", "P21", "persona", "el padre del que declara", "contra el padre del que declara q era cobrador")
m("M-UT14-530", "UT14", "P21", "lugar", "casa del corregidor", "refugiandose todos en casa del corregidor", tipo="edificio")
m("M-UT14-531", "UT14", "P21", "grupo", "toda su familia", "han ocasionado a toda su familia el dicho chuquitapa")
m("M-UT14-532", "UT14", "P21", "persona", "el dicho chuquitapa", "a toda su familia el dicho chuquitapa")

FO = "M-UT14-001"
ANTE21 = "M-UT14-004"
a("A-UT14-511", "UT14", "P21", ANTE21, "fedatario", {"mencion": FO},
  "ejerce-cargo", {"concepto": "soldado"}, "el soldado fernando ore vecino español")
a("A-UT14-512", "UT14", "P21", ANTE21, "fedatario", {"mencion": FO},
  "tiene-condicion", {"concepto": "espanol"}, "el soldado fernando ore vecino español")
a("A-UT14-513", "UT14", "P21", ANTE21, "fedatario", {"mencion": FO},
  "tiene-condicion", {"concepto": "vecino"}, "el soldado fernando ore vecino español")
a("A-UT14-514", "UT14", "P21", ANTE21, "fedatario", {"mencion": FO},
  "presta-juramento", {"literal": "a dios y que una señal de cruz"}, "quien le decia juramento que los hijos a dios y que una señal de cruz")
a("A-UT14-515", "UT14", "P21", FO, "declarante", {"pieza": "P04"},
  "autenticidad-firma", {"mencion": FO}, "no obstante que sabe firmar el declarante no quiso hacerlo", polaridad="niega",
  nota="Respuesta a la pregunta de si la firma «fernando orue» de la certificación es de su puño y letra; ver A-UT14-001.")
a("A-UT14-516", "UT14", "P21", FO, "declarante", {"mencion": FO},
  "sabe-firmar", {"literal": "sabe firmar"}, "no obstante que sabe firmar el declarante no quiso hacerlo")
a("A-UT14-517", "UT14", "P21", FO, "declarante", {"mencion": FO},
  "solicita", {"literal": "firmase dicha certificacion"},
  "guancachoqueel q es ahijado del hermano mayor del q declaro le llebo p q firmase dicha certificacion",
  segun="M-UT14-512", fundamento="oidas", nota=SOLICITA)
a("A-UT14-518", "UT14", "P21", FO, "declarante", {"mencion": "M-UT14-512"},
  "parentesco", {"mencion": "M-UT14-513"}, "guancachoqueel q es ahijado del hermano mayor del q declaro",
  nota="Tipo de parentesco escrito: «ahijado».")
a("A-UT14-519", "UT14", "P21", FO, "declarante", {"mencion": "M-UT14-513"},
  "parentesco", {"mencion": FO}, "es ahijado del hermano mayor del q declaro", nota="Tipo de parentesco escrito: «hermano mayor».")
a("A-UT14-520", "UT14", "P21", FO, "declarante", {"hecho": "H-p21-alboroto"},
  "lugar-del-hecho", {"mencion": "M-UT14-516"}, "q el aboroto q dise de indios advirtió a la puerta de la carcel")
a("A-UT14-521", "UT14", "P21", FO, "declarante", {"mencion": "M-UT14-515"},
  "participa-en-hecho", {"hecho": "H-p21-alboroto"}, "q el aboroto q dise de indios advirtió a la puerta de la carcel",
  rol_en_hecho="participante-en-hecho")
a("A-UT14-522", "UT14", "P21", FO, "declarante", {"mencion": "M-UT14-515"},
  "calificacion-de-conducta", {"literal": "estaban ebrios"}, "advirtió a la puerta de la carcel y q estaban ebrios")
a("A-UT14-523", "UT14", "P21", FO, "declarante", {"pieza": "P04"},
  "motivo", {"literal": "con motibo de saber q de andres chuquitaza fue en tiempo del rebelde tupa-amaru coronel y comisionado"},
  "con motibo de saber q de andres chuquitaza fue en tiempo del rebelde tupa-amaru coronel y comisionado puso las expresiones de a fabor del insurgente tupa")
a("A-UT14-524", "UT14", "P21", FO, "declarante", {"mencion": "M-UT14-519"},
  "ejerce-cargo", {"concepto": "corregidor"}, "en tiempo del sor corregidor d juan antonio repuras")
a("A-UT14-525", "UT14", "P21", FO, "declarante", {"mencion": "M-UT14-520"},
  "parentesco", {"mencion": FO}, "un muchacho Diego orue sobrino del q declaran", nota="Tipo de parentesco escrito: «sobrino».")
a("A-UT14-526", "UT14", "P21", FO, "declarante", {"mencion": "M-UT14-523"},
  "participa-en-hecho", {"hecho": "H-p21-prision-diego"},
  "a vacar un caballo del corral de chuquitapa lo mando poner a la carcel con sus propios criados", rol_en_hecho="ordenante")
a("A-UT14-527", "UT14", "P21", FO, "declarante", {"mencion": "M-UT14-520"},
  "participa-en-hecho", {"hecho": "H-p21-prision-diego"},
  "haviendo ido un muchacho Diego orue sobrino del q declaran a vacar un caballo del corral de chuquitapa lo mando poner a la carcel",
  rol_en_hecho="preso")
a("A-UT14-528", "UT14", "P21", FO, "declarante", {"hecho": "H-p21-prision-diego"},
  "fecha-del-hecho", {"literal": "en tiempo del sor corregidor d juan antonio repuras"},
  "en tiempo del sor corregidor d juan antonio repuras haviendo ido un muchacho Diego orue")
a("A-UT14-529", "UT14", "P21", FO, "declarante", {"hecho": "H-p21-prision-diego"},
  "motivo", {"literal": "a vacar un caballo del corral de chuquitapa"},
  "haviendo ido un muchacho Diego orue sobrino del q declaran a vacar un caballo del corral de chuquitapa")
a("A-UT14-530", "UT14", "P21", FO, "declarante", {"mencion": "M-UT14-526"},
  "participa-en-hecho", {"hecho": "H-p21-motin"},
  "esa misma noche se juntaronmosos indios y lo votaron de la carcel y q se amotinaron contra el corregidor",
  rol_en_hecho="agresor")
a("A-UT14-531", "UT14", "P21", FO, "declarante", {"hecho": "H-p21-motin"},
  "fecha-del-hecho", {"literal": "esa misma noche"}, "de lo q resulto q esa misma noche se juntaronmosos indios")
a("A-UT14-532", "UT14", "P21", FO, "declarante", {"mencion": "M-UT14-528"},
  "participa-en-hecho", {"hecho": "H-p21-motin"}, "se amotinaron contra el corregidor y contra el padre del que declara",
  rol_en_hecho="victima")
a("A-UT14-533", "UT14", "P21", FO, "declarante", {"mencion": "M-UT14-529"},
  "participa-en-hecho", {"hecho": "H-p21-motin"},
  "se amotinaron contra el corregidor y contra el padre del que declara q era cobrador del departamento en cuya noche le vaguear y maltrataron",
  rol_en_hecho="victima",
  nota="Cargo escrito «cobrador del departamento»: no hay concepto equivalente en tes:cargos; no se anota ejerce-cargo.")
a("A-UT14-534", "UT14", "P21", FO, "declarante", {"mencion": "M-UT14-529"},
  "parentesco", {"mencion": FO}, "contra el padre del que declara", nota="Tipo de parentesco escrito: «padre».")
a("A-UT14-535", "UT14", "P21", FO, "declarante", {"hecho": "H-p21-motin"},
  "lugar-del-hecho", {"mencion": "M-UT14-530"}, "refugiandose todos en casa del corregidor",
  nota="Lugar del refugio de los agredidos durante el motín.")
a("A-UT14-536", "UT14", "P21", FO, "declarante", {"pieza": "P04"},
  "motivo", {"literal": "este agravio y perjuicio que han ocasionado a toda su familia el dicho chuquitapa"},
  "q con este motivo converso siempre este agravio y perjuicio que han ocasionado a toda su familia el dicho chuquitapa",
  nota="Enemistad con Chuquitapa como motivo de lo puesto en la certificación P04 (lectura de un pasaje defectuoso).")
a("A-UT14-537", "UT14", "P21", FO, "declarante", {"pieza": "P21"},
  "ratifica-contenido", {"mencion": FO}, "dijo ser la que acaba de haser en laque se afirma")


if __name__ == "__main__":
    out = Path(__file__).with_suffix(".jsonl")
    with out.open("w", encoding="utf-8") as f:
        for r in M + A:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{len(M)} menciones, {len(A)} afirmaciones -> {out}")
