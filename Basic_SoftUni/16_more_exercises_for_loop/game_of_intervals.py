players = int(input())
result = 0
points = 0
total_turns = 0
percent_to_nine = 0
percent_to_nineteen = 0
percent_to_twentynine = 0
percent_to_thirthynine = 0
percent_to_fivty = 0
percent_to_invalid = 0

for x in range(players):
    turn = int(input())
    total_turns += 1
    if turn < 0 or turn > 50:
        percent_to_invalid += 1
        result /= 2
    elif 0 <= turn <= 9:
        points = turn * 0.2
        percent_to_nine += 1
        result += points
    elif 10 <= turn <= 19:
        percent_to_nineteen += 1
        points = turn * 0.3
        result += points
    elif 20 <= turn <= 29:
        percent_to_twentynine += 1
        points = turn * 0.4
        result += points
    elif 30 <= turn <= 39:
        percent_to_thirthynine += 1
        points = 50
        result += points
    elif 40 <= turn <= 50:
        percent_to_fivty += 1
        points = 100
        result += points

turn_to_nine = percent_to_nine / total_turns * 100
turn_to_nineteen = percent_to_nineteen / total_turns * 100
turn_to_twentynine = percent_to_twentynine / total_turns * 100
turn_to_thirthynine = percent_to_thirthynine / total_turns * 100
turn_to_fivty = percent_to_fivty / total_turns * 100
turn_to_invalid = percent_to_invalid / total_turns * 100

print(f'{result:.2f}')
print(f'From 0 to 9: {turn_to_nine:.2f}%')
print(f"From 10 to 19: {turn_to_nineteen:.2f}%")
print(f"From 20 to 29: {turn_to_twentynine:.2f}%")
print(f"From 30 to 39: {turn_to_thirthynine:.2f}%")
print(f"From 40 to 50: {turn_to_fivty:.2f}%")
print(f"Invalid numbers: {turn_to_invalid:.2f}%")
