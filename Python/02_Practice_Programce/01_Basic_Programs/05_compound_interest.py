p= float(input("Enter principle amount = "))
r= float(input("Enter rate of interest = "))
t= float(input("Enter time period = "))
print(F"Simple interest is = {(p* r* t)/ 100}")
amount= p* ((1+(r/100))** t)
ci= amount- p
print(ci)