from random import choice
print("Vamos jogar Jokenpô?")
print("""Escolha entre PEDRA, PAPEL e TESOURA e descubra se você venCeu o computador.
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA""")
lista = 1, 2, 3
escolha = int(input("Sua escolha: "))
jokenpo = choice(lista)
if escolha == 1 and escolha == jokenpo:
    escolha = "PEDRA"
    jokenpo = "PEDRA"
    print("EMPATE")
elif escolha == 1 and jokenpo == 2:
    escolha = "PEDRA"
    jokenpo = "PAPEL"
    print("Você perdeu!")
elif escolha == 1 and jokenpo == 3:
    escolha = "PEDRA"
    jokenpo = "TESOURA"
    print("Você venceu!")
if escolha == 2 and escolha == jokenpo:
    escolha = "PAPEL"
    jokenpo = "PAPEL"
    print("EMPATE")
elif escolha == 2 and jokenpo == 3:
    escolha = "PAPEL"
    jokenpo = "TESOURA"
    print("Você perdeu!")
elif escolha == 2 and jokenpo == 1:
    escolha = "PAPEL"
    jokenpo = "PEDRA"
    print("Você venceu!")
if escolha == 3 and escolha == jokenpo:
    escolha = "TESOURA"
    jokenpo = "TESOURA"
    print("EMPATE")
elif escolha == 3 and jokenpo == 2:
    escolha = "TESOURA"
    jokenpo = "PAPEL"
    print("Você venceu!")
elif escolha == 3 and jokenpo == 1:
    escolha = "TESOURA"
    jokenpo = "PEDRA"
    print("Você perdeu!")
print("Você jogou {} e o computador jogou {}.".format(escolha, jokenpo))
