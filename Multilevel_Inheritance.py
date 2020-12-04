
class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Yes I dance very awesomely {self.dance} no of times"

d1 = Dad()
s1 = Son()
g1 = Grandson()

print(g1.guitar)
print(g1.isdance())




