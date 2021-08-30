class Aluno:

    def __init__(self, nome, sobrenome, nota1, nota2):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nota1 = nota1
        self.nota2 = nota2

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setSobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def getSobrenome(self):
        return self.sobrenome

    def setNota1(self, nota1):
        self.nota1 = nota1

    def getNota1(self):
        return self.nota1

    def setNota2(self, nota2):
        self.nota2 = nota2

    def getNota2(self):
        return self.nota2

    def getNomeCompleto(self):
        return self.nome + " " + self.sobrenome

    def getSomaNotas(self):
        return self.nota1 + self.nota2

    def getMediaNotas(self):
        return (self.nota1 + self.nota2) / 2


nome = input("Digite o nome do aluno: ")
sobrenome = input("Digite o sobrenome do aluno: ")
nota1 = int(input("Digite a primeira nota do aluno: "))
nota2 = int(input("Digite a segunda nota do aluno: "))

aluno = Aluno(nome, sobrenome, nota1, nota2)

print(f"Nome  = {aluno.getNomeCompleto()}")
print(f"Soma  = {aluno.getSomaNotas()}")
print(f"Média = {aluno.getMediaNotas()}")



