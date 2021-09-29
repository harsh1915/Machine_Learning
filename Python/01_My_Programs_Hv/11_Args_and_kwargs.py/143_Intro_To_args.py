# *Operator
# *args

def total(num1, num2):          # You can pass only two arguments
    return num1+ num2
print(total(9, 19))

def total_2(*args):           #Creates a tuple of all arguments
    print(args)
    print(type(args))

total_2(1, 2, 3, 4, 5, 6, 7)

def total_3(*args):
    return sum(args)

print(total_3(1, 2, 3, 4, 5))