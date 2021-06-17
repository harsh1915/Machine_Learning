def fibonacci( num):
    a= 0
    b= 1
    for i in range(0, num):
        print(a, end=(", "))
        c= a+ b
        a= b
        b= c
num= int( input("How many fibonacci nubers you have to print = "))
print( fibonacci( num))  