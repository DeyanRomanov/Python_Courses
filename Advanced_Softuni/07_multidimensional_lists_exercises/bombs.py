def is_inside(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board):
        return True
    return False


def explosion(board, r, c, blow):
    board[r][c] = 0
    if is_inside(board, r, c + 1) and board[r][c + 1] > 0:
        board[r][c + 1] -= blow
    if is_inside(board, r, c - 1) and board[r][c - 1] > 0:
        board[r][c - 1] -= blow
    if is_inside(board, r + 1, c) and board[r + 1][c] > 0:
        board[r + 1][c] -= blow
    if is_inside(board, r - 1, c) and board[r - 1][c] > 0:
        board[r - 1][c] -= blow
    if is_inside(board, r + 1, c + 1) and board[r + 1][c + 1] > 0:
        board[r + 1][c + 1] -= blow
    if is_inside(board, r + 1, c - 1) and board[r + 1][c - 1] > 0:
        board[r + 1][c - 1] -= blow
    if is_inside(board, r - 1, c - 1) and board[r - 1][c - 1] > 0:
        board[r - 1][c - 1] -= blow
    if is_inside(board, r - 1, c + 1) and board[r - 1][c + 1] > 0:
        board[r - 1][c + 1] -= blow
    return board


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

bombs_coordinates = [x.split(',') for x in input().split()]
for bomb in bombs_coordinates:
    row, col = int(bomb[0]), int(bomb[1])
    if not matrix[row][col] <= 0:
        tnt = matrix[row][col]
        matrix = explosion(matrix, row, col, tnt)

alive = []
for row in matrix:
    alive.extend([x for x in row if x > 0])

print(f"Alive cells: {len(alive)}")
print(f"Sum: {sum(alive)}")

for row in matrix:
    print(' '.join([str(x) for x in row]))
