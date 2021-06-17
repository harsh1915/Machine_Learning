name= input( "Enter your name = ")
i= 0
temp= ""
while i< len( name):
    if name[i] not in temp:
        print( f"{ name[i]} : { name.count( name[ i])}")
    temp+= name[i]
    i+=1
    