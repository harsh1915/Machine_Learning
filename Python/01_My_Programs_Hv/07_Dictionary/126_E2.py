dis={}

dis["name"]= input("Enter your name = ")
dis["age"]= int(input("Enter your age = "))
dis["fav songs"]= input("Enter your fav songs = ").split(",")
dis["fav movies"]= input("Enter your fav movies = ").split(",")

for key,value in dis.items():
    print(f"{key} : {value}")