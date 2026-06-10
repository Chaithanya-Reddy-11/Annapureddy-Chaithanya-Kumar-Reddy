class Hero:
    def __init__(self,name,health):
        self.name=name
        self.health=health
        self.is_alive=True
    def take_damage(self,amount):
        self.health -= amount
        print( self.health)
        if self.health<=0:
            self.is_alive=False
            self.health=0
            return self.health
    def display(self):
        print("Health is ",self.health)
    def heal_amount(self,amount1):
        if self.is_alive is True:
            self.health+=amount1
            print("after heal",self.health)
            if self.health > 100:
                self.health = 100
        else:
            print("Cannot Heal to fallen hero")
h1=Hero("Hulk",100)
h1.display()
h1.take_damage(40)
h1.heal_amount(40)

class Laptop:
    def __init__(self,brand,ram,price):
        self.brand = brand
        self.ram = ram
        self.price = price
    def upgrade_ram(self,extra_ram):
        self.ram = self.ram + extra_ram
    def __str__(self):
        return f"Brand : {self.brand}, Ram : {self.ram} , Price : {self.price}"
    def __add__(self,other):
        return self.price + other.price
    def __mul__(self, qty):
        return self.price*qty
    def __lt__(self, other):
        return self.price < other.price
    def __eq__(self, other):
        return self.ram == other.ram
    def __getattribute__(self, name):
        print(name)
        return super().__getattribute__(name)
    def __setattr__(self, name, value):
        if name in ["ram", "price"] and value <= 0:
            print(f"{name} must be positive")
        super().__setattr__(name, value)

l1 = Laptop("Dell", 8, 50000)
l2 = Laptop("HP", 16, 60000)
print(l1)
print(l2)
l1.upgrade_ram(4)
print("After upgrade:", l1)
print("Total Price:", l1 + l2)
print( l1 * 5)
print( l1 < l2)
print( l1 == l2)

class Book:
    def __init__(self, book_name, isbn_number, is_borrowed=False):
        self.book_name = book_name
        self.isbn_number = isbn_number
        self.is_borrowed = is_borrowed
    def __str__(self):
        return f"Book({self.book_name}, ISBN={self.isbn_number}, Borrowed={self.is_borrowed})"
class User:
    max_limit = 3
    def __init__(self, name):
        self.name = name
        self.borrowed = 0
        self.books = []
    def __add__(self, book):
        if self.borrowed < User.max_limit and not book.is_borrowed:
            self.books.append(book)
            book.is_borrowed = True
            self.borrowed += 1
        else:
            print("Cannot borrow book")
    def __sub__(self, book):
        if book in self.books:
            self.books.remove(book)
            book.is_borrowed = False
            self.borrowed -= 1
    def __contains__(self, book):
        return book in self.books
    def __len__(self):
        return self.borrowed
    def __str__(self):
        return f"User({self.name}, Books Borrowed={self.borrowed})"


b1 = Book("Python Basics", 12345)
b2 = Book("Data Science", 67890)
b3 = Book("Data Science", 67890)
b4= Book("Data Science", 67890)
u1 = User("Chaithanya")
u2=User("Chaithanya")
u1 + b1
u1 + b2
u1+b3
u1+b4
print("hi",u1)
print(b1 in u1)
print("Total borrowed:",len(u1))
u1 - b1
print(u1)
print(b1 in u1)
print("Total borrowed:", len(u1))
