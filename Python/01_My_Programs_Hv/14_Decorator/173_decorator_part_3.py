import functools
def decorator_function(function):
    @functools.wraps(function)          # This is a convenience function to simplify applying partial() to update_wrapper().
    def wrapper_function(*args, **kwargs):
        """ This is wrapper function !"""
        print("This is awesome function !")
        return function(*args, **kwargs)
    return wrapper_function

@decorator_function
def add(num1, num2):
    """This is add function !"""
    return num1+ num2
print(add.__doc__)