from math import hypot
oposto = float(input("Qual o comprimento do cateto oposto? "))
adjacente = float(input("Qual o comprimento do cateto adjacente? "))
hipotenusa = hypot(oposto, adjacente)
print("O comprimento da hipotenusa é {:.2f}".format(hipotenusa))
