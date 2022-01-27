classificação = ("Bragantino", "Athletico-PR", "Palmeiras", "Fortaleza,", "Atlético-MG",
                 "Flamengo", "Santos", "Juventude", "Bahia", "Atlético-GO",
                 "Corinthians", "Ceará", "Fluminense", "Internacional", "Sport",
                 "América-MG", "São Paulo", "Cuiabá", "Chapecoense", "Grêmio")
print("-=-"*30)
print(f"Lista de times do Brasileirão 2021: {classificação}")
print("-=-"*30)
print(f"Os 5 primeiros colocados são {classificação[0:5]}")
print("-=-"*30)
print(f"Os 4 últimos são {classificação[-4:]}")
print("-=-"*30)
print(f"Times em ordem alfabética: {sorted(classificação)}")
print("-=-"*30)
print(f"Chapecoense está na {classificação.index('Chapecoense') + 1}ª posição")

# for c in classificação:
#   print(c)

