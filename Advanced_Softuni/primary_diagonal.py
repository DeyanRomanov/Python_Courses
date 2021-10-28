rows = int(input())
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

counter = -1
diagonal_sum = 0
for i in range(rows):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)
