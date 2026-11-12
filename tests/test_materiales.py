"""Ancla las citas usadas en docs/01_materiales.md (contradicciones de los materiales) a su tramo."""
import pytest
from laad.fuente import verificar_cita

CITAS_DOC_MATERIALES = [
    # N1 variantes del denunciante
    ("Mancachoque", "UT00"), ("Guamanchoque", "UT02"), ("HUANCACHOQQUE", "UT06"),
    ("Guancoichoque", "UT19"), ("gancahoque", "UT14"), ("guarcachoque", "UT13"),
    ("guasscachoque", "UT14"), ("guancachay", "UT15"),
    # N2 variantes del cacique
    ("Chuquiitapa", "UT01"), ("Chukitapa", "UT02"), ("Choquitapa", "UT05"), ("Choquetapa", "UT09"),
    ("Chuquitape", "UT11"), ("chuquitaza", "UT14"), ("Chiquitas", "UT15"),
    # N3–N10
    ("teniente Alguacil, don Juan Quiñones", "UT02"), ("Juan Cazorla.", "UT02"),
    ("no hay tal hombre en el pueblo de Tinta", "UT17"),
    ("el Gobernador Señor Don Mariano Casorla", "UT12.a"), ("De folio 4 su firma Martin casorla", "UT12.a"),
    ("Pedro de la Mara", "UT10"), ("Pedro de la Mara", "UT11"), ("Pedro de la Mata", "UT11"),
    ("pedro de Mata", "UT15"), ("[María Rubrica]", "UT17"),
    ("Luis Gomez del Rio", "UT08"), ("Luis Gonsalo del Rio", "UT09"), ("Lucio Gonzalo del Rio y Vial", "UT20"),
    ("Doctor Don Antonio Valdes", "UT15"), ("Doctor Don Agustin Valdes", "UT18"),
    ("don Antonio Reparas", "UT01"), ("Don Juan Antonio Reparas", "UT03"), ("corregidor Don Andres", "UT11"),
    ("d juan antonio repuras", "UT14"), ("su segundo sargento", "UT11"), ("segundo en la compañia", "UT13"),
    ("Ruiz de Castilla", "UT09"), ("Don Francisco Muñoz y Señor Clemente", "UT18"),
    # H1–H7
    ("a las dies o a las once", "UT02"), ("a las diez de la noche", "UT03"), ("a las nueve de la noche", "UT06"),
    ("sino el primer puesto del gallo", "UT14"), ("dos días preso", "UT06"),
    ("puse en libertad al otro dia por la tarde", "UT18"), ("Simon Arce", "UT12.b"),
    ("Tupa Amaro fue complice y coronel", "UT01"),
    ("en tiempo de su pariente Tupaamaro fue coronel, comecionado", "UT03"),
    ("Comisionado por este y no coronel", "UT11"),
    ("fue en tiempo del rebelde tupa-amaru coronel y comisionado", "UT14"), ("era muchacho", "UT12.b"),
    ("hijo Espurio de Antolin Ortiz , Sanbo cerros", "UT16.a"), ("Chispa soplada por Guancachoque", "UT18"),
    ("Indio originario y vecino del pueblo de Tinta", "UT05"), ("Agustina Falcon India Ordinaria", "UT16.a"),
    ("soldado en mi compañía más de cinco años", "UT02"),
    # F1–F7
    ("CUSCO AGOSTO 22 DE 1806", "UT05"), ("Agosto 21 de 1806", "UT08"), ("trece días del mees de Agosto", "UT08"),
    ("en 27 de Agosto proximo pasado", "UT10"), ("año pasado de 1809", "UT10"),
    ("Noviembre 26 de 1806", "UT16.b"), ("mil ochocientos 10 años", "UT20"),
    # material ajeno
    ("El ciudadano Matias Ugarte", "UT20"), ("Instancia", "UT00"),
]


@pytest.mark.parametrize("cita,tramo", CITAS_DOC_MATERIALES)
def test_cita_del_documento_de_materiales(cita, tramo):
    r = verificar_cita(cita, tramo)
    assert r.valida, r.motivo
