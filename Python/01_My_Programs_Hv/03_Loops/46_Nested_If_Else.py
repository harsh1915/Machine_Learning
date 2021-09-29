win_num= 20
unum= int( input( "Guess a number = "))

if unum == win_num:
    print( "You won !")
else:
    if unum > win_num:
        print( "Too high !")
    else:
        print( "Too low !")