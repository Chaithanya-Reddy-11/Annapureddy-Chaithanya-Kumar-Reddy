
class Animal:
    def sound(self):
        print("aah!")
class Dog(Animal):
    def sound(self):
        print("Bark")
d = Dog()
d.sound()

class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        super().show()
        print("Class B")
b = B()
b.show()

class A:
    def display(self):
        print("Class A")
class B(A):
    def display(self):
        print("Class B")
class C(B):
    def display(self):
        print("Class C")
c = C()
c.display()

class Vehicle:
    def wheels(self):
        print("Vehicle has wheels")
class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")
class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")
c = Car()
b = Bike()
c.wheels()
b.wheels()

class Employee:
    def salary(self):
        return 30000
class Manager(Employee):
    def salary(self):
        return super().salary() + 10000
e = Employee()
m = Manager()
print(e.salary())
print(m.salary())

class University:
    name = "MIT"
    @classmethod
    def show(cls):
        print("University:", cls.name)
class College(University):
    pass
College.show()

class MathOps:
    @staticmethod
    def add(a, b):
        return a + b
class AdvancedOps(MathOps):
    pass
print(AdvancedOps.add(5, 3))

class Father:
    def skills(self):
        print("Father: Driving")
class Mother:
    def skills(self):
        print("Mother: Cooking")
class Child(Father, Mother):
    pass
c = Child()
c.skills()
class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
s = Student("Chaithanya", 101)
print(s.name, s.roll)

class A:
    def __init__(self):
        print("Init A")
    def feature(self):
        print("Feature from A")

class B(A):
    def __init__(self):
        super().__init__()   # calls A's __init__
        print("Init B")
    def feature(self):
        super().feature()    # calls A's feature
        print("Feature from B")

class C(A):
    def __init__(self):
        super().__init__()   # calls A's __init__
        print("Init C")
    def feature(self):
        super().feature()    # calls A's feature
        print("Feature from C")

class D(B, C):   # Multiple inheritance
    def __init__(self):
        super().__init__()   # follows MRO
        print("Init D")
    def feature(self):
        super().feature()    # follows MRO
        print("Feature from D")

d = D()
d.feature()
D.__mro__
print(D.__mro__)