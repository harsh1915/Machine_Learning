def even(num):
    for i in range(2, num+ 1, 2):
        if i%2 == 0:
            yield(i)

number= even(15)
for i in number:
    print(i)

for i in number:
    print(i)

for i in even(15):
    print(i)