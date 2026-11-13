"""Las 20 preguntas de competencia (docs/B_preguntas_competencia.md) como funciones sobre el grafo.

Cada función devuelve una Respuesta compuesta SOLO con filas de consultas con nombre (consultas/*.rq).
Las PC que requieren anotación aún no hecha devuelven forma "PENDIENTE" con el motivo: nunca se improvisa.
"""
from __future__ import annotations

from .consulta import ID, TES, atributo, consultar, evento, persona
from .responder import Respuesta, _quien, _unicas, disputa, forma_de, pronunciamientos, reconstrucciones_de

PIEZA = ID + "cc-14-18/pieza/"


def _afirm(**kw) -> list[dict]:
    return _unicas(consultar("afirmaciones", **kw))


def pc01() -> Respuesta:
    filas = consultar("piezas")
    lineas = [f"  {f['pieza']} [{f['tipo']}] {f['titulo']} — fecha escrita: «{f['fecha']}»" if f["fecha"]
              else f"  {f['pieza']} [{f['tipo']}] {f['titulo']} — sin fecha escrita" for f in filas]
    sec = consultar("control_secuencia")
    lineas += ["", "Control de secuencia (fechas normalizadas en capa 4 frente al orden físico):"]
    lineas += [f"  {s['p1']} ({s['f1']}) antes que {s['p2']} ({s['f2']}): {s['motivo']}" if s["p2"]
               else f"  {s['p1']} ({s['f1']}): {s['motivo']}" for s in sec]
    return Respuesta("¿Qué piezas forman el expediente, en qué orden, de qué tipo y con qué fecha?", "D",
                     f"{len(filas)} piezas en orden físico de la transcripción; {len(sec)} incoherencias de fecha señaladas.",
                     extra=lineas)


def pc05() -> Respuesta:
    filas = consultar("menciones_de", filtroEntidad=persona("huancachoque"))
    lineas = [f"  «{f['texto']}» — {f['tramo']}, pieza {f['pieza']} ({f['tipoAct']}), mención {f['mid']}" for f in filas]
    grafias = sorted({f["texto"] for f in filas})
    return Respuesta("¿Con qué grafías aparece el denunciante y dónde?", "D",
                     f"{len(grafias)} grafías en {len(filas)} menciones anotadas: " + ", ".join(grafias)
                     + ". (Agrupadas por la reconstrucción R-huancachoque; ver capa 4.)",
                     reconstrucciones=reconstrucciones_de(persona("huancachoque")), extra=lineas)


def pc06() -> Respuesta:
    dudosas = [r for r in consultar("reconstrucciones") if r["creencia"] in ("posible", "indeterminado", "improbable")]
    return Respuesta("¿Qué menciones no se pueden identificar con seguridad y por qué?", "R",
                     f"{len(dudosas)} reconstrucciones de identidad con creencia posible o indeterminada.",
                     reconstrucciones=dudosas)


def pc08(slug: str = "cano") -> Respuesta:
    filas = sorted(_afirm(filtroAfirmante=persona(slug)), key=lambda f: (f["pieza"], f["aid"]))
    tipos = sorted({f["tipoAct"] for f in filas})
    return Respuesta(f"¿Qué afirmó {slug} en su certificación de agosto y qué en su declaración de septiembre?", "A",
                     f"{len(filas)} afirmaciones en {', '.join(tipos)}.", filas,
                     reconstrucciones_de(persona(slug)))


def pc09() -> Respuesta:
    ent = persona("chuquitapa")
    res, filas = disputa(ent, "ejerce-cargo", "coronel (de Túpac Amaru)")
    extra = ["Afirmaciones relacionadas (no forman la disputa):"]
    for f in _afirm(filtroEntidad=ent, atributo=atributo("ejerce-cargo")):
        if f["valorLabel"] != "coronel (de Túpac Amaru)":
            extra.append(f"  {f['aid']}: {_quien(f)} → {f['valorLabel']} ({f['pol']}) «{f['cita']}»")
    extra.append(pronunciamientos(filas))
    return Respuesta("¿Fue Andrés Chuquitapa coronel de Túpac Amaru en la rebelión?", forma_de(filas), res, filas,
                     reconstrucciones_de(ent), extra)


