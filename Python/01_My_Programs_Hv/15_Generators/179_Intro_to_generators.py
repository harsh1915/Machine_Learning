# generators are intrator
ls= list(range(1, 11))          # iterable
square_ls= list(map(lambda i : i** 2, ls))          # map returns iterators
print(ls)
print(square_ls)