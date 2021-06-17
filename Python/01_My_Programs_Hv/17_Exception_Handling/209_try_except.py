while True:
    try:
        age = int(input("Enter your age = "))
        break
    except ValueError:
        print("You entered String instead of number, Try Again")
    except:
        print("Unexpected error !")

print("You can play this game !" if age >= 18 else "You can't play this game !")