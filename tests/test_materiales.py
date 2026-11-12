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


CITAS_DOC_PC = [
    ("yndio originario del Pueblo de Tinta", "UT08"), ("recaudaderor", "UT05"),
    ("Recaudador de Tributos", "UT07"), ("Recaudador de Reales Tributos de dicho Pueblo", "UT09"),
    ("recaudador de tributos de los Ayllus Tinta y Ucho", "UT17"), ("su casique y alcalde mayor", "UT16.b"),
    ("casique del Ayllo Tinta", "UT00"), ("quatro o seis Yndios", "UT12.b"), ("una caterva de indios", "UT06"),
    ("un montón de indios", "UT02"), ("un montón de indios", "UT03"), ("menos conforme a la verdad", "UT19"),
    ("por la malicia con que aparece", "UT19"), ("de conformidad", "UT19"), ("a fin de contener los excesos", "UT19"),
    ("a falta de Escribano", "UT11"), ("San Pedro de Cacha", "UT02"), ("Ayllu nominado Uchu", "UT05"),
    ("No sabe escribir", "UT12.b"), ("Simon Arce", "UT12.b"), ("no le consta nada de esto", "UT12.b"),
    ("no le cons", "UT11"), ("Santiago Casorla", "UT11"), ("Desglocese de este Expediente", "UT10"),
    ("Se agrego las dos fojas", "UT10"), ("informen el mismo Subdelegado", "UT08"),
    ("quejas dadas por Manuel Guancoichoque", "UT19"), ("Noviembre 20 de 1806", "UT20"),
    ("Siquani Noviembre 8 de 1806", "UT18"), ("Sicuani Noviembre 8 de 1806", "UT17"),
    ("Sicuani Setiembre. 17 de 1806", "UT10"), ("Veinte y tres dias del mes de Septiembre", "UT11"),
    ("en veinti quatro dias del mes de setiembre", "UT13"), ("setiembre 24 de 1806", "UT15"),
    ("Cusco y Agosto 28 de 1806", "UT09"), ("Agosto 27 de 1806", "UT09"),
    ("agosto cinco de mil ochocientos seis", "UT02"), ("En el pueblo de Tinta, en primero de agosto de 1806", "UT01"),
    ("la mujer de Chiquitas", "UT15"), ("Juan Cazorla de quien aparece firmada la Certificación a folios 2", "UT17"),
    ("en la remuneración que he conseguido", "UT06"), ("hasta aquí no había tributado", "UT06"),
]


@pytest.mark.parametrize("cita,tramo", CITAS_DOC_PC)
def test_cita_de_respuestas_provisionales(cita, tramo):
    r = verificar_cita(cita, tramo)
    assert r.valida, r.motivo
