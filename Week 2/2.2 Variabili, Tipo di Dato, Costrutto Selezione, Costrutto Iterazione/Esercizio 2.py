import random

persona = [0, 0]
# Lista di numeri da 1 a 10 da cui scegliere a random
list1 = range(0, 10)
# Aggiungiamo un po' di randomness
list2 = [0,1]
list3 = [0,1]
# Passi casuali da 1 a 10; direzioni: Nord, Est == +; Sud, Ovest == -; ripeti 100 volte 10 passi
# Sergio Cristiano ed io vogliamo considerare 4 casi: random positivo-positivo, random negativo-negativo, e i due casi misti
# Primo if-statement: pos-pos, pos-neg;
# Secondo if-statement: neg-pos, neg-neg;
i = 0
while i < 100:
    # Primo random positivo
    if random.choice(list2) == 0:
        persona[0] = persona[0] + random.choice(list1)
        # Secondo random positivo
        if random.choice(list3) == 0:
            persona[1] = persona[1] + (10 - abs(random.choice(list1)))
        # Secondo random negativo
        else:
            persona[1] = persona[1] - (10 - abs(random.choice(list1)))
    # Primo random negativo
    else:
        persona[0] = persona[0] - random.choice(list1)
        # Secondo random positivo
        if random.choice(list3) == 0:
            persona[1] = persona[1] - (10 - abs(random.choice(list1)))
        # Secondo random negativo
        else:
            persona[1] = persona[1] + (10 - abs(random.choice(list1)))
    i += 1
print(persona)