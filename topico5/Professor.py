from topico5.Pessoa import Pessoa


class Professor(Pessoa):

    def __init__(self, nome):
        Pessoa.__init__(self, nome)