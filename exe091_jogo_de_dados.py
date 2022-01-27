from random import randint
from time import sleep
from operator import itemgetter
print('Valores sorteados')
jogadores = {}
jogadores["jogador1"] = randint(1,6)
jogadores["jogador2"] = randint(1,6)
jogadores["jogador3"] = randint(1,6)
jogadores["jogador4"] = randint(1,6)
ranking = {}
for k, v in jogadores.items():
    print(f"{k} tirou {v} no dado")
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print("=" * 50)
print(" == RANKING DOS JOGADORES == ")
for i, v in enumerate(ranking):
    print(f"  {i+1}° lugar: {v[0]} com {v[1]}")
    sleep(1)