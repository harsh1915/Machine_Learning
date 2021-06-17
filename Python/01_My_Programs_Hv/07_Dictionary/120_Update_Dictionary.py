user= dict(
    name= "harsh",
    age= 22
)
print(user)

more= dict(
    name= "Harsh Darji",
    fav_movie= ["movie1", "movie2"],
    fav_song= ["song1", "song2"]
)

user.update(more)           #update mathod-->user.update(more)
print(user)