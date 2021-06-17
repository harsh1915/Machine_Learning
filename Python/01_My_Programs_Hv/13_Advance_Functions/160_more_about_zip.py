# *operator with zip function()
ls= [(1, 2), (4, 3), (5, 6)]
ls2, ls3= list(zip(*ls))
print(ls2)
print(ls3)
ls4= []

for pair in zip(ls2, ls3):
    ls4.append(max(pair))
print(ls4)