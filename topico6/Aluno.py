from topico6.Pessoa import Pessoa


class Aluno (Pessoa):

    def __init__(self, nome, genero):
        Pessoa.__init__(self, nome, genero)

