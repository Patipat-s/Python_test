
while True:
    num_inp = int(input("Select Number : "))
    if num_inp >= 0:
        if num_inp >= 50:
            print ('Pass')
            break
        else:
            print('Fail')
            continue
    else:
        print("Please insert the number that is greater or equal zero")
        continue