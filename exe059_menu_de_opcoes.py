from time import sleep
valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    print("     [ 1 ] SOMAR")
    print("     [ 2 ] MULTIPLICAR")
    print("     [ 3 ] MAIOR")
    print("     [ 4 ] NOVOS NÚMEROS")
    print("     [ 5 ] SAIR DO PROGRAMA")
    opcao = int(input("Qual é a sua opção? "))
    if opcao == 1:
        soma = valor1 + valor2
        print("A soma entre {} e {} é [{}]".format(valor1, valor2, soma))
    elif opcao == 2:
        multiplicar = valor1 * valor2
        print("A multiplicação entre {} e {} é [{}]".format(valor1, valor2, multiplicar))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
            print("O maior valor entre {} e {} é [{}]".format(valor1, valor2, maior))
        elif valor2 > valor1:
            maior = valor2
            print("O maior valor entre {} e {} é [{}]".format(valor1, valor2, maior))
        else:
            print("O dois valores são iguais")
    elif opcao == 4:
        print("Informe os valores novamente")
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
        sleep(2)
    else:
        print("Opção inválida. Tente novamente.")
print("Fim do programa")





