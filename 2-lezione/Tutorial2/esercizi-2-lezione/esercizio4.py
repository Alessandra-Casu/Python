# Prendere in input base e altezza di un rettangolo.
# Successivamente verificare se entrambe le misure sono positive
# Se sia la base che l'altezza sono positivi, calcolare l'area

base = float(input("Inserisci la base del rettangolo: "))
altezza = float(input("Inserisci l'altezza' del rettangolo: "))

if base >= 0 and altezza >= 0:
    area = base * altezza
    print("Area calcolata = ", area)
else:
    print("Attenzione sia la base che l'altezza devono essere positivi")
