class NameIsToShort(ValueError):        # inheritance of error class
    pass
def validate(name):
    if len(name)<8:
        raise NameIsToShort("Name is too short !")

name= input("Enter your name = ")
validate(name)
print(f"Hello {name} !")