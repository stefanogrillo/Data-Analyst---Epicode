stringa = str(input("Quale frase vediamo oggi? ")).upper()
# Trova solo le vocali e rimpiazzale in vocali minuscole
stringanuova = stringa.replace('A', 'a').replace('E', 'e').replace('I','i').replace('O','o').replace('U','u')
print(stringanuova)