def loot_command(treasure, items):
    for item in items:
        if item not in treasure:
            treasure.insert(0, item)
    return treasure


def drop_command(treasure, index):
    if 0 <= index < len(treasure):
        a = treasure.pop(index)
        treasure.append(a)
    return treasure


def steal_command(treasure, count):
    count *= -1
    steal_treasure = treasure[count::]
    print(', '.join(steal_treasure))
    return treasure[:count]


treasure_chest = input().split('|')
commands = input()

while not commands == "Yohoho!":
    commands = commands.split()
    command = commands[0]
    if command == 'Loot':
        commands.pop(0)
        treasure_chest = loot_command(treasure_chest, commands)
    elif command == 'Drop':
        indx = int(commands[1])
        treasure_chest = drop_command(treasure_chest, indx)
    elif command == 'Steal':
        counter = int(commands[1])
        treasure_chest = steal_command(treasure_chest, counter)
    commands = input()

if len(treasure_chest) > 0:
    divide = len(treasure_chest)
    all_treasure = 0
    for treasure in treasure_chest:
        all_treasure += len(treasure)
    average = all_treasure / divide
    print(f"Average treasure gain: {average:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
