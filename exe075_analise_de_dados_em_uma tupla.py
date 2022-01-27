numbers = (int(input("Digite um valor: ")), int(input("Digite um valor: ")), int(input("Digite um valor: ")),
           int(input("Digite um valor: ")))
print(f"Você digitou os valores: {numbers}")
print(f"O valor 9 apareceu {numbers.count(9)} vezes")
if 3 in numbers:
    print(f"o valor 3 apareceu na {numbers.index(3) + 1}ª posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print(f"Os valores pares digitados foram ", end=" ")
for n in numbers:
    if n % 2 == 0:
        print(n, end=" ")



