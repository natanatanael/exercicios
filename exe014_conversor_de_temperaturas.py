cels = float(input("Quantos graus ºC? "))
fahrenheit = cels * 1.8 + 32
print("Isso corresponde a {} graus fahrenheit".format(fahrenheit))
fahr = float(input("Quantos graus fahrenheit? "))
celsius = (fahr - 32) / 1.8
print("Isso corresponde a {:.2f} graus celsius".format(celsius))

