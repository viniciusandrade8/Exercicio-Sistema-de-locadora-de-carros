
# 🚗 Sistema de Locadora de Carros

Este é um projeto simples de um sistema de locadora de carros desenvolvido em Python, utilizando os princípios da **Programação Orientada a Objetos (POO)**.

O objetivo é gerenciar o cadastro de carros e clientes, realizar o aluguel e devolução de veículos, e exibir os carros disponíveis no momento. O sistema roda no terminal com um menu interativo.

---

## 📁 Estrutura do Projeto

- `carro.py`: contém a classe `Carro`, responsável por representar os veículos da locadora.
- `cliente.py`: (em desenvolvimento) será responsável por representar os clientes do sistema.
- `locadora.py`: (em desenvolvimento) gerenciará os carros, clientes e operações de aluguel e devolução.
- `main.py`: (em desenvolvimento) será o ponto de entrada do sistema, com um menu para o usuário interagir.

---

## 🧱 Classe Carro

A classe `Carro` possui os seguintes atributos e métodos:

### Atributos:
- `modelo` (str): modelo do carro
- `ano` (int): ano de fabricação
- `placa` (str): placa do carro
- `disponivel` (bool): status de disponibilidade (padrão: `True`)

### Métodos:
- `alugar()`: altera o status do carro para indisponível, se estiver disponível
- `devolver()`: altera o status para disponível, se estiver alugado
- `__str__()`: retorna uma descrição formatada do carro

---

## 🛠 Tecnologias Utilizadas

- Python 3.x
- `dataclasses` (módulo padrão do Python)

---

## 🚀 Como Executar

Por enquanto, você pode testar a classe `Carro` diretamente com um script Python:

```python
from carro import Carro

carro1 = Carro("Civic", 2022, "XYZ-1234")
print(carro1)

carro1.alugar()
print(carro1)

carro1.devolver()
print(carro1)
```

---

## 📌 Objetivos Futuros

- Implementar a classe `Cliente`
- Criar a classe `Locadora` para controlar os cadastros e operações
- Adicionar persistência dos dados com arquivos ou banco de dados
- Criar uma interface gráfica ou web futuramente
