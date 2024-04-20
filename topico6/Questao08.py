from topico6.Aluno import Aluno
from topico6.Curso import Curso

curso = Curso("Informatica")
aluno1 = Aluno("Jose", "M")
aluno2 = Aluno("Julia", "F")

curso.matricular(aluno1)

print(curso.verificarAluno(aluno1))
print(curso.verificarAluno(aluno2))


