text = input("Enter Text: ")

Vowels = 0
for letter in text:
    if letter in 'aeiouAEIOU':
        Vowels += 1

print("Number Of Vowels =",Vowels)