# Exercise 1

students = ("student1","student2","student3","student4","student5",)

for student in students:
    print(student)

# Exercise 2

total = 0
marks = (70,80,65,90,85)
for mark in marks:
    total += mark
    average = total / len(marks)

print("Total =",total)
print("Average =",average)

# Exercise 3

numbers = (45, 12, 78, 34, 91, 23)
largest_num = max(numbers)
smallest_num = min(numbers)

print("Largest Number =",largest_num)
print("Smallest Number =",smallest_num)

# Exercise 4

numbers = (10, 20, 10, 30, 10, 40, 10, 20, 10, 30, 10, 40, 10, 20, 10, 30, 10, 40,)
print("Numbers =",numbers)
counted_number = int(input("Tell The Number You Want To Count From The Tuple: "))
counting = numbers.count(counted_number)
print("Amount Of",counted_number,"In The Tuple =",counting)