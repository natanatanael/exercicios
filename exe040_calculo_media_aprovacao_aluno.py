nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
media = (nota1 + nota2) / 2
if media < 5.0:
    print("Média abaixo de 5: REPROVADO")
elif 7 > media >= 5:
    print("Média entre 5.0 e 6.9: RECUPERAÇÃO")
elif media >= 7:
    print("Média 7.0 ou superior: APROVADO")
