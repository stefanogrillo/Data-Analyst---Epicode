# Ask for the 3 inputs
a = int(input("Inserisci a:"))
b = int(input("Inserisci b:"))
c = int(input("Inserisci c:"))

# IF-statements
if a > b:
    if a > c:
        print("Il massimo è ",a)
else:
    if b > c:
        print("Il massimo è ",b)
    else:
        print("Il massimo è ",c)
