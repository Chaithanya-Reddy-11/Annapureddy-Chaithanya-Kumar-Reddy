class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        return self.marks > 40
s1 = Student("Alice", 35)
s2 = Student("Bob", 75)
print(f"{s1.name} Passed? {s1.is_passed()}")
print(f"{s2.name} Passed? {s2.is_passed()}")
