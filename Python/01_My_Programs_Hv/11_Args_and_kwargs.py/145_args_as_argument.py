def multiply_nums(*args):      
    multiply= 1
    for i in args:
        multiply*= i
    return multiply

ls= list(range(1, 6))
print(multiply_nums(ls))
print(multiply_nums(*ls))       # unpack of argument
