students = []
def _grade(_percent):
    if _percent >= 90:
        return 'A'
    elif _percent >=80:
        return 'B'
    elif _percent >=70:
        return 'C'
    elif _percent >=60:
        return 'D'
    else:
        return 'F'
while True:
    print("\n====== STUDENT GRADE MANAGEMENT SYSTEM ======\n")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Show Class Summary")
    print("7. Exit\n")
    choose = input("Choose an option: ")
    if choose =='1':
        name = input("Enter Student Name: ")
        sid = input("Enter Student ID: ").lower()
        sub1=int(input("Enter Subject1 Marks: "))
        sub2=int(input("Enter Subject2 Marks: "))
        sub3=int(input("Enter Subject3 Marks: "))
        tmarks = sub1 + sub2 + sub3
        pmarks = tmarks / 3
        gmarks = _grade(pmarks)
        student ={
            "sid" : sid,
            "name":name,
            "sub1":sub1,
            "sub2":sub2,
            "sub3":sub3,
            "tmarks":tmarks,
            "pmarks":pmarks,
            "gmarks":gmarks,
        }
        students.append(student)
        file = open("student.txt","a")
        file.write(student["sid"] +","+student["name"]+","+str(student["sub1"])+","+str(student["sub2"])+","+str(student["sub3"])+","+str(student["tmarks"])+","+str(student["pmarks"])+","+str(student["gmarks"])+"\n")
        file.close()
    elif choose == '2':
        try:
            file = open("student.txt", "r")
            for line in file:
                line = line.strip()
                data = line.split(",")
                print("Student ID   :", data[0])
                print("Name         :", data[1])
                print("Subject1 Mark:", data[2])
                print("Subject2 Mark:", data[3])
                print("Subject3 Mark:", data[4])
                print("Total Marks  :", data[5])
                print("Percent Marks:", data[6])
                print("Grade        :", data[7])
                print("----------------------------------------")

            file.close()
        except FileNotFoundError:
            print("No Record Available!")
    elif choose == '3':
        sid = input("Enter Student ID: ").lower()
        found = False
        try:
            file = open("student.txt", "r")
            for line in file:
                line = line.strip()
                data = line.split(",")
                if sid == data[0].lower():
                    print("Student ID   :", data[0])
                    print("Name         :", data[1])
                    print("Subject1 Mark:", data[2])
                    print("Subject2 Mark:", data[3])
                    print("Subject3 Mark:", data[4])
                    print("Total Marks  :", data[5])
                    print("Percent Marks:", data[6])
                    print("Grade        :", data[7])

                    found = True
                    break

            file.close()

            if not found:
                print("Student Not Found!")

        except FileNotFoundError:
            print("No Record Available!")
    elif choose == '4':
        sid = input("Enter Student ID: ").lower()
        records = []
        try:
            file = open("student.txt", "r")
            for line in file:
                records.append(line.strip())
            file.close()
            new_records = []
            found = False
            for record in records:
                data = record.split(",")
                if data[0].lower() == sid:
                    print("Student Found!")

                    name = input("New Name: ")
                    sub1 = int(input("Subject1: "))
                    sub2 = int(input("Subject2: "))
                    sub3 = int(input("Subject3: "))

                    total = sub1 + sub2 + sub3
                    percent = total / 3
                    grade = _grade(percent)

                    new_line = (
                        sid + "," +
                        name + "," +
                        str(sub1) + "," +
                        str(sub2) + "," +
                        str(sub3) + "," +
                        str(total) + "," +
                        str(percent) + "," +
                        grade
                    )

                    new_records.append(new_line)

                    found = True

                else:
                    new_records.append(record)
            if found:
                file = open("student.txt", "w")
                for record in new_records:
                    file.write(record + "\n")
                file.close()
                print("Record Updated Successfully!")
            else:
                print("Student Not Found!")
        except FileNotFoundError:
            print("No Record Available!")
    elif choose == '5':
        sid = input("Enter Student ID: ").lower()
        records = []
        try:
            file = open("student.txt", "r")
            for line in file:
                records.append(line.strip())
            file.close()
            new_records = []
            found = False
            for record in records:
                data = record.split(",")
                if data[0].lower() == sid:
                    print("Student Deleted Successfully!")
                    found = True
                else:
                    new_records.append(record)
            if found:
                file = open("student.txt", "w")
                for record in new_records:
                    file.write(record + "\n")
                file.close()
            else:
                print("Student Not Found!")

        except FileNotFoundError:
            print("No Record Available!")
    elif choose == '6':
        try:
            file = open("student.txt", "r")
            total_students = 0
            total_percentage = 0

            highest = 0
            highest_name = ""

            lowest = 100
            lowest_name = ""

            gradeA = 0
            gradeB = 0
            gradeC = 0
            gradeD = 0
            gradeF = 0

            for line in file:

                line = line.strip()
                data = line.split(",")

                name = data[1]
                percentage = float(data[6])
                grade = data[7]

                total_students += 1
                total_percentage += percentage

                if percentage > highest:
                    highest = percentage
                    highest_name = name

                if percentage < lowest:
                    lowest = percentage
                    lowest_name = name

                if grade == "A":
                    gradeA += 1
                elif grade == "B":
                    gradeB += 1
                elif grade == "C":
                    gradeC += 1
                elif grade == "D":
                    gradeD += 1
                else:
                    gradeF += 1

            file.close()

            if total_students == 0:
                print("No Students Available!")
            else:
                print("\n====== CLASS SUMMARY ======\n")

                print("Total Students :", total_students)
                print("Average Percentage :", total_percentage / total_students)

                print("Highest Scorer :", highest_name, highest, "%")
                print("Lowest Scorer  :", lowest_name, lowest, "%")

                print("Grade A Students :", gradeA)
                print("Grade B Students :", gradeB)
                print("Grade C Students :", gradeC)
                print("Grade D Students :", gradeD)
                print("Grade F Students :", gradeF)

        except FileNotFoundError:
            print("No Record Available!")
    elif choose == '7':
        print("Good Bye!")
        break
    else:
        print("Invalid Input!")
        