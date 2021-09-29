def power(p):
    def number(n):
        return n** p
    return number

square= power(2)
print(square(3))

cube= power(3)
print(cube(3))