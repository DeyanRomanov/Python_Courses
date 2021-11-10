def is_valid(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board):
        return True
    return False


size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]

command = input()
while not command == 'END':
    command, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)
    if is_valid(matrix, row, col):
        if command == 'Add':
            matrix[row][col] += value
        elif command == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')
    command = input()

[print(' '.join([str(x) for x in line])) for line in matrix]
