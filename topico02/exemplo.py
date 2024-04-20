class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome


class PessoaFisica(Pessoa):

    def __init__(self, nome, cpf):
        Pessoa.__init__(self, nome)
        self.cpf = cpf

    def getCpf(self):
        return self.cpf

    def setCpf(self, cpf):
        self.cpf = cpf


class Cliente(PessoaFisica):

    def __init__(self, nome, cpf, limiteCredito):
        PessoaFisica.__init__(self, nome, cpf)
        self.limiteCredito = limiteCredito

    def getLimiteCredito(self):
        return self.limiteCredito

    def setLimiteCredito(self, limiteCredito):
        self.limiteCredito = limiteCredito


# nome = input("Digite um nome: ")
# cpf = input("Digite um cpf: ")
# limiteCredito = input("Digite um limite de credito: ")

# cliente = Cliente(nome, cpf, limiteCredito)

cliente = Cliente("Ana", 123, 1000)

print(f"Nome = {cliente.getNome()}")
print(f"CPF = {cliente.getCpf()}")
print(f"Limite de credito = {cliente.getLimiteCredito()}")



