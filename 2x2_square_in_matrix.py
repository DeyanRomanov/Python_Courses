rows, columns = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(input().split())

square = 0
for r in range(rows-1):
    for c in range(columns-1):
        symbol = matrix[r][c]
        if symbol == matrix[r][c+1] and symbol == matrix[r+1][c] and symbol == matrix[r+1][c+1]:
            square += 1

print(square)
