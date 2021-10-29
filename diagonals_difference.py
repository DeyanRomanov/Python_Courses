size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

primary_diagonal = 0
secondary_diagonal = 0

for x in range(size):
    primary_diagonal += matrix[x][x]

for x in range(size):
    secondary_diagonal += matrix[x][size - x - 1]

print(abs(primary_diagonal - secondary_diagonal))
