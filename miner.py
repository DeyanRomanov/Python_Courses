def is_inside(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board):
        return True
    return False


size = int(input())

matrix = []

commands = input().split()

start_position = ''
end_of_the_road = []
coals = []
is_over = False

for rows in range(size):
    col = input().split()
    matrix.append(col)
    if 's' in col or 'c' in col or 'e' in col:
        for x in range(len(col)):
            if col[x] == 's':
                start_position = [rows, x]
            elif col[x] == 'e':
                end_of_the_road.append([rows, x])
            elif col[x] == 'c':
                coals.append([rows, x])

player_start_row = start_position[0]
player_start_col = start_position[1]
for command in commands:
    if command == 'right':
        if is_inside(matrix, player_start_row, player_start_col + 1):
            player_start_col += 1
            if matrix[player_start_row][player_start_col] == 'c':
                coals.remove([player_start_row, player_start_col])
                if len(coals) == 0:
                    break
            elif matrix[player_start_row][player_start_col] == 'e':
                is_over = True
                break
            matrix[player_start_row][player_start_col] = '*'
            matrix[player_start_row][player_start_col] = 's'
        else:
            continue
    elif command == 'left':
        if is_inside(matrix, player_start_row, player_start_col - 1):
            player_start_col -= 1
            if matrix[player_start_row][player_start_col] == 'c':
                coals.remove([player_start_row, player_start_col])
                if len(coals) == 0:
                    break
            elif matrix[player_start_row][player_start_col] == 'e':
                is_over = True
                break
            matrix[player_start_row][player_start_col] = '*'
            matrix[player_start_row][player_start_col] = 's'
        else:
            continue
    elif command == 'up':
        if is_inside(matrix, player_start_row - 1, player_start_col):
            player_start_row -= 1
            if matrix[player_start_row][player_start_col] == 'c':
                coals.remove([player_start_row, player_start_col])
                if len(coals) == 0:
                    break
            elif matrix[player_start_row][player_start_col] == 'e':
                is_over = True
                break
            matrix[player_start_row][player_start_col] = '*'
            matrix[player_start_row][player_start_col] = 's'
        else:
            continue
    elif command == 'down':
        if is_inside(matrix, player_start_row + 1, player_start_col):
            player_start_row += 1
            if matrix[player_start_row][player_start_col] == 'c':
                coals.remove([player_start_row, player_start_col])
                if len(coals) == 0:
                    break
            elif matrix[player_start_row][player_start_col] == 'e':
                is_over = True
                break
            matrix[player_start_row][player_start_col] = '*'
            matrix[player_start_row][player_start_col] = 's'
        else:
            continue

if is_over:
    print(f'Game over! {player_start_row, player_start_col}')

else:
    if len(coals) == 0:
        print(f'You collected all coal! {player_start_row, player_start_col}')
    else:
        print(f'{len(coals)} pieces of coal left. {player_start_row, player_start_col}')
