def is_inside(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board):
        return True
    return False


def make_matrix(sizes):
    matrix = []
    for r in range(sizes):
        line = []
        for c in range(sizes):
            line.append(0)
        matrix.append(line)
    return matrix


size = int(input())
mine_field = make_matrix(size)
number_of_mines = int(input())
mine_coordinates = []

mines_dict = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'right': lambda x, y: (x, y + 1),
    'left': lambda x, y: (x, y - 1),
    'left_up': lambda x, y: (x - 1, y - 1),
    'right_up': lambda x, y: (x - 1, y + 1),
    'right_down': lambda x, y: (x + 1, y + 1),
    'left_down': lambda x, y: (x + 1, y - 1),
}

for _ in range(number_of_mines):
    row, col = [int(x) for x in input()[1:-1].split(', ')]
    mine_field[row][col] = '*'
    mine_coordinates.append((row, col))

for coordinates in mine_coordinates:
    row, col = coordinates
    for command in mines_dict:
        rows, cols = mines_dict[command](row, col)
        if is_inside(mine_field, rows, cols) and not mine_field[rows][cols] == '*':
            mine_field[rows][cols] += 1

for line in mine_field:
    print(' '.join(str(x) for x in line))
