ls1= [1, 2, 4, 5, 6, 8, 9]
ls2= [1, 2, 6, 7, 8]

def common_element(ls1, ls2):
    ls3= []
    if len(ls1)>= len(ls2):
        for i in ls1:
            for j in ls2:
                if i == j:
                    ls3.append(j)
    else:
        for i in ls2:
            for j in ls1:
                if i == j:
                    ls3.append(j)

    return ls3
print(common_element(ls1, ls2))

def common_element_2(ls1, ls2):
    ls3= []
    for i in ls1:
        if i in ls2:
            ls3.append(i)
    return ls3

print(common_element_2(ls1, ls2))