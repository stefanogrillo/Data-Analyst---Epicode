def main():
    # Check if input value is a positive integer   
    while True:
        a = float(input("Base: "))
        if a < 0:
            print("NO")
            continue
        elif a != int(a):
            print("NOO")
            continue
        else:
            break

    # Check if input value is a positive integer
    while True:
        b = float(input("Power: "))
        if b < 0:
            print("NO")
            continue
        elif b != int(b):
            print("NOO")
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
