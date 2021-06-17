name= input( "Enter your name = ")

for i in range(len(name)):      #In All Language
    print(name[i])
    
for i in name:      #In Python
    print(i)

num= input( "Enter a number = ")
total= 0
for i in num:
    total+= int(i)

print( total)