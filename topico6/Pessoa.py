class Pessoa:

    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def setGenero(self, genero):
        self.genero = genero

    def getGenero(self):
        return self.genero


