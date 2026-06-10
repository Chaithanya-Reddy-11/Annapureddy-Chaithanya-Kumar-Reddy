class Animal:
    def make_sound(self):
        print("Some generic animal sound")
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")
class Cat(Animal):
    def make_sound(self):
        print("Meow! Meow!")
class Cow(Animal):
    def make_sound(self):
        print("Moo! Moo!")
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.make_sound()



def operate(device):
    device.start()

class Car:
    def start(self):
        print("Car engine started!")

class Computer:
    def start(self):
        print("Computer booting up...")

class WashingMachine:
    def start(self):
        print("Washing machine cycle started!")

car = Car()
computer = Computer()
wm = WashingMachine()

devices = [car, computer, wm]

for d in devices:
    operate(d)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
print(2 + 3)
print("Hello" + "World")
print([1, 2] + [3, 4])
v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)


class Transport:
    def move(self):
        print("Transport is moving...")
class Bus(Transport):
    def move(self):
        super().move()
        print("Bus is carrying passengers on the road.")
class Bike(Transport):
    def move(self):
        super().move()
        print("Bike is zipping through traffic.")
vehicles = [Bus(), Bike()]
for v in vehicles:
    v.move()

class Payment:
    def process(self, amount):
        print(f"Processing payment of {amount}")
class CreditCardPayment(Payment):
    def process(self, amount, card_type="Visa"):
        print(f"Processing {card_type} card payment of {amount}")
p = Payment()
p.process(100)
c = CreditCardPayment()
c.process(200, "MasterCard")

class Sorter:
    def change(self, strategy):
        self.strategy = strategy
    def sort(self, data):
        self.strategy.logic(data)
class BS:
    def logic(self, data):
        print("Bubble Sort:", sorted(data))
class MS:
    def logic(self, data):
        print("Merge Sort:", sorted(data))
class QS:
    def logic(self, data):
        print("Quick Sort:", sorted(data))

s = Sorter()
for i in [BS(), MS(), QS()]:
    s.change(i)
    s.sort([3, 1, 2])

class Account:
    def withdraw(self):
        print("Withdraw from Account")
class SavingsAccount(Account):
    def withdraw(self):
        print("Withdraw from Savings Account")
class PremiumSavingsAccount(SavingsAccount):
    def withdraw(self):
        super().withdraw()
        print("Extra benefits for Premium Account")
for i in [Account(), SavingsAccount(), PremiumSavingsAccount()]:
    i.withdraw()

def draw(shape):
    shape.draw()
class Circle:
    def draw(self): print("Drawing Circle")
class Square:
    def draw(self): print("Drawing Square")
class Rectangle:
    def draw(self): print("Drawing Rectangle")
class Car:
    def draw(self): print("Drawing Car")
for s in [Circle(), Square(), Rectangle(), Car()]:
    draw(s)

class UPI:
    def pay(self):
        print("Paying via UPI")
class Card:
    def pay(self):
        print("Paying via Card")
class Cash:
    def pay(self):
        print("Paying via Cash")
for method in [UPI(), Card(), Cash()]:
    if isinstance(method, UPI):
        method.pay()
    elif isinstance(method, Card):
        method.pay()
    elif isinstance(method, Cash):
        method.pay()

