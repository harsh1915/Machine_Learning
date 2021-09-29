num= int(input("Enter any number = "))
ls= [i** 2 for i in range(1,num+1)]
print(ls)
total= 0
for i in ls:
    total+= i
    print(total, end=", ")
print(f"Sum of squares of {num} = {total}")