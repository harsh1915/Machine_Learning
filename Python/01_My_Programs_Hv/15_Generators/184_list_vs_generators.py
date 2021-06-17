import time

t1= time.time()
ls= [i** 2 for i in range(1, 10000)]
print(f"Time to create list = {time.time()- t1}")

t1= time.time()
gen= (i** 2 for i in range(1, 10000000000000))
print(f"Time to create generator = {time.time()- t1}")