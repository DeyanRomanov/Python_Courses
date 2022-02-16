def is_inside(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board):
        return True
    return False


def knight_conflict(board, r, c, knight):
    if is_inside(board, r - 2, c + 1) and matrix[row - 2][col + 1] == 'K':
        knight += 1
    if is_inside(board, r - 2, c - 1) and matrix[row - 2][col - 1] == 'K':
        knight += 1
    if is_inside(board, r - 1, c - 2) and matrix[row - 1][col - 2] == 'K':
        knight += 1
    if is_inside(board, r - 1, c + 2) and matrix[row - 1][col + 2] == 'K':
        knight += 1
    if is_inside(board, r + 1, c - 2) and matrix[row + 1][col - 2] == 'K':
        knight += 1
    if is_inside(board, r + 1, c + 2) and matrix[row + 1][col + 2] == 'K':
        knight += 1
    if is_inside(board, r + 2, c + 1) and matrix[row + 2][col + 1] == 'K':
        knight += 1
    if is_inside(board, r + 2, c - 1) and matrix[row + 2][col - 1] == 'K':
        knight += 1
    return knight


size = int(input())

matrix = []

for _ in range(size):
    matrix.append(list(input()))

knight_conflict_list = []
removed = 0

while True:
    knight_conflict_list.clear()
    max_conflict = float('-inf')

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            knight_conflicts = 0
            if matrix[row][col] == 'K':
                knight_conflicts += knight_conflict(matrix, row, col, knight_conflicts)
                if knight_conflicts > 0:
                    row_position, col_position = row, col
                    knight_conflict_list.append([row_position, col_position, knight_conflicts])
    if knight_conflict_list:
        index_to_remove = 0
        for index in range(len(knight_conflict_list)):
            if knight_conflict_list[index][2] > max_conflict:
                max_conflict = knight_conflict_list[index][2]
                index_to_remove = index
        matrix[knight_conflict_list[index_to_remove][0]][knight_conflict_list[index_to_remove][1]] = 0
        knight_conflict_list.remove(knight_conflict_list[index_to_remove])
        removed += 1
    else:
        break

print(removed)
