num= int(input("Enter any number = "))

d1={i:i** 2 for i in range(1, num+1)}
for i,j in d1.items():
    print(f"square of {i} = {j}")

def cube_Finder(num):
    dis= {}
    for i in range(1, num+ 1):
        dis[i]= i**3
    return dis
print(cube_Finder(num))

name= "harsh"
d2= {i:name.count(i) for i in name if name}
print(d2)