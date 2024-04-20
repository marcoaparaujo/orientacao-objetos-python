class Curso:

    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def getNome(self):
        return self.nome

    def matricular(self, aluno):
        self.alunos.append(aluno)

    def listarAlunos(self):
        for aluno in self.alunos:
            print(aluno.getNome())

    def verificarAluno(self, aluno):
        return aluno in self.alunos

    def removerAluno(self, aluno):
        self.alunos.remove(aluno)


class Aluno:

    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome

    def getMatricula(self):
        return self.matricula

    def getNome(self):
        return self.nome


curso1 = Curso("Computacao")
curso2 = Curso("Arquitetura")
aluno1 = Aluno(1, "Ana")
aluno2 = Aluno(2, "Jose")
aluno3 = Aluno(3, "Maria")
curso1.matricular(aluno1)
curso1.matricular(aluno2)
curso2.matricular(aluno3)
print(curso1.verificarAluno(aluno1))
# print("Alunos no curso")
# curso1.listarAlunos()
curso1.removerAluno(aluno1)
# print("Alunos no curso")
# curso1.listarAlunos()
print(curso1.verificarAluno(aluno1))


