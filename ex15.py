num1 = int(input("Fill num1 : "))
num2 = int(input("Fill num2 : "))

num_sum = num1 + num2

if num_sum > 0:
    if num_sum%2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif num_sum < 0:
    if num_sum%2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")
else:
    print("Zero")