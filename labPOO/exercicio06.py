# 6.	Classe Funcionario:
#
# Atributos: nome, cargo, salario, departamento
# Métodos: receber_aumento, mudar_departamento, exibir_dados
#
# •	receber_aumento(percentual): Aplica um aumento de percentual ao salario.
# •	mudar_departamento(novo_departamento): Altera o departamento para o novo_departamento.
# •	exibir_dados(): Exibe os dados do funcionário, incluindo nome, cargo, salário e departamento.

class Funcionario:

    def __init__(self):
        self.nome = ""
        self.cargo = ""
        self.salario = 0.0
        self.departamento = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getCargo(self):
        return self.cargo

    def setCargo(self, cargo):
        self.cargo = cargo

    def getSalario(self):
        return self.salario

    def setSalario(self, salario):
        self.salario = salario

    def getDepartamento(self):
        return self.departamento

    def mudar_departamento(self, departamento):
        self.departamento = departamento

    def receber_aumento(self, percentual):
        if percentual > 0:
            self.salario = self.salario * (1 + (percentual / 100))

    def exibir_dados(self):
        print(f"Nome = {self.nome}, Cargo = {self.cargo}, Salário = {self.salario:.2f}, Departamento = {self.departamento}")


funcionario = Funcionario()
funcionario.setSalario(1000)
funcionario.receber_aumento(10)
# print(funcionario.getSalario())

funcionario.mudar_departamento("Informatica")
# print(funcionario.getDepartamento())

funcionario.setNome("Luann")
funcionario.setCargo("Estagiário")
funcionario.exibir_dados()

