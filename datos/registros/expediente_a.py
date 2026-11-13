"""Anotación completa de los tramos UT00–UT08 (piezas P00–P09), lote A.

Completa lo que ya anota el hilo central (datos/registros/hilo_central.py) sin duplicar menciones: cuando una
aparición escrita ya tiene mención en el hilo central, se reutiliza su id. Mismo esquema plano
(src/laad/esquema.py) y mismas convenciones. Ordinales 201–499 dentro de cada tramo.

Decisiones generales del anotador:
* P00 (carátula) no nombra a su autor: se anotan sus menciones, pero no afirmaciones (no hay afirmante).
* Las peticiones de la vista fiscal al Presidente se registran como «solicita» (el fiscal no ordena; propone).
* Los hechos narrados son locales a cada pieza (H-pNN-…); su identidad entre piezas es capa 4.
* Las referencias descriptivas («dicho denunciante», «el subdelegado») son menciones propias; la
  correferencia se deja para la capa 4.

Anotador: Claude Opus 5.5 (subagente), 2026-11-13. Lote: anotacion-manual-expediente-a-v1.
Ejecutar: python datos/registros/expediente_a.py  -> escribe expediente_a.jsonl
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


# ───────────── P00 · Carátula · UT00 ─────────────
m("M-UT00-201", "UT00", "P00", "persona", "Manuel Mancachoque", "Expediente seguido por el indio Manuel Mancachoque")
m("M-UT00-202", "UT00", "P00", "grupo", "Ayllo Tinta", "le ha inferido el casique del Ayllo Tinta", tipo="ayllu")
m("M-UT00-203", "UT00", "P00", "persona", "D. Andres Chuquitapa", "el casique del Ayllo Tinta D. Andres Chuquitapa")
m("M-UT00-204", "UT00", "P00", "cosa", "matricula", "se le borre de la matricula en que lo han numerado", tipo="matricula")
m("M-UT00-205", "UT00", "P00", "grupo", "Real Hacienda", "Instancia Real Hacienda")
# Sin afirmaciones: la carátula no nombra autor (ni escribano ni archivero) que pueda ser afirmante.

# ───────────── P01 · Certificación de Isidro Cano · UT01 ─────────────
m("M-UT01-201", "UT01", "P01", "grupo", "compañía de Tinta de Milicias", "de esta compañía de Tinta de Milicias de este cuerpo",
  tipo="compania-milicias")
m("M-UT01-202", "UT01", "P01", "grupo", "regimiento de este partido", "del regimiento de este partido sertifico")
m("M-UT01-203", "UT01", "P01", "lugar", "este partido", "del regimiento de este partido sertifico", tipo="partido")
m("M-UT01-204", "UT01", "P01", "grupo", "sus enemigos", "lo esta lo estropearon sus enemigos lo tendieron")
m("M-UT01-205", "UT01", "P01", "lugar", "la carcel", "lo pusieron a la carcel a esa noche", tipo="carcel")
m("M-UT01-206", "UT01", "P01", "grupo", "todos los indios", "todos los indios se alzaron a media noche")
m("M-UT01-207", "UT01", "P01", "persona", "dicho denunciante", "a acabar al dicho denunciante y animados")
m("M-UT01-208", "UT01", "P01", "grupo", "los españoles", "hacen una matanza a los españoles")
m("M-UT01-209", "UT01", "P01", "lugar", "la plaza", "porque estaba cubierto de indiada la plaza", tipo="plaza")
m("M-UT01-210", "UT01", "P01", "grupo", "indiada", "porque estaba cubierto de indiada la plaza")
m("M-UT01-211", "UT01", "P01", "persona", "don Antonio Reparas", "En tiempo del señor corregidor don Antonio Reparas")
m("M-UT01-212", "UT01", "P01", "cosa", "Chicha", "cargando. [....] y Chicha ay se alzaron")
m("M-UT01-213", "UT01", "P01", "persona", "don Miguel Orey", "se alzaron contra el capitan don Miguel Orey")
m("M-UT01-214", "UT01", "P01", "grupo", "cerca de sesenta indios", "con pedradas palos cerca de sesenta indios")
m("M-UT01-215", "UT01", "P01", "lugar", "su tienda", "pedrearon su tienda hasta quebrar la puerta", tipo="edificio")
m("M-UT01-216", "UT01", "P01", "persona", "capitán Orey", "Y el dicho capitán Orey escapo por una ventana")
m("M-UT01-217", "UT01", "P01", "persona", "su mujer", "su mujer resien parida le causo un horror")
m("M-UT01-218", "UT01", "P01", "grupo", "los indios", "A los indios perjudica quitando sus chacras")
m("M-UT01-219", "UT01", "P01", "cosa", "sus chacras o tierras", "perjudica quitando sus chacras o tierras")
m("M-UT01-220", "UT01", "P01", "grupo", "los tributarios", "les harrea con fainas a los tributarios")
m("M-UT01-221", "UT01", "P01", "grupo", "los señores jueces", "pongan remedio los señores jueces porque", rol="destinatario")
m("M-UT01-222", "UT01", "P01", "persona", "dicho alzado", "de sus traiciones, del dicho alzado")
m("M-UT01-223", "UT01", "P01", "persona", "señor gobernador, subdelegado", "ni hace aprecio al señor gobernador, subdelegado")

C1 = "M-UT01-001"
a("A-UT01-201", "UT01", "P01", C1, "certificante", {"mencion": C1},
  "ejerce-cargo", {"concepto": "sargento"}, "Yo el sargento Don Isidro Cano de esta compañía")
a("A-UT01-202", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-002"},
  "participa-en-hecho", {"hecho": "H-p01-maltrato"},
  "al denunciante mayor Guancachoque lo esta lo estropearon sus enemigos lo tendieron cuasi muerto", rol_en_hecho="victima")
a("A-UT01-203", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-204"},
  "participa-en-hecho", {"hecho": "H-p01-maltrato"},
  "lo esta lo estropearon sus enemigos lo tendieron cuasi muerto", rol_en_hecho="agresor")
a("A-UT01-204", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-002"},
  "participa-en-hecho", {"hecho": "H-p01-prision"},
  "al denunciante mayor Guancachoque lo esta lo estropearon sus enemigos lo tendieron cuasi muerto y lo pusieron a la carcel",
  rol_en_hecho="preso")
a("A-UT01-205", "UT01", "P01", C1, "certificante", {"hecho": "H-p01-prision"},
  "lugar-del-hecho", {"mencion": "M-UT01-205"}, "lo pusieron a la carcel a esa noche")
a("A-UT01-206", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-206"},
  "participa-en-hecho", {"hecho": "H-p01-alboroto"},
  "todos los indios se alzaron a media noche todos con garrotes a acabar al dicho denunciante", rol_en_hecho="agresor")
a("A-UT01-207", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-207"},
  "participa-en-hecho", {"hecho": "H-p01-alboroto"}, "todos con garrotes a acabar al dicho denunciante", rol_en_hecho="victima",
  nota="Víctima intentada: el alboroto buscaba «acabar» al denunciante.")
a("A-UT01-208", "UT01", "P01", C1, "certificante", {"hecho": "H-p01-alboroto"},
  "motivo", {"literal": "a acabar al dicho denunciante"}, "todos con garrotes a acabar al dicho denunciante")
a("A-UT01-209", "UT01", "P01", C1, "certificante", {"hecho": "H-p01-alboroto"},
  "motivo", {"literal": "hacen una matanza a los españoles"},
  "animados en animas conformes, hacen una matanza a los españoles")
a("A-UT01-210", "UT01", "P01", C1, "certificante", {"hecho": "H-p01-alboroto"},
  "lugar-del-hecho", {"mencion": "M-UT01-209"}, "porque estaba cubierto de indiada la plaza")
a("A-UT01-211", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-004"},
  "participa-en-hecho", {"hecho": "H-p01-alzamiento-orey"},
  "mando dicho Chuquitapa cargando. [....] y Chicha ay se alzaron contra el capitan don Miguel Orey", rol_en_hecho="instigador")
a("A-UT01-212", "UT01", "P01", C1, "certificante", {"hecho": "H-p01-alzamiento-orey"},
  "fecha-del-hecho", {"literal": "En tiempo del señor corregidor don Antonio Reparas"},
  "En tiempo del señor corregidor don Antonio Reparas, mando dicho Chuquitapa")
a("A-UT01-213", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-211"},
  "ejerce-cargo", {"concepto": "corregidor"}, "En tiempo del señor corregidor don Antonio Reparas")
a("A-UT01-214", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-213"},
  "ejerce-cargo", {"concepto": "capitan"}, "se alzaron contra el capitan don Miguel Orey")
a("A-UT01-215", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-213"},
  "participa-en-hecho", {"hecho": "H-p01-alzamiento-orey"}, "se alzaron contra el capitan don Miguel Orey", rol_en_hecho="victima")
a("A-UT01-216", "UT01", "P01", C1, "certificante", {"hecho": "H-p01-alzamiento-orey"},
  "fecha-del-hecho", {"literal": "a las ocho de la noche"}, "don Miguel Orey a las ocho de la noche con pedradas")
a("A-UT01-217", "UT01", "P01", C1, "certificante", {"hecho": "H-p01-alzamiento-orey"},
  "numero-de-participantes", {"literal": "cerca de sesenta indios"}, "con pedradas palos cerca de sesenta indios")
a("A-UT01-218", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-214"},
  "participa-en-hecho", {"hecho": "H-p01-alzamiento-orey"}, "con pedradas palos cerca de sesenta indios", rol_en_hecho="agresor")
a("A-UT01-219", "UT01", "P01", C1, "certificante", {"hecho": "H-p01-alzamiento-orey"},
  "fecha-del-hecho", {"literal": "otra vuelta de dos horas"}, "y otra vuelta de dos horas. Con mas aumento de indios",
  nota="Lectura dudosa: puede ser una segunda acometida a las dos horas o una duración de dos horas.")
a("A-UT01-220", "UT01", "P01", C1, "certificante", {"hecho": "H-p01-alzamiento-orey"},
  "lugar-del-hecho", {"mencion": "M-UT01-215"}, "pedrearon su tienda hasta quebrar la puerta")
a("A-UT01-221", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-217"},
  "participa-en-hecho", {"hecho": "H-p01-alzamiento-orey"}, "su mujer resien parida le causo un horror", rol_en_hecho="victima")
a("A-UT01-222", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-218"},
  "participa-en-hecho", {"hecho": "H-p01-despojo"}, "A los indios perjudica quitando sus chacras o tierras", rol_en_hecho="victima")
a("A-UT01-223", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-004", "eliptico": True},
  "participa-en-hecho", {"hecho": "H-p01-despojo"}, "A los indios perjudica quitando sus chacras o tierras", rol_en_hecho="agresor",
  nota="Sujeto elíptico de «perjudica»: el párrafo trata de las acciones de Chuquitapa; se remite a su mención anterior en P01.")
a("A-UT01-224", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-220"},
  "participa-en-hecho", {"hecho": "H-p01-faenas"}, "y les harrea con fainas a los tributarios", rol_en_hecho="victima")
a("A-UT01-225", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-004", "eliptico": True},
  "participa-en-hecho", {"hecho": "H-p01-faenas"}, "y les harrea con fainas a los tributarios", rol_en_hecho="agresor",
  nota="Mismo sujeto elíptico que A-UT01-223.")
a("A-UT01-226", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-222"},
  "calificacion-de-conducta", {"literal": "no estamos libres de sus traiciones"},
  "porque no estamos libres de sus traiciones, del dicho alzado", fundamento="vista",
  nota="El certificante declara «esto es lo que hey obserbado».")
a("A-UT01-227", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-222", "eliptico": True},
  "calificacion-de-conducta", {"literal": "Nada respeta ni hace aprecio al señor gobernador, subdelegado"},
  "Nada respeta ni hace aprecio al señor gobernador, subdelegado",
  nota="Sujeto elíptico de «Nada respeta»: el «dicho alzado» de la frase anterior.")
a("A-UT01-228", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-223"},
  "ejerce-cargo", {"concepto": "gobernador"}, "ni hace aprecio al señor gobernador, subdelegado")
a("A-UT01-229", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-223"},
  "ejerce-cargo", {"concepto": "subdelegado"}, "ni hace aprecio al señor gobernador, subdelegado",
  nota="Se lee «gobernador, subdelegado» como dos títulos de una misma persona; podrían ser dos personas.")
a("A-UT01-230", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-221"},
  "solicita", {"literal": "pongan remedio"}, "pongan remedio los señores jueces")
a("A-UT01-231", "UT01", "P01", C1, "certificante", {"mencion": C1},
  "presta-juramento", {"literal": "una señal de cruz como fiel christiano"}, "juro una señal de cruz como fiel christiano")
a("A-UT01-232", "UT01", "P01", C1, "certificante", {"mencion": "M-UT01-208"},
  "participa-en-hecho", {"hecho": "H-p01-alboroto"}, "hacen una matanza a los españoles", rol_en_hecho="victima",
  nota="Víctimas intentadas («hacen una matanza»).")

# ───────────── P02 · Certificación de Santiago Cazorla · UT02 ─────────────
m("M-UT02-201", "UT02", "P02", "grupo", "regimiento de Tinta", "sargento primero del regimiento de Tinta de la primera compañía")
m("M-UT02-202", "UT02", "P02", "grupo", "primera compañía", "del regimiento de Tinta de la primera compañía", tipo="compania-milicias")
m("M-UT02-203", "UT02", "P02", "grupo", "mi compañía", "ha estado soldado en mi compañía más de cinco años", tipo="compania-milicias")
m("M-UT02-204", "UT02", "P02", "lugar", "Tinta", "doy mi certificación en Tinta agosto", tipo="pueblo")
m("M-UT02-205", "UT02", "P02", "grupo", "sus enemigos", "quien padece de sus enemigos por ser leal")

C2 = "M-UT02-005"
a("A-UT02-201", "UT02", "P02", C2, "certificante", {"mencion": C2},
  "ejerce-cargo", {"concepto": "sargento-primero"}, "como yo sargento primero del regimiento de Tinta")
a("A-UT02-202", "UT02", "P02", C2, "certificante", {"mencion": "M-UT02-003"},
  "participa-en-hecho", {"hecho": "H-p02-servicio"}, "Manuel Guamanchoque ha estado soldado en mi compañía",
  rol_en_hecho="participante-en-hecho")
a("A-UT02-203", "UT02", "P02", C2, "certificante", {"hecho": "H-p02-servicio"},
  "duracion", {"literal": "más de cinco años poco más o menos"}, "en mi compañía más de cinco años poco más o menos")
a("A-UT02-204", "UT02", "P02", C2, "certificante", {"mencion": "M-UT02-003", "eliptico": True},
  "calificacion-de-conducta", {"literal": "leal"}, "quien padece de sus enemigos por ser leal",
  nota="El relativo «quien» se resuelve a Manuel Guamanchoque, único sujeto de la certificación.")

# ───────────── P03 · Certificación a nombre de Juan Quiñones · UT02 ─────────────
m("M-UT02-206", "UT02", "P03", "persona", "Manuel Huancachoque", "al denunciante Manuel Huancachoque, cuasi lo acaban")
m("M-UT02-207", "UT02", "P03", "lugar", "las calles públicas", "en las calles públicas y plaza los indios")
m("M-UT02-208", "UT02", "P03", "lugar", "plaza", "en las calles públicas y plaza los indios", tipo="plaza")
m("M-UT02-209", "UT02", "P03", "grupo", "los indios", "plaza los indios del cacique don Andrés")
m("M-UT02-210", "UT02", "P03", "persona", "don Andrés Chukitapa", "del cacique don Andrés Chukitapa a puñetes")
m("M-UT02-211", "UT02", "P03", "lugar", "la cárcel", "de los pelos nomás llevaron a la cárcel", tipo="carcel")
m("M-UT02-212", "UT02", "P03", "grupo", "los indios", "se alzaron los indios en la plaza")
m("M-UT02-213", "UT02", "P03", "lugar", "la plaza", "los indios en la plaza todos con garrotes", tipo="plaza")
m("M-UT02-214", "UT02", "P03", "lugar", "la cárcel", "allegaron a la puerta de la cárcel a dar muerte", tipo="carcel")
m("M-UT02-215", "UT02", "P03", "persona", "dicho Guancachoque", "a dar muerte a dicho Guancachoque")
m("M-UT02-216", "UT02", "P03", "grupo", "los españoles", "despues pasar a los españoles")
m("M-UT02-217", "UT02", "P03", "grupo", "todos los españoles", "porque todos los españoles tuvimos por bien hecho")
m("M-UT02-218", "UT02", "P03", "grupo", "Real Hacienda", "haver manifestado el robo a favor de la Real Hacienda")
m("M-UT02-219", "UT02", "P03", "lugar", "esta plaza", "en cada esquina de esta plaza hubo", tipo="plaza")
m("M-UT02-220", "UT02", "P03", "grupo", "un montón de indios", "hubo un montón de indios y pusieron de guardia")
m("M-UT02-221", "UT02", "P03", "persona", "don Santiago Cazorla", "en la puerta de don Santiago Cazorla")
m("M-UT02-222", "UT02", "P03", "persona", "Este mismo cacique", "Este mismo cacique invento el alzamiento")
m("M-UT02-223", "UT02", "P03", "persona", "don Miguel Orey", "el alzamiento contra don Miguel Orey")
m("M-UT02-224", "UT02", "P03", "grupo", "los indios", "hizo embriagar a los indios tan mansos")
m("M-UT02-225", "UT02", "P03", "lugar", "su casa", "a su casa hicieron pedazos la puerta", tipo="edificio")
m("M-UT02-226", "UT02", "P03", "grupo", "dos españoles", "lo vimos entre dos españoles")
m("M-UT02-227", "UT02", "P03", "persona", "don Javier Aparicio", "con don Javier Aparicio español soldado")
m("M-UT02-228", "UT02", "P03", "cosa", "la llave de la carcel", "si esa noche parece la llave de la carcel")
m("M-UT02-229", "UT02", "P03", "grupo", "los señores jueces", "para que es cierto los señores jueces pongan remedio",
  rol="destinatario")

m("M-UT02-230", "UT02", "P03", "persona", "cacique", "trabuco el robo. del cacique que le va")

C3 = "M-UT02-001"
a("A-UT02-301", "UT02", "P03", C3, "certificante", {"mencion": C3},
  "ejerce-cargo", {"concepto": "teniente-alguacil"}, "El teniente Alguacil, don Juan Quiñones")
a("A-UT02-302", "UT02", "P03", C3, "certificante", {"mencion": "M-UT02-206"},
  "participa-en-hecho", {"hecho": "H-p03-maltrato"},
  "al denunciante Manuel Huancachoque, cuasi lo acaban en las calles públicas y plaza", rol_en_hecho="victima")
a("A-UT02-303", "UT02", "P03", C3, "certificante", {"mencion": "M-UT02-209"},
  "participa-en-hecho", {"hecho": "H-p03-maltrato"},
  "los indios del cacique don Andrés Chukitapa a puñetes y puntapiés", rol_en_hecho="agresor")
a("A-UT02-304", "UT02", "P03", C3, "certificante", {"mencion": "M-UT02-210"},
  "ejerce-cargo", {"concepto": "cacique"}, "los indios del cacique don Andrés Chukitapa")
a("A-UT02-305", "UT02", "P03", C3, "certificante", {"hecho": "H-p03-maltrato"},
  "lugar-del-hecho", {"mencion": "M-UT02-207"}, "cuasi lo acaban en las calles públicas y plaza")
a("A-UT02-306", "UT02", "P03", C3, "certificante", {"hecho": "H-p03-maltrato"},
  "lugar-del-hecho", {"mencion": "M-UT02-208"}, "cuasi lo acaban en las calles públicas y plaza")
a("A-UT02-307", "UT02", "P03", C3, "certificante", {"hecho": "H-p03-maltrato"},
  "motivo", {"literal": "que por que trabuco el robo. del cacique"},
  "tratando mil insolencias que por que trabuco el robo. del cacique")
a("A-UT02-308", "UT02", "P03", C3, "certificante", {"mencion": "M-UT02-206", "eliptico": True},
  "participa-en-hecho", {"hecho": "H-p03-prision"}, "de los pelos nomás llevaron a la cárcel", rol_en_hecho="preso",
  nota="Objeto omitido de «llevaron»: el denunciante Manuel Huancachoque de la misma frase.")
a("A-UT02-309", "UT02", "P03", C3, "certificante", {"hecho": "H-p03-prision"},
  "lugar-del-hecho", {"mencion": "M-UT02-211"}, "de los pelos nomás llevaron a la cárcel")
a("A-UT02-310", "UT02", "P03", C3, "certificante", {"mencion": "M-UT02-212"},
  "participa-en-hecho", {"hecho": "H-p03-alboroto"}, "se alzaron los indios en la plaza todos con garrotes",
  rol_en_hecho="agresor", fundamento="vista")
a("A-UT02-311", "UT02", "P03", C3, "certificante", {"hecho": "H-p03-alboroto"},
  "lugar-del-hecho", {"mencion": "M-UT02-213"}, "se alzaron los indios en la plaza todos con garrotes")
a("A-UT02-312", "UT02", "P03", C3, "certificante", {"hecho": "H-p03-alboroto"},
  "lugar-del-hecho", {"mencion": "M-UT02-214"}, "allegaron a la puerta de la cárcel a dar muerte")
a("A-UT02-313", "UT02", "P03", C3, "certificante", {"mencion": "M-UT02-215"},
  "participa-en-hecho", {"hecho": "H-p03-alboroto"}, "a dar muerte a dicho Guancachoque", rol_en_hecho="victima",
  nota="Víctima intentada.")
a("A-UT02-314", "UT02", "P03", C3, "certificante", {"hecho": "H-p03-alboroto"},
  "motivo", {"literal": "a dar muerte a dicho Guancachoque y despues pasar a los españoles"},
  "a dar muerte a dicho Guancachoque y despues pasar a los españoles")
a("A-UT02-315", "UT02", "P03", C3, "certificante", {"mencion": "M-UT02-212", "eliptico": True},
  "calificacion-de-conducta", {"literal": "estaban hebreos"}, "y como estaban hebreos, a todos los hubieran acabado",
  nota="Sujeto elíptico: los indios alzados. «hebreos» se transcribe tal cual (probablemente «ebrios»; no se normaliza).")
a("A-UT02-316", "UT02", "P03", C3, "certificante", {"hecho": "H-p03-alboroto"},
  "numero-de-participantes", {"literal": "en cada esquina de esta plaza hubo un montón de indios"},
  "en cada esquina de esta plaza hubo un montón de indios")
a("A-UT02-317", "UT02", "P03", C3, "certificante", {"mencion": "M-UT02-220"},
  "participa-en-hecho", {"hecho": "H-p03-guardias"}, "hubo un montón de indios y pusieron de guardia en nuestras puertas",
  rol_en_hecho="agresor")
a("A-UT02-318", "UT02", "P03", C3, "certificante", {"hecho": "H-p03-guardias"},
  "lugar-del-hecho", {"literal": "lo primero en mi puerta hasta harta gente, lo segundo en la puerta de don Santiago Cazorla"},
  "lo primero en mi puerta hasta harta gente, lo segundo en la puerta de don Santiago Cazorla")
a("A-UT02-319", "UT02", "P03", C3, "certificante", {"hecho": "H-p03-alboroto"},
  "motivo", {"literal": "haver manifestado el robo a favor de la Real Hacienda"},
  "porque todos los españoles tuvimos por bien hecho haver manifestado el robo a favor de la Real Hacienda",
  nota="Motivo que el certificante atribuye a la hostilidad contra los españoles.")
a("A-UT02-320", "UT02", "P03", C3, "certificante", {"mencion": "M-UT02-222"},
  "participa-en-hecho", {"hecho": "H-p03-alzamiento-orey"}, "Este mismo cacique invento el alzamiento contra don Miguel Orey",
  rol_en_hecho="instigador")
a("A-UT02-321", "UT02", "P03", C3, "certificante", {"mencion": "M-UT02-223"},
  "participa-en-hecho", {"hecho": "H-p03-alzamiento-orey"}, "Este mismo cacique invento el alzamiento contra don Miguel Orey",
  rol_en_hecho="victima")
a("A-UT02-322", "UT02", "P03", C3, "certificante", {"hecho": "H-p03-alzamiento-orey"},
  "fecha-del-hecho", {"literal": "muy antes de la rebelion"}, "no es la primera vez sino muy antes de la rebelion")
a("A-UT02-323", "UT02", "P03", C3, "certificante", {"mencion": "M-UT02-224"},
  "participa-en-hecho", {"hecho": "H-p03-alzamiento-orey"}, "hizo embriagar a los indios tan mansos", rol_en_hecho="agresor")
a("A-UT02-324", "UT02", "P03", C3, "certificante", {"hecho": "H-p03-alzamiento-orey"},
  "lugar-del-hecho", {"mencion": "M-UT02-225"}, "a su casa hicieron pedazos la puerta hecho una astilla", fundamento="vista",
  nota="El certificante añade «Esto es lo que vi de con mis ojos».")
a("A-UT02-325", "UT02", "P03", C3, "certificante", {"mencion": "M-UT02-227"},
  "tiene-condicion", {"concepto": "espanol"}, "con don Javier Aparicio español soldado")
a("A-UT02-326", "UT02", "P03", C3, "certificante", {"mencion": "M-UT02-227"},
  "ejerce-cargo", {"concepto": "soldado"}, "con don Javier Aparicio español soldado")
a("A-UT02-327", "UT02", "P03", C3, "certificante", {"mencion": "M-UT02-229"},
  "solicita", {"literal": "pongan remedio"}, "los señores jueces pongan remedio")
a("A-UT02-328", "UT02", "P03", C3, "certificante", {"mencion": C3},
  "presta-juramento", {"literal": "una señal de cruz"}, "prometo declarar y ratificar en que quien tiempo jurando una señal de cruz")
a("A-UT02-329", "UT02", "P03", C3, "certificante", {"mencion": "M-UT02-216"},
  "participa-en-hecho", {"hecho": "H-p03-alboroto"}, "despues pasar a los españoles", rol_en_hecho="victima",
  nota="Víctimas intentadas.")

# ───────────── P04 · Certificación a nombre de Fernando Orue · UT03 ─────────────
m("M-UT03-201", "UT03", "P04", "grupo", "compañía de Tinta", "Yo el cabo primero en esta compañía de Tinta", tipo="compania-milicias")
m("M-UT03-202", "UT03", "P04", "lugar", "Tinta", "de este mismo cuerpo del puesto de Tinta", tipo="pueblo")
m("M-UT03-203", "UT03", "P04", "grupo", "los Indios del Ayllu de tinta", "que hicieron los Indios del Ayllu de tinta contra")
m("M-UT03-204", "UT03", "P04", "grupo", "Ayllu de tinta", "los Indios del Ayllu de tinta contra Manuel", tipo="ayllu")
m("M-UT03-205", "UT03", "P04", "persona", "Manuel Huancachoque", "de tinta contra Manuel Huancachoque. Que declaro")
m("M-UT03-206", "UT03", "P04", "grupo", "los Indios ocultados", "Que declaro por los Indios ocultados")
m("M-UT03-207", "UT03", "P04", "persona", "nuestro soberano", "ocultados a favor de nuestro soberano")
m("M-UT03-208", "UT03", "P04", "cosa", "reales arcas", "y aumento a las reales arcas a dicho")
m("M-UT03-209", "UT03", "P04", "persona", "dicho denunciante", "a dicho denunciante los indios llevaron preso")
m("M-UT03-210", "UT03", "P04", "grupo", "los indios", "dicho denunciante los indios llevaron preso")
m("M-UT03-211", "UT03", "P04", "lugar", "la cárcel", "llevaron preso a la cárcel maltratando", tipo="carcel")
m("M-UT03-212", "UT03", "P04", "lugar", "la cárcel", "cruelmente pusieron a la cárcel y a las diez", tipo="carcel")
m("M-UT03-213", "UT03", "P04", "lugar", "la plaza", "todos ebrios al redor de la plaza", tipo="plaza")
m("M-UT03-214", "UT03", "P04", "grupo", "un montón de indios", "un montón de indios asumaron a la puerta")
m("M-UT03-215", "UT03", "P04", "lugar", "la cárcel", "asumaron a la puerta de la cárcel todos armados", tipo="carcel")
m("M-UT03-216", "UT03", "P04", "persona", "el alcalde", "los primeros ay el alcalde y segunda")
m("M-UT03-217", "UT03", "P04", "persona", "segunda", "los primeros ay el alcalde y segunda")
m("M-UT03-218", "UT03", "P04", "persona", "Tupaamaro", "a favor del insurgente, Tupaamaro")
m("M-UT03-219", "UT03", "P04", "persona", "Don Juan Antonio Reparas", "en tiempo del señor corregidor Don Juan Antonio Reparas")
m("M-UT03-220", "UT03", "P04", "grupo", "los españoles", "ninguno estamos libres de su traición los españoles")

C4 = "M-UT03-001"
a("A-UT03-201", "UT03", "P04", C4, "certificante", {"mencion": C4},
  "ejerce-cargo", {"concepto": "cabo-primero"},
  "Yo el cabo primero en esta compañía de Tinta de este mismo cuerpo del puesto de Tinta Fernando Orue")
a("A-UT03-202", "UT03", "P04", C4, "certificante", {"mencion": C4},
  "tiene-condicion", {"concepto": "vecino"}, "Fernando Orue, vecino de esta misma comprehencion")
a("A-UT03-203", "UT03", "P04", C4, "certificante", {"mencion": "M-UT03-203"},
  "participa-en-hecho", {"hecho": "H-p04-maltrato"},
  "he visto con mis ojos, mortales el alboroto que hicieron los Indios del Ayllu de tinta contra Manuel Huancachoque",
  rol_en_hecho="agresor", fundamento="vista")
a("A-UT03-204", "UT03", "P04", C4, "certificante", {"mencion": "M-UT03-205"},
  "participa-en-hecho", {"hecho": "H-p04-maltrato"},
  "el alboroto que hicieron los Indios del Ayllu de tinta contra Manuel Huancachoque", rol_en_hecho="victima", fundamento="vista")
a("A-UT03-205", "UT03", "P04", C4, "certificante", {"hecho": "H-p04-maltrato"},
  "motivo", {"literal": "por los Indios ocultados a favor de nuestro soberano y aumento a las reales arcas"},
  "Que declaro por los Indios ocultados a favor de nuestro soberano y aumento a las reales arcas")
a("A-UT03-206", "UT03", "P04", C4, "certificante", {"mencion": "M-UT03-209"},
  "participa-en-hecho", {"hecho": "H-p04-prision"}, "a dicho denunciante los indios llevaron preso a la cárcel",
  rol_en_hecho="preso")
a("A-UT03-207", "UT03", "P04", C4, "certificante", {"mencion": "M-UT03-210"},
  "participa-en-hecho", {"hecho": "H-p04-maltrato"},
  "a dicho denunciante los indios llevaron preso a la cárcel maltratando cruelmente", rol_en_hecho="agresor")
a("A-UT03-208", "UT03", "P04", C4, "certificante", {"hecho": "H-p04-prision"},
  "lugar-del-hecho", {"mencion": "M-UT03-211"}, "llevaron preso a la cárcel maltratando")
a("A-UT03-209", "UT03", "P04", C4, "certificante", {"hecho": "H-p04-alboroto"},
  "lugar-del-hecho", {"mencion": "M-UT03-213"}, "peor alboroto todos ebrios al redor de la plaza")
a("A-UT03-210", "UT03", "P04", C4, "certificante", {"hecho": "H-p04-alboroto"},
  "numero-de-participantes", {"literal": "un montón de indios"}, "un montón de indios asumaron a la puerta de la cárcel")
a("A-UT03-211", "UT03", "P04", C4, "certificante", {"mencion": "M-UT03-214"},
  "participa-en-hecho", {"hecho": "H-p04-alboroto"}, "un montón de indios asumaron a la puerta de la cárcel todos armados",
  rol_en_hecho="agresor")
a("A-UT03-212", "UT03", "P04", C4, "certificante", {"hecho": "H-p04-alboroto"},
  "lugar-del-hecho", {"mencion": "M-UT03-215"}, "asumaron a la puerta de la cárcel todos armados")
a("A-UT03-213", "UT03", "P04", C4, "certificante", {"hecho": "H-p04-alboroto"},
  "motivo", {"literal": "con ánimo de dar muerte"}, "todos armados con ánimo de dar muerte")
a("A-UT03-214", "UT03", "P04", C4, "certificante", {"mencion": "M-UT03-216"},
  "participa-en-hecho", {"hecho": "H-p04-alboroto"}, "con ánimo de dar muerte, los primeros ay el alcalde y segunda",
  rol_en_hecho="agresor")
a("A-UT03-215", "UT03", "P04", C4, "certificante", {"mencion": "M-UT03-217"},
  "participa-en-hecho", {"hecho": "H-p04-alboroto"}, "con ánimo de dar muerte, los primeros ay el alcalde y segunda",
  rol_en_hecho="agresor")
a("A-UT03-216", "UT03", "P04", C4, "certificante", {"mencion": "M-UT03-216"},
  "ejerce-cargo", {"concepto": "alcalde"}, "los primeros ay el alcalde y segunda")
a("A-UT03-217", "UT03", "P04", C4, "certificante", {"mencion": "M-UT03-217"},
  "ejerce-cargo", {"concepto": "segunda"}, "los primeros ay el alcalde y segunda")
a("A-UT03-218", "UT03", "P04", C4, "certificante", {"mencion": "M-UT03-216"},
  "calificacion-de-conducta", {"literal": "a favor del insurgente, Tupaamaro"},
  "el alcalde y segunda; a favor del insurgente, Tupaamaro",
  nota="Puntuación ambigua: «a favor del insurgente» puede calificar al alcalde y la segunda o abrir la frase siguiente sobre Chuquitapa.")
a("A-UT03-219", "UT03", "P04", C4, "certificante", {"mencion": "M-UT03-218"},
  "calificacion-de-conducta", {"literal": "insurgente"}, "a favor del insurgente, Tupaamaro")
a("A-UT03-220", "UT03", "P04", C4, "certificante", {"mencion": "M-UT03-002"},
  "participa-en-hecho", {"hecho": "H-p04-alzamiento-reparas"},
  "a dicho Chuquitapa, primero hizo en tiempo del señor corregidor Don Juan Antonio Reparas", rol_en_hecho="instigador")
a("A-UT03-221", "UT03", "P04", C4, "certificante", {"hecho": "H-p04-alzamiento-reparas"},
  "fecha-del-hecho", {"literal": "en tiempo del señor corregidor Don Juan Antonio Reparas"},
  "primero hizo en tiempo del señor corregidor Don Juan Antonio Reparas")
a("A-UT03-222", "UT03", "P04", C4, "certificante", {"mencion": "M-UT03-219"},
  "ejerce-cargo", {"concepto": "corregidor"}, "en tiempo del señor corregidor Don Juan Antonio Reparas")
a("A-UT03-223", "UT03", "P04", C4, "certificante", {"mencion": "M-UT03-002"},
  "participa-en-hecho", {"hecho": "H-p04-alzamiento-1780"},
  "a dicho Chuquitapa, primero hizo en tiempo del señor corregidor Don Juan Antonio Reparas y el otro alzamiento que hizo, en tiempo de su pariente Tupaamaro",
  rol_en_hecho="instigador")
a("A-UT03-224", "UT03", "P04", C4, "certificante", {"hecho": "H-p04-alzamiento-1780"},
  "fecha-del-hecho", {"literal": "en tiempo de su pariente Tupaamaro"}, "el otro alzamiento que hizo, en tiempo de su pariente Tupaamaro")
a("A-UT03-225", "UT03", "P04", C4, "certificante", {"mencion": "M-UT03-002", "eliptico": True},
  "calificacion-de-conducta", {"literal": "ninguno estamos libres de su traición"},
  "ninguno estamos libres de su traición los españoles",
  nota="Posesivo «su» resuelto a Chuquitapa, de quien trata la frase anterior.")

# ───────────── P05 · Certificación a nombre de Martín Cazorla · UT04 ─────────────
m("M-UT04-201", "UT04", "P05", "persona", "Manuel Huancachoque", "Tuve grande sentimiento por Manuel Huancachoque")
m("M-UT04-202", "UT04", "P05", "grupo", "Real Hacienda", "denunciante a favor de la Real Hacienda que defendió")
m("M-UT04-203", "UT04", "P05", "cosa", "las reales arcas", "que defendió a las reales arcas")
m("M-UT04-204", "UT04", "P05", "persona", "cacique", "el total robo del cacique que dice en usurpación")
m("M-UT04-205", "UT04", "P05", "grupo", "los indios", "los indios estiraron a golpes de los pelos")
m("M-UT04-206", "UT04", "P05", "lugar", "la cárcel", "de los pelos pusieron a la cárcel", tipo="carcel")
m("M-UT04-207", "UT04", "P05", "persona", "mi cacique", "declararon el robo de mi cacique")
m("M-UT04-208", "UT04", "P05", "lugar", "la cárcel", "pidieron a la cárcel al denunciante", tipo="carcel")
m("M-UT04-209", "UT04", "P05", "persona", "denunciante", "a la cárcel al denunciante, maltratando")
m("M-UT04-210", "UT04", "P05", "grupo", "los Indios", "se alzaron los Indios todos con garrotes")
m("M-UT04-211", "UT04", "P05", "grupo", "Real Hacienda", "condolían por a favor de la Real Hacienda que hablamos")
m("M-UT04-212", "UT04", "P05", "grupo", "Real Hacienda", "Sintiéndonos a favor de la Real Hacienda")
m("M-UT04-213", "UT04", "P05", "grupo", "los señores jueces", "romediando aora los señores jueces abra", rol="destinatario")

m("M-UT04-214", "UT04", "P05", "persona", "desvalido", "en usurpación al desvalido lo castigaron")

C5 = "M-UT04-001"
a("A-UT04-201", "UT04", "P05", C5, "certificante", {"mencion": C5},
  "ejerce-cargo", {"concepto": "soldado"}, "Yo el soldado granadero Martin Cazorla",
  nota="«granadero» no tiene concepto propio en tes:cargos; se registra el cargo genérico soldado.")
a("A-UT04-202", "UT04", "P05", C5, "certificante", {"mencion": C5},
  "calificacion-de-conducta", {"literal": "soldado fiel hijo de la causa real"}, "como soldado fiel hijo de la causa real")
a("A-UT04-203", "UT04", "P05", C5, "certificante", {"mencion": "M-UT04-201", "eliptico": True},
  "participa-en-hecho", {"hecho": "H-p05-maltrato"},
  "por haber sacado a la luz el total robo del cacique que dice en usurpación al desvalido lo castigaron cruelmente",
  rol_en_hecho="victima", nota="«al desvalido … lo castigaron» se resuelve a Manuel Huancachoque, nombrado en la frase anterior.")
a("A-UT04-217", "UT04", "P05", C5, "certificante", {"mencion": "M-UT04-214"},
  "participa-en-hecho", {"hecho": "H-p05-maltrato"}, "en usurpación al desvalido lo castigaron cruelmente",
  rol_en_hecho="victima")
a("A-UT04-204", "UT04", "P05", C5, "certificante", {"mencion": "M-UT04-205"},
  "participa-en-hecho", {"hecho": "H-p05-maltrato"}, "los indios estiraron a golpes de los pelos pusieron a la cárcel",
  rol_en_hecho="agresor")
a("A-UT04-205", "UT04", "P05", C5, "certificante", {"hecho": "H-p05-maltrato"},
  "motivo", {"literal": "por haber sacado a la luz el total robo del cacique"},
  "por haber sacado a la luz el total robo del cacique")
a("A-UT04-206", "UT04", "P05", C5, "certificante", {"mencion": "M-UT04-204"},
  "calificacion-de-conducta", {"literal": "el total robo del cacique que dice en usurpación"},
  "el total robo del cacique que dice en usurpación")
a("A-UT04-207", "UT04", "P05", C5, "certificante", {"hecho": "H-p05-maltrato"},
  "motivo", {"literal": "porque declararon el robo de mi cacique"},
  "todos con groserías que porque declararon el robo de mi cacique",
  nota="Motivo puesto en boca de los agresores («mi cacique»).")
a("A-UT04-208", "UT04", "P05", C5, "certificante", {"hecho": "H-p05-prision"},
  "lugar-del-hecho", {"mencion": "M-UT04-208"}, "pidieron a la cárcel al denunciante")
a("A-UT04-209", "UT04", "P05", C5, "certificante", {"mencion": "M-UT04-209"},
  "participa-en-hecho", {"hecho": "H-p05-prision"}, "pidieron a la cárcel al denunciante, maltratando cruelmente",
  rol_en_hecho="preso")
a("A-UT04-210", "UT04", "P05", C5, "certificante", {"hecho": "H-p05-prision"},
  "fecha-del-hecho", {"literal": "El siguiente día de la revisita"}, "El siguiente día de la revisita pidieron a la cárcel")
a("A-UT04-211", "UT04", "P05", C5, "certificante", {"mencion": "M-UT04-210"},
  "participa-en-hecho", {"hecho": "H-p05-alboroto"}, "se alzaron los Indios todos con garrotes, armados a dar muerte",
  rol_en_hecho="agresor")
a("A-UT04-212", "UT04", "P05", C5, "certificante", {"hecho": "H-p05-alboroto"},
  "fecha-del-hecho", {"literal": "Esa misma noche"}, "Esa misma noche se alzaron los Indios")
a("A-UT04-213", "UT04", "P05", C5, "certificante", {"hecho": "H-p05-alboroto"},
  "motivo", {"literal": "a dar muerte a los que condolían por a favor de la Real Hacienda"},
  "armados a dar muerte a los que condolían por a favor de la Real Hacienda")
a("A-UT04-214", "UT04", "P05", C5, "certificante", {"mencion": "M-UT04-213"},
  "solicita", {"literal": "romediando aora los señores jueces"}, "romediando aora los señores jueces")
a("A-UT04-215", "UT04", "P05", C5, "certificante", {"mencion": C5},
  "presta-juramento", {"literal": "a Dios una señal de fe"}, "Juro a Dios una señal de fe ser mi verdad")
a("A-UT04-216", "UT04", "P05", C5, "certificante", {"mencion": "M-UT04-201"},
  "calificacion-de-conducta", {"literal": "denunciante a favor de la Real Hacienda que defendió a las reales arcas"},
  "Manuel Huancachoque, denunciante a favor de la Real Hacienda que defendió a las reales arcas")

# ───────────── P06 · Escrito de Huancachoque · UT05 ─────────────
m("M-UT05-201", "UT05", "P06", "cosa", "SELLO CUARTO", "SELLO CUARTO, UN CUARTILLO")
m("M-UT05-202", "UT05", "P06", "persona", "SEÑOR FISCAL PROTECTOR GENERAL DE NATURALES",
  "SEÑOR FISCAL PROTECTOR GENERAL DE NATURALES", rol="destinatario")
m("M-UT05-203", "UT05", "P06", "lugar", "pueblo de Tinta", "vecino del pueblo de Tinta, partido", tipo="pueblo")
m("M-UT05-204", "UT05", "P06", "lugar", "partido de este nombre", "Tinta, partido de este nombre ante", tipo="partido")
m("M-UT05-205", "UT05", "P06", "persona", "mi soberano y señor natural", "fidelidad a mi soberano y señor natural")
m("M-UT05-206", "UT05", "P06", "grupo", "Indios tributarios", "considerable número de Indios tributarios que")
m("M-UT05-207", "UT05", "P06", "persona", "muy ilustre señor presidente", "de orden del muy ilustre señor presidente que")
m("M-UT05-208", "UT05", "P06", "grupo", "Real Audiencia", "presidente que esta Real Audiencia se procedio")
m("M-UT05-209", "UT05", "P06", "persona", "actual apoderado del fiscal", "por el actual apoderado del fiscal que ha sido")
m("M-UT05-210", "UT05", "P06", "persona", "recaudador", "a presencia del recaudador y juez subdelegado")
m("M-UT05-211", "UT05", "P06", "persona", "juez subdelegado", "a presencia del recaudador y juez subdelegado")
m("M-UT05-212", "UT05", "P06", "persona", "el denominado", "revertido de encomo el denominado, ansioso")
m("M-UT05-213", "UT05", "P06", "persona", "subdelegado", "dio queja al subdelegado, protestando")
m("M-UT05-214", "UT05", "P06", "lugar", "la cárcel", "ordeno se me llevase a la cárcel", tipo="carcel")
m("M-UT05-215", "UT05", "P06", "grupo", "los segundas", "fue cuando los segundas, los alcaldes")
m("M-UT05-216", "UT05", "P06", "grupo", "los alcaldes", "los segundas, los alcaldes, sus parientes")
m("M-UT05-217", "UT05", "P06", "grupo", "sus parientes", "los alcaldes, sus parientes y demás")
m("M-UT05-218", "UT05", "P06", "grupo", "demás dependientes suyos", "y demás dependientes suyos embriagados")
m("M-UT05-219", "UT05", "P06", "lugar", "la cárcel", "me hicieron llegar al lugar de la cárcel", tipo="carcel")
m("M-UT05-220", "UT05", "P06", "grupo", "cuarenta y cuatro tributarios", "el descubrimiento de cuarenta y cuatro tributarios")

m("M-UT05-221", "UT05", "P06", "grupo", "los que quedan ya matriculados", "y los que quedan ya matriculados")

D = "M-UT05-001"
a("A-UT05-201", "UT05", "P06", D, "denunciante", {"mencion": D},
  "tiene-condicion", {"concepto": "indio"}, "Manuel Huancachoque Indio originario y vecino del pueblo de Tinta")
a("A-UT05-202", "UT05", "P06", D, "denunciante", {"mencion": D},
  "tiene-condicion", {"concepto": "vecino"}, "Manuel Huancachoque Indio originario y vecino del pueblo de Tinta")
a("A-UT05-203", "UT05", "P06", D, "denunciante", {"mencion": D},
  "participa-en-hecho", {"hecho": "H-p06-denuncia"}, "parezco y digo: Que conducido del amor y fidelidad a mi soberano y señor natural denuncie",
  rol_en_hecho="participante-en-hecho", fundamento="experiencia-propia",
  nota="Papel de denunciante en el hecho; tes:roles no tiene un hijo de participante-en-hecho para «denunciante».")
a("A-UT05-204", "UT05", "P06", D, "denunciante", {"hecho": "H-p06-denuncia"},
  "motivo", {"literal": "conducido del amor y fidelidad a mi soberano y señor natural"},
  "conducido del amor y fidelidad a mi soberano y señor natural")
a("A-UT05-205", "UT05", "P06", D, "denunciante", {"mencion": "M-UT05-002"},
  "participa-en-hecho", {"hecho": "H-p06-ocultacion"},
  "Indios tributarios que de muchos años atrás tenia ocultos el recaudaderor Don Andres Choquitapa",
  rol_en_hecho="participante-en-hecho")
a("A-UT05-206", "UT05", "P06", D, "denunciante", {"hecho": "H-p06-ocultacion"},
  "duracion", {"literal": "de muchos años atrás"}, "que de muchos años atrás tenia ocultos")
a("A-UT05-207", "UT05", "P06", D, "denunciante", {"mencion": "M-UT05-002"},
  "cantidad-denunciada", {"literal": "considerable número de Indios tributarios"},
  "denuncie considerable número de Indios tributarios")
a("A-UT05-208", "UT05", "P06", D, "denunciante", {"mencion": "M-UT05-207"},
  "participa-en-hecho", {"hecho": "H-p06-averiguacion"},
  "de orden del muy ilustre señor presidente que esta Real Audiencia se procedio a la averiguacion",
  rol_en_hecho="ordenante")
a("A-UT05-209", "UT05", "P06", D, "denunciante", {"mencion": "M-UT05-207"},
  "ejerce-cargo", {"concepto": "presidente-audiencia"}, "del muy ilustre señor presidente que esta Real Audiencia")
a("A-UT05-210", "UT05", "P06", D, "denunciante", {"mencion": "M-UT05-209"},
  "participa-en-hecho", {"hecho": "H-p06-averiguacion"}, "se procedio a la averiguacion, por el actual apoderado del fiscal",
  rol_en_hecho="participante-en-hecho")
a("A-UT05-211", "UT05", "P06", D, "denunciante", {"mencion": "M-UT05-209"},
  "ejerce-cargo", {"concepto": "apoderado-fiscal-revisita"}, "por el actual apoderado del fiscal que ha sido")
a("A-UT05-212", "UT05", "P06", D, "denunciante", {"mencion": "M-UT05-210"},
  "ejerce-cargo", {"concepto": "recaudador-de-tributos"}, "a presencia del recaudador y juez subdelegado")
a("A-UT05-213", "UT05", "P06", D, "denunciante", {"mencion": "M-UT05-211"},
  "ejerce-cargo", {"concepto": "subdelegado"}, "a presencia del recaudador y juez subdelegado")
a("A-UT05-214", "UT05", "P06", D, "denunciante", {"mencion": D},
  "participa-en-hecho", {"hecho": "H-p06-maltrato"}, "a más de ser gravemente maltratado", rol_en_hecho="victima",
  fundamento="experiencia-propia")
a("A-UT05-215", "UT05", "P06", D, "denunciante", {"mencion": "M-UT05-212"},
  "participa-en-hecho", {"hecho": "H-p06-queja"},
  "el denominado, ansioso de tomar de mi venganza, al siguiente día que prove la ocultación de Indios, dio queja al subdelegado",
  rol_en_hecho="participante-en-hecho")
a("A-UT05-216", "UT05", "P06", D, "denunciante", {"hecho": "H-p06-queja"},
  "motivo", {"literal": "ansioso de tomar de mi venganza"}, "el denominado, ansioso de tomar de mi venganza")
a("A-UT05-217", "UT05", "P06", D, "denunciante", {"hecho": "H-p06-queja"},
  "fecha-del-hecho", {"literal": "al siguiente día que prove la ocultación de Indios"},
  "al siguiente día que prove la ocultación de Indios, dio queja")
a("A-UT05-218", "UT05", "P06", D, "denunciante", {"mencion": "M-UT05-212"},
  "dijo", {"literal": "le había yo perdido el respeto"}, "protestando le había yo perdido el respeto")
a("A-UT05-219", "UT05", "P06", D, "denunciante", {"mencion": "M-UT05-213", "eliptico": True},
  "participa-en-hecho", {"hecho": "H-p06-prision"}, "ordeno se me llevase a la cárcel", rol_en_hecho="ordenante",
  nota="Sujeto elíptico de «ordeno»: el subdelegado ante quien se dio la queja (misma frase).")
a("A-UT05-220", "UT05", "P06", D, "denunciante", {"hecho": "H-p06-prision"},
  "lugar-del-hecho", {"mencion": "M-UT05-214"}, "ordeno se me llevase a la cárcel")
NOTA_AGR = ("«los segundas, los alcaldes, sus parientes y demás dependientes suyos … me envistieron» se reparte en un "
            "registro por grupo (A-UT05-221 a A-UT05-224).")
for i, mm in enumerate(["M-UT05-215", "M-UT05-216", "M-UT05-217", "M-UT05-218"], 221):
    a(f"A-UT05-{i}", "UT05", "P06", D, "denunciante", {"mencion": mm},
      "participa-en-hecho", {"hecho": "H-p06-maltrato"},
      "los segundas, los alcaldes, sus parientes y demás dependientes suyos embriagados al propósito, me envistieron como fieras",
      rol_en_hecho="agresor", fundamento="experiencia-propia", distribuida=True, nota=NOTA_AGR)
a("A-UT05-225", "UT05", "P06", D, "denunciante", {"hecho": "H-p06-maltrato"},
  "lugar-del-hecho", {"mencion": "M-UT05-219"}, "me hicieron llegar al lugar de la cárcel")
a("A-UT05-226", "UT05", "P06", D, "denunciante", {"mencion": "M-UT05-218"},
  "calificacion-de-conducta", {"literal": "embriagados al propósito"}, "demás dependientes suyos embriagados al propósito")

# ───────────── P06 · Escrito de Huancachoque · UT06 ─────────────
m("M-UT06-201", "UT06", "P06", "lugar", "pueblo", "a ser expelido del pueblo, y otros", tipo="pueblo")
m("M-UT06-202", "UT06", "P06", "grupo", "una caterva de indios", "se apareció una caterva de indios")
m("M-UT06-203", "UT06", "P06", "lugar", "el pueblo", "los alaridos aterrorizaron el pueblo", tipo="pueblo")
m("M-UT06-204", "UT06", "P06", "persona", "el subdelegado", "sin que el subdelegado se moviese")
m("M-UT06-205", "UT06", "P06", "persona", "Chuquitapa", "ha hecho de mi Chuquitapa lo que ha querido")
m("M-UT06-206", "UT06", "P06", "grupo", "las milicias de aquella provincia", "empleado en las milicias de aquella provincia")
m("M-UT06-207", "UT06", "P06", "lugar", "aquella provincia", "las milicias de aquella provincia, hasta")
m("M-UT06-208", "UT06", "P06", "grupo", "vecindario", "el objeto de la ogerisa del vecindario")
m("M-UT06-209", "UT06", "P06", "persona", "Chuquitapa", "por parte de Chuquitapa se me amenaza")
m("M-UT06-210", "UT06", "P06", "persona", "Monarca", "mi fidelidad al Monarca padezca")
m("M-UT06-211", "UT06", "P06", "persona", "vuestro señor", "a la celosa protección de vuestro señor")
m("M-UT06-212", "UT06", "P06", "cosa", "documentos calificativos del hecho", "tener yo documentos calificativos del hecho que refiero")
m("M-UT06-213", "UT06", "P06", "persona", "muy ilustre señor presidente", "esta mi representación al muy ilustre señor presidente")
m("M-UT06-214", "UT06", "P06", "cosa", "matricula", "se me saque de la matricula relevándoseme", tipo="matricula")
m("M-UT06-215", "UT06", "P06", "persona", "Chuquitapa", "que mi por Chuquitapa ni por otros")
m("M-UT06-216", "UT06", "P06", "grupo", "otros de su compañía", "ni por otros de su compañía se me infiera")
m("M-UT06-217", "UT06", "P06", "cosa", "ingente cantidad de dinero", "la ingente cantidad de dinero que ha usurpado aquel")
m("M-UT06-218", "UT06", "P06", "grupo", "Juzgado", "elevar mi queja al Juzgado que expreso")
m("M-UT06-219", "UT06", "P06", "persona", "vuestro señor", "A vuestro señor pido y suplico")
m("M-UT06-220", "UT06", "P06", "persona", "aquel", "dinero que ha usurpado aquel al Real grasia")

a("A-UT06-201", "UT06", "P06", D, "denunciante", {"mencion": D},
  "participa-en-hecho", {"hecho": "H-p06-prision"}, "al fin me encerraron allí", rol_en_hecho="preso",
  fundamento="experiencia-propia", nota="El afirmante es la mención inicial del escrito (UT05), misma pieza.")
a("A-UT06-202", "UT06", "P06", D, "denunciante", {"hecho": "H-p06-maltrato"},
  "dijo", {"literal": "decían que lo harian con hondas y piedras"},
  "y otros, decían que lo harian con hondas y piedras",
  nota="Amenaza referida de los agresores (sujeto plural sin mención); se ancla al hecho del maltrato.")
a("A-UT06-203", "UT06", "P06", D, "denunciante", {"mencion": "M-UT06-202"},
  "participa-en-hecho", {"hecho": "H-p06-alboroto"}, "se apareció una caterva de indios, a quienes había entregado",
  rol_en_hecho="agresor", fundamento="experiencia-propia")
a("A-UT06-204", "UT06", "P06", D, "denunciante", {"mencion": D},
  "participa-en-hecho", {"hecho": "H-p06-alboroto"}, "manifestándome los palos que traían, me anunciaban la muerte",
  rol_en_hecho="victima", fundamento="experiencia-propia")
a("A-UT06-205", "UT06", "P06", D, "denunciante", {"hecho": "H-p06-alboroto"},
  "motivo", {"literal": "me anunciaban la muerte"}, "manifestándome los palos que traían, me anunciaban la muerte")
a("A-UT06-206", "UT06", "P06", D, "denunciante", {"mencion": "M-UT06-204"},
  "calificacion-de-conducta", {"literal": "sin que el subdelegado se moviese a cosa alguna"},
  "sin que el subdelegado se moviese a cosa alguna", fundamento="experiencia-propia")
a("A-UT06-207", "UT06", "P06", D, "denunciante", {"mencion": "M-UT06-205"},
  "participa-en-hecho", {"hecho": "H-p06-matricula"},
  "ha hecho de mi Chuquitapa lo que ha querido y conseguido también el que se me matricule", rol_en_hecho="instigador")
a("A-UT06-208", "UT06", "P06", D, "denunciante", {"mencion": D},
  "participa-en-hecho", {"hecho": "H-p06-matricula"}, "conseguido también el que se me matricule", rol_en_hecho="victima")
a("A-UT06-209", "UT06", "P06", D, "denunciante", {"mencion": D},
  "calificacion-de-conducta", {"literal": "fiel vasallo"}, "en la remuneración que he conseguido por fiel vasallo")
a("A-UT06-210", "UT06", "P06", D, "denunciante", {"mencion": "M-UT06-209"},
  "participa-en-hecho", {"hecho": "H-p06-amenaza"}, "por parte de Chuquitapa se me amenaza con la muerte",
  rol_en_hecho="agresor", fundamento="experiencia-propia")
a("A-UT06-211", "UT06", "P06", D, "denunciante", {"mencion": "M-UT06-211"},
  "solicita", {"literal": "se digne dirigir esta mi representación al muy ilustre señor presidente"},
  "se digne dirigir esta mi representación al muy ilustre señor presidente")
a("A-UT06-212", "UT06", "P06", D, "denunciante", {"mencion": "M-UT06-213"},
  "solicita", {"literal": "se me saque de la matricula relevándoseme de la contribución del tributo"},
  "se me saque de la matricula relevándoseme de la contribución del tributo",
  nota="Lo pide al Presidente por medio del Fiscal Protector; sujeto = autoridad a quien se dirige la súplica.")
a("A-UT06-213", "UT06", "P06", D, "denunciante", {"mencion": "M-UT06-213"},
  "solicita", {"literal": "se liberen las mas serias providencias"},
  "por lo que respecta a las injurias reales de que llevo hecha mención, se liberen las mas serias providencias")
a("A-UT06-214", "UT06", "P06", D, "denunciante", {"mencion": "M-UT06-213"},
  "solicita", {"literal": "que mi por Chuquitapa ni por otros de su compañía se me infiera daño"},
  "mandándose ante todas cosas, que mi por Chuquitapa ni por otros de su compañía se me infiera daño")
a("A-UT06-215", "UT06", "P06", D, "denunciante", {"mencion": "M-UT06-219"},
  "solicita", {"literal": "se sirva elevar mi queja al Juzgado que expreso"},
  "A vuestro señor pido y suplico se sirva elevar mi queja al Juzgado que expreso")
a("A-UT06-216", "UT06", "P06", D, "denunciante", {"mencion": D},
  "presta-juramento", {"literal": "no proceder de malicia"}, "jurando no proceder de malicia")
a("A-UT06-217", "UT06", "P06", D, "denunciante", {"mencion": "M-UT06-220"},
  "cantidad-denunciada", {"literal": "la ingente cantidad de dinero que ha usurpado"},
  "la ingente cantidad de dinero que ha usurpado aquel al Real grasia")
a("A-UT06-218", "UT06", "P06", D, "denunciante", {"hecho": "H-p06-alboroto"},
  "veracidad", {"literal": "documentos calificativos del hecho que refiero"},
  "en el supuesto de tener yo documentos calificativos del hecho que refiero",
  nota="El denunciante dice tener documentos que prueban el hecho; se entiende que alude a las certificaciones P01–P05 (inferencia).")

# ───────────── P07 · Vista fiscal · UT07–UT08 ─────────────
m("M-UT07-201", "UT07", "P07", "persona", "Muy ilustre Señor Presidente", "Muy ilustre Señor Presidente El fiscal", rol="destinatario")
m("M-UT07-202", "UT07", "P07", "persona", "El fiscal de su Majestad", "El fiscal de su Majestad acompañando", rol="dictaminador")
m("M-UT07-203", "UT07", "P07", "cosa", "el antecedente escrito", "acompañando el antecedente escrito que le ha presentado")
m("M-UT07-204", "UT07", "P07", "persona", "Manuel Guancachoque", "presentado Manuel Guancachoque indio del Pueblo de Tinta")
m("M-UT07-205", "UT07", "P07", "lugar", "Pueblo de Tinta", "indio del Pueblo de Tinta: Dice", tipo="pueblo")
m("M-UT07-206", "UT07", "P07", "grupo", "cincuenta y un tributarios", "aver denunciado cincuenta y un tributarios en la revisita")
m("M-UT07-207", "UT07", "P07", "lugar", "aquel partido", "en la revisita de aquel partido contra", tipo="partido")
m("M-UT07-208", "UT07", "P07", "grupo", "sus parciales", "este y sus parciales amén")
m("M-UT07-209", "UT07", "P07", "lugar", "la carcel", "estando aquel en la carcel", tipo="carcel")
m("M-UT07-210", "UT07", "P07", "cosa", "las certificaciones de testigos", "lo califican con las certificaciones de testigos que acompañan")
m("M-UT07-211", "UT07", "P07", "persona", "subdelegado del partido de Tinta", "la respectiva orden del subdelegado del partido de Tinta")
m("M-UT07-212", "UT07", "P07", "lugar", "partido de Tinta", "del subdelegado del partido de Tinta, para", tipo="partido")
m("M-UT07-213", "UT07", "P07", "persona", "el referido recaudador", "el referido recaudador incomode")
m("M-UT07-214", "UT07", "P07", "persona", "el suplicante", "reconociendo el suplicante su escrito")
m("M-UT07-216", "UT07", "P07", "persona", "aquel", "estando aquel en la carcel")
m("M-UT07-215", "UT07", "P07", "persona", "al suplicante", "ni infiera perjuicio al suplicante en odio")
m("M-UT08-201", "UT08", "P07", "persona", "Subdelegado", "que informen el mismo Subdelegado, con el Apoderado")
m("M-UT08-202", "UT08", "P07", "persona", "Apoderado Fiscal de la revisita", "con el Apoderado Fiscal de la revisita, verificandolo")
m("M-UT08-203", "UT08", "P07", "persona", "el suplicante", "en premio de ella solicita el suplicante, que informen")
m("M-UT08-204", "UT08", "P07", "lugar", "Cusco", "Cusco y Agosto 21 de 1806", tipo="ciudad")

F = "M-UT08-001"
NOTA_F = ("Afirmante: el firmante de la vista («Gómez del Rio», UT08), como en A-UT07-001; el texto se enuncia como "
          "«El fiscal de su Majestad … Dice» (M-UT07-202).")
a("A-UT07-201", "UT07", "P07", F, "dictaminador", {"mencion": "M-UT07-204"},
  "tiene-condicion", {"concepto": "indio"}, "Manuel Guancachoque indio del Pueblo de Tinta", fundamento="actuado", nota=NOTA_F)
a("A-UT07-202", "UT07", "P07", F, "dictaminador", {"mencion": "M-UT07-001"},
  "cantidad-denunciada", {"literal": "cincuenta y un tributarios"},
  "aver denunciado cincuenta y un tributarios en la revisita de aquel partido contra el Recaudador", fundamento="actuado",
  nota="Resume el escrito P06 (44 + 7 = 51).")
a("A-UT07-203", "UT07", "P07", F, "dictaminador", {"mencion": "M-UT07-204", "eliptico": True},
  "participa-en-hecho", {"hecho": "H-p07-denuncia"},
  "se queja de que en odio de aver denunciado cincuenta y un tributarios en la revisita de aquel partido",
  rol_en_hecho="participante-en-hecho", fundamento="actuado", nota="Sujeto elíptico: el que se queja, Manuel Guancachoque.")
a("A-UT07-204", "UT07", "P07", F, "dictaminador", {"hecho": "H-p07-denuncia"},
  "lugar-del-hecho", {"mencion": "M-UT07-207"}, "en la revisita de aquel partido contra", fundamento="actuado")
a("A-UT07-205", "UT07", "P07", F, "dictaminador", {"mencion": "M-UT07-208"},
  "participa-en-hecho", {"hecho": "H-p07-maltrato"},
  "este y sus parciales amén de aver logrado su prision, lo han maltratado de obra, e injuriado de palabra",
  rol_en_hecho="agresor", fundamento="actuado")
a("A-UT07-206", "UT07", "P07", F, "dictaminador", {"mencion": "M-UT07-001", "eliptico": True},
  "participa-en-hecho", {"hecho": "H-p07-maltrato"},
  "este y sus parciales amén de aver logrado su prision, lo han maltratado de obra, e injuriado de palabra",
  rol_en_hecho="agresor", fundamento="actuado", nota="«este» remite al Recaudador Chuquitapa nombrado justo antes.")
a("A-UT07-207", "UT07", "P07", F, "dictaminador", {"mencion": "M-UT07-001", "eliptico": True},
  "participa-en-hecho", {"hecho": "H-p07-prision"}, "este y sus parciales amén de aver logrado su prision",
  rol_en_hecho="instigador", fundamento="actuado", nota="Mismo sujeto elíptico que A-UT07-206.")
a("A-UT07-208", "UT07", "P07", F, "dictaminador", {"mencion": "M-UT07-204", "eliptico": True},
  "participa-en-hecho", {"hecho": "H-p07-prision"}, "amén de aver logrado su prision", rol_en_hecho="preso",
  fundamento="actuado", nota="«su prision»: la del quejoso Manuel Guancachoque.")
a("A-UT07-209", "UT07", "P07", F, "dictaminador", {"hecho": "H-p07-alboroto"},
  "fecha-del-hecho", {"literal": "antes ayer"}, "antes ayer precurado matarlo con alboroto de noche", fundamento="actuado",
  nota="«antes ayer» es relativo a la fecha de la vista (21 de agosto) o del escrito; véase la contradicción F1.")
a("A-UT07-210", "UT07", "P07", F, "dictaminador", {"hecho": "H-p07-alboroto"},
  "fecha-del-hecho", {"literal": "de noche"}, "precurado matarlo con alboroto de noche", fundamento="actuado")
a("A-UT07-211", "UT07", "P07", F, "dictaminador", {"hecho": "H-p07-alboroto"},
  "lugar-del-hecho", {"mencion": "M-UT07-209"}, "estando aquel en la carcel", fundamento="actuado")
a("A-UT07-220", "UT07", "P07", F, "dictaminador", {"mencion": "M-UT07-216"},
  "participa-en-hecho", {"hecho": "H-p07-alboroto"}, "precurado matarlo con alboroto de noche, y estando aquel en la carcel",
  rol_en_hecho="victima", fundamento="actuado")
a("A-UT07-212", "UT07", "P07", F, "dictaminador", {"hecho": "H-p07-alboroto"},
  "veracidad", {"literal": "parece que lo califican con las certificaciones de testigos"},
  "este hecho parece que lo califican con las certificaciones de testigos que acompañan a su escrito", fundamento="actuado")
a("A-UT07-213", "UT07", "P07", F, "dictaminador", {"mencion": "M-UT07-204", "eliptico": True},
  "tiene-condicion", {"concepto": "tributario"}, "ampliando su queja al de averse matriculado en clase de tributario",
  fundamento="actuado", nota="El fiscal refiere la queja de haber sido matriculado como tributario (cf. A-UT06-005).")
a("A-UT07-214", "UT07", "P07", F, "dictaminador", {"mencion": "M-UT07-204", "eliptico": True},
  "solicita", {"literal": "se le exima en premio del servicio que ha hecho"},
  "solicita se le exima en premio del servicio que ha hecho", fundamento="actuado",
  nota="El fiscal refiere lo que solicita el suplicante; sujeto elíptico = Manuel Guancachoque.")
a("A-UT07-215", "UT07", "P07", F, "dictaminador", {"mencion": "M-UT07-201"},
  "solicita", {"literal": "reconociendo el suplicante su escrito en la forma acostumbrada"},
  "siendo servido mandar que reconociendo el suplicante su escrito en la forma acostumbrada")
a("A-UT07-216", "UT07", "P07", F, "dictaminador", {"mencion": "M-UT07-201"},
  "solicita", {"literal": "se dirija la respectiva orden del subdelegado del partido de Tinta"},
  "se dirija la respectiva orden del subdelegado del partido de Tinta")
a("A-UT07-217", "UT07", "P07", F, "dictaminador", {"mencion": "M-UT07-201"},
  "solicita", {"literal": "el referido recaudador incomode ni infiera perjuicio al suplicante"},
  "por medio de otro alguno el referido recaudador incomode ni infiera perjuicio al suplicante en odio de la denuncia",
  nota="Petición en forma negativa en el original («ni por simi- por medio de otro alguno … incomode»); el literal es la acción a impedir.")
a("A-UT07-218", "UT07", "P07", F, "dictaminador", {"mencion": "M-UT07-211"},
  "ejerce-cargo", {"concepto": "subdelegado"}, "la respectiva orden del subdelegado del partido de Tinta")
a("A-UT07-219", "UT07", "P07", F, "dictaminador", {"mencion": "M-UT07-213"},
  "ejerce-cargo", {"concepto": "recaudador-de-tributos"}, "el referido recaudador incomode")
a("A-UT08-201", "UT08", "P07", F, "dictaminador", {"mencion": "M-UT07-201"},
  "solicita", {"literal": "proceda a reesivir de oficio con la prudencia y reserva conducente la justificación correspondiente sobre el alboroto o exceso que se enuncia, y los principales que lo huviesen fomentado"},
  "proceda a reesivir de oficio con la prudencia y reserva conducente la justificación correspondiente sobre el alboroto o exceso que se enuncia, y los principales que lo huviesen fomentado",
  nota="Continúa la petición de UT07: el subdelegado debe recibir información de oficio.")
a("A-UT08-202", "UT08", "P07", F, "dictaminador", {"mencion": "M-UT07-201"},
  "solicita", {"literal": "que informen el mismo Subdelegado, con el Apoderado Fiscal de la revisita, verificandolo por separado"},
  "que informen el mismo Subdelegado, con el Apoderado Fiscal de la revisita, verificandolo por separado")
a("A-UT08-203", "UT08", "P07", F, "dictaminador", {"mencion": "M-UT08-202"},
  "ejerce-cargo", {"concepto": "apoderado-fiscal-revisita"}, "con el Apoderado Fiscal de la revisita")
a("A-UT08-204", "UT08", "P07", F, "dictaminador", {"mencion": "M-UT08-201"},
  "ejerce-cargo", {"concepto": "subdelegado"}, "que informen el mismo Subdelegado")
a("A-UT08-205", "UT08", "P07", F, "dictaminador", {"mencion": "M-UT08-203"},
  "solicita", {"literal": "lo que en premio de ella solicita el suplicante"},
  "Y en quanto a la denuncia, y por lo que en premio de ella solicita el suplicante", fundamento="actuado",
  nota="Referencia de la vista a la solicitud del suplicante (exención de matrícula), ya registrada en A-UT07-214.")

# ───────────── P08 · Notificación del decreto al fiscal · UT08 ─────────────
m("M-UT08-205", "UT08", "P08", "lugar", "Cusco", "En el Cusco y Agosto veinte y tres", tipo="ciudad")
m("M-UT08-206", "UT08", "P08", "cosa", "el Decreto que antecede", "en el presente el Decreto que antecede al Señor")
m("M-UT08-207", "UT08", "P08", "persona", "Don Luis Gomez del Rio", "al Señor Don Luis Gomez del Rio del consejo", rol="notificado")
m("M-UT08-233", "UT08", "P08", "grupo", "consejo de su Majestad", "del consejo de su Majestad su fiscal")
m("M-UT08-208", "UT08", "P08", "grupo", "Real Audiencia", "su fiscal en esta Real Audiencia estando")
m("M-UT08-209", "UT08", "P08", "lugar", "las casas de su morada", "estando en las casas de su morada doy fe", tipo="edificio")
m("M-UT08-210", "UT08", "P08", "persona", "Chacón", "Firma de Chacón", rol="firmante")

E8 = "M-UT08-210"
a("A-UT08-206", "UT08", "P08", E8, "fedatario", {"mencion": "M-UT08-207"},
  "ejerce-cargo", {"concepto": "fiscal-audiencia"}, "del consejo de su Majestad su fiscal en esta Real Audiencia")
a("A-UT08-207", "UT08", "P08", E8, "fedatario", {"mencion": "M-UT08-207"},
  "se-hallaba", {"mencion": "M-UT08-209"}, "estando en las casas de su morada doy fe")
a("A-UT08-208", "UT08", "P08", E8, "fedatario", {"pieza": "P08"},
  "firmo", {"mencion": E8}, "doy fe Firma de Chacón",
  nota="El fedatario se identifica solo por la firma «Chacón»; la transcripción no da su cargo.")

# ───────────── P09 · Reconocimiento y ratificación ante el teniente asesor · UT08 ─────────────
m("M-UT08-211", "UT08", "P09", "lugar", "ciudad del Cuzco", "En la ciudad del Cuzco en trece días", tipo="ciudad")
m("M-UT08-212", "UT08", "P09", "cosa", "Decreto marginal", "lo mando en el Decreto marginal")
m("M-UT08-213", "UT08", "P09", "persona", "Don Manuel Galeano", "El señor Don Manuel Galeano Teniente Asesor", rol="receptor")
m("M-UT08-214", "UT08", "P09", "lugar", "este Govierno e intendencia", "Teniente Asesor de este Govierno e intendencia en virtud",
  tipo="intendencia")
m("M-UT08-215", "UT08", "P09", "cosa", "dicho decreto", "conferida por dicho decreto mandó")
m("M-UT08-216", "UT08", "P09", "persona", "Manuel Guancachoque", "comparecer ante su a Manuel Guancachoque yndio",
  rol="declarante")
m("M-UT08-217", "UT08", "P09", "lugar", "Pueblo de Tinta", "yndio originario del Pueblo de Tinta de quien", tipo="pueblo")
m("M-UT08-218", "UT08", "P09", "persona", "Doctor Don Manuel Valencia", "presencia del Doctor Don Manuel Valencia Abogado",
  rol="protector")
m("M-UT08-219", "UT08", "P09", "lugar", "esta provincia", "de naturales de esta provincia e interpretes")
m("M-UT08-220", "UT08", "P09", "grupo", "interpretes generales", "e interpretes generales por mi el presente", rol="interprete")
m("M-UT08-221", "UT08", "P09", "persona", "Escribano mayor de Gobierno", "el presente Escribano mayor de Gobierno le recivio",
  rol="fedatario")
m("M-UT08-222", "UT08", "P09", "cosa", "su escrito", "leído se le su escrito de folio dijo")
m("M-UT08-223", "UT08", "P09", "persona", "al que se lo hizo", "las instrucciones que comunico al que se lo hizo en cuyo")
m("M-UT08-224", "UT08", "P09", "persona", "su Merced", "lo firmó con su Merced protector")
m("M-UT08-225", "UT08", "P09", "persona", "protector", "con su Merced protector e interpretes de que")
m("M-UT08-226", "UT08", "P09", "grupo", "interpretes", "su Merced protector e interpretes de que doy fe")
m("M-UT08-227", "UT08", "P09", "persona", "Galeano", "Firma Galeano", rol="firmante")
m("M-UT08-228", "UT08", "P09", "persona", "Don Valencia", "Firma Don Valencia", rol="firmante")
m("M-UT08-229", "UT08", "P09", "persona", "Marcos Salcedo", "Firma Marcos Salcedo", rol="firmante")
m("M-UT08-230", "UT08", "P09", "persona", "Juan Clemente Jordan", "Firma Juan Clemente Jordan", rol="firmante")
m("M-UT08-231", "UT08", "P09", "persona", "Manuel Guancachoque", "Firma Manuel Guancachoque", rol="firmante")
m("M-UT08-232", "UT08", "P09", "lugar", "Cuzco", "Firma Manuel Guancachoque Cuzco", tipo="ciudad")

E9 = "M-UT08-221"
G9 = "M-UT08-216"
a("A-UT08-209", "UT08", "P09", E9, "fedatario", {"mencion": "M-UT08-213"},
  "ejerce-cargo", {"concepto": "teniente-asesor"}, "Don Manuel Galeano Teniente Asesor de este Govierno e intendencia")
a("A-UT08-210", "UT08", "P09", E9, "fedatario", {"mencion": "M-UT08-213"},
  "participa-en-hecho", {"hecho": "H-p09-comparecencia"},
  "en virtud de la comiscion a el conferida por dicho decreto mandó comparecer ante su a Manuel Guancachoque",
  rol_en_hecho="ordenante")
a("A-UT08-211", "UT08", "P09", E9, "fedatario", {"mencion": G9},
  "tiene-condicion", {"concepto": "indio"}, "Manuel Guancachoque yndio originario del Pueblo de Tinta")
a("A-UT08-212", "UT08", "P09", E9, "fedatario", {"mencion": G9},
  "tiene-condicion", {"concepto": "originario"}, "Manuel Guancachoque yndio originario del Pueblo de Tinta")
a("A-UT08-213", "UT08", "P09", E9, "fedatario", {"mencion": "M-UT08-218"},
  "ejerce-cargo", {"concepto": "protector-partidario"},
  "Doctor Don Manuel Valencia Abogado protector partidario de naturales de esta provincia")
a("A-UT08-214", "UT08", "P09", E9, "fedatario", {"mencion": E9},
  "ejerce-cargo", {"concepto": "escribano"}, "el presente Escribano mayor de Gobierno")
a("A-UT08-215", "UT08", "P09", E9, "fedatario", {"mencion": G9},
  "presta-juramento", {"literal": "a Dios nuestro Señor y a una señal de Cruz"},
  "le recivio juramento que lo hizo a Dios nuestro Señor y a una señal de Cruz")
a("A-UT08-216", "UT08", "P09", G9, "declarante", {"pieza": "P06"},
  "redacto", {"mencion": "M-UT08-223"}, "según las instrucciones que comunico al que se lo hizo",
  nota="El declarante no nombra a quien escribió materialmente el escrito; solo que lo hizo otro según sus instrucciones.")
a("A-UT08-217", "UT08", "P09", G9, "declarante", {"pieza": "P06"},
  "ratifica-contenido", {"mencion": G9}, "en cuyo contesto se afirma y ratifica y siendo necesario lo reproduce")
a("A-UT08-218", "UT08", "P09", G9, "declarante", {"pieza": "P06"},
  "motivo", {"literal": "está hecho se su voluntad"}, "dijo: que esté está hecho se su voluntad")
a("A-UT08-219", "UT08", "P09", E9, "fedatario", {"pieza": "P06"},
  "folio-de-pieza", {"literal": "de folio"}, "leído se le su escrito de folio dijo",
  nota="La transcripción no da número de folio tras «de folio».")
for i, mm in enumerate([G9, "M-UT08-224", "M-UT08-225", "M-UT08-226"], 220):
    a(f"A-UT08-{i}", "UT08", "P09", E9, "fedatario", {"pieza": "P09"},
      "firmo", {"mencion": mm}, "lo firmó con su Merced protector e interpretes de que doy fe",
      distribuida=True,
      nota="«lo firmó con su Merced protector e interpretes» se reparte en un registro por firmante; el sujeto de "
           "«lo firmó» es el declarante Manuel Guancachoque.")

if __name__ == "__main__":
    out = Path(__file__).with_suffix(".jsonl")
    with out.open("w", encoding="utf-8") as f:
        for r in M + A:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{len(M)} menciones, {len(A)} afirmaciones -> {out}")
