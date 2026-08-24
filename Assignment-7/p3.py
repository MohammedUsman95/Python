text = input("Enter Text: ")
search = input("Enter A Charector To Search: ")

count = 0
for searched_letter in text:
    if searched_letter == search:
        count += 1

print("Number Of",search,"=",count)
