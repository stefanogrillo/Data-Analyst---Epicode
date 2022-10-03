a = int(input("Inserisci a:"))
b = int(input("Inserisci b:"))
c = int(input("Inserisci c:"))

if a > b:
    if a > c:
        print("Il massimo è ",a)
else:
    if b > c:
        print("Il massimo è ",b)
    else:
        print("Il massimo è ",c)