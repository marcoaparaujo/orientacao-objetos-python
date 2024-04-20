class Pessoa():
    def __init__(self):
        self.nome = ""

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

class Professor(Pessoa):
    None


class Aluno(Pessoa):
    None


class Curso():
    def __init__(self):
        self.alunos = []
        self.turmas = []

    def matricular(self, aluno):
        self.alunos.append(aluno)

    def abrir_turma(self, turma):
        self.turmas.append(turma)

    def exibirNomesProfessoresTurmas(self):
        for turma in self.turmas:
            print(turma.getNomeProfessor())

class Turma():
    def __init__(self):
        self.professor = None
        self.disciplina = None
        self.alunos = []

    def setProfessor(self, professor):
        self.professor = professor

    def getProfessor(self):
        return self.professor

    def setDisciplina(self, disciplina):
        self.disciplina = disciplina

    def getDisciplina(self):
        return self.disciplina

    def matricular(self, aluno):
        self.alunos.append(aluno)

    def getNomeProfessor(self):
        if self.professor == None:
            return "Turma sem professor"
        else:
            return self.professor.getNome()

    def exibirAlunos(self):
        for aluno in self.alunos:
            print(aluno.getNome())

    def verificarAlunoMatriculado(self, aluno):
        return aluno in self.alunos

    def desmatricularAluno(self, aluno):
        self.alunos.remove(aluno)

class Disciplina():
    None

# Questao 1
# professor = Professor()
# professor.setNome("Paulo Henrique")
# turma = Turma()
# turma.setProfessor(professor)
# print(turma.getNomeProfessor())
#
# Questao 2
# turma = Turma()
# aluno1 = Aluno()
# aluno1.setNome("Bernardo")
# aluno2 = Aluno()
# aluno2.setNome("Murilo")
# turma.matricular(aluno1)
# turma.matricular(aluno2)
# turma.exibirAlunos()
#
# Questao 3
curso = Curso()
turma1 = Turma()
turma2 = Turma()
professor1 = Professor()
professor2 = Professor()
professor1.setNome("Paulo")
professor2.setNome("Henrique")
turma1.setProfessor(professor1)
turma2.setProfessor(professor2)
curso.abrir_turma(turma1)
curso.abrir_turma(turma2)
curso.exibirNomesProfessoresTurmas()
#
# Questao 7
# turma = Turma()
# aluno1 = Aluno()
# aluno2 = Aluno()
# turma.matricular(aluno1)
# print(turma.verificarAlunoMatriculado(aluno1))
# print(turma.verificarAlunoMatriculado(aluno2))

# Questao 10
turma = Turma()
aluno = Aluno()
turma.matricular(aluno)
print(turma.verificarAlunoMatriculado(aluno))
turma.desmatricularAluno(aluno)
print(turma.verificarAlunoMatriculado(aluno))

