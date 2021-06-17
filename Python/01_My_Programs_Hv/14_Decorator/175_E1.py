import time
def decorator_function(function):
    def wrapper(*args, **kwargs):
        t1= time.time()
        return_value= function(*args, **kwargs)
        t2= time.time()
        print(f"{function.__name__} Took {t2- t1} Total time to Execute !")
        return return_value
    return wrapper
    
@decorator_function
def square(n):
    return [i** 2 for i in range(1, n+ 1)]

print(square(3))