def range_exist(target: list, indx):
    if indx in range(len(target)):
        return True
    return False


def shooting(target, indx, power):
    if target[indx] <= power:
        target.pop(indx)
        return target
    target[indx] -= power
    return target


def add_targets(target, indx, power):
    target.insert(index, power)
    return target

def strike_shot(target, indx, power):
    if indx + power >= len(target) or indx < power: # here may be have mistake
        print("Strike missed!")
    else:
        target = target[:indx - power] + target[indx + power + 1:]
    return target


targets = [int(target) for target in input().split()]
manipulating = input()

while not manipulating == 'End':
    command, index, value = manipulating.split()
    index = int(index)
    value = int(value)
    if command == 'Shoot':
        if range_exist(targets, index):
            targets = shooting(targets, index, value)
    elif command == 'Add':
        if range_exist(targets, index):
            targets = add_targets(targets, index, value)
        else:
            print(f"Invalid placement!")
    elif command == 'Strike':
        targets = strike_shot(targets, index, value)
    manipulating = input()

targets = [str(target) for target in targets]
print('|'.join(targets))
