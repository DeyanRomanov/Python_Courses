import math


def is_inside(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board):
        return True
    return False


player_one, player_two = input().split(', ')
dartboard = [input().split() for x in range(7)]
player_one_points = 501
player_two_points = 501
turns = 0
while True:
    points = 0
    turns += 1
    row_col = input()
    row_col = row_col[1:-1]
    row, col = row_col.split(', ')
    row, col = int(row), int(col)
    if not is_inside(dartboard, row, col):
        continue
    if dartboard[row][col] == 'B':
        if turns % 2 == 0:
            print(f"{player_two} won the game with {turns // 2} throws!")
        else:
            print(f"{player_one} won the game with {math.ceil(turns / 2)} throws!")
        break
    if dartboard[row][col].isnumeric():
        points = int(dartboard[row][col])
    elif dartboard[row][col] == 'D':
        points = (int(dartboard[0][col]) + int(dartboard[-1][col]) +
                  int(dartboard[row][0]) + int(dartboard[row][-1])) * 2
    elif dartboard[row][col] == 'T':
        points = (int(dartboard[0][col]) + int(dartboard[-1][col]) +
                  int(dartboard[row][0]) + int(dartboard[row][-1])) * 3
    if not turns % 2 == 0:
        player_one_points -= points
        if player_one_points <= 0:
            print(f"{player_one} won the game with {math.ceil(turns / 2)} throws!")
            break
    else:
        player_two_points -= points
        if player_two_points <= 0:
            print(f"{player_two} won the game with {turns // 2} throws!")
            break
