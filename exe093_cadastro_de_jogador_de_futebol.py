jogador = {}
jogador["nome"] = str(input("Nome do jogador: ")),
jogador["partidas"] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
gols = []
if jogador["partidas"] == 0:
    print(jogador)
for c in range(jogador["partidas"]):
    gols.append(int(input(f"  Quantos gols na partida {c+1}? ")))
    jogador["gols"] = gols
jogador["totalgols"] = sum(gols)
print("=" * 30)
print(jogador)
print("=" * 30)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("=" * 30)
print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.")
"""for c in range(jogador["partidas"]):
    print(f"=> Na partida {c+1}, fez ", )
for i, v in enumerate(gols):
    print(f"{v} gols")"""

for i, v in enumerate(jogador["gols"]):
    print(f"=> Na partida {i+1}, fez {v} gols", )
print(f"Foi um total de {jogador['totalgols']} gols")
