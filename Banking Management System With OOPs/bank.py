class Bank:

    def __init__(self,accnum,name,age,gender,phone,email,addres,acctyp,balance,opendate,status):
        self.accnum = accnum
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.email = email
        self.addres = addres
        self.acctyp = acctyp
        self.opendate = opendate
        self.status = status
        self.__balance = balance

    def display(self):
        print("Account Number:",self.accnum)
        print("Customer Name:",self.name)
        print("Age:",self.age)
        print("Phone:",self.phone)
        print("Email ID:",self.email)
        print("Address:",self.addres)
        print("Account Type:",self.acctyp)
        print("Opening Date:",self.opendate)

    def balance_check(self):
        return self.__balance

    def deposit(self,amount):
        if amount <=0:
            print("Invalid Amount!...")
            return False
        else:
            self.__balance = self.__balance + amount
            return True

    def withdraw(self,amount):
        if amount > 0:
            if (self.__balance - amount) >=1000:
                self.__balance = self.__balance - amount
                return True
            else:
                print("Insufficient Balance!......")
                return False
        else:
            print("Invalid Amount!......")            
            return False

    def show_balance(self):
        print("Available Balance:Rs.",self.__balance)

    def _nullBalance(self):
        self.__balance = 0.00