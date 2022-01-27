print("-=-" * 20)
print("Simulação de Crédito Imobiliário")
print("-=-" * 20)
valorcasa = float(input("Informe o valor do imóvel: R$ "))
salario = float(input("Qual o salário do comprador? R$ "))
tempo = int(input("Em quantos anos será realizado o pagamento? "))
anos = tempo * 12
margem = (valorcasa / anos / salario) * 100
parcela = valorcasa / anos
print("Para pagar um imóvel de R${:.2f} em {} anos, a prestação mensal será de R${:.2f}".format(valorcasa, tempo, parcela))
if margem <= 30:
    print("Parabéns! Seu empréstimo foi aprovado.")
else:
    print("Infelizmente seu empréstimo foi negado.")
print("Agrademos pela confiança!")