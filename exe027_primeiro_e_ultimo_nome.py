nome = str(input("Digite seu nome completo: ")).upper().strip()
dividido = nome.split()
print("Seu primeiro nome é {}.".format(dividido[0]))
print("Seu último nome é {}.".format(dividido[len(dividido)-1]))




