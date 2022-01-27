preco = float(input('Informe o preço do produto: R$ '))
desconto = preco / 100 * 5
final = preco - desconto
print('Você ganhou {:.2f} de desconto. O produto será vendido por {:.2f}'.format(desconto, final))



