names = input().split(', ')

names_dict = {}
names_dict = {name: {'items': [], 'costs': 0} for name in names if name not in names_dict}

command = input()

while not command == 'End':
    name, item, cost = command.split('-')
    if item not in names_dict[name]['items']:
        names_dict[name]['items'].append(item)
        names_dict[name]['costs'] += int(cost)
    command = input()

for key, value in names_dict.items():
    print(f"{key} -> Items: {len(set(names_dict[key]['items']))}, Cost: {names_dict[key]['costs']}")
