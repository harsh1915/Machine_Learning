class Laptop:
    discount= 10            # class variable --> discount= 10 
    def __init__(self, brand, model, price):
        self.brand= brand
        self.model= model
        self.price= price
        self.brand_model= brand+ " "+ model

    def apply_discount(self, num):
        return f"price of {self.brand_model} is {self.price- ((self.price*num)/ 100)}"

    def sale_discount(self):
        return f"price of {self.brand_model} is {self.price- ((self.price* Laptop.discount)/ 100)}"

l1= Laptop("Hp", "M1", 30000)
print(l1.apply_discount(20))

print(l1.sale_discount())