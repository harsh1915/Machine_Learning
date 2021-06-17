class Phone:
    def __init__(self ,brand, model, price):
        self.brand= brand
        self.model= model
        self._price= price

    @property
    def complete_name(self):
        return f"{self.brand} {self.model}"

    def make_phonecall(self, number):
        return f"Calling to {number} ....."

class Smart_Phone(Phone):
    def __init__(self, brand, model, price, ram, rom):
        super().__init__(brand, model, price)

        self.ram= ram
        self.rom= rom

    @property
    def complete_name(self):            # mathod overriding
        return f"{super().complete_name} and price is {self._price}"

class Flagship_Phone(Smart_Phone):          # --> multilevel inheritance
    def __init__(self, brand, model, price, ram, rom, rear_camera, front_camera):
        super().__init__(brand, model, price, ram, rom)

        self.rear_camera= rear_camera
        self.front_camera= front_camera

    @property
    def complete_name(self):            # mathod overriding
        return f"{super().complete_name} and rear camera is {self.rear_camera}"

p1= Phone("Nokia", "NK_1100", 1000)
sp1= Smart_Phone("OnePlus", "5T", 2000, "8_GB", "64_GB")
fp1= Flagship_Phone("Apple", "8", 30000, "2 GB", "32 GB", "8 MP", "5 MP")

print(p1.complete_name)
print(sp1.complete_name)
print(fp1.complete_name)

# print(help(Flagship_Phone))         # mathod resolution order 