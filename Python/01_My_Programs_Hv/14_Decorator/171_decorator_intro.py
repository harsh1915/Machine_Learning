# Decorators = incraese the functionality of other functions
# @ --> use for decorators
def func1():
    print("This is function 1 !")

def decorator_function(function):
    def wrapper_function():
        print("This is awesome function !")
        function()
    return wrapper_function
var= decorator_function(func1)
var()

@decorator_function
def func2():
    print("This is function 2 !")
func2()