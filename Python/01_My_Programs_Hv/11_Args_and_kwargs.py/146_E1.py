from typing import NoReturn


def power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "Hey, You didn't pass any args !"
nums= list(range(1, 11))
print(power(3))
print(power(3,*nums))