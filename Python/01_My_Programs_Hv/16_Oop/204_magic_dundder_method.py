class Phone:
    def __init__(self ,brand, model, price):
        self.brand= brand
        self.model= model
        self._price= price

    def complete_name(self):
        return f"{self.brand} {self.model}"

    def __str__(self):          # pretiontatin for normal users
        return f"{self.brand} {self.model} and price is {self._price} !"

    def __repr__(self):         # pretiontatin for normal devlopers
        return f"Phone('{self.brand}', '{self.model}', '{self._price}')"

    def __len__(self):
        return len(self.complete_name())

    def __add__(self, other):           # operator overloding
        return self._price + other._price

    def __mul__(self, other):           # operator overloding
        return self._price * other._price

class Smart_Phone(Phone):
    def __init__(self, brand, model, price, camera):
        super().__init__(brand, model, price)
        self.camera= camera

    @property
    def complete_name(self):
        return f"{super().complete_name()} and camera is {self.camera} !"

p1= Phone("Nokia", "NK_1100", 1000)
p2= Phone("Nokia", "NK_1200", 1200)
sp1= Smart_Phone("OnePlus", 8, 30000, "8 MP")

print(p1)
print(repr(p1))
print(len(p1))

print(p1+ p2)
print(p1* p2)

print(p1.complete_name())
print(sp1.complete_name)