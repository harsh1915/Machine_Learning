ls= list(range(1, 11))

even= []
for i in ls:
    if i%2== 0:
        even.append(i)      

print(ls)
print(f"evens are ={even}")

odd= [i for i in range(1, 11) if i%2 != 0]
print(f"odds are ={odd}")