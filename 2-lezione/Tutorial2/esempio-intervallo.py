# Prendiamo in input un numero
# dopo verifica se le condizioni
# numero > 10 e
# numero < 20
# sono entrambe vere

numero = int(input("Inserisci un numero intero: "))

if numero > 10 and numero < 20:
    print(f"{numero} è compreso tra 10 e 20.")
else:
    print("Il numero non è compreso tra 10 e 20.")

# if not(numero > 10 and numero < 20):
#     print(f"{numero} non è compreso tra 10 e 20.")
# else:
#     print("Il numero è compreso tra 10 e 20.")
