"""
way to define a function

P-> A-> D-> K

P --> Normal Parameters     --> name
A --> *args                 --> name, *args
D --> Defualt parameters    --> name, *args, age= 22
K --> **kwargs              --> name, *args, age= 22, **kwargs
"""

def func(name, *args, age= 22, **kwargs):
    print(name)
    print(args)
    print(age)
    print(kwargs)
func("Harsh")
func("Rohan", [1, 2, 3])
func("Bhargav", 4, 5, 6, a= 1, b= 2)