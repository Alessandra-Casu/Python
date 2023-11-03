# Prendiamo in input l'anno
# dopo verifichiamo:
# se l'anno è divisibile per 4, ma non è divisibile per 100, oppure
# se l'anno è divisibile per 400

anno = int(input("Inserisci l'anno da controllare: "))

if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
    print(f"{anno} è un anno bisestile")
else:
    print(f"{anno} NON è un anno bisestile")
