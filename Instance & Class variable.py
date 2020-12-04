class Employee:
    no_of_leaves = 8
    pass

e1 = Employee()
e2 = Employee()

e1.name = "Umang"
e1.salary = 455
e1.role = "Instructor"

e2.name = "Rohan"
e2.salary = 4554
e2.role = "Student"

print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)

