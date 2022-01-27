primeiro = int(input("Informe o termo da PA: "))
razao = int(input("Informe a razão da PA: "))
termo = primeiro
cont = 1
total = 0
segue = 10
while segue != 0:
    total = total + segue
    while cont <= total:
        print("{} > ".format(termo), end=" ")
        termo += razao
        cont += 1
    print("PAUSA")
    segue = int(input("Quantos termos você quer mostrar a mais? "))
print("Progressão finalizada com {} termos.".format(total))