totalpreco = mais1000 = menor = cont = 0
barato = " "
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço do produto: "))
    cont += 1
    totalpreco += preco
    if preco > 1000:
        mais1000 += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    continua = " "
    while continua not in "SN":
        continua = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continua == "N":
        break
print(f"O total gasto na compra foi de R$ {totalpreco:.2f}")
print(f"{mais1000} produtos custaram mais de R$ 1000 reais.")
print(f"O produto mais barato foi {barato} e custou R$ {menor:.2f}")
print("FIM")