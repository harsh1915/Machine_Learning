user= dict(
    name= "harsh",
    age= 22,
    fav_movie= ["movie1", "movie2"],
    fav_song= ["song1", "song2"]
)
print(user)

poped_item= user.pop("fav_song")            #pop mathod to delete items --> user.pop("fav_song")
print(f"poped item is {poped_item}")
print(type(poped_item))         #pop mathod returns --> only value

print(user)

poped_item_2= user.popitem()            # rendomly deletes any elements --> user.popitem()
print(poped_item_2)             #popitem mathod returns --> tuple as popitem with key :value
print(type(poped_item_2))

print(user)