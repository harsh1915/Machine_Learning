num1= int(input("Enter number 1 = "))
num2= int(input("Enter number 2 = "))
print(f"Maximum from {num1} and {num2} = {num1 if num1> num2 else num2}")
print(f"Using Max() function Maximum from {num1} and {num2} = {max(num1, num2)}")