# Calcolare il fattoriale di un numero

# n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
# 4! = 4 * 3 * 2 * 1 = 24
# 0! = 1 per convenzione

numero = int(input("Inserisci un numero intero positivo: "))
fattoriale = 1

for i in range(1, numero + 1):
    fattoriale *= i

print(f"Il fattoriale è: {fattoriale}")
