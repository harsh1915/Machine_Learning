class Circle:
    pi= 3.14            # class variable --> pi= 3.14
    def __init__(self, radius):
        self.radius= radius

    def circumference(self):
        return 2* Circle.pi* self.radius            # class variable called by --> Circle

c1= Circle(4)
print(c1.circumference())