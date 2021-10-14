from calendar import isleap
from datetime import date
ano = int(input("Qual ano você quer analisar? Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
bissexto = isleap(ano)
if bissexto:
    print("O ano de {} É BISSEXTO".format(ano))
else:
    print("O ano de {} NÃO É BISSEXTO.".format(ano))

