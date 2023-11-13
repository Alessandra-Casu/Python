# Scrivere un programma che verifica se la stringa è palindorma

word = input("Scrivi una parola: ")
if str(word) == "".join(reversed(word)):
    print(f"{word} è una parola palidroma {word[::-1]}")
else:
    print(f"{word} non è una parola palidroma {word[::-1]}")
