def shoot_manipulation(indx, power, targets_list):
    if 0 <= indx < len(targets_list):
        if targets_list[indx] - power <= 0:
            targets_list.pop(indx)
        else:
            targets_list[indx] -= power
    return targets_list


def add_manipulation(indx, value, targets_list):
    if 0 <= indx < len(targets_list):
        targets_list.insert(indx, value)
        return targets_list
    return print("Invalid placement!")


def strike_manipulation(indx, radius, targets_list):
    if indx + radius < len(targets_list) and indx - radius >= 0:
        for r in range(indx - radius, radius + indx + 1):
            targets_list.pop(indx - radius)
        return targets_list
    return print("Strike missed!")


targets = [int(num) for num in input().split()]
command = input()

while not command == 'End':
    command = command.split()
    manipulation = command[0]
    index = int(command[1])
    last_number = int(command[-1])
    if manipulation == 'Shoot':
        shoot_manipulation(index, last_number, targets)
    elif manipulation == 'Add':
        add_manipulation(index, last_number, targets)
    elif manipulation == 'Strike':
        strike_manipulation(index, last_number, targets)
    command = input()


print('|'.join([str(num) for num in targets]))