def pc10() -> Respuesta:
    filas = _afirm(atributo=atributo("redacto"))
    firmas = consultar("disputas_firma")
    extra = [f"Disputa texto/afirmación: la pieza {f['pieza']} muestra la firma «{f['firmaEscrita']}» "
             f"({f['mencionFirma']}), y {f['negacion']} («{f['afirmante']}») lo niega: «{f['cita']}»" for f in firmas]
    piezas = sorted({f["sujetoLabel"] for f in filas})
    # disputa calculada: alguna pieza con dos redactores distintos atribuidos, o una firma negada
    por_pieza: dict[str, set[str]] = {}
    for f in filas:
        por_pieza.setdefault(f["sujetoLabel"], set()).add(f["valorLabel"])
    forma = "DISPUTA" if firmas or any(len(v) > 1 for v in por_pieza.values()) else forma_de(filas)
    detalle = "; ".join(f"{p}: " + ", ".join(sorted(v)) for p, v in sorted(por_pieza.items()))
    return Respuesta("¿Quién redactó las certificaciones de agosto?", forma,
                     f"{len(piezas)} piezas con redactor atribuido ({detalle}); {len(firmas)} firmas negadas.",
                     filas, extra=extra)


def pc11() -> Respuesta:
    ent = evento("prision")
    res, filas = disputa(ent, "duracion")
    return Respuesta("¿Cuánto tiempo estuvo preso Huancachoque?", forma_de(filas), res, filas, reconstrucciones_de(ent))


def _resolutivas() -> list[dict]:
    return [f for f in _afirm() if f["fuerza"] in ("resolutiva", "dictaminadora")]


def pc12() -> Respuesta:
    """NC estructural: ¿hay alguna afirmación dictaminadora o resolutiva que atribuya o retire una condición
    fiscal (originario, forastero, tributario, reservado) al denunciante, o que ordene algo sobre la matrícula? (Sin heurísticas sobre el texto del valor.)"""
    ent = persona("huancachoque")
    # Solo las condiciones que deciden la matrícula (originario, forastero, tributario, reservado); «indio» a secas
    # no se pronuncia sobre ella.
    fiscales = {f"https://w3id.org/laad/tesauro/condicion/{c}" for c in ("originario", "forastero", "tributario", "reservado")}
    condicion = [f for f in _afirm(filtroEntidad=ent, atributo=atributo("tiene-condicion"))
                 if f["fuerza"] in ("resolutiva", "dictaminadora") and f["valor"] in fiscales
                 and f["fundamento"] != "resulta de lo actuado"]  # resumir lo actuado (la queja) no es pronunciarse
    ordenes = [f for f in _afirm(atributo=atributo("ordena"))
               if f["fuerza"] in ("resolutiva", "dictaminadora") and "matr" in f["valorLabel"].lower()]
    pertinentes = condicion + ordenes
    desglose = [p for p in consultar("piezas") if p["tipo"] == "desglose y agregación"]
    extra = [f"Pieza {p['pieza']}: {p['titulo']} — fecha escrita «{p['fecha']}»" for p in desglose]
    extra.append("Advertencia: «no lo dice» vale en la medida en que la extracción de afirmaciones resolutivas sea "
                 "exhaustiva (exhaustividad medida contra el estándar de oro, docs/G_evaluacion.md).")
    if pertinentes:
        return Respuesta("¿Se sacó finalmente a Huancachoque de la matrícula de tributarios?", "A",
                         "Hay afirmaciones dictaminadoras o resolutivas sobre su condición o la matrícula.", pertinentes,
                         extra=extra)
    return Respuesta("¿Se sacó finalmente a Huancachoque de la matrícula de tributarios?", "NC",
                     "El expediente no lo dice: ninguna afirmación dictaminadora o resolutiva se pronuncia sobre su "
                     "condición tributaria ni sobre la matrícula; la petición se desglosó al expediente de la primera "
                     "denuncia (P14–P15).", extra=extra)


