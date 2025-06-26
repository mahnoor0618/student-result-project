students={}

def add_students(name,marks):
    students[name]=marks

def student_grade(marks):
    if marks >= 90:
        return("Grade A++")
    elif marks >= 80:
        return("Grade A+")
    elif marks >= 70:
        return("Grade A")
    elif marks >= 60:
        return("Grade B")
    else:
        return("Fail")

def student_result():
    print("STUDENTS RESULT:")
    for name,marks in students.items():
        grade=student_grade(marks)
        print(f"Name: {name}\nMarks: {marks}\nGrade: {grade} ")

n=int(input("Enter number of students:"))
for i in range(1,n+1):
    if i == 1:
        name=str(input(f"Enter {i}st student name:"))
    elif i == 2 :
        name=str(input(f"Enter {i}nd student name:"))
    elif i == 3 :
        name=str(input(f"Enter {i}rd student name:"))
    else:
        name=str(input(f"Enter {i}th student name:"))
    marks=float(input("Enter marks:"))
    add_students(name,marks)

student_result()