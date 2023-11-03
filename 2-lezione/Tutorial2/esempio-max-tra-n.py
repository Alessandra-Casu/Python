# Prendere in input 3 numeri e stabilire il maggiore

a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))
c = int(input("Inserisci il terzo e ultimo numero: "))

if a >= b and a >= c:
    massimo = a
elif b >= a and b >= c:
    massimo = b
else:
    massimo = c

print(f"Il numero masssimo tra {a}, {b}, {c} è {massimo}.")
