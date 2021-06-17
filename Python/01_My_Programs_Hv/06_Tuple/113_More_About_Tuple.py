mixed= (1, 2, 3, 4.0)

for i in mixed:         #looping in tuple
    print(i)

num= (1,)               #Tuple with one element
print(type(num))

num2= 1, 2, 3           #Tuple without parenthisis
print(type(num2))

num3= (100, 110, 120)
number1, number2, number3=(num3)            #tuple unpacking
print(number1)

num4= (200, 210, [220, 230, 240])           #list inside tuple
print(num4)

num4[2].pop()
print(num4)

num4[2].append(250)
print(num4)

print(min(mixed))
print(max(mixed))
print(sum(mixed))