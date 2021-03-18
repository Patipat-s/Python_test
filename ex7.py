num = int(input("Insert Score : "))
if num < 0:
    print("Please insert the number that is greater or equal zero")
else:
    if num >= 80:
        print('A')
    elif num >= 70 and num < 80:
        print('B')
    elif num >= 60 and num < 70:
        print('C')
    elif num >= 50 and num < 60:
        print('D')
    else:
        print('F')
