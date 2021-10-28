import sys

row, column = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(row):
    matrix.append([int(x) for x in input().split(', ')])

biggest_sum = -sys.maxsize
best_sum_cords = ''
current_sum = 0
for r in range(0, row - 1):
    for c in range(0, column - 1):
        current_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r+1][c] + matrix[r+1][c+1]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            best_sum_cords = (r, c)

r, c = best_sum_cords
print(matrix[r][c], matrix[r][c+1])
print(matrix[r+1][c], matrix[r+1][c+1])
print(biggest_sum)
