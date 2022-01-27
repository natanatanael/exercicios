import math
angulo = float(input("Informe um ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("Seno de {}º = {:.3f}".format(angulo, seno))
print("Cosseno de {}º = {:.3f}".format(angulo, cosseno))
print("Tangente de {}º = {:.3f}".format(angulo, tangente))
