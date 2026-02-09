from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("Car Engine Started with Key/Ignition")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike Engine Started with Self/Kick")
class Bus(Vehicle):
    def start_engine(self):
        print("Bus Engine Started with Heavy Ignition System")
v1 = Car()
v2 = Bike()
v3 = Bus()
v1.start_engine()
v2.start_engine()
v3.start_engine()

#DAY Feb 9
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def sleep(self):
        print("Animal is sleeping")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
class Cow(Animal):
    def sound(self):
        print("Moo")
d = Dog()
c = Cat()
co = Cow()
d.sound()
d.sleep()
c.sound()
c.sleep()
co.sound()
co.sleep()

