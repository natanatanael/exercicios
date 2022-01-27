num = int(input("Digite um número: "))
for c in range(1, 11):
    print("{} x {} = {}".format(num, c, num*c))


number = int(input("Informe um número: "))
zero = - 1
for c in range(11):
    zero = zero + 1
    multi = number * zero
    print("{} x {} = {}".format(number, zero, multi))