# Calcola la somma dei primi N numeri naturali
# N = 3
# somma = 1 + 2+ 3 = 6

# N = 10  # Inizializzazione
# somma = 0  # variabile che accumulerà la somma, inizializz a 0 in quanto elemento neutro della somma

# for n in range(1, N + 1):
#     somma += n

# print(f"La somma dei primi {N} numeri naturali è: {somma} !")


# Lo stesso algoritmo si può risolvere:
N = 10
somma = (N * (N + 1)) // 2  # formula per la somma di una progressione automatica
print(f"La somma dei primi {N} numeri naturali è: {somma} !")
