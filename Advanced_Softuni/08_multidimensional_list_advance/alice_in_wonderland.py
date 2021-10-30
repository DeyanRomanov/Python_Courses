def is_inside_or_hole(matrix, r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False


size = int(input())

field = []
alice_position = 0
rabbit_hole_position = 0
tea = 0

direction_dictionary = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1)
}

for row in range(size):
    field.append(input().split())
    for column in range(size):
        if field[row][column] == 'A':
            alice_position = [row, column]
        elif field[row][column] == 'R':
            rabbit_hole_position = [row, column]
command = input()
while command:
    alice_row, alice_col = alice_position
    field[alice_row][alice_col] = '*'
    alice_row, alice_col = direction_dictionary[command](alice_row, alice_col)
    if is_inside_or_hole(field, alice_row, alice_col):
        alice_position = [alice_row, alice_col]
        if field[alice_row][alice_col] == 'R':
            field[alice_row][alice_col] = '*'
            print("Alice didn't make it to the tea party.")
            break
        elif field[alice_row][alice_col].isdigit():
            tea += int(field[alice_row][alice_col])
            field[alice_row][alice_col] = "*"
            if tea >= 10:
                print("She did it! She went to the party.")
                break
    else:
        print("Alice didn't make it to the tea party.")
        break
    command = input()

for rows in field:
    print(' '.join(rows))
