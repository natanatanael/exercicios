maior = homem = mulher20under = 0
while True:
    print("-=-" * 30)
    print("DADOS CADASTRAIS")
    print("-=-" * 30)
    idade = int(input("Idade: "))
    if idade >= 18:
        maior += 1
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    if sexo == "M":
        sexo = homem
        homem += 1
    if sexo == "F" and idade < 20:
        mulher20under += 1
    continua = str(input("Quer continuar? [S/N] "))
    if continua in "Nn":
        break
print(f"Foram cadastradas {maior} pessoas com mais de 18 anos")
print(f"Foram cadastrados {homem} homens.")
print(f"Foram cadastradas {mulher20under} mulheres com menos de 20 anos")
print("FIM DO CADASTRO")