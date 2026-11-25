"""Genera el visor del grafo: un único HTML autónomo (visor/index.html) con los datos incrustados.

    python scripts/visor.py            # lee el grafo construido y escribe visor/index.html desde visor/plantilla.html

El visor, al estilo de Neo4j Browser, muestra quién afirma qué sobre quién como nodos con etiqueta y relaciones con
tipo:
* nodos: reconstrucciones de la capa 4 (Persona, Lugar, Grupo, Cosa, Hecho, Cargo), piezas del expediente (Pieza),
  menciones que no pertenecen a una sola reconstrucción (Mención) y hechos narrados sin reconstrucción (HechoNarrado);
* relaciones:
  - AFIRMA / NIEGA: afirmante → sujeto, una por (afirmante, sujeto, atributo, polaridad), con sus afirmaciones;
  - TIENE_VALOR: sujeto → valor, cuando el valor de una afirmación es otra entidad (rotulada con el atributo);
  - HIPOTESIS_DE: mención ambigua → cada reconstrucción que la reclama (lecturas rivales);
  - INTERVIENE_EN: afirmante → pieza en la que afirma, con su papel procesal.

Regla de identidad, la misma del harness: una mención se dibuja como su reconstrucción solo si pertenece a UNA; si
pertenece a varias (hipótesis rivales) queda como nodo propio unido a cada una. Nada se fusiona en silencio.
Las disputas se calculan con laad.responder.grupos_en_disputa (no se almacenan).
"""
import json
import pathlib
import sys
import time

RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from laad.consulta import consultar  # noqa: E402
from laad.responder import grupos_en_disputa  # noqa: E402

PLANTILLA = RAIZ / "visor" / "plantilla.html"
SALIDA = RAIZ / "visor" / "index.html"
MARCA = "/*DATOS_DEL_GRAFO*/null"

ETIQUETA_CLASE = {"persona": "Persona", "lugar": "Lugar", "grupo": "Grupo", "cosa": "Cosa", "evento": "Hecho",
                  "ejercicio-cargo": "Cargo"}


def _s(x):
    return None if x is None or str(x) == "None" else str(x)


def _cola(iri: str) -> str:
    return iri.rsplit("/", 1)[-1]


