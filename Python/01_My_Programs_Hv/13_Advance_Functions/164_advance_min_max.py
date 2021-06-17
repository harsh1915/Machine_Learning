names= ["Harsh", "Hasmukh", "Himanshu"]
print(len(max(*names)))
print(min(len(i) for i in names))

def func(item):
    return len(item)

print(min(names, key= func))
print(max(names, key= lambda a: len(a)))

students= [
    {"name": "harsh","score": 50, "age": 22},
    {"name": "Hasmukh", "score": 70, "age": 23},
    {"name": "Himanshu", "score": 60, "age": 24}
]

students2={
    "harsh" : {"score": 50, "age": 22},
    "Hasmukh" : {"score": 70, "age": 23},
    "Himanshu" : {"score": 60, "age": 24}
}

print(max(students,key= lambda item: item.get("score"))["name"])
print(max(students2,key= lambda item: students2[item]["age"]))