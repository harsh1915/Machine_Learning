num= int(input("Enter any number = "))
a= 0
b= 1
c= 0
ls= []
for i in range(num+1):
    ls.append(c)
    a= b
    b= c
    c= a+ b
print(ls)
print(f"{ls[num]} is at {num} position !")