marks1 = int(input("Enter English Marks: "))
marks2 = int(input("Enter Maths Marks: "))
marks3 = int(input("Enter Science Marks: "))

def calculate_result(marks1, marks2, marks3):
    TotalMarks = marks1 + marks2 + marks3
    print("Total =",TotalMarks)
    Average = TotalMarks / 3
    print("Average =",Average)
    if Average >= 40:
        print("Result = Pass")
    else:
        print("Result = Fail")

calculate_result(marks1, marks2, marks3)