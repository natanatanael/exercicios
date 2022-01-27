"""from math import factorial
num = int(input("Informe um número para descobrir o seu fatorial: "))
fatorial = factorial(num)
print(fatorial)"""


num = int(input("Informe um número para descobrir o seu fatorial: "))
c = num
fatorial = 1
while c > 0:
    print("{}".format(c),end=" ")
    print(" x " if c > 1 else " = ", end=" ")
    fatorial = fatorial * c
    c = c - 1
print("{}".format(fatorial))



