termo = int(input("Informe o termo da PA: "))
razao = int(input("Informe a razão da PA: "))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    pa = c
    print("{}".format(pa), end=" ")






