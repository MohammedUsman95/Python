num1 = int(input("Enter Your First Number: "))

num2 = int(input("Enter Your Second Number: "))

num3 = int(input("Enter Your Third Number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest Number =", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest Number =", num2)
else:
    print("Largest Number =", num3)