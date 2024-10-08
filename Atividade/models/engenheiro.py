from Atividade.models.funcionario import Funcionario
from Atividade.models.endereco import Endereco

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crea = self._verificar_crea(crea)

    def _verificar_crea(self,valor):
        self._verificar_crea_tipo_invalido(valor)
        self._verificar_crea_vazio(valor)

        self.crea = valor
        return self.crea
    
    def _verificar_crea_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O CREA não pode ficar vazio!")

    def _verificar_crea_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O CREA deve ser um texto!")

    def __str__(self) -> str:
        return (f"CREA: {self.crea}\n"
               f"{super().__str__()}"
        )