# Abstraction is used to obscure background information or any
# other extraneous data implementation so that people only see
# what they need to see. The term "abstract class" refers to a class that contains one or
# more abstract methods. Python has an abstraction module called ABC.
from abc import ABC


class Vehicle(ABC): # Inherits abstract class
    # Abstract method
    def no_of_wheels(self):
        pass

class Cycle(Vehicle):
    def no_of_wheels(self): # Provide definition for abstract method
        print("Cycle has 2 wheels")

class Car(Vehicle):
    def no_of_wheels(self): # Provide definition for abstract method
        print("Car has 4 wheels")

class HeavyTruck(Vehicle):
    def no_of_wheels(self): # Provide definition for abstract method
        print("HeavyTruck has 8 wheels")

Cycle = Cycle()
Car = Car()
HeavyTruck = HeavyTruck()
for vehicles in (Cycle, Car, HeavyTruck):
    vehicles.no_of_wheels()
