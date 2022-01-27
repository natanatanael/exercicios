num = int(input("Digite um número: "))
print("""Escolha a base de conversão: 
[ 1 ] para Binário  
[ 2 ] para Octal 
[ 3 ] para Hexadecimal """)
escolha = int(input("Sua escolha: "))
binario = bin(num)[2:]
octal = oct(num)[2:]
hexadecimal = hex(num)[2:]
if escolha == 1:
    print("O número {} convertido para Binário é {}".format(num, binario))
elif escolha == 2:
    print("O número {} convertido para Octal é {}".format(num, octal))
elif escolha == 3:
    print("O número {} convertido para Hexadecimal é {}".format(num, hexadecimal))
else:
    print("Opção inválida. Tente novamente.")
