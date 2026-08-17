# <---------- Print Odd Even Numbers ---------->

numbers = [12, 17, 20, 25, 32, 41, 50, 63, 70, 81]

even_numbers = 0
odd_numbers = 0


for number in numbers:
    if number % 2 == 0:
        even_numbers = even_numbers + 1

    else:
        odd_numbers = odd_numbers + 1

print("Total Even Numbers =",even_numbers)
print("Total Odd Numbers =",odd_numbers)
