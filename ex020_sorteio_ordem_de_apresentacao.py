from random import shuffle
aluno1 = str(input("Aluno 1: "))
aluno2 = str(input("Aluno 2: "))
aluno3 = str(input("Aluno 3: "))
aluno4 = str(input("Aluno 4: "))
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print("A ordem de apresentação será a seguinte: {}".format(alunos))








