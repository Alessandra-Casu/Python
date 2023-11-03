# Prendere in input username e password e controllare se corrispondono alle credenziali valide per l'accesso

username = "utente123"
password = "passwordSegreta"

input_username = input("Inserisci il nome utente: ")
input_password = input("Inserisci la password: ")

if input_username == username and input_password == password:
    print("Accesso riuscito")
else:
    print("Accesso non riuscito")
    if input_username != username:
        print("Username errato")
    if input_password != password:
        print("Password errata")
