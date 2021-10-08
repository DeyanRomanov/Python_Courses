def blacklisted(friend, name):
    if name not in friend:
        print(f'{name} was not found.')
        return friend
    print(f'{name} was blacklisted.')
    a = friend.index(name)
    friend[a] = 'Blacklisted'
    return friend


def valid_index(friend, index_to_check):
    if 0 <= index_to_check < len(friend):
        return True
    return False


def errors(friend, index_of_friend):
    if valid_index(friend, index_of_friend):
        if not friends[index] == 'Blacklisted' and not friends[index] == 'Lost':
            print(f'{friend[index_of_friend]} was lost due to an error.')
            friend[index_of_friend] = 'Lost'
    return friend


def changing(friend, index_of_friend, new_friend):
    if valid_index(friend, index_of_friend):
        print(f'{friend[index_of_friend]} changed his username to {new_friend}.')
        friend[index_of_friend] = new_friend
        return friend
    return friend


friends = input().split(', ')
commands = input()

while not commands == 'Report':
    commands = commands.split()
    command = commands[0]
    if command == 'Blacklist':
        friend_name = commands[1]
        friends = blacklisted(friends, friend_name)
    elif command == 'Error':
        index = int(commands[1])
        friends = errors(friends, index)
    elif command == 'Change':
        index = int(commands[1])
        new_name = commands[2]
        friends = changing(friends, index, new_name)
    commands = input()

print(f"Blacklisted names: {friends.count('Blacklisted')}")
print(f"Lost names: {friends.count('Lost')}")
print(' '.join(friends))