def pc13() -> Respuesta:
    """NC calculado: una orden no implica su cumplimiento (tes:atributo/ordena). Su ejecución constaría como una
    afirmación que responde a la orden (P17 + anot:responde-a); si no hay ninguna, el expediente no lo dice."""
    ordenes = [f for f in _afirm(atributo=atributo("ordena")) if f["fuerza"] == "resolutiva"]
    ids = {f["aid"] for f in ordenes}
    cumplimiento = [f for f in _afirm() if f.get("respondeA") in ids]
    pregunta = "¿Qué castigo concreto se ejecutó contra Huancachoque tras el auto del 26 de noviembre?"
    if cumplimiento:
        return Respuesta(pregunta, "A", "Hay afirmaciones que responden a la orden resolutiva.", ordenes + cumplimiento)
    return Respuesta(pregunta, "NC", f"El expediente no lo dice: constan {len(ordenes)} órdenes resolutivas "
                     "y ninguna afirmación que responda a ellas (ejecución o cumplimiento).", ordenes)


def pc14() -> Respuesta:
    ent = evento("alboroto-carcel")
    res, filas = disputa(ent, "fecha-del-hecho")
    _, num = disputa(ent, "numero-de-participantes")
    return Respuesta("¿A qué hora fue el alboroto ante la cárcel y cuántos indios participaron?", forma_de(filas),
                     res, filas + num, reconstrucciones_de(ent))


def pc16() -> Respuesta:
    filas = _resolutivas()
    return Respuesta("¿Qué resolvió la autoridad sobre la queja y en qué se apoyó?", "A",
                     "Son afirmaciones con fuerza dictaminadora o resolutiva, no hechos: el fiscal califica las quejas "
                     "de «menos conforme a la verdad» y el auto se conforma con la vista fiscal; ambas se apoyan en el "
                     "informe del subdelegado (parte en la prisión del denunciante).", filas)


def pc19() -> Respuesta:
    m = ID + "cc-14-18/mencion/M-UT12.a-005"
    recs = [r for r in consultar("reconstrucciones") if "M-UT12.a-005" in r["menciones"]]
    return Respuesta("¿Son la misma persona «Mariano Casorla» (declarante) y «Martin Cazorla» (certificante)?", "R",
                     f"Hay {len(recs)} reconstrucciones en competencia; ninguna se impone en el grafo: "
                     + "; ".join(f"«{r['label']}» ({r['creencia']})" for r in recs) + ".", reconstrucciones=recs,
                     extra=[f"Mención afectada: {m}"])


def pc20(aid: str = "A-UT11-004") -> Respuesta:
    x = ID + f"cc-14-18/afirmacion/{aid}"
    filas = consultar("procedencia", x=x)
    lineas = [f"  grafo {f['grafo']} ({f['capa'].rsplit('/', 1)[1]}): actividad {f['actividad']}, agente {f['agente']} "
              f"({f['tipoAgente'].rsplit('#', 1)[1]}), plan «{f['plan']}», transcripción {f['sha']}, "
              f"fecha {f['fecha']}, validación humana: {f['validador'] or 'NO REGISTRADA'}" for f in filas]
    return Respuesta(f"¿De dónde procede el dato {aid}?", "P",
                     "Procedencia del dato (PROV-O), no del testimonio de 1806.", extra=lineas)


def pc02() -> Respuesta:
    filas = _afirm(atributo=atributo("folio-de-pieza"))
    return Respuesta("¿Qué pieza es la «certificación De folio 4» y dónde está?", "D",
                     "El expediente se refiere a sus propias fojas; esa foliación es una afirmación del documento, no "
                     "una marca del transcriptor. " + "; ".join(f"{f['sujetoLabel']} → «{f['valorLabel']}»" for f in filas)
                     + ". En la transcripción esas piezas no tienen marca de folio (folio no consta).", filas)


def pc07() -> Respuesta:
    recs = [r for r in consultar("reconstrucciones")
            if "/lugar/" in r["entidad"] or "/grupo/" in r["entidad"]]
    ext = consultar("identificadores_externos")
    lineas = [f"  {e['label']}: {e['identificador']} {e['url'] or ''}" for e in ext]
    sin = [r["label"] for r in recs if r["entidad"] not in {e["entidad"] for e in ext}]
    return Respuesta("¿Qué lugares y ayllus se mencionan y con qué identificador de HGIS?", "R",
                     f"{len(recs)} lugares o grupos reconstruidos; {len(ext)} con identificador HGIS. Sin entrada en "
                     f"HGIS: {', '.join(sin) or 'ninguno'}.", reconstrucciones=recs, extra=lineas)


