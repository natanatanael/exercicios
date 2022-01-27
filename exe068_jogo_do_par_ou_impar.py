from random import choice
print("-=-"* 30)
print("VAMOS JOGAR PAR OU ÍMPAR?")
print("-=-"* 30)
v = 0
while True:
    num = range(0, 10)
    jogador = int(input("Digite um número: "))
    comp = choice(num)
    total = jogador + comp
    escolha = " "
    while escolha not in "PI":
        escolha = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    par = impar = 0
    resultado = 0
    if total % 2 == 0:
        resultado = "Par"
    else:
        resultado = "Impar"
    if escolha == "P":
        escolha = "Par"
    else:
        escolha = "Impar"
    print("-=-"* 30)
    print(f"Você jogou {jogador} e o computador jogou {comp}. Total de {total}. Deu {resultado}")
    print("-=-"* 30)
    if escolha == resultado:
       v += 1
       print("Você VENCEU")
    else:
        print("Você PERDEU")
    if escolha != resultado:
        break
    print("Vamos jogar novamente...")
    print("-=-" * 30)
print(f"GAME OVER! Você venceu {v} vezes.")

