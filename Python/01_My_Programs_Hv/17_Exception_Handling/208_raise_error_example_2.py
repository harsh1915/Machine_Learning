class Mobile:
    def __init__(self, name):
        self.name= name

class Mobile_Store:
    def __init__(self):
        self.mobile_ls= []

    def add_mobile(self, new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobile_ls.append(new_mobile)
        else:
            raise TypeError("New mobile sould be object of mobile class !")

m1= Mobile("OnePlus 8")
ms1= Mobile_Store()

print(ms1.mobile_ls)
ms1.add_mobile(m1)
print(ms1.mobile_ls)

ms1_ls= ms1.mobile_ls
print(ms1_ls[0].name)