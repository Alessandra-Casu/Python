# Prendere in input un numero,
# se è multiplo di 3 e di 5 stampa FizzBuzz,
# se è multiplo di 3 stampa Fizz,
# se è multiplo di 5 stampa Buzz,
# altrimenti stampa il numero

numero = int(input("Inserisci un numero intero: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
elif numero % 3 == 0:
    print("Fizz")
elif numero % 5 == 0:
    print("Buzz")
else:
    risultato = numero
