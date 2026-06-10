# class MathOps:
#     @staticmethod
#     def is_even(num):
#         return num % 2 == 0
# print(MathOps.is_even(10))
# m = MathOps()
# print(m.is_even(15))
from os import name


# class Car:
#     wheels = 4
#     def __init__(self, mileage):
#         self.mileage = mileage
#     def display_specs(self):
#         print(f"Mileage: {self.mileage}, Wheels: {Car.wheels}")
#     @classmethod
#     def change_wheels(cls, new_count):
#         cls.wheels = new_count
# c1 = Car(20)
# c1.display_specs()
# Car.change_wheels(6)
# c1.display_specs()


# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius
#
#     @staticmethod
#     def to_fahrenheit(celsius):
#         return (celsius * 9/5) + 32
#
#     def show_conversion(self):
#         print(f"{self.celsius}°C = {Temperature.to_fahrenheit(self.celsius)}°F")
#
# # Demo
# t = Temperature(25)
# t.show_conversion()

# class Book:
#     total_count=0
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#         Book.total_count+=1
#     @classmethod
#     def from_string(cls,book_str):
#         t,a=book_str.split("-")
#         return cls(t,a)
#     @staticmethod
#     def is_valid_title(title):
#         return len(title)>3
# b1 = Book("Python", "Guido")
# b2 =Book.from_string("Python-Guido")
# print(b2.title,b2.author)


# class Employee:
#     bonus_rate=0.1
#     def __init__(self,name,base_salary):
#         self.name=name
#         self.base_salary=base_salary
#     def final_salary(self):
#         return self.base_salary+(self.base_salary*Employee.bonus_rate)
#     @classmethod
#     def update_bonus(cls,new_rate):
#         cls.bonus_rate=new_rate
#     @staticmethod
#     def is_valid_salary (sal):
#         return sal >0
# e1 = Employee("Tom", 50000)
# e2 = Employee("Jerry", 60000)
# print(e1.final_salary(), e2.final_salary())
# Employee.update_bonus(0.2)
# print(e1.final_salary(), e2.final_salary())


# class Course:
#     total_students=0
#     def __init__(self,student_name):
#         self.name=student_name
#     def enroll(self):
#         Course.total_students+=1
#     @classmethod
#     def show_total(cls):
#         print("Total Students:",cls.total_students)
#     @staticmethod
#     def is_eligible(age):
#         return age>18
# c1 = Course("Alice")
# c1.enroll()
# c2 = Course("Bob")
# c2.enroll()
# Course.show_total()


# class  Student:
#     passing_marks=40
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def results(self):
#         if self.marks>=self.passing_marks:
#             return f"{self.name} Pass"
#         else:
#             return f"{self.name} Fail"
#     @classmethod
#     def update_passing_marks(cls,new_marks):
#         cls.passing_marks=new_marks
#
#     @staticmethod
#     def grade_category(marks):
#         if marks >= 75:
#             return "A"
#         elif marks >= 50:
#             return "B"
#         else:
#             return "C"
# s1 = Student("Alice", 55)
# s2 = Student("Bob", 30)
# print(Student.grade_category(s1.marks))

# class BankAccount:
#     bank_name = "Global Bank"
#     def __init__(self, holder, balance=0):
#         self.holder = holder
#         self.balance = balance
#     def deposit(self, amount):
#         if BankAccount.validate_amount(amount):
#             self.balance += amount
#             print(f"{self.holder} deposited {amount}. New balance: {self.balance}")
#         else:
#             print("Invalid amount")
#     @classmethod
#     def change_bank_name(cls, new_name):
#         cls.bank_name = new_name
#     @staticmethod
#     def validate_amount(amount):
#         return amount > 0
# acc = BankAccount("Alice", 1000)
# acc.deposit(500)
# BankAccount.change_bank_name("NextBank")
# print(BankAccount.bank_name)


# class student:
#     total_no_of_students = 0
#     max_marks=100
#     passing_marks=50
#     def __init__(self, name,marks):
#         self.name = name
#         self.marks = marks
#     def is_passed(self):
#         print("Student Name = " +self.name)
#         print(f"Percentage ; {self.marks/self.max_marks*100:.2f}%")
#         if self.marks >= self.passing_marks:
#             print("Passed")
#         else:
#             print("Failed")
#     @classmethod
#     def curve_marks(cls,mm):
#         cls.max_marks=mm
#     @staticmethod
#     def grade(marks):
#         if marks >= 90:
#             print("Grade: A")
#         elif marks >= 80:
#             print("Grade: B")
#         elif marks >= 70:
#             print("Grade: C")
#         elif marks >= 60:
#             print("Grade: D")
#
# s1=student("Sarah",30)
# s2=student("Reddy",50)
# s1.is_passed()
# s2.is_passed()
# s1.grade(70)
# student.curve_marks(90)
# s1=student("Ruthu",30)
# s1.is_passed()


# class LibraryMember:
#     total_active=0
#     books_limit=5
#     def __init__(self, name,bbooks):
#         self.name = name
#         self.books_borrowed=bbooks
#         self.is_active = True
#         LibraryMember.total_active += 1
#
#     def borrow_books(self,b):
#         if self.books_borrowed+b <= self.books_limit:
#             self.books_borrowed += b
#             print("Borrowed Books Succesfully")
#         else:
#             print("Limit Crossed")
#         @classmethod
#         def update_bookss(cls,nl):
#             cls.books_limit = nl
#         @staticmethod
#         def valid(title):
#             if not title:
#                 return "Empty Title"
#             elif len(title) >6:
#                 return "Valid Title"
#             else:
#                 "Lenght of title id too short"
















