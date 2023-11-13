# Inserire N numeri e
# contare quanti numeri pari e dispari sono stati chiesti

n = int(input("Inserisci il numero di elementi: "))
cont_pari = 0
cont_dispari = 0

while n <= 0:
    n = int(input("Inserisci il numero di elementi: "))

for _ in range(n):
    numero = int(input("Inserisci un numero:"))
    # se_vero if codizione else se_falso
    if numero % 2 != 0:
        cont_dispari += 1
    else:
        cont_pari += 1

print(f" Sono stati inseriti {cont_dispari} numeri dipari e {cont_pari} numeri pari")
