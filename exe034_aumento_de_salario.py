salario = float(input("Informe o seu salário: R$"))
if salario > 1250:
    aumento = ((salario / 100) * 10)
else:
    aumento = ((salario / 100) * 15)
print("Parabéns, você recebeu um aumento de R${:.2f}".format(aumento))
print("Seu salário era R${:.2f} e passa a ser R${:.2f}".format(salario, (salario + aumento)))
