from functools import reduce
a=[1,2,3,4,5,6,7,8,9,10]
k=list(map(lambda x:x**2,a))
m=list(filter(lambda x:x%2==1,k))
n=reduce(lambda x,y:x+y,m,0)
print(n)

l=reduce(lambda x,y:x+y,filter(lambda x:x%2==1,map(lambda x:x**2,a)))
print(l)


class student:
    pass_marks=25
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Student Name : ",self.name)
        print("Marks : ",self.marks)
    @classmethod
    def update_pass_marks(cls,marks):
        cls.pass_marks=marks
    @staticmethod
    def check_marks(marks):
        if marks >=student.pass_marks:
            return "Passed"
        return "Failed"

s=student(name="Reddy",marks=25)
s.display()
print("Updating marks")
student.update_pass_marks(student.pass_marks)
student.update_pass_marks(28)
print(student.pass_marks)
print(student.check_marks(25))

