def func(num1, num2):
        try:
            return num1/ num2
        except TypeError as err:
            return err
        except ZeroDivisionError as err:
            return err
        except:
            return "Unexpected Error !"

print(func(4, 2))
print(func("4", 2))
print(func(4, 0))