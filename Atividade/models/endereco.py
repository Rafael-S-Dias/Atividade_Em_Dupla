
class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = self._verificar_logradouro(logradouro)
        self.numero = self._verificar_numero(numero)
        self.complemento = self._verificar_complemento(complemento)
        self.cep = self._verificar_cep(cep)
        self.cidade = self._verificar_cidade(cidade)


    def _verificar_logradouro(self, valor):
        self._verificar_logradouro_tipo_invalido(valor)
        self._verificar_logradouro_vazio(valor)

        self.logradouro = valor
        return self.logradouro
    
    def _verificar_numero(self, valor):
        self._verificar_numero_tipo_invalido(valor)
        self._verificar_numero_vazio(valor)
        
        self.numero = valor
        return self.numero
    
    def _verificar_complemento(self, valor):
        self._verificar_complemento_tipo_invalido(valor)
        self._verificar_complemento_vazio(valor)

        self.complemento = valor
        return self.complemento
    
    def _verificar_cep(self, valor):
        self._verificar_cep_tipo_invalido(valor)
        self._verificar_cep_vazio(valor)

        self.cep = valor
        return self.cep
    
    def _verificar_cidade(self, valor):
        self._verificar_cidade_tipo_invalido(valor)
        self._verificar_cidade_vazio(valor)

        self.cidade = valor
        return self.cidade
    
    
    def _verificar_logradouro_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O logradouro não pode ficar vazio!")
        
    def _verificar_logradouro_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O logradouro deve ser um texto!")

    def _verificar_numero_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O número não pode ficar vazio!")
        
    def _verificar_numero_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O número deve ser um texto!")

    def _verificar_complemento_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O complemento não pode ficar vazio!")

    def _verificar_complemento_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O complemento deve ser um texto!")

    def _verificar_cep_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O CEP não pode ficar vazio!")

    def _verificar_cep_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O CEP deve ser um texto!")
        
    def _verificar_cidade_vazio(self, valor):
        if not valor.strip():
            raise TypeError("A cidade não pode ficar vazio!")

    def _verificar_cidade_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("A cidade deve ser um texto!")

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}\n"
                f"Numero: {self.numero}\n"
                f"Complemento: {self.complemento}\n"
                f"CEP: {self.cep}\n"
                f"Cidade: {self.cidade}\n"
        )