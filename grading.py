# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter
# grade, and a message stating whether the student is passing.

# Changed exam_3 to exam_three
# Added int to exam_two and exam_three
# Added commas to the grades list
# Added colon to line 41
# Fixed a typo line 46 and line 40
# Added statement to line 50
# Fixed print typo added parenthesis

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grade = [exam_one, exam_two, exam_three]
sum = 0

for grade in grade:
    sum = sum + grade

avg = sum / grade

letter_grade = grade

if avg >= 90:
    letter_grade = "A"
elif 80 <= avg < 90:
    letter_grade = "B"
elif 69 < avg < 80:
    letter_grade = "C"
elif 69 >= avg >= 65:
    letter_grade = "D"
if avg <= 59:
    letter_grade = "F"

for grade in range(grade):
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + str(letter_grade))

if grade != "F":
    print("Student is passing.")
else:
    print("Student is failing.")
