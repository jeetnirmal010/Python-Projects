import json
def display(student):
    print("Roll No: ",student["roll"])
    print("Name   : ",student["name"])
    print("Age    : ",student["age"])
    print("Course : ",student["course"])
    print("Marks  : ",student["marks"])
def load():
    try:
        students = []
        with open("students.json","r") as file:
            students = json.load(file)
        return students
    except FileNotFoundError:
        return students
def save(students):
    with open("students.json","w") as file:
        json.dump(students,file,indent= 4)
def add(students,student):
    students.append(student)
    save(students)
    return True
def search(students,roll):
    for student in students:
        if roll == student["roll"]:
            return student
    return False
def update(students,roll):
    student = search(students,roll)
    if student:
        name = input("New Name: ")
        while True:
            try:
                age = int(input("New Age: "))
                break
            except ValueError:
                print("Age Should be a Number!......")
        course = input("New Course: ")
        while True:
            try:
                marks = int(input("New Marks: "))
                break
            except ValueError:
                print("Marks Should be an Integer!......")

        student["name"] = name
        student["age"] = age
        student["course"] =course
        student["marks"] =marks

        save(students)
        print("Record Updated Successfully!......")
    else:
        print(f"Roll NO :{roll} No Student Found!....")
def delete(students,roll):
    student = search(students,roll)
    if student:
        print("=====================================")
        display(student)
        print("=====================================")
        print("======= DELETED SUCCESSFULLY ========")
        students.remove(student)
        save(students)
    else:
        print("No Student Found!...")


    