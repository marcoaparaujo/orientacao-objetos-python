class Estado:

    def __init__(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome


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


class Escolaridade:

    def __init__(self, descricao):
        self.descricao = descricao

    def getDescricao(self):
        return self.descricao

    def setDescricao(self, descricao):
        self.descricao = descricao


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


class Professor(Pessoa):

    def __init__(self, nome):
        Pessoa.__init__(self, nome)


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


# estado = Estado("MG")
#
# cidade = Cidade("Juiz de Fora")
# print(cidade.getNome())
#
# cidade.setEstado(estado)
# print(cidade.getNomeEstado())


# letra A: Qual a escolaridade de um professor?
# escolaridade = Escolaridade("Mestrado")
# professor = Professor("Ana")
# professor.setEscolaridade(escolaridade)
#
# print(professor.getDescricaoEscolaridade())

# letra B: Qual a escolaridade do coordenador de um curso?
escolaridade = Escolaridade("Pos-Graduacao")
professor = Professor("Maria")
curso = Curso("Computacao")
professor.setEscolaridade(escolaridade)
curso.setCoordenador(professor)

print(curso.getDescricaoEscolaridadeCoordenador())

