class Curso:

    def __init__(self, nome):
        self.nome = nome
        self.coordenador = None

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setCoordenador(self, coordenador):
        self.coordenador = coordenador

    def getCoordenador(self):
        return self.coordenador

    def getDescricaoEscolaridadeCoordenador(self):
        if self.coordenador == None:
            return "Curso sem coordenador"
        else:
            return self.coordenador.getDescricaoEscolaridade()