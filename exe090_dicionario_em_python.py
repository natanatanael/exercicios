"""
aluno = {}
situacao = {}
aluno["nome"] = str(input("Nome: "))
aluno["média"] = float(input(f"Média de {aluno['nome']}: "))
situacao['aprovado'] = aluno["média"] >= 6
situacao['recuperação'] = aluno["média"] < 6
print("-=" * 30)
print(f"- Nome é igual a {aluno['nome']}")
print(f"- Média é igual a {aluno['média']}")
if situacao['aprovado']:
    print(f"- Situação é igual a Aprovado")
else:
    print(f"- Situação é igual a Recuperação")"""


aluno = {}
situacao = {}
aluno["nome"] = str(input("Nome: "))
aluno["média"] = float(input(f"Média de {aluno['nome']}: "))
if aluno["média"] >= 7:
    aluno["situacao"] = "Aprovado"
elif 5 < aluno["média"] < 7:
    aluno["situacao"] = "Recuperação"
else:
    aluno["situacao"] = "Reprovado"
for k, v in aluno.items():
    print(f"{k} é igual a {v}")




