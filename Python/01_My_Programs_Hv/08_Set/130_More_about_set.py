s= {1, 2, 3, "H", "a", "r"}

for i in s:
    print(i)

s1= {1, 2, 3, 4}
s2= {3, 4, 5, 6}

union_set= s1 | s2          # | --> pipe --> union
print(union_set)

intersection_set= s1 & s2       # & --> AND --> intersection
print(intersection_set)