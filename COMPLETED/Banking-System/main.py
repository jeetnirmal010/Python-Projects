accounts = []
while True:
    print("====== BANKING SYSTEM ======\n")
    print("1. Create Account")
    print("2. View Account")
    print("3. Search Account")
    print("4. Deposit Account")
    print("5. Withdraw Money")
    print("6. Delete Account")
    print("7. Bank Summary")
    print("8. Exit")
    choose = input("Choose an option: ")
    if choose == '1':
        name = input("Enter Account Holder Name: ")
        accnum=input("Enter Account Number: ")
        acctype=input("Account Type (Saving / Current): ")
        bal = float(input("Initial Balance: "))
        account={
        "accnum" : accnum,
        "name" : name,
        "acctype" : acctype,
        "bal" : bal
        }
        accounts.append(account)
        print("One Account Added Successfully!")
    elif choose == '2':
        if len(accounts) ==0:
            print("No Accounts Available!")
        else:
            print("====== ACCOUNT DETAILS ======\n")
            for account in accounts:
                print("Account Number:",account["accnum"])
                print("Name          :",account["name"])
                print("Account Type  :",account["acctype"])
                print("Balance       :",account["bal"])
                print("----------------------------\n")
    elif choose == '3':
        accnum = input("Enter Account Number: ")
        found = False
        for account in accounts:
            if accnum == account["accnum"]:
                print("Account Number:",account["accnum"])
                print("Name          :",account["name"])
                print("Account Type  :",account["acctype"])
                print("Balance       :",account["bal"])
                print("----------------------------\n")
                found = True
                break
        if not found:
            print("No Account Found!")
    elif choose == '4':
        accnum = input("Enter Account Number: ")
        found = False
        for account in accounts:
            if accnum == account["accnum"]:
                amt = float(input("Enter Amount to Deposit: "))
                if amt <= 0:
                    print("Invalid Amount!")
                    continue
                else:
                    account["bal"] = account["bal"] + amt
                    print("Rs.",amt,"Deposited to Account Number:",account["accnum"])
                found = True
                break
        if not found:
            print("No Account Found!")
    elif choose == '5':
        accnum = input("Enter Account Number: ")
        found = False
        for account in accounts:
            if accnum == account["accnum"]:
                amt = float(input("Enter Amount to Withdraw: "))
                if amt > account["bal"]:
                    print("Insufficient Balance!")
                    continue
                elif amt <=0:
                    print("Invalid Amount!")
                    continue
                else:
                    account["bal"] = account["bal"] - amt
                    print("Rs.",amt,"Withdrawal from Account Number:",account["accnum"])
                found = True
                break
        if not found:
            print("No Account Found!")
    elif choose == '6':
        accnum = input("Enter Account Number: ")
        found = False
        for account in accounts:
            if accnum == account["accnum"]:
                print("Account Number:",account["accnum"],"Deleted Successfully!")
                accounts.remove(account)
                found = True
                break
        if not found:
            print("No Account Found!")
    elif choose == '7':
        if len(accounts) == 0:
            print("No Account Available!")
        else:
            print("\n====== ACCOUNT SUMMARY ======\n")
            tacc = 0
            tmon = 0
            nmax = ""
            bmax = 0
            print("Account Details:")
            for account in accounts:
                print(account["name"],":",account["accnum"])
                tacc = tacc + 1
                tmon = tmon +account["bal"]
                if bmax < account["bal"] :
                    bmax = account["bal"]
                    nmax = account["name"]
            print("Total Accounts:",tacc)
            print("Total Money in the bank: Rs.",tmon)
            print("Average Account Balance: Rs.",tmon/tacc)
            print("Account Holder:",nmax,"Has Maximum Balance of Rs.",bmax)
            print("Highest Balance Amount:",bmax)
    elif choose =='8':
        print("Good Bye!")
        break
    else:
        print("Invalid Input!")