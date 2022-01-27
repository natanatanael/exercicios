from datetime import date
cont = 0
contmenor = 0
for c in range(1, 8):
    ano = int(input("Em que ano a {}ª nasceu: ".format(c)))
    if (date.today().year - ano) >= 18:
        maior = (date.today().year - ano) >= 18
        cont += maior
    else:
        menor = (date.today().year - ano) < 18
        contmenor += menor
print("Quantidade de pessoas que atingiram a maioridade: {}".format(cont))
print("Quantidade de pessoas que ainda não atingiram a maioridade: {}".format(contmenor))

