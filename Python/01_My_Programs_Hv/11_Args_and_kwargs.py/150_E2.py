def title_1(ls, **kwargs):
    if kwargs.get("revers"):
        return [i[::-1].title() for i in ls]
    return [i.title() for i in ls]
names= ["harsh", "kuldip", "rohan"]
print(title_1(names))
print(title_1(names, revers= True))