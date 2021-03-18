import math
def usdMoney(u_money):
    return u_money * 32.80

def income_bank(usd_money):
    return usd_money * (30/100)

user_money = int(input("Fill your money : "))

if user_money > 0:
    print (math.ceil(income_bank(usdMoney(user_money))),"BATH")
else:
    print("You don't have " '"money !"')


