def is_inside(matrix_board, r, c):
    if 0 <= r < len(matrix_board) and 0 <= c < len(matrix_board):
        return True
    return False


def matrix(size):
    matrix_board = []
    position = ''
    for r in range(size):
        matrix_board.append(list(input()))
        for c in range(size):
            if matrix_board[r][c] == 'P':
                position = (r, c)
    return matrix_board, position


initial_string = input()
size_of_matrix = int(input())
board, player_position = matrix(size_of_matrix)
number_of_commands = int(input())

movement_dict = {'up': lambda x, y: (x - 1, y),
                 'down': lambda x, y: (x + 1, y),
                 'left': lambda x, y: (x, y - 1),
                 'right': lambda x, y: (x, y + 1)
                 }
for _ in range(number_of_commands):
    row, col = player_position
    command = input()
    next_row, next_col = movement_dict[command](row, col)
    if is_inside(board, next_row, next_col):
        if not board[next_row][next_col] == '-':
            initial_string += board[next_row][next_col]
            board[row][col] = '-'
            board[next_row][next_col] = "P"
        else:
            board[row][col] = '-'
            board[next_row][next_col] = "P"
        player_position = (next_row, next_col)
    else:
        initial_string = initial_string[:len(initial_string) - 1]

print(initial_string)
[print(''.join(line)) for line in board]
