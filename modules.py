# Excercise 1

from math import sqrt

n = int(input("Enter a number: "))
print("Square Root =", sqrt(n))

# Excercise 2

from math import pi

r = int(input("Enter radius: "))
area = pi * r * r
print("Area =", area)

# Exercise 3

import random

random_num = random.randint(1,100)
print("Random Number =", random_num)

# Exercise 4

import random

students = [
    "Alex",
    "Beatrix",
    "Charlie",
    "David",
    "Emma",
    "Fiona",
    "Gabriel",
    "Hannah",
    "Ian",
    "Julia"
]

random_student = random.choice(students)
print("Student =", random_student)

# Excercise 5

import datetime

current_date = datetime.date.today()
print("Date =", current_date)