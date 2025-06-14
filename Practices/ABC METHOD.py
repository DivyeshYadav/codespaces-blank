from abc import ABC
class Animal(ABC):
    def move(self):
        pass

class Falcon(Animal):
    def move(self):
        print("Falcons can Fly")
class Fish(Animal):
    def move(self):
        print("Fish can swim")
class Lion(Animal):
    def move(self):
        print("Lions Roar")
class Monkey(Animal):
    def move(self):
        print("Monkeys can climb on trees")

F = Falcon()
F.move()
Fi = Fish()
Fi.move()
l = Lion()
l.move()
m = Monkey()
m.move()