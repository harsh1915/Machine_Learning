ls1= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def average_finder(*args):
    ls=[]
    for pair in zip(*args):
        ls.append(sum(pair)/len(pair))
    return(ls)

print(average_finder(*ls1))
ls2= lambda *ls : [sum(pair)/len(pair) for pair in zip(*ls)]
print(ls2(*ls1))