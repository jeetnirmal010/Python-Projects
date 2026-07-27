import studentDB
def home():
    print("\n======School Management System\n\n======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. EXIT\n")
students = studentDB.load()
while True:
    home()
    temp = input("Choose an Option: ")
    if temp == "1":
        while True:
            roll = input("Roll No: ")
            if studentDB.search(students,roll):
                print("Roll Number Already Exits!...")
            else:
                break

        name = input("Name: ")
        while True:
            try:
                age = int(input("Age: "))
                break
            except ValueError:
                print("Age Should be a Number!......")
        course = input("Course: ")
        while True:
            try:
                marks = int(input("Marks: "))
                break
            except ValueError:
                print("Marks Should be an Integer!......")
        student = {
            "roll" : roll,
            "name" : name,
            "age" : age,
            "course":course,
            "marks":marks
        }
        studentDB.add(students,student)
        print("Student Added Successfully!......")
    elif temp == "2":
        if not students:
            print("No Student Available!....")
        else:
            count =1
            print("============================================")
            print("============= Students Records =============")
            print("============================================")
            for student in students:
                print(count)
                studentDB.display(student)
                print("-------------------------------------------")
                count+=1
            print("********************************************")
    elif temp == "3":
        roll = input("Roll No: ")
        student = studentDB.search(students,roll)
        if student:
            studentDB.display(student)
        else:
            print(f"Roll No: {roll} No Student Found!......")
    elif temp == "4":
        roll = input("Roll No: ")
        studentDB.update(students,roll)
    elif temp == "5":
        roll = input("Roll No: ")
        studentDB.delete(students,roll)
    elif temp == "6":
        print("Good Bye!")
        break
    else:
        print("Invalid Input!.......")