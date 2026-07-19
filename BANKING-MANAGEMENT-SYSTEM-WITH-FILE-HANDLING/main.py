accounts = []
def _validaccount(x):
    if len(accounts) == 0:
        return False
    for acc in accounts:
        if x == acc[0]:
            return True
   
def _valid(x):
    if x<=0:
        print ("Invalid Amount!")
        return False
    else:
        return True

def _lsave():
    file = open("accounts.txt","w")
    for acc in accounts:
        file.write(str(acc[0])+","+str(acc[1])+","+str(acc[2])+","+str(acc[3])+","+str(acc[4])+"\n")
    file.close()
    
def _readaccounts():
    
    try:
        file = open("accounts.txt","r")
        for line in file:
            line = line.strip()
            data = line.split(",")
            data[3] = float(data[3])
            accounts.append(data)
        file.close()
    except FileNotFoundError:
        print("")

def _show(acc):
    print("Account Number:",acc[0])
    print("Customer Name :",acc[1])
    print("Phone Number  :",acc[2])
    print("Balance       :Rs.",acc[3])
    print("Account Type  :",acc[4])
    print("---------------------------------------")
    
    
    
    
def _search():
    accnum = input("Account Number: ").lower()
    f = False
    for acc in accounts:
        if accnum == acc[0]:
            _show(acc)
            f = True
            break
    if not f:
        print("No Account Found!")
    
def _deposit():
    accnum = input("Account Number: ").lower()
    amt = float(input("Amount: "))
    if _valid(amt):
        f = False
        for acc in accounts:
            if accnum == acc[0]:
                acc[3] = float(acc[3]) + amt
                print("Amount Deposited Successfully!")
                f = True
                break
        if not f:
            print("Account Not Found")
    
def _withdraw():
    accnum = input("Account Number: ").lower()
    found = False
    for acc in accounts:
        if accnum == acc[0].lower():
            amt = float(input("Amount to be Withdraw: "))
            if _valid(amt) and amt<=float(acc[3]):
                acc[3] = acc[3] - amt
                print(amt,"Withdraw Successfully!")
            else:
                print("Rs.",acc[3])
                print("Or In Sufficient Balance!")
            found = True
            break
    if not found:
        print("Account Not Found!")
            
def _update():
    accnum = input("Account Number: ").lower()
    f = False
    for acc in accounts:
        if accnum == acc[0]:
            _show(acc)
            name = input("Enter Customer Name: ")
            phone = input("Enter Phone Number: ")
            ''' Account balance can't be update mannually it should either deposit or withdral'''
            typ = input("enter account type: ")
            acc[1]=name
            acc[2]=phone
            acc[4]=typ
            print("Record Updated Successfully!")
            f= True
            break
    if not f:
        print("No Account Found!")
                


def _delete():
    accnum = input("Enter Account Number: ").lower()
    f = False
    for acc in accounts:
        if accnum == acc[0]:
            _show(acc)
            print("Deleted Successfully..........................!")
            f = True
            accounts.remove(acc)
            break
    if not f:
        print("No Record found!")

def _home():
    print("====== BANKING MANAGEMENT SYSTEM ======\n")
    print("1. CREATE ACCOUNT")
    print("2. VIEW ACCOUNTS")
    print("3. SEARCH ACCOUNT")
    print("4. DEPOSIT MONEY")
    print("5. WITHDRAW MONEY")
    print("6. UPDATE ACCOUNT")
    print("7. DELETE ACCOUNT")
    print("8. EXIT")
    
def _view():
    if len(accounts) == 0:
        print("No Account Created Yet!")
    
    else:
        for account in accounts:
            _show(account)

def _addaccount():
    accnumber = input("Account Number: ").lower()
    if not _validaccount(accnumber):
        name = input("Customer Name: ")
        phone=input("Phone Number: ")
        ''' Initially Default Account Balance Should be 1000 also this will be the minimum balance '''
        bal = float(1000)
        acctype=input("Account Type: ")
        account =[accnumber,name,phone,bal,acctype]
        accounts.append(account)
        print("Account Added Successfully!")
    else :
        print("Account number already Exits!")
        

_readaccounts()
while True:
    _home()
    choose = input("Choose an Option:")
    if choose == '1':
        _addaccount()
        _lsave()
    elif choose=='2':
        _view()
    elif choose=='3':
        _search()
    elif choose=='4':
        _deposit()
        _lsave()
    elif choose=='5':
        _withdraw()
        _lsave()
    elif choose=='6':
        _update()
        _lsave()
    elif choose=='7':
        _delete()
        _lsave()
    elif choose == '8':
        print("Good Bye!")
        _lsave()
        break
    else:
        print("Invalid Input!")
    