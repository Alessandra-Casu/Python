# Trova il massimo di N numeri

N = int(input("Inserisci il numero di elementi: "))

if N < 2:
    print("Inserisci almeno due numeri!")
else:
    massimo = float(input("Inserisci il primo numero: "))
    for _ in range(N - 1):
        numero = float(input("Inserisci un altro numero: "))
        if numero > massimo:
            massimo = numero

print(f"Il valore massimo tra i numeri inseriti è: {massimo}")
