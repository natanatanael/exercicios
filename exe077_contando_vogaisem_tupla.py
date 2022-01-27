palavras = ("MUSICA", "PIANO", "VIOLONCELLO", "CLARINETE", "VIOLINO", "FLAUTA",
            "SAX", "BATERIA", "BAIXO", "GUITARRA", "TROMPETE", "TROMBONE", "TECLADO")
vogais = ("a", "e", "i", "o", "u")
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos", end=" ")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra.lower(), end=" ")
