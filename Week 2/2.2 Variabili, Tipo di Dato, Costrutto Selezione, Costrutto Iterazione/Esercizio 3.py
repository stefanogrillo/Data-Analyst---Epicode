litri = float(input("Quanti litri hai nel serbatoio?"))
km_l = float(input("Quanti km/l fa la tua macchina?"))
prezzo_l = float(input("Quanto costa la benzina per litro?"))

print("100 km ti costano ", 100/km_l*prezzo_l)
print("Con i " + str(litri) + " L di serbatoio, puoi percorrere " + str(litri*km_l) + " km")