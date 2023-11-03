# Convertire un punteggio numerico in una valutazione.
# A, B, C, D, E, F
# corrispondono a 10, 9, 8, 7, 6, 5 rispettivamente

voto = int(input("Inserisci il tuo voto (5 < voto < 10): "))

if voto == 10:
    print(f"Hai inserito {voto}; la tua valutazione è A")
elif voto == 9:
    print(f"Hai inserito {voto}; la tua valutazione è B")
elif voto == 8:
    print(f"Hai inserito {voto}; la tua valutazione è C")
elif voto == 7:
    print(f"Hai inserito {voto}; la tua valutazione è D")
elif voto == 6:
    print(f"Hai inserito {voto}; la tua valutazione è E")
elif voto == 5:
    print(f"Hai inserito {voto}; la tua valutazione è F")
else:
    print("Il voto inserito non è corretto.")
