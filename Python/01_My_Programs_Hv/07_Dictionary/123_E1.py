num= int(input("Enter any number = "))

def cube_Finder(num):
    dis= {}
    for i in range(1, num+ 1):
        dis[i]= i**3
    return dis

print(cube_Finder(num))
