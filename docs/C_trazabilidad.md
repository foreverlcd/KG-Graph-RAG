# C · Trazabilidad: pregunta → capa → términos → consulta → prueba

> Es el patrón «pregunta de competencia como prueba de aceptación». Se adoptó a mano a partir de la búsqueda de
> skills (ver `docs/bitacora.md`). Cada PC se traza hasta:
> * los términos que la hacen posible;
> * la consulta con nombre que la responde;
> * la prueba que la fija.
>
> Si un término desapareciera del modelo, la prueba de la PC correspondiente fallaría.

| PC | Capas | Términos imprescindibles | Consulta(s) | Prueba(s) | Estado |
|---|---|---|---|---|---|
| PC01 | 1, 4 | `rico:Record`, `rico:directlyPrecedesInSequence`, `rico:expressedDate`, `act:*`; `P82a` en R-fechas | `piezas`, `control_secuencia` | `test_pc01_orden_y_secuencia` | Respondida |
| PC02 | 1, 3 | `atr:folio-de-pieza`, `P140` → pieza | `afirmaciones` | `test_pc02_autorreferencias_de_foliacion` | Respondida (folio en imagen: L1) |
| PC03 | 1, 3 (catálogo) | E13 cuyo afirmante es el equipo catalogador; `rico:Record` de la ficha | `afirmaciones` | — | PENDIENTE de anotación |
| PC04 | 1, 3 (serie) | Ídem, a escala de serie | `afirmaciones` | — | PENDIENTE de anotación |
| PC05 | 2, 4 | `picom:PersonObservation`, `crm:P1/E41/P190`, `oa:TextQuoteSelector`, `picom:PersonReconstruction`, `prov:wasDerivedFrom` | `menciones_de` | `test_pc05_grafias_sin_fusionar_en_capa_2` | Respondida |
| PC06 | 4 | `crminf:I2_Belief`, `J5_holds_to_be` (posible o indeterminado) | `reconstrucciones` | (cubierta por `test_pc19`) | Respondida |
| PC07 | 2, 4 | `roar:LocationObservation`, `roar:Observation` + `ent:ayllu`, `roar:LocationReconstruction`, `crm:P48/E42` (HGIS), `rdfs:seeAlso` (WHG) | `reconstrucciones`, `identificadores_externos` | `test_pc07_lugares_con_hgis` | Respondida |
| PC08 | 3, 4 | E13, `P9i` → E65 (`act:certificacion` frente a `act:declaracion-jurada`), PC14 del afirmante, reconstrucción del afirmante | `afirmaciones` (`filtroAfirmante`) | `test_pc08_mismo_testigo_agosto_y_septiembre` | Respondida |
| PC09 | 3, 4 | E13, `atr:ejerce-cargo`, `cargo:coronel-rebelde`, `pol:afirma` / `pol:niega`, `anot:sujeto-eliptico`, `P17` (`responde_a`) | `afirmaciones`, `disputas` | `test_pc09_cano_afirma_y_niega_coronel`, `test_disputas_detecta_negaciones_explicitas` | DISPUTA |
| PC10 | 2, 3 | `atr:redacto`, `atr:firmo`, PC14 `rol:firmante` (capa 2) | `afirmaciones`, `disputas`, `disputas_firma` | `test_pc10_redaccion_disputada_y_firma_negada` | DISPUTA |
| PC11 | 3, 4 | `atr:duracion`, E89 (hecho narrado), E5 (evento reconstruido) | `afirmaciones`, `disputas` | `test_pc11_dos_duraciones` | DISPUTA |
| PC12 | 1, 3 | `fza:resolutiva` / `fza:dictaminadora`, `atr:tiene-condicion`, `act:desglose` | `afirmaciones`, `piezas` | `test_pc12_y_pc13_no_lo_dice_pero_muestra_evidencia` | NC |
| PC13 | 3 | `atr:ordena` (una orden no implica su ejecución) | `afirmaciones` | ídem | NC |
| PC14 | 3, 4 | `atr:fecha-del-hecho`, `atr:numero-de-participantes`, E52 con valor literal, `responde_a` | `afirmaciones`, `disputas` | `test_pc14_al_menos_cinco_horas` | DISPUTA |
| PC15 | 1, 2, 3 | PC14 con `rol:receptor`, `rol:fedatario`, `rol:firmante`, `rol:redactor` en todas las actuaciones | `afirmaciones`, `piezas` | — | PENDIENTE de anotación |
| PC16 | 3 | `fza:*`, `atr:veracidad`, `atr:se-conforma-con`, ausencia de `J5` en E13 (SHACL) | `afirmaciones` | `test_pc16_resolucion_es_afirmacion_no_hecho`, `test_formas_negativas::afirmacion-valor-de-verdad` | Respondida |
| PC17 | 3, 4 | `atr:tiene-condicion` (`dct:conformsTo tes:condiciones`), `atr:filiacion`, `atr:ejerce-cargo` | `afirmaciones` | `test_pc17_condiciones_atribuidas_por_quien` | Respondida |
| PC18 | 3, 4 | `atr:ejerce-cargo`; `crm:E7_Activity` + PC14 (cargo como `P14.1`) + E52 (P82a/P82b) | `afirmaciones`, `cargos` | `test_pc18_cargos_con_vigencia` | Respondida |
| PC19 | 2, 4 | Dos `picom:PersonReconstruction` en competencia; `I2` con J5 distinto | `reconstrucciones` | `test_pc19_reconstrucciones_en_competencia` | Respondida |
| PC20 | P | `prov:wasGeneratedBy`, `prov:used` (sha256), `prov:qualifiedAssociation/hadPlan`, `prov:SoftwareAgent` | `procedencia` | `test_pc20_procedencia_declara_falta_de_validacion_humana` | Respondida |

## Términos del tesauro sin uso todavía

De los 164 conceptos del tesauro, 70 no aparecen aún en el grafo del hilo central (medido el 2026-11-12; 94 en uso): cargos de la Audiencia, condiciones como «forastero» o «reservado», tipos de entidad. Es **esperable**, porque solo está anotado el hilo central.

Antes de la extracción completa, la prueba `test_terminos_existen` debería ampliarse con un informe de cobertura. Ese informe serviría para retirar los conceptos que no use ningún expediente del Tomo I y para añadir los que pidan las nuevas extracciones. Cada concepto añadido se cuenta en el criterio 5 (`docs/G_evaluacion.md`).
