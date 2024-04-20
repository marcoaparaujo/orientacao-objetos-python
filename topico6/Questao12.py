from topico6.Aluno import Aluno
from topico6.Curso import Curso

curso = Curso("Informatica")
aluno1 = Aluno("Macedo", "M")
aluno2 = Aluno("Marina", "F")

curso.matricular(aluno1)
curso.matricular(aluno2)

curso.listarAlunos()

curso.removerAluno(aluno1)

print("Lista após a remoçao")

curso.listarAlunos()

curso.removerAluno(aluno1)
