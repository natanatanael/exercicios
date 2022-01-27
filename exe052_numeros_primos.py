num = int(input("Informe um número para descobrir se ele é um NÚMERO PRIMO: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(c), end=" ")
print("\n\033[mO número {} foi divisível {} vezes.".format(num, tot))
if tot == 2:
    print("\033[33mELE É PRIMO")
else:
    print("\033[31mELE NÃO É PRIMO")


