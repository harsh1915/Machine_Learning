def nums(n):
    for i in range(1, n+ 1):
        yield(i)           # yield creates generator

number= nums(5)
for i in number:
    print(i)

# memory --> list --> [1, 2, 3, 4, 5]
# memory --> gen  --> (1)       one by one generating