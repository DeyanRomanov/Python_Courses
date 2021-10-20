number_of_pieces = int(input())

pieces_dict = {}
for piece in range(number_of_pieces):
    pieces, composer, key = input().split('|')
    pieces_dict[pieces] = {composer: key}

commands = input()

while not commands == 'Stop':
    commands = commands.split('|')
    command = commands[0]
    if command == "Add":
        pieces, composer, key = commands[1], commands[2], commands[3]
        if pieces not in pieces_dict:
            print(f"{pieces} by {composer} in {key} added to the collection!")
            pieces_dict[pieces] = {composer: key}
        else:
            print(f"{pieces} is already in the collection!")
    elif command == 'Remove':
        pieces = commands[1]
        if pieces in pieces_dict:
            print(f"Successfully removed {pieces}!")
            del pieces_dict[pieces]
        else:
            print(f"Invalid operation! {pieces} does not exist in the collection.")
    elif command == 'ChangeKey':
        pieces, new_key = commands[1], commands[2]
        if pieces not in pieces_dict:
            print(f"Invalid operation! {pieces} does not exist in the collection.")
        else:
            print(f"Changed the key of {pieces} to {new_key}!")
            for k, v in pieces_dict[pieces].items():
                pieces_dict[pieces][k] = new_key
    commands = input()

for key, value in sorted(pieces_dict.items(), key=lambda x: (x[0], x[1])):
    for k, v in value.items():
        print(f"{key} -> Composer: {k}, Key: {v}")
