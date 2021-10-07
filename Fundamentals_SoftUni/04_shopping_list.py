def urgent_command(initials, item):
    if item not in initials:
        initials.insert(0, item)
    return initials


def unnecessary_command(initials, item):
    if item in initials:
        initials.remove(item)
    return initials


def correction(initials, old, new):
    for index in range(len(initials)):
        if initials[index] == old:
            initials[index] = new
    return initials


def rearrangle_command(initials, item):
    for index in range(len(initials)):
        if initials[index] == item:
            initials.pop(index)
            initials.append(item)
            break
    return initials


initial_list = input().split('!')
commands = input()

while not commands == "Go Shopping!":
    commands = commands.split()
    command = commands[0]
    product = commands[1]
    if command == 'Urgent':
        initial_list = urgent_command(initial_list, product)
    elif command == 'Unnecessary':
        initial_list = unnecessary_command(initial_list, product)
    elif command == 'Correct':
        new_product_per_correct = commands[2]
        initial_list = correction(initial_list, product, new_product_per_correct)
    elif command == 'Rearrange':
        initial_list = rearrangle_command(initial_list, product)
    commands = input()

print(', '.join(initial_list))
