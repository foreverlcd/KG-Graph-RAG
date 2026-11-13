"""Pruebas del mapeo determinista registros → RDF (src/laad/mapeo.py)."""
from __future__ import annotations

import re
import subprocess
import sys

import pytest
from rdflib import RDF, RDFS, URIRef
from rdflib.compare import isomorphic

from laad import fuente
from laad import mapeo as M
from laad.registros import cargar

from ._fixtures import LOTES, PROCEDENCIA, RAIZ, REGISTROS, construir, dataset, union


def _grafos(ds):
    return {g.identifier: g for g in ds.graphs() if len(g)}


def test_determinismo():
    a, b = _grafos(dataset()), _grafos(construir())
    assert set(a) == set(b)
    distintos = [str(k) for k in a if not isomorphic(a[k], b[k])]
    assert not distintos, f"grafos no isomorfos entre dos construcciones: {distintos}"


def test_cada_afirmacion_tiene_un_afirmante():
    g = union()
    afirmaciones = list(g.subjects(RDF.type, M.CRM.E13_Attribute_Assignment))
    assert afirmaciones
    malas = {str(a): n for a in afirmaciones
             if (n := len(set(g.objects(a, M.CRM.P14_carried_out_by)))) != 1}
    assert not malas, malas


def test_id_duplicado_es_error(tmp_path):
    lineas = [l for l in REGISTROS.read_text(encoding="utf-8").splitlines() if l.strip()]
    ruta = tmp_path / "duplicado.jsonl"
    ruta.write_text("\n".join([lineas[0], lineas[0]]) + "\n", encoding="utf-8")
    lote = cargar([ruta])
    assert any("id duplicado" in e for e in lote.errores), lote.errores
    with pytest.raises(ValueError):
        M.construir(lote, PROCEDENCIA)


def test_verificar_citas_100():
    r = subprocess.run([sys.executable, str(RAIZ / "scripts/verificar_citas.py"), *map(str, LOTES)],
                       cwd=RAIZ, capture_output=True, text=True, timeout=120)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "100.0 %" in r.stdout, r.stdout


IRI_INVALIDA = re.compile(r'[\s\\<>"{}|^`]')


def test_iris_validas():
    ds = dataset()
    iris = {x for g in ds.graphs() for t in g for x in t if isinstance(x, URIRef)}
    iris |= {g.identifier for g in ds.graphs() if isinstance(g.identifier, URIRef)}
    malas = sorted(str(x) for x in iris if IRI_INVALIDA.search(str(x)))
    assert not malas, malas


CLASES_MENCION = (M.PICOM.PersonObservation, M.ROAR.Observation, M.ROAR.LocationObservation)


def test_selector_de_posicion_reproduce_la_cita():
    g = union()
    texto_tramo = {t.id: t.texto for t in fuente.tramos()}
    menciones = sorted({m for c in CLASES_MENCION for m in g.subjects(RDF.type, c)})
    assert menciones
    errores = []
    for m in menciones:
        anotaciones = list(g.subjects(M.OA.hasBody, m))
        if len(anotaciones) != 1:
            errores.append(f"{m}: {len(anotaciones)} anotaciones")
            continue
        tgt = g.value(anotaciones[0], M.OA.hasTarget)
        tramo = str(g.value(g.value(tgt, M.OA.hasSource), RDFS.label))
        sels = list(g.objects(tgt, M.OA.hasSelector))
        qs = [s for s in sels if (s, RDF.type, M.OA.TextQuoteSelector) in g]
        ps = [s for s in sels if (s, RDF.type, M.OA.TextPositionSelector) in g]
        if len(qs) != 1 or len(ps) != 1 or tramo not in texto_tramo:
            errores.append(f"{m}: selectores {len(qs)}/{len(ps)} o tramo {tramo!r} desconocido")
            continue
        ini, fin = int(g.value(ps[0], M.OA.start)), int(g.value(ps[0], M.OA.end))
        trozo = fuente.colapsar(texto_tramo[tramo][ini:fin])
        exacta = fuente.colapsar(str(g.value(qs[0], M.OA.exact)))
        if trozo != exacta:
            errores.append(f"{m}: [{ini}:{fin}] de {tramo} = {trozo!r} ≠ {exacta!r}")
    assert not errores, "\n".join(errores)


def test_selector_prefijo_exacto_sufijo_reconstruye_el_tramo():
    """prefix + exact + suffix es subcadena literal del tramo y coincide con la posición (Web Annotation §4.2.4)."""
    g = union()
    revisadas = 0
    for tgt in g.subjects(RDF.type, M.OA.SpecificResource):
        tramo_id = str(g.value(tgt, M.OA.hasSource)).rsplit("/", 1)[-1]
        texto = fuente.tramo(tramo_id).texto
        sels = list(g.objects(tgt, M.OA.hasSelector))
        qs = next(s for s in sels if (s, RDF.type, M.OA.TextQuoteSelector) in g)
        ps = next(s for s in sels if (s, RDF.type, M.OA.TextPositionSelector) in g)
        ini, fin = int(g.value(ps, M.OA.start)), int(g.value(ps, M.OA.end))
        pre, suf = str(g.value(qs, M.OA.prefix) or ""), str(g.value(qs, M.OA.suffix) or "")
        assert texto[ini - len(pre):ini] == pre and texto[fin:fin + len(suf)] == suf, tgt
        revisadas += 1
    assert revisadas >= 140
