def is_inside(board, ri, ci):
    if 0 <= ri < len(board) and 0 <= ci < len(board[0]):
        return True
    return False


def spreads(board, ro, co, bunnie):
    if is_inside(board, ro, co + 1):
        bunnie.append([ro, co + 1])
    if is_inside(board, ro, co - 1):
        bunnie.append([ro, co - 1])
    if is_inside(board, ro + 1, co):
        bunnie.append([ro + 1, co])
    if is_inside(board, ro - 1, co):
        bunnie.append([ro - 1, co])
    return bunnie


rows, columns = [int(x) for x in input().split()]

is_win = None
matrix = []
player_position = []
bunnies_positions = []
new_bunnies = []
for row in range(rows):
    column = list(input())
    for col in range(columns):
        if column[col] == 'P':
            player_position = [row, col]
        elif column[col] == 'B':
            bunnies_positions.append([row, col])
    matrix.append(column)

commands = input()
commands_dictionary = {
    'R': lambda r, c: (r, c + 1),
    'L': lambda r, c: (r, c - 1),
    'U': lambda r, c: (r - 1, c),
    'D': lambda r, c: (r + 1, c)
}

player_position_row = ''
player_position_col = ''

for command in commands:
    for side, position in commands_dictionary.items():
        if side == command:

            player_position_row, player_position_col = position(player_position[0], player_position[1])
            if not is_inside(matrix, player_position_row, player_position_col):
                matrix[player_position[0]][player_position[1]] = '.'
                is_win = True
            elif matrix[player_position_row][player_position_col] == 'B':
                is_win = False
            else:
                matrix[player_position[0]][player_position[1]] = '.'
                matrix[player_position_row][player_position_col] = 'P'
                player_position = [player_position_row, player_position_col]

            for index in range(len(bunnies_positions)):
                row, col = bunnies_positions[index]
                new_bunnies = spreads(matrix, row, col, bunnies_positions)
            bunnies_positions.extend(new_bunnies)
            for bunnies in bunnies_positions:
                re, ce = bunnies
                if matrix[re][ce] == 'P':
                    is_win = False
                matrix[re][ce] = 'B'

    if is_win is not None:
        break

for row in matrix:
    print(''.join(row))
if is_win:
    print(f'won: {player_position[0]} {player_position[1]}')
else:
    print(f'dead: {player_position_row} {player_position_col}')
