commands = input()
message = []
while not commands == 'end':
    commands = commands.split()
    command = commands[0]
    if command == 'Chat':
        message.append(commands[1])
    elif command == 'Delete':
        if commands[1] in message:
            message.remove(commands[1])
    elif command == 'Edit':
        message_to_edit = commands[1]
        new_message = commands[2]
        if message_to_edit in message:
            index = message.index(message_to_edit)
            message[index], new_message = new_message, message[index]
    elif command == 'Pin':
        message_to_pin = commands[1]
        if message_to_pin in message:
            message.remove(message_to_pin)
            message.append(message_to_pin)
    elif command == 'Spam':
        spams = commands[1::]
        message.extend(spams)
    commands = input()

for x in message:
    print(x)