def pc17() -> Respuesta:
    filas = _afirm(filtroEntidad=persona("huancachoque"), atributo=atributo("tiene-condicion"))
    filas += _afirm(filtroEntidad=persona("huancachoque"), atributo=atributo("ejerce-cargo"))
    filas += _afirm(filtroEntidad=persona("huancachoque"), atributo=atributo("filiacion"))
    return Respuesta("¿Qué condición fiscal y social se atribuye a Huancachoque y quién la atribuye?", "A",
                     f"{len(filas)} atribuciones, cada una de quien la hace (ninguna es un hecho).", filas,
                     reconstrucciones_de(persona("huancachoque")))


def pc18() -> Respuesta:
    filas = [f for f in _afirm(filtroEntidad=persona("chuquitapa"), atributo=atributo("ejerce-cargo"))
             if "Túpac Amaru" not in f["valorLabel"]]
    cargos = consultar("cargos", titular=persona("chuquitapa"))
    lineas = [f"  EJERCICIO DE CARGO (capa 4): {c['cargo']} — vigencia: {c['inicio'] or '¿?'} a {c['fin'] or '¿?'} "
              f"({c['vigenciaNota'] or 'sin nota'}); creencia: {c['creencia']}; premisas: {c['premisas']}" for c in cargos]
    return Respuesta("¿Qué cargos ejercía Andrés Chuquitapa, con qué vigencia y según quién?", "R",
                     f"{len(filas)} afirmaciones de cargo (capa 3) y {len(cargos)} ejercicios de cargo reconstruidos "
                     "(capa 4). Los cargos en la rebelión de 1780 están en PC09.", filas, extra=lineas)


def pc15() -> Respuesta:
    """Cadena de autoridades: por pieza, tipo de actuación, fecha y data escritas, y quién actuó con qué papel
    procesal (capa 2, PC14 + P14.1), con la identidad reconstruida cuando la hay (capa 4). La circulación se lee de
    la data escrita de cada pieza, sin inferir traslados que el texto no dice."""
    filas = consultar("participantes")
    piezas = {f["pieza"]: f for f in consultar("piezas")}
    por_pieza: dict[str, dict] = {}
    for f in filas:
        d = por_pieza.setdefault(f["pieza"], {"tipo": f["tipoAct"], "fecha": f["fecha"], "lugar": None, "roles": {}})
        d["lugar"] = d["lugar"] or f["lugar"]
        quien = f"«{f['texto']}»" + (f" [{f['persona']}]" if f["persona"] else "")
        d["roles"].setdefault(f["rol"], [])
        if quien not in d["roles"][f["rol"]]:
            d["roles"][f["rol"]].append(quien)
    lineas, circulacion = [], []
    for pz in sorted(piezas):
        d = por_pieza.get(pz)
        if not d:
            lineas.append(f"  {pz} [{piezas[pz]['tipo']}]: no consta ningún participante con papel en la pieza.")
            continue
        cab = f"  {pz} [{d['tipo']}] fecha escrita «{d['fecha'] or 'no consta'}»; data «{d['lugar'] or 'no consta'}»"
        lineas.append(cab)
        for rol in sorted(d["roles"]):
            lineas.append(f"      {rol}: " + "; ".join(d["roles"][rol]))
        if d["lugar"]:
            circulacion.append(f"{pz}: {d['lugar']}")
    sin_firma = [pz for pz in sorted(piezas) if not any(r.startswith("firmante") for r in por_pieza.get(pz, {}).get("roles", {}))]
    lineas += ["", "Circulación según la data escrita de las piezas (solo donde consta):", "  " + " → ".join(circulacion),
               "", "Piezas sin firmante anotado: " + (", ".join(sin_firma) or "ninguna")]
    return Respuesta("¿Qué autoridades actuaron, en qué actuación, en qué fecha, quién escribió y quién firmó cada una, "
                     "y en qué orden circuló el expediente?", "D",
                     f"{len(por_pieza)} de {len(piezas)} piezas con participantes anotados ({len(filas)} participaciones); "
                     f"{len(sin_firma)} piezas sin firmante anotado.", filas, extra=lineas)


