if __name__ == '__main__':
    list_for_manipulation = []
    for operations in range(int(input())):
        commands = input().split()
        command = commands[0]
        if command == 'insert':
            index = int(commands[1])
            number = int(commands[2])
            list_for_manipulation.insert(index, number)
        elif command == 'print':
            print(list_for_manipulation)
        elif command == "remove":
            list_for_manipulation.remove(int(commands[1]))
        elif command == 'append':
            list_for_manipulation.append(int(commands[1]))
        elif command == 'sort':
            list_for_manipulation = sorted(list_for_manipulation, reverse=False)
        elif command == 'pop':
            list_for_manipulation.pop()
        elif command == 'reverse':
            list_for_manipulation = list_for_manipulation[::-1]
