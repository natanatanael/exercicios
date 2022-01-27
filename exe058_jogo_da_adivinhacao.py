from random import randint
comp = randint(0,10)
print("Acabei de pensar em número entre 0 a 10.")
print("Será que você consegue adivinhar qual foi?")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    palpite += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print("Mais...")
        else:
            print("Menos...")
print("Acertou com {} tentativas.".format(palpite))