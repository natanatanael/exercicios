soma = 0
cont = 0
for c in range(0, 6):
    num = int(input("Informe o {} valor: ".format(c)))
    par = num % 2 == 0
    if par:
        soma = soma + num
        cont = cont + 1
print("Você infomou {} números PARES e a soma de todos os números pares é {}".format(cont, soma))