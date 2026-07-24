from student import Student
def add(student_list,student):
    student_list.append(student)
def view(student_list):
    if len(student_list) == 0:
        print("No Record Available!......")
    else:
        for student in student_list:
            student.display()
def read():
    try:
        student_list = []
        file = open("students.txt","r")
        for line in file:
            line = line.strip()
            if line =="":
                continue
            data = line.split(",")
            print(line)
            data[2] = int(data[2])
            data[4] = int(data[4])
            data[7] = int(data[7])
            data[8] = int(data[8])
            data[9] = int(data[9])
            student = Student(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10])
            student_list.append(student)
        file.close()
    except FileNotFoundError:
        pass
    return student_list

def save(student_list):
    file = open("students.txt","w")
    for student in student_list:
        file.write(student.sid+","+student.name+","+str(student.age)+","+student.gender+","+str(student._class)+","+student.section+","+student.rollno+","+str(student.eng)+","+str(student.math)+","+str(student.sci)+","+student.cont+"\n")
    file.close()

def search(student_list,sid):
    for student in student_list:
        if sid == student.sid:
            return student
    return None