def song():
    print("Happy Birthday Song !")
song()

def last_char( name):
    return name[-1]
name= input("Enter your name = ")
print( f"Last charecter of your name is { last_char( name)}")

def even_or_odd( num):
    if num% 2== 1:
        return "Odd !"
    return "Even !"
num= int( input("Enter any number = "))
print( f"Your number is { even_or_odd( num)}")

def is_even( num):
    return num% 2== 0
num= int( input("Enter any number = "))
print( f"Your number is Even { is_even( num)}")