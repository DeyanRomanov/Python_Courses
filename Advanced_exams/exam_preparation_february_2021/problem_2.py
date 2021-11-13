import math


def is_inside(rows, cols, matrix):
    if 0 <= rows < len(matrix) and 0 <= cols < len(matrix):
        return True
    return False


def make_matrix(size):
    matrix = []
    walls_in_field = []
    one_player_position = ''
    for row in range(size):
        matrix.append(input().split())
        for col in range(size):
            if matrix[row][col] == 'P':
                one_player_position = [row, col]
            elif matrix[row][col] == 'X':
                walls_in_field.append((row, col))
            else:
                matrix[row][col] = int(matrix[row][col])
    return matrix, one_player_position, walls_in_field


field, player_position, walls = make_matrix(int(input()))
player_path = []
points = 0
is_win = False
movement = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1)
}

while True:
    commands = input()
    if commands not in movement:
        continue
    player_position = movement[commands](player_position[0], player_position[1])
    if is_inside(player_position[0], player_position[1], field)\
            and not field[player_position[0]][player_position[1]] == 'X':
        player_path.append([*player_position])
        points += field[player_position[0]][player_position[1]]
        if points >= 100:
            is_win = True
            break
    else:
        points /= 2
        points = math.floor(points)
        break
if is_win:
    print(f"You won! You've collected {points} coins.")
else:
    print(f"Game over! You've collected {points} coins.")
print('Your path:')
for path in player_path:
    print(path)
