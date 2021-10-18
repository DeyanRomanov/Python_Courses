concealed_message = input()
instructions = input()

while not instructions == 'Reveal':
    instructions = instructions.split(':|:')
    command = instructions[0]
    if command == 'InsertSpace':
        index = int(instructions[1])
        concealed_message = concealed_message[:index] + ' ' + concealed_message[index:]
        print(concealed_message)
    elif command == 'Reverse':
        substring = instructions[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            concealed_message += substring[::-1]
            print(concealed_message)
        else:
            print('error')
    elif command == 'ChangeAll':
        substring = instructions[1]
        new_letter = instructions[2]
        while substring in concealed_message:
            concealed_message = concealed_message.replace(substring, new_letter)
        print(concealed_message)
    instructions = input()

print(f"You have a new text message: {concealed_message}")
