# A zip object yielding tuples until an input is exhausted.
id= ["user1", "user2", "user3"]
name= ["Harsh", "Rohan", "Bhargav"]
number= [110, 111, 112]
print(zip(id, name))
print(list(zip(id, name)))
print(dict(zip(id, name)))
print(list(zip(id, name, number)))