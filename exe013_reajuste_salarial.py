salario = float(input('Informe seu salário atual: R$ '))
aumento = salario / 100 *15
novo = salario + aumento
print('Parabéns! Você recebeu {:.2f} de aumento salarial. Seu novo salário será {:.2f}'.format(aumento, novo))


