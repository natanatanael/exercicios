'''import math
num = float(input("Digite um número com vários dígitos: "))
inteiro = math.floor(num)
print("O valor digitado foi {} e a sua porção inteira é {}".format(num, inteiro))'''

import math
num = float(input("Digite um número com vários dígitos: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num, math.trunc(num)))








