def is_inside(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board):
        return True
    return False


size = int(input())

matrix = []
bunny_position_row = ''
bunny_position_col = ''

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'B':
            bunny_position_row, bunny_position_col = row, col

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}
counter = 0
max_eggs = 0
best_side = ''
best_path = []
for direction, step in directions.items():
    eggs_in_row = 0
    current_path = []
    current_step_row, current_step_col = bunny_position_row, bunny_position_col
    while True:
        current_step_row, current_step_col = step(current_step_row, current_step_col)
        if not is_inside(matrix, current_step_row, current_step_col):
            break
        if matrix[current_step_row][current_step_col] == 'X':
            break
        eggs_in_row += int(matrix[current_step_row][current_step_col])
        current_path.append([current_step_row, current_step_col])
        if eggs_in_row >= max_eggs:
            max_eggs = eggs_in_row
            best_side = direction
            best_path = current_path


print(best_side)
for way in best_path:
    print(way)
print(max_eggs)
