primeiro = int(input("Informe o termo da PA: "))
razao = int(input("Informe a razão da PA: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} > ".format(termo), end=" ")
    termo += razao
    cont += 1
print("FIM")