from dataclasses import dataclass
from carro import Carro
from cliente import Cliente
from typing import List


@dataclass
class Locadora:
    lista_de_carros: list[Carro]
    lista_de_clientes: list[Cliente]

    def adicionar_carro(self, modelo, ano, placa):
        novo_carro = Carro(modelo=modelo, ano=ano, placa=placa)

        self.lista_de_carros.append(novo_carro)


    def adicionar_cliente(self, nome, cpf):
        novo_cliente = Cliente(nome=nome, cpf=cpf)

        self.lista_de_clientes.append(novo_cliente)

    def listar_carros_disponiveis(self):
        carros_disponiveis = [c for c in self.lista_de_carros if c.disponivel]

        if carros_disponiveis:
            for c in carros_disponiveis:
                print(f"Modelo: {c.modelo} | Ano: {c.ano} | Placa: {c.placa}")
        else:
            print("Todos os carros estão alugados.")


    def alugar_carro(self, placa, cpf):
        cliente_encontrado = any(cliente.cpf == cpf for cliente in self.lista_de_clientes)
        if not cliente_encontrado:
            print("Cliente não encontrado.")
            return

        for carro in self.lista_de_carros:
            if carro.placa == placa:
                if carro.disponivel:
                    carro.alugar()
                    print(f"O carro com a placa {placa} alugado com sucesso para o cliente {cpf}.")
                else:
                    print(f"O carro com a placa {placa} já está alugado.")
                return
            print("Carro não encontrado")


    def devolver_carro(self, placa):
        for carro in self.lista_de_carros:
            if carro.placa == placa:
                if not carro.disponivel:
                    carro.devolver()
                    print(f"O carro com a placa {placa} foi devolvido com sucesso.")
                else:
                    print(f"O carro com a placa {placa} já está disponivel.")
                return
            print("Carro não encontrado.")
