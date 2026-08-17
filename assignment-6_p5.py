# <---------- Check Fruit List ---------->

fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]
fruit = input("Enter a Fruit: ")

if fruit in fruits:
    print(fruit, "is available.")
    
else:
    print(fruit, "is not available")
