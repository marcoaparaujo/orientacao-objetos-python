class Curso():

    def __init__(self):
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

class Aluno():
    def __init__(self):
        self.curso = None
    def getCurso(self):
        return self.curso
    def setCurso(self, curso):
        self.curso = curso
    def getNomeCurso(self):
        if self.curso == None:
            return "Aluno sem curso"
        else:
            return self.curso.getNome()


curso = Curso()
curso.setNome("Engenharia de Software")

aluno = Aluno()
aluno.setCurso(curso)

print(aluno.getNomeCurso())


