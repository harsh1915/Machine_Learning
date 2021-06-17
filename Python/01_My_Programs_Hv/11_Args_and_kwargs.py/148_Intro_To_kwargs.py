# kwargs --> keyword argument
# **kwargs --> Double star operator

# kwargs as a parameters
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
func(firstname= "Harsh", lastname= "Darji")

def func2(**kwargs):
    print({f"key is {key} and value is":value for key,value in kwargs.items()})
func2(firstname= "Harsh", lastname= "Darji")

d1= {"firstname":"Harsh", "lastname": "Darji"}
func2(**d1)         # Dictionary un packing