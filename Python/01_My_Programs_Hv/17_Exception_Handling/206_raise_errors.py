def add(int1, int2):
    if (type(int1) is int) and (type(int2) is int):
        return int1+ int2
    return "Invalid data for this function !"

print(add(2, 3))
print(add("2", "3"))

def add_2(int1, int2):
    if (type(int1) is int) and (type(int2) is int):
        return int1+ int2
    raise TypeError("Invalid data for this function !")         # raise error

print(add_2(2, 3))
print(add_2("2", "3"))