class Cidade:

    def __init__(self, nome):
        self.nome = nome
        self.estado = None

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def getNomeEstado(self):
        if self.estado == None:
            return "Cidade não tem Estado"
        else:
            return self.estado.getNome()

