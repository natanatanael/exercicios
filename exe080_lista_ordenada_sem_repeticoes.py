numeros = []
for c in range(0, 5):
    n = int(input("Digite um valor: "))
    if c == 0: # or n > numeros[-1]:
        numeros.append(n)
        print("Adicionado ao final da lista...")
    elif n > numeros[-1]: # se usar o OR no if, não preciso desse elif.
        numeros.append(n)
        print("Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos += 1
print(f"Os valores digitados, em ordem, foram: {numeros}")