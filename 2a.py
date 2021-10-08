friends = input().split(', ')
commands = input()


while not commands == 'Report':
    commands = commands.split()
    command = commands[0]
    if command == 'Blacklist':
        friend_name = commands[1]
        if friend_name in friends:
            print(f'{friend_name} was blacklisted.')
            a = friends.index(friend_name)
            friends[a] = 'Blacklisted'
        else:
            print(f'{friend_name} was not found.')
    elif command == 'Error':
        index = int(commands[1])
        if 0 <= index < len(friends):
            if not friends[index] == 'Blacklisted' and not friends[index] == 'Lost':
                print(f'{friends[index]} was lost due to an error.')
                friends[index] = 'Lost'
    elif command == 'Change':
        index = int(commands[1])
        new_name = commands[2]
        if 0 <= index < len(friends):
            print(f'{friends[index]} changed his username to {new_name}.')
            friends[index] = new_name
    commands = input()

print(f"Blacklisted names: {friends.count('Blacklisted')}")
print(f"Lost names: {friends.count('Lost')}")
print(' '.join(friends))
