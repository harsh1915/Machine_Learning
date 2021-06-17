def squqre(num):
    return num** 2

ls= [1, 2, 3, 4, 5]         #--> iterable
ls2= map(lambda i: squqre(i), ls)           #--> iterator
ls3= list(ls2)
print(ls3)