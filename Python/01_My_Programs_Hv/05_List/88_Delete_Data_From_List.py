words= ["word_1", 'word_2', "word_3", "word_4", "word_6", "word_5", "word_6", 'word_7', "word_8"]
words.pop()         #delete last element of list --> words.pop()  
print(words)

words.pop(1)
print(words)

del words[1]        #delete operator --> del words[1]    
print(words) 

words.remove("word_6")      #remove any element from any position --> words.remove("word_6")
print(words)                   #removes first mached elements