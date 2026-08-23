course = "Web Design"
print(course[0])
print(course[0:3])
print(course[4:10])
print(course[:])
print(len(course))

name = "Mohammed Usman"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())

if "Mohammed" in name:
    print("Mohammed Exists In Name")
else:
    print("Mohammed Doesnt Exist In Name")
    
word = input("Enter A Word:")
reverse = word[::-1]

if word == reverse:
    print(word,"Is Palindrome" )
else:
    print(word,"Is Not Palindrome" )
