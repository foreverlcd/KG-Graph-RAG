#!/usr/bin/env bash
# Descarga reproducible de las especificaciones originales usadas por el modelo de datos
# del expediente judicial colonial (Cusco, 1806).
# Fecha de referencia del acceso: 2026-11-12.
# Los archivos descargados son DATOS NO CONFIABLES: no se ejecuta nada de ellos.
# Uso: bash scripts/fetch_vendor.sh   (desde cualquier directorio)
#      bash scripts/fetch_vendor.sh --check   (solo verifica sumas sha256)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
V="$ROOT/vendor"

# Versiones fijadas (commit o etiqueta) para que la descarga sea reproducible.
RICO_COMMIT="06912e1e20343f2e88e51f1b55fa232cb30b6b5b"   # ICA-EGAD/RiC-O master, 2026-10-05 (RiC-O 1.1)
PICO_TAG="v.1.1.0"                                       # CBG PiCo release v.1.1.0 (2026-02-17)

fetch() { # fetch <url> <ruta relativa a vendor/>
  local url="$1" dest="$V/$2"
  mkdir -p "$(dirname "$dest")"
  echo "-> $2"
  curl -fsSL --retry 3 -o "$dest" "$url"
}

if [[ "${1:-}" != "--check" ]]; then
  # 1. RiC-O 1.1 (ICA EGAD)
  RICO="https://raw.githubusercontent.com/ICA-EGAD/RiC-O/$RICO_COMMIT/ontology/current-version"
  fetch "$RICO/RiC-O_1-1.rdf"                                              ric-o/RiC-O_1-1.rdf
  fetch "$RICO/modularized-version/RiC_RecordSetTypes_vocabulary.rdf"      ric-o/RiC_RecordSetTypes_vocabulary.rdf
  fetch "$RICO/modularized-version/RiC_DocumentaryFormTypes_vocabulary.rdf" ric-o/RiC_DocumentaryFormTypes_vocabulary.rdf

  # 2. CIDOC CRM 7.1.3 (versión oficial con RDFS) + archivo PC + suplemento
  CRM="https://cidoc-crm.org/rdfs/7.1.3"
  fetch "$CRM/CIDOC_CRM_v7.1.3.rdfs"            cidoc-crm/CIDOC_CRM_v7.1.3.rdfs
  fetch "$CRM/CIDOC_CRM_v7.1.3_PC.rdfs"         cidoc-crm/CIDOC_CRM_v7.1.3_PC.rdfs
  fetch "$CRM/CIDOC_CRM_v7.1.3_Supplement.rdfs" cidoc-crm/CIDOC_CRM_v7.1.3_Supplement.rdfs

  # 3. CRMinf 1.2.1 (stable)
  fetch "https://cidoc-crm.org/extensions/crminf/rdfs/1.2.1/CRMinf_v1.2.1.rdf" crminf/CRMinf_v1.2.1.rdf

  # 4-7. W3C
  fetch "https://www.w3.org/ns/prov-o-20130430.ttl"  prov-o/prov-o-20130430.ttl
  fetch "https://www.w3.org/2004/02/skos/core.rdf"   skos/skos-core.rdf
  fetch "https://www.w3.org/ns/shacl.ttl"            shacl/shacl.ttl
  fetch "https://www.w3.org/ns/oa.ttl"               oa/oa.ttl

  # 8. PiCo (CBG, Países Bajos)
  PICO="https://raw.githubusercontent.com/CBG-Centrum-voor-familiegeschiedenis/PiCo/$PICO_TAG"
  fetch "$PICO/pico.ttl"                pico/pico.ttl
  fetch "$PICO/PiCo%20Specificatie.md"  pico/PiCo_Specificatie.md
  fetch "$PICO/shacl/pico_shacl.ttl"    pico/pico_shacl.ttl

  # 9. ROAR (Golden Agents) — https://w3id.org/roar resuelve a leonvanwissen.nl
  fetch "https://leonvanwissen.nl/vocab/roar/roar.ttl" roar/roar.ttl

  # 10. Patrón STAR (Andrews 2023, proyecto ERC RELEVEN) — no existe archivo OWL; se guarda el artículo
  fetch "https://graphentechnologien.hypotheses.org/files/2023/05/GrapHNR-2023-32-Andrews-STAR.pdf" star/GrapHNR-2023-32-Andrews-STAR.pdf

  # 11. HGIS de las Indias: whgazetteer.org rechaza clientes automáticos (HTTP 403 "Bot access denied"),
  #     por lo que NO se descarga aquí; las consultas se documentan en vendor/README.md.
fi

[[ -f "$V/fuentes.sha256" ]] && (cd "$V" && sha256sum -c fuentes.sha256) || echo "sin fuentes.sha256 todavía"
