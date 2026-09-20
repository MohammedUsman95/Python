# Example 1

try:
    x = int(input("Enter A Number: "))
    y = int(input("Enter A Number: "))
    result = x/y
    print("Result =", result)
except:
    print("You have submitted a incorrect number")

# Example 2

try:
    x = int(input("Enter A Number: "))
    y = int(input("Enter A Number: "))
    result = x/y
    print("Result =", result)
except ValueError:
    print("Only use whole numbers")
except ZeroDivisionError:
    print("Dont input number zero(0) in y, only use whole numbers")