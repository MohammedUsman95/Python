import numpy as num

data1 = [62, 87, 71, 94, 56, 83, 69, 77, 91, 64]
data2 = [38, 47, 55, 42, 60, 35, 49, 53, 44, 51]

marks = num.array(data1)
average_marks = num.mean(marks)
max_marks = num.max(marks)
min_marks = num.min(marks)

print("Marks =", marks)
print("Average Marks =", average_marks)
print("Highest Marks Scored =", max_marks)
print("Lowest Marks Scored =", min_marks)

numbers = num.array([10,20,40,100])
print(numbers * 4)
print(numbers + 10)
