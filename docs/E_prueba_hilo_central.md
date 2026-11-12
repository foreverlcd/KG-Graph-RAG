# E · Prueba en profundidad: certificaciones de agosto frente a declaraciones de septiembre

> Un solo hilo de punta a punta: cita → registro plano → tripletas → consulta → respuesta. Todo lo de este
> documento sale de archivos versionados: `datos/registros/hilo_central.py`, `datos/grafo/hilo_central.trig`,
> `consultas/afirmaciones.rq` y `docs/anexos/respuestas_pc.md`. Ese último lo genera `scripts/responder_pc.py`,
> no está escrito a mano.
>
> **Quién anotó.** La anotación de este hilo la hizo el modelador, que es un LLM (Claude Opus 5.5), y no tiene validación humana. Así
> consta en la procedencia del grafo (PC20: «validación humana: NO REGISTRADA»). Es un ejemplo trabajado y la semilla
> del estándar de oro, no el estándar de oro (ver `docs/G_evaluacion.md` §4).

## 1. El hilo en la fuente

En agosto de 1806, Huancachoque presenta certificaciones firmadas por milicianos de Tinta (P01–P05). En septiembre,
el subdelegado Pedro de la Mata, juez comisionado y la misma autoridad que mandó encarcelar al denunciante (UT18),
recibe declaraciones juradas a esos mismos firmantes (P18–P21). La tabla resume lo anotado. Cada celda es una o varias
afirmaciones con su id; las citas exactas están en `datos/registros/hilo_central.jsonl`.

| Testigo (reconstrucción) | Certificación (agosto) | Declaración jurada (septiembre) |
|---|---|---|
| Isidro Cano (R-cano) | P01, UT01. Chuquitapa fue «complice y coronel» de Túpac Amaru (A-UT01-001/002). Alzamiento «a media noche» (A-UT01-003). Sospecha de que lo ordenó Chuquitapa (A-UT01-004). | P18, UT11–12.a. La firma es suya (A-UT11-001) y se ratifica (A-UT11-002), con dos salvedades: «Comisionado por este y **no coronel**» (A-UT11-003/004) y lo del alzamiento «no le consta» salvo de oídas, por Santiago Cazorla (A-UT11-005). Dio la certificación porque Huancachoque «fue a su casa suplicandole» (A-UT12a-001). |
| Fernando Orue (R-orue) | P04, UT03. «coronel, comecionado» (A-UT03-001/002), «pariente» de Túpac Amaru (A-UT03-003), «a las diez de la noche» (A-UT03-004). | P21, UT14–15. **No firmó**: firmó un hijo suyo (A-UT14-001, A-UT15-002). La redactó «un hijo suyo» y, en la misma declaración, «como ha puesto guasscachoque» (A-UT14-002/003). La hora **no** fue «a las dies», sino «el primer puesto del gallo» (A-UT14-004/005). Mantiene «coronel y comisionado» (A-UT14-006/007). Actuó por enemistad con la mujer de Chuquitapa (A-UT15-001). |
| Martín Cazorla (R-martin-cazorla) y declarante de P19 (hipótesis en competencia, PC19) | P05, UT04. «se alzaron los Indios todos con garrotes» (A-UT04-002) y «abra nuevamente porque es desde el rebelde» (A-UT04-001). | P19, UT12. No sabe escribir (A-UT12b-001). Mandó a **Simón Arce** ponerla por escrito (A-UT12b-002) y no sabe quién firmó (A-UT12b-003). **No dijo** lo del alzamiento ni lo del «Rebelde», porque era muchacho (A-UT12b-004/005). Vio «quatro o seis Yndios» (A-UT12b-006). Tenía 28 años (A-UT13-001). |
| «don Juan Quiñones» / Juan Cazorla (R-quinones, indeterminado; R-juan-cazorla) | P03, UT02. «a las dies o a las once» (A-UT02-001). | No declaró: estaba ausente. El juez afirma que «no hay tal hombre en el pueblo de Tinta» (A-UT17-002) y que la firmó Juan Cazorla (A-UT17-001). |

Después llegan dos informes y una resolución:

* **Informe del subdelegado** (P27, UT17–18): las certificaciones «fueron hechos por el mismo Guancachoque» y se firmaron «sin saber lo mas de sus contenidos» (A-UT17-101…114).
* **Vista fiscal** (P29, UT19–20): las quejas son «menos conforme a la verdad» (A-UT19-001).
* **Auto** (P28, UT19): «de conformidad» con la vista fiscal (A-UT19-004).

