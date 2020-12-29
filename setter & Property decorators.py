
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@abxy.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@abxy.com"

    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


e1 = Employee("Umang", "Tank")
# e2 = Employee("Nikhil", "kumar")

print(e1.email)

e1.fname = "raj"

print(e1.email)
e1.email = "this.that@abxy.com"
print(e1.fname)

del e1.email
print(e1.email)
e1.email = "ravina.raj@abxy.com"
print(e1.email)

