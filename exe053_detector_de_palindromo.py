frase = str(input("Escreva uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
"""inverso = " "     """
inverso = junto[::-1]

"""for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(" O inverso de {} é {}".format(junto, inverso))"""

if junto == inverso:
    print("Isso é um PALÍNDROMO.")
else:
    print("Isso não é um PALÍNDROMO")
