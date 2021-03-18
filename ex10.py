def money_us(money):
    return money * 32.5

my_money = float(input("My money : "))

if my_money > 0 :
    print((money_us(my_money)),"BATH")
else:
    print("You don't have money")


