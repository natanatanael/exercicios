"""import random
from time import sleep
print("-=-" * 20)
num = int(input("Escolha um número de 0 a 5 e descubra se foi o mesmo que o computador escolheu: ")) # numero jogador
lista = [1, 2, 3, 4, 5]
comp = random.choice(lista)
print("-=-" * 20)
print("PROCESSANDO...")
sleep(3)
print("O numero que o computador escolheu foi: {}".format(comp))
if comp == num:
    print("Parabéns, você ganhou!")
else:
    print("O computador venceu!")"""


from random import randint
from time import sleep
comp = randint(0,5)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(3)
if jogador == comp:
    print("Parabéns, você me venceu!")
else:
    print("Você perdeu. Eu pensei no número {}!".format(comp))
