media = 0
soma = 0
velho = 0
nomevelho = " "
mulher = 0
mulhervinte = 0
contmulhervinte = 0
for d in range(1, 5):
    print("----- {}ª PESSOA -----".format(d))
    nome = str(input("Nome completo: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M/F): ")).strip()
    soma = soma + idade
    media = soma / 4
    mulher = mulher + (sexo == "F")
    nomesplit = nome.split()
    if nomesplit == [0]:
        print("Escreva seu nome completo")
    if d == 1 and sexo in "Mn":
        velho = idade
        nomevelho = nome
    if sexo in "Mm" and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo == "F" and idade < 20:
        mulhervinte = sexo == "F" and idade < 20
        contmulhervinte = contmulhervinte + mulhervinte
print("A média de idade do grupo é de {} anos".format(media))
print("O homem mais velho tem {} anos e se chama {}".format(velho, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(contmulhervinte))

# outra opção:  """ if sexo == "F" and idade < 20:
#                      mulhervinte = mulhervinte + 1 """
