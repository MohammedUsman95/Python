age = int(input("Enter Your Age: "))

def check_voting_eligibility(age):
    if age >= 18:
        print("You Are Eligible To Vote")
    else:
        print("You Are Not Eligible To Vote")

check_voting_eligibility(age)
