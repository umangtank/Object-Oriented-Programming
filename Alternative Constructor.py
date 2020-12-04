
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))


e1 = Employee("Umang", 255, "Instructor")
e2 = Employee("Rohan", 455, "Student")
e3 = Employee.from_dash("Karan-480-Student")

print(e3.no_of_leaves)
print(e3.salary)


