name= input("Enter your name = ")

def c_counter(name):
    c_count= ""
    dis= {}
    for i in range(len(name)):
        if name[i] not in c_count:
            dis[name[i]]= name.count(name[i])
    c_count+= name[i]
    return dis

print(c_counter(name))

def c_counter_2(name):
    dis= {}
    for i in name:
        dis[i]= name.count(i)
    return dis

print(c_counter_2(name))