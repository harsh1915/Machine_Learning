def func():
    x= 7            #Local variable
    return x
x= 5                #global variable
print(func())
print(x)

def func_2():
    global x        #global keyword
    x= 9 
    return x
print(x)
print(func_2())
print(x)