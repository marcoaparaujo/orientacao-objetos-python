class Pessoa:

    def __init__(self):
        self.nome = ""

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

class Professor(Pessoa):

    def __init__(self):
        Pessoa.__init__(self)
        self.titulacao = ""

    def setTitulacao(self, titulacao):
        self.titulacao = titulacao


    def getTitulacao(self):
        return self.titulacao


class Aluno(Pessoa):

    def __init__(self):
        Pessoa.__init__(self)
        self.matricula = 0
        self.nota1 = 0
        self.nota2 = 0

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula

    def setNota1(self, nota1):
        self.nota1 = nota1

    def getNota1(self):
        return self.nota1

    def setNota2(self, nota2):
        self.nota2 = nota2

    def getNota2(self):
        return self.nota2

    def calcularMedia(self):
        return (self.nota1 + self.nota2) / 2


class AlunoEnsinoMedio(Aluno):

    def calcularAprovacao(self):
        media = self.calcularMedia()
        if media >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

class AlunoGraduacao(Aluno):

    def calcularAprovacao(self):
        media = self.calcularMedia()
        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"


aluno1 = AlunoEnsinoMedio()
aluno1.setMatricula(1)
aluno1.setNome("Ana")
aluno1.setNota1(6)
aluno1.setNota2(6)
print(aluno1.calcularAprovacao())

aluno2 = AlunoGraduacao()
aluno2.setMatricula(2)
aluno2.setNome("Maria")
aluno2.setNota1(7)
aluno2.setNota2(7)
print(aluno2.calcularAprovacao())

aluno3 = AlunoEnsinoMedio()
aluno3.setMatricula(3)
aluno3.setNome("Pedro")
aluno3.setNota1(5)
aluno3.setNota2(5)
print(aluno3.calcularAprovacao())

aluno4 = AlunoGraduacao()
aluno4.setMatricula(4)
aluno4.setNome("Joao")
aluno4.setNota1(6)
aluno4.setNota2(6)
print(aluno4.calcularAprovacao())

professor1 = Professor()
professor1.setNome("Antonio")
professor1.setTitulacao("Doutorado")
print(professor1.getNome())
print(professor1.getTitulacao())
