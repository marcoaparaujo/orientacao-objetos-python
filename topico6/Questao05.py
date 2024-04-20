from topico6.Aluno import Aluno
from topico6.Curso import Curso

curso1 = Curso("Informatica")
curso2 = Curso("Computacao")

aluno1 = Aluno("Ana", "F")
aluno2 = Aluno("Antonio", "M")
aluno3 = Aluno("Maria", "F")

curso1.matricular(aluno1)
curso2.matricular(aluno2)
curso1.matricular(aluno3)

curso2.listarAlunos()