from datetime import datetime
trabalho = {}
trabalho["nome"] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
trabalho["idade"] = datetime.now().year - nasc
trabalho["carteira"] = int(input("N° da Carteira de Trabalho (0 se não tem): "))
print("=" * 30)
for k, v in trabalho.items():
    print(f" - {k} tem o valor {v}")
if trabalho["carteira"] != 0:
    trabalho["contratação"] = int(input("Ano de contratação: "))
    trabalho["salario"] = float(input("Salário: "))
    trabalho["aposentadoria"] = trabalho["idade"] + ((trabalho["contratação"] + 35) - datetime.now().year)
    for k, v in trabalho.items():
        print(f" - {k} tem o valor {v}")
else:
    print("FIM")
