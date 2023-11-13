# Un numero primo è
# un numero maggiore di 1 che ha esattamente due divisori positivi:
# 1 e se stesso
# 2
# 3
# 5
# 7

# n = int(input("Inserisci un numero maggiore di 1: "))

# count = 0
# div = 2

# while div <= n // 2 and count == 0:
#     if n % div == 0:
#         count += 1
#     div += 1

# if count == 0:
#     risultato = "è un numero primo"
# else:
#     risultato = "NON è un numero primo"

# print(f"{n} {risultato}")

from sympy import isprime

numero = int(input("Inserisci un numero maggiore di 1: "))

if isprime(numero):
    print(f"{numero} è un numero primo")
else:
    print(f"{numero} NON è un numero primo")
