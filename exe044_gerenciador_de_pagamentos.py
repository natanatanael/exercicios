preco = float(input("Qual o preço do produto? R$ "))
print("""Escolha a forma de pagamento:
[ 1 ] à vista dinheiro/cheque: 10% de desconto
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão: sem juros
[ 4 ] 3x ou mais no cartão: 20% de juros""")
opcao = int(input("Sua escolha: "))
if opcao == 1:
    print("""O pagamento de R$ {} será à vista e terá um desconto de 10% no valor de R$ {}. 
Valor final do produto: R$ {:.2f}""".format(preco, (preco/100*10), (preco - (preco/100*10))))
elif opcao == 2:
    print("""O pagamento de R$ {} será à vista no cartão e terá um desconto de 5% no valor de R$ {}. 
Valor final do produto: R$ {:.2f}""".format(preco, (preco/100*5), (preco - (preco/100*5))))
elif opcao == 3:
    print("""O pagamento de R$ {} será em 2x no cartão e não terá juros. 
2 parcelas de R$ {}. Valor final do produto: R$ {:.2f}""".format(preco, (preco / 2), preco))
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    print("""O pagamento de R$ {} será em {}x de R$ {:.2f}. Valor final do produto: R$ {:.2f}, com 20% de juros."""
          .format(preco, parcelas, ((preco + (preco / 100 * 20)) / parcelas), (preco + (preco / 100 * 20))))
else:
    print("Opção Inválida. Tente novamente.")








