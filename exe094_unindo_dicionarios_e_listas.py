from statistics import mean
galera = []
idade = []
dados = {}
mulheres = []
media = []
acima = []
while True:
    dados.clear()
    dados["nome"] = str(input("Nome: "))
    while True:
        dados["sexo"] = str(input("Sexo [M/F]: ")).upper().strip()[0]
        if dados["sexo"] in "F":
            mulheres.append(dados["nome"])
        if dados["sexo"] in "MF":
            break
        print("ERRO! Por favor, digite apenas M ou F")
    dados["idade"] = int(input("Idade: "))
    idade.append(dados["idade"])
    galera.append(dados.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if resp in "SN":
            break
        print("ERRO! Responda S ou N")
    if resp == "N":
        break
media = sum(idade) / len(idade)
print("=" * 30)
print(galera)
print("=" * 30)
print(f"Foram cadastradas {len(galera)} pessoas")
print(f"A média de idade de todas as pessoas cadastradas é: {media:5.2f} anos")
print(f"Foram cadastradas {len(mulheres)} mulheres: {mulheres}")
print("Lista das pessoas com idade acima da média: ")
for p in galera:
    if p["idade"] >= media:
        print(f"    ", end=" ")
        for k, v in p.items():
            print(f"{k} = {v}; ", end=" ")
        print()
print("<< ENCERRADO >>")








