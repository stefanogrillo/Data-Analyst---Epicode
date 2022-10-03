def main():
    # Check if first number is a positive integer
    while True:
        a = float(input("First: "))
        if a < 0:
            print("NOoO")
            continue
        elif a != int(a):
            print("NO")
            continue
        else:
            break

    # Check if second number is a positive integer and is bigger than the first number
    while True:
        b = float(input("Second: "))
        if b < 0:
            print("NOoO")
            continue
        elif b != int(b):
            print("NO")
            continue
        elif b <= a:
            print("no")
            continue
        else:
            break

    # Print the integers between Second and First
    # To exclude Second and First from the printed list:
    # 1: To exclude the Second, use: "while i < difference - 1"
    # 2: To exclude the First, use: "decrescent = b - i - 1"
    difference = b - a
    i = 0
    while i <= difference:
        decrescent = b - i
        print(decrescent)
        i += 1

main()
