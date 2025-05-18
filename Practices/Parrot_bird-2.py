class Parrot:
    species = "bird"

    def __init__(self,name,age,sing,dance) :
        self.name = name
        self.age = age
        self.sing = sing
        self.dance = dance

inpar = Parrot("inpar",5,"happily","energeticaly")
nepar = Parrot("nepar",7,"happily","energeticaly")

print("Inpar is a {}".format(inpar.species))
print("Nepar is a {}".format(nepar.species))
print("{} is {} years old".format(inpar.name,inpar.age))
print("{} is {} years old".format(nepar.name,nepar.age))
print("Inpar sings {}".format(inpar.sing))
print("Nepar also sings {}".format(nepar.sing))
print("Inpar dances {}".format(inpar.dance))
print("Nepar dances {}".format(nepar.dance))