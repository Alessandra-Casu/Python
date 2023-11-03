# Si desidera verificare se un numero inserito in input è un multiplo di 7.
# Se il numero è effettivamente multiplo di 7, stampare un messaggio che lo conferma.
# In caso contrario, stampare un messaggio diverso

numero = int(input("Inserire il numero da verificare: "))
if numero % 7 == 0:
    print(f"{numero} è multiplo di 7")
else:
    print(f"Spiacenti, {numero} non è multiplo di 7")
