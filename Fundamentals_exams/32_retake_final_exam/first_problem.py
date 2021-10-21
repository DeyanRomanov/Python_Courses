user_mail = input()
commands = input()

while not commands == 'Valid':
    commands = commands.split()
    command = commands[0]
    if command == 'Upper':
        index = int(commands[1])
        user_mail = user_mail[:index] + user_mail[index].upper() + user_mail[index + 1:]
        print(user_mail)
    elif command == 'Lower':
        index = int(commands[1])
        user_mail = user_mail[:index] + user_mail[index].lower() + user_mail[index + 1:]
        print(user_mail)
    elif command == 'Insert':
        index = int(commands[1])
        char = commands[2]
        user_mail = user_mail[:index] + char + user_mail[index:]
        print(user_mail)
    elif command == 'Change':
        char = commands[1]
        if char in user_mail:
            index = int(commands[2])
            new_char = ord(char) + index
            user_mail = user_mail.replace(char, chr(new_char))
        print(user_mail)
    elif command == 'Validation':
        is_digit = False
        is_alph_dig = True
        is_lower = True
        is_upper = True
        if len(user_mail) < 6:
            print("Email must be at least 6 characters long!")
        for letter in user_mail:
            if not letter.isalnum() and not letter == '@':
                is_alph_dig = False
                print("Email must consist only of letters, digits and @!")
            if not is_alph_dig:
                break
        for letter in user_mail:
            if not letter.islower():
                is_lower = False
            else:
                is_lower = True
                break
        if not is_lower:
            print("Email must consist at least one lowercase letter!")
        for letter in user_mail:
            if not letter.isupper():
                is_upper = False
            else:
                is_upper = True
                break
        if not is_upper:
            print("Email must consist at least one uppercase letter!")
        for letter in user_mail:
            if letter.isdigit():
                is_digit = True
        if not is_digit:
            print("Email must consist at least one digit!")
    commands = input()