def datos() -> dict:
    R = consultar("indice_reconstrucciones")
    M = consultar("indice_menciones")
    A = consultar("afirmaciones")
    P = consultar("piezas")

    nodos: dict[str, dict] = {}
    rels: dict[tuple, dict] = {}
    por_label, hecho_a_r = {}, {}

    for r in R:
        nodos[r["rid"]] = {"id": r["rid"], "etiqueta": ETIQUETA_CLASE.get(r["clase"], r["clase"]), "nombre": r["label"],
                           "creencia": r["creencia"], "menciones": [], "afirmaciones": []}
        por_label[r["label"]] = r["rid"]
        for ref in (_s(r["derivaDe"]) or "").split():
            if "/hecho/" in ref:
                hecho_a_r.setdefault(_cola(ref), []).append(r["rid"])
    for p in P:
        nodos[p["pieza"]] = {"id": p["pieza"], "etiqueta": "Pieza", "nombre": f"{p['pieza']} · {p['tipo']}",
                             "tipoActo": p["tipo"], "titulo": p["titulo"], "fecha": _s(p["fecha"]),
                             "ajena": str(p["ajena"]) == "true", "afirmaciones": []}

    mencion = {m["mid"]: m for m in M}
    for m in M:
        for rid in (_s(m["reconstrucciones"]) or "").split():
            if rid in nodos:
                nodos[rid]["menciones"].append({"mid": m["mid"], "texto": m["texto"], "pieza": m["pieza"],
                                                "tramo": m["tramo"], "cita": m["cita"]})

    def rel(de, a, tipo, rotulo="", **extra):
        k = (de, a, tipo, rotulo)
        return rels.setdefault(k, {"source": de, "target": a, "tipo": tipo, "rotulo": rotulo, "afirmaciones": [],
                                   **extra})

    def nodo_de(iri, etiqueta):
        """Nodo que representa un sujeto o un valor: su reconstrucción si es única; si no, un nodo propio."""
        if not iri or not iri.startswith("http"):
            return None
        cola = _cola(iri)
        if "/pieza/" in iri:
            return cola if cola in nodos else None
        if "/mencion/" in iri:
            m = mencion.get(cola)
            rids = (_s(m["reconstrucciones"]) or "").split() if m else []
            if len(rids) == 1:
                return rids[0]
            nid = "M:" + cola
            if nid not in nodos:
                nodos[nid] = {"id": nid, "etiqueta": "Mención", "nombre": f"«{(m or {}).get('texto') or etiqueta}»",
                              "mid": cola, "pieza": (m or {}).get("pieza"), "tramo": (m or {}).get("tramo"),
                              "cita": (m or {}).get("cita"), "rivales": rids, "afirmaciones": []}
                for rid in rids:
                    rel(nid, rid, "HIPOTESIS_DE")
            return nid
        if "/hecho/" in iri:
            rids = hecho_a_r.get(cola, [])
            if len(rids) == 1:
                return rids[0]
            nid = "H:" + cola
            if nid not in nodos:
                nodos[nid] = {"id": nid, "etiqueta": "HechoNarrado", "nombre": etiqueta or cola, "hid": cola,
                              "rivales": rids, "afirmaciones": []}
                for rid in rids:
                    rel(nid, rid, "HIPOTESIS_DE")
            return nid
        return None

    def afirmante_de(a) -> str:
        etiquetas = [x.strip() for x in (_s(a["afirmanteR"]) or "").split(" | ") if x.strip()]
        rids = [por_label[x] for x in etiquetas if x in por_label]
        if len(rids) == 1:
            return rids[0]
        nid = "AF:" + a["afirmante"] + ":" + "+".join(sorted(rids))
        if nid not in nodos:
            nodos[nid] = {"id": nid, "etiqueta": "Mención", "nombre": f"«{a['afirmante']}»", "pieza": a["pieza"],
                          "rivales": rids, "afirmaciones": []}
            for rid in rids:
                rel(nid, rid, "HIPOTESIS_DE")
        return nid

    vistos, filas = set(), []
    for a in A:
        if a["aid"] in vistos:                      # una fila por afirmación
            continue
        vistos.add(a["aid"])
        suj = nodo_de(_s(a["sujeto"]), _s(a["sujetoLabel"]))
        val = nodo_de(_s(a["valor"]), _s(a["valorLabel"]))
        filas.append({**a, "sujeto": suj or _s(a["sujeto"]), "_valorNodo": val, "_valorTexto": _s(a["valorLabel"]),
                      "valorLabel": val if val and not val.startswith(("M:", "H:")) else a["valorLabel"]})
    en_disputa = {f["aid"] for _, g in grupos_en_disputa(filas) for f in g}

    afirmaciones = {}
    for f in filas:
        aid, atr = f["aid"], _cola(str(f["atributo"]))
        de = afirmante_de(f)
        suj = f["sujeto"] if f["sujeto"] in nodos else None
        niega = f["pol"] != "afirma"
        afirmaciones[aid] = {
            "aid": aid, "afirmante": f["afirmante"], "rol": _s(f["rolAf"]), "pieza": f["pieza"],
            "tipoAct": _s(f["tipoAct"]), "fecha": _s(f["fecha"]), "sujeto": _s(f["sujetoLabel"]), "sujetoNodo": suj,
            "atributo": f["atrLabel"], "atr": atr, "valor": f["_valorTexto"], "valorNodo": f["_valorNodo"],
            "niega": niega, "fuerza": _s(f["fuerza"]), "fundamento": _s(f["fundamento"]), "cita": f["cita"],
            "tramo": _s(f["tramo"]), "folio": _s(f["folio"]), "eliptico": str(f["eliptico"]) == "true",
            "respondeA": _cola(f["respondeA"]) if _s(f["respondeA"]) else None, "segun": _s(f["segun"]),
            "disputa": aid in en_disputa, "afirmanteNodo": de}
        for n in {de, suj, f["_valorNodo"], f["pieza"]} - {None}:
            if n in nodos:
                nodos[n]["afirmaciones"].append(aid)
        if f["pieza"] in nodos:
            rel(de, f["pieza"], "INTERVIENE_EN", _s(f["rolAf"]) or "")["afirmaciones"].append(aid)
        if suj:
            rel(de, suj, "NIEGA" if niega else "AFIRMA", atr)["afirmaciones"].append(aid)
            if f["_valorNodo"] and f["_valorNodo"] != suj:
                rel(suj, f["_valorNodo"], "TIENE_VALOR", atr)["afirmaciones"].append(aid)

    relaciones = []
    for i, r in enumerate(rels.values()):
        ids = r["afirmaciones"]
        r["id"] = i
        r["n"] = len(ids)
        r["disputa"] = any(afirmaciones[x]["disputa"] for x in ids)
        relaciones.append(r)
    grado = {}
    for r in relaciones:
        if r["tipo"] != "INTERVIENE_EN":
            grado[r["source"]] = grado.get(r["source"], 0) + max(r["n"], 1)
            grado[r["target"]] = grado.get(r["target"], 0) + max(r["n"], 1)
    for n in nodos.values():
        n["grado"] = grado.get(n["id"], 0)

    return {"generado": time.strftime("%Y-%m-%d"),
            "fuente": "datos/grafo/*.nq · consultas indice_reconstrucciones, indice_menciones, afirmaciones, piezas",
            "nodos": list(nodos.values()), "relaciones": relaciones, "afirmaciones": afirmaciones,
            "nDisputa": len(en_disputa)}


