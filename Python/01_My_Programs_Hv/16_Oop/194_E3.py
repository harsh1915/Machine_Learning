class Person:
    count_instance= 0
    def __init__(self, name, age):
        Person.count_instance+= 1
        self.name= name
        self.age= age

p1= Person("Harsh", 22)
print(Person.count_instance)

p2= Person("Rohan", 23)
print(Person.count_instance)