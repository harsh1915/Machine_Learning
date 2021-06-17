fruits= ["Grapes", "Apple"]
fruits.insert(1, "Mango")           #insert data at any position --> fruits.insert(1, "Mango")
print(fruits)

fruits2= ["Banan", "Orange"]
fruits3= fruits+ fruits2                    #list concatenate
print(fruits3)
print(fruits2)

fruits.extend(fruits2)              #add items from other list -->fruits.extend(fruits2) 
fruits.append(fruits2)              #add as a list --> fruits.append(fruits2)
print(fruits)
print(fruits2)