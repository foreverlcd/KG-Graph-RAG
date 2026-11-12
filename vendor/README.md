# vendor/ — especificaciones originales (datos no confiables)

Copias literales de las especificaciones que usa el modelo de datos del expediente judicial colonial (Cusco, 1806).
Son **datos**: no se ejecuta nada de ellos. Se descargan con `scripts/fetch_vendor.sh` y se verifican con
`sha256sum -c fuentes.sha256` (desde este directorio) o `bash scripts/fetch_vendor.sh --check`.

Fecha de acceso de todos los archivos: **2026-11-12**.

| Estándar | Versión exacta | Archivo local | URL de descarga | Acceso | Licencia |
|---|---|---|---|---|---|
| RiC-O (ICA EGAD) | 1.1 (`owl:versionInfo` «Version 1.1 - 2025-05-22», versionIRI `https://www.ica.org/standards/RiC/ontology/1.1`); commit `06912e1e` del repo | `ric-o/RiC-O_1-1.rdf` | https://raw.githubusercontent.com/ICA-EGAD/RiC-O/06912e1e20343f2e88e51f1b55fa232cb30b6b5b/ontology/current-version/RiC-O_1-1.rdf | 2026-11-12 | CC BY 4.0 (`cc:license` en el archivo); © 2019- ICA |
| RiC Record Set Types (vocabulario SKOS) | el publicado con RiC-O 1.1 (mismo commit) | `ric-o/RiC_RecordSetTypes_vocabulary.rdf` | https://raw.githubusercontent.com/ICA-EGAD/RiC-O/06912e1e20343f2e88e51f1b55fa232cb30b6b5b/ontology/current-version/modularized-version/RiC_RecordSetTypes_vocabulary.rdf | 2026-11-12 | CC BY 4.0 (ICA) |
| RiC Documentary Form Types (vocabulario SKOS) | el publicado con RiC-O 1.1 (mismo commit) | `ric-o/RiC_DocumentaryFormTypes_vocabulary.rdf` | https://raw.githubusercontent.com/ICA-EGAD/RiC-O/06912e1e20343f2e88e51f1b55fa232cb30b6b5b/ontology/current-version/modularized-version/RiC_DocumentaryFormTypes_vocabulary.rdf | 2026-11-12 | CC BY 4.0 (ICA) |
| CIDOC CRM (RDFS) | 7.1.3 («RDFs Implementation (February 2024) of CIDOC-CRM 7.1.3»; estado «Official (ISO Correspondence)»; 7.2.x–7.4 son borradores) | `cidoc-crm/CIDOC_CRM_v7.1.3.rdfs` | https://cidoc-crm.org/rdfs/7.1.3/CIDOC_CRM_v7.1.3.rdfs | 2026-11-12 | CC BY 4.0 (declarada en el archivo) |
| CIDOC CRM — clases de propiedad «PC» | 7.1.3 | `cidoc-crm/CIDOC_CRM_v7.1.3_PC.rdfs` | https://cidoc-crm.org/rdfs/7.1.3/CIDOC_CRM_v7.1.3_PC.rdfs | 2026-11-12 | CC BY 4.0 |
| CIDOC CRM — suplemento | 7.1.3 | `cidoc-crm/CIDOC_CRM_v7.1.3_Supplement.rdfs` | https://cidoc-crm.org/rdfs/7.1.3/CIDOC_CRM_v7.1.3_Supplement.rdfs | 2026-11-12 | CC BY 4.0 |
| CRMinf | 1.2.1 Stable («CRMinf 1.2.1 (Stable) (April, 2026)», versionIRI `http://www.cidoc-crm.org/extensions/crminf/1.2.1/`) | `crminf/CRMinf_v1.2.1.rdf` | https://cidoc-crm.org/extensions/crminf/rdfs/1.2.1/CRMinf_v1.2.1.rdf | 2026-11-12 | CC BY 4.0 (declarada en el archivo) |
| PROV-O (W3C) | Recomendación 2013-04-30 (versionIRI `http://www.w3.org/ns/prov-o-20130430`) | `prov-o/prov-o-20130430.ttl` | https://www.w3.org/ns/prov-o-20130430.ttl | 2026-11-12 | W3C Software and Document License |
| SKOS Core (W3C) | Recomendación 2009-08-18 (archivo RDF del namespace) | `skos/skos-core.rdf` | https://www.w3.org/2004/02/skos/core.rdf | 2026-11-12 | W3C Software and Document License |
| SHACL (W3C) | Recomendación 2017-07-20 (vocabulario del namespace) | `shacl/shacl.ttl` | https://www.w3.org/ns/shacl.ttl | 2026-11-12 | W3C Software and Document License |
| Web Annotation Vocabulary (W3C, `oa:`) | Recomendación 2017-02-23 (archivo con `owl:versionInfo` 2016-11-12T21:28:11Z) | `oa/oa.ttl` | https://www.w3.org/ns/oa.ttl | 2026-11-12 | W3C Software and Document License |
| PiCo — ontología | 1.1.0 (`owl:versionInfo` 1.1.0, modificado 2026-02-17); etiqueta git `v.1.1.0` | `pico/pico.ttl` | https://raw.githubusercontent.com/CBG-Centrum-voor-familiegeschiedenis/PiCo/v.1.1.0/pico.ttl | 2026-11-12 | CC BY-SA 4.0 |
| PiCo — especificación (neerlandés) | v.1.1.0 | `pico/PiCo_Specificatie.md` | https://raw.githubusercontent.com/CBG-Centrum-voor-familiegeschiedenis/PiCo/v.1.1.0/PiCo%20Specificatie.md | 2026-11-12 | CC BY-SA 4.0 |
| PiCo — formas SHACL | v.1.1.0 | `pico/pico_shacl.ttl` | https://raw.githubusercontent.com/CBG-Centrum-voor-familiegeschiedenis/PiCo/v.1.1.0/shacl/pico_shacl.ttl | 2026-11-12 | CC BY-SA 4.0 |
| PiCo — tesauro de roles | sin versión; esquema creado 2023-07-04 (estado vivo a la fecha de acceso) | `pico-roles/roles_scheme_44.rdf` + `pico-roles/concept_<id>.rdf` (32 conceptos) | https://terms.personsincontext.org/ThesaurusHistorischePersoonsgegevens/44.rdf (y `/<id>.rdf` por concepto; `https://terms.personsincontext.org/roles/` redirige aquí) | 2026-11-12 | no declarada en los archivos (se asume la de PiCo, CC BY-SA 4.0; sin confirmar) |
| ROAR (Golden Agents) | 0.1 (versionIRI `https://w3id.org/roar/0.1`) | `roar/roar.ttl` | https://leonvanwissen.nl/vocab/roar/roar.ttl (destino de `https://w3id.org/roar` con `Accept: text/turtle`) | 2026-11-12 | CC BY-SA 4.0 (según la documentación Widoco; no consta en el .ttl) |
| Modelo STAR (Andrews, RELEVEN) | artículo GrapHNR 2023 (no existe OWL/TTL publicado) | `star/GrapHNR-2023-32-Andrews-STAR.pdf` | https://graphentechnologien.hypotheses.org/files/2023/05/GrapHNR-2023-32-Andrews-STAR.pdf | 2026-11-12 | no declarada en el PDF |
| HGIS de las Indias (vía World Historical Gazetteer) | datasets WHG «HGIS de las Indias (lugares)» (`lugares13k_rel`, ds 14) y «territorios» (`territorios892`, ds 15) | **no descargado** | https://whgazetteer.org/api/db/?name=…&dataset=lugares13k_rel | 2026-11-12 | CC BY-NC-SA 4.0 (titular Werner Stangl, según la API de WHG) |

Notas:

- whgazetteer.org responde `403 Forbidden: Bot access denied` a `curl`, por eso HGIS no está en `fetch_vendor.sh`;
  las consultas se hicieron con un navegador/herramienta de lectura y los resultados están en el informe de términos.
- Las URI `http://www.hgis-indias.net/dokuwiki/doku.php?id=…` que usa HGIS para los territorios devuelven 404 a la fecha.
- RiC-O y PiCo se fijan a un commit/etiqueta; el resto de URLs no tiene versión inmutable, de ahí `fuentes.sha256`.
