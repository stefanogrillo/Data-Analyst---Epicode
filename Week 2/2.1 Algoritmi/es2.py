n = int(input("Inserisci quanti numeri vuoi: "))
MAX = int(input("Inserisci il primo numero: "))

i = 0
while i < n - 1:
    m = int(input("Inserisci un altro numero: "))
    if MAX < m:
        MAX = m
    i +=1
print(MAX)