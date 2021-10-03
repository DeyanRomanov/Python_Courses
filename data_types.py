def change_type(command, num):
    result = 0
    if command == 'int':
        result = int(num) * 2
    elif command == 'real':
        result = float(num) * 1.5
        result = f'{result:.2f}'
    elif command == 'string':
        result = '$' + num + '$'
    return result


task = input()
number = input()

print(change_type(task, number))
