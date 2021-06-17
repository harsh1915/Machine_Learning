class Person:
    count_instance= 0
    def __init__(self, firstname, lastname, age):
        Person.count_instance+= 1
        self.firstname= firstname
        self.lastname= lastname
        self.age= age

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class !"

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def is_above_22(self):
        return self.age>22

p1= Person("Harsh", "Darji", 22)
p2= Person("Rohan", "Khatri", 23)

print(Person.count_instances())