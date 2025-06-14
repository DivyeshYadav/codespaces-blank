class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def display(self):
        print(f"Your fullname is {self.fname} {self.lname}")
class Student(Person):
    def __init__(self,fname,lname,gyear):
        self.fname = fname
        self.lname = lname
        self.gyear = gyear
        super().__init__(fname,lname)

student = Student("Divyesh","Yadav",2032)
student.display()
print(f"Your graduation year is {student.gyear}")
    