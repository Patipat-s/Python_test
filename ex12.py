num = int(input("Fill number : "))

if num == 0:
    print("zero")
else:
    if num > 0:
        if num%2 == 0:
            print("Positive Even")
        else:
            print("Positive Odd")
    elif num < 0:
        if num%2 == 0:
            print("Negative Even")
        else:
            print("Negative Odd")
