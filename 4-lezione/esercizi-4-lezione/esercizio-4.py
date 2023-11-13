# Date due stringhe valutare qual è più lunga
cont1 = 0
cont2 = 0

stringa1 = input("Inserisci la prima parola: ")
for i in range(len(stringa1)):
    cont1 += 1

stringa2 = input("Inserisci la seconda parola: ")
for i in range(len(stringa2)):
    cont2 += 1

if cont1 > cont2:
    print(f"{stringa1} è la parola più lunga")
else:
    print(f"{stringa2} è la parola più lunga")
