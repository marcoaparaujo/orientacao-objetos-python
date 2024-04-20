class Curso:

    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def matricular(self, aluno):
        self.alunos.append(aluno)

    def listarAlunos(self):
        for aluno in self.alunos:
            print(aluno.getNome())

    def verificarAluno(self, aluno):
        saida = aluno.getNome()
        if aluno not in self.alunos:
            saida += " não"
        saida += " está "
        if aluno.getGenero() == "F":
            saida += "matriculada"
        else:
            saida += "matriculado"
        return saida

    def removerAluno(self, aluno):
        if aluno not in self.alunos:
            print("Aluno nao matriculado")
        else:
            print(f"{aluno.getNome()} removido")
            self.alunos.remove(aluno)


