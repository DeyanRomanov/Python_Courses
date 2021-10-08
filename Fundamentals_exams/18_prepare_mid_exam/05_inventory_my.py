def combine_items(journal, items):
    items = items.split(':')
    old = items[0]
    new = items[1]
    for itm in range(len(journal)):
        if journal[itm] == old:
            journal.insert(itm + 1, new)
    return journal


def renew_items(journal, items):
    for itm in range(len(journal)):
        if journal[itm] == items:
            journal.pop(itm)
            journal.append(items)
    return journal


journal_collect = input().split(', ')
commands = input()

while not commands == 'Craft!':
    commands = commands.split(' - ')
    command, item = commands[0], commands[1]
    if command == 'Collect':
        if item not in journal_collect:
            journal_collect.append(item)
    elif command == 'Drop':
        if item in journal_collect:
            journal_collect.remove(item)
    elif command == 'Combine Items':
        journal_collect = combine_items(journal_collect, item)
    elif command == 'Renew':
        journal_collect = renew_items(journal_collect, item)
    commands = input()

print(', '.join(journal_collect))
