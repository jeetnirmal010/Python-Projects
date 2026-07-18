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
        sid = input("Enter Student ID: ")
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
    elif choose == '2':
        if len(students)==0:
            print("No Record Available!")
        else:
            for student in students:
                print("Student ID   :",student["sid"])
                print("Name         :",student["name"])
                print("Subject1 Mark:",student["sub1"])
                print("Subject2 Mark:",student["sub2"])
                print("Subject3 Mark:",student["sub3"])
                print("Total Marks  :",student["tmarks"])
                print("Percent Marks:",student["pmarks"])
                print("Grade        :",student["gmarks"])
                print("----------------------------------------------\n")
    elif choose == '3':
        sid = input("Enter Student ID: ").lower()
        found = False
        for student in students:
            if sid == student["sid"].lower():
                print("Student ID   :",student["sid"])
                print("Name         :",student["name"])
                print("Subject1 Mark:",student["sub1"])
                print("Subject2 Mark:",student["sub2"])
                print("Subject3 Mark:",student["sub3"])
                print("Total Marks  :",student["tmarks"])
                print("Percent Marks:",student["pmarks"])
                print("Grade        :",student["gmarks"])
                found = True
                break
        if not found:
            print("Student Not Found!")
    elif choose == '4':
        sid = input("Enter Student ID: ").lower()
        found = False
        for student in students:
            if sid == student["sid"].lower():
                student["name"] = input("Enter Student Name: ")
                sub1=int(input("Enter Subject1 Marks: "))
                sub2=int(input("Enter Subject2 Marks: "))
                sub3=int(input("Enter Subject3 Marks: "))
                tmarks = sub1 + sub2 + sub3
                pmarks = tmarks / 3
                gmarks = _grade(pmarks)
                student["sub1"] = sub1
                student["sub2"] = sub2
                student["sub3"] = sub3
                student["tmarks"] = tmarks
                student["pmarks"] = pmarks
                student["gmarks"] = gmarks
                print("Record Updated Successfully!")
                found = True
                break
        if not found:
            print("Student Not Found!")
    elif choose == '5':
        sid = input("Enter Student ID: ").lower()
        found = False
        for student in students:
            if sid == student["sid"].lower():
                print("Student ID:",student["sid"])
                print("Name      :",student["name"])
                print("Deleted Successfully!")
                students.remove(student)
                found = True
                break
        if not found:
            print("Student Not Found!")
    elif choose == '6':
        if len(students) == 0:
            print("No Students Available!")
        else:
            tstudent = 0
            tp = 0.0
            hscore = 0      	
            lscore = students[0]["pmarks"]
            lname = students[0]["name"]
            hname =""
            ga = 0
            gb = 0
            gc = 0
            gd = 0
            gf = 0
            print("====== CLASS SUMMARY ======\n")
            print("Students Name:")
            for student in students:
                print(student["name"])
                tstudent = tstudent + 1
                tp = tp + student["pmarks"]
                if hscore < student["pmarks"]:
                    hscore = student["pmarks"]
                    hname = student["name"]
                    
                if lscore > student["pmarks"]:
                    lscore = student["pmarks"]
                    lname = student["name"]
                if student["gmarks"] == 'A':
                    ga = ga + 1
                elif student["gmarks"] == 'B':
                    gb = gb + 1
                elif student["gmarks"] == 'C':
                    gc = gc + 1
                elif student["gmarks"] == 'D':
                    gd = gd + 1
                else:
                    gf = gf + 1
            print("Total Students:",tstudent)
            print("Average Percentage:",tp /tstudent)
            print("Highest Scorer:",hname,hscore,"%")
            print("Lowest Scorer:",lname,lscore,"%")
            print("Grade A Students:",ga)
            print("Grade B Students:",gb)
            print("Grade C Students:",gc)
            print("Grade D Students:",gd)
            print("Grade F Students:",gf)
    elif choose == '7':
        print("Good Bye!")
        break
    else:
        print("Invalid Input!")
        