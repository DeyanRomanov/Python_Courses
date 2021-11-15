def is_win(player):
    if player["score"] <= 0:
        return True
    return False


def take_corresponding_numbers(game_board, rows, cols):
    return game_board[rows][0] + game_board[rows][-1] + game_board[0][cols] + game_board[-1][cols]


def hit(coordinates):
    rows, cols = coordinates[1:-1].split(', ')
    return int(rows), int(cols)


def gamers(player_1, player_2, score):
    current_player = {"name": player_1,
                      "score": score,
                      'turns': 0
                      }
    other_player = {"name": player_2,
                    "score": score,
                    "turns": 0
                    }
    return current_player, other_player


def is_inside(board, rows, cols):
    if 0 <= rows < len(board) and 0 <= cols < len(board):
        return True
    return False


def play(board, score):
    current_player, other_player = gamers(player_one, player_two, score)
    while True:
        row, col = hit(input())
        current_player["turns"] += 1
        if not is_inside(board, row, col):
            current_player, other_player = other_player, current_player
            continue
        throw = board[row][col]
        if throw == "B":
            current_player["score"] = 0
            break
        elif isinstance(throw, int):
            point = throw
            current_player["score"] -= point
        elif throw == "D":
            point = take_corresponding_numbers(board, row, col)
            current_player["score"] -= point * 2
        elif throw == 'T':
            point = take_corresponding_numbers(board, row, col)
            current_player["score"] -= point * 3
        if is_win(current_player):
            break
        current_player, other_player = other_player, current_player
    return f"{current_player['name']} won the game with {current_player['turns']} throws!"


player_one, player_two = input().split(', ')
dartboard_rows = 7
dartboard = []
for row in range(dartboard_rows):
    column = []
    for col in input().split():
        if col.isnumeric():
            col = int(col)
        column.append(col)
    dartboard.append(column)
final_score = 501

print(play(dartboard, final_score))