El hilo sobre Túpac Amaru tiene **dos direcciones**. Los testigos de agosto imputan a Chuquitapa un cargo en la rebelión.
El cura, a petición del subdelegado, imputa al denunciante ser «hijo Espurio de Antolin Ortiz… caudillo» de Túpac Amaru
(A-UT16a-001/002). El subdelegado lo remata con «Chispa soplada por Guancachoque» (UT18). El modelo registra las
dos imputaciones como afirmaciones de quien las hace, y ninguna como hecho.

## 2. Recorrido completo de una afirmación: A-UT11-004 (Cano niega «coronel»)

### 2.1 Cita en la fuente

* Tramo **UT11**, líneas 146–193 de la transcripción canónica.
* **Folio: no consta en la transcripción**. El primer folio explícito es el 20, en UT12.b. Recto o vuelto: no consta.
* Texto (las líneas parten la frase; la cita es literal tras colapsar los espacios):

```text
el porque sucedió en tiempo de corregidor Don Andres
……..y que en tiempo del rebelde Tupa amaro fue
Comisionado por este y no coronel como expone en
su certificación que el parajeque expone de la noche
```

### 2.2 Registros planos: lo que escribe el LLM o el anotador

Son dos menciones (capa 2) y una afirmación (capa 3). Sin IRIs, sin CIDOC CRM y con listas cerradas tomadas del tesauro:

```json
{"tipo_registro": "mencion", "id": "M-UT11-001", "tramo": "UT11", "pieza": "P18", "clase": "persona",
 "texto": "Ysidro Cano", "rol_en_pieza": "declarante", "cita": "la persona de D. Ysidro Cano vecino Español"}
{"tipo_registro": "mencion", "id": "M-UT01-004", "tramo": "UT01", "pieza": "P01", "clase": "persona",
 "texto": "Chuquitapa", "rol_en_pieza": null, "cita": "mando dicho Chuquitapa cargando"}
{"tipo_registro": "afirmacion", "id": "A-UT11-004", "tramo": "UT11", "pieza": "P18",
 "afirmante": "M-UT11-001", "rol_afirmante": "declarante",
 "sujeto": {"mencion": "M-UT01-004", "eliptico": true}, "atributo": "ejerce-cargo",
 "valor": {"concepto": "coronel-rebelde"}, "polaridad": "niega", "fundamento": "no-indica",
 "cita": "Comisionado por este y no coronel como expone en su certificación",
 "nota": "Sujeto elíptico (ver A-UT11-003). Niega expresamente lo afirmado en A-UT01-001."}
```

Validaciones que pasa antes de mapearse (`src/laad/esquema.py`, `src/laad/registros.py`):

* la cita es subcadena exacta de UT11;
* `ejerce-cargo`, `coronel-rebelde`, `declarante` y `niega` existen en el tesauro;
* `declarante` está en la rama `rol:afirmante`;
* el sujeto elíptico lleva nota;
* el tramo UT11 pertenece a la pieza P18;
* las dos menciones existen;
* el id no se repite.

### 2.3 Tripletas: lo que produce el mapeo determinista

Extracto literal de `datos/grafo/hilo_central.trig`. Hay un grafo nombrado por capa:

