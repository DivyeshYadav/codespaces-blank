class Person:
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(f"Your name is {self.name}")
        print(f"Your idnumber is {self.idnumber}")

class Emplyoee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.name = name
        self.idnumber = idnumber
        self.salary = salary
        self.post = post
        Person.__init__(self,name,idnumber) 

emplyoee = Emplyoee("Rohan",35552564,50000,"Proffesor")
emplyoee.display()