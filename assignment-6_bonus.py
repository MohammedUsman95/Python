# <---------- Print Number Of Odd And Even Numbers ---------->

numbers = [12, 17, 20, 25, 32, 41, 50, 63, 70, 81]

even_numbers = []
odd_numbers = []


for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Original List =", numbers)
print()
print("Even Numbers =",even_numbers)
print("Odd Numbers =",odd_numbers)