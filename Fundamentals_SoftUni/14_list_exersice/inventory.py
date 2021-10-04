def collect_command(item_to_collect, items_list):
    if item_to_collect not in items_list:
        items_list.append(item_to_collect)
    return item_to_collect


def drop_command(item_to_drop, items_list):
    if item_to_drop in items_list:
        items_list.remove(item_to_drop)
    return item_to_drop


def renew_command(item_to_renew, items_list):
    for index in range(len(items_list)):
        if items_list[index] == item_to_renew:
            items_list.pop(index)
            items_list.append(item_to_renew)
    return items_list


def combine_command(item_to_combine, items_list):
    item_to_combine = item_to_combine.split(':')
    old_item = item_to_combine[0]
    new_item = item_to_combine[1]
    for index in range(len(items_list)):
        if items_list[index] == old_item:
            items_list.insert(index + 1, new_item)
    return items_list


collecting_items = input().split(', ')
command = input()

while not command == 'Craft!':
    command = command.split(' - ')
    task = command[0]
    item = command[-1]
    if task == 'Collect':
        collect_command(item, collecting_items)
    elif task == 'Drop':
        drop_command(item, collecting_items)
    elif task == 'Combine Items':
        combine_command(item, collecting_items)
    elif task == 'Renew':
        renew_command(item, collecting_items)
    command = input()

print(', '.join(collecting_items))
