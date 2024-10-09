import pytest
from Atividade.models.medico import Medico
from Atividade.models.endereco import Endereco

@pytest.fixture
def medico_valido():
    medico1 = Medico("Icaro", "07112398787", "Icaro123@...",  3500, Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador"), "999")
    return medico1

def test_crm_valido(medico_valido):
    assert medico_valido.crm == "999"

def test_crm_vazio():
    with pytest.raises(TypeError, match = "O CRM não pode ficar vazio!"):
        Medico("Rafael", "07112398787", "Icaro123@...",  3500, Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador"), " ")

def test_crm_tipo_invalido():
    with pytest.raises(TypeError, match = "O CRM deve ser um texto!"):
        Medico("Rafael", "07112398787", "Icaro123@...",  3500, Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador"), 999)