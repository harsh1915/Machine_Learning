class Laptop:
    def __init__(self, brand, model, price):
        self.brand= brand
        self.model= model
        self.price= price
        self.brand_model= brand+ " "+ model

l1= Laptop("HP", "M1", 31000)
l2= Laptop("HP", "M2", 32000)

print(l1.price)
print(l2.model)
print(l2.brand_model)