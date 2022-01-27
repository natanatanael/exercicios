numeros = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input("Digite um numero: "))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f"Valores pares: {numeros[0]}")
print(f"Valores ímpares: {numeros[1]}")




