fruits= ["banana", "mango", "apple", "grapes"]
fruits.sort()           # List
print(fruits)

fruits2= ("banana", "mango", "apple", "grapes")
print(sorted(fruits2))          # Tuple

fruits3= {"banana", "mango", "apple", "grapes"}
print(sorted(fruits3))

students= [
    {"name": "harsh", "score": 50},
    {"name": "Hasmukh", "score": 70},
    {"name": "Himanshu", "score": 60}
]

print(sorted(students, key= lambda d: d["score"]))
print(sorted(students, key= lambda d: d["score"], reverse= True))