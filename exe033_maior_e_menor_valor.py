# Informando a posição do menor e do maior valor

"""valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))
valor3 = float(input("Digite outro valor: "))
menor = min(valor1, valor2, valor3)
maior = max(valor1, valor2, valor3)
if menor == valor1:
    print("O valor 1 foi o menor valor)
if menor == valor2:
    print("O valor 2 foi o menor valor)
if menor == valor3:
    print("O valor 3 foi o menor valor)
if maior == valor1:
    print("O valor 1 foi o maior valor)
if maior == valor2:
    print("O valor 2 foi o maior valor)
if maior == valor3:
    print("O valor 3 foi o maior valor)"""

# Informando o menor e o maior valor utilizando a lógica

v1 = float(input("Digite um valor: "))
v2 = float(input("Digite outro valor: "))
v3 = float(input("Digite outro valor: "))
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
print("O menor valor informado foi {}".format(menor))
maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print("O maior valor informado foi {}".format(maior))

# Informando o menor e o maior valor utilizando as funções de mínima e máxima.

"""valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))
valor3 = float(input("Digite outro valor: "))
menor = min(valor1, valor2, valor3)
maior = max(valor1, valor2, valor3)
print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))"""
