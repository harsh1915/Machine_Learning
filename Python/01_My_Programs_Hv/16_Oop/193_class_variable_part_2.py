class Laptop:
    discount= 10            # class variable --> discount= 10 
    def __init__(self, brand, model, price):
        self.brand= brand
        self.model= model
        self.price= price
        self.brand_model= brand+ " "+ model

    def sale_discount(self):
        return f"price of {self.brand_model} is {self.price- ((self.price* self.discount)/ 100)}"

l1= Laptop("Hp", "M1", 30000)
l2= Laptop("Dell", "M2", 50000)

print(l1.sale_discount())

l2.discount= 20             # we can change class variable by calling self

print(l2.__dict__)
print(l2.sale_discount())