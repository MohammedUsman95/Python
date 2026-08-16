n = int(input("Enter a Number: "))

print("----- Printing Table of", n, "-----")

for i in range(1,11):
    ans = n * i 
    print(n, "x", i, "=", ans)