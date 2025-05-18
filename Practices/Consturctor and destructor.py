class Employee:
    def __init__(self):
        print("Employeee added")
    def __del__(self):
        print("Employee removed")

ob = Employee()
del ob