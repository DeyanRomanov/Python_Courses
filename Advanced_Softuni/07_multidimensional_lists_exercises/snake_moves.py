rows, columns = [int(x) for x in input().split()]
snake = list(input())

matrix = []
index = 0
for r in range(rows):
    matrix.append([None] * columns)
    for col in range(columns):
        if r % 2 == 0:
            matrix[r][col] = snake[index]
        else:
            matrix[r][columns - 1 - col] = snake[index]
        index = (index + 1) % len(snake)

for row in matrix:
    print(''.join(row))
