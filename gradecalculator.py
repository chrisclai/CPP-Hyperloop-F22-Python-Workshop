# Single line comment

"""
Multi
line
comment
"""

"""
Grade Calculator

if the grade is above a 100, the student gets an A
if the grade is between 90 and 100, the student gets an A
if the grade is between 80 and 89, the student gets a B
if the grade is between 70 and 79, the student gets a C
if the grade is between 60 and 69, the student gets a D
if the grade is lower than 60, the student gets an F

"""

grade = 0
validInput = False

while not validInput: # If validInput = False, then loop. Otherwise, skip.
    try:
        grade = int(input("Enter the student's grade: "))
        validInput = True
    except Exception as e:
        print(e)

answer = ""

if grade >= 90:
    answer = "A"
elif grade >= 80:
    answer = "B"
elif grade >= 70:
    answer = "C"
elif grade >= 60:
    answer = "D"
else:
    answer = "F"

print(answer)