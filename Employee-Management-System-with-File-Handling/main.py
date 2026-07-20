employees = []
deptart = ["HR","SALES","MARKETING","OPERATION"]
design = ["MANAGER","EMPLOYEE"]

def show_(emp):
    print("Employee ID:",emp[0])
    print("Employee Name:",emp[1])
    print("Employee Age:",emp[2])
    print("Gender:",emp[3])
    print("Department:",emp[4])
    print("Designation:",emp[5])
    print("Salary:Rs.",emp[6])
    print("Contact:+91",emp[7])
    print("_______________")

def saverecord():
    file =open("employees.txt","w")
    for emp in employees:
        file.write(str(emp[0])+","+str(emp[1])+","+str(emp[2])+","+str(emp[3])+","+str(emp[4])+","+str(emp[5])+","+str(emp[6])+","+str(emp[7])+"\n")
    file.close()

def readrecord():
    try:
        file = open("employees.txt","r")
        for line in file:
            line = line.strip()
            data = line.split(",")
            data[6] = float(data[6])
            employees.append(data)
        file.close()
    except FileNotFoundError:
        print("")


def _home():
    print("\n====== Employee Management System ======\n\n")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Increase Employee Salary")
    print("7. View Highest Salary")
    print("8. View Department wise Employee")
    print("9. Exit")

def _addemp():
    eid = input("Employee ID: ").lower()
    for emp in employees:
        if emp[0] == eid:
            print("Employee Already Available!..........")
            break
    else:
        name = input("Employee Name: ")
        age = input("Employee Age: ")
        gend = input("Employee Gender: ")
        while True:
            dept = input("Department\n   HR SALES MARKETING  OPERATION\nSelect dept ").upper()
            if dept in deptart:
                break
            print("Invalid Department")
        while True:
            desig = input("Department\n   \n       MANAGER  EMPLOYEE\nSelect designation: ").upper()
            if desig in design:
                break
            print("Invalid Department")
        sal = float(input("Employee Salary: Rs. "))
        cont = input("Contact Details: +91 ")
        emp = [eid,name,age,gend,dept,desig,sal,cont]
        employees.append(emp)
        print("New Employee Added Successfully!..........")

def _viewemp():
    if len(employees) == 0:
        print("No Record Available!..........")
    else:
        for emp in employees:
            show_(emp)

def _saladd():
    eid = input("Employee ID: ").lower()
    found = False
    for emp in employees:
        if emp[0] == eid:
            show_(emp)
            sal_inc = float(input("Enter Percentage to Increase: "))
            emp[6] = emp[6] + (emp[6] * sal_inc / 100)
            print("Salary increased By",sal_inc,"% Successfully!...")
            found = True
            break
    if not found:
        print("No Record Found!..........")
                            
def _deleteemp():
    eid = input("Employee ID: ").lower()
    found = False
    for emp in employees:
        if emp[0] == eid:
            show_(emp)
            print("Deleted Successfully!..........")
            employees.remove(emp)
            found = True
            break
    if not found:
         print("No Employee Record Found!..........")

def _updateemp():
    eid = input("Employee ID: ").lower()
    found = False
    for emp in employees:
        if emp[0] == eid:
            show_(emp)
            emp[1] = input("New Name: ")
            emp[2] = input("New Age: ")
            emp[3] = input("New Gender: ")
            while True:
                dept = input("Department\n   HR SALES MARKETING  OPERATION\nSelect dept ").upper()
                if dept in deptart:
                    break
                print("Invalid Department")
            while True:
                desig = input("Department\n   \n       MANAGER  EMPLOYEE\nSelect designation: ").upper()
                if desig in design:
                    break
                print("Invalid Department")
            emp[4] = dept
            emp[5] = desig
            emp[6] = float(input("New Salary: "))
            emp[7] = input("New Contact: ")
            found = True
            print("Employee Record Updated Successfully!..........")
            break
    if not found:
         print("No Employee Record Found!..........")   

def _searchemp():
    eid = input("Employee ID: ").lower()
    found = False
    for emp in employees:
        if emp[0] == eid:
            show_(emp)
            found = True
            break
    if not found:
         print("No Employee Record Found!..........")


readrecord()
while True:
    _home()
    temp = input("Choose an Option: ")
    if temp == '1':
        _addemp()
        saverecord()
    elif temp =='2':
        _viewemp()
    elif temp == '3':
        _searchemp()
    elif temp == '4':
         _updateemp()
         saverecord()
    elif temp == '5':
        _deleteemp()
        saverecord()
    elif temp == '6':
        _saladd()
        saverecord()
    elif temp == '7':
        if len(employees) == 0:
            print("No Record Available!..........")
        else:
            hemp= employees[0]
            for emp in employees:
                if hemp[6] < emp[6]:
                    hemp = emp
            print("------ Highest Salary Employee ------")
            show_(hemp)
    elif temp == '8':
        print("------ Employees By Department ------\n")
        print("Department : HR")
        for emp in employees:
            if emp[4] == deptart[0]:
                show_(emp)

        print("Department: SALES")
        for emp in employees:
            if emp[4] == deptart[1]:
                show_(emp)
        
        print("Department: MARKETING")
        for emp in employees:
            if emp[4] == deptart[2]:
                show_(emp)

        print("Department: OPERATION")
        for emp in employees:
            if emp[4] == deptart[3]:
                show_(emp)
    elif temp == '9':
        saverecord()
        print(" _________________________________________________")
        print("|                                                 |")
        print("|       Designed By Sardar Nirmaljeet Singh       |")
        print("|_________________________________________________|")
        print("Good Bye!..........")
        break
    else:
        print("Invalid Input!..........")
