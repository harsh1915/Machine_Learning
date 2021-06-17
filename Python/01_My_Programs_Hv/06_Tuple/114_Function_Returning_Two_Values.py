def func(int1, int2):
    add= int1+ int2
    multiply=int1* int2
    return add,multiply         #Function Returns Tuple

print(func(2, 3))

add, multiply= func(3, 4)
print(add)
print(multiply)