import math
while True:
    num1= int(input("Enter Any number = "))
    fact= 1
    if num1> 0:
        for i in range(1, num1+ 1):
            fact= fact* i
        print(f"Factorial of {num1} = {fact}")
        break
    print("Invalid input !\nTry Again")

# using math.factoril() function
# num1= int(input("Enter Any number = "))
# print(f"Factorial of {num1} = {math.factorial(num1)}")