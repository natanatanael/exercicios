from datetime import date

# Perguntar o sexo antes de seguir

# """print("""Por gentileza, informe o seu sexo:
# [ 1 ] Masculino
# [ 2 ] Feminino """)
# sexo = int(input("Informe aqui:"))
# if sexo == 1:
#   print("Veja abaixo as informações sobre seu alistamento militar:")
# elif sexo == 2:
#   print("Você não precisa realizar o alistamento militar")
# else:
#   print("Opção inválida. Tente novamente.")"""

nascimento = int(input("Informe o ano de nascimento: "))
idade = date.today().year - nascimento
if idade > 18:
    print("""Você está com {} anos e deveria ter se alistado {} anos atrás, quando tinha 18 anos. 
Procure um posto da PF para se regularizar.""".format(idade, (idade - 18)))
elif idade < 18:
    print("""Você está com {} anos e precisará se alistar em {} anos, 
quando completar 18 anos.""".format(idade, (18 - idade)))
else:
    print("Você está com {} anos e deverá se alistar IMEDIATAMENTE".format(idade))
