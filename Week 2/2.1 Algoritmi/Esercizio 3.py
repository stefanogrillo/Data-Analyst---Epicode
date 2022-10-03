def main():
    # Check if input value is a positive integer   
    while True:
        a = float(input("Base: "))
        if a < 0:
            print("NOoO")
            continue
        elif a != int(a):
            print("NO")
            continue
        else:
            break

    # Check if input value is a positive integer
    while True:
        b = float(input("Power: "))
        if b < 0:
            print("NOoO")
            continue
        elif b != int(b):
            print("NO")
            continue
        else:
            break
            
    # Create a Power Function, step by step
    i = 0
    p = 1
    while i < b:
        p = p * a
        i += 1

    print(p)
main()
