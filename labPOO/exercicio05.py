# 5.	Classe Produto:
#
# Atributos: nome, preco, quantidade_estoque, categoria
# Métodos: adicionar_estoque, remover_estoque, aplicar_desconto
# •	adicionar_estoque(quantidade): Adiciona quantidade ao quantidade_estoque.
# •	remover_estoque(quantidade): Remove quantidade do quantidade_estoque, se houver quantidade suficiente.
# •	aplicar_desconto(percentual): Aplica um desconto de percentual ao preco do produto.

class Produto:

    def __init__(self):
        self.nome = ""
        self.preco = 0.0
        self.quantidade = 0
        self.categoria = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        self.preco = preco

    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

    def getCategoria(self):
        return self.categoria

    def setCategoria(self, categoria):
        self.categoria = categoria

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

    def remover_estoque(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade

    def aplicar_desconto(self, percentual):
        if percentual >= 0 and percentual <= 100:
            self.preco = self.preco * ((100 - percentual) / 100)


# preco = 50
# desconto = 10
# preco final = 45
# 50 * ((100 - 10) / 100)
# 50 * (90 / 100)
# 50 * 0.9
# 45


produto = Produto()
# print(produto.quantidade)
# produto.adicionar_estoque(10)
# print(produto.quantidade)
# produto.remover_estoque(8)
# print(produto.quantidade)

produto.setPreco(50)

produto.aplicar_desconto(-10)
print(produto.getPreco())
produto.aplicar_desconto(110)
print(produto.getPreco())

produto.aplicar_desconto(10)
print(produto.getPreco())

