# filter(function or None, iterable) --> filter object

# Return an iterator yielding those items of iterable 
# for which function(item) is true. 
# If function is None, return the items that are true.
def is_odd(num):
    return num%2 != 0

numbers= list(range(1, 11))
print(filter(is_odd, numbers))          # returns filter object  position

odds= list(filter(is_odd, numbers))     # use of function
print(odds)

odds_2= list(filter(lambda i: i%2 !=0, numbers))        # use of lambda expretion
print(odds_2)

for i in odds_2:
    print(i)