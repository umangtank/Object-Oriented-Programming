
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves

e1 = Employee("Umang", 255000, "Instructor")

#print(e1.salary)

e1.change_leaves(43)
print(e1.no_of_leaves)

