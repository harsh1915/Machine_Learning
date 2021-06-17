#Palindrome names --> madam, naman, etc
def is_palindrome( name):
    return name== name[::-1]

name= input("Enter your name = ")
print(is_palindrome( name))