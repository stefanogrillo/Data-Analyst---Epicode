# Chiediamo un input all'utente
stringa = input("Quale frase vediamo oggi? ").upper()
# Trova solo le vocali e rimpiazzale in vocali minuscole
stringanuova = stringa.replace('A', 'a').replace('E', 'e').replace('I','i').replace('O','o').replace('U','u')

l = stringanuova.split(' ')

# Creiamo il dizionario di tuple, dove ad ogni key corrisponde una tuple di parole che contengono quella key
# [elem for elem in l if 'a' in elem] è una List Comprehension, che significa:
# Per ogni elemento della lista l, se la vocale è presente nell'elemento, aggiungi l'elemento alla lista
d = {'a': tuple([elem for elem in l if 'a' in elem]),
     'e': tuple([elem for elem in l if 'e' in elem]),
     'i': tuple([elem for elem in l if 'i' in elem]),
     'o': tuple([elem for elem in l if 'o' in elem]),
     'u': tuple([elem for elem in l if 'u' in elem])}

print(d)
