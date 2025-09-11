class Employee:
    def __init__(self):
        print("Emplyoee passed the interview and is hired!")
    def __del__(self):
        print("Employee is fired!")

obj = Employee()
del obj
        

    