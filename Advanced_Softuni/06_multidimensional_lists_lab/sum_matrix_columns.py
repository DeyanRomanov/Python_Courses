row, columns = [int(x) for x in input().split(', ')]

matrix = []
r = []

for _ in range(row):
    matrix.append([int(x) for x in input().split(' ')])

for y in range(0, columns):
    col_sum = 0
    for x in range(0, row):
        col_sum += matrix[x][y]
    print(col_sum)
