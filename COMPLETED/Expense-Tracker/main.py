expenses = []
while True:    
    print("====== EXPENSE TRACKER ======\n")
    print("1. Add Expense\n2. View Expense\n3. Show Expense\n4. Exit\n\n")
    choice = input("Choose an option: ")
    if choice =='1':
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))
        expense = {
        "category" :category,"amount" : amount
        }
        expenses.append(expense)
        print("Expense Added Successfully!")
    elif choice == '2':
        if len(expenses) ==0:
            print("No expenses found!")
        else:
            print("\n===== EXPENSE LIST =====")
            for expense in expenses:
                print("Category: ",expense["category"])
                print("Amount: ₹",expense["amount"])
                print("----------------------")
        
    elif choice =='3':
        total = 0
        for expense in expenses:
            total = total + expense["amount"]
        print("\n===== TOTAL EXPENSE =====")
        print("Total Spent: ₹",total)
        
        
    elif choice == '4':
        print("Good Bye!")
        break
    else:
        print("Invalid Input")
