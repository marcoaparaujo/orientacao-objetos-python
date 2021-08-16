class Aluno:

    def __init__(self, nome, sobrenome):
        self._nome = nome
        self._sobrenome = sobrenome

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_sobrenome(self):
        return self._sobrenome

    def set_sobrenome(self, sobrenome):
        self._sobrenome = sobrenome

    def matricular(self):
        return f"Aluno {self._nome} {self._sobrenome} matriculado"


aluno = Aluno("Antonio", "Silva")
print(aluno.matricular())

