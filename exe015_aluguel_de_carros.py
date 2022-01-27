dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))
aluguel = 60.00
precokm = 0.15
totaldiarias = dias * aluguel
totalkm = km * precokm
precototal = totaldiarias + totalkm
print("O valor a pagar por {} diárias é de R$ {}, mais R$ {} por {} km rodados, totalizando o valor de R$ {}.".format(dias, totaldiarias, totalkm, km, precototal))


