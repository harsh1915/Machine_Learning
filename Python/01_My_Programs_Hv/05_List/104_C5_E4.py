ls= list(range(1, 11))

def odd_Even(ls):
    odds= []
    evens= []
    for i in ls:
        if i %2!= 0:
            odds.append(i)
        else:
            evens.append(i)
    ls1= [odds, evens]
    return ls1

print(odd_Even(ls))