# ── ontología: tripletas reales por capa, tesauro y formas SHACL ──────────────────────────────────────────────

PREFIJOS = [  # del más largo al más corto, para que gane el prefijo más específico
    ("https://w3id.org/laad/tesauro/actuacion/", "act:"), ("https://w3id.org/laad/tesauro/anotacion/", "anot:"),
    ("https://w3id.org/laad/tesauro/atributo/", "atr:"), ("https://w3id.org/laad/tesauro/cargo/", "cargo:"),
    ("https://w3id.org/laad/tesauro/condicion/", "cond:"), ("https://w3id.org/laad/tesauro/documento/", "doc:"),
    ("https://w3id.org/laad/tesauro/entidad/", "ent:"), ("https://w3id.org/laad/tesauro/fundamento/", "fun:"),
    ("https://w3id.org/laad/tesauro/fuerza/", "fza:"), ("https://w3id.org/laad/tesauro/polaridad/", "pol:"),
    ("https://w3id.org/laad/tesauro/rol/", "rol:"), ("https://w3id.org/laad/tesauro/creencia/", "cre:"),
    ("https://w3id.org/laad/tesauro/", "tes:"), ("https://w3id.org/laad/grafo/", "g:"),
    ("https://w3id.org/laad/id/", "id:"), ("http://www.cidoc-crm.org/extensions/crminf/", "crminf:"),
    ("http://www.cidoc-crm.org/cidoc-crm/", "crm:"), ("https://www.ica.org/standards/RiC/ontology#", "rico:"),
    ("http://www.w3.org/ns/oa#", "oa:"), ("http://www.w3.org/ns/prov#", "prov:"), ("http://purl.org/dc/terms/", "dct:"),
    ("http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdf:"), ("http://www.w3.org/2000/01/rdf-schema#", "rdfs:"),
    ("http://www.w3.org/2001/XMLSchema#", "xsd:"), ("http://www.w3.org/2004/02/skos/core#", "skos:"),
    ("https://personsincontext.org/model#", "picom:"), ("https://w3id.org/roar#", "roar:"),
    ("http://www.w3.org/2002/07/owl#", "owl:"),
]


def _c(t) -> str:
    """Término RDF compacto: prefijo:local para IRIs, "texto" para literales."""
    from rdflib import Literal
    if isinstance(t, Literal):
        s = str(t)
        return '"' + (s if len(s) <= 400 else s[:399] + "…") + '"' + (f"@{t.language}" if t.language else "")
    s = str(t)
    for largo, corto in PREFIJOS:
        if s.startswith(largo):
            return corto + s[len(largo):]
    return "<" + s + ">"


def _quads():
    from rdflib import Dataset
    ds = Dataset()
    for f in sorted((RAIZ / "datos" / "grafo").glob("*.nq")):
        ds.parse(f, format="nquads")
    return [(s, p, o, g) for s, p, o, g in ds.quads((None, None, None, None)) if g is not None]


