encrypted_message = input()
commands = input()

while not commands == 'Decode':
    commands = commands.split('|')
    command = commands[0]
    if command == 'Move':
        number_of_letter = int(commands[1])
        encrypted_message = encrypted_message[number_of_letter:] + encrypted_message[:number_of_letter]
    elif command == 'Insert':
        index = int(commands[1])
        letter = commands[2]
        encrypted_message = encrypted_message[:index] + letter + encrypted_message[index:]
    elif command == 'ChangeAll':
        old_letter = commands[1]
        new_letter = commands[2]
        encrypted_message = encrypted_message.replace(old_letter, new_letter)
    commands = input()

print(f"The decrypted message is: {encrypted_message}")
