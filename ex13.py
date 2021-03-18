import math
num = int(input("Fill your number : "))
root2 = math.sqrt(num)
print (root2)

if root2%1 == 0:
    print("Yes, It's integer")
else:
    print("No,It isn't integer")

