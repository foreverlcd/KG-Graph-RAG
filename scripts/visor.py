"""Genera los datos del visor del grafo (visor/datos.js) a partir del grafo construido.

    python scripts/visor.py            # escribe visor/datos.js; abrir visor/index.html en el navegador

El visor muestra una red de quién afirma qué sobre quién:
* nodos: reconstrucciones de la capa 4 (personas, lugares, grupos, cosas, hechos), piezas del expediente y menciones
  que no pertenecen a una sola reconstrucción (sueltas o con hipótesis rivales);
* aristas: «afirma sobre» (afirmante → sujeto, una por par, con todas sus afirmaciones), «valor» (sujeto → valor
  cuando el valor es una entidad) e «hipótesis» (mención ambigua → cada reconstrucción que la reclama).

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

SALIDA = RAIZ / "visor" / "datos.js"


def _s(x):
    return None if x is None or str(x) == "None" else str(x)


def _cola(iri: str) -> str:
    return iri.rsplit("/", 1)[-1]


def main() -> int:
    R = consultar("indice_reconstrucciones")
    M = consultar("indice_menciones")
    A = consultar("afirmaciones")
    P = consultar("piezas")

    nodos: dict[str, dict] = {}
    aristas: dict[tuple, dict] = {}

    por_label = {}
    hecho_a_r: dict[str, list[str]] = {}
    for r in R:
        nodos[r["rid"]] = {"id": r["rid"], "tipo": "reconstruccion", "clase": r["clase"], "label": r["label"],
                           "creencia": r["creencia"], "menciones": [], "afirmaciones": []}
        por_label[r["label"]] = r["rid"]
        for ref in (_s(r["derivaDe"]) or "").split():
            if "/hecho/" in ref:
                hecho_a_r.setdefault(_cola(ref), []).append(r["rid"])
    for p in P:
        nodos[p["pieza"]] = {"id": p["pieza"], "tipo": "pieza", "clase": "pieza",
                             "label": f"{p['pieza']} · {p['tipo']}", "titulo": p["titulo"], "fecha": _s(p["fecha"]),
                             "ajena": str(p["ajena"]) == "true", "afirmaciones": []}

    mencion = {m["mid"]: m for m in M}
    for m in M:
        for rid in (_s(m["reconstrucciones"]) or "").split():
            if rid in nodos:
                nodos[rid]["menciones"].append({"mid": m["mid"], "texto": m["texto"], "pieza": m["pieza"],
                                                "cita": m["cita"]})

    def arista(a, b, tipo, **extra):
        k = (a, b, tipo)
        e = aristas.setdefault(k, {"de": a, "a": b, "tipo": tipo, "afirmaciones": [], **extra})
        return e

    def nodo_de(iri: str | None, etiqueta: str | None) -> str | None:
        """Nodo que representa un sujeto o un valor: reconstrucción si es única, si no un nodo propio."""
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
                nodos[nid] = {"id": nid, "tipo": "mencion", "clase": (m or {}).get("clase") or "mención",
                              "label": f"«{(m or {}).get('texto') or etiqueta}»",
                              "pieza": (m or {}).get("pieza"), "cita": (m or {}).get("cita"),
                              "rivales": rids, "afirmaciones": []}
                for rid in rids:
                    arista(nid, rid, "hipotesis")
            return nid
        if "/hecho/" in iri:
            rids = hecho_a_r.get(cola, [])
            if len(rids) == 1:
                return rids[0]
            nid = "H:" + cola
            if nid not in nodos:
                nodos[nid] = {"id": nid, "tipo": "hecho", "clase": "hecho", "label": etiqueta or cola,
                              "rivales": rids, "afirmaciones": []}
                for rid in rids:
                    arista(nid, rid, "hipotesis")
            return nid
        return None

    def afirmante_de(a) -> str:
        etiquetas = [x.strip() for x in (_s(a["afirmanteR"]) or "").split(" | ") if x.strip()]
        rids = [por_label[x] for x in etiquetas if x in por_label]
        if len(rids) == 1:
            return rids[0]
        nid = "AF:" + a["afirmante"] + ":" + "+".join(sorted(rids))
        if nid not in nodos:
            nodos[nid] = {"id": nid, "tipo": "mencion", "clase": "persona", "label": f"«{a['afirmante']}»",
                          "pieza": a["pieza"], "rivales": rids, "afirmaciones": []}
            for rid in rids:
                arista(nid, rid, "hipotesis")
        return nid

    # disputas calculadas, con la identidad de la reconstrucción (como en el harness)
    filas = []
    for a in A:
        suj = nodo_de(_s(a["sujeto"]), _s(a["sujetoLabel"]))
        val = nodo_de(_s(a["valor"]), _s(a["valorLabel"]))
        filas.append({**a, "sujeto": suj or _s(a["sujeto"]), "_valorNodo": val,
                      "valorLabel": val if val and not val.startswith(("M:", "H:")) else a["valorLabel"]})
    en_disputa = {f["aid"] for _, g in grupos_en_disputa(filas) for f in g}

    afirmaciones = {}
    for f in filas:
        aid = f["aid"]
        de = afirmante_de(f)
        suj = f["sujeto"] if f["sujeto"] in nodos else None
        afirmaciones[aid] = {
            "aid": aid, "afirmante": f["afirmante"], "rol": _s(f["rolAf"]), "pieza": f["pieza"],
            "tipoAct": _s(f["tipoAct"]), "fecha": _s(f["fecha"]), "sujeto": _s(f["sujetoLabel"]), "sujetoNodo": suj,
            "atributo": f["atrLabel"], "valor": _s(f["valorLabel"]) if not f["_valorNodo"] else _s(next(
                (x["valorLabel"] for x in A if x["aid"] == aid), None)),
            "valorNodo": f["_valorNodo"], "niega": f["pol"] != "afirma", "fuerza": _s(f["fuerza"]),
            "fundamento": _s(f["fundamento"]), "cita": f["cita"], "tramo": _s(f["tramo"]), "folio": _s(f["folio"]),
            "respondeA": _cola(f["respondeA"]) if _s(f["respondeA"]) else None,
            "disputa": aid in en_disputa, "afirmanteNodo": de}
        for n in {de, suj, f["_valorNodo"], f["pieza"]} - {None}:
            if n in nodos:
                nodos[n]["afirmaciones"].append(aid)
        if suj:
            e = arista(de, suj, "afirma")
            e["afirmaciones"].append(aid)
            if suj and f["_valorNodo"] and f["_valorNodo"] != suj:
                arista(suj, f["_valorNodo"], "valor")["afirmaciones"].append(aid)

    for e in aristas.values():
        ids = e["afirmaciones"]
        e["n"] = len(ids)
        e["niega"] = any(afirmaciones[i]["niega"] for i in ids)
        e["disputa"] = any(afirmaciones[i]["disputa"] for i in ids)

    datos = {
        "generado": time.strftime("%Y-%m-%d"),
        "fuente": "datos/grafo/*.nq (consultas indice_reconstrucciones, indice_menciones, afirmaciones, piezas)",
        "nodos": list(nodos.values()),
        "aristas": list(aristas.values()),
        "afirmaciones": afirmaciones,
    }
    SALIDA.parent.mkdir(exist_ok=True)
    SALIDA.write_text("// Generado por scripts/visor.py. No editar a mano.\nwindow.GRAFO = "
                      + json.dumps(datos, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    tipos = {}
    for n in nodos.values():
        tipos[n["tipo"]] = tipos.get(n["tipo"], 0) + 1
    print(f"{len(nodos)} nodos {tipos}, {len(aristas)} aristas, {len(afirmaciones)} afirmaciones "
          f"({len(en_disputa)} en disputa) → {SALIDA.relative_to(RAIZ)} ({SALIDA.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