def rdf_por_recurso(quads) -> dict:
    """Tripletas reales agrupadas por recurso, con el grafo nombrado (la capa) en que viven: afirmación (E13 +
    participación PC14 + anotación), mención (+ su anotación), actuación y pieza, reconstrucción (sus dos grafos) y,
    en «_procedencia», el PROV-O del lote anotado. Formato compacto: {grafos: [...], r: {clave: [[i_grafo, sujeto,
    [[predicado, objeto], …]], …]}}."""
    import re
    patron = re.compile(r"https://w3id\.org/laad/id/[^/]+/(afirmacion|anotacion|mencion|actuacion|pieza)/([^/]+)")
    prov = ("cc-14-18/afirmaciones/anotacion-manual", "cc-14-18/texto/anotacion-manual",
            "actividad/cc-14-18/anotacion-manual", "agente/claude-opus", "transcripcion/bd945513f8e1")
    grafos, idx, crudo = [], {}, {}
    for s, p, o, g in quads:
        gs = str(g.identifier if hasattr(g, "identifier") else g)
        clave = None
        m = patron.match(str(s))
        if m:
            clave = m.group(2)
        elif "/grafo/reconstruccion/" in gs or "/grafo/argumentacion/" in gs:
            clave = gs.rsplit("/", 1)[-1]
        elif gs.endswith("/grafo/procedencia") and any(x in str(s) for x in prov):
            clave = "_procedencia"
        if not clave:
            continue
        gc = _c(g.identifier if hasattr(g, "identifier") else g)
        if gc not in idx:
            idx[gc] = len(grafos); grafos.append(gc)
        crudo.setdefault(clave, {}).setdefault((idx[gc], _c(s)), []).append([_c(p), _c(o)])
    r = {}
    for clave, por_suj in crudo.items():
        filas = []
        for (gi, suj), po in sorted(por_suj.items(), key=lambda x: (x[0][0], x[0][1])):
            po.sort(key=lambda x: (x[0] != "rdf:type", x[0], x[1]))
            filas.append([gi, suj, po])
        r[clave] = filas
    return {"grafos": grafos, "r": r}


def tesauro(quads) -> list:
    from rdflib import Graph, Namespace, RDF, URIRef
    from rdflib.namespace import OWL, SKOS
    t = Graph()
    for f in ("tesauro.ttl", "candidatos.ttl", "alineaciones.ttl"):
        t.parse(RAIZ / "ontologia" / f, format="turtle")
    TES = Namespace("https://w3id.org/laad/tesauro/")
    candidatos = set(t.objects(TES.candidatos, SKOS.member))
    usos: dict = {}
    for _, _, o, _ in quads:
        if isinstance(o, URIRef) and str(o).startswith(str(TES)):
            usos[o] = usos.get(o, 0) + 1
    es = lambda x: next((str(v) for v in t.objects(x[0], x[1]) if getattr(v, "language", None) in ("es", None)), None)
    esquemas = []
    for sch in sorted(t.subjects(RDF.type, SKOS.ConceptScheme), key=str):
        if sch == TES.candidatos:
            continue
        conceptos = []
        for c in sorted(set(t.subjects(SKOS.inScheme, sch)) | set(t.subjects(SKOS.topConceptOf, sch)), key=str):
            nota = es((c, SKOS.editorialNote)) or ""
            conceptos.append({
                "id": _c(c), "etiqueta": es((c, SKOS.prefLabel)) or _c(c),
                "definicion": es((c, SKOS.definition)), "alcance": es((c, SKOS.scopeNote)) or es((c, SKOS.historyNote)),
                "ocultas": sorted(str(v) for v in t.objects(c, SKOS.hiddenLabel)),
                "fuente": nota.replace("Fuente de la definición: ", "") if nota.startswith("Fuente") else None,
                "trabajo": nota.startswith("Definición de trabajo"),
                "candidato": c in candidatos, "retirado": (c, OWL.deprecated, None) in t,
                "padre": _c(next(iter(t.objects(c, SKOS.broader)))) if (c, SKOS.broader, None) in t else None,
                "relacionado": sorted(_c(v) for v in t.objects(c, SKOS.related)),
                "alineaciones": sorted(str(v) for p in (SKOS.closeMatch, SKOS.relatedMatch) for v in t.objects(c, p)),
                "usos": usos.get(c, 0)})
        esquemas.append({"id": _c(sch), "etiqueta": es((sch, SKOS.prefLabel)) or _c(sch), "conceptos": conceptos})
    return esquemas


def formas() -> list:
    from rdflib import Graph, RDF, RDFS, Namespace
    SH = Namespace("http://www.w3.org/ns/shacl#")
    g = Graph()
    g.parse(RAIZ / "ontologia" / "formas.ttl", format="turtle")
    out = []
    for f in sorted(g.subjects(RDF.type, SH.NodeShape), key=str):
        objetivo = next(iter(g.objects(f, SH.targetClass)), None)
        out.append({"id": _c(f).replace("<https://w3id.org/laad/ohac#", "ohac:").rstrip(">"),
                    "objetivo": _c(objetivo) if objetivo is not None else None,
                    "explica": str(next(iter(g.objects(f, RDFS.comment)), "")) or None,
                    "severidad": "aviso" if str(next(iter(g.objects(f, SH.severity)), "")).endswith("Warning") else "error"})
    return out


