class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def check_balance(self):
        print("Current Balance: ₹", self.balance)
    def deposit(self, amount):
        self.balance += amount
        print("₹", amount, "deposited successfully!")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print("₹", amount, "withdrawn successfully!")

account = BankAccount("Nirmaljeet", 1000)

while True:
    print("\n====== BANK ACCOUNT ======")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: ₹"))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: ₹"))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you for using the Bank Account System!")
        break

    else:
        print("Invalid Choice!")