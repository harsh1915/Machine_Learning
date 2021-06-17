ls= list(range(1, 11))

def square_list(ls):
    square_ls= []
    for i in ls:
        square_ls.append(i**2)
    return square_ls

print(square_list(ls))