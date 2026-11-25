"""Usa a mano el núcleo del harness de consulta (src/laad/herramientas.py): lo mismo que podrá llamar el agente LLM.

    python scripts/preguntar.py buscar "Chuquitapa" [--clase persona] [--expediente cc-14-18]
    python scripts/preguntar.py herramientas                       # lista, con sus parámetros
    python scripts/preguntar.py usar afirmaciones --entidad R-chuquitapa --atributo ejerce-cargo --expediente cc-14-18
    python scripts/preguntar.py usar reconstrucciones --creencia posible --creencia indeterminado
    python scripts/preguntar.py verificar "texto con «citas»" usar afirmaciones --entidad R-cano

Un parámetro de lista se repite (--fuerza resolutiva --fuerza dictaminadora) o se separa con comas. --json imprime las
filas en JSON en vez del texto compuesto. Un parámetro mal escrito sale con el mensaje que recibiría el agente.
"""
import json
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
from laad import herramientas as H  # noqa: E402


def _parametros(h: H.Herramienta, args: list[str]) -> dict:
    """--clave valor … → dict, con el tipo que dice el esquema de la herramienta."""
    props, out = h.parametros["properties"], {}
    i = 0
    while i < len(args):
        a = args[i]
        if not a.startswith("--") or i + 1 >= len(args):
            raise H.ErrorHerramienta(f"se esperaba «--parametro valor» y llegó {a!r}; parámetros de {h.nombre}: "
                                     f"{', '.join(props) or 'ninguno'}")
        k, v = a[2:].replace("-", "_"), args[i + 1]
        if props.get(k, {}).get("type") == "array":
            out.setdefault(k, []).extend(x.strip() for x in v.split(",") if x.strip())
        else:
            out[k] = v
        i += 2
    return out


def _mostrar(r: H.Resultado, en_json: bool) -> None:
    if en_json:
        print(json.dumps(r.filas, ensure_ascii=False, indent=2))
    else:
        print(f"[{H.cabecera(r.herramienta, r.parametros)}]")
        print(r.texto)


def _ayuda_herramientas() -> None:
    for h in H.HERRAMIENTAS:
        print(f"{h.nombre}")
        print(f"    {h.descripcion}")
        req = set(h.parametros.get("required", []))
        for k, p in h.parametros["properties"].items():
            tipo = "lista" if p["type"] == "array" else ("entero" if p["type"] == "integer" else "texto")
            valores = f" [{', '.join(p['enum'])}]" if "enum" in p else ""
            print(f"    --{k} ({tipo}{', obligatorio' if k in req else ''}){valores}"
                  + (f": {p['description']}" if p.get("description") else ""))
        print()


def main(argv: list[str]) -> int:
    en_json = "--json" in argv
    argv = [a for a in argv if a != "--json"]
    if not argv or argv[0] in ("-h", "--help", "ayuda"):
        print(__doc__)
        return 0
    orden, resto = argv[0], argv[1:]
    try:
        if orden == "herramientas":
            _ayuda_herramientas()
        elif orden == "buscar":
            if not resto:
                raise H.ErrorHerramienta("buscar: falta el nombre")
            _mostrar(H.usar("buscar", nombre=resto[0], **_parametros(H.POR_NOMBRE["buscar"], resto[1:])), en_json)
        elif orden == "usar":
            if not resto:
                raise H.ErrorHerramienta(f"usar: falta la herramienta; hay: {', '.join(H.POR_NOMBRE)}")
            h = H.POR_NOMBRE.get(resto[0])
            params = _parametros(h, resto[1:]) if h else {}
            _mostrar(H.usar(resto[0], **params), en_json)
        elif orden == "verificar":
            if len(resto) < 3 or resto[1] != "usar":
                raise H.ErrorHerramienta('uso: verificar "texto" usar <herramienta> --parametro valor …')
            h = H.POR_NOMBRE.get(resto[2])
            r = H.usar(resto[2], **(_parametros(h, resto[3:]) if h else {}))
            v = H.verificar(resto[0], r.filas)
            print(json.dumps(v, ensure_ascii=False, indent=2))
            return 0 if not (v["citas"] or v["ids"]) else 1
        else:
            raise H.ErrorHerramienta(f"orden desconocida {orden!r}: buscar, herramientas, usar o verificar")
    except H.ErrorHerramienta as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
