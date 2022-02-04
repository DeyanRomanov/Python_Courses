first_line = input().split()
second_line = input().split()
three_line = input().split()

first_player_win = False
second_player_win = False

if first_line[0] == '1' and first_line[1] == '1' and first_line[2] == '1':
    first_player_win = True
elif first_line[0] == '2' and first_line[1] == '2' and first_line[2] == '2':
    second_player_win = True

if second_line[0] == '1' and second_line[1] == '1' and second_line[2] == '1':
    first_player_win = True
elif second_line[0] == '2' and second_line[1] == '2' and second_line[2] == '2':
    second_player_win = True

if three_line[0] == '1' and three_line[1] == '1' and three_line[2] == '1':
    first_player_win = True
elif three_line[0] == '2' and three_line[1] == '2' and three_line[2] == '2':
    second_player_win = True

if first_line[0] == '1' and second_line[0] == '1' and three_line[0] == '1':
    first_player_win = True
elif first_line[0] == '2' and second_line[0] == '2' and three_line[0] == '2':
    second_player_win = True

if first_line[1] == '1' and second_line[1] == '1' and three_line[1] == '1':
    first_player_win = True
elif first_line[1] == '2' and second_line[1] == '2' and three_line[1] == '2':
    second_player_win = True

if first_line[2] == '1' and second_line[2] == '1' and three_line[2] == '1':
    first_player_win = True
elif first_line[2] == '2' and second_line[2] == '2' and three_line[2] == '2':
    second_player_win = True

if first_line[0] == '1' and second_line[1] == '1' and three_line[2] == '1':
    first_player_win = True
elif first_line[0] == '2' and second_line[1] == '2' and three_line[2] == '2':
    second_player_win = True

if first_line[2] == '1' and second_line[1] == '1' and three_line[0] == '1':
    first_player_win = True
elif first_line[2] == '2' and second_line[1] == '2' and three_line[0] == '2':
    second_player_win = True

if first_player_win:
    print('First player won')
elif second_player_win:
    print('Second player won')
else:
    print('Draw!')
