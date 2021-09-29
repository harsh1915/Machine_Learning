import functools

def only_int_allow(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        for i in args:
            if type(i)!= int:
                return f"{type(i)} is not allow here !"
        return function(*args, **kwargs)
    return wrapper

@only_int_allow
def all_total(*args):
    total= 0
    for i in args:
        total+= i
    return total

ls=[1, 2, 3, 4]
print(all_total(ls))
print(all_total(*ls, 1, 2, 3, 4))
print(all_total(*ls, 1, 2, 3, 4, "Harsh"))