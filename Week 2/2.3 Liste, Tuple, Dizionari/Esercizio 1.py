# Chiediamo un input all'utente
stringa = input("Quale frase vediamo oggi? ").upper()
# Trova solo le vocali e rimpiazzale in vocali minuscole
stringanuova = stringa.replace('A', 'a').replace('E', 'e').replace('I','i').replace('O','o').replace('U','u')

l = stringanuova.split(' ')

# Creiamo i tuple iterando se nella lista l compaiono parole con il valore richiesto (la vocale)
a = tuple([elem for elem in l if 'a' in elem])
e = tuple([elem for elem in l if 'e' in elem])
i = tuple([elem for elem in l if 'i' in elem])
o = tuple([elem for elem in l if 'o' in elem])
u = tuple([elem for elem in l if 'u' in elem])

# Creiamo il dizionario di tuple
dizionario = {'a': a, 'e': e, 'i': i, 'o': o, 'u': u}
print(dizionario)