AVISO_CATALOGO = ("Respuesta según el catálogo del ARC (afirmaciones de los catalogadores, no hechos del modelo), "
                  "extraída de la capa de texto del PDF sin cotejo de imágenes; la pertinencia la marcó el extractor "
                  "(nota con motivo y dudas).")


def _catalogo(pc: str) -> list[dict]:
    return [f for f in consultar("catalogo") if f["pc"] == pc]


def _linea_ficha(f: dict) -> str:
    texto = " ".join(f["texto"].split())
    return f"  {f['etiqueta']} ({f['paginas']}): «{texto}» — {f['motivo'] or 'entrada de índice'}"


def pc03() -> Respuesta:
    """Según el catálogo: otros expedientes que mencionan a Chuquitapa, a Guancachoque o el pueblo de Tinta."""
    filas = _catalogo("PC03")
    base = ID + "arc/expediente/cc-14-18"
    fichas = [f for f in filas if f["etiqueta"].startswith("Ficha") and f["expediente"] != base]
    personas = [f for f in fichas if any(n in f["texto"] for n in ("Chuquitapa", "Guancachoque"))]
    pueblo = [f for f in fichas if f["pueblo"] in (True, "true")]
    otras_tinta = [f for f in fichas if f not in pueblo and f not in personas]
    indices = [f for f in filas if not f["etiqueta"].startswith("Ficha")]
    extra = [AVISO_CATALOGO, "", "Índices del catálogo:"] + [_linea_ficha(f) for f in indices]
    extra += ["", "Fichas que nombran «pueblo de Tinta» (otros expedientes):"] + [_linea_ficha(f) for f in pueblo]
    extra += ["", f"Otras {len(otras_tinta)} fichas nombran Tinta como partido, provincia, doctrina o regimiento "
              "(no consta que se refieran al pueblo):"] + [f"  {f['etiqueta']}" for f in otras_tinta]
    return Respuesta("¿Qué otros expedientes del Tomo I mencionan a Andrés Chuquitapa, a Manuel Guancachoque o al "
                     "pueblo de Tinta, según el catálogo?", "A",
                     f"Según el catálogo, Chuquitapa y Guancachoque solo constan en CCc 14 (18) ({len(personas)} otras "
                     f"fichas los nombran); {len(pueblo)} otras fichas nombran el «pueblo de Tinta» y {len(otras_tinta)} "
                     "más nombran Tinta en otro sentido.", extra=extra)


def pc04() -> Respuesta:
    """Según la ficha: expedientes CC de 1805–1807 con un cacique, recaudador o alcalde de indios como demandado."""
    filas = [f for f in _catalogo("PC04") if f["etiqueta"].startswith("Ficha")]
    seguros = [f for f in filas if f["certeza"] == "seguro"]
    dudosos = [f for f in filas if f["certeza"] != "seguro"]
    extra = [AVISO_CATALOGO, "", "Seguros (la ficha nombra el cargo del demandado):"]
    extra += [_linea_ficha(f) for f in seguros]
    extra += ["", "Dudosos (la ficha no dice si el alcalde es de indios):"]
    extra += [_linea_ficha(f) + (f" [duda: {f['dudas']}]" if f["dudas"] else "") for f in dudosos]
    return Respuesta("En Causas Criminales, ¿qué expedientes de 1805–1807 tienen como demandado a un cacique, "
                     "recaudador o alcalde de indios, según la ficha?", "A",
                     f"Según el catálogo: {len(seguros)} seguros ("
                     + ", ".join(f["etiqueta"].replace("Ficha del catálogo ", "") for f in seguros)
                     + f") y {len(dudosos)} dudosos.", extra=extra)


def pendiente(pc: str, motivo: str) -> Respuesta:
    return Respuesta(pc, "PENDIENTE", motivo)


PREGUNTAS = {
    "PC01": pc01, "PC05": pc05, "PC06": pc06, "PC08": pc08, "PC09": pc09, "PC10": pc10, "PC11": pc11,
    "PC12": pc12, "PC13": pc13, "PC14": pc14, "PC16": pc16, "PC19": pc19, "PC20": pc20,
    "PC02": pc02, "PC07": pc07, "PC17": pc17, "PC18": pc18,
    "PC03": pc03,
    "PC04": pc04,
    "PC15": pc15,
}
