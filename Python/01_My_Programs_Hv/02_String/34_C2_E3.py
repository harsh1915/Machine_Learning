name, char= input( "Enter ypur name and char you have to count by comma separated =").split(",")
print( f"Lenth of your name = { len( name)}")
print( f"Lenth of your name = { len( name.strip())}")

print( f"count of your char = { name.count( char)} ")       #case sesitive
print( f"count of your char = { name.strip().lower().count( char.strip().lower())}")       #case insesitive
