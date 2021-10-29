def valid(first_index, second_index, third_index, fourth_index, r, c):
    if 0 <= first_index < r and 0 <= second_index < c and 0 <= third_index < r and 0 <= fourth_index < c:
        return True
    else:
        return False


rows, columns = [int(x) for x in input().split()]

matrix = []
for row in range(rows):
    matrix.append([x for x in input().split()])

commands = input()

while not commands == 'END':
    is_valid = True
    commands = commands.split()
    if not commands[0] == 'swap' or not len(commands) == 5:
        is_valid = False
    else:
        commands.pop(0)
        first, second, third, fourth = commands[0], commands[1], commands[2], commands[3]
        if first.isnumeric() and second.isnumeric() and third.isnumeric() and fourth.isnumeric():
            if valid(int(first), int(second), int(third), int(fourth), rows, columns):
                matrix[int(first)][int(second)], matrix[int(third)][int(fourth)] = \
                    matrix[int(third)][int(fourth)], matrix[int(first)][int(second)]
                for row in matrix:
                    print(' '.join(row))
            else:
                is_valid = False
        else:
            is_valid = False
    if not is_valid:
        print('Invalid input!')

    commands = input()
