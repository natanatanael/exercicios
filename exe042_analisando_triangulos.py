r1 = float(input("Informe o comprimento da reta 1: "))
r2 = float(input("Informe o comprimento da reta 2: "))
r3 = float(input("Informe o comprimento da reta 3: "))
equilatero = r1 == r2 and r1 == r3 and r2 == r3
isosceles = (r1 == r2 != r3) or (r1 == r3 != r2) or (r2 == r3 != r1)
escaleno = r1 != r2 and r1 != r3 and r2 != r3
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and equilatero:
    print("Sim. Essas 3 retas podem formar um triângulo EQUILÁTERO.")
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and isosceles:
    print("Sim. Essas 3 retas podem formar um triângulo ISOSCELES.")
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and escaleno:
    print("Sim. Essas 3 retas podem formar um triângulo ESCALENO.")
else:
    print("Não. Essas 3 retas não podem formar um triângulo")
