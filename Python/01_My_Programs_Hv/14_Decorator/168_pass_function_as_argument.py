def square(num1):
    return num1** 2

ls= list(range(1, 11))
print(list(map(square, ls)))

def my_map(function, iterable):
    return [function(i) for i in iterable]
print(my_map(square, ls))
print(my_map(lambda i : i** 3, ls))