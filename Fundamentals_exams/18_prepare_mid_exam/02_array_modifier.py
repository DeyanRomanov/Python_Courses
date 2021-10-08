def swaping(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]
    return array


def multiplying(array, index1, index2):
    array[index1] = array[index1] * array[index2]
    return array


def decreaseing(array):
    new_aray = []
    for num in array:
        num -= 1
        new_aray.append(num)
    return new_aray


integers_array = [int(num) for num in input().split()]
commands = input()

while not commands == 'end':
    commands = commands.split()
    command = commands[0]
    if command == 'swap':
        index_1, index_2 = int(commands[1]), int(commands[2])
        integers_array = swaping(integers_array, index_1, index_2)
    elif command == 'multiply':
        index_1, index_2 = int(commands[1]), int(commands[2])
        integers_array = multiplying(integers_array, index_1, index_2)
    elif command == 'decrease':
        integers_array = decreaseing(integers_array)
    commands = input()

integers_array = [str(num) for num in integers_array]
print(', '.join(integers_array))
