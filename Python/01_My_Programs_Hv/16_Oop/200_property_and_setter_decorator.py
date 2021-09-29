class Phone:
    def __init__(self, brand, model, price):
        self.brand= brand
        self.model= model
        self._price= max(price, 0)
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, setter_price):
        self._price= max(setter_price, 0)

    @property
    def specs(self):
        return f"{self.brand} {self.model} and price is {self._price}"

    def make_a_call(self, phone_num):
        return f"calling to {phone_num} ....."

    def full_name(self):
        return f"{self.brand} {self.model}"

p1= Phone("Nokia", "NK_1100", 1000)

print(p1.brand)
print(p1.model)
print(p1.specs)
print(p1.__dict__)

p1._price= -500
print(p1.__dict__)

p1.price= -500
print(p1.specs)
print(p1.__dict__)

p1.price= 500
print(p1.specs)
print(p1.__dict__)