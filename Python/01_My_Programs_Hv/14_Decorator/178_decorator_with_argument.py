import functools
def only_data_of(data_Type):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            for i in args:
                if type(i)!= data_Type:
                    return f"{type(i)} is not allow here !"
            return function(*args) 
        return wrapper
    return decorator

@only_data_of(int)
def add(*args):
    total= 0
    for i in args:
        total+= i
    return total
print(add(2, 3, 4, 5.0))