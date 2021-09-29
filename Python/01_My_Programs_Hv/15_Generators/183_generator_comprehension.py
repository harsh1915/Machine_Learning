ls= [i** 2 for i in range(1, 11)]           # --> list
print(ls)

gen= (i** 2 for i in range(1, 11))          # --> generator
print(gen)

for i in gen:
    print(i)