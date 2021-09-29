age= int( input( "Enter your age = "))

if age>0 and age<=3:
    print( "Tcket price is : free")
elif age>=4 and age<=10:
    print( "Tcket price is : 150")
elif age>=11 and age<=60:
    print( "Tcket price is : 250")
elif age>60:
    print( "Tcket price is : 200")
else:
    print( "You can't Watch !")