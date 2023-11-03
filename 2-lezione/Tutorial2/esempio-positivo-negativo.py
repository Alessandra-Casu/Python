# prendiamo un numero n in input e ne valutiamo la positività, la netraulità o la negatività
# stampiamo poi un messaggio appropriato in base a verificarsi o no delle condizioni

n = int(input("Inserisci un numero intero: "))

if n > 0:
    print(f"Il numero {n} è positivo.")
elif n == 0:
    print(f"Il numero {n} è nullo.")
else:
    print(f"Il numero {n} è negativo.")
