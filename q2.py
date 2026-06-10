class Employee:
    company_name = "TechCorp"
    def __init__(self, name):
        self.name = name
    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name
e1 = Employee("John")
e2 = Employee("Jane")
print(e1.company_name, e2.company_name)
Employee.change_company("NextGenTech")
print(e1.company_name, e2.company_name)
