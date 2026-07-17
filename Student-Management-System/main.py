students = []

while True:
    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        student = {
            "name": name,
            "age": age,
            "course": course
        }
        students.append(student)
        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found!")
        else:
            print("\n===== STUDENT LIST =====")
        for student in students:
            print("Name  :", student["name"])
            print("Age   :", student["age"])
            print("Course:", student["course"])
            print("----------------------")

    elif choice == "3":
        search = input("Enter student name: ")
        found = False
        for student in students:
            if student["name"].lower() == search.lower():
                print("\n===== STUDENT FOUND =====")
                print("Name  :", student["name"])
                print("Age   :", student["age"])
                print("Course:", student["course"])
                found = True
                break

        if not found:
            print("Student not found!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")