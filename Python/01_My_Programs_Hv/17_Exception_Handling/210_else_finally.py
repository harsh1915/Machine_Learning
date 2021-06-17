while True:
    try:
        num1= int(input("Enter any number = "))
    except ValueError:
        print("Please Enter integer !")
    except:
        print("Unexpected error !")
    else:
        print(f"You entered = {num1}")
        break
    finally:
        print("Finally block is here 😎")