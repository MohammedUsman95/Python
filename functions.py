# Print Hello World
def hello():
    print("Hello World!")

hello()
hello()

# Sum
def add(a,b):
    sum = a + b
    print(sum)

a = int(input("Enter A Number: "))
b = int(input("Enter Another Number: "))
add(a,b)

# Square area
def sq_area(s):
    area = s * s
    return area

s = int(input("Enter A Number:"))
area = sq_area(s)
print("Area =", area)

# Tables
def tables(n):
    print("******* Table of",n,"*******")
    for i in range(1,11):
        answer = n * i
        print(n,"X",i,"=",answer)
    print("----------------------------")
    print()

y = int(input("Enter A Number: "))
for n in range(1,y+1):
    tables(n)

# Exercise 4
def c_to_f(C):
    Fahrenheit = (C * 9/5) + 32
    print("Celsius =",C)
    print("Fahrenheit =",Fahrenheit)

C = int(input("Enter Celsius: "))
c_to_f(C)

# Exercise 5
def discount(p,dp):
    d = p * dp / 100
    fp = p - d
    print("Discount =",d)
    print("Final Price =",fp)

p = int(input("Enter The Price: "))
dp = int(input("Enter The Discount Percentage: "))
discount(p,dp)