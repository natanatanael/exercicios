"""num = str(input("Digite um número de 0 a 9999: "))
print("Unidade: {}".format(num[3]))
print("Dezena: {}".format(num[2]))
print("Centena: {}".format(num[1]))
print(("Milhar: {}".format(num[0])))"""


num = int(input("Digite um número de 0 a 9999: "))
uni = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10
print("Unidade: {}".format(uni))
print("Dezena: {}".format(dez))
print("Centena: {}".format(cent))
print("Milhar: {}".format(mil))









