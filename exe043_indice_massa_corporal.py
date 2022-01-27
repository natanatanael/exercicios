peso = float(input("Informe o peso: "))
altura = float(input("Informe a altura: "))
imc = peso / (altura * altura)
print("Seu IMC é {:.1f}".format(imc))
if imc <= 18.5:
        print("IMC abaixo de 18,5: Abaixo do Peso")
elif imc <= 25.0:
        print("IMC entre 18,5 e 25: Peso Ideal")
elif imc <= 30.0:
        print("IMC entre 25 e 30: Sobrepeso")
elif imc <= 40.0:
        print("IMC entre 30 e 40: Obesidade")
else:
        print("IMC acima de 40: Obesidade Mórbida")
