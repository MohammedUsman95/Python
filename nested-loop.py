# Nested Loop Test

# for i in range(1,4):
#     print("--- OuterLoop ---", i)
#     for j in range(1,4):
#         print("InnerLoop", j)


# Square Shape

# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()

# Number loop 1

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

# Number loop 2

# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()

# Tables

# n = int(input("Enter a Number: "))

# for i in range(1, n + 1):
#     print("----- Printing Table Of", i, "-----")
#     for j in range(1,11):
#         print(i, "X", j, "=", j * i)

# Number Triangle

for i in range(1,6):
    for j in range(i):
        print(j + 1, end=" ")
    print()