word = input("Enter A Word:")
reverse = word[::-1]

if word == reverse:
    print(word,"Is Palindrome" )
else:
    print(word,"Is Not Palindrome" )