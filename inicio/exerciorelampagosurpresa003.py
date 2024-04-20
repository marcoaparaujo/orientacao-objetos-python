class Funcionario:

    def __init__(self):
        self.nome = ""
        self.salarioBruto = 0
        self.desconto = 0
        self.acrescimo = 0

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getSalarioBruto(self):
        return self.salarioBruto

    def setSalarioBruto(self, salarioBruto):
        self.salarioBruto = salarioBruto

    def getDesconto(self):
        return self.desconto

    def setDesconto(self, desconto):
        self.desconto = desconto

    def getAcrescimo(self):
        return self.acrescimo

    def setAcrescimo(self, acrescimo):
        self.acrescimo = acrescimo


    def calcularSalarioLiquido(self):
        return self.salarioBruto + self.acrescimo - self.desconto


nome = input("Digite o nome funcionario: ")
salarioBruto = int(input("Digite o salario bruto: "))
desconto = int(input("Digite o desconto: "))
acrescimo = int(input("Digite o acrescimo: "))

funcionario = Funcionario()
funcionario.setSalarioBruto(salarioBruto)
funcionario.setAcrescimo(acrescimo)
funcionario.setDesconto(desconto)

print(f"Salario Liquido = {funcionario.calcularSalarioLiquido()}")