# ── Ejemplo en tres niveles: ontología (el molde), grafo (los datos) y tesauro (el vocabulario) ──
# Una sola afirmación (Cano niega que Chuquitapa fuera coronel) con todo lo que toca. Cada arista se comprueba contra el
# grafo (datos/grafo/*.nq) o contra el tesauro (ontologia/tesauro.ttl): si no existe, el visor no se genera.
EJ_NODOS = [
    # nivel, id compacto, x, y, título, subtítulo, clave para «ver en RDF» o para el tesauro
    ("onto", "crm:E65_Creation", 130, 95, "Actuación procesal", "crm:E65_Creation", None),
    ("onto", "picom:PersonObservation", 420, 95, "Mención de persona", "picom:PersonObservation", None),
    ("onto", "crm:E13_Attribute_Assignment", 720, 95, "Afirmación", "crm:E13_Attribute_Assignment", None),
    ("onto", "picom:PersonReconstruction", 980, 95, "Persona reconstruida", "picom:PersonReconstruction", None),
    ("onto", "skos:Concept", 1205, 95, "Concepto", "skos:Concept", None),
    ("datos", "id:cc-14-18/actuacion/P18", 130, 340, "Actuación P18", "id:…/actuacion/P18", "P18"),
    ("datos", "id:cc-14-18/mencion/M-UT11-001", 400, 340, "«Ysidro Cano»", "id:…/mencion/M-UT11-001", "M-UT11-001"),
    ("datos", "id:cc-14-18/afirmacion/A-UT11-004", 720, 340, "Afirmación A-UT11-004", "id:…/afirmacion/A-UT11-004", "A-UT11-004"),
    ("datos", "id:cc-14-18/mencion/M-UT01-004", 1040, 395, "«Chuquitapa»", "id:…/mencion/M-UT01-004", "M-UT01-004"),
    ("datos", "id:persona/chuquitapa", 1040, 245, "Andrés Chuquitapa", "id:persona/chuquitapa", "R-chuquitapa"),
    ("tes", "act:declaracion-jurada", 130, 560, "declaración jurada", "act:declaracion-jurada", "act:declaracion-jurada"),
    ("tes", "fza:testimonial", 480, 560, "testimonial", "fza:testimonial", "fza:testimonial"),
    ("tes", "rol:declarante", 330, 640, "declarante", "rol:declarante", "rol:declarante"),
    ("tes", "pol:niega", 660, 640, "niega", "pol:niega", "pol:niega"),
    ("tes", "atr:ejerce-cargo", 800, 560, "ejerce o ejerció un cargo", "atr:ejerce-cargo", "atr:ejerce-cargo"),
    ("tes", "cargo:coronel-rebelde", 1080, 640, "coronel (de Túpac Amaru)", "cargo:coronel-rebelde", "cargo:coronel-rebelde"),
    ("tes", "cargo:cargo-rebelde-1780", 1205, 560, "cargo en las fuerzas de 1780", "cargo:cargo-rebelde-1780", "cargo:cargo-rebelde-1780"),
]
EJ_ARISTAS = [
    # sujeto, predicado, objeto, rótulo corto, curvatura, posición del rótulo (0 = sujeto, 1 = objeto)
    ("id:cc-14-18/afirmacion/A-UT11-004", "crm:P14_carried_out_by", "id:cc-14-18/mencion/M-UT11-001", "P14 · quién", 0, .5),
    ("id:cc-14-18/afirmacion/A-UT11-004", "crm:P140_assigned_attribute_to", "id:cc-14-18/mencion/M-UT01-004", "P140 · sobre quién", 0, .5),
    ("id:cc-14-18/afirmacion/A-UT11-004", "crm:P9i_forms_part_of", "id:cc-14-18/actuacion/P18", "P9i · en qué actuación", -110, .8),
    ("id:persona/chuquitapa", "prov:wasDerivedFrom", "id:cc-14-18/mencion/M-UT01-004", "reúne esta mención", 0, .5),
    ("id:cc-14-18/actuacion/P18", "rdf:type", "crm:E65_Creation", "es un", 0, .5),
    ("id:cc-14-18/mencion/M-UT11-001", "rdf:type", "picom:PersonObservation", "es un", 0, .5),
    ("id:cc-14-18/mencion/M-UT01-004", "rdf:type", "picom:PersonObservation", "es un", 0, .3),
    ("id:cc-14-18/afirmacion/A-UT11-004", "rdf:type", "crm:E13_Attribute_Assignment", "es un", 0, .5),
    ("id:persona/chuquitapa", "rdf:type", "picom:PersonReconstruction", "es un", 0, .5),
    ("id:cc-14-18/actuacion/P18", "crm:P2_has_type", "act:declaracion-jurada", "P2 · tipo de acto", 0, .5),
    ("id:cc-14-18/mencion/M-UT11-001", "picom:hasRole", "rol:declarante", "rol", 0, .5),
    ("id:cc-14-18/afirmacion/A-UT11-004", "crm:P2_has_type", "fza:testimonial", "P2 · fuerza", 0, .5),
    ("id:cc-14-18/afirmacion/A-UT11-004", "crm:P2_has_type", "pol:niega", "P2 · polaridad", 0, .5),
    ("id:cc-14-18/afirmacion/A-UT11-004", "crm:P177_assigned_property_of_type", "atr:ejerce-cargo", "P177 · qué afirma", 0, .5),
    ("id:cc-14-18/afirmacion/A-UT11-004", "crm:P141_assigned", "cargo:coronel-rebelde", "P141 · el valor", 0, .5),
    ("act:declaracion-jurada", "skos:related", "fza:testimonial", "da la fuerza", 0, .5),
    ("cargo:coronel-rebelde", "skos:broader", "cargo:cargo-rebelde-1780", "dentro de", 0, .5),
]


def ejemplo(quads) -> dict:
    from rdflib import Graph
    tes = Graph()
    tes.parse(RAIZ / "ontologia" / "tesauro.ttl", format="turtle")
    en_datos = {}
    for s, p, o, g in quads:
        en_datos.setdefault((_c(s), _c(p), _c(o)), _c(g))
    en_tes = {(_c(s), _c(p), _c(o)) for s, p, o in tes}
    ids = {n[1] for n in EJ_NODOS}
    aristas = []
    for s, p, o, rot, curva, pos in EJ_ARISTAS:
        assert s in ids and o in ids, (s, o)
        if (s, p, o) in en_datos:
            fuente = en_datos[(s, p, o)]
        elif (s, p, o) in en_tes:
            fuente = "ontologia/tesauro.ttl"
        else:
            raise SystemExit(f"El ejemplo dibuja una arista que no está en el grafo ni en el tesauro: {s} {p} {o}")
        aristas.append({"s": s, "p": p, "o": o, "rotulo": rot, "curva": curva, "pos": pos, "fuente": fuente})
    # todos los conceptos dibujados son skos:Concept (una sola flecha agregada en el dibujo)
    for n in EJ_NODOS:
        if n[0] == "tes" and (n[1], "rdf:type", "skos:Concept") not in en_tes:
            raise SystemExit(f"{n[1]} no es un skos:Concept del tesauro")
    return {"nodos": [dict(zip(("nivel", "id", "x", "y", "titulo", "sub", "clave"), n)) for n in EJ_NODOS], "aristas": aristas}


def main() -> int:
    d = datos()
    quads = _quads()
    d["rdf"] = rdf_por_recurso(quads)
    d["tesauro"] = tesauro(quads)
    d["formas"] = formas()
    d["ejemplo"] = ejemplo(quads)
    d["cifras"] = json.loads((RAIZ / "datos" / "cifras.json").read_text(encoding="utf-8"))
    plantilla = PLANTILLA.read_text(encoding="utf-8")
    if plantilla.count(MARCA) != 1:
        raise SystemExit(f"{PLANTILLA.name} debe contener una sola vez la marca {MARCA}")
    # «</» se escapa para que ninguna cita pueda cerrar la etiqueta <script> que contiene los datos
    js = json.dumps(d, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    SALIDA.write_text(plantilla.replace(MARCA, js), encoding="utf-8")
    tipos, etiquetas = {}, {}
    for r in d["relaciones"]:
        tipos[r["tipo"]] = tipos.get(r["tipo"], 0) + 1
    for n in d["nodos"]:
        etiquetas[n["etiqueta"]] = etiquetas.get(n["etiqueta"], 0) + 1
    print(f"{len(d['nodos'])} nodos {etiquetas}\n{len(d['relaciones'])} relaciones {tipos}\n"
          f"{len(d['afirmaciones'])} afirmaciones ({d['nDisputa']} en disputa) → {SALIDA.relative_to(RAIZ)} "
          f"({SALIDA.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
