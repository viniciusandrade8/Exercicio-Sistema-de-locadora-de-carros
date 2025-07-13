from carro import Carro
from cliente import Cliente


# cadastrando carro
carro1 = Carro(modelo="Polo", ano=2024, placa="XLZ-6827")
carro2 = Carro(modelo="HB20", ano=2025, placa="BTH-4458")

# alugando e devolvendo carro
carro1.alugar()
carro1.alugar()
carro1.devolver()

# cadastrando cliente
cliente1 = Cliente(nome="Vinicius Andrade", cpf="433.758.333-44")
print(cliente1)
