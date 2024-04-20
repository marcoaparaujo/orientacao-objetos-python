# 4.	Calcular a média de combustível gasto pelo usuário, sendo informado a quantidade de
# quilômetros rodados e a quantidade de combustível consumido.

class Carro:

    def __init__(self):
        self.quantidade_km = 0
        self.quantidade_litros = 0

    def calcular_media_combustivel(self):
        return self.quantidade_km / self.quantidade_litros

carro1 = Carro()
carro1.quantidade_km = 180
carro1.quantidade_litros = 50
print(carro1.calcular_media_combustivel())