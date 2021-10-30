import sys

rows, columns = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

a = 0
max_sum_square = -sys.maxsize
max_sum_square_coords = ''
for row in range(rows - 2):
    for col in range(columns - 2):
        a = matrix[row][col] + \
            matrix[row][col + 1] + \
            matrix[row][col + 2] + \
            matrix[row + 1][col] + \
            matrix[row + 1][col + 1] + \
            matrix[row + 1][col + 2] + \
            matrix[row + 2][col] + \
            matrix[row + 2][col + 1] + \
            matrix[row + 2][col + 2]
        if a > max_sum_square:
            max_sum_square = a
            max_sum_square_coords = (row, col)

print(f'Sum = {max_sum_square}')
r, c = max_sum_square_coords
for rows in range(3):
    print(matrix[r + rows][c], matrix[r + rows][c + 1], matrix[r + rows][c + 2])
