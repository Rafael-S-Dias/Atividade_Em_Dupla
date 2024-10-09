from abc import ABC
from Atividade.models.endereco import Endereco

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verificar_email(email) 
        self.salario = self._verificar_salario(salario)
        self.endereco = endereco

    def _verificar_nome(self, valor):
        self._verificar_nome_tipo_invalido(valor)
        self._verificar_nome_vazio(valor)

        self.nome = valor
        return self.nome
    
    def _verificar_telefone(self, valor):
        self._verificar_telefone_tipo_invalido(valor)
        self._verificar_telefone_vazio(valor)

        self.telefone = valor
        return self.telefone

    def _verificar_email(self, valor):
        self._verificar_email_tipo_invalido(valor)
        self._verificar_email_vazio(valor)

        self.email = valor
        return self.email
    
    def _verificar_salario(self, valor):
        self._verificar_salario_vazio(valor)
        
        self._verificar_salario_tipo_invalido(valor)
        self._verificar_salario_negativo(valor)

        self.salario = valor
        return self.salario

    def _verificar_nome_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O nome não pode ficar vazio!")
             
    def _verificar_nome_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto!")
         
    def _verificar_telefone_vazio(self, valor):
         if not valor.strip():
            raise TypeError("O telefone não pode ficar vazio!")
        
    def _verificar_telefone_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O telefone deve ser um texto!")
        
    def _verificar_email_vazio(self, valor):
         if not valor.strip():
            raise TypeError("O email não pode ficar vazio!")
        
    def _verificar_email_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O email deve ser um texto!")
        
    def _verificar_salario_vazio(self, valor):
        if valor is None:
            raise TypeError("O salário não pode ficar vazio!")   

    def _verificar_salario_tipo_invalido(self, valor):
         if not isinstance(valor, (int, float)):
            raise TypeError("O salário deve ser composto por números!")
        
    def _verificar_salario_negativo(self, valor):
        if valor < 0:
            raise ValueError("O salário não pode ser negativo!")

    def __str__(self) -> str:
        return ( f"Nome: {self.nome}\n"
                 f"Telefone: {self.telefone}\n"
                 f"Email: {self.email}\n"
                 f"Salario: {self.salario}\n"
                 f"=== Endereço === {self.endereco}"
        )