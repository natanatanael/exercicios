def area(larg, comp):
    a = larg * comp
    print(f"A área de um terreno com {larg}x{comp} é de {a}mª")


print("Controle de Terrenos")
print("===" * 20)
l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
area(l, c)