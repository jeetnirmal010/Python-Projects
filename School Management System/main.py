from student import Student
import student_database

student_list = student_database.read()
def _add():
    while True:
        sid = input("Student ID: ")
        student = student_database.search(student_list,sid)
        if student is None:
            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            _class = int(input("Class: "))
            section = input("Section: ")
            rollno = input("Roll Number: ")
            eng = int(input("English Marks: "))
            math = int(input("Math Marks: "))
            sci = int(input("Science Marks: "))
            cont = input("Contact: ")
            student = Student(sid,name,age,gender,_class,section,rollno,eng,math,sci,cont)
            student_database.add(student_list,student)
            print("Student Added Successfully!..........")
            break
        print("Student ID Already Available!..........")
def _home():
    print("\n====== SCHOOL MANAGEMENT SYSTEM ======\n\n")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save")
    print("7. Exit\n")


while True:
    _home()
    temp = input("Choose an Option: ")
    if temp == '1':
        _add()
        student_database.save(student_list)
    elif temp == '2':
        student_database.view(student_list)
    elif temp == '3':
        sid = input("Student ID: ")
        student = student_database.search(student_list,sid)
        if student:
            student.display()
        else:
            print("No Record Found!..........")
    elif temp == '4':
        sid = input("Student ID: ")
        student = student_database.search(student_list,sid)
        if student is None:
            print("No Record Found!......")
        else:
            student.name = input("New Name: ")
            student.age = int(input("New Age: "))
            student.gender = input("New Gender: ")
            student._class = int(input("New Class: "))
            student.section = input("New Section: ")
            student.rollno = input("New Roll Number: ")
            student.eng = int(input("New English Marks: "))
            student.math = int(input("New Math Marks: "))
            student.sci = int(input("New Science Marks: "))
            student.cont = input("New Contact: ")
            print("Record Updated Successfully!..........")
            student_database.save(student_list)

    elif temp =='5':
        sid = input("Student ID: ")
        student = student_database.search(student_list,sid)
        if student:
            student.display()
            student_list.remove(student)
            print("Student Deleted Successfully!..........")
            student_database.save(student_list)
        else:
            print("No Record Found!..........")
    elif temp =='6':
        student_database.save(student_list)
        print("Saved Successfully!..........")
    elif temp == '7':
        student_database.save(student_list)
        print("Good Bye!")
        break