```turtle
g:documento {                                              # capa 1 (curada a mano)
  id:cc-14-18/actuacion/P18  crm:P2_has_type act:declaracion-jurada, fza:testimonial ;
                             crm:P94_has_created id:cc-14-18/pieza/P18 . }

<…/grafo/texto/anotacion-manual-hilo-central-v1> {        # capa 2: la mención tal como está escrita
  id:…/mencion/M-UT11-001 a picom:PersonObservation, crm:E21_Person ;
      rdfs:label "Ysidro Cano" ; prov:hadPrimarySource id:…/pieza/P18 ; picom:hasRole rol:declarante ;
      crm:P1_is_identified_by [ a crm:E41_Appellation ; crm:P190_has_symbolic_content "Ysidro Cano" ] . }

<…/grafo/afirmaciones/anotacion-manual-hilo-central-v1> {  # capa 3: la afirmación (patrón STAR sobre E13)
  id:…/afirmacion/A-UT11-004 a crm:E13_Attribute_Assignment ;
      crm:P9i_forms_part_of id:…/actuacion/P18 ;                     # en qué actuación (→ tipo, fecha, ante quién, firmas)
      crm:P14_carried_out_by id:…/mencion/M-UT11-001 ;               # quién lo afirma
      crm:P140_assigned_attribute_to id:…/mencion/M-UT01-004 ;       # sobre quién (sujeto elíptico)
      crm:P177_assigned_property_of_type atr:ejerce-cargo ;          # qué se afirma
      crm:P141_assigned cargo:coronel-rebelde ;                       # valor
      crm:P2_has_type pol:niega, fun:no-indica, fza:testimonial, anot:sujeto-eliptico .
  id:…/afirmacion/A-UT11-004/participacion/afirmante a crm:PC14_carried_out_by ;
      crm:P01_has_domain id:…/afirmacion/A-UT11-004 ; crm:P02_has_range id:…/mencion/M-UT11-001 ;
      crm:P14.1_in_the_role_of rol:declarante .
  id:…/anotacion/A-UT11-004 a oa:Annotation ; oa:hasBody id:…/afirmacion/A-UT11-004 ; oa:motivatedBy oa:describing ;
      oa:hasTarget [ oa:hasSource id:…/transcripcion/bd945513f8e1/UT11 ;
                     oa:hasSelector [ a oa:TextQuoteSelector ; oa:exact "Comisionado por este y no coronel como expone en su certificación" ],
                                    [ a oa:TextPositionSelector ; oa:start 1533 ; oa:end 1599 ] ] . }

<…/grafo/reconstruccion/R-cano> {                         # capa 4: el investigador identifica a Cano
  id:persona/cano a picom:PersonReconstruction, crm:E21_Person ;
      prov:wasDerivedFrom id:…/mencion/M-UT01-001, …/M-UT01-006, …/M-UT11-001, …/M-UT12.a-001 ;
      prov:wasGeneratedBy id:inferencia/R-cano .
  id:inferencia/R-cano a crminf:I5_Inference_Making ; crm:P14_carried_out_by id:agente/claude-opus-5-5 ;
      crm:P17_was_motivated_by id:…/afirmacion/A-UT11-001 ;          # premisa: reconoce su firma
      crminf:J2_concluded_that id:creencia/R-cano .
  id:creencia/R-cano a crminf:I2_Belief ; crminf:J4_that <…/grafo/reconstruccion/R-cano> ; crminf:J5_holds_to_be "probable" . }
```

La procedencia del dato (grafo `g:procedencia`) dice que el grafo de afirmaciones `prov:wasGeneratedBy` la actividad
`actividad/anotacion-manual-hilo-central-v1`. Esa actividad `prov:used` la transcripción `sha256:bd945513…`, con el
plan «anotacion-manual» y el agente `claude-opus-5-5` (`prov:SoftwareAgent`). No hay validación humana registrada.

### 2.4 La consulta

El agente no escribe SPARQL. Elige la consulta con nombre `afirmaciones` y le pasa dos IRIs validadas, que se
insertan como bloque `VALUES` (`src/laad/consulta.py`):

```sparql
VALUES ?filtroEntidad { <https://w3id.org/laad/id/persona/chuquitapa> }
VALUES ?atributo { <https://w3id.org/laad/tesauro/atributo/ejerce-cargo> }
```

La consulta (`consultas/afirmaciones.rq`) reúne todas las facetas de cada E13:

* quién afirma (mención y reconstrucción) y con qué rol;
* el tipo de actuación y la fecha escrita;
* **ante quién**: PC14 en la actuación con un rol en la rama `rol:receptor`;
* **quién firma la pieza**: PC14 con un rol en la rama `rol:firmante`;
* la polaridad, el fundamento y la fuerza institucional;
* la cita, el tramo y el folio. Si no hay folio, el campo queda vacío y la respuesta dice «no consta».

La disputa no está almacenada. `responder.disputa()` la calcula agrupando por valor y polaridad, y `consultas/disputas.rq`
la detecta en todo el grafo.

### 2.5 La respuesta que ve el investigador (PC09, generada)

