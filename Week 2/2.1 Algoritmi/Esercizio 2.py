# Ask for how many numbers we want to check (number of iterations required)
n = int(input("Inserisci quanti numeri vuoi: "))
# Set the first number as the MAX
MAX = int(input("Inserisci il primo numero: "))

# While loop from 0 to n - 1; i increasing every cycle; print MAX
i = 0
while i < n - 1:
    m = int(input("Inserisci un altro numero: "))
    if MAX < m:
        MAX = m
    i +=1
print(MAX)
