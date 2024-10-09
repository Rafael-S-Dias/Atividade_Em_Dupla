import pytest
from Atividade.models.endereco import Endereco


@pytest.fixture
def endereco_valido():
    endereco1 = Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador")
    return endereco1

def test_logradouro_valido(endereco_valido):
    assert endereco_valido.logradouro == "Rua A"

def test_numero_valido(endereco_valido):
    assert endereco_valido.numero == "444"

def test_complemento_valido(endereco_valido):
    assert endereco_valido.complemento == "Qd 10 Lt 7"

def test_cep_valido(endereco_valido):
    assert endereco_valido.cep == "41....."

def test_cidade_valida(endereco_valido):
    assert endereco_valido.cidade == "Salvador"

def test_logradouro_vazio():
    with pytest.raises(TypeError, match = "O logradouro não pode ficar vazio!"):
       Endereco(" ", "444", "Qd 10 Lt 7", "41.....", "Salvador") 

def test_logradouro_tipo_invalido():
    with pytest.raises(TypeError, match = "O logradouro deve ser um texto!"):
       Endereco(111, "444", "Qd 10 Lt 7", "41.....", "Salvador") 

def test_numero_vazio():
    with pytest.raises(TypeError, match = "O número não pode ficar vazio!"):
        Endereco("Rua A", " ", "Qd 10 Lt 7", "41.....", "Salvador")

def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match = "O número deve ser um texto!"):
        Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador")

def test_complemento_vazio():
    with pytest.raises(TypeError, match = "O complemento não pode ficar vazio!"):
        Endereco("Rua A", "444", " ", "41.....", "Salvador")

def test_complemento_tipo_invalido():
    with pytest.raises(TypeError, match = "O complemento deve ser um texto!"):
        Endereco("Rua A", "444", 1, "41.....", "Salvador")

def test_cep_vazio():
    with pytest.raises(TypeError, match = "O CEP não pode ficar vazio!"):
        Endereco("Rua A", "444", "Qd 10 Lt 7", " ", "Salvador")

def test_cep_tipo_invalido():
    with pytest.raises(TypeError, match = "O CEP deve ser um texto!"):
        Endereco("Rua A", "444", "Qd 10 Lt 7", 10, "Salvador")

def test_cidade_vazio():
    with pytest.raises(TypeError, match = "A cidade não pode ficar vazio!"):
        Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", " ")

def test_cidade_tipo_invalido():
    with pytest.raises(TypeError, match = "A cidade deve ser um texto!"):
        Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", 10)