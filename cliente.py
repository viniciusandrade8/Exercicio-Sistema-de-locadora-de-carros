from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    cpf: str

    def __str__(self):
        return f"Nome: {self.nome} | CPF: {self.cpf}"
