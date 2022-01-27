velocidade = float(input("Qual a velocidade do carro? "))
limite = 80
multa = 7
if velocidade > limite:
    print("Você foi multado! Sua multa será de {} reais.".format((velocidade - limite) * 7))
print("Tenha uma boa viagem! Dirija com segurança.")
