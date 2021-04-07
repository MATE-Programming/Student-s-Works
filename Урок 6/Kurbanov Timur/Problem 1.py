while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Not a number", end="\n\n")
    else:
        print("Number")
        break