import pytest
from Atividade.models.funcionario import Funcionario
from Atividade.models.endereco import Endereco


@pytest.fixture
def funcionario_valido():
    funcionario1 = Funcionario("Rafael", "07198998787", "Rafael123@...",  1500, Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador") )
    return funcionario1

def test_nome_valido(funcionario_valido):
    assert funcionario_valido.nome == "Rafael"

def test_telefone_valido(funcionario_valido):
    assert funcionario_valido.telefone == "07198998787"

def test_email_valido(funcionario_valido):
    assert funcionario_valido.email == "Rafael123@..."

def test_salario_valido(funcionario_valido):
    assert funcionario_valido.salario == 1500

def test_nome_vazio():
    with pytest.raises(TypeError, match = "O nome não pode ficar vazio!"):
        Funcionario(" ", "07198998787", "Rafael123@...",  1500, Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador") )
def test_nome_tipo_invalido():
    with pytest.raises(TypeError, match = "O nome deve ser um texto!"):
        Funcionario(12232, "07198998787", "Rafael123@...",  1500, Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador") )

def test_telefone_vazio():
    with pytest.raises(TypeError, match = "O telefone não pode ficar vazio!"):
        Funcionario("Rafael", " ", "Rafael123@...",  1500, Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador") )

def test_telefone_tipo_invalido():
    with pytest.raises(TypeError, match = "O telefone deve ser um texto!"):
        Funcionario("Rafael", 12312, "Rafael123@...",  1500, Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador") )
    
def test_email_vazio():  
    with pytest.raises(TypeError, match = "O email não pode ficar vazio!"):
        Funcionario("Rafael", "07198998787", " ",  1500, Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador") )
def test_email_tipo_invalido():  
    with pytest.raises(TypeError, match = "O email deve ser um texto!"):
        Funcionario("Rafael", "07198998787", 123231,  1500, Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador") )

def test_salario_vazio():
    with pytest.raises(TypeError, match = "O salário não pode ficar vazio!"):
        Funcionario("Rafael", "07198998787", "Rafael123@...",  None, Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador") )
def test_salario_tipo_invalido():
    with pytest.raises(TypeError, match = "O salário deve ser composto por números!"):
        Funcionario("Rafael", "07198998787", "Rafael123@...",  "1500", Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador") )
def test_salario_negativo():
    with pytest.raises(ValueError, match = "O salário não pode ser negativo!"):
        Funcionario("Rafael", "07198998787", "Rafael123@...",  -1500, Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador") )