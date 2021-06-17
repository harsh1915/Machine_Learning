def decorator_function(function):
    def wrapper_function(*args, **kwargs):
        print(f"You are calling a {function.__name__} function")
        print(function.__doc__)
        return function(*args, **kwargs)
    return wrapper_function

@decorator_function
def add(num1, num2):
    """This is add Function !"""
    return num1+ num2

print(add(25, 26))