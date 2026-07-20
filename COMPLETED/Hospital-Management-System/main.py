patients =[]

def _preload():
    try:
        file = open("patient.txt","r")
        for line in file:
            line = line.strip()
            data = line.split(",")
            patients.append(data)
        file.close()
    except FileNotFoundError:
        print("")

def _save():
    file = open("patient.txt","w")
    for pat in patients:
        file.write(str(pat[0])+","+str(pat[1])+","+str(pat[2])+","+str(pat[3])+","+str(pat[4])+","+str(pat[5])+","+str(pat[6])+"\n")
    file.close()

def _nvalid(x):
    found = False
    for pat in patients:
        if x == pat[0]:
            found = True
            return False
    if not found:
        return True

def _show(pat):
    print("Patient ID: ",pat[0])
    print("Name    : ",pat[1])
    print("Age     : ",pat[2])
    print("Gender  : ",pat[3])
    print("Disease: ",pat[4])
    print("Doctor  : ",pat[5])
    print("Contact : ",pat[6])
    print("____________________________________________\n")

def _addp():
    idp = input("Enter Patient ID: ")
    if _nvalid(idp):
        name = input("Enter Name: ")
        age = input("Age: ")
        gender = input("Gender: ")
        dies = input("Disease: ")
        doc = input("Doctor: ")
        cont = input("Contact: ")
        pat =[idp,name,age,gender,dies,doc,cont]
        patients.append(pat)
        print("NEW PATIENT ADDED SUCCESSFULLY!...................")
    else:
        print(idp,"Already Exits!")
    
def _viewp():
    if len(patients)==0:
        print("No Patient Available\n")
    else:
        print("====== ALL PATIENT's RECORD ======")
        for pat in patients:
            _show(pat)

def _searchp():
    idp = input("Patient ID: ")
    found = False
    for pat in patients:
        if idp == pat[0]:
            _show(pat)
            found = True
            break
    if not found:
        print("No Patient Found!")

def _updatep():
    idp = input("Patient ID: ")
    found = False
    for pat in patients:
        if idp == pat[0]:
            _show(pat)
            pat[1] = input("Enter New Name: ")
            pat[2] = input("New Age: ")
            pat[3] = input("New Gender: ")
            pat[4] = input("New Disease: ")
            pat[5] = input("New Doctor: ")
            pat[6] = input("New Contact: ")
            print("Patient Record Updated Successfully!______________________________________")
            found = True
            break
    if not found:
        print("No Patient Found!")
        
def _delp():
    idp = input("Patient ID: ")
    found = False
    for pat in patients:
        if idp == pat[0]:
            _show(pat)
            print("Deleted Successfully!................................")
            patients.remove(pat)
            found = True
            break
    if not found:
        print("No Patient Found!")

def _home():
    print("\n\n====== HOSPITAL MANAGEMENT SYSTEM ======\n")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Exit\n")


_preload()
while True:
    _home()
    temp = input("Choose an Option: ")
    if temp =='1':
        _addp()
        _save()
    elif temp =='2':
        _viewp()
    elif temp =='3':
        _searchp()
    elif temp =='4':
        _updatep()
        _save()
    elif temp =='5':
        _delp()
        _save()
    elif temp =='6':
        _save()
        print("Good Bye!")
        print("Designed By Sardar Nirmaljeet Singh on 19 - July - 2026")
        break
    else:
        print("Invalid Input!")
