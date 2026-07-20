student_name = input("Enter student name: ")
score = int(input("Enter score: "))

print("----- REPORT CARD -----")
print("Student :", student_name)
print("Score   :", score)

if score < 0 or score > 100:
    print("Grade   : Invalid Score")
elif score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

if 0 <= score <= 100:
    print("Grade   :", grade)