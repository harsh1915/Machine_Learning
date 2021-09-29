ls= ["Rohan", "Bhargav", 1, 2, 3, 3.0, 4.1, True, False]

def num_finder(ls):
    return [str(i) for i in ls if type(i)== int or type(i)== float]

print(num_finder(ls))