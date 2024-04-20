class Obra:

    def __init__(self):
        self.titulo = ""
        self.ano = 0
        self.editora = ""

    def getTitulo(self):
        return self.titulo

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getAno(self):
        return self.ano

    def setAno(self, ano):
        self.ano = ano

    def getEditora(self):
        return self.editora

    def setEditora(self, editora):
        self.editora = editora


class Livro(Obra):

    def __init__(self):
        Obra.__init__(self)
        self.autor_principal = ""
        self.isbn = 0
        self.estado = "disponivel"
        self.qtde_emprestimos = 0

    def getAutorPrincipal(self):
        return self.autor_principal

    def setAutorPrincipal(self, autor_principal):
        self.autor_principal = autor_principal

    def getIsbn(self):
        return self.isbn

    def setIsbn(self, isbn):
        self.isbn = isbn

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getQtdeEmprestimos(self):
        return self.qtde_emprestimos

    def setQtdeEmprestimos(self, qtde_emprestimos):
        self.qtde_emprestimos = qtde_emprestimos

    def emprestar(self):
        if self.estado == "disponivel":
            self.estado = "emprestado"
            self.qtde_emprestimos += 1

    def devolver(self):
        if self.estado == "emprestado":
            self.estado = "disponivel"

    def exibir(self):
        print(self.titulo, self.autor_principal, self.ano, self.editora, self.isbn, self.estado, self.qtde_emprestimos)


class Revista(Obra):

    def __init__(self):
        Obra.__init__(self)
        self.issn = 0

    def getIssn(self):
        return self.issn

    def setIssn(self, issn):
        self.issn = issn

    def exibir(self):
        if 2024 - self.ano <= 5:
            print(self.titulo, self.ano, self.editora, self.issn)
        else:
            print("Dados da revista não podem ser exibidos")


class Pessoa():

    def __init__(self):
        self.nome = ""
        self.telefone = ""
        self.email = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getTelefone(self):
        return self.telefone

    def setTelefone(self, telefone):
        self.telefone = telefone

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email


class Bibliotecario(Pessoa):

    def __init__(self):
        Pessoa.__init__(self)
        self.matricula = 0
        self.tempo_servico = 0

    def getMatricula(self):
        return self.matricula

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getTempoServico(self):
        return self.tempo_servico

    def setTempoServico(self, tempo_servico):
        self.tempo_servico = tempo_servico

    def calcularSalario(self):
        return 2000 + (self.tempo_servico * 0.1 * 2000)

    def exibir(self):
        print(self.nome, self.telefone, self.email, self.matricula, self.tempo_servico, self.calcularSalario())

class Leitor(Pessoa):

    def __init__(self):
        Pessoa.__init__(self)
        self.idade = 0
        self.logradouro = ""
        self.numero = 0
        self.complemento = ""
        self.bairro = ""
        self.cidade = ""
        self.estado = ""
        self.cep = 0

    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade

    def getLogradouro(self):
        return self.logradouro

    def setLogradouro(self, logradouro):
        self.logradouro = logradouro

    def getNumero(self):
        return self.numero

    def setNumero(self, numero):
        self.numero = numero

    def getComplemento(self):
        return self.complemento

    def setComplemento(self, complemento):
        self.complemento = complemento

    def getBairro(self):
        return self.bairro

    def setBairro(self, bairro):
        self.bairro = bairro

    def getCidade(self):
        return self.cidade

    def setCidade(self, cidade):
        self.cidade = cidade

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getCep(self):
        return self.cep

    def setCep(self, cep):
        self.cep = cep

    def validar(self):
        if self.idade < 18:
            print("Leitor nao pode fazer emprestimos")
        else:
            print("Leitor pode fazer emprestimos")

    def incrementar_idade(self):
        self.idade += 1

    def decrementar_idade(self):
        if self.idade > 0:
            self.idade -= 1

    def exibir(self):
        print(self.nome, self.telefone, self.email, self.idade, self.logradouro, self.numero, self.complemento, self.bairro, self.cidade, self.estado, self.cep)


livro = Livro()
livro.setTitulo("Algoritmos")
livro.setAutorPrincipal("Horowitz")
livro.setAno(2020)
livro.setEditora("Atlas")
livro.setIsbn(1)
livro.exibir()
livro.emprestar()
livro.exibir()
livro.devolver()
livro.exibir()

revista = Revista()
revista.setTitulo("Revista de Programação")
revista.setAno(2020)
revista.setEditora("Editora A")
revista.setIssn(1)
revista.exibir()
revista.setAno(1990)
revista.exibir()

bibliotecario = Bibliotecario()
bibliotecario.setNome("Maria")
bibliotecario.setTelefone("(24)1234-5678")
bibliotecario.setEmail("maria@biblioteca.com.br")
bibliotecario.setMatricula(100)
bibliotecario.setTempoServico(2)
bibliotecario.exibir()

leitor = Leitor()
leitor.setNome("Joao")
leitor.setTelefone("(24)1234-2345")
leitor.setEmail("joao@leitor.com.br")
leitor.setIdade(17)
leitor.setLogradouro("Rua A")
leitor.setNumero(20)
leitor.setComplemento("apto 201")
leitor.setBairro("Centro")
leitor.setCidade("Vassouras")
leitor.setEstado("RJ")
leitor.setCep("20000-000")
leitor.validar()
leitor.setIdade(18)
leitor.validar()
leitor.decrementar_idade()
leitor.validar()
leitor.incrementar_idade()
leitor.validar()
leitor.exibir()
leitor.setIdade(0)
leitor.exibir()
leitor.decrementar_idade()
leitor.exibir()


