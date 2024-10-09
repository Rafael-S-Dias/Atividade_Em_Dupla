import pytest
from Atividade.models.engenheiro import Engenheiro
from Atividade.models.endereco import Endereco

@pytest.fixture
def engenheiro_valido():
    engenheiro1 = Engenheiro("João", "07193338787", "João123@...",  2500, Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador"), "888")
    return engenheiro1

def test_crea_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "888"

def test_crea_vazio():
    with pytest.raises(TypeError, match = "O CREA não pode ficar vazio!"):
        Engenheiro("João", "07193338787", "João123@...",  2500, Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador")," ")

def test_crea_tipo_invalido():
    with pytest.raises(TypeError, match = "O CREA deve ser um texto!"):
        Engenheiro("Rafael", "07193338787", "João123@...",  2500, Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador"), 888)