import random
win_num= random.randint(1, 10)

g_count= 1
num= int( input( "Enter a number 1 to 10 = "))

while True:
    if win_num== num:
        print( f"You won !Your guess count is = {g_count}")
        break
    else:
        if win_num> num:
            print("\nToo Low !")
            num= int( input( "Enter again !"))
            g_count+= 1
        else:
            print( "\nToo high !")
            num= int( input( "Enter again !"))
            g_count+= 1