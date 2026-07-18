'''
Employee ID
Name
Department
Salary
Experience (Years)
'''
employees = []
while True:
    print("\n====== Employee Management System ======\n")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Show Employee Summary")
    print("7. Exit")
    choose = input("Choose an option: ")
    if choose=='1':
        empid = input("Enter Employee Id: ")
        name = input("Enter Employee Name: ")
        dept = input("Enter Department: ")
        salary = float(input("Employee Salary: "))
        exp = int(input("Employee Experience(Years)"))
        employee={
        "eid" : empid,
        "name":name,
        "dept":dept,
        "sal":salary,
        "exp" :exp
        }
        employees.append(employee)
        print("Employee Added Successfully!")
    elif choose =='2':
        if len(employees)==0:
            print("No Employee Available!")
        else:
            print("====== Employees Details ======\n")
            for employee in employees:
                print("Employee ID:",employee["eid"])
                print("Name:",employee["name"].capitalize())
                print("Department:",employee["dept"].capitalize())
                print("Salary:",employee["sal"])
                print("Experience:",employee["exp"],"Years")
                print("------------------------------")
    elif choose =='3':
        empid = input("Enter Employee ID: ").lower()
        found = False
        for employee in employees:
            if empid == employee["eid"].lower():
                found = True
                print("Employee ID:",employee["eid"])
                print("Name:",employee["name"].capitalize())
                print("Department:",employee["dept"].capitalize())
                print("Salary:",employee["sal"])
                print("Experience:",employee["exp"],"Years")
                print("------------------------------")
                break
        if not found:
            print("No Employee Found!")
    elif choose == '4':
        empid = input("Enter Employee ID: ").lower()
        found = False
        for employee in employees:
            if empid == employee["eid"].lower():
                found = True
                print("Employee ID:",employee["eid"])
                name = input("Enter Employee Name: ")
                dept = input("Enter Department: ")
                salary = float(input("Employee Salary: "))
                exp = int(input("Employee Experience(Years)"))
                employee["name"]=name
                employee["dept"]=dept
                employee["sal"]=salary
                employee["exp"]=exp
                print("Record Updated Successfully!")
                
                break
        if not found:
            print("No Employee Found!")
    elif choose == '5':
        empid = input("Enter Employee ID: ").lower()
        found = False
        for employee in employees:
            if empid == employee["eid"].lower():
                found = True
                employees.remove(employee)
                print("Employee Deleted Successfully!")
                break
        if not found:
            print("No Employee Found!")
    elif choose == '6':
        if len(employees) == 0:
            print("No Employee Available!")
        else:
            temp = 0
            tsal = 0
            mexp = 0
            memp = ""
            print("====== EMPLOYEE SUMMARY ======\n")
            print("Employee Names:")
            for employee in employees:
                print(employee["name"])
                temp = temp + 1
                tsal = tsal + employee["sal"]
                if mexp< employee["exp"]:
                    mexp = employee["exp"]
                    memp = employee["name"]
            print("\n\n Total Employee:",temp)
            print("Total Salary Expenses:",tsal)
            print("Average Salary:",tsal/temp)
            print("Most Experience Employee:",memp,mexp,"Years")
                
    elif choose =='7':
        print("Good Bye!")
        break
    else:
        print("Invalid Input")
        
    