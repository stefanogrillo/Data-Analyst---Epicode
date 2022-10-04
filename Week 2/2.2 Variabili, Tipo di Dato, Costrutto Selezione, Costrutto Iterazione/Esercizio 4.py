metri = float(input("Quanti metri vuoi convertire in miglia, piedi, pollici?"))

miglia = metri * 0.00062137
pollici = metri * 39.370
piedi = metri * 3.2808

print("I " + str(metri) + " metri equivale a " + str(miglia) + " miglia, oppure a " + str(piedi) + " piedi, e a " +
      str(pollici) + " pollici")
