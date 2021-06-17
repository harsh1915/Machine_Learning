"""
all --> Return True if bool(x) is True for all values x in the iterable.
        If the iterable is empty, return True.

any --> Return True if bool(x) is True for any x in the iterable.
        If the iterable is empty, return False.
"""
odd= list(range(1, 11, 2))
odd2= [1, 2, 3]
print([num%2 != 0 for num in odd])
print(all([num%2 != 0 for num in odd]))
print(any([num%2 != 0 for num in odd2]))