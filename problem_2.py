def is_inside(matrix, r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False


def make_matrix_find_king(sizes):
    matrix = []
    start_position = ''
    for r in range(sizes):
        matrix.append(input().split())
        for c in range(sizes):
            if matrix[r][c] == 'K':
                start_position = (r, c)
    return matrix, start_position


size = 8
board, king = make_matrix_find_king(size)
queens = []
row_king, col_king = king
while True:
    search_row, search_col = row_king, col_king
    while is_inside(board, row_king, col_king):
        if board[row_king][col_king] == 'Q':
            queens.append([row_king, col_king])
            break
        col_king += 1
    row_king, col_king = search_row, search_col
    while is_inside(board, row_king, col_king):
        if board[row_king][col_king] == 'Q':
            queens.append([row_king, col_king])
            break
        col_king -= 1
    row_king, col_king = search_row, search_col
    while is_inside(board, row_king, col_king):
        if board[row_king][col_king] == 'Q':
            queens.append([row_king, col_king])
            break
        row_king += 1
    row_king, col_king = search_row, search_col
    while is_inside(board, row_king, col_king):
        if board[row_king][col_king] == 'Q':
            queens.append([row_king, col_king])
            break
        row_king -= 1
    row_king, col_king = search_row, search_col
    while is_inside(board, row_king, col_king):
        if board[row_king][col_king] == 'Q':
            queens.append([row_king, col_king])
            break
        row_king -= 1
        col_king += 1
    row_king, col_king = search_row, search_col
    while is_inside(board, row_king, col_king):
        if board[row_king][col_king] == 'Q':
            queens.append([row_king, col_king])
            break
        row_king += 1
        col_king -= 1
    row_king, col_king = search_row, search_col
    while is_inside(board, row_king, col_king):
        if board[row_king][col_king] == 'Q':
            queens.append([row_king, col_king])
            break
        row_king -= 1
        col_king -= 1
    row_king, col_king = search_row, search_col
    while is_inside(board, row_king, col_king):
        if board[row_king][col_king] == 'Q':
            queens.append([row_king, col_king])
            break
        row_king += 1
        col_king += 1
    break

if queens:
    for queen in queens:
        print(queen)
else:
    print('The king is safe!')
