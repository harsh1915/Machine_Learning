# we can use enumerate function with for loop to track position of our item in iterable

names= ["Harsh", "Krunal", "Karan"]         # without enumerate function
pos= 0
for i in names:
    print(f"{pos} --> {i}")
    pos+= 1

for pos, i in enumerate(names):         # with enumearte function
    print(f"{pos} --> with enumerate --> {i}")

def finds(ls, s):          
    pos= 0
    for i in ls:            # without enumerate function
        if i== s:
            return pos
        pos+= 1
    return -1

print(finds(names, "Krunal"))

def finds_2(ls, s):
    for pos, i in enumerate(ls):            # with enumearte function
        if i== s:
            return pos
    return -1
print(finds_2(names, "Karan"))