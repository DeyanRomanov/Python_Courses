def is_inside(matrix, r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False


def shooting(matrix, direct, r, c, s):
    while is_inside(matrix, r, c) and not matrix[r][c] == 'x':
        r, c = moving_dictionary[direct](r, c, s)
        if is_inside(matrix, r, c):
            if matrix[r][c] == 'x':
                target_positions.append([r, c])
                matrix[r][c] = '.'
                break
        else:
            break
    return target_positions


my_position = []
shotgun_range = []
target_positions = []
all_targets = 0

for row in range(5):
    shotgun_range.append(input().split())
    for col in range(5):
        if shotgun_range[row][col] == 'A':
            my_position = [row, col]
        elif shotgun_range[row][col] == 'x':
            all_targets += 1

number_of_commands = int(input())
moving_dictionary = {
    'right': lambda r, c, s: (r, c + s),
    'left': lambda r, c, s: (r, c - s),
    'up': lambda r, c, s: (r - s, c),
    'down': lambda r, c, s: (r + s, c)
}

for _ in range(number_of_commands):
    commands = input().split()
    command = commands[0]
    if command == 'move':
        direction, steps = commands[1], int(commands[2])
        my_position_row, my_position_col = my_position
        my_position_row_next, my_position_col_next = moving_dictionary[direction](my_position_row, my_position_col, steps)
        if is_inside(shotgun_range, my_position_row_next, my_position_col_next) and \
                not shotgun_range[my_position_row_next][my_position_col_next] == 'x':
                shotgun_range[my_position_row_next][my_position_col_next] = 'A'
                my_position = [my_position_row_next, my_position_col_next]
                shotgun_range[my_position_row][my_position_col] = "."
        else:
            my_position = [my_position_row, my_position_col]
    elif command == 'shoot':
        direction = commands[1]
        my_position_row, my_position_col = my_position
        target_positions = shooting(shotgun_range, direction, my_position_row, my_position_col, 1)
    if len(target_positions) == all_targets:
        print(f"Training completed! All {all_targets} targets hit.")
        for targets in target_positions:
            print(targets)
        break

if not len(target_positions) == all_targets:
    print(f"Training not completed! {all_targets - len(target_positions)} targets left.")
    for targets in target_positions:
        print(targets)