```text
PREGUNTA: ¿Fue Andrés Chuquitapa coronel de Túpac Amaru en la rebelión?
RESPUESTA (DISPUTA): Está en disputa («coronel (de Túpac Amaru)»). Lo afirman: «Isidro Cano» [= Isidro Cano, sargento
de milicias, vecino español de Tinta, según reconstrucción] (certificación P01, UT01); «Fernando Orue» [= Fernando Orue,
…] (certificación P04, UT03); «fernando ore» [= Fernando Orue, …] (declaración jurada P21, UT14). Lo niegan: «Ysidro
Cano» [= Isidro Cano, …] (declaración jurada P18, UT11).

— Lo que se afirma en el expediente (capa 3) —
AFIRMACIÓN A-UT11-004 [NIEGA]: ejerce o ejerció un cargo → coronel (de Túpac Amaru) (sujeto elíptico resuelto por el anotador)
    «Comisionado por este y no coronel como expone en su certificación»
    Afirmante: «Ysidro Cano» (declarante) [= Isidro Cano, …, según reconstrucción]; declaración jurada P18, fecha escrita
    «Veinte y tres dias del mes de Septiembre de mil ochocientos y seis años»; ante: Pedro de la Mata;
    firma la pieza: YSIDRO CANO / PEDRO DE LA MATA
    Fundamento invocado: no lo indica; fuerza institucional: testimonial; UT11, folio no consta en la transcripción
(… A-UT01-001, A-UT03-001, A-UT14-006 con el mismo formato …)

— Reconstrucción del investigador (capa 4) —
RECONSTRUCCIÓN «Andrés Chuquitapa, cacique y recaudador de tributos de Tinta» — creencia: probable; autor: claude-opus-5-5; …

Afirmaciones relacionadas (no forman la disputa): A-UT01-002 (cómplice), A-UT03-002, A-UT11-003, A-UT14-007 (comisionado).
Ninguna actuación de fuerza dictaminadora o resolutiva se pronuncia sobre este punto.
```

La respuesta completa está en `docs/anexos/respuestas_pc.md` §PC09.

## 3. Qué demuestra el hilo (y qué no)

**Demuestra:**

1. **El mismo testigo, dos actuaciones y la polaridad contraria quedan juntos** sin fusionar menciones. «Isidro Cano» (P01) e «Ysidro Cano» (P18) siguen siendo dos observaciones. Las une una reconstrucción con autor, creencia y premisa: reconoce su firma, A-UT11-001.
2. **Una resolución no es un hecho.** La vista fiscal y el auto aparecen en PC16 como afirmaciones de fuerza dictaminadora o resolutiva. El grafo informa además de que ninguna se pronuncia sobre el cargo de Chuquitapa en 1780.
3. **Las disputas se calculan.** `consultas/disputas.rq` encuentra ocho en la versión revisada:

   | Disputa | Tipo |
   |---|---|
   | Hora del alboroto | 6 afirmaciones; «valores distintos (revisar)» |
   | Orue niega la hora de su propia certificación | niega lo afirmado (responde_a) |
   | «coronel» | afirma/niega |
   | «coronel»: Cano niega lo afirmado en P01 | responde_a |
   | Redacción de P04 | valores distintos |
   | Redacción de P05 | valores distintos |
   | Las frases de P05 negadas en P19 | responde_a; solo bajo la hipótesis «el declarante es Martín» |
   | Duración de la prisión | valores distintos |

   Además, `disputas_firma.rq` encuentra la firma de P04: lo que el texto muestra frente a lo que el declarante niega.

4. **Las facetas «ante quién / quién firma»** salen de la actuación, y responden «no consta» cuando la fuente calla. Las certificaciones de agosto no tienen receptor: no se dieron ante juez.

**No demuestra (límites conocidos):**

* **El folio y el recto/vuelto de casi todas las citas.** Hacen falta las imágenes (`docs/01_materiales.md` §3).
* **Que la *extracción* automática alcance esta calidad.** Esto está anotado a mano; la medición está en `docs/G_evaluacion.md`.
* **La equivalencia entre valores literales** («a las dies de la noche» frente a «a las diez de la noche»). Se resuelve con una normalización de capa 4, todavía no implementada (`docs/C_modelo.md` §8).
* **La cobertura completa del expediente.** Están anotadas 66 menciones y 74 afirmaciones (hilo central más las ampliaciones de la revisión 1), no todo el expediente. Por eso PC03, PC04 y PC15 constan como **PENDIENTES**.
