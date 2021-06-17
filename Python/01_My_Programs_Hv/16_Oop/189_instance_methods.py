class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname= firstname
        self.lastname= lastname
        self.age= age

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def is_above_22(self):
        return self.age>22

p1= Person("Harsh", "Darji", 22)
p2= Person("Rohan", "Khatri", 23)

print(p1.firstname)
print(p2.lastname)

print(p2.fullname())
print(p2.is_above_22())