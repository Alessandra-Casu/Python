# Calcola la media di N umeri inseriti da tastiera

N = int(input("Inserisci il numero di elementi: "))

somma = 0

for i in range(N):
    numero = float(input(f"Inserisci il numero {i + 1}: "))
    somma += numero

media = somma / N

print(f"La somma è: {media}")
