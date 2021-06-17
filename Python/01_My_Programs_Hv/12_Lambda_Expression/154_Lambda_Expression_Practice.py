def isodd_1(num):
    return num%2 != 0
print(isodd_1(2))
print(isodd_1)

isodd_2= lambda num : num%2 != 0
print(isodd_2(1))
print(isodd_2)

lastchar = lambda s : s[-1]
print(lastchar("Harsh"))

def func(s):
    if len(s)> 5:
        return True
    return False
print(func("Harsh"))

func2= lambda s : True if len(s)> 5 else False
print(func2("Harsh Darji"))