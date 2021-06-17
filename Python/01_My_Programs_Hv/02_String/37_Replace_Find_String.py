name= "Harsh is cricketer and he is very good batsman !"

print( name.replace( " ", "_"))
print( name.replace( "is", "was"))
print( name.replace( "is", "was", 1))

print( f"Position of first->is = {name.find( 'is')}")       #name.find( 'is')
print( f"Position of second->is = {name.find( 'is', 7)}")

is_Positon_1= name.find( " is")
print( f"Position of first->is = {name.find( 'is', is_Positon_1)}")
print( f"Position of second->is = {name.find( 'is', is_Positon_1+ 1)}")
