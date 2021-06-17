def greatest(num1 ,num2):
    if num1> num2:
        return f"{ num1} is greter than { num2} "
    elif num1== num2:
        return f"{ num1} is equal to { num2} "
    return f"{ num2} is greter than { num1} "

num1= int( input("Enter first number = "))
num2= int( input("Enter second number = "))
print( greatest(num1, num2))