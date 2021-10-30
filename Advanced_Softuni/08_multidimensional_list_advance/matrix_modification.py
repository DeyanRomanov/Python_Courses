def is_valid(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board):
        return True
    return False


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

commands = input()

while not commands == 'END':
    commands = commands.split()
    if commands[0] == 'Add':
        row, col, value = [int(x) for x in commands[1:]]
        if not is_valid(matrix, row, col):
            print("Invalid coordinates")
        else:
            matrix[row][col] += value
    elif commands[0] == 'Subtract':
        row, col, value = [int(x) for x in commands[1:]]
        if not is_valid(matrix, row, col):
            print("Invalid coordinates")
        else:
            matrix[row][col] -= value
    commands = input()

for row in matrix:
    print(" ".join(str(x) for x in row))
