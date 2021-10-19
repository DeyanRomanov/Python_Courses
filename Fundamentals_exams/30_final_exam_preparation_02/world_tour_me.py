world_tour = input()

commands = input()

while not commands == 'Travel':
    if ' ' in commands:
        commands = commands.split()
    else:
        commands = commands.split(':')
    command = commands[0]
    if command == 'Add':
        stop, index, string = commands[1].split(':')
        if 0 <= int(index) < len(world_tour):
            world_tour = world_tour[:int(index)] + string + world_tour[int(index):]
        print(world_tour)
    elif command == 'Remove':
        stop, start_index, end_index = commands[1].split(':')
        start_index = int(start_index)
        end_index = int(end_index)
        if 0 <= start_index < len(world_tour) and 0 <= end_index < len(world_tour):
            world_tour = world_tour[:start_index] + world_tour[end_index + 1:]
        print(world_tour)
    elif command == 'Switch':
        old_string, new_string = commands[1], commands[2]
        if old_string in world_tour:
            world_tour = world_tour.replace(old_string, new_string)
        print(world_tour)
    commands = input()

print(f"Ready for world tour! Planned stops: {world_tour}")
