valores = []
resp = 0
while True:
    num = int(input("Digite um valor: "))
    if num not in valores:
        valores.append(num)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado. Não foi possível adicionar...")
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp in "Nn":
        break
valores.sort()
print(f"Esses foram os valores adicionados: {valores}")