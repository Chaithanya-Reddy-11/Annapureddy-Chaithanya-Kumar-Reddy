class Student:
    total_students = 0
    passing_mark = 40
    students_list = []
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1
        Student.students_list.append(self)
    def has_passed(self):
        return self.marks >= Student.passing_mark
    @classmethod
    def curve_marks(cls, percentage):
        for student in cls.students_list:
            student.marks += student.marks * (percentage / 100)
    @staticmethod
    def convert_to_grade(marks):
        if marks >= 90: return "A"
        elif marks >= 75: return "B"
        elif marks >= 60: return "C"
        elif marks >= 40: return "D"
        else: return "F"
# Demonstration
s1 = Student("Alice", 35)
s2 = Student("Bob", 80)
s3 = Student("Charlie", 60)
print("Before curve:")
for s in Student.students_list:
    print(s.name, s.marks, Student.convert_to_grade(s.marks), s.has_passed())
Student.curve_marks(10)
print("\nAfter curve:")
for s in Student.students_list:
    print(s.name, s.marks, Student.convert_to_grade(s.marks), s.has_passed())

class Course:
    total_courses = 0
    min_duration = 3

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.enrolled_students = []
        Course.total_courses += 1

    def enroll_student(self, student_name):
        self.enrolled_students.append(student_name)

    @classmethod
    def update_min_duration(cls, duration):
        cls.min_duration = duration

    @staticmethod
    def is_valid_duration(duration):
        return 0 < duration < 60

# Demonstration
c1 = Course("Math", 4)
c1.enroll_student("Alice")
c2 = Course("Science", 2)

print(c1.title, c1.enrolled_students)
Course.update_min_duration(5)
print("Valid duration?", Course.is_valid_duration(100))


class Inventory:
    total_items = 0              # Shared count of all items across inventories
    min_stock_threshold = 5      # Shared minimum safe stock level

    def __init__(self):
        self.stock = {}          # Each inventory object has its own stock dictionary

    def add_stock(self, item, qty):
        # Add items to this inventory
        self.stock[item] = self.stock.get(item, 0) + qty
        Inventory.total_items += qty

    def remove_stock(self, item, qty):
        # Remove items if available in enough quantity
        if item in self.stock and self.stock[item] >= qty:
            self.stock[item] -= qty
            Inventory.total_items -= qty

    @classmethod
    def update_threshold(cls, threshold):
        # Update shared minimum stock threshold
        cls.min_stock_threshold = threshold

    @staticmethod
    def is_below_threshold(qty):
        # Check if a given quantity is below threshold
        return qty < Inventory.min_stock_threshold


# ---------------- DEMONSTRATION ----------------

# Create objects (instances of Inventory)
inv1 = Inventory()   # OBJECT → Inventory instance with its own stock
inv2 = Inventory()   # OBJECT → Another Inventory instance with its own stock

# Add stock to inv1
inv1.add_stock("Apples", 10)
print("Inventory 1 stock:", inv1.stock)   # Shows {"Apples": 10}
print("Total items across inventories:", Inventory.total_items)

# Add stock to inv2
inv2.add_stock("Bananas", 5)
print("Inventory 2 stock:", inv2.stock)   # Shows {"Bananas": 5}
print("Total items across inventories:", Inventory.total_items)

# Check threshold
print("Is 3 below threshold?", Inventory.is_below_threshold(3))   # True (threshold = 5)

# Update threshold for all inventories
Inventory.update_threshold(2)
print("Is 1 below new threshold?", Inventory.is_below_threshold(1))   # True (threshold = 2)
# Remove stock from inv1
inv1.remove_stock("Apples", 4)
print("Inventory 1 after removal:", inv1.stock)
print("Total items across inventories:", Inventory.total_items)


class LibraryMember:
    total_members = 0
    borrow_limit = 3

    def __init__(self, name):
        self.name = name
        self.books_borrowed = 0
        LibraryMember.total_members += 1

    def borrow_book(self, title):
        if self.books_borrowed < LibraryMember.borrow_limit and LibraryMember.is_valid_title(title):
            self.books_borrowed += 1
            print(f"{self.name} borrowed '{title}'")
        else:
            print(f"{self.name} cannot borrow '{title}'")

    @classmethod
    def update_borrow_limit(cls, limit):
        cls.borrow_limit = limit

    @staticmethod
    def is_valid_title(title):
        return isinstance(title, str) and 0 < len(title) < 100

# Demo
m1 = LibraryMember("Alice")
m2 = LibraryMember("Bob")
m1.borrow_book("Python Basics")
LibraryMember.update_borrow_limit(5)
m1.borrow_book("Data Science")
