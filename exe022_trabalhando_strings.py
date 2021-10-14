from re import split

nome = str(input("Informe seu nome completo: ")).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
dividido = nome.split()
print(dividido[0])
print(len(dividido[0]))



































