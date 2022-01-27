from datetime import date
ano = int(input("Informe o ano de nascimento: "))
idade = date.today().year - ano
if idade <= 9:
    print("O atleta tem {} anos".format(idade))
    print("Classificação: MIRIM")
elif idade <= 14:
    print("O atleta tem {} anos".format(idade))
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("O atleta tem {} anos".format(idade))
    print("Classificação: JÚNIOR")
elif idade <= 25:
    print("O atleta tem {} anos".format(idade))
    print("Classificação: SÊNIOR")
elif idade > 25:
    print("O atleta tem {} anos".format(idade))
    print("Classificação: MASTER")