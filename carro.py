from dataclasses import dataclass

@dataclass
class Carro:
    modelo: str
    ano: int
    placa: str
    disponivel: bool = True

    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O carro {self.modelo} {self.placa} foi alugado com sucesso.")
        else:
            print(f"O carro {self.modelo} {self.placa} já está alugado.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O carro {self.modelo} {self.placa} foi devolvido com sucesso.")
        else:
            print(f"O carro {self.modelo} {self.placa} já está disponível.")

    def __str__(self):
        status = "Disponível" if self.disponivel else "Alugado"
        return f"Modelo: {self.modelo}, Ano: {self.ano}, Placa: {self.placa}, Status: {status}"
