quant = soma = 0
while True:
    num = int(input("Digite um número [999 para parar]: "))
    if num == 999:
        break
    quant += 1
    soma += num
print(f"Foram informados {quant} e a soma deles é {soma}")
