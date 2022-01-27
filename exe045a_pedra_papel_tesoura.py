from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
print("""Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 3 ] Tesoura""")
jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)
print("-=" * 10)
print("O computador jogou {}.".format(itens[computador]))
print("O jogador jogou {}.".format(itens[jogador]))
print("-=" * 10)
if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("Jogador venceu!")
    elif jogador == 2:
        print("Computador venceu!")
    else:
        print("Jogada inválida. Tente novamente.")
elif computador == 1:
    if jogador == 0:
        print("Computador venceu!")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("Jogador venceu!")
    else:
        print("Jogada inválida. Tente novamente.")
elif computador == 2:
    if jogador == 0:
        print("Jogador venceu!")
    elif jogador == 1:
        print("Computador venceu!")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("Jogada inválida. Tente novamente.")