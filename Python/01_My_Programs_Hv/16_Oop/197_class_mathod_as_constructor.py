class Person:
    def  __init__(self, firstname, lastname, age):
        self.firstname= firstname
        self.lastname= lastname
        self.age= age

    @classmethod
    def from_string(cls, string):
        firstname, lastname, age= string.split(",")
        return cls(firstname, lastname, age)
    
    def complete_name(self):
        return f"{self.firstname} {self.lastname}"

p1= Person("Harsh", "Darji", 22)
print(p1.complete_name())
p2= Person.from_string("Rohan,Katri,23")
print(p2.__dict__)