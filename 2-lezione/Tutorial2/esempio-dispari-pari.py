# realizziamo un algoritmo che prende in input un numero n e
# controlla se il resto della divisione di n per 2 è uguale a zero

# SE il resto è 0, la condizione è vera e stampa a video che il numero è pari
# ALTRIMENTI la condizione è falsa e stampa a video che il numero è dispari

# 8 % 2 fa 4 resto 0 dunque è pari
# 7 % 2 fa 3 resto 1 dunque è dispari


n = int(input("Inserisci il tuo numero: "))

if n % 2 == 0:
    print((f"Il numero {n} è pari."))
else:
    print(f"Il numero {n} è dispari.")
