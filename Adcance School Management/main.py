import sqlite3
def home():
    print("=" * 40)
    print("     STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Count Students")
    print("7. Exit")
    print("=" * 40)
def add():
    student_id = int(input("Student ID   : "))
    name = input("Student Name : ")
    age = int(input("Student Age  : "))

    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?)",
        (student_id, name, age)
    )

    connection.commit()

    print("\nStudent Added Successfully.\n")

def view():
    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if len(students) == 0:
        print("\nNo Students Found.\n")
        return

    print("\n-------------------------------")
    print("ID\tNAME\t\tAGE")
    print("-------------------------------")

    for student in students:
        print(f"{student[0]}\t{student[1]}\t\t{student[2]}")

    print("-------------------------------\n")
def search():
    student_id = int(input("Enter Student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print("------------------------")
        print("ID   :", student[0])
        print("Name :", student[1])
        print("Age  :", student[2])
        print("------------------------\n")
    else:
        print("\nStudent Not Found.\n")
def update():
    student_id = int(input("Enter Student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student is None:
        print("\nStudent Not Found.\n")
        return

    print("\nCurrent Details")
    print("----------------------")
    print("Name :", student[1])
    print("Age  :", student[2])
    print("----------------------")

    new_name = input("New Name : ")
    new_age = int(input("New Age  : "))

    cursor.execute(
        "UPDATE students SET name=?, age=? WHERE id=?",
        (new_name, new_age, student_id)
    )

    connection.commit()

    print("\nStudent Updated Successfully.\n")

def delete():
    student_id = int(input("Enter Student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student is None:
        print("\nStudent Not Found.\n")
        return

    print("\nStudent Found")
    print("----------------------")
    print("ID   :", student[0])
    print("Name :", student[1])
    print("Age  :", student[2])
    print("----------------------")

    confirm = input("Delete this student? (Y/N): ").upper()

    if confirm == "Y":

        cursor.execute(
            "DELETE FROM students WHERE id=?",
            (student_id,)
        )

        connection.commit()

        print("\nStudent Deleted Successfully.\n")

    else:
        print("\nDelete Cancelled.\n")


def count_students():
    cursor.execute("SELECT COUNT(*) FROM students")

    total = cursor.fetchone()[0]

    print("\n----------------------")
    print(f"Total Students : {total}")
    print("----------------------\n")

connection = sqlite3.connect("students.db")
cursor = connection.cursor()
while True:
    home()
    choice = input("Choose an option: ")

    if choice == "1":
        add()

    elif choice == "2":
        view()

    elif choice == "3":
        search()

    elif choice == "4":
        update()

    elif choice == "5":
        delete()

    elif choice == "6":
        count_students()

    elif choice == "7":
        connection.close()
        print("Good Bye!")
        break

    else:
        print("Invalid Choice")