numeros = []
while True:
    numeros.append(int(input("Digite um número: ")))
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp in "Nn":
        break
numeros.sort(reverse=True)
print(f"Quantidade de valores digitados: {len(numeros)}")
print(f"Foram digitados os seguintes valores: {numeros}")
if 5 in numeros:
    print(f"O valor 5 está na lista na posição {numeros.index(5)}")
else:
    print("O valor 5 não foi digitado.")