import re
def home():
    print("1. Validate Email")
    print("2. Validate Mobile Number")
    print("3. Validate PIN Code")
    print("4. Validate Password")
    print("5. Exit")
def emailvalid(email):
    if re.fullmatch(r"[\w\.-]+@[\w\.-]+\.\w+", email):
        return True
    else:
        return False
def mobilevalid(mobile):
    if re.fullmatch(r"\d{10}", mobile):
        return True
    else:
        return False
def zipvalid(pin):
    if re.fullmatch(r"\d{6}", pin):
        return True
    else:
        return False
def passwordvalid(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    if re.fullmatch(pattern, password):
        return True
    else:
        return False
while True:
    home()
    temp = input("choose an option: ")
    if temp == "1":
        email = input("Email: ")
        if emailvalid(email):
            print("VALID EMAIL")
        else:
            print("INVALID EMAIL")
    elif temp == "2":
        mobile = input("Mobile Number: ")
        if mobilevalid(mobile):
            print("VALID MOBILE NUMBER")
        else:
            print("INVALID MOBILE NUMBER")
    elif temp == "3":
        pin = input("Pin Code: ")
        if zipvalid(pin):
            print("VALID Pin Code")
        else:
            print("INVALID Pin Code")
    elif temp == "4":
        password = input("Password: ")
        if passwordvalid(password):
            print("VALID PASSWORD")
        else:
            print("INVALID PASSWORD")
    elif temp == "5":
        print("Good Bye!")
        break
    else:
        print("INVALID INPUT")
