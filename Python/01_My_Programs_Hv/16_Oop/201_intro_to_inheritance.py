class Phone:
    def __init__(self, brand, model, price):
        self.brand= brand
        self.model= model
        self.price= max(price, 0)

    @property
    def complete_name(self):
        return (f"{self.brand} {self.model}")

    def make_a_call(self, number):
        return f"calling to {number} ......."

class Smartphone(Phone):
    def __init__(self, brand, model, price, ram, rom):
        super().__init__(brand, model, price)
        self.ram= ram
        self.rom= rom

p1= Phone("Nokia", "NK_1100", 1000)
sp1= Smartphone("OnePlus", "5T", 2000, "8_GB", "64_GB")
print(p1.complete_name)
print(f"{sp1.complete_name} and price is {sp1.price}")