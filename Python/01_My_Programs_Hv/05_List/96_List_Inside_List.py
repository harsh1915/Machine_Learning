matrix= [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(matrix[0])

for i in matrix:
    print(i)

for i in matrix:
    for i in i:
        print(i, end=" ,")

print(matrix[1][1])