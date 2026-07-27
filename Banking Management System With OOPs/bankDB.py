from bank import Bank
from datetime import date
import random
def read():
    account_list = []
    try:
        file= open("accounts.txt","r")
        for line in file:
            line = line.strip()
            if line == "":
                continue
            data = line.split(",")
            data[8] = float(data[8])
            account = Bank(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10])
            account_list.append(account)
        file.close()
    except FileNotFoundError:
        pass
    return account_list

def save(account_list):
    file = open("accounts.txt","w")
    for account in account_list:
        file.write(str(account.accnum)+","+str(account.name)+","+str(account.age)+","+str(account.gender)+","+str(account.phone)+","+str(account.email)+","+str(account.addres)+","+str(account.acctyp)+","+str(account.balance_check())+","+str(account.opendate)+","+str(account.status)+"\n")
    file.close()

def view(account_list):
    if len(account_list)==0:
        print("No Account Opened Yet!......")
    else:
        for account in account_list:
            if account.status =="ACTIVE":
                account.display()
    
def search(account_list,accnum):
    for account in account_list:
        if accnum == account.accnum:
            return account
    return None

def add(account_list,account):
    while True:
        serial_number = f"{random.randint(0, 99999999):08d}"
        account_number = "12060"  + serial_number
        if not search(account_list,account_number):
            break
    account.accnum = account_number
    account.opendate = date.today() 
    account.status = "ACTIVE"     
    account_list.append(account)
    return account_number          

def update(account_list,accnum):
    account = search(account_list,accnum)
    if account and account.status == "ACTIVE":
        account.name = input("New Name: ")
        account.age = input("New Age: ")
        account.gender = input("New Gender: ")
        account.phone = input("New Contact: ")
        account.email = input("New Email: ")
        account.acctyp = input("New Account Type: ")
        account.addres = input("New Address: ")
        print("Account Details Updated Successfully!......")
        return True
    else:
        print("No Account Found!......")
        return False

def delete(account_list,account):
        account.display()
        print("Account Closed Successfully!......")
        account.status="CLOSED"
        account._nullBalance()
        return True
