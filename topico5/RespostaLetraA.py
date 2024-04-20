
# letra A: Qual a escolaridade de um professor?
from topico5 import Escolaridade, Professor

escolaridade = Escolaridade("Mestrado")
professor = Professor("Ana")
professor.setEscolaridade(escolaridade)

print(professor.getDescricaoEscolaridade())