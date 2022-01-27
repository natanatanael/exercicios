import random
aluno1 = str(input("Aluno 1: "))
aluno2 = str(input("Aluno 2: "))
aluno3 = str(input("Aluno 3: "))
aluno4 = str(input("Aluno 4: "))
alunos = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(alunos)
print("O aluno sorteado para apagar a lousa na aula de hoje foi: {}".format(sorteio))

