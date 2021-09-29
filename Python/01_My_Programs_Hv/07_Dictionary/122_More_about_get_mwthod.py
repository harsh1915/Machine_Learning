user={
    "name": "harsh",
    "age": 22,
    "age": 23,
    "age": 21
}

print(user)
print(user.get("name"))
print(user.get("names"))            #returns None
print(user.get("names", "not found !"))     #you can retur not found msg in place of None
