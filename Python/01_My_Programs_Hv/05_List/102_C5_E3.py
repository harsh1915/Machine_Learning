ls= ["abc", "def", "ghi"]
print(ls[0][::-1])

def list_reverse(ls):
    ls1= []
    for i in ls:
        ls1.append(i[::-1])
    return ls1

print(list_reverse(ls))