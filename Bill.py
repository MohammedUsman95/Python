Units = int(input("Enter Amount Of Electricity Units Used: "))

Rate1 = 5
Rate2 = 7
Rate3 = 10

if Units <= 100:
    Bill = Units * Rate1
elif Units <= 200:
    Bill = (100 * Rate1) + ((Units - 100) * Rate2)
else:
    Bill = (100 * Rate1) + (100 * Rate2) + ((Units - 200) * Rate3)

print("-------Electricity Bill for July 2026-------")
print("Your units consumed:", Units)
print("Your total bill for the month is Rs", Bill)