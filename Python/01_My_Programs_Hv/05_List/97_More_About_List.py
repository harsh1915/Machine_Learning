numbers= list(range(1, 11))         #Create list using range function --> list(range(1, 11)) 
print(numbers)

print(numbers.pop())                #returns poped value --> numbers.pop()
print(numbers)

print(numbers.index(2))             #Return index of value --> numbers.index(2)

numbers2= [1, 2, 3, 4, 5, 1]
print(numbers2.index(1))
print(numbers2.index(1, 1))

def nagative_list(list):
    nagative_l= []
    for i in list:
        nagative_l.append(-i)
    return nagative_l

print(nagative_list(numbers))