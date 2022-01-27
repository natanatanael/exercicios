from time import sleep

def maior(* num):
    cont = maior = 0
    print("=" * 20)
    print(f"Analisando os valores passados...")
    for valor in num:
        print(f"{valor}", end=" ")
        sleep(0.3)
        if cont == 0:
           maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"\nForam informados {cont} valores.")
    print(f"O maior valor informado foi {maior}.")


maior(2, 5, 4, 6, 8, 1, 3)
maior(5, 8, 7, 9, 0, 3)
maior(5, 2)
