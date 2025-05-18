class Parrot:
    species = "bird"

    def __init__(self,name,age) :
        self.name = name
        self.age = age

inpar = Parrot("inpar",5)
nepar = Parrot("nepar",7)

print("Inpar is a {}".format(inpar.species))
print("Nepar is a {}".format(nepar.species))
print("{} is {} years old".format(inpar.name,inpar.age))
print("{} is {} years old".format(nepar.name,nepar.age))