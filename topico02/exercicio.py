class Pessoa:

    def __init__(self, nome, celular, email):
        self.nome = nome
        self.celular = celular
        self.email = email

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getCelular(self):
        return self.celular

    def setCelular(self, celular):
        self.celular = celular

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email


class PessoaFisica(Pessoa):

    def __init__(self, nome, celular, email, cpf):
        Pessoa.__init__(self, nome, celular, email)
        self.cpf = cpf

    def setCpf(self, cpf):
        self.cpf = cpf

    def getCpf(self):
        return self.cpf


class Funcionario(PessoaFisica):

    def __init__(self, nome, celular, email, cpf, salario):
        PessoaFisica.__init__(self, nome, celular, email, cpf)
        self.salario = salario

    def setSalario(self, salario):
        self.salario = salario

    def getSalario(self):
        return self.salario


class Cliente(PessoaFisica):

    def __init__(self, nome, celular, email, cpf, limiteCredito):
        PessoaFisica.__init__(self, nome, celular, email, cpf)
        self.limiteCredito = limiteCredito

    def getLimiteCredito(self):
        return self.limiteCredito

    def setLimiteCredito(self, limiteCredito):
        self.limiteCredito = limiteCredito


class Fornecedor(Pessoa):

    def __init__(self, nome, celular, email, cnpj, prazoEntrega):
        Pessoa.__init__(self, nome, celular, email)
        self.cnpj = cnpj
        self.prazoEntrega = prazoEntrega

    def getCnpj(self):
        return self.cnpj

    def setCnpj(self, cnpj):
        self.cnpj = cnpj

    def getPrazoEntrega(self):
        return self.prazoEntrega

    def setPrazoEntrega(self, prazoEntrega):
        self.prazoEntrega = prazoEntrega



funcionario = Funcionario("Josue", "99881122", "josue@gmail.com", "123456", 1000)

cliente = Cliente("Julia", "99998888", "julia@gmail.com", "987654", 2000)

fornecedor = Fornecedor("Empresa ABC", "88887777", "empresaabc@gmail.com", "21436587", 10)


print(f"Nome do Funcionário = {funcionario.getNome()}")
print(f"Celular do Funcionário = {funcionario.getCelular()}")
print(f"Email do Funcionário = {funcionario.getEmail()}")
print(f"CPF do Funcionário = {funcionario.getCpf()}")
print(f"Salário do Funcionário = {funcionario.getSalario()}")
print()
print(f"Nome do Cliente = {cliente.getNome()}")
print(f"Celular do Cliente = {cliente.getCelular()}")
print(f"Email do Cliente = {cliente.getEmail()}")
print(f"CPF do Cliente = {cliente.getCpf()}")
print(f"Limite de Crédito do Cliente = {cliente.getLimiteCredito()}")
print()
print(f"Nome do Fornecedor = {fornecedor.getNome()}")
print(f"Celular do Fornecedor = {fornecedor.getCelular()}")
print(f"Email do Fornecedor = {fornecedor.getEmail()}")
print(f"CNPJ do Fornecedor = {fornecedor.getCnpj()}")
print(f"Prazo de Entrega do Fornecedor = {fornecedor.getPrazoEntrega()}")

