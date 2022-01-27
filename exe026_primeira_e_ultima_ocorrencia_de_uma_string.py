nome = str(input("Digite seu nome completo: ")).upper().strip()
letra = "A"
contagem = nome.count("A")
print("A letra {} apareceu {} vezes na frase.".format(letra, contagem))
primeira = nome.find("A") + 1
print("A primeira letra {} apareceu na posição {}.".format(letra, primeira))
ultima = nome.rfind("A") + 1
print("A última letra {} apareceu na posição {}.".format(letra, ultima))


