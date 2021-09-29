start= int(input("Enter start point = "))
stop= int(input("Enter stop point = "))
for i in range(start, stop+1):
    count= 0
    for j in range(1, i+1):
        if i%j== 0:
            count+=1
    if count== 2:
        print(i,end=(", "))