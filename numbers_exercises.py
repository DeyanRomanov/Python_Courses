def add_number(list, set):
    for num in list:
        set.add(num)
    return set


def remove_number(list, set):
    for num in list:
        if num in set:
            set.remove(num)
    return set


first_sequence = set([int(num) for num in input().split()])
second_sequence = set([int(num) for num in input().split()])
number_of_commands = int(input())

for commands in range(number_of_commands):
    command = input()
    if command.startswith('Add First '):
        command = command.replace('Add First ', '')
        numbers = [int(num) for num in command.split()]
        first_sequence = add_number(numbers, first_sequence)
    elif command.startswith('Add Second '):
        command = command.replace('Add Second ', '')
        numbers = [int(num) for num in command.split()]
        second_sequence = add_number(numbers, second_sequence)
    elif command.startswith('Remove First '):
        command = command.replace('Remove First ', '')
        numbers = [int(num) for num in command.split()]
        first_sequence = remove_number(numbers, first_sequence)
    elif command.startswith('Remove Second '):
        command = command.replace('Remove Second ', '')
        numbers = [int(num) for num in command.split()]
        second_sequence = remove_number(numbers, second_sequence)
    else:
        if not first_sequence.issubset(second_sequence) and not second_sequence.issubset(first_sequence):
            print('False')
        else:
            print('True')

first_list = sorted([num for num in first_sequence])
second_list = sorted([num for num in second_sequence])
print(', '.join(str(num) for num in first_list))
print(', '.join(str(num) for num in second_list))
