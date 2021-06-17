def outer():
    def inner():
        print("Inner function !")
    return inner
val= outer()
val()

def outer2(msg):
    def inner2():
        print(f"Hello {msg} !")
    return inner2
val2= outer2("Harsh")
val2()
