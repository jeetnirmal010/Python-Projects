class Student:
    def __init__(self,sid,name,age,gender,_class,section,rollno,eng,math,sci,cont):
        self.sid = sid
        self.name = name
        self.age = age
        self.gender = gender
        self._class = _class
        self.section = section
        self.rollno = rollno
        self.eng = eng
        self.math = math
        self.sci = sci
        self.cont = cont
    def display(self):
        print("Student ID:",self.sid)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Class:",self._class)
        print("Section:",self.section)
        print("Roll No:",self.rollno)
        print("English Marks:",self.eng)
        print("Math Marks:",self.math)
        print("Science Marks:",self.sci)
        print("Contact:",self.cont)