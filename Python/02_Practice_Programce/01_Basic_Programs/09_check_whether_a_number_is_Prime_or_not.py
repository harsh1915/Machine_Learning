num= int(input("Enter any number = "))
count= 0
for i in range(1, num+1):
    if num%i ==0:
        count+= 1
if count== 2:
    print(f"{num} is Prime !")
else:
    print(f"{num} is Not Prime !")