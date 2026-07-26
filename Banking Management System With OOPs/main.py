from bank import Bank
from transaction import Transact
import bankDB
import transactionDB
import random
account_list = bankDB.read()
transaction_list = transactionDB.read()

def accountmenu(account_list,transaction_list):
    while True:
        print("====== Account Management ======\n")
        print("1. Open Account")
        print("2. View Accounts")
        print("3. Search Account")
        print("4. Update Account")
        print("5. Close Account")
        print("6. Back\n")
        atemp = input("Choose an Option: ")
        if atemp == '1':
            name = input("Customer Name: ")
            age = input("Customer Age: ")
            gender = input("Gender: ")
            phone = input("Contact: ")
            email = input("Email ID: ")
            addres = input("Address: ")
            acctyp = input("Account Type: ")
            account = Bank("",name,age,gender,phone,email,addres,acctyp,1000.00,"","")
            accnum = bankDB.add(account_list,account)
            while True:
                tid = "IN" +f"{random.randint(0,99999999):08d}"
                if not transactionDB.search(transaction_list,tid):
                    break

            transaction = Transact(tid,"",accnum," Opening Account "," CR ",1000.00,1000.00)
            transactionDB.add(transaction_list,transaction)
            bankDB.save(account_list)
            transactionDB.save(transaction_list)
            print("==============================")
            print("Account Opened Successfully!...\n\n")
            print("Account Number: ",accnum)
            print("Opening Balance: Rs.",account.balance_check())
            print("==============================")

        elif atemp == "2":
            bankDB.view(account_list)
        elif atemp =="3":
            accnum = input("Account Number: ")
            print("=================================")
            account = bankDB.search(account_list,accnum)
            if account and account.status == "ACTIVE":
                account.display()
            elif account and account.status =="CLOSED":
                print("Account Is Closed Already")
                account.display()
            else:
                print("No Account Found!...")
            print("=================================")
        elif atemp == '4':
            accnum = input("Account Number: ")
            bankDB.update(account_list,accnum)
            bankDB.save(account_list)
        elif atemp == '5':
            accnum = input("Account Number: ")
            account = bankDB.search(account_list,accnum)
            if account:
                if account.status == "ACTIVE":
                    while True:
                        tid = "IN" +f"{random.randint(0,99999999):08d}"
                        if not transactionDB.search(transaction_list,tid):
                            break
                    
                    transaction = Transact(tid,"",accnum," Closing Account "," DR ",account.balance_check(),0.00)
                    bankDB.delete(account_list,account)
                    transactionDB.add(transaction_list,transaction)
                    bankDB.save(account_list)
                    transactionDB.save(transaction_list)
                elif account.status=="CLOSED":
                    print("Account Number:" ,accnum ,"Already Closed\n")
            else:
                print("No Such Account Found!...")
                
        elif atemp == "6":
            break
        else:
            print("INVALID INPUT!......")
def transactionmenu(account_list,transaction_list):
    while True:
        print("\n====== Transaction Management ======\n\n")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Fund Transfer")
        print("4. Back\n")
        ttemp = input("Choose an Option: ")
        if ttemp == "1":
            accnum = input("Account Number: ")
            account = bankDB.search(account_list,accnum)
            if account and account.status =="ACTIVE":
                while True:
                    amount = float(input("Amount to Deposit: "))
                    if amount> 0:
                        break
                    else:
                        print("Invalid Amount!......")
                account.deposit(amount)
                while True:
                    tid = "IN" +f"{random.randint(0,99999999):08d}"
                    if not transactionDB.search(transaction_list,tid):
                        break

                transaction = Transact(tid,"",accnum,"Cash Deposit","CR",amount,account.balance_check())
                transactionDB.add(transaction_list,transaction)
                bankDB.save(account_list)
                transactionDB.save(transaction_list)
                print("==============================")
                print("Deposit Successful!")
                print("Current Balance: Rs.", account.balance_check())
                print("==============================")
            else:
                print("No Account Found!.......")

        elif ttemp == "2":
            accnum = input("Account Number: ")
            account = bankDB.search(account_list,accnum)
            if account and account.status == "ACTIVE":
                while True:
                    amount = float(input("Amount to Withdraw: "))
                    if (amount+1000) <= account.balance_check() and amount > 0:
                        account.withdraw(amount)
                        while True:
                            tid = "IN" +f"{random.randint(0,99999999):08d}"
                            if not transactionDB.search(transaction_list,tid):
                                break

                        transaction = Transact(tid,"",accnum,"Cash Withdraw","DR",amount,account.balance_check())
                        transactionDB.add(transaction_list,transaction)
                        bankDB.save(account_list)
                        transactionDB.save(transaction_list)
                        print("==============================")
                        print("Withdraw Successful!")
                        print("Current Balance: Rs.", account.balance_check())
                        print("==============================")
                        break
                    else:
                        print("Invalid Amount!......")
            else:
                print("No Account Found!......")
        elif ttemp == "3":
            daccnum = input("Debitor's Account Number: ")
            daccount = bankDB.search(account_list,daccnum)
            if daccount and daccount.status == "ACTIVE":
                caccnum = input("Creditor's Account Number: ")
                caccount = bankDB.search(account_list,caccnum)
                if caccount and caccount.status == "ACTIVE" and caccnum != daccnum:
                    while True:
                        amount = float(input("Amount to be Transfer: "))
                        if amount > 0 and (amount + 1000)<= daccount.balance_check():
                            daccount.withdraw(amount)
                            caccount.deposit(amount)
                            while True:
                                tid = "IN" +f"{random.randint(0,99999999):08d}"
                                if not transactionDB.search(transaction_list,tid):
                                    break
                            
                            dtransaction = Transact(tid,"",daccnum,f"Fund Transfer to {caccount.accnum}","DR",amount,daccount.balance_check())
                            ctransaction = Transact(tid,"",caccnum,f"Fund Transfer from {daccount.accnum}","CR",amount,caccount.balance_check())
                            transactionDB.add(transaction_list,dtransaction)
                            transactionDB.add(transaction_list,ctransaction)
                            bankDB.save(account_list)
                            transactionDB.save(transaction_list)
                            print("==============================")
                            print("Successfull Fund Transfer")
                            daccount.display()
                            print("Available Balance: ",daccount.balance_check())
                            print("---------------------------------------------------")
                            caccount.display()
                            print("Available Balance: ",caccount.balance_check())
                            print("==============================")
                            break
                        else:
                            print("Invalid Amount!......")
                else:
                    print("Creditor's Account Not Found!......")

            else:
                print("Debitor's Account Not Found!......")
        elif ttemp =="4":
            break
        else:
            print("Invalid Input!......")
def homemenu():
    print("\n====== BANKING MANAGEMENT SYSTEM ======\n\n")
    print("1. Account Management")
    print("2. Transaction Management")
    print("3. Balance Inquiry")
    print("4. Statement of Accounts")
    print("5. Reports")
    print("6. Exit")
def reportmenu(account_list,transaction_list):
    while True:
        print("====== Report Menu ======")
        print("1. Total Active Accounts")
        print("2. Total Closed Accounts")
        print("3. Total Bank Balance")
        print("4. Total Transaction")
        print("5. Back")
        rtemp = input("Choose an Option: ")
        if rtemp == "1":
            c = 0
            for account in account_list:
                if account.status == "ACTIVE":
                    c = c + 1
            print(f"Total Active Accounts: {c}")
        elif rtemp == "2":
            c = 0
            for account in account_list:
                if account.status == "CLOSED":
                    c = c + 1
            print(f"Total Closed Account: {c}")
        elif rtemp == "3":
            tbalance = 0
            for account in account_list:
                tbalance = tbalance + account.balance_check()
            print(f"Total Bank Balance: Rs.{tbalance}")
        elif rtemp == "4":
            print("=====================================")
            for transaction in transaction_list:
                transaction.display()
                    
            print("====================================")
        elif rtemp == "5":
            break
        else:
            print("Invalid Input!......")
        
while True:
    homemenu()
    temp = input("Choose an Option: ")
    if temp == "1":
        accountmenu(account_list,transaction_list)
        
    elif temp == "2":
        transactionmenu(account_list,transaction_list)
    elif temp == "3":
        accnum = input("Account Number: ")
        account = bankDB.search(account_list,accnum)
        if account and account.status == "ACTIVE":
            print(f"Account Number: {account.accnum}")
            print(f"Available Balance: Rs.{account.balance_check()}")
            print("================================================")
        else:
            print("No Account Found!......")
    elif temp =="4":
        accnum = input("Account Number: ")
        account= bankDB.search(account_list,accnum)
        if account and account.status =="ACTIVE":
            transactionDB.view(transaction_list,accnum)
            print("=========================================")
        else:
            print("No Account Found!......")
    elif temp == "5":
        reportmenu(account_list,transaction_list)

    elif temp =="6":
        bankDB.save(account_list)
        transactionDB.save(transaction_list)
        print("Good Bye!.")
        break
