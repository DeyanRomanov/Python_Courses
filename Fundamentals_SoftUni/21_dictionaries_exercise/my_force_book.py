command = input()

force_book = {}

while not command == 'Lumpawaroo':
    if '|' in command:
        side_force, user_force = command.split(' | ')
        is_There = False
        for key, value in force_book.items():
            if user_force in value:
                is_There = True
        if side_force not in force_book and not is_There:
            force_book[side_force] = [user_force]
        elif not is_There:
            force_book[side_force].append(user_force)

    elif '-' in command:
        user_force, side_force = command.split(' -> ')
        is_There = False
        for key, value in force_book.items():
            if user_force in value:
                is_There = True
        if not is_There:
            if side_force not in force_book:
                force_book[side_force] = [user_force]
                print(f"{user_force} joins the {side_force} side!")
            else:
                force_book[side_force].append(user_force)
                print(f"{user_force} joins the {side_force} side!")
        else:
            for key, value in force_book.items():
                if user_force in force_book[key]:
                    force_book[key].remove(user_force)
            if side_force not in force_book:
                force_book[side_force] = []
            force_book[side_force].append(user_force)
            print(f"{user_force} joins the {side_force} side!")
    command = input()

for key, value in sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0])):
    if len(force_book[key]) > 0:
        print(f'Side: {key}, Members: {len(value)}')
        for name in sorted(value):
            print(f'! {name}')
