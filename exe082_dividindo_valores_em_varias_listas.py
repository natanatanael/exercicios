numeros = []
pares = []
impares = []
while True:
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        numeros.append(n)
        pares.append(n)
    else:
        numeros.append(n)
        impares.append(n)
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp in "Nn":
        break
print(f"Essa é a lista de TODOS os números digitados: {numeros}")
print(f"Essa é a lista de números pares digitados: {pares}")
print(f"Essa é a lista de números impares digitados: {impares}")

