from locadora import Locadora


# Criação da instância da locadora
locadora = Locadora(lista_de_carros=[], lista_de_clientes=[])

def exibir_menu():
    print("\n===== LOCADORA DE CARROS =====")
    print("1. Cadastrar Carro")
    print("2. Cadastrar Cliente")
    print("3. Alugar Carro")
    print("4. Devolver Carro")
    print("5. Listar Carros Disponíveis")
    print("0. Sair")

def opcao_valida():
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao in [0, 1, 2, 3, 4, 5]:
                return opcao
            else:
                print("Opção inválida! Digite um número entre 0 e 5.")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

# loop principal do menu
while True:
    exibir_menu()
    opcao = opcao_valida()

    if opcao == 0:
        print("encerrando o programa.")
        break

    elif opcao == 1:
        modelo = input("Modelo do carro: ")
        ano = input("Ano do carro: ")
        placa = input("Placa do carro: ")
        locadora.adicionar_carro(modelo, ano, placa)
        print("Carro adicionado com sucesso!")
    
    elif opcao == 2:
        nome = input("Nome do cliente: ")
        cpf = input("CPF do cliente: ")
        locadora.adicionar_cliente(nome, cpf)

    elif opcao == 3:
        placa = input("Digite a placa do carro a ser alugado: ")
        cpf = input("Digite o CPF do cliente:")
        locadora.alugar_carro(placa, cpf)

    elif opcao == 4:
        placa = input("Digite a placa do carro a ser devolvido: ")
        locadora.devolver_carro(placa)

    elif opcao == 5:
        locadora.listar_carros_disponiveis()

