count_even = 0
count_odd = 0

for i in range(2,21,2):
    print(i)
    count_even = count_even + 1

for i in range(1,21,2):
    print(i)
    count_odd = count_odd + 1 

print("Even Numbers = ", count_even)
print("Odd Numbers = ", count_odd)