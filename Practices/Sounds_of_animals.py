class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Name of dog is {self.name} and age is {self.age}")
    def speak(self):
        print("Woof Woof")
class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Name of cat is {self.name} and age is {self.age}")
    def speak(self):
        print("Meow Meow")

d = dog("Banjo",2)
d.info()
d.speak()
c = cat("Tommy",3)
c.info()
c.speak()