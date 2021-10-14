"""distancia = float(input("Qual a distância do local de destino (km): "))
preco1 = distancia * 0.50
preco2 = distancia * 0.45
if distancia <= 200:
    print("Você percorrerá {} km de distância e a sua viagem custará R${:.2f}.".format(distancia, preco1))
else:
    print("Você percorrerá {} km de distância e a sua viagem custará R${:.2f}.".format(distancia, preco2))"""

distancia = float(input("Qual a distância do local de destino (km): "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print("Você percorrerá {} km de distância e a sua viagem custará R${:.2f}.".format(distancia, preco))

