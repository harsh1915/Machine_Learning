class Animal:
    def __init__(self, name):
        self.name= name

    @property
    def sound(self):            # abstract mahtod
        raise NotImplementedError("You have to deffine sound mathod in subclasses !")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed= breed

    @property
    def sound(self):
        return "Bhow Bhow"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed= breed

d1= Dog("Tom", "Pug")
print(d1.sound)

c1= Cat("Jerry", "Pug")
print(c1.sound)