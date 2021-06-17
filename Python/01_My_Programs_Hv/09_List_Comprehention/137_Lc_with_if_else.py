ls= list(range(1, 11))
ls2=[]
for i in ls:
    if i%2 != 0:
        ls2.append(-i)
    else:
        ls2.append(i** 2)
print(ls)
print(ls2)

ls3= [-i if i%2 != 0 else i**2 for i in ls]
print(ls)
print(ls3)