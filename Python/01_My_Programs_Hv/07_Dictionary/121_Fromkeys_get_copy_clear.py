dis= dict.fromkeys(["name", "age", "height"], "unkhown")         #pass defualt value --> fromkeys
print(dis)

dis2= dict.fromkeys("abc", "unkhown")
print(dis2)

dis3= dict.fromkeys(range(1 ,11), "unkhown")
print(dis3)

dis4= dict.fromkeys(["name", "age"], ["unkhown", "unkhown"])
print(dis4)

user= dict(
    name= "harsh",
    age= 22,
    fav_movie= ["movie1", "movie2"],
    fav_song= ["song1", "song2"]
)

print(user["name"])
print(user.get("name"))         # better to acces --> user.get("name")

user1= user.copy()              #user.copy()
print(user1)

user1.clear()
print(user1)