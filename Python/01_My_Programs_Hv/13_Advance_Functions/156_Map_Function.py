ls= list(range(1, 11))

def square(num):
    return num** 2

print([square(i) for i in ls])          # list comprehention

print(map(square, ls))
print(list(map(square, ls)))            # Map function

print(list(map(lambda i : square(i), ls)))          # Map And Lambda expretion

names= ["Harsh", "Krunal", "Karan"]
print(list(map(len, names)))

ls1= list(map(len, names))
for i in ls1:               # For loop in Map function
    print(i)
