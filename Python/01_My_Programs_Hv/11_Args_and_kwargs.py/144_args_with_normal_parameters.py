def multiply_nums(num, *args):          # num is a normal paarameter
    print(num)
    print(args)
    multiply= 1
    for i in args:
        multiply*= i
    return multiply

print(multiply_nums(2, 3, 4))