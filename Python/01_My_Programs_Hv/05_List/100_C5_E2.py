ls= list(range(1, 11))

def reverse_list(ls):
    ls1= []
    for i in range(len(ls)):
        ls1.append(ls.pop())
    return ls1

def reverse_ls_slicing(ls):
    return ls[::-1]


print(reverse_list(ls))

ls1= list(range(1, 11))
print(reverse_ls_slicing(ls1))
print(ls1[::-1])