num= int(input("Enter any number = "))
a= 0
b= 1
c= 0
ls= []
for i in range(num+1):
    a= b
    b= c
    c= a+ b
    ls.append(c)
print(ls)
for i in range(1, num+1):
    if i in ls:
        print(f"{i} is fibonacci number !")
    else:
        print(f"{i} is not fibonacci number !")