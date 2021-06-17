name= ["Harsh", "Karan", "Krunal", "Rohan", "Bhargav"]
def reverse_name(name):
    return [i[::-1] for i in name]
print(f"name = {name}")
print(f"reverse of your name = {reverse_name(name)}")

def reverse_name2(name):
    ls= []
    for i in name:
        ls.append(i[::-1])
    return ls
print(reverse_name2(name))