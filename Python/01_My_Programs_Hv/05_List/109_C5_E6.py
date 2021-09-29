ls= [1, 2, [1, 2, 3], 3, 4, [4, 5, 6]]

def check_how_many_list(ls):
    ls_count= 0
    for i in ls:
        if type(i) == list:
            ls_count+= 1
    return ls_count

print(check_how_many_list(ls))