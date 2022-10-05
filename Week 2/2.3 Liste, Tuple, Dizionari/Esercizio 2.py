continuare = True
# Creiamo una matrice con schema "nomi", "ammontare"
lista = [[], []]

# Chiedi il nome del cliente e l'ammontare della spesa, inseriscile in due liste apposite, chiedi se si vuole continuare
while continuare == True:
    lista[0].append(input("Nome del cliente "))
    lista[1].append(float(input("Ammontare spesa del cliente ")))
    # Per uscire dal ciclo
    continuare = bool(int(input("Vuoi continuare? Sì = 1; No = 0 ")))

# Trova la spesa massima e il nome del cliente corrispettivo
indice_max = lista[1].index(max(lista[1]))
print("Il nome del cliente che ha speso di più è {} per un valore di {} €".format(lista[0][indice_max], lista[1][indice_max]))

# Trova la spesa minima e il nome del cliente corrispettivo
indice_min = lista[1].index(min(lista[1]))
print("Il nome del cliente che ha speso di più è {} per un valore di {} €".format(lista[0][indice_min], lista[1][indice_min]))

# Calcola la media di tutte le spese
print("La media è ", sum(lista[1]) / len(lista[1]))

