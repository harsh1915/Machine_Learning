user= dict(
    name= "harsh",
    age= 22,
    fav_movie= ["movie1", "movie2"],
    fav_song= ["song1", "song2"]
)

# Check if key is exist in Dictionary --> keys mathod
if "name" in user.keys():          #in keyword
    print("Present !")

# Check if value is exist in Dictionary --> values mathod
if "harsh" in user.values():        
    print("Present !")

for i in user.values():
    print(i)

user_values= user.values()          #Store values of dictionary --> user.values()
print(user_values)
print(type(user_values))

user_keys= user.keys()          #Store keys of dictionary --> user.keys()
print(user_keys)
print(type(user_keys))

user_items= user.items()            # items mathod returns list with sub tuples
print(user_items)
#out put --> dict_items([('name', 'harsh'), ('age', 22), ('fav_movie', ['movie1', 'movie2']), ('fav_song', ['song1', 'song2'])])
print(type(user_items))

for key, value in user.items():
    print(f"key is {key} and value is {value} !")