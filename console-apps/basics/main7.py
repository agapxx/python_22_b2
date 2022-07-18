# Py OOP (classes & objects)
class Human:
    def __init__(self,gender,complexion,race):
        self.gender = gender
        self.complexion = complexion
        self.race = race

    def introduction(self):
        print(f"Hello goons, my gender is {self.gender} and I am {self.complexion} in complexion")


# object creation
man = Human("Male","Dark","Black")
woman = Human("Female","Fair","Black")
bob = Human("Stupidity","Bleach","Unknown")

print(man.gender)
print(bob.gender)
print(woman.gender)
bob.introduction()
man.introduction()
woman.introduction()

bob.gender = "madness"
bob.introduction()
man.introduction()

del bob.complexion
bob.introduction()
man.introduction()

#Inheritance
class Vehicle:
    def __init__(plchd,type,wheelNo,seats,color,weight):
        plchd.type = type
        plchd.wheelNo = wheelNo
        plchd.seats = seats
        plchd.color = color
        plchd.weight = weight


    def description(obj):
        print(f"{obj.} has {obj.wheelNo} wheels and {obj.seats} seats. The color is {obj.color} and its weight is {obj.weight}")

# v = Vehicle("Truck",48,5,"Velvet",12.6)
# v.description()

class Car(Vehicle):
        pass

suv = Car()
suv.description("SUV",4,8,"Gray",103.9)
suv.description()



