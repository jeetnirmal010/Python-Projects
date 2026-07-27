from student import Student
import sqlite3
def add():
    rollno = input("Roll No: ")
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    _class = input("Class: ")
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO student VALUES(?,?,?,?,?)""",(rollno,name,age,gender,_class))
    conn.commit()
    conn.close()
    print("Student Added Successfully!...")
def view():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM  student")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    conn.commit()
    conn.close()

def update():
    rollno = input("Roll No: ")
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    _class = input("Class: ")
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE student SET name = ?, age = ? , gender = ?,class =? WHERE rollno = ?",(name,age,gender,_class,rollno))
    conn.commit()
    conn.close()
    print("Updated Successfully!...")
def delete():
    rollno = input("Roll No: ")
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM student WHERE rollno = ?""",(rollno,))
    conn.commit()
    conn.close()
    print("Deleted Successfully!....")


while True:
    temp = input("Choice: ")
    if temp == "1":
        add()
    elif temp == "2":
        view()
    elif temp == "3":
        update()
    elif temp =="4":
        delete()
    elif temp  == "5":
        break