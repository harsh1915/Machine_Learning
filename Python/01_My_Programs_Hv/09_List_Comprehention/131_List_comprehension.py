squares= []

for i in range(1, 11):
    squares.append(i** 2)

print(squares)

squares_2= [i** 2 for i in range(1, 11)]            #List comprehension
print(squares_2)

nagatives= [-i for i in range(1, 11)]
print(nagatives)

name= ["Harsh", "Karan", "Krunal", "Rohan", "Bhargav"]
first_char= [i[0] for i in name]
print(name)
print(first_char)