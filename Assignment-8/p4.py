n = int(input("Enter a Number: "))

def calculate_sum(n):
    number = 0
    for number in range(n-1):
        number += 1
        n = n + number
    print("Sum =",n)

calculate_sum(n)