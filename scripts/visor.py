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


def main() -> int:
    d = datos()
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
