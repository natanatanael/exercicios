num = cont = soma = 0
num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um número [999 para parar]: "))
print("O total de números informados foi {} e a soma de todos os números informados é {}.".format(cont, soma))

