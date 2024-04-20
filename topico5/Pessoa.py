
class Pessoa:

    def __init__(self, nome):
        self.nome = nome
        self.escolaridade = None
        self.naturalidade = None

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade

    def getEscolaridade(self):
        return self.escolaridade

    def setNaturalidade(self, cidade):
        self.naturalidade = cidade

    def getNaturalidade(self):
        return self.naturalidade

    def getDescricaoEscolaridade(self):
        if self.escolaridade == None:
            return "Pessoa sem escolaridade"
        else:
            return self.escolaridade.getDescricao()