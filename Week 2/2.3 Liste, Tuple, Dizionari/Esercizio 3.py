# Dizionari
multiset1 = {'banane': 2, 'mele': 3, 'birra': 2, 'capperi': 2, 'olio': 3}
multiset2 = {'banane': 5, 'birra': 3, 'origano': 1, 'capperi': 2}

# Crea un dizionario che contenga tutte le chiavi
new_multiset = dict.fromkeys(list(multiset1) + list(multiset2))
# print("new_multiset è", new_multiset)

# Unisci i dizionari, sommando le frequenze
unione = new_multiset
for k in new_multiset:
    if k in multiset1:
        unione[k] = multiset1[k]
    if k in multiset2 and unione.get(k, None) != None:
        unione[k] += multiset2[k]
    if k in multiset2 and unione.get(k, None) == None:
        unione[k] = multiset2[k]
print("unione è", unione)

# Interseziona i dizionari, ossia crea un dizionario che contenga solo la frequenza minima di ogni key
intersezione = new_multiset
for k in new_multiset:
    if k in multiset1 and k in multiset2:
        # Se la frequenza minima è nel primo dizionario
        if multiset1[k] < multiset2[k]:
            intersezione[k] = multiset1[k]
        else:
            intersezione[k] = multiset2[k]
    elif multiset2.get(k, None) is not None:
        intersezione[k] = multiset2[k]
    else:
        intersezione[k] = multiset1[k]
print("intersezione è", intersezione)

# Differenza tra le frequenze, non minore di zero
differenza = new_multiset
for k in new_multiset:
    # Si può usare anche "multiset1.get(k, None) is not None and multiset2.get(k, None) is not None:"
    if k in multiset1 and k in multiset2:
        differenza[k] = abs(multiset1[k] - multiset2[k])
    elif multiset2.get(k, None) is not None:
        differenza[k] = multiset2[k]
    else:
        differenza[k] = multiset1[k]
print("differenza è", differenza)
