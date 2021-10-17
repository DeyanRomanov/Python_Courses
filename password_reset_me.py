secret_password = input()
commands = input()

while not commands == 'Done':
    if commands == 'TakeOdd':
        new_password = ''
        for index in range(len(secret_password)):
            if not index % 2 == 0:
                new_password += secret_password[index]
        secret_password = new_password
        print(secret_password)
    else:
        commands = commands.split()
        command = commands[0]
        if command == 'Cut':
            start_index = int(commands[1])
            lenghts = int(commands[2])
            secret_password = secret_password[:start_index] + secret_password[start_index + lenghts:]
            print(secret_password)
        elif command == 'Substitute':
            substring = commands[1]
            substitute = commands[2]
            new_password = ''
            if substring in secret_password:
                secret_password = secret_password.replace(substring, substitute)
                print(secret_password)
            else:
                print("Nothing to replace!")
    commands = input()

print(f"Your password is: {secret_password}")
