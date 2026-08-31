# Exercise 1

student = {
    "Name": "Usman",
    "Age": 15,
    "Course": "Python Programming",
    "City": "Bhatkal" 
}

print(student.values())

# Exercise 2

product = {
    "Title": "Lenovo Laptop",
    "Price": 50000,
    "Quantity": 2
}

for key, value in product.items():
    print(key, "=", value)

total_cost = product["Price"] * product["Quantity"]
print("Total Cost =", total_cost)

# Exercise 3

employee = {
    "Name": "John",
    "Department": "Software Engineering",
    "Salary": 40000
}

for key, value in employee.items():
    print(key, "=", value)

# Exercise 4

student = {
    "name": "Ahmed",
    "english": 75,
    "maths": 85,
    "science": 80
}

for key, value in student.items():
    print(key, "=", value)

total_marks = student["english"] + student["maths"] + student["science"] 
average = total_marks / 3

print("Total Marks =",total_marks)
print("Average Marks =",average)

if total_marks >= 90:
    print(student["name"], "- Pass")
else:
    print(student["name"], "- Fail")

# Exercise 5

students = [
    {"Name": "Steve", "Marks": "90"},
    {"Name": "John", "Marks": "80"},
    {"Name": "Usman", "Marks": "100"}
]

for student in students:
    print("Name =", student["Name"])
    print("Marks =", student["Marks"])
    print()
