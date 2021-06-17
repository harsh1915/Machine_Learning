num= input( "Enter any number that contain more than one digit = ")
i= 0
total= 0
print( f"Len of your number is = { len( num)}")
while i<len(num):
    total+= int( num[ i])
    i+= 1
print( f"Total = { total}")
