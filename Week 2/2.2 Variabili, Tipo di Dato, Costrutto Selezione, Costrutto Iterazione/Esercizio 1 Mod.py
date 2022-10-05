# Chiediamo un input
parole = input("Scrivi una frase ").upper()

# Creiamo una lista vuota dove usare "append()"
parole_nuovo = []

# Iteriamo per ogni lettera nella stringa
# "list(parole)" ci avrebbe dato una lista dei singoli caratteri
for i in parole:
    if i in ['A','E','I','O','U']:
        parole_nuovo.append(i.lower())
    else:
        parole_nuovo.append(i)

string = '' .join(parole_nuovo)

print(string)
