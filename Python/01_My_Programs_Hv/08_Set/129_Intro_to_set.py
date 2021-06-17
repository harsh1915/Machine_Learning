#set is a unordered collection of unique items
#You can't store list and dictionary in Set

s= {1, 2, 3, 4, 2, 3}
print(s)

ls= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 6, 8]
print(ls)
print(set(ls))           # List to Set

s.add(6)            # s.add(4) 
print(s)

s.remove(6)         # s.remove(6)   
print(s)

s.discard(6)        # If 6 is not exist in set than removes nothing --> s.discard(6)
print(s)

s1= s.copy()        # Return a shallow copy of a set --> s.copy()
print(s)

s.clear()           # Remove all elements from this set --> s.clear()
print(s)