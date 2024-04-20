# Classe Carro:
#
# Atributos: marca, modelo, ano, velocidade_atual, estado
# Métodos: acelerar, frear, ligar, desligar
# •	acelerar(quantidade): aumenta a velocidade atual do carro pela quantidade especificada.
# •	frear(quantidade): diminui a velocidade atual do carro pela quantidade especificada, sem deixar que a velocidade fique negativa.
# •	ligar(): altera o estado do carro para ligado.
# •	desligar(): altera o estado do carro para desligado e zera a velocidade atual.

class Carro:

    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.ano = 0
        self.cor = ""
        self.velocidade_atual = 0
        self.estado = "desligado"

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    def getAno(self):
        return self.ano

    def setAno(self, ano):
        self.ano = ano

    def getCor(self):
        return self.cor

    def setCor(self, cor):
        self.cor = cor

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def setVelocidadeAtual(self, velocidade):
        if self.estado == "ligado":
            if velocidade >= 0:
                self.velocidade_atual = velocidade

    def getVelocidadeAtual(self):
        return self.velocidade_atual

    def desligar(self):
        self.estado = "desligado"
        self.velocidade_atual = 0

    def ligar(self):
        self.estado = "ligado"

    def acelerar(self, quantidade):
        if self.estado == "ligado":
            self.velocidade_atual += quantidade

    def frear(self, quantidade):
        if self.estado == "ligado":
            self.velocidade_atual -= quantidade
            if self.velocidade_atual < 0:
                self.velocidade_atual = 0


carro = Carro()
carro.setMarca("VW")
# print(carro.getMarca())
# print(carro.getEstado())
# carro.ligar()
# print(carro.getEstado())
# carro.desligar()
# print(carro.getEstado())
carro.ligar()
carro.setVelocidadeAtual(100)
print(carro.getVelocidadeAtual())
carro.acelerar(30)
print(carro.getVelocidadeAtual())
carro.frear(20)
print(carro.getVelocidadeAtual())
carro.desligar()
print(carro.getVelocidadeAtual())

carro2 = Carro()
carro2.setMarca("Fiat")
carro2.ligar()
carro2.setVelocidadeAtual(-80)
print(carro2.getVelocidadeAtual())