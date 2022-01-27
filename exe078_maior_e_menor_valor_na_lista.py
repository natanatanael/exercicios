listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input("Digite um valor: ")))
    if c == 0:
        mai = men = listanum[c]
    elif listanum[c] > mai:
        mai = listanum[c]
    elif listanum[c] < men:
        men = listanum[c]
print(mai)
print(men)
print(f"Você digitou os valores: {listanum}")
print(f"O maior valor informado foi {mai} nas posições ", end=" ")
for i, v in enumerate(listanum):
    if v == mai:
        print(f"{i}")
print(f"O menor valor informado foi {men} nas posições ", end=" ")
for i, v in enumerate(listanum):
    if v == men:
        print(f"{i}")



