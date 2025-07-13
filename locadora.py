from dataclasses import dataclass

@dataclass
class Locadora:
    lista_de_carros: str
    lista_de_clientes: str

    def adicionar_carro(self, carro):
        pass

    def adicionar_cliente(self, cliente):
        pass

    def listar_carros_disponiveis(self):
        pass

    def alugar_carro(self, placa, cpf):
        pass

    def devolver_carro(self, placa):
        pass
