# Scrivere un programma che controlla se una stringa contiene solo numeri
stringa = input("SCrivi qui la tua sequenza di numeri interi:")

if stringa.isdecimal() == True:
    print(f"Perfetto, la tua sequenza è correta: {stringa}")
else:
    print("Errato, ci sono delle lettere nella tua sequenza!")
