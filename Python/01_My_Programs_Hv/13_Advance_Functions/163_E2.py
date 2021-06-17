def my_sum(*args):
    total= 0
    if any(type(i)!= (int or float) for i in args):
        return "Invalid Input !" 
    else:
        for i in args:
            total+= i
        return total

ls= list(range(1, 11))
print(my_sum(*ls, 3))
print(my_sum(*ls, 3, "harsh"))