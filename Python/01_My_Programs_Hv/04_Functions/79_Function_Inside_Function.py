def greatest(num1, num2):
    if num1> num2:
        return num1
    return num2

def new_greatest(num1, num2, num3):
    return greatest(greatest( num1, num2), num3)

u_num1= int( input("Enter number 1 = "))
u_num2= int( input("Enter number 2 = "))
u_num3= int( input("Enter number 3 = "))

print(new_greatest(u_num1, u_num2, u_num3))