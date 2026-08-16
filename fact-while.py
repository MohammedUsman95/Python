n = int(input("Enter a Number: "))
fact = 1

i = 1
while i <=n :
    fact = fact * i
    print("fact now = ", fact)
    i = i + 1


print("Factorial of",n,"=", fact)
