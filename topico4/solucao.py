class Estado:

    def __init__(self, sigla):
        self.sigla = sigla

    def getSigla(self):
        return self.sigla

    def setSigla(self, sigla):
        self.sigla = sigla


class Cidade:

    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def getNomeEstado(self):
        return self.estado.getSigla()



class Escolaridade:

    def __init__(self, descricao):
        self.descricao = descricao

    def getDescricao(self):
        return self.descricao


class Pessoa:

    def __init__(self, escolaridade, naturalidade, nome):
        self.escolaridade = escolaridade
        self.naturalidade = naturalidade
        self.nome = nome

    def getEscolaridade(self):
        return self.escolaridade

    def getDescricaoEscolaridade(self):
        return self.escolaridade.getDescricao()

    def getNaturalidade(self):
        return self.naturalidade

    def setNaturalidade(self, naturalidade):
        self.naturalidade = naturalidade

    def getNomeEstadoNaturalidade(self):
        return self.naturalidade.getNomeEstado()

    def getNomeCidadeNaturalidade(self):
        return self.naturalidade.getNome()

    def getNome(self):
        return self.nome


class Professor(Pessoa):

    def __init__(self, escolaridade, naturalidade, curso, nome):
        Pessoa.__init__(self, escolaridade, naturalidade, nome)
        self.curso = curso

    def getDescricaoTipoEnsino(self):
        return self.curso.getDescricaoTipoEnsino()

    def getNomeDiretor(self):
        return self.curso.getNomeDiretor()

    def getNomeCoordenador(self):
        return self.curso.getNomeCoordenador()


class Aluno(Pessoa):

    def __init__(self, escolaridade, naturalidade, curso, nome):
        Pessoa.__init__(self, escolaridade, naturalidade, nome)
        self.curso = curso

    def getSiglaEstadoCurso(self):
        return self.curso.getSiglaEstado()

    def getNomeCoordenadorCurso(self):
        return self.curso.getNomeCoordenador()


class Curso:

    def __init__(self, coordenador, escola, tipoEnsino):
        self.coordenador = coordenador
        self.escola = escola
        self.tipoEnsino = tipoEnsino

    def getEscolaridadeCoordenador(self):
        return self.coordenador.getDescricaoEscolaridade()

    def getSiglaEstado(self):
        return self.escola.getSiglaEstado()

    def getDescricaoTipoEnsino(self):
        return self.tipoEnsino.getDescricao()

    def getNomeCoordenador(self):
        return self.coordenador.getNome()

    def getNomeDiretor(self):
        return self.escola.getNomeDiretor()


class Escola:

    def __init__(self, diretor, cidade):
        self.diretor = diretor
        self.cidade = cidade

    def getEscolaridadeDiretor(self):
        return self.diretor.getDescricaoEscolaridade()

    def getSiglaEstado(self):
        return self.cidade.getNomeEstado()

    def getNomeDiretor(self):
        return self.diretor.getNome()


class TipoEnsino:

    def __init__(self, descricao):
        self.descricao = descricao

    def getDescricao(self):
        return self.descricao



# letra A
print("Letra A")
escolaridade = Escolaridade("Nivel superior")
professor = Professor(escolaridade, None, None, None)
print(professor.getDescricaoEscolaridade())


# letra B
print("Letra B")
escolaridade = Escolaridade("Pos graducao")
professor = Professor(escolaridade, None, None, None)
curso = Curso(professor, None, None)
print(curso.getEscolaridadeCoordenador())


# letra C
print("Letra C")
escolaridade = Escolaridade("Mestrado")
professor = Professor(escolaridade, None, None, None)
escola = Escola(professor, None)
print(escola.getEscolaridadeDiretor())

# letra D
print("Letra D")
estado = Estado("MG")
cidade = Cidade("Juiz de Fora", estado)
aluno = Aluno(None, cidade, None, None)
print(aluno.getNomeEstadoNaturalidade())

# letra E
print("Letra E")
estado = Estado("MG")
cidade = Cidade("Juiz de Fora", estado)
professor = Professor(None, cidade, None, None)
print(professor.getNomeCidadeNaturalidade())

# letra F
print("Letra F")
estado = Estado("MG")
cidade = Cidade("Juiz de Fora", estado)
escola = Escola(None, cidade)
curso = Curso(None, escola, None)
aluno = Aluno(None, None, curso, None)
print(aluno.getSiglaEstadoCurso())

# letra G
print("Letra G")
tipoEnsino = TipoEnsino("Ensino Superior")
curso = Curso(None, None, tipoEnsino)
professor = Professor(None, None, curso, None)
print(professor.getDescricaoTipoEnsino())

# letra H
print("Letra H")
professor = Professor(None, None, None, "Ana")
curso = Curso(professor, None, None)
aluno = Aluno(None, None, curso, None)
print(aluno.getNomeCoordenadorCurso())

# letra I
print("Letra I")
diretor = Professor(None, None, None, "Maria")
escola = Escola(diretor, None)
curso = Curso(None, escola, None)
professor = Professor(None, None, curso, "Jose")
print(professor.getNomeDiretor())

# letra J
print("Letra J")
coordenador = Professor(None, None, None, "Pedro")
curso = Curso(coordenador, None, None)
professor = Professor(None, None, curso, None)
print(professor.getNomeCoordenador())