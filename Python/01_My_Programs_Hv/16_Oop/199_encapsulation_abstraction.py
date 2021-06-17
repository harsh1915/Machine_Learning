class Phone:
    def __init__(self, brand, model, price):
        self.brand= brand
        self._model= model
        self.__price= price

    def make_a_call(self, phone_number):
        return f"calling to {phone_number}......"

    def complete_name(self):
        return f"{self.brand} {self._model}"

p1= Phone("Nokia", "NK_1100", 1000)
print(p1._model)

print(p1.__dict__)
print(p1._Phone__price)