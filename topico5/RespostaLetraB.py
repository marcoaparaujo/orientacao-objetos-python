from topico5.Curso import Curso
from topico5.Escolaridade import Escolaridade
from topico5.Professor import Professor


# letra B: Qual a escolaridade do coordenador de um curso?

escolaridade = Escolaridade("Pos-Graduacao")
professor = Professor("Maria")
curso = Curso("Computacao")
professor.setEscolaridade(escolaridade)
curso.setCoordenador(professor)

print(curso.getDescricaoEscolaridadeCoordenador())