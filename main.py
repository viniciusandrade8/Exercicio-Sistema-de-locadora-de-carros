from carro import Carro
from cliente import Cliente
from locadora import Locadora


# instâncias com listas vazias
locadora = Locadora(lista_de_carros=[], lista_de_clientes=[])

# adicionando alguns carros
locadora.adicionar_carro("Polo", 2024, "XVT-2045")
locadora.adicionar_carro("HB-20", 2025, "TZD-4955")
locadora.adicionar_carro("City", 2023, "GHN-0946")

# alugando um dos carros manualmente
locadora.lista_de_carros[1].alugar() #Aluga o HB-20

# testando o método que lista os carros disponíveis
print("Carros dispníveis para aluguel:")
locadora.listar_carros_disponiveis()

locadora.lista_de_carros[1].devolver()
print("Carros disponíveis para aluguel:")
locadora.listar_carros_disponiveis()
