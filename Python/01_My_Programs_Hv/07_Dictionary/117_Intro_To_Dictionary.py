# unordered collection of data in key : value pair
user= {"name": "Harsh", "age": 22}
print(user)
print(type(user))

user1= dict(name= "Parth", age= 17)         #Creat dictionary with dict keyword
print(user1)
print(type(user1))

print(user["name"])         #acces data from Dictionary
print(user["age"])

user_info= dict(            #Clean syntex
    name= "harsh",
    age= 22,
    number= 8511281915,
    fav_movies= ["movie_1", "movie_2"],         #List inside Dictionary
    fav_songs= ["song_1", "song_2"]
)

print(user_info)
print(type(user_info))

print(user_info["fav_movies"])

user_info2= dict(           #dictionary inside dictionary
    u1= dict(
        name= "Parth",
        age= 17
    ),
    u2= dict(
        name= "harsh",
        age= 22,
    )
)

print(user_info2)
print(user_info2["u1"])

user_info3= dict()
print(user_info3)

user_info3["name"]= "harsh"         #Add data in dictionary
user_info3["age"]= 22
print(user_info3)