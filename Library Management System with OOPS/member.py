class Member:
    def __init__(self,mid,name,age,gender,phone,email):
        self.mid = mid
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.email = email
    def display(self):
        print("Member ID:",self.mid)
        print("Name     :",self.name)
        print("Age      :",self.age)
        print("Gender   :",self.gender)
        print("Phone    :",self.phone)
        print("Email ID :",self.email)