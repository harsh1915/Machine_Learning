# Lambda Expression --> anonymous function

def add1(num1, num2):
    return num1+ num2
print(add1(2, 3))

add2= lambda num1, num2 : num1+ num2
print(add2(2, 3))

multiply= lambda num1, num2 : num1* num2
print(multiply(2, 3))

print(add1)
print(add2)
print(multiply)