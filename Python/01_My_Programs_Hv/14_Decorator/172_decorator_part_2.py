def decorator_function(function):
    def wrapper_function(*args, **kwargs):
        print("This is awesome function !")
        return function(*args, **kwargs)
    return wrapper_function

@decorator_function
def func1(a):
    print(f"This is function with argument {a}")
func1(5)

@decorator_function
def add(num1, num2):
    return num1+ num2
print(add(25, 26))