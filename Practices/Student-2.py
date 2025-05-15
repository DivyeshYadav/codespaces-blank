class Student:
    grade = 5
    name = "Divyesh Yadav"

    def intro(self):
        print("Hi I am a student")

    def about(self):
        print("Hi am a student of grade ",self.grade,"and my name is ",self.name)

obj = Student()
obj.intro()
obj.about()
