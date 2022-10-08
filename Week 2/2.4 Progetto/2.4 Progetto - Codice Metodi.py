def selected_country_variables(original, indice1, valore1, indice2, valore2, listae):
    """
    Legge una lista di liste e crea una nuova lista di liste con solo le righe selezionate
    :param original: lista di liste di origine
    :param indice1: indice nella lista di liste di origine dove controllare per un valore
    :param valore1: valore nella lista di liste di origine in posizione indice
    :param indice2: indice nella lista di liste di origine dove controllare per un valore
    :param valore2: valore nella lista di liste di origine in posizione indice
    :param lista: lista con gli indici delle colonne che vogliamo estrarre
    :return: lista di liste
    """
    country = []
    for i in range(0, (len(original))):
        valori1 = original[i][int(indice1)]
        valori2 = original[i][int(indice2)]
        # Se il valore del indice scelto è quello che voglio
        if valori1 == str(valore1) and valori2 in valore2:
            riga = []
            country.append(riga)
            # Allora aggiungi dalla riga corrispondente solo i valori degli indici scelti in "listae"
            for j in listae:
                riga.append(original[i][j])
    return country


def inhabitants(original):
    """
    Legge una lista di liste e restituisce il numero di abitanti per regione; avviene dopo la preselezione del metodo
    "selected_country_variables", quindi va eseguita sugli indici specifici location (1) e population (6)
    :param original: lista di liste di origine
    :return: stampa del numero di abitanti
    """
    nations_in_region = []
    for i in range(0, len(original)):
        nations_in_region.append((original[i][1], original[i][6]))

    # Voglio recuperare solo i valori univoci dei Paesi e sommarne le Popolazioni
    set_nations_in_region = set(nations_in_region)
    sum_set = [float(t[1]) for t in set_nations_in_region]

    return sum(sum_set)


def new_daily(original, indice):
    """
    Legge una lista di liste e restituisce il numero di nuovi casi
    :param original: lista di liste di origine
    :param indice: indice nella lista di liste di cosa vogliamo ottenere (X)
    :return: lista dei valori di X; somma totale di X; somma valori mancanti
    """
    cases = []
    counter = 0
    for i in range(0,len(original)):
        # Voglio contare solo i valori non vuoti
        if original[i][int(indice)] != '':
            cases.append(float(original[i][int(indice)]))
        else:
            counter += 1

    total = int(sum(cases))

    return cases, total, int(counter)


def new_date(original, indice):
    """
    Legge una lista di liste e restituisce una lista di date (in formato data)
    :param original: lista di liste di origine
    :param indice: indice nella lista di liste di cosa vogliamo ottenere (X)
    :return: lista dei valori di X; somma valori mancanti
    """
    cases = []
    counter = 0
    for i in range(0, len(original)):
        # Voglio contare solo i valori non vuoti
        if original[i][int(indice)] != '':
            cases.append(original[i][int(indice)])
        else:
            counter += 1

    return cases, int(counter)


def first_case(original):
    """
    Legge una lista di liste e restituisce il valore minimo
    :param original: lista di liste di origine
    :return: prima data
    """
    min_date = []
    for i in range(0,len(original)):
        min_date.append(original[i][1])

    return min(min_date)
