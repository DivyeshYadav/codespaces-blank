class Student:
    grade = "V"
    age = 10
    section = "B"
    school = "Delhi Public School"
    def introduction(self):
        print("Hello, I am Studet")
    def details(self):
        print("I am in grade ",self.grade)
        print("I am ",self.age," years old")
        print("I am in section ",self.section)
        print("I study in ",self.school)

obj = Student()
obj.introduction()
obj.details()