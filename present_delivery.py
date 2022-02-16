def is_inside(matrix, r, c):
    if 0 <= r < len(matrix) or 0 <= c < len(matrix):
        return True
    return False


def cookies(r, c, houses):
    houses.append([r + 1, c])
    houses.append([r - 1, c])
    houses.append([r, c + 1])
    houses.append([r, c - 1])
    return houses


presents = int(input())

neighborhood = []
santa_row = 0
santa_col = 0
all_nice_kids = 0
houses_whit_kids = []

for row in range(int(input())):
    neighborhood.append(input().split())
    for col in range(len(neighborhood[0])):
        if neighborhood[row][col] == 'S':
            santa_row = row
            santa_col = col
        elif neighborhood[row][col] == 'V':
            all_nice_kids += 1

total_nice_kids = all_nice_kids

side_dictionary = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

command = input()

while not command == 'Christmas morning':
    santa_row_next, santa_col_next = santa_row, santa_col
    santa_row_next, santa_col_next = side_dictionary[command](santa_row_next, santa_col_next)
    neighborhood[santa_row][santa_col] = '-'
    if is_inside(neighborhood, santa_row_next, santa_col_next):
        if neighborhood[santa_row_next][santa_col_next] == 'V':
            neighborhood[santa_row_next][santa_col_next] = 'S'
            all_nice_kids -= 1
            presents -= 1
            if all_nice_kids == 0 or presents == 0:
                break
        elif neighborhood[santa_row_next][santa_col_next] == 'C':
            houses_whit_kids = cookies(santa_row_next, santa_col_next, houses_whit_kids)
            neighborhood[santa_row_next][santa_col_next] = 'S'
            for row, col in houses_whit_kids:
                if neighborhood[row][col] == 'V':
                    neighborhood[row][col] = '-'
                    all_nice_kids -= 1
                    presents -= 1
                    if all_nice_kids == 0 or presents == 0:
                        break
                elif neighborhood[row][col] == 'X':
                    neighborhood[row][col] = '-'
                    presents -= 1
                    if presents == 0:
                        break
        neighborhood[santa_row_next][santa_col_next] = 'S'
        santa_row, santa_col = santa_row_next, santa_col_next
        if all_nice_kids == 0 or presents == 0:
            break
    command = input()

if presents == 0 and all_nice_kids > 0:
    print('Santa ran out of presents!')
for row in neighborhood:
    print(' '.join(row))
if all_nice_kids > 0:
    print(f"No presents for {all_nice_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")

