# Prendiamo in input il prezzo di un prodotto e se è superiore a 100$
# effettuiamo uno sconto del 10%,
# altrimenti se è compreso tra 50$ e 100$ effettuiamo uno sconto del 5%,
# altrimenti non facciamo lo sconto

prezzo = float(input("Inserisci il tuo prezzo: "))

if prezzo > 100:
    sconto = prezzo * 0.10
elif 50 < prezzo < 100:
    sconto = prezzo * 0.05
else:
    sconto = 0

importo_scontato = prezzo - sconto

print(f"Importo totale scontato: $ {importo_scontato:.2f}")
