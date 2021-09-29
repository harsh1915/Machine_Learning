# orderd collection of items

numbers= [1, 2, 3, 4]           #Square Brakets []
print(numbers)

words= ["word_1", 'word_2', "word_3"]
print(words)
print(words[:2])                #words[:2] slicing

mixed= [words, numbers, 2.3, None, True]
print(mixed)
print(mixed[2])         #acces any element with Squere brackets []

mixed[1]= "number"      #change value of list elements -->mixed[1]= "number"
print(mixed)

mixed[1:]= "HarsH"
print(mixed)