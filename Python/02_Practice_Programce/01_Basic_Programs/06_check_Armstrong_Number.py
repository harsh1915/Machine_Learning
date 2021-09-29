"""
Armstrong number
1*1*1 + 5*5*5 + 3*3*3 = 153
1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634
"""
num1= input("Enter Any number = ")
total= 0
for i in num1:
    temp= 1
    for j in range(len(num1)):
        temp*=int(i)
    total+=temp
print(f"{int(num1)} is an Armstrong" if total== int(num1) else f"{int(num1)} is not a Armstrong")