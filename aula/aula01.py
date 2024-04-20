class Aluno:
    def __init__(self):
        self.nome = ""
        self.matricula = 0
        self.endereco = ""
        self.telefone = ""
        self.nota1 = 0
        self.nota2 = 0

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEndereco(self):
        return self.endereco

    def setTelefone(self, telefone):
        self.telefone = telefone

    def getTelefone(self):
        return self.telefone

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
    def verificarAprovacao(self):
        media = self.calcularMedia()
        if media < 4:
            resultado = "Reprovado"
        else:
            if media >= 7:
                resultado = "Aprovado"
            else:
                resultado = "Prova Final"
        return resultado

aluno = Aluno()
aluno.setNome("Caio")
aluno.setNota1(5)
aluno.setNota2(5)
print(aluno.verificarAprovacao())


# aluno.setMatricula(123)
# aluno.setEndereco("Av. Expedicionarios")
# aluno.setTelefone("24 1234")
# print(aluno.getNome())
# print(aluno.getMatricula())
# print(aluno.getEndereco())
# print(aluno.getTelefone())