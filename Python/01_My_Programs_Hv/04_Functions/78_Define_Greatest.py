def greatest(num1, num2, num3):
    if num1> num2 and num1> num3:
        return f"{ num1} is greter than { num2} and { num3}"
    elif num2> num1 and num2> num3:
        return f"{ num2} is greater to { num1} and { num3}"
    return f"{ num3} is greter than { num1} and { num2}"

num1= int( input("Enter first number = "))
num2= int( input("Enter second number = "))
num3= int( input("Enter third number = "))
print( greatest(num1, num2, num3))