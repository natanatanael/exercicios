r1 = float(input("Informe o comprimento da reta 1: "))
r2 = float(input("Informe o comprimento da reta 2: "))
r3 = float(input("Informe o comprimento da reta 3: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Sim. Essas 3 retas podem formar um triângulo.")
else:
    print("Não. Essas 3 retas não podem formar um triângulo